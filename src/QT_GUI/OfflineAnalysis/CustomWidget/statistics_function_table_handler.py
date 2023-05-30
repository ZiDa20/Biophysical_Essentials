from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from scipy import stats
from functools import partial
import pandas as pd
from CustomWidget.Pandas_Table import PandasTable
from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import Ui_StatisticsTable
from Offline_Analysis.error_dialog_class import CustomErrorDialog
import itertools

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from statannotations.Annotator import Annotator

class StatisticsTablePromoted(QWidget, Ui_StatisticsTable):
    """
    Statisics Module
    
    """
    def __init__(self, parent_stacked, analysis_stacked, hierachy_stacked_list, SeriesItems, database_handler, frontend_style, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.tabWidget.widget(1).hide()
        self.statistics_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.statistics_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.frontend_style = frontend_style
        self.parent_stacked = parent_stacked
        self.analysis_stacked = analysis_stacked
        self.hierachy_stacked_list = hierachy_stacked_list
        self.SeriesItems = SeriesItems
        self.database_handler = database_handler
        self.check_meta_data_selected()
        self.autofill_statistics_table_widget()
        self.tabWidget.setTabVisible(1,False)   

    
    def check_meta_data_selected(self):
        """
        statistics  can be only applied between meta data groups and therefore the user must select meta data groups before,
        otherwise each cell is displayed solely and statistics wont work.
        """
        df = self.get_analysis_specific_statistics_df(0) # request the first table since all will have the same meta data for now
        are_equal = df["experiment_name"] == df["meta_data"] # Compare the two columns for equality
        if are_equal.all():
            d = CustomErrorDialog("To run statistics, you have to choose meta data first. Please open the meta-data selection from the ribbon bar above.", self.frontend_style)
            d.exec_()
        else:
            return


    def autofill_statistics_table_widget(self):
        """
        based on the analysis function data are scanned and prepared for the statistical analysis
        """
        self.series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")[0]
        tuple_list = self.database_handler.get_analysis_functions_for_specific_series(self.series_name) # list of tuples
        self.analysis_functions = [item[0] for item in tuple_list]

        existing_row_numbers = self.statistics_table_widget.rowCount() #initiate the table in case there are no rows yet

        if  existing_row_numbers == 0:
            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT ;) !
            self.statistics_table_widget.setColumnCount(5)
            if "Action_Potential_Fitting" in self.analysis_functions:
                #@todo: dynamically ? dz
                self.statistics_table_widget.setRowCount(18+ len(self.analysis_functions)-1) # -1 to remove the AP Fitting
            else:
                self.statistics_table_widget.setRowCount(len(self.analysis_functions))
            self.statistics_table_buttons = [0] * len(self.analysis_functions)
            self.statistics_table_widget.resizeRowsToContents()   

        self.statistics_add_meta_data_buttons = [0]*len(self.analysis_functions)

        for i in range(len(self.analysis_functions)):

            if self.analysis_functions[i] == "Action_Potential_Fitting":
                df = self.get_analysis_specific_statistics_df(i)
                self.autofill_ap_fitting(df,existing_row_numbers)
            else:
               self.autofill_by_analysis_function(i, self.analysis_functions,existing_row_numbers)
        
        self.statistics_table_widget.resizeRowsToContents()   
        start_statistics = QPushButton("Run Statistic Test")
        self.verticalLayout_2.addWidget(start_statistics)
        start_statistics.clicked.connect(partial(self.calculate_statistics))

    def autofill_ap_fitting(self,df,row_count):
        """prepare a row for each ap fitting column"""
        unique_meta_data = list(df["meta_data"].unique())
        for c in range(len(df.columns[0:-2])):
            row_to_insert = row_count+c
            self.statistics_table_widget.setItem(row_to_insert,1, QTableWidgetItem(str(df.columns[c])))
            self.statistics_table_widget.setItem(row_to_insert,2, QTableWidgetItem('\n'.join(unique_meta_data)))
            cell_widget_layout = self.insert_data_distribution(row_to_insert)
            self.insert_statistical_test(row_to_insert)
            #self.get_and_set_data_distribution(df[df.columns[c]],cell_widget_layout)
            self.statistics_table_widget.setRowHeight(row_to_insert, 100)
            print("inserting into" + str(row_to_insert) + df.columns[c])

    def autofill_by_analysis_function(self, function_pos:int, analysis_functions:list, row_count:int):
        """prepare a row for each analysis function and fill the columns appropriately """
        
        analysis_function = analysis_functions[function_pos]
        row_to_insert = function_pos + row_count

        #add the analysis function to column 1
        self.statistics_table_widget.setItem(row_to_insert, 1, QTableWidgetItem(str(analysis_function)))

        df = self.get_analysis_specific_statistics_df(function_pos)
        unique_meta_data = list(df["meta_data"].unique())
        self.statistics_table_widget.setItem(row_to_insert,2, QTableWidgetItem('\n'.join(unique_meta_data))) #insert selected meta data as labels
        self.insert_statistical_test(row_to_insert)
        cell_widget_layout = self.insert_data_distribution(row_to_insert)
        self.get_and_set_data_distribution(df,cell_widget_layout)


    def insert_statistical_test(self,row_to_insert):
        # show test
        self.stat_test = QComboBox()
        self.stat_test.addItems(["Independent t-test","Welchs t-test", "Paired t-test", "Wilcoxon Signed-Rank test", "Kruskal Wallis test", "Brunner-Munzel test"])
        self.statistics_table_widget.setCellWidget(row_to_insert, 4, self.stat_test)

    def insert_data_distribution(self,row_to_insert):
        """
        Insert a combobox to select between normal distribution and non-normal distribution.
        Shapiro Wilk test will be executed to determine data distribution and the combo box will be set to the apropriate distribution
        """
       
        self.data_dist  = QComboBox()
        self.data_dist.addItems(["Normal Distribution", "Non-Normal Distribution"])  # "Bernoulli Distribution", "Binomial Distribution", "Poisson Distribution"
        cell_widget = QWidget()
        cell_widget_layout = QGridLayout()
        cell_widget.setLayout(cell_widget_layout)
        cell_widget_layout.addWidget(self.data_dist,0,0)
        self.statistics_table_widget.setCellWidget(row_to_insert, 3, cell_widget)
        return cell_widget_layout

    def get_and_set_data_distribution(self,df,cell_widget_layout):
        "performs shapiro wil test and sets up the data distribution accordingly"

        if isinstance(df, pd.Series): # AP fittign case, only a single column in the df
            shapiro_test = stats.shapiro(df.tolist())
        else:
            if "Result" in df.columns:
                shapiro_test = stats.shapiro(df["Result"])
            elif "Rheoramp" in df.columns:
                shapiro_test = stats.shapiro(df["Number AP"])
            

        print(shapiro_test)
        test_res = str(round(shapiro_test.pvalue,3))
        
        
        if test_res == "0.0":
            cell_widget_layout.addWidget(QLabel("Test-Performed: Shapiro Wilk\n Result: p< 0.001"),1,0)
        else:
            cell_widget_layout.addWidget(QLabel("Test-Performed: Shapiro Wilk\n Result: p=" + test_res),1,0)
        if shapiro_test.pvalue >= 0.05:
            # evidence that data comes from normal distribution
            self.data_dist.setCurrentIndex(0)
            self.stat_test.setCurrentIndex(0)
        else:
            # no evidence that data comes from normal distribution
            self.data_dist.setCurrentIndex(1)
            self.stat_test.setCurrentIndex(3)


    def get_analysis_specific_statistics_df(self, widget_position):
        """
        function to retrieve the correct statistics df.
        based on the shown plot widget order which is indeitified by widget position (row in the plot view and tab in the table tabwidget)
        """
        # get the meta data from the plot widget
        # @todo better get them from the database
        self.analysis_stacked.setCurrentIndex(self.parent_stacked)
        self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(1)
        result_plot_widget = self.hierachy_stacked_list[self.parent_stacked].currentWidget()
        self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(3)

        # get the table widget that holds the dataframe -- can this be removed then ?? 
        qwidget_item_1 = result_plot_widget.OfflineResultGrid.itemAtPosition(1, widget_position)
        custom_plot_widget = qwidget_item_1.widget()
        return custom_plot_widget.statistics

    def calculate_statistics(self):
        """
        calculate statistics for all the plot widgets
        """
        for row in range(self.statistics_table_widget.rowCount()):   
            
            if "Action_Potential_Fitting" in self.analysis_functions: # ap fitting is one function but i want to show each parameter already
                df = self.get_analysis_specific_statistics_df(0)
            else:
                df = self.get_analysis_specific_statistics_df(row)

            
            test_type = self.statistics_table_widget.cellWidget(row,4).currentText()  # get the test to be performed from the combo box (position 4)
            unique_groups  = list(df["meta_data"].unique()) # get unique meta data groups to compare
            pairs = self.get_pairs(unique_groups) # get a list of tuples for pairwise comparison
            
            # tables from voltage clamp analysis have a column "Voltage" to identify voltage step (e.g. KO_80mV vs CTRL_80mV)
            # tables from rheoramp analysis will have a column "Rheoramp" to identify the rheoramp number
            # 

            if "Voltage" in df.columns:
                voltage_steps = list(df["Voltage"].unique())
                res_df = pd.DataFrame(columns=["Voltage", "Group_1", "Group_2", "p_Value"])
                for v in voltage_steps:
                
                    for p in pairs:
                        group1 = df[(df["meta_data"]==p[0]) & (df["Voltage"]==v)]["Result"]
                        group2 = df[(df["meta_data"]==p[1]) & (df["Voltage"]==v)]["Result"]
                        tmp = self.apply_stats_test(test_type,group1,group2, p, "Voltage", v)
                        res_df = pd.concat([res_df, tmp])

                self.create_statistics_for_steps(row, test_type,res_df)
                

            elif "Rheoramp" in df.columns:
                ramp_steps = list(df["Rheoramp"].unique())
                res_df = pd.DataFrame(columns=["Rheoramp", "Group_1", "Group_2", "p_Value"])
                for v in ramp_steps:
                
                    for p in pairs:
                        group1 = df[(df["meta_data"]==p[0]) & (df["Rheoramp"]==v)]["Number AP"]
                        group2 = df[(df["meta_data"]==p[1]) & (df["Rheoramp"]==v)]["Number AP"]
                        tmp = self.apply_stats_test(test_type,group1,group2, p, "Rheoramp", v)
                        res_df = pd.concat([res_df, tmp])

                self.create_statistics_for_steps(row, test_type,res_df)

            elif "AP_Amplitude [mV]" in df.columns:

                c_name = df.columns[row] # get the current name of the parameter
                res_df = pd.DataFrame(columns=["Parameter", "Group_1", "Group_2", "p_Value"]) # result data frame to be displayed
                for p in pairs:
                    group1 = df[df["meta_data"]==p[0]][c_name]
                    group2 = df[df["meta_data"]==p[1]][c_name]
                    tmp = self.apply_stats_test(test_type,group1,group2, p)
                    res_df = pd.concat([res_df, tmp])
                res_df["Parameter"] = c_name

                row_layout = self.create_statistics_for_steps(row, test_type,res_df)
                        
                canvas= self.show_statistic_results(df, pairs,test_type, c_name) # data to visualize are in the column that is named according the current parameter name

                row_layout.addWidget(canvas,0, 1, 3, 1)
                
                canvas.draw_idle()
                  
            else: # simple boxplots for each meta data group to be compared
                
                res_df = pd.DataFrame(columns=["Group_1", "Group_2", "p_Value"]) # result data frame to be displayed
                for p in pairs:
                    group1 = df[df["meta_data"]==p[0]]["Result"]
                    group2 = df[df["meta_data"]==p[1]]["Result"]
                    tmp = self.apply_stats_test(test_type,group1,group2, p)
                    res_df = pd.concat([res_df, tmp])

                statistics_table_view = QTableView()
                model = PandasTable(res_df)
                statistics_table_view.setModel(model)
                self.statistics_result_grid.addWidget(statistics_table_view)
                #statistics_table_view.show()    

                canvas = self.show_statistic_results(df, pairs,test_type, "Result") # data to visualize are in column "results"
                self.statistics_result_grid.addWidget(canvas)
                canvas.draw_idle()

                self.tabWidget.setTabVisible(1,True)
                #self.tabWidget.widget(1).show()   
                self.tabWidget.setCurrentIndex(1)

    def create_statistics_for_steps(self, row:int, test_type:str, res_df:pd.DataFrame):
        """
        frontend handling to show tables for the statistics results
        """
        layout  = QVBoxLayout()
        row_layout  = QGridLayout()
        
        label = QLabel("Statistics of " + self.statistics_table_widget.item(row,1).text())
        #label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(400, 50)  # Set the maximum width and height as desired
        label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        row_layout.addWidget(label,0,0)

        label = QLabel("Performed Statistics:" + test_type)
        #label.setAlignment(Qt.AlignCenter)
        label.setMaximumSize(400, 50)  # Set the maximum width and height as desired
        label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        row_layout.addWidget(label,1,0)

        statistics_table_view = QTableView()
        #statistics_table_view.setAlignment(Qt.AlignCenter)
        model = PandasTable(res_df)
        statistics_table_view.setModel(model)
        model.resize_header(statistics_table_view)
        row_layout.addWidget(statistics_table_view,2,0)
        
        statistics_table_view.setSizeAdjustPolicy(QTableView.AdjustToContents)

        # Set the size policy of the QTableView and its parent widget to MinimumExpanding
        statistics_table_view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        statistics_table_view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        
        #statistics_table_view.resizeColumnsToContents()

        #self.statistics_result_grid.addLayout(row_layout)
        grid_widget = QWidget()
        grid_widget.setLayout(row_layout)
        layout.addWidget(grid_widget)
        self.statistics_result_grid.addLayout(layout)
        self.tabWidget.setTabVisible(1,True)   
        self.tabWidget.setCurrentIndex(1)

        return row_layout


    def show_statistic_results(self, df, pairs, test_type, y_column):
        """
        create a plot of the data
        """

        # Create a FigureCanvasQTAgg from the Figure object returned by Seaborn
        
        fig = plt.Figure()
        ax = fig.add_subplot(111)

        sns.boxplot(data=df,x ="meta_data" ,y = y_column, ax=ax)
        annotator = Annotator(ax, pairs, data=df, x ="meta_data" ,y = y_column)
        test_identifier= {"Independent t-test": "t-test_ind",
                          "Welchs t-test":"t-test_welch", 
                          "Paired t-test":"test_paired",
                           "Wilcoxon Signed-Rank test":"Wilcoxon", 
                           "Kruskal Wallis test":"Kruskal"}
        # t-test_ind, t-test_welch, t-test_paired, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, Levene, Wilcoxon, Kruskal, Brunner-Munzel.

        annotator.configure(test=test_identifier[test_type], text_format='star', loc='inside') #Mann-Whitney
        annotator.apply_and_annotate()
        canvas = FigureCanvas(fig)
        print("returning filled canvas")
        return canvas

    def apply_stats_test(self,test_type,group1,group2, group_pair, data_type=None, voltage=None):
        """
        apply a specific test to the specified data in group1 and group2
        """
        if len(group2)>=len(group1):
            group2 = group2[0:len(group1)]
        else:
            group1 = group1[0:len(group2)]
    
        try:
            if test_type == "Independent t-test":
                res =  stats.ttest_ind(group1,group2)
            elif test_type == "Wilcoxon Signed-Rank test":
                res = stats.wilcoxon(group1,group2)
            
            if data_type: # for all voltage clamp recordings
                tmp = pd.DataFrame({str(data_type):voltage, "Group_1":[group_pair[0]], "Group_2":[group_pair[1]], "p_Value":[round(res.pvalue,4)]})
            else:
                tmp = pd.DataFrame({"Group_1":[group_pair[0]], "Group_2":[group_pair[1]], "p_Value":[round(res.pvalue,4)]})

        except Exception as e:
            #@todo better handling ? DZ
            print("Error in statistics", e)
            if data_type == "Voltage":
                tmp = pd.DataFrame({"Voltage":voltage, "Group_1":[group_pair[0]], "Group_2":[group_pair[1]], "p_Value":["Error"]})
            else:
                tmp = pd.DataFrame({"Group_1":[group_pair[0]], "Group_2":[group_pair[1]], "p_Value":["Error"]})

        return tmp
    

    def get_pairs(self, item_list):
        # Initialize an empty list to store the pairs
        pairs = []
        # Iterate over the items in the list
        for i, item1 in enumerate(item_list):
            # Iterate over the remaining items in the list
            for item2 in item_list[i+1:]:
                # Add the pair to the list
                pairs.append((item1, item2))
        return pairs
