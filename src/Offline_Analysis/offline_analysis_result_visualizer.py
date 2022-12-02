import sys
import os
from QT_GUI.OfflineAnalysis.CustomWidget.specific_visualization_plot import ResultPlotVisualizer
from database.data_db import DuckDBDatabaseHandler
from functools import partial
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import *

from QT_GUI.OfflineAnalysis.CustomWidget.tab_offline_result import OfflineResultTab
from Offline_Analysis.OfflinePlot import OfflinePlots

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore



class OfflineAnalysisResultVisualizer():
    """
    Class to handle GUI interaction between user and visualization tab to display offline analysis results
    @author dz, 13.07.2022
    """

    def __init__(self, visualization_tab_widget, database: DuckDBDatabaseHandler, offline_analysis_widget):

        self.frontend_style = None
        self.visualization_tab_widget = visualization_tab_widget
        self.database_handler = database
        self.result_directory = ""
        self.series_wise_function_list = ["Single_AP_Amplitude [mV]", "Single_AP_Threshold_Amplitude[mV]",
                    "Single_AP_Afterhyperpolarization_Amplitude [mV]", "Single_AP_Afterhyperpolarization_time[ms], Rheobase_Detection"]
        self.canvas = None
        self.offline_analysis_widget = offline_analysis_widget


    def show_results_for_current_analysis(self,analysis_id: int, series_name = None):
        """
        1) Identify the number of series (e.g. IV, Block Pulse, .. and create tabs for each analyzed series
        @param analysis_id: offline analysis id: id of the current analysis
        @param series_name: specific series name that can be none
        @author dz, 13.07.2022
        """

        q = """select analysis_series_name from analysis_series where analysis_id = (?)"""
        list_of_series = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                        [analysis_id])

        print(list_of_series)

        for series in list_of_series:
            print(series)
            # create visualization for each specific series in specific tabs
            # print("running analysis")
            if series[0] == series_name:
                print(analysis_id)
                print(series_name)
                offline_tab = self.analysis_function_specific_visualization(series[0],analysis_id)
                print(offline_tab)
                return offline_tab
            else:
                print("no analysis function selected")


    def analysis_function_specific_visualization(self,series,analysis_id):
        """
        Function to identify the amount of analysis functions (different functions) per series ( = plots per tab)
        @param series:
        @param analysis_id:
         @author dz, 13.07.2022
        """

        # series name e.g. IV
        q = """select distinct analysis_function_id from analysis_functions where analysis_id = (?) and analysis_series_name =(?)"""
        list_of_analysis = self.database_handler.get_data_from_database(self.database_handler.database, q, (analysis_id,series))

        # print("series= " + series)
        # print("list of analysis")
        # print(list_of_analysis)
        # e.g. [(43,), (45,), (47,)]

        offline_tab = OfflineResultTab()
        offline_tab.OfflineScroll.setStyleSheet("background-color: rgba(0,0,0,0")

        for analysis in list_of_analysis:

            # create new custom plot visualizer and parametrize data
            custom_plot_widget = ResultPlotVisualizer()

            custom_plot_widget.analysis_id = analysis_id
            custom_plot_widget.analysis_function_id = analysis[0]
            custom_plot_widget.series_name = series

            analysis_name = self.database_handler.get_analysis_function_name_from_id(analysis[0])
            custom_plot_widget.analysis_name = analysis_name

            custom_plot_widget.analysis_name = analysis_name

            custom_plot_widget.specific_plot_box.setTitle("Analysis: " + analysis_name)

            custom_plot_widget.save_plot_button.clicked.connect(partial(self.save_plot_as_image, custom_plot_widget))
            custom_plot_widget.export_data_button.clicked.connect(partial(self.export_plot_data,custom_plot_widget))

            # fill the plot widget with analysis specific data
            self.single_analysis_visualization(custom_plot_widget)

            # widgets per row = 2

            widget_x_pos = list_of_analysis.index(analysis) // 1#1  # 2 widgets per row
            widgte_y_pos = list_of_analysis.index(analysis) % 1# 1 # 2 widgets per row

            print("x pos widget = ", widget_x_pos)
            print("y pos widget = ", widgte_y_pos)
            offline_tab.OfflineResultGrid.addWidget(custom_plot_widget, widget_x_pos, widgte_y_pos)

        # after all plots have been added

        return offline_tab

    def single_analysis_visualization(self,parent_widget,plot_type=None):
        """
        For each specific analysis function a new custom widget will be created and filled with available results
        from the database
        @param parent_widget:
        @param plot_type:
        @author dz, 13.07.2022
        """
        # get the class object name for this analysis
        class_object = AnalysisFunctionRegistration().get_registered_analysis_class(parent_widget.analysis_name)
        self.canvas = self.handle_plot_widget_settings(parent_widget, class_object().plot_type_options)

        if plot_type is None:
            #if class_object.database is None:
            #    print("I am setting the database")
            class_object.database = self.database_handler
            result_table_names = class_object.visualize_results(parent_widget, self.canvas, class_object().plot_type_options[0])
            if result_table_names:
                plot_type = class_object().plot_type_options[0]
            else:
                plot_type = None
        else:
            result_table_names = class_object.visualize_results(parent_widget, self.canvas, plot_type)
            if result_table_names:
                plot_type = plot_type
            else:
                plot_type = None

        OfflinePlots(parent_widget, plot_type, self.canvas, result_table_names, self.database_handler, self.frontend_style, self.visualization_tab_widget, self.offline_analysis_widget)
    

    def handle_plot_widget_settings(self, parent_widget:ResultPlotVisualizer, plot_type_list):
        """
        Handle the setting of the plot widget, which is inside a custom made widget called parent widget.
        The plot needs to be cleared and combo boxes might need to be initialized.
        @param parent_widget: custom widget class ResultPlotVisualizer
        @param plot_type_list: list of display options to be displayed in the combo box dropdown, such as boxplot, ...
        @author dz, 13.07.2022
        """
        try:
            # print("overriding existing plot widget")

            # remove the old plot if there is one already existing
            for i in reversed(range(parent_widget.plot_layout.count())):
                parent_widget.plot_layout.itemAt(i).widget().deleteLater()
            #parent_widget.plot_layout.takeAt(0)

            # create a new plot and insert it into the already exsiting plot layout
            self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.scroll_area = QScrollArea()
            self.scroll_layout = QGridLayout()


            self.scroll_layout.addWidget(self.canvas)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setWidget(self.canvas)
            parent_widget.plot_layout.addWidget(self.scroll_area)
        

            # add options only once
            try:
                if parent_widget.plot_type_combo_box.currentText() not in plot_type_list:
                    parent_widget.plot_type_combo_box.addItems(plot_type_list)

                    parent_widget.plot_type_combo_box.currentTextChanged.connect(
                        partial(self.plot_type_changed, parent_widget))
            except Exception as e:
                print(str(e))

            return self.canvas

        except Exception as e:
            print(str(e))


    def export_plot_data(self,parent_widget:ResultPlotVisualizer):
        """
        Write the data shown in the plot into a csv file. The data are stored in the export data frame object
        in the parent widget
        @param parent_widget: custom widget class ResultPlotVisualizer
        @author dz, 13.07.2022
        """
        result_directory = QFileDialog.getExistingDirectory()
        try:
            parent_widget.export_data_frame.to_csv(result_directory+"/result_export_analysis_function_id_"
                                                   + str(parent_widget.analysis_function_id) + ".csv")
            print("file stored successfully")
        except Exception as e:
            print("Results were not stored successfully")
            print(e)


    def save_plot_as_image(self,parent_widget:ResultPlotVisualizer):
        """
        Plot the figure as it is shwon in the canvas
        @param parent_widget: custom widget class ResultPlotVisualizer
        @author dz, 13.07.2022
        """
        result_path = QFileDialog.getSaveFileName()[0]
        canvas= parent_widget.plot_layout.itemAt(0).widget()
        canvas.print_figure(result_path)
        #print("saved plot in " + result_path)

    def plot_type_changed(self, parent_widget, new_text):
        """
        Will change the plot type whenever the combo box selected item is changed by the user
        @param parent_widget: custom widget class ResultPlotVisualizer
        @param new_text: item text of the new displayed item in the combo boc
        @author dz, 13.07.2022
        """
        self.single_analysis_visualization(parent_widget,new_text)