from matplotlib.backends.backend_qtagg import (NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from Offline_Analysis.Analysis_Functions.Function_Templates.SpecificAnalysisCalculations import SpecificAnalysisFunctions
import logging
from numpy import nan
from matplotlib.cm import get_cmap

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
        self.violin = None # should be set if violinplot should be run
        self.canvas = None # The Figure canvas that is drawn
        self.ax = None # the axis of the canvas
        self.holded_dataframe = None
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
    
    def set_frontend_axes(self, canvas):
        """_summary_: This function should set the axis and teh figure of the canvas
        and assign this as instance member

        Args:
            canvas (Figure Canvas): Matplotlib Figure Canvas holding the plot
        """
        
        self.canvas = canvas
        self.ax = self.canvas.figure.subplots()
        self.frontend.ax.append(self.ax)
        self.frontend.canvas = self.canvas 
        self.style_plot()

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
    
    def retrieve_analysis_function(self,parent_widget= None, result_table_list = None, analysis_function_id = None, switch = None):
        """Retrieves the appropriate Analysis Function, sets the parent widget as instance variable
        retrieves the analysis function id from from parent widget and also evaluate the swithc

        Args:
            self.parent_widget (_type_): The Parent Widget to draw in as canvas
            result_table_list (_type_): The tables that will be visualized for the specific series
            analysis_function (_type_): The analysis function choosen for the specific series
            switch (bool): Should indicate if redraw without 
        """
        self.logger.info("Retrieving analysis function")
        # code goes here
        
        if switch:
            self.holded_dataframe = None
 
        if not self.parent_widget:
            self.parent_widget = parent_widget
            
        analysis_function = self.parent_widget.plot_type_combo_box.currentText()
        
        # should retrieve the right function based on the selected analysis function
        self.plot_dictionary = {"Boxplot": self.make_boxplot,
                                "No Split": self.simple_plot, 
                                "Rheobase Plot": self.rheobase_plot,
                                "Sweep Plot": self.single_rheobase_plot,
                                "Rheoramp-AUC": self.rheoramp_plot,
                                "Action Potential Fitting": self.ap_fitting_plot,
                                "Linear Regression": self.regression_plot,
                                "PCA-Plot": self.pca_plot
                                }

        # retrieve the appropiate plot from the combobox
        if analysis_function == "Violinplot":
            self.violin = True

        try:    
            selected_meta_data = self.database_handler.get_selected_meta_data(analysis_function_id)
        except Exception as e:
            selected_meta_data = None

        try:
            self.plot_dictionary.get(analysis_function)(result_table_list, selected_meta_data)
        except Exception as e:
            self.logger.error(f"Analysis function could not be retrieved {e}")
            raise KeyError(f"Analysis function could not be retrieved {e}")	
        
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
        self.frontend.change_canvas_bright()
        self.logger.info("Styling the Plot ended")

    def make_boxplot(self,result_table_list: list, selected_meta_data = None):

        """Specific Function to draw Boxplots from long table formats
        of different Analysis Function

        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): Result Table List of the specific Analysis Function
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            plot_dataframe = SpecificAnalysisFunctions.boxplot_calc(result_table_list, self.database_handler)
            self.merge_meta_plot_and_assign_meta(plot_dataframe, selected_meta_data)
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.comparison_plot(self.holded_dataframe)
            for ax in self.canvas.figure.axes:
                ax.clear()  
            self.canvas.draw()

        self.canvas.figure.tight_layout()
        self.logger.info("Created Boxplot successfully")
        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe
        self.add_data_frame_to_result_dictionary(self.holded_dataframe)

    
    def simple_plot(self, result_table_list:list, selected_meta_data = None):
        """
        Plot all data without incorporating meta data groups
        :param self.parent_widget: the widget to which the plot is added
        :param result_table_list: the list of result tables for the specific analysis
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
            pivoted_table = self.simple_plot_make(plot_dataframe, increment)
            self.increment = increment
            self.holded_dataframe = plot_dataframe
        
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear()  
            pivoted_table = self.simple_plot_make(self.holded_dataframe, self.increment)
            
            self.canvas.draw()
        
        #plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        
        self.parent_widget.export_data_frame = pivoted_table
        self.parent_widget.statistics = self.holded_dataframe

                
    def rheobase_plot(self, result_table_list:list, selected_meta_data = None):
        """Plotting Function to draw rheobase boxplot into the OfflineAnalysisResultAnalyzer

        Args:
            self.parent_widget (ResultVisualizer): _description_
            result_table_list (list): Result Table list of the generate by the Analysis Function
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.rheobase_calc(result_table_list, self.database_handler)
            self.merge_meta_plot_and_assign_meta(plot_dataframe, selected_meta_data)
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear() 
            self.comparison_plot(self.holded_dataframe)
            self.canvas.draw()

        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe


    def merge_meta_plot_and_assign_meta(self, plot_dataframe: pd.DataFrame, selected_meta_data: list):
        """_summary_

        Args:
            plot_dataframe (pd.DataFrame): _description_
            selected_meta_data (list): _description_
        """
        plot_dataframe = pd.merge(
            plot_dataframe,
            self.meta_data,
            left_on="experiment_name",
            right_on="experiment_name",
            how="left",
        )
        plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg(
            '::'.join, axis=1
        )
        self.comparison_plot(plot_dataframe)
        self.holded_dataframe = plot_dataframe
        
    def single_rheobase_plot(self, result_table_list:list, selected_meta_data = None):
        """Creates Plots for single rheobase calculation --> stepplot

        Args:
            self.parent_widget (_type_): Class Widget to Plot in 
            result_table_list (_type_): List of Rheobase Result Tables
        """
        if not selected_meta_data:
                selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.sweep_rheobase_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.simple_plot_make(plot_dataframe)
            self.holded_dataframe = plot_dataframe
        
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear() 
            self.simple_plot_make(self.holded_dataframe)
            self.canvas.draw()
        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe
        
        

    def rheoramp_plot(self, result_table_list: list, selected_meta_data = None):
        """Creates Lineplot and boxplot for Rheoramp Protocols

        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): Result Table list for Rheoramp Analysis
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe = SpecificAnalysisFunctions.rheoramp_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.line_boxplot(plot_dataframe)
            self.holded_dataframe = plot_dataframe
        
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear() 
            self.line_boxplot(self.holded_dataframe)
            self.canvas.draw()

        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe



    def ap_fitting_plot(self, result_table_list: list, selected_meta_data = None, agg = False):
        """Should Create the Heatmap for each Fitting Parameter
        calculated by the APFitting Procedure
        
        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): List of queried result tables
            selected_meta_data (str, optional): Meta Data to be used for aggregation. Defaults to None.
            agg (bool, optional): If True, the data will be aggregated by the selected meta data. Defaults to False.
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            statitics_dataframe, plot_dataframe = SpecificAnalysisFunctions.ap_calc(result_table_list, self.database_handler)
            self.statistics = statitics_dataframe
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.holded_dataframe = plot_dataframe
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.holded_daataframe = self.holded_dataframe.sort_values(by = ["meta_data", "experiment_name"])
            for ax in self.canvas.figure.axes:
                ax.clear() 


        self.parent_widget.specific_plot_box.setMinimumHeight(500)
        self.canvas.setMinimumSize(self.canvas.size())
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        drawing_data = self.holded_dataframe[self.statistics.columns[1:-1]].T
        sns.heatmap(data = drawing_data, ax = self.ax)
        self.canvas.figure.tight_layout()
        self.parent_widget.export_data_frame = self.statistics
        self.parent_widget.statistics = self.holded_dataframe
       
    def regression_plot(self, result_table_list: list, selected_meta_data = None):
        """Draws a Regression line which determines the slope of the 

        Args:
            self.parent_widget (_type_): _description_
            result_table_list (list): _description_
        """
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"]

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, increment = SpecificAnalysisFunctions.simple_plot_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
            self.hue_regplot(data=plot_dataframe, x='index', y='values', hue='meta_data', ax=self.ax)
            self.holded_dataframe = plot_dataframe


        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear() 
            self.hue_regplot(data=self.holded_dataframe, x='index', y='values', hue='meta_data', ax=self.ax)
            self.canvas.draw()

        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe
    
    def pca_plot(self, result_table_list: list, selected_meta_data = None):
         
        if not selected_meta_data:
            selected_meta_data = ["experiment_name"] 

        if self.holded_dataframe is None:
            # retrieve the plot_dataframe
            plot_dataframe, self.explained_ratio = SpecificAnalysisFunctions.pca_calc(result_table_list, self.database_handler)
            plot_dataframe = pd.merge(plot_dataframe, self.meta_data, left_on = "experiment_name", right_on = "experiment_name", how = "left")
            plot_dataframe["meta_data"] = plot_dataframe[selected_meta_data].agg('::'.join, axis=1)
          
                
            self.scatter_plot_make(plot_dataframe, self.explained_ratio)
            self.holded_dataframe = plot_dataframe
        
        else:
            self.holded_dataframe["meta_data"] = self.holded_dataframe[selected_meta_data].agg('::'.join, axis=1)
            for ax in self.canvas.figure.axes:
                ax.clear() 
            self.scatter_plot_make(self.holded_dataframe, self.explained_ratio)
            self.canvas.draw()

        self.parent_widget.export_data_frame = self.holded_dataframe
        self.parent_widget.statistics = self.holded_dataframe
  
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
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "meta_data", ax = self.ax,  errorbar=("se", 2))
            self.connect_hover(g)
            try:
                pivoted_table =  pd.pivot_table(plot_dataframe, index = ["Unit"], columns = ["meta_data"], values = "values")
            except Exception as e:
                print(e)
        
        self.ax.autoscale()
        self.canvas.figure.tight_layout()        
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
                    ax = self.ax, 
                    width = 0.5)
                
        z = sns.swarmplot(data = plot_dataframe, 
                x="meta_data", 
                y = "values",  
                ax = self.ax, 
                color = self.color, 
                size = 10)
        
        g.set_xticklabels(g.get_xticklabels(),rotation=45)
        z.set_xticklabels(g.get_xticklabels(),rotation=45)
        
    def box_plot_maker(self, plot_dataframe):
        """_summary_: Draws a boxplot and a Swarmplot from the data

        Args:
            plot_dataframe (pd.DataFrame): DataFrame long format holding result data
        """
        g = sns.boxplot(data = plot_dataframe, 
                    x="meta_data", 
                    y = "values",  
                    ax = self.ax, 
                    width = 0.5)

        z = sns.swarmplot(data = plot_dataframe, 
                    x="meta_data", 
                    y = "values",  
                    ax = self.ax, 
                    color = self.color, 
                    size = 2) 
        
        g.set_xticklabels(g.get_xticklabels(),rotation=45)
        z.set_xticklabels(g.get_xticklabels(),rotation=45)


    def scatter_plot_make(self, plot_dataframe, explaind_ratios = None):
        """_summary_: Creates a scatter plot from the data"""
        sns.scatterplot(x = "PC1", y = "PC2", data = plot_dataframe, hue = "meta_data", ax = self.ax)
        if explaind_ratios:
            self.ax.set_xlabel(f"PC1: {str(explaind_ratios[0])}")
            self.ax.set_ylabel(f"PC2: {str(explaind_ratios[1])}")


    def line_boxplot(self, plot_dataframe):
        """_summary_: Creates a line plot with boxplots

        Args:
            plot_dataframe (_type_): _description_
        """
        g = sns.lineplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "meta_data", ax = self.ax, errorbar=("se", 2), legend = False)
        sns.boxplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "meta_data", ax = self.ax)
        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.canvas.figure.tight_layout()
        self.ax.autoscale()


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
    # Hovering Functions: and Plot Controls
    ################################################################################

      
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
        text = f'{" ".join(list(map(str, ind["ind"])))}, {" ".join([name for _ in ind["ind"]])}'
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
                self.offline_tree.SeriesItems.setCurrentItem(self.SeriesItems.selectedItems()[0].parent().child(0))
                self.offline_tree.offline_tree.offline_analysis_result_tree_item_clicked()


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
        
