from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import SweepWiseAnalysisTemplate
class OfflinePlots():

    def __init__(self,parent_widget, analysis_function, canvas, result_table_list, database_handler, frontend):
        """ plot the results"""
        self.analysis_function = analysis_function
        self.frontend = frontend
        self.canvas = canvas
        self.ax = self.canvas.figure.subplots()
        self.frontend.ax.append(self.ax)
        self.frontend.canvas = self.canvas
        self.style_plot()

        self.plot_dictionary = {"Boxplot": self.make_boxplot,
                                "No Split": self.simple_plot, 
                                "Split by Meta Data": self.plot_mean_per_meta_data,
                                "Rheobase Plot": self.rheobase_plot,
                                "Sweep Plot": self.single_rheobase_plot,
                                "Rheoramp-AUC": self.rheoramp_plot,
                                "Rheoramp-Single": self.rheoramp_single_plot}

        self.database_handler = database_handler
        self.plot_dictionary.get(self.analysis_function)(parent_widget, result_table_list)
        
    def style_plot(self):
        self.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.ax.spines.right.set_visible(False)
        self.ax.spines.top.set_visible(False)
        self.ax.patch.set_alpha(0)
        self.canvas.figure.patch.set_alpha(0)
        self.canvas.figure.tight_layout()
        self.frontend.change_canvas_dark()
        

    def make_boxplot(self,parent_widget, result_table_list):
    
        boxplot_df = SweepWiseAnalysisTemplate.boxplot_calc(result_table_list, self.database_handler)

        # print(filtered_box_plot_data)
        print(boxplot_df)
        sns.boxplot(data = boxplot_df, x="meta_data", y = "values",  ax = self.ax, width = 0.5)
        sns.swarmplot(data = boxplot_df, x="meta_data", y = "values",  ax = self.ax, color = "black", size = 10)
        self.canvas.figure.tight_layout()

        #self.canvas.mpl_connect("button_press_event", self.on_click)
        # self.ax.violinplot(filtered_box_plot_data)
    
        #self.ax.legend(self.plot['boxes'], custom_labels, loc='upper left')

        parent_widget.export_data_frame = pd.DataFrame(boxplot_df)
        parent_widget.export_data_frame = parent_widget.export_data_frame
        #parent_widget.export_data_frame.columns = meta_data_groups
        
    def on_click(self, event):
        """click event for the plot"""
        print(event)
    
    def simple_plot(self, parent_widget, result_table_list):
        """
        Plot all data without incorporating meta data groups
        :param parent_widget: the widget to which the plot is added
        :param result_table_list: the list of result tables for the specific analysis
        """
        plot_dataframe, increment = SweepWiseAnalysisTemplate.simple_plot_calc(result_table_list, self.database_handler)

        if increment:
            g = sns.boxplot(data = plot_dataframe, x = "name", y = "values", ax = self.ax)
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            pivoted_table = plot_dataframe.pivot(index = "index", columns = "name", values = "values")
        else:
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "name", ax = self.ax)
            self.connect_hover(g)
            pivoted_table = plot_dataframe.pivot(index = "Unit", columns = "name", values = "values")
        
        parent_widget.export_data_frame = pivoted_table
        print("succesfully stored data")


    def plot_mean_per_meta_data(self, parent_widget, result_table_list):
        """
        Plot all data together into one specific analysis plot widget without any differentiation between meta data groups
        :param parent_widget: the widget to which the plot is added
        :param result_table_list: the list of result tables for the specific analysis
        """
        plot_dataframe, increment = SweepWiseAnalysisTemplate.simple_plot_calc(result_table_list, self.database_handler)

        if increment:
            grouped_dataframe = plot_dataframe.groupby(["meta_data", "name", "index"]).mean("values").reset_index()
            g = sns.boxplot(data = grouped_dataframe, x = "meta_data", y = "values", ax = self.ax)
            sns.swarmplot(data = grouped_dataframe, x = "meta_data", y = "values", ax = self.ax, color = "black", size = 10)
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            self.canvas.figure.tight_layout()
            pivoted_table = grouped_dataframe.pivot(index = "index", columns = "meta_data", values = "values")
            
        else:
            g = sns.lineplot(data = plot_dataframe, x = "Unit", y = "values", hue = "meta_data", ax = self.ax, errorbar=("se", 2))
            g.set_xticklabels(g.get_xticklabels(),rotation=45)
            self.connect_hover(g)
            
            grouped_dataframe = plot_dataframe.groupby(["meta_data", "Unit"]).mean("values").reset_index()
            pivoted_table = grouped_dataframe.pivot(index = "Unit", columns = "meta_data", values = "values").reset_index()
        
        parent_widget.export_data_frame = pivoted_table

    def rheobase_plot(self, parent_widget, result_table_list):
        """_summary_

        Args:
            parent_widget (_type_): _description_
            result_table_list (_type_): _description_
        """
        plot_dataframe = SweepWiseAnalysisTemplate.rheobase_calc(result_table_list, self.database_handler)
        g = sns.boxplot(data = plot_dataframe, x = "Meta_data", y = "AP", ax = self.ax)
        parent_widget.export_data_frame = plot_dataframe
        
    def single_rheobase_plot(self, parent_widget, result_table_list):
        """_summary_

        Args:
            parent_widget (_type_): _description_
            result_table_list (_type_): _description_
        """
        plot_dataframe = SweepWiseAnalysisTemplate.sweep_rheobase_calc(result_table_list, self.database_handler)
        g = sns.lineplot(data = plot_dataframe, x = "current", y = "voltage", hue = "Meta_data", ax = self.ax, errorbar=("se", 2))
        parent_widget.export_data_frame = plot_dataframe

    def rheoramp_plot(self, parent_widget, result_table_list):
        """_summary_

        Args:
            parent_widget (_type_): _description_
            result_table_list (_type_): _description_
        """
        plot_dataframe = SweepWiseAnalysisTemplate.rheoramp_calc(result_table_list, self.database_handler)
        g = sns.lineplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "Meta_data", ax = self.ax, errorbar=("se", 2))
        sns.boxplot(data = plot_dataframe, x = "Rheoramp", y = "Number AP", hue = "Meta_data", ax = self.ax)
        parent_widget.export_data_frame = plot_dataframe

    def rheoramp_single_plot(self, parent_widget, result_table_list):
        """_summary_

        Args:
            parent_widget_ (_type_): Analysis Function parent widget
            result_table_list (_type_): Rheoramp result tables where _max is for single analysis
            
        """
        plot_dataframe = SweepWiseAnalysisTemplate.rheoramp_calc(result_table_list, self.database_handler)
        g = sns.lineplot(data = plot_dataframe,
                         x = "Rheoramp", 
                         y = "Number AP", 
                         hue = "experiment_name", 
                         ax = self.ax, 
                         picker=4
                         )
        
        self.connect_hover(g)
        
        parent_widget.export_data_frame = plot_dataframe

    def on_click(self, event, annot):
        """hover event for the plot"""
        for line in self.ax.lines:
            if line.contains(event)[0]:
                cont, ind = line.contains(event)
                line.set_linewidth(6)
                self.update_annot(ind,annot,line)
                annot.set_visible(True)
                self.canvas.draw_idle()
            else:
                line.set_linewidth(1)
                self.canvas.draw_idle()
    
    def update_annot(self, ind, annot, line):
        x,y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        index_line = line.axes.get_lines().index(line)
        name = line.axes.get_legend().texts[index_line].get_text()
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                            " ".join([name for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)
        
        
    def connect_hover(self, plot):
        self.ax.legend().set_visible(False)
        
        annot = self.ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        
        plot.figure.canvas.mpl_connect("motion_notify_event", 
                                    lambda event: self.on_click(event, 
                                                                annot
                                                                ))
        