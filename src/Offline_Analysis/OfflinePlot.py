from matplotlib.backends.backend_qtagg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Offline_Analysis.Analysis_Functions.Function_Templates.SpecificAnalysisCalculations import SpecificAnalysisFunctions
import logging

class OfflinePlots():
    
    logger = logging.getLogger(__name__)
    """Class to handle the Plot Drawing and Calculations for the Offline Analysis
    Basis Analysis Functions
    """
    def __init__(self,
                 parent_widget, 
                 analysis_function: str, 
                 canvas, 
                 result_table_list: list, 
                 database_handler, 
                 frontend, 
                 SeriesItem, 
                 offline_analysis_widget,
                 final_result_holder):
        
        """Initializing the Plotting class with canvas and axis

        Args:
            parent_widget (_type_): _description_
            analysis_function (str): The Function that should be used for plot drawing
            canvas (FigureCanvas): FigureCanvas where the plot should drawn in
            result_table_list (list): Analysis Function Result Table names
            database_handler (duckdb): DataBase Handler
            frontend (Frontend_Style): Frontend_Style Class that handles dark-light mode
            final_result_holder: ResultHolder Class that holds the Final Output Data of the Offline Analysis

        """
        self.SeriesItems = SeriesItem
        self.frontend = frontend
        self.canvas = canvas
        self.violin = None # should be set if violinplot should be run
        self.ax = self.canvas.figure.subplots()
        self.frontend.ax.append(self.ax)
        self.frontend.canvas = self.canvas
        self.current_meta_data_column = None
        
        # reference the needed classes
        self.offline_analysis_widget = offline_analysis_widget
        self.database_handler = database_handler
        self.result_holder = final_result_holder.analysis_result_dictionary
        self.custom_plot = None
        self.holded_dataframe = None
        self.style_plot()
        self.retrieve_analysis_function(parent_widget, result_table_list, analysis_function)
        self.set_logger()
         # this retrieves the dictionary to fill the data in
        # This should be implemented for the result tables to be integrated into the DataBase
      
    
    def set_logger(self):
        """Sets the logger for the Offline Analyiss Plotting
        """
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler("offline_plots.log")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    
    def retrieve_analysis_function(self, parent_widget, result_table_list, analysis_function):
        """Retrieves the appropriate Analysis Function

        Args:
            parent_widget (_type_): The Parent Widget to draw in as canvas
            result_table_list (_type_): The tables that will be visualized for the specific series
            analysis_function (_type_): The analysis function choosen for the specific series
        """
        self.logger.info("Retrieving analysis function")
        # code goes here
        
        
        self.plot_dictionary = {"Boxplot": self.make_boxplot,
                                "No Split": self.simple_plot, 
                                "Split by Meta Data": self.plot_mean_per_meta_data,
                                "Rheobase Plot": self.rheobase_plot,
                                "Sweep Plot": self.single_rheobase_plot,
                                "Rheoramp-AUC": self.rheoramp_plot,
                                "Rheoramp-Single": self.rheoramp_single_plot,
                                "Action Potential Fitting": self.ap_fitting_plot,
                                "Linear Regression": self.regression_plot,
                                "PCA Plot": self.pca_plot
                                }

    # retrieve the appropiate plot from the combobox
        if analysis_function == "Violinplot":
            self.violin = True
        selected_meta_data = self.database_handler.get_selected_meta_data()
        self.plot_dictionary.get(analysis_function)(parent_widget, result_table_list, selected_meta_data)
        self.logger.info(f"Analysis function retrieved successfully {analysis_function}")
        
    def style_plot(self):
        
        """Plot Styling Class, this can be used for general changes of the plot visualization
        """
        self.logger.info("Styling the Plot started")
        self.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.ax.spines.right.set_visible(False)
        self.ax.spines.top.set_visible(False)
        self.ax.patch.set_alpha(0)
        self.canvas.figure.patch.set_alpha(0)
        self.frontend.change_canvas_dark()
        self.logger.info("Styling the Plot ended")

    def make_boxplot(self,parent_widget, result_table_list: list, selected_meta_data = None):
        
        """Specific Function to draw Boxplots from long table formats
        of different Analysis Function

        Args:
            parent_widget (_type_): _description_
            result_table_list (list): Result Table List of the specific Analysis Function
        """

        if self.holded_dataframe is not None:
            boxplot_df = SpecificAnalysisFunctions.boxplot_calc(result_table_list, self.database_handler)
            
            if selected_meta_data:
                boxplot_df["meta_data"] = boxplot_df[selected_meta_data].agg('::'.join, axis=1)
            else:
                boxplot_df["meta_data"] = boxplot_df["experiment_name"]

            self.boxplot_from_template(parent_widget, boxplot_df)

        else:

            self.boxplot_from_template(parent_widget, boxplot_df)

    def boxplot_from_template(self, parent_widget, boxplot_df):
        """Creates a boxplot from a template

        Args:
            boxplot_df (_type_): _description_
        """
         if self.violin:
                sns.violinplot(data = boxplot_df, 
                    x="meta_data", 
                    y = "values",  
                    ax = self.ax, 
                    width = 0.5)
        else:
            sns.boxplot(data = boxplot_df, 
                        x="meta_data", 
                        y = "values",  
                        ax = self.ax, 
                        width = 0.5)
        
        sns.swarmplot(data = boxplot_df, 
                      x="meta_data", 
                      y = "values",  
                      ax = self.ax, 
                      color = "black", 
                      size = 10)
        
        self.logger.info("Created Boxplot successfully")
        self.canvas.figure.tight_layout()
        parent_widget.export_data_frame = boxplot_df
        self.add_data_frame_to_result_dictionary(boxplot_df)


    def simple_plot(self, parent_widget, result_table_list:list, selected_meta_data = None):
        """
        Plot all data without incorporating meta data groups
        :param parent_widget: the widget to which the plot is added
        :param result_table_list: the list of result tables for the specific analysis
        """
        # retrieve the plot_dataframe
        plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
        print(plot_dataframe.shape)
        if increment: # if sweep have different voltage steps indicated by increment in pgf file
            g = sns.boxplot(data = plot_dataframe, x = "name", y = "values", ax = self.ax)
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            try: 
                pivoted_table = plot_dataframe.pivot(index = "index", columns = "name", values = "values")
            except:
                pivoted_table = plot_dataframe
            
        else: # if stable voltage dependency
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "name", ax = self.ax)
            self.connect_hover(g)
            try:
                pivoted_table = plot_dataframe.pivot(index = "Unit", columns = "name", values = "values")
            except:
                pivoted_table = plot_dataframe
        
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.ax.autoscale()
        self.canvas.figure.tight_layout()

        parent_widget.export_data_frame = pivoted_table

    def plot_mean_per_meta_data(self, parent_widget, result_table_list: list, selected_meta_data = None):
        """
        Plot all data together into one specific analysis plot widget without any differentiation between meta data groups
        :param parent_widget: the widget to which the plot is added
        :param result_table_list: the list of result tables for the specific analysis
        """
        plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)

        if increment: # increment describes the differences between a step and a stable protocol
            grouped_dataframe = plot_dataframe.groupby(["meta_data", "name", "index"]).mean("values").reset_index()
            g = sns.boxplot(data = grouped_dataframe, x = "meta_data", y = "values", ax = self.ax)
            sns.swarmplot(data = grouped_dataframe, x = "meta_data", y = "values", ax = self.ax, color = "black", size = 5)
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            self.canvas.figure.tight_layout()
            self.ax.autoscale()
            pivoted_table = grouped_dataframe.pivot(index = "index", columns = "meta_data", values = "values")
            
        else:
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "meta_data", ax = self.ax, errorbar=("se", 2))
            self.canvas.figure.tight_layout()
            self.ax.autoscale()
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            self.connect_hover(g)
            
            grouped_dataframe = plot_dataframe.groupby(["meta_data", "Unit"]).mean("values").reset_index()
            pivoted_table = grouped_dataframe.pivot(index = "Unit", columns = "meta_data", values = "values").reset_index()
        
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.ax.autoscale()
        self.canvas.figure.tight_layout()

        parent_widget.export_data_frame = pivoted_table

    def rheobase_plot(self, parent_widget, result_table_list:list, selected_meta_data = None):
        """Plotting Function to draw rheobase boxplot into the OfflineAnalysisResultAnalyzer

        Args:
            parent_widget (ResultVisualizer): _description_
            result_table_list (list): Result Table list of the generate by the Analysis Function
        """
        
        plot_dataframe = SpecificAnalysisFunctions.rheobase_calc(result_table_list, self.database_handler)
        
        g = sns.boxplot(data = plot_dataframe, x = "Meta_data", y = "AP", ax = self.ax)
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.ax.autoscale()
        self.canvas.figure.tight_layout()
        parent_widget.export_data_frame = plot_dataframe
        
    def single_rheobase_plot(self, parent_widget, result_table_list:list, selected_meta_data = None):
        """Creates Plots for single rheobase calculation --> stepplot

        Args:
            parent_widget (_type_): Class Widget to Plot in 
            result_table_list (_type_): List of Rheobase Result Tables
        """
        plot_dataframe = SpecificAnalysisFunctions.sweep_rheobase_calc(result_table_list, self.database_handler)
        g = sns.lineplot(data = plot_dataframe, x = "current", y = "voltage", hue = "Meta_data", ax = self.ax, errorbar=("se", 2))
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        
        self.ax.autoscale()
        self.canvas.figure.tight_layout()
        parent_widget.export_data_frame = plot_dataframe

    def rheoramp_plot(self, parent_widget, result_table_list: list, selected_meta_data = None):
        """Creates Lineplot and boxplot for Rheoramp Protocols

        Args:
            parent_widget (_type_): _description_
            result_table_list (list): Result Table list for Rheoramp Analysis
        """
        plot_dataframe = SpecificAnalysisFunctions.rheoramp_calc(result_table_list, self.database_handler)
        
        g = sns.lineplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "Meta_data", ax = self.ax, errorbar=("se", 2))
        sns.boxplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "Meta_data", ax = self.ax)
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.canvas.figure.tight_layout()
        self.ax.autoscale()
        parent_widget.export_data_frame = plot_dataframe

    def rheoramp_single_plot(self, parent_widget, result_table_list, selected_meta_data = None):
        """_summary_

        Args:
            parent_widget_ (_type_): Analysis Function parent widget
            result_table_list (list): Rheoramp result tables where _max is for single analysis
            
        """
        plot_dataframe = SpecificAnalysisFunctions.rheoramp_calc(result_table_list, self.database_handler)
        g = sns.lineplot(data = plot_dataframe,
                        x = "Rheoramp", 
                        y = "Number AP", 
                        hue = "experiment_name", 
                        ax = self.ax, 
                        picker= 4
                        )
        
        self.connect_hover(g)
        self.canvas.figure.tight_layout()
        self.ax.autoscale()
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        parent_widget.export_data_frame = plot_dataframe

    def ap_fitting_plot(self, parent_widget, result_table_list: list, selected_meta_data = None):
        """Should Create the Heatmap for each Fitting Parameter
        calculated by the APFitting Procedure
        
        Args:
            parent_widget (_type_): _description_
            result_table_list (list): List of queried result tables
        """
        plot_dataframe, z_score = SpecificAnalysisFunctions.ap_calc(result_table_list, self.database_handler)
        parent_widget.specific_plot_box.setMinimumHeight(500)
        self.canvas.setMinimumSize(self.canvas.size())
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        
        #parent_widget.specific_plot_box.
        sns.heatmap(data = z_score.T, ax = self.ax)
        self.canvas.figure.tight_layout()
        parent_widget.export_data_frame = plot_dataframe
       
    def regression_plot(self, parent_widget, result_table_list: list, selected_meta_data = None):
        """Draws a Regression line which determines the slope of the 

        Args:
            parent_widget (_type_): _description_
            result_table_list (list): _description_
        """
        plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
        g = sns.regplot(data = plot_dataframe, x = "Unit", y = "values", ax = self.ax, fit_reg = True, robust = True)
        g.set_xticklabels(g.get_xticklabels(),rotation=45)
        parent_widget.export_data_frame = plot_dataframe
    
    def pca_plot(self, parent_widget, result_table_list: list, selected_meta_data = None):
        print("needs to be implemented")
    
    def on_click(self, event, annot):
        """Event Detection in the Matplotlib Plot
        
        Args:
            event (mpl_connect_event): Event Connection via hovering motion notify
            annot (ax.annotate): Annotations of the axis
        
        """
        for line in self.ax.lines:
            #check if the selected line is drawn
            if line.contains(event)[0]:
                cont, ind = line.contains(event)
                line.set_linewidth(6)
                self.update_annot(ind,annot,line)
                annot.set_visible(True)
                self.canvas.draw_idle()
            else:
                line.set_linewidth(1)
                self.canvas.draw_idle()
    
    def update_annot(self, ind: tuple, annot, line):
        """Annotation Update for visualization of the lineplot name
        when hovering

        Args:
            ind (tuple): _description_
            annot (_type_): _description_
            line (_type_): _description_
        """
        x,y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        index_line = line.axes.get_lines().index(line)
        name = line.axes.get_legend().texts[index_line].get_text()
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                            " ".join([name for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)
        
    def connect_hover(self, plot):
        """Function to connect the plot with the on_click function

        Args:
            plot (seaborn plot): seaborn plot (g) which should be connected
        """
        self.ax.legend().set_visible(False)
        
        annot = self.ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        
        plot.figure.canvas.mpl_connect("motion_notify_event", 
                                    lambda event: self.on_click(event, 
                                                                annot
                                                                ))
        plot.figure.canvas.mpl_connect("button_press_event",self.on_pick)

    def on_pick(self, event):
        """Event Detection in the Matplotlib Plot to retrieve the Experiment from the TreeView
        
        Args:
            event (mpl_connect_event): Event Connection via button pressing"""
        for line in self.ax.lines:
            if line.contains(event)[0]:
                index_line = line.axes.get_lines().index(line)
                name = line.axes.get_legend().texts[index_line].get_text()
                self.SeriesItems.setCurrentItem(self.SeriesItems.selectedItems()[0].parent().child(0))
                self.offline_analysis_widget.offline_analysis_result_tree_item_clicked()

    def add_data_frame_to_result_dictionary(self, dataframe: pd.DataFrame):
        """_summary_

        Args:
            dataframe (_type_): _description_
        """
        dataframe["analysis_id"] = self.database_handler.analysis_id
        self.result_holder.append(dataframe)              
        