from PySide6.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from QT_GUI.OfflineAnalysis.CustomWidget.ui_SubstractDialog import Ui_CreateNewSeries


class SubstractDialog(Ui_CreateNewSeries):

    def __init__(self, database, frontend_style, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database
        self.frontend_style = frontend_style
        self.canvas = FigureCanvas()
        self.PlotGrid.addWidget(self.canvas)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.fill_combobox_with_series()
        self.series_1.currentIndexChanged.connect(self.connected_box)
        self.series_2.currentIndexChanged.connect(self.connected_box)
        self.comboBox.currentIndexChanged.connect(self.retrieve_raw_data_series)
        self.experiment_intersect_list = None
        

    def fill_combobox_with_series(self):
        """_summary_: Retrieves the initial experiments and series_names that can be identified for both series
        """
        unique_series = [i[0] for i in self.select_series_to_be_analized()]
        self.series_1.addItems(unique_series)
        self.series_2.addItems(unique_series)
        experiment_names_1 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id(self.series_1.currentText())]
        experiment_names_2 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id(self.series_2.currentText())]
        self.experiment_intersect_list = list(set(experiment_names_1).intersection(set(experiment_names_2)))
        self.comboBox.addItems(self.experiment_intersect_list)
        self.retrieve_raw_data_series()
        print("gotcha")

    def select_series_to_be_analized(self):
        """
        executed after all experiment files have been loaded
        :return:
        """
        return self.database_handler.get_distinct_non_discarded_series_names()
    
    def connected_box(self):
        """ Retrieve the experiments that represent both series
        """
        experiment_names_1 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id(self.series_1.currentText())]
        experiment_names_2 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id(self.series_2.currentText())]
        self.experiment_intersect_list = list(set(experiment_names_1).intersection(set(experiment_names_2)))
        self.comboBox.clear()
        self.comboBox.addItems(self.experiment_intersect_list)
        self.retrieve_raw_data_series()

    def retrieve_raw_data_series(self):
        """_summary: Should retrieve the Analysis Functions
        """
        sweep_tables_series_name_1 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText()) if self.comboBox.currentText() in i ] 
        sweep_tables_series_name_2 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText()) if self.comboBox.currentText() in i] 
        sweep_table_1 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_1[0])
        sweep_table_2 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_2[0])
        self.draw_plots(sweep_table_1)
        print(sweep_table_1)

    def draw_plots(self, sweep_table):
        """_summary__ 
        """
        self.ax = self.canvas.figure.subplots()
        self.ax.plot(sweep_table)
        


        
