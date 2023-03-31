
from Offline_Analysis.ResultPlotVisualizer import ResultPlotVisualizer
from database.data_db import DuckDBDatabaseHandler
from functools import partial
from PySide6.QtWidgets import *
from matplotlib.figure import Figure
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import *
from matplotlib.backends.backend_qtagg import FigureCanvas
from QT_GUI.OfflineAnalysis.CustomWidget.tab_offline_result import OfflineResultTab
from Offline_Analysis.OfflinePlot import OfflinePlots
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from loggers.offlineplot_logger import offlineplot_logger


class OfflineAnalysisResultVisualizer():
    """
    Class to handle GUI interaction between user and visualization tab to display offline analysis results
    @author dz, 13.07.2022
    """

    def __init__(self,
                 visualization_tab_widget,
                 database: DuckDBDatabaseHandler,
                 final_result_holder,
                 frontend_style,
                 plot_meta_button,
                 splitter):
        """_summary_

        Args:
            visualization_tab_widget (_type_): _description_
            database (DuckDBDatabaseHandler): _description_
            offline_analysis_widget (OfflineAnalysis Class): _description_
        """
        self.frontend_style = frontend_style
        self.visualization_tab_widget = visualization_tab_widget.SeriesItems
        self.offline_tree = visualization_tab_widget
        self.database_handler = database
        self.final_result_holder = final_result_holder
        self.canvas = None
        self.splitter = splitter
        self.offlineplot = OfflinePlots(
                     self.database_handler,
                     self.frontend_style,
                     self.offline_tree,
                     self.final_result_holder)

        self.change_meta_data = plot_meta_button
        self.logger = offlineplot_logger
        self.logger.info("Successfully initialized the Offline Analysis Result Visualizer")


    def show_results_for_current_analysis(self,analysis_id: int, series_name = None):
        """
        1) Identify the number of series (e.g. IV, Block Pulse, .. and create tabs for each analyzed series
        @param analysis_id: offline analysis id: id of the current analysis
        @param series_name: specific series name that can be none
        @author dz, 13.07.2022
        """

        q = """select analysis_series_name from analysis_series where analysis_id = (?)"""

        print(self.database_handler.database.execute("""select analysis_series_name
                                                     from analysis_series
                                                     where analysis_id = 4""").fetchdf())

        list_of_series = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                        [analysis_id])

        for series in list_of_series:
            # create visualization for each specific series in specific tabs
            # print("running analysis")
            if series[0] == series_name:
                return self.analysis_function_specific_visualization(series[0],analysis_id)
            else:
                print("The logger should be added here to show that the series is not available in the database")


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
        parent_list = []
        offline_tab = OfflineResultTab()
        offline_tab.OfflineScroll.setStyleSheet("background-color: rgba(0,0,0,0")

        for analysis in list_of_analysis:

            # create new custom plot visualizer and parametrize data
            custom_plot_widget = ResultPlotVisualizer(self.offline_tree)
            custom_plot_widget.analysis_id = analysis_id
            custom_plot_widget.analysis_function_id = analysis[0]
            custom_plot_widget.series_name = series
            analysis_name = self.database_handler.get_analysis_function_name_from_id(analysis[0])
            custom_plot_widget.analysis_name = analysis_name
            custom_plot_widget.specific_plot_box.setTitle(f"Analysis: {analysis_name}")
            custom_plot_widget.save_plot_button.clicked.connect(partial(self.save_plot_as_image, custom_plot_widget))
            custom_plot_widget.export_data_button.clicked.connect(partial(self.export_plot_data,custom_plot_widget))
            # fill the plot widget with analysis specific data
            analysis_function = self.single_analysis_visualization(custom_plot_widget)
            # widgets per row = 2
            widget_x_pos = list_of_analysis.index(analysis) // 2#1  # 2 widgets per row
            widgte_y_pos = list_of_analysis.index(analysis) % 2# 1 # 2 widgets per row

            self.logger.info(f"Logging the position of the widget x pos widget = {widget_x_pos} ")
            self.logger.info(f"Logging the position of the widget y pos widget = {widgte_y_pos}")
            offline_tab.OfflineResultGrid.addWidget(custom_plot_widget, widget_x_pos+1, widgte_y_pos)
            parent_list.append(custom_plot_widget)


        # after all plots have been added
        self.visualization_tab_widget.currentItem().parent().setData(10, Qt.UserRole, parent_list)
        return offline_tab

    def open_meta_data(self):
        """_summary_: This opens the meta data from the selected meta data table to
        retrieve the the condition columns holding the column string that can be used
        for meta data retrieval in offline plot
        column example: "genotype"

        Args:
            analysis_function (_type_): _description_

        Returns:
            _type_: _description_
        """
        dialog = SelectMetaDataForTreeviewDialog(self.database_handler,
                                                 update_treeview = False,
                                                 update_plot = self.offlineplot,
                                                 analysis_function_id = self.visualization_tab_widget.currentItem().parent().data(8, Qt.UserRole))

        dialog.setWindowTitle("Available Meta Data Label")
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

        parents = self.visualization_tab_widget.currentItem().parent().data(10, Qt.UserRole)
        for parent in parents:
            self.offlineplot.retrieve_analysis_function(parent_widget = parent)
        return None

    def single_analysis_visualization(self,parent_widget,analysis_function=None, switch = None):
        """
        For each specific analysis function a new custom widget will be created and filled with available results
        from the database
        @param parent_widget:
        @param plot_type:
        @author dz, 13.07.2022
        @reworked MZ        """
        # get the class object name for this analysis
        class_object = AnalysisFunctionRegistration().get_registered_analysis_class(parent_widget.analysis_name)()
        self.handle_plot_widget_settings(parent_widget, class_object.plot_type_options)

        if analysis_function is None:
            result_table_names = class_object.visualize_results(parent_widget, self.database_handler)
            if result_table_names:
                self.logger.info("No analysis function specified, retrieving first available analysis function")
                analysis_function = class_object.plot_type_options[0]
            else:
                analysis_function = None
        else:
            result_table_names = class_object.visualize_results(parent_widget,self.database_handler)
            analysis_function = analysis_function if result_table_names else None

        self.offlineplot.set_frontend_axes(parent_widget)
        self.offlineplot.set_metadata_table(result_table_names)

        # switch checks if the current plot type is switched in the combobox within the plot widget
        if switch:
            self.logger.info("Switching plot type, retrieving analysis function")
            self.offlineplot.retrieve_analysis_function(parent_widget = parent_widget,
                                                        result_table_list = result_table_names,
                                                        switch = True)
        else:
            self.offlineplot.retrieve_analysis_function(parent_widget =parent_widget,
                                                        result_table_list =result_table_names)
        return analysis_function

    def handle_metadata_click(self):
        """
        Handle the click on the metadata button
        @return: None
        @author dz, 13.07.2022
        """
        self.metadata_widget = MetadataWidget(self.database_handler, self.analysis_id)
        self.metadata_widget.show()

    def handle_plot_widget_settings(self, parent_widget:ResultPlotVisualizer, plot_type_list):
        """
        Handle the setting of the plot widget, which is inside a custom made widget called parent widget.
        The plot needs to be cleared and combo boxes might need to be initialized.
        @param parent_widget: custom widget class ResultPlotVisualizer
        @param plot_type_list: list of display options to be displayed in the combo box dropdown, such as boxplot, ...
        @author dz, 13.07.2022
        """

            # print("overriding existing plot widget")
        if isinstance(plot_type_list, list):
        # remove the old plot if there is one already existing
            for i in reversed(range(parent_widget.plot_layout.count())):
                parent_widget.plot_layout.itemAt(i).widget().deleteLater()

            # create a new plot and insert it into the already exsiting plot layout
            self.logger.info("Creating a new plot widget")
            parent_widget.canvas = FigureCanvas(Figure())
            parent_widget.canvas.setMinimumSize(500, 500)  # set minimum size for the canvas
            parent_widget.canvas.setMaximumSize(1000, 500)

            self.scroll_area = QScrollArea()
            self.scroll_layout = QGridLayout()
            self.scroll_layout.addWidget(parent_widget.canvas)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setWidget(parent_widget.canvas)
            parent_widget.plot_layout.addWidget(self.scroll_area)
            parent_widget.add_labels_to_plot(plot_type_list, self.single_analysis_visualization)
            # add options only once
        else:
            self.logger.error(f"""The plot options in the combobox are not of list type but of type {type(plot_type_list)}
                              Also the plot type list is {plot_type_list}""")


    def export_plot_data(self,parent_widget:ResultPlotVisualizer):
        """
        Write the data shown in the plot into a csv file. The data are stored in the export data frame object
        in the parent widget
        @param parent_widget: custom widget class ResultPlotVisualizer
        @author dz, 13.07.2022
        """
        self.logger.info("Exporting data started to csv!")
        result_directory = QFileDialog.getExistingDirectory()
        try:
            parent_widget.export_data_frame.to_csv(
                f"{result_directory}/result_export_analysis_function_id_{str(parent_widget.analysis_function_id)}.csv"
            )
            print("file stored successfully")
            self.logger.info("Successfully stored results")
        except Exception as e:
            self.logger.error(f"Could not store results error message: {str(e)}")

    def save_plot_as_image(self,parent_widget:ResultPlotVisualizer):
        """
        Plot the figure as it is shwon in the canvas
        @param parent_widget: custom widget class ResultPlotVisualizer
        @author dz, 13.07.2022
        """
        self.logger.info("Saving plot as image")
        result_path = QFileDialog.getSaveFileName()[0]
        parent_widget.canvas.print_figure(result_path)
        #print("saved plot in " + result_path)
