from __future__ import annotations
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib.cm import get_cmap
from Offline_Analysis.Analysis_Functions.Function_Templates.SpecificAnalysisCalculations import SpecificAnalysisFunctions
from mplcursors import cursor
import picologging
class OfflinePlots():

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
        if self.frontend.default_mode == 0:
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
        self.holded_dataframe = None
        self.statistics = None
        self.explained_ratio = None # should be the expalined variance ratio of the PCA
        self.plot_dictionary = {"Boxplot": self.make_boxplot,
                                "No Split": self.simple_plot,
                                "Rheobase Plot": self.rheobase_plot,
                                "Sweep Plot": self.single_rheobase_plot,
                                "Rheoramp-AUC": self.rheoramp_plot,
                                "Parameter-Heatmap": self.ap_fitting_plot,
                                "Single_AP_Parameter": self.single_ap_parameter_plot,
                                "Mean_Action_Potential_Fitting": self.mean_ap_fitting_plot,
                                "Linear Regression": self.regression_plot,
                                "PCA-Plot": self.pca_plot,
                                "AP-Overlay": self.ap_overlay,
                                "Capacitance Plot": self.capacitance_plot
                                }

        # initialize the logger
        self.logger = picologging.getLogger(__name__)
        sns.set_palette("Set2")

    def set_frontend_axes(self, parent_widget):
        """_summary_: This function should set the axis and teh figure of the canvas
        and assign this as instance member

        Args:
            canvas (Figure Canvas): Matplotlib Figure Canvas holding the plot
        """

        parent_widget.ax = parent_widget.canvas.figure.subplots()
        self.frontend.ax.append(parent_widget.ax)
        self.frontend.canvas = parent_widget.canvas

    def set_metadata_table(self, result_table_list: list) -> None:
        """_summary_: Sets the metadata table retrieved from the result_table_list

        Args:
            result_table_list (list): Holding the result tables for the specific
            analysis function id
        """
        result_table_list = tuple(result_table_list)

        # this we have do redo
        q = f'select * from global_meta_data where experiment_name IN (select experiment_name from {result_table_list[0]})'


        self.meta_data = self.database_handler.get_data_from_database(self.database_handler.database, q,fetch_mode = 2)
        self.meta_data = self.meta_data.dropna(axis='columns', how ='all')
        self.meta_data = self.meta_data.fillna("None")

    def retrieve_analysis_function(self,parent_widget= None, result_table_list: list = None, switch: bool = None):
        """Retrieves the appropriate Analysis Function, sets the parent widget as instance variable
        retrieves the analysis function id from from parent widget and also evaluate the swithc

        Args:
            parent_widget (QTWidget[]): The Parent Widget to draw in the canvas
            result_table_list (_type_): The tables that will be visualized for the specific series
            analysis_function (_type_): The analysis function choosen for the specific series
            switch (bool): Should indicate if redraw without
        """

        # code goes here
        self.parent_widget = parent_widget
        if switch:
            self.parent_widget.holded_dataframe = None

        # the combo box could have been already deleted     
        try:
            analysis_function = self.parent_widget.plot_type_combo_box.currentText()
        except Exception as e:
            analysis_class_name = self.parent_widget.analysis_name
            class_object = AnalysisFunctionRegistration.get_registered_analysis_class(analysis_class_name)
            analysis_function = class_object().plot_type_options[0]

        analysis_function_id = self.parent_widget.analysis_function_id
        self.logger.info(f"Retrieving analysis function: {analysis_function}, {analysis_function_id}")
        # should retrieve the right function based on the selected analysis function
        # retrieve the appropiate plot from the combobox
        if analysis_function == "Violinplot":
            self.violin = True

        self.parent_widget.selected_meta_data = self.database_handler.get_selected_meta_data(analysis_function_id)
        #debug = self.database_handler.get_selected_meta_data(analysis_function_id)

        self.logger.info("retrieving analysis function")
        self.logger.info(analysis_function)
        self.logger.info("result table list is")
        self.logger.info(result_table_list)
        self.logger.info(self.plot_dictionary)

        try:
            self.plot_dictionary.get(analysis_function)(result_table_list)
        except Exception as e:
            self.logger.error(f"Analysis function could not be retrieved {e}")
            raise KeyError(f"Analysis function could not be retrieved {e}")

        self.logger.info(f"Analysis function retrieved successfully {analysis_function}")

    def add_sweep_meta_data_to_result_table(self,result_table):
        # replace column Sweep_Table_Name with series_identifier and add the series meta data
        experiment_series_table = self.database_handler.database.execute("select * from experiment_series").fetchdf()
        series_merge = pd.merge(result_table, experiment_series_table, left_on = "Sweep_Table_Name", right_on = "sweep_table_name", how = "left")
        result_table["Sweep_Table_Name"]=series_merge["series_identifier"]
        result_table["series_meta_data"]=series_merge["series_meta_data"]
        return result_table
   

    def make_boxplot(self,result_table_list: list) -> None:

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


    def simple_plot(self, result_table_list:list) -> None:
        """
        Plot all data without incorporating meta data groups
        :param result_table_list: the list of result tables for the specific analysis
        """

        self.logger.info("Simple Plot started")
        try:
            if not self.parent_widget.selected_meta_data:
                self.parent_widget.selected_meta_data = ["experiment_name"]

            if self.parent_widget.holded_dataframe is None:
                # retrieve the plot_dataframe
                plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
                plot_dataframe = self.add_sweep_meta_data_to_result_table(plot_dataframe) # adds series identifier and series meta data
                # merge with the experiment meta data
                self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
                self.parent_widget.increment = increment

            else:
                for ax in self.parent_widget.canvas.figure.axes:
                    ax.clear()

            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            self.logger.info("ready to do the simple plot")
            pivoted_table = self.simple_plot_make(self.parent_widget.holded_dataframe, increment = self.parent_widget.increment)
            self.parent_widget.canvas.draw_idle()
            self.parent_widget.export_data_frame = pivoted_table
            self.parent_widget.statistics = self.parent_widget.holded_dataframe
        except Exception as e:
            self.logger.error(f"Simple Plot could not be created {e}")


    def capacitance_plot(self, result_table_list:list) -> None:
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
        self.plot_capacitance(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe

    def rheobase_plot(self, result_table_list:list) -> None:
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
            plot_dataframe = self.add_sweep_meta_data_to_result_table(self.parent_widget.holded_dataframe) # adds series identifier and series meta data
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()

        self.comparison_plot(self.parent_widget.holded_dataframe)
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe


    def merge_meta_plot_and_assign_meta(self, plot_dataframe: pd.DataFrame) -> None:
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
        plot_dataframe = self.add_sweep_meta_data_to_result_table(plot_dataframe) # adds series identifier and series meta data
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

        self.simple_plot_make(self.parent_widget.holded_dataframe, value = "current")
        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe


    def rheoramp_plot(self, result_table_list: list) -> None:
        """Creates Lineplot and boxplot for Rheoramp Protocols

        Args:
            result_table_list (list): Result Table list for Rheoramp Analysis
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.rheoramp_calc(result_table_list, self.database_handler)
            plot_dataframe = self.add_sweep_meta_data_to_result_table(plot_dataframe) # adds series identifier and series meta data
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

    def initiate_hidden_selection_widgets(self) -> None:
        """
        specific function to show single ap parameter:  therefore, a hidden combobox is made visible
        """
        self.parent_widget.parameter_label.show()
        self.parent_widget.parameter_combobox.show()
        for i in list(self.statistics.columns[0:-1]): # last item is the experiment name which is non numeric and would throw an error
            self.parent_widget.parameter_combobox.addItem(i)

        self.parent_widget.parameter_combobox.currentIndexChanged.connect(self.show_single_ap_param_selected_in_combobox)


    def single_ap_parameter_plot(self, result_table_list:list) -> None:
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
            self.add_sweep_meta_data_to_result_table(statitics_dataframe)
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
        plot_df.rename(columns={param[0]:"Result"}, inplace=True)

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

    def ap_fitting_plot(self, result_table_list: list, agg: bool = False) -> None:
        """Should Create the Heatmap for each Fitting Parameter
        calculated by the APFitting Procedure

        Args:
            result_table_list (list): List of queried result tables
            agg (bool, optional): If True, the data will be aggregated by the selected meta data. Defaults to False.
        """


        df_names_to_drop = ['Analysis_ID', 'Function_Analysis_ID', 'Sweep_Table_Name', 'Sweep_Number', 
                            'Current', 'Duration', 'Result', 'Increment', 'experiment_name',
                            'series_meta_data','analysis_id','experiment_label','species','genotype','sex','celltype','condition','individuum_id',"meta_data"]
        
     
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        # cbar = parameter to control the display of the colorbar next to the plot.
        # should only be plotted once and then never again when meta data is changed.
        cbar = True
        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            statitics_dataframe, plot_dataframe = SpecificAnalysisFunctions.ap_calc(result_table_list, self.database_handler)
            self.statistics = statitics_dataframe
            self.add_sweep_meta_data_to_result_table(plot_dataframe)
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                if not ax._label =="<colorbar>":
                    ax.cla()
                    cbar = False

        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].astype(str).agg('::'.join, axis=1)

        self.statistics["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].astype(str).agg('::'.join, axis=1)

        self.holded_dataframe = self.parent_widget.holded_dataframe.sort_values(by = ["meta_data", "experiment_name"])

        if agg:  # if agg - calculate the mean for each meta data group
            new_df = pd.DataFrame()
            for m in list(self.holded_dataframe["meta_data"].unique() ):  # calculate the mean for each meta data group and for each ap parameter

                subset = self.parent_widget.holded_dataframe[self.holded_dataframe["meta_data"]==m]
                subset = subset.drop(columns=[col for col in subset.columns if col in df_names_to_drop])
                tmp_dict = {}
                for c in  subset.columns: 
                    tmp_dict[c] = [np.mean(subset[c].values)]
                tmp_df = pd.DataFrame(tmp_dict)
                new_df = pd.concat([new_df, tmp_df])

            drawing_data = new_df.T
            sns.heatmap(data = drawing_data , ax = self.parent_widget.ax, cbar = cbar, xticklabels=self.holded_dataframe["meta_data"].unique(), yticklabels=drawing_data.index)
        else:
           # get rid of the last 3: since this is the experiment name, series identifier and meta data
           drawing_data = self.parent_widget.holded_dataframe.drop(columns=[col for col in self.parent_widget.holded_dataframe.columns if col in df_names_to_drop]).T
           #drawing_data = self.parent_widget.holded_dataframe[self.statistics.columns[1:-3]].T
           print(drawing_data.columns)
           sns.heatmap(data = drawing_data, ax = self.parent_widget.ax, cbar = cbar, xticklabels=self.holded_dataframe["meta_data"], yticklabels=drawing_data.index)

        self.parent_widget.canvas.figure.tight_layout()
        self.parent_widget.export_data_frame = self.statistics
        self.parent_widget.statistics = self.statistics #drawing_data #self.parent_widget.holded_dataframe
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
        sns.set_palette("colorblind")
        sns.lineplot(data = self.parent_widget.holded_dataframe , x= "AP_Timing", y = "AP_Window", hue = "meta_data", ax = self.parent_widget.ax)
        # errorbar=("se", 2),
        self.parent_widget.canvas.draw_idle()


    def regression_plot(self, result_table_list: list) -> None:
        """Draws a Regression line which determines the slope of the

        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): _description_
        """
        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, _ = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            self.add_sweep_meta_data_to_result_table(plot_dataframe) # adds series identifier and series meta data
            plot_dataframe["meta_data"] = plot_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            self.hue_regplot(data=plot_dataframe, x='Sweep_Number', y='Result', hue='meta_data', ax=self.parent_widget.ax)
            self.parent_widget.holded_dataframe = plot_dataframe


        else:
            self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].agg('::'.join, axis=1)
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()

            self.hue_regplot(data=self.parent_widget.holded_dataframe, x='Sweep_Number', y='Result', hue='meta_data', ax=self.parent_widget.ax)
            self.parent_widget.canvas.draw_idle()

        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe

    def pca_plot(self, result_table_list: list):

        if not self.parent_widget.selected_meta_data:
            self.parent_widget.selected_meta_data = ["experiment_name"]

        if self.parent_widget.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, self.explained_ratio = SpecificAnalysisFunctions.pca_calc(result_table_list, self.database_handler)
            self.add_sweep_meta_data_to_result_table(plot_dataframe) # adds series identifier and series meta data
            self.parent_widget.holded_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
        else:
            for ax in self.parent_widget.canvas.figure.axes:
                ax.clear()

        self.parent_widget.holded_dataframe["meta_data"] = self.parent_widget.holded_dataframe[self.parent_widget.selected_meta_data].astype(str).agg('::'.join, axis=1)
        self.scatter_plot_make(self.parent_widget.holded_dataframe, self.explained_ratio)

        self.parent_widget.canvas.draw_idle()
        self.parent_widget.export_data_frame = self.parent_widget.holded_dataframe
        self.parent_widget.statistics = self.parent_widget.holded_dataframe

    def simple_plot_make(self,plot_dataframe, value = "Voltage", increment = None):
        """Makes either a boxplot if increment is indicating no step protocol


        Args:
            plot_dataframe (_type_): dataframe holding data that fits the natures of a box plot or a line plot
            increment (_type_): should indicate if step protocol was use, if None step protocol was used else single step

        Returns:
            pd.DataFrame: Pivoted dataframe having columns either as experiment name or as metadata name
        """
        self.logger.info("Simple Plot started")

        if increment: # if sweep has no voltage steps --> check naming of thev ariable
            self.logger.info("Simple Plot without voltage steps")
            self.comparison_plot(plot_dataframe)
            try:
                pivoted_table = pd.pivot_table(plot_dataframe, index = ["Sweep_Number"], columns = ["meta_data"], values = "Result")
            except Exception as e:
                print(e)

        else: # if stable voltage dependency
            self.logger.info("Simple Plot with voltage steps")
            self.logger.info(plot_dataframe)
            sns.set_palette("colorblind")
            try:
                if "meta_data" in plot_dataframe.columns:
                   g = sns.lineplot(data = plot_dataframe, x = value, y = "Result", hue = "meta_data", ax = self.parent_widget.ax)
                   pivoted_table =  pd.pivot_table(plot_dataframe, index = [value], columns = ["meta_data"], values = "Result")
                else:
                    g = sns.lineplot(data = plot_dataframe, x = value, y = "Result", hue = "series_meta_data", ax = self.parent_widget.ax)
                    pivoted_table =  pd.pivot_table(plot_dataframe, index = [value], columns = ["series_meta_data"], values = "Result")
            except Exception as e:
                g = sns.lineplot(data = plot_dataframe, x = value, y = "Result", hue = "series_meta_data", ax = self.parent_widget.ax)
                # errorbar=("se", 2) not working with the current seaborn version
            self.parent_widget.connect_hover(g)

        self.parent_widget.ax.autoscale()
        self.parent_widget.canvas.figure.tight_layout()
        self.logger.info("Simple Plot returning")
        
        return pivoted_table
    
    def plot_capacitance(self, plot_dataframe: pd.DataFrame) -> None:
        """_summary_: Plots the capacitance of the cell

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        # check if violin parameter is set then use the violin plots
        #sns.lineplot(data = plot_dataframe, x = "Duration", y = "Result", hue = "meta_data", ax = self.parent_widget.ax)
        sns.set_palette("colorblind")
        if self.parent_widget.selected_meta_data == ["experiment_name"]:
            sns.boxplot(data = plot_dataframe, x = "Duration", y = "Result", ax = self.parent_widget.ax)
        else:
            sns.boxplot(data = plot_dataframe, x = "Duration", y = "Result", hue = "meta_data", ax = self.parent_widget.ax)

    def comparison_plot(self, plot_dataframe: pd.DataFrame) -> None:
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

    def violin_plot_maker(self, plot_dataframe: pd.DataFrame) -> None:
        """_summary_: Draws a Violin and a Swarmplot from the data

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        sns.set_palette("colorblind")
        g = sns.violinplot(data = plot_dataframe,
                    x="meta_data",
                    y = "Result",
                    ax = self.parent_widget.ax,
                    width = 0.5)

        self.swarm_plot(plot_dataframe, 10, g)

    def box_plot_maker(self, plot_dataframe: pd.DataFrame) -> None:
        """_summary_: Draws a boxplot and a Swarmplot from the data

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        sns.set_palette("colorblind")
        sns.boxplot(data = plot_dataframe,
                    x="meta_data",
                    y = "Result",
                    ax = self.parent_widget.ax,
                    width = 0.5)
        self.parent_widget.ax.tick_params(axis='x', rotation=45)

    # TODO Rename this here and in `violin_plot_maker` and `box_plot_maker`
    def swarm_plot(self, plot_dataframe: pd.DataFrame, size: int, g) -> None:
        sns.set_palette("colorblind")
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


    def scatter_plot_make(self, plot_dataframe: pd.DataFrame, explaind_ratios:list = None) -> None:
        """_summary_: Creates a scatter plot from the data
        plot_dataframe needs to have the columns PC1 and PC2
        explaind_ratios is a list of the explained ratios of the first two components"""
        
        sns.set_palette("colorblind")
        scatter_plot = sns.scatterplot(x = "PC1", y = "PC2", data = plot_dataframe, hue = "meta_data", ax = self.parent_widget.ax, s = 50, linewidth = False)
        
        if explaind_ratios:
            self.parent_widget.ax.set_xlabel(f"PC1: {str(round(explaind_ratios[0],3))}")
            self.parent_widget.ax.set_ylabel(f"PC2: {str(round(explaind_ratios[1],3))}")
        sns.move_legend(self.parent_widget.ax, "upper left", bbox_to_anchor=(1, 1))
       
        # Add hover information using mplcursors
        scatter_cursor = cursor(scatter_plot, hover=True)
        
        scatter_cursor.connect("add", lambda sel: sel.annotation.set_text(
            f"Experiment: {plot_dataframe['experiment_name'].iloc[sel.index]}\n"
        ))

        # Customize the appearance of the hover box using sel
        scatter_cursor.connect("add", lambda sel: sel.annotation.set_bbox(
            dict(boxstyle='round', facecolor='white', edgecolor='black')
        ))

        self.parent_widget.canvas.figure.tight_layout()

    


         # Add hoverinfo using ax.text
        #for index, row in plot_dataframe.iterrows():
        #    self.parent_widget.ax.text(row["PC1"], row["PC2"], f"{row['experiment_name']}\nPC1: {row['PC1']}\nPC2: {row['PC2']}", fontsize=8)


    def line_boxplot(self, plot_dataframe: pd.DataFrame):
        """_summary_: Creates a line plot with boxplots

        Args:
            plot_dataframe (_type_): _description_
        """
        sns.set_palette("colorblind")
        sns.lineplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "meta_data", ax = self.parent_widget.ax, legend = False)
        # @todo: statannotations requires a seaborn version < 0.12 but <0.12 does not have the errobar function
        #errorbar=("se", 2),

        self.parent_widget.canvas.figure.tight_layout()
        self.parent_widget.ax.autoscale()


    def hue_regplot(self,data, x, y, hue, palette=None, **kwargs):
        """Draw a scatterplot with regression line for each unique value of a column."""
        levels = data[hue].unique()
        if palette is None:
            default_colors = get_cmap('tab10')
            palette = {k: default_colors(i) for i, k in enumerate(levels)}
        sns.set_palette("colorblind")
        return [
            sns.regplot(
                x=x, y=y, data=data[data[hue] == key], color=palette[key], **kwargs
            )
            for key in levels
        ]

    ################################################################################
    # Upload Data Controls
    ################################################################################

    def add_data_frame_to_result_dictionary(self, dataframe: pd.DataFrame) -> None:
        """_summary_ Should add the dataframe to the result dictionary

        Args:
            dataframe (_type_): _description_
        """
        dataframe["analysis_id"] = self.database_handler.analysis_id
        self.result_holder.append(dataframe)
