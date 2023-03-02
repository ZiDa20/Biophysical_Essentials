import logging
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt

from numpy import nan

from Offline_Analysis.Analysis_Functions.Function_Templates.SpecificAnalysisCalculations import \
    SpecificAnalysisFunctions


class OfflinePlots():
    
    logger = logging.getLogger(__name__)
    """Class to handle the Plot Drawing and Calculations for the Offline Analysis
    Basis Analysis Functions
    """
    def __init__(self,  
                 database_handler,
                 frontend, 
                 offline_tree, 
                 final_result_holder):
        
        """Initializing the Plotting class with canvas and axis

        Args:
            database_handler (DuckDBHandler): DataBase Handler
            frontend (Frontend_Style): Frontend_Style Class that handles dark-light mode
            offline_tree(SeriesItemTreeWidget): SeriesItemsManager Class
            final_result_holder(ResultHolder): ResultHolder Class that holds the Final Output Data of the Offline Analysis

        """
        self.frontend = frontend
        if self.frontend.current_style == 0:
            self.frontend.set_mpl_style_dark()
        else:
            self.frontend.set_mpl_style_white()
        self.violin = None # should be set if violinplot should be run
        self.meta_data = None
        self.parent_widget = None
        # reference the needed classes
        self.offline_tree = offline_tree
        self.database_handler = database_handler
        self.result_holder = final_result_holder.analysis_result_dictionary 
        self.color = frontend.get_color_plots()
        self.statistics = None
        self.explained_ratio = None # should be the expalined variance ratio of the PCA
       
    
        # initialize the logger
        self.set_logger()
        
    def set_logger(self):
        """Sets the logger for the Offline Analyiss Plotting
        """
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler("offline_plots.log")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def set_frontend_axes(self, parent_widget):
        """_summary_: This function should set the axis and teh figure of the canvas
        and assign this as instance member

        Args:
            canvas (Figure Canvas): Matplotlib Figure Canvas holding the plot
        """
        
        #parent_widget.canvas = canvas
        parent_widget.ax = parent_widget.canvas.figure.subplots()
        self.frontend.ax.append(parent_widget.ax)
        self.frontend.canvas = parent_widget.canvas

    def set_metadata_table(self, result_table_list):
        """_summary_: Sets the metadata table retrieved from the result_table_list

        Args:
            result_table_list (list): Holding the result tables for the specific
            analysis function id
        """
        result_table_list = tuple(result_table_list)
        q = f'select * from global_meta_data where experiment_name IN (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name IN (select sweep_table_name from results where ' \
                f'specific_result_table_name IN {result_table_list}))'
                
                
        self.meta_data = self.database_handler.get_data_from_database(self.database_handler.database, q,fetch_mode = 2)
        self.meta_data = self.meta_data.replace("None", nan)
        self.meta_data = self.meta_data.dropna(axis='columns', how ='all')
    
    def retrieve_analysis_function(self,parent_widget= None, result_table_list = None, switch = None, meta = None):
        """Retrieves the appropriate Analysis Function, sets the parent widget as instance variable
        retrieves the analysis function id from from parent widget and also evaluate the swithc

        Args:
            parent_widget (_type_): The Parent Widget to draw in the canvas
            result_table_list (_type_): The tables that will be visualized for the specific series
            analysis_function (_type_): The analysis function choosen for the specific series
            switch (bool): Should indicate if redraw without 
        """
        self.logger.info("Retrieving analysis function")
        # code goes here
        
        
        self.parent_widget = parent_widget
            
        if switch:
            self.parent_widget.holded_dataframe = None
            
        analysis_function = self.parent_widget.plot_type_combo_box.currentText()
        analysis_function_id = self.parent_widget.analysis_function_id
        # should retrieve the right function based on the selected analysis function
        self.plot_dictionary = {"Boxplot": self.make_boxplot,
                                "No Split": self.simple_plot, 
                                "Rheobase Plot": self.rheobase_plot,
                                "Sweep Plot": self.single_rheobase_plot,
                                "Rheoramp-AUC": self.rheoramp_plot,
                                "Action_Potential_Fitting": self.ap_fitting_plot,
                                "Single_AP_Parameter": self.single_ap_parameter_plot,
                                "Mean_Action_Potential_Fitting": self.mean_ap_fitting_plot,
                                "Linear Regression": self.regression_plot,
                                "PCA-Plot": self.pca_plot,
                                "AP-Overlay": self.ap_overlay
                                }

        # retrieve the appropiate plot from the combobox
        if analysis_function == "Violinplot":
            self.violin = True

        self.parent_widget.selected_meta_data = self.database_handler.get_selected_meta_data(analysis_function_id)
            
        try:
            self.plot_dictionary.get(analysis_function)(result_table_list)
        except Exception as e:
            self.logger.error(f"Analysis function could not be retrieved {e}")
            raise KeyError(f"Analysis function could not be retrieved {e}")	
        
        self.logger.info(f"Analysis function retrieved successfully {analysis_function}")
        
    def make_boxplot(self,result_table_list: list):

        """Specific Function to draw Boxplots from long table formats
        of different Analysis Function

        Args:
            result_table_list (list): Result Table List of the specific Analysis Function
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            plot_dataframe = SpecificAnalysisFunctions.boxplot_calc(result_table_list, self.database_handler)
            self.merge_meta_plot_and_assign_meta(plot_dataframe)
        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()  
                
        self.comparison_plot(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.logger.info("Created Boxplot successfully")
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        self.add_data_frame_to_result_dictionary(self.parent_widget.holded_dataframe)

    
    def simple_plot(self, result_table_list:list):
        """
        Plot all data without incorporating meta data groups
        :param result_table_list: the list of result tables for the specific analysis
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            self.parent_widget.increment = increment
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()  
                
        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)    
        pivoted_table = self.simple_plot_make(self.parent_widget.holded_dataframe, self.parent_widget.increment)
        self.parent_widget.canvas.draw_idle()        
        self.parent_widget.export_data_frame = pivoted_table
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        
    def rheobase_plot(self, result_table_list:list):
        """Plotting Function to draw rheobase boxplot into the OfflineAnalysisResultAnalyzer

        Args:
            result_table_list (list): Result Table list of the generate by the Analysis Function
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.rheobase_calc(result_table_list, self.database_handler)
            self.merge_meta_plot_and_assign_meta(plot_dataframe)
        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
        
        self.comparison_plot(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe


    def merge_meta_plot_and_assign_meta(self, plot_dataframe: pd.DataFrame):
        """_summary_

        Args:
            plot_dataframe (pd.DataFrame): _description_
            self.parent_widget.selected_meta_data (list): _description_
        """
        plot_dataframe = pd.merge(
            plot_dataframe,
            self.meta_data,
            left_on="experiment_name",
            right_on="experiment_name",
            how="left",
        )
        plot_dataframe["meta_data"] = plot_dataframe[self.parent_widget.selected_meta_data].agg(
            '::'.join, axis=1
        )
        self.parent_widget.holded_dataframe = plot_dataframe
        
    def single_rheobase_plot(self, result_table_list:list):
        """Creates Plots for single rheobase calculation --> stepplot

        Args:
            result_table_list (_type_): List of Rheobase Result Tables
        """
        if not self.parent_widget.selected_meta_data:
                self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.sweep_rheobase_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            self.parent_widget.holded_dataframe = plot_dataframe
        
        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
                
        self.simple_plot_make(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        
        
    def rheoramp_plot(self, result_table_list: list):
        """Creates Lineplot and boxplot for Rheoramp Protocols

        Args:
            result_table_list (list): Result Table list for Rheoramp Analysis
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.rheoramp_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            self.parent_widget.holded_dataframe = plot_dataframe
        
        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
                
        self.line_boxplot(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe

    def initiate_hidden_selection_widgets(self):
        """
        specific function to show single ap parameter:  therefore, a hidden combobox is made visible
        """
        self.parent_widget.parameter_label.show()
        self.parent_widget.parameter_combobox.show()
        for i in list(self.statistics.columns[0:-1]): # last item is the experiment name which is non numeric and would throw an error
            self.parent_widget.parameter_combobox.addItem(i)

        self.parent_widget.parameter_combobox.currentIndexChanged.connect(self.show_single_ap_param_selected_in_combobox)


    def single_ap_parameter_plot(self, result_table_list:list):
        """
        creates a boxplot of a single AP parameter, specific ap can be selected by the user
        therefore, a hidden combobox is made visible

        Args:
            result_table_list (list): Result Table list for AP Analysis
        
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            statitics_dataframe, _ = SpecificAnalysisFunctions.ap_calc(result_table_list, self.database_handler)
            # its the unscaled dataframe
            self.parent_widget.statistics = statitics_dataframe
            self.parent_widget.holded_dataframe = pd.merge(statitics_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")

        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()  
        
        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
        self.holded_dataframe = self.parent_widget.holded_dataframe.sort_values(by = ["meta_data", "experiment_name"])

        if self.parent_widget.parameter_label.isHidden():
            self.initiate_hidden_selection_widgets()

        self.show_single_ap_param_selected_in_combobox()

    def show_single_ap_param_selected_in_combobox(self):
        """
        creates the boxplot of a single AP parameter, specific ap can be selected by the user in a combobox
        """
        param = [self.parent_widget.parameter_combobox.currentText()]
        param.append("meta_data")
        plot_df = self.holded_dataframe[param]
        plot_df.rename(columns={param[0]:"values"}, inplace=True)

        #drawing_data = self.parent_widget.holded_dataframe[self.statistics.columns[1:-1]].T
        
        for ax in self.parent_widget.canvas.figure.axes:
            ax.cla() 
                     
        self.comparison_plot(plot_df)
        self.parent_widget.canvas.draw_idle()
        self.logger.info("Created Boxplot successfully")
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        self.add_data_frame_to_result_dictionary(self.parent_widget.holded_dataframe)

    def mean_ap_fitting_plot(self, result_table_list:list):
        # calculate a mean for each column per meta data type
        self.ap_fitting_plot(result_table_list, True)

    def ap_fitting_plot(self, result_table_list: list, agg: bool = False):
        """Should Create the Heatmap for each Fitting Parameter
        calculated by the APFitting Procedure
        
        Args:
            result_table_list (list): List of queried result tables
            agg (bool, optional): If True, the data will be aggregated by the selected meta data. Defaults to False.
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]
        
        # cbar = parameter to control the display of the colorbar next to the plot. 
        # should only be plotted once and then never again when meta data is changed.
        cbar = True 
        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            statitics_dataframe, plot_dataframe = SpecificAnalysisFunctions.ap_calc(result_table_list, self.database_handler)
            self.statistics = statitics_dataframe
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                if not ax._label =="<colorbar>":
                     ax.cla() 
                     cbar = False

        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
        self.holded_dataframe = self.parent_widget.holded_dataframe.sort_values(by = ["meta_data", "experiment_name"])
        
       
        if agg:  # if agg - calculate the mean for each meta data group
            new_df = pd.DataFrame()
            for m in list(self.holded_dataframe["meta_data"].unique() ):  # calculate the mean for each meta data group and for each ap parameter
                subset = self.holded_dataframe[self.holded_dataframe["meta_data"]==m]
                tmp_dict = {}
                for c in  self.statistics.columns[0:-1]: # get rid of the last since this is the experiment name
                    tmp_dict[c] = [np.mean(subset[c].values)]
                new_df = pd.concat([new_df, pd.DataFrame(tmp_dict)])
            drawing_data = new_df.T
            sns.heatmap(data = drawing_data, ax = self.parent_widget.ax, cbar = cbar, xticklabels=self.holded_dataframe["meta_data"].unique(), yticklabels=drawing_data.index)
        else:
           drawing_data = self.parent_widget.holded_dataframe[self.statistics.columns[1:-1]].T
           sns.heatmap(data = drawing_data, ax = self.parent_widget.ax, cbar = cbar, xticklabels=self.holded_dataframe["meta_data"], yticklabels=drawing_data.index)
    
        self.parent_widget.canvas.figure.tight_layout()
        self.parent_widget.export_data_frame = self.statistics
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        self.parent_widget.canvas.draw_idle()



    def ap_overlay(self, result_table_list:list):
        """_summary_

        Args:
            result_table_list (list): _description_
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            plot_dataframe = SpecificAnalysisFunctions.overlay_cal(result_table_list, self.database_handler)
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            #plot_dataframe = plot_dataframe.groupby(["meta_data", "Time"])["AP_Window"].agg(["mean", "sem"]).reset_index()
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
          
        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)  
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
        sns.lineplot(data = self.parent_widget.holded_dataframe , x= "AP_Timing", y = "AP_Window", hue = "meta_data", errorbar=("se", 2), ax = self.parent_widget.ax) 
        self.parent_widget.canvas.draw_idle()
       
    def regression_plot(self, result_table_list: list):
        """Draws a Regression line which determines the slope of the 

        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): _description_
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            self.hue_regplot(data=plot_dataframe, x='index', y='values', hue='meta_data', ax=self.parent_widget.ax)
            self.parent_widget.holded_dataframe = plot_dataframe


        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
            self.hue_regplot(data=self.parent_widget.holded_dataframe, x='index', y='values', hue='meta_data', ax=self.parent_widget.ax)
            self.parent_widget.canvas.draw_idle()

        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
    
    def pca_plot(self, result_table_list: list):
         
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"] 

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, self.explained_ratio = SpecificAnalysisFunctions.pca_calc(result_table_list, self.database_handler)
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear() 
        
        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)     
        self.scatter_plot_make(self.parent_widget.holded_dataframe, self.explained_ratio)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe
  
    def simple_plot_make(self,plot_dataframe, increment = None):
        """Makes either a boxplot if increment is indicating no step protocol
        

        Args:
            plot_dataframe (_type_): dataframe holding data that fits the natures of a box plot or a line plot
            increment (_type_): should indicate if step protocol was use, if None step protocol was used else single step

        Returns:
            pd.DataFrame: Pivoted dataframe having columns either as experiment name or as metadata name
        """
        if increment: # if sweep have different voltage steps indicated by increment in pgf file
            self.comparison_plot(plot_dataframe)
            try: 
                pivoted_table = pd.pivot_table(plot_dataframe, index = ["index"], columns = ["meta_data"], values = "values")
            except Exception as e:
                print(e)
                
        else: # if stable voltage dependency
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "meta_data", ax = self.parent_widget.ax,  errorbar=("se", 2))
            self.parent_widget.connect_hover(g)
            try:
                pivoted_table =  pd.pivot_table(plot_dataframe, index = ["Unit"], columns = ["meta_data"], values = "values")
            except Exception as e:
                print(e)
        
        self.parent_widget.ax.autoscale()
        self.parent_widget.canvas.figure.tight_layout()        
        return pivoted_table    
    
    def comparison_plot(self, plot_dataframe):
        """Creates a comparison plot using either boxplots or violin plots 
        as selected

        Args:
            boxplot_df (_type_): _description_
        """
        # check if violin parameter is set then use the violin plots
        if self.violin:
            self.violin_plot_maker(plot_dataframe)        
        else:
            self.box_plot_maker(plot_dataframe)
                
    
    def violin_plot_maker(self, plot_dataframe):
        """_summary_: Draws a Violin and a Swarmplot from the data

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        g = sns.violinplot(data = plot_dataframe, 
                    x="meta_data", 
                    y = "values",  
                    ax = self.parent_widget.ax, 
                    width = 0.5)

        self.swarm_plot(plot_dataframe, 10, g)
        
    def box_plot_maker(self, plot_dataframe):
        """_summary_: Draws a boxplot and a Swarmplot from the data

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        g = sns.boxplot(data = plot_dataframe, 
                    x="meta_data", 
                    y = "values",  
                    ax = self.parent_widget.ax, 
                    width = 0.5)

        #self.swarm_plot(plot_dataframe, 2, g)

    # TODO Rename this here and in `violin_plot_maker` and `box_plot_maker`
    def swarm_plot(self, plot_dataframe, size, g):
        z = sns.swarmplot(
            data=plot_dataframe,
            x="meta_data",
            y="values",
            ax=self.parent_widget.ax,
            color=self.color,
            size=size,
        )
        g.set_xticklabels(g.get_xticklabels(), rotation=45)
        z.set_xticklabels(g.get_xticklabels(), rotation=45)
        self.parent_widget.canvas.figure.tight_layout()


    def scatter_plot_make(self, plot_dataframe, explaind_ratios = None):
        """_summary_: Creates a scatter plot from the data"""
        sns.scatterplot(x = "PC1", y = "PC2", data = plot_dataframe, hue = "meta_data", ax = self.parent_widget.ax, s = 50, linewidth = False)
        if explaind_ratios:
            self.parent_widget.ax.set_xlabel(f"PC1: {str(explaind_ratios[0])}")
            self.parent_widget.ax.set_ylabel(f"PC2: {str(explaind_ratios[1])}")
        sns.move_legend(self.parent_widget.ax, "upper left", bbox_to_anchor=(1, 1))
        self.parent_widget.canvas.figure.tight_layout()


    def line_boxplot(self, plot_dataframe):
        """_summary_: Creates a line plot with boxplots

        Args:
            plot_dataframe (_type_): _description_
        """
        g = sns.lineplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "meta_data", ax = self.parent_widget.ax, errorbar=("se", 2), legend = False)
        sns.boxplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "meta_data", ax = self.parent_widget.ax)
        self.parent_widget.canvas.figure.tight_layout()
        self.parent_widget.ax.autoscale()


    def hue_regplot(self,data, x, y, hue, palette=None, **kwargs):
        """Draw a scatterplot with regression line for each unique value of a column."""
        levels = data[hue].unique()
        if palette is None:
            default_colors = get_cmap('tab10')
            palette = {k: default_colors(i) for i, k in enumerate(levels)}

        return [
            sns.regplot(
                x=x, y=y, data=data[data[hue] == key], color=palette[key], **kwargs
            )
            for key in levels
        ]

    ################################################################################
    # Upload Data Controls
    ################################################################################

    def add_data_frame_to_result_dictionary(self, dataframe: pd.DataFrame):
        """_summary_ Should add the dataframe to the result dictionary

        Args:
            dataframe (_type_): _description_
        """
        dataframe["analysis_id"] = self.database_handler.analysis_id
        self.result_holder.append(dataframe)  
        
