
from QT_GUI.OfflineAnalysis.CustomWidget.second_layor_analysis_dialog import Ui_Dialog
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import *  # type: ignore
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from Offline_Analysis.Analysis_Functions.Function_Templates.SpecificAnalysisCalculations import SpecificAnalysisFunctions
import seaborn as sns
class Second_Layor_Analysis_Functions(QDialog, Ui_Dialog):

    def __init__(self, database_handler, result_visualizer, parent=None):
        
        super().__init__(parent)
        self.setupUi(self)
 
        self.database_handler = database_handler
        self.cancel.clicked.connect(self.close)
        self.run_second_layer_analysis_function.clicked.connect(self.run_second_layer_analysis)
        
        self.result_visualizer = result_visualizer
        self.offline_tree = self.result_visualizer.offline_tree
        self.series_name = self.offline_tree.SeriesItems.currentItem().parent().data(6,Qt.UserRole)
        analysis_function_tuple = self.database_handler.get_series_specific_analysis_functions(self.series_name)
        self.name_tuple_mapping = {}

        # Replace QComboBox with checkboxes
        self.checkboxes = []  # Keep track of checkboxes
        #self.checkbox_all = QCheckBox("All")
        #self.checkbox_all.setChecked(True)  # Set default state to checked
        #self.checkbox_grid_layout.addWidget(self.checkbox_all)
        #self.checkboxes.append(self.checkbox_all)

        for tuple in analysis_function_tuple:
            checkbox = QCheckBox(f"Analysis: {tuple[1]}, {tuple[0]}")
            self.checkbox_grid_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)
            self.name_tuple_mapping[f"Analysis: {tuple[1]}, {tuple[0]}"] = tuple

        
        self.checkboxes[0].setChecked(True)  # Set default state to checked

    def run_second_layer_analysis(self):
        """This function is called when the user clicks on the run button. It will execute the function selected in the second layer analysis function combobox.
        """
        function_to_execute = self.second_layer_analysis_functions.currentText()
        if function_to_execute == "PCA":
            self.principle_component_analysis()
        if function_to_execute == "IV-Boltzmann Fitting":
           self.make_iv_boltzmann_fitting()
        else:
           print("Not implemented yet")

        # once the function is executed, the offline tab for this specific series only needs to be re-generated
        offline_tab = self.result_visualizer.analysis_function_specific_visualization(self.series_name,self.database_handler.analysis_id)
        # now add the plot to the tree 
        if self.offline_tree.SeriesItems.currentItem().child(0):
            parent_item = self.offline_tree.SeriesItems.currentItem()
        else:
            parent_item = self.offline_tree.SeriesItems.currentItem().parent()

        print(parent_item.text(0))

        """add the results at position 1 of the stacked widget ( position 0  is the analysis config ) """
        self.offline_tree.hierachy_stacked_list[parent_item.data(7, Qt.UserRole)].insertWidget(1,offline_tab)
        analysis_function_tuple = self.database_handler.get_series_specific_analysis_functions(self.offline_tree.SeriesItems.currentItem().parent().data(6,Qt.UserRole))
        analysis_function_tuple = tuple(i[1] for i in analysis_function_tuple)
        self.offline_tree.SeriesItems.currentItem().parent().setData(8, Qt.UserRole,analysis_function_tuple)
        """simulate click on  "Plot" children """
        self.offline_tree.SeriesItems.setCurrentItem(parent_item.child(1))
        #execute the click and all should be done
        self.offline_tree.offline_analysis_result_tree_item_clicked()
        self.close()

    def get_checked_analysis_functions(self):
        checked_items = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        print("Checked Items:", checked_items)
        return checked_items

    def principle_component_analysis(self):
       df_names_to_drop = ['Analysis_ID', 'Function_Analysis_ID', 'Sweep_Table_Name', 'Sweep_Number', 
                            'Duration', 'Increment', 'series_meta_data','analysis_id',
                            'experiment_label','species','genotype','sex','celltype','condition','individuum_id']
      
       # removed on purpose 'Current','Voltage' and 'experiment_name'
       
       analysis_function_list = self.get_checked_analysis_functions()

       if len(analysis_function_list) == 1:
           analysis_function_tuple = self.name_tuple_mapping[analysis_function_list[0]]
           table_name = "results_analysis_function_"+str(analysis_function_tuple[1])+"_"+analysis_function_tuple[0]
           
           plot_dataframe, self.explained_ratio = SpecificAnalysisFunctions.pca_calc([table_name], self.database_handler)
       else:
           concatted_result_table = pd.DataFrame()
           for analysis in analysis_function_list:
               analysis_function_tuple = self.name_tuple_mapping[analysis]
               table_name = "results_analysis_function_"+str(analysis_function_tuple[1])+"_"+analysis_function_tuple[0]
               res_df = self.database_handler.database.execute(f'select * from {table_name}').fetchdf()
              
               reduced_df = res_df.drop(columns=[col for col in res_df.columns if col in df_names_to_drop])
        
               # column result should be renamed in smth like "result_analysis_function_id_100"
               # results must be merged by experiment name 
               
               if concatted_result_table.empty:
                   concatted_result_table = reduced_df
               else:
                   concatted_result_table = pd.merge(concatted_result_table,res_df,on=["experiment_name","Voltage"],how="left")
           concatted_result_table.reset_index()
           plot_dataframe, self.explained_ratio = SpecificAnalysisFunctions.pca_calc("", self.database_handler,concatted_result_table)

       q = """insert into analysis_functions (function_name, analysis_series_name, analysis_id,lower_bound,upper_bound,pgf_segment) values (?,?,?,?,?,?)"""
       self.database_handler.database.execute(q, ("PCA",self.series_name,self.database_handler.analysis_id,-1,-1,-1))

       # get the db id of the inserted fitting
       new_id = self.database_handler.get_last_inserted_analysis_function_id()
       new_table_name = "results_analysis_function_"+str(new_id)+"_PCA"

       # write the results in to the database
       self.database_handler.database.register(new_table_name, plot_dataframe)
       self.database_handler.database.execute(f'CREATE TABLE {new_table_name} AS SELECT * FROM {new_table_name}')

       # and now the link of each experiment name and the sweep table name to analysis id and analysis function id in the results table
       q = """insert into  results values (?,?,?,?) """
    
       for data_table_name in plot_dataframe["Sweep_Table_Name"].values:
           self.database_handler.database.execute(q, (self.database_handler.analysis_id, new_id,data_table_name,new_table_name))

    def make_iv_boltzmann_fitting(self):
       """boltzmann fitting is performed to model voltage-dependent behavior of ion channels and receptors

       """ 
       # get the analysis function and id and the name to query the correct table

       if self.first_layer_analysis_functions.currentText() == "All":
           print("not implemented")
       else:
           analysis_function_tuple = self.name_tuple_mapping[self.first_layer_analysis_functions.currentText()]
       
       table_name = "results_analysis_function_"+str(analysis_function_tuple[1])+"_"+analysis_function_tuple[0]
       result_df = self.database_handler.database.execute(f"select * from {table_name}").fetchdf()


       # insert the fitting analysis
       q = """insert into analysis_functions (function_name, analysis_series_name, analysis_id,lower_bound,upper_bound,pgf_segment) values (?,?,?,?,?,?)"""
       self.database_handler.database.execute(q, ("IV-Boltzmann Fitting",self.series_name,self.database_handler.analysis_id,-1,-1,-1))

       
       # get the db id of the inserted fitting
       new_id = self.database_handler.get_last_inserted_analysis_function_id()
       new_table_name = "results_analysis_function_"+str(new_id)+"_IV-Boltzmann Fitting"

       # make an initial guess:
       initial_guess = [-50,10]
       pos = 0
       for t in result_df["Sweep_Table_Name"].unique():

            tmp = result_df[result_df["Sweep_Table_Name"] == t]
            tmp = tmp.sort_values(by='Voltage', ascending=False)
            
            voltage_steps = tmp["Voltage"].values
            conductance = 1/tmp["Result"].values
            # params[0] = v-half-fit, params[1] = k-fit
            params, params_covariance = curve_fit(self.boltzman_fit, voltage_steps, conductance, p0=initial_guess)

            print(params)
            print(params_covariance)

            # Create a figure and set the title
            voltage_fit = np.linspace(min(voltage_steps),max(voltage_steps), 50)
            current_fit = self.boltzman_fit(voltage_fit, params[0], params[1])
            pos += 1
            plt.subplot(120+pos)
            plt.plot(voltage_fit,current_fit)
            plt.show()
    
    
    def boltzman_fit(self,V,V_half,k):
        return 1/(1+np.exp((V_half-V)/k))