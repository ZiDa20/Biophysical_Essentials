from PySide6.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from QT_GUI.OfflineAnalysis.CustomWidget.ui_SubstractDialog import Ui_CreateNewSeries
from functools import partial
import seaborn as sns

class SubstractDialog(Ui_CreateNewSeries):

    def __init__(self, database, frontend_style, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database
        self.frontend_style = frontend_style
        self.canvas = FigureCanvas()
        self.canvas_2 = FigureCanvas()
        self.ax = self.canvas.figure.subplots()
        self.ax.spines[['right', 'top']].set_visible(False)
        self.ax_2 = self.canvas_2.figure.subplots()
        self.ax_2.spines[['right', 'top']].set_visible(False)
        self.PlotGrid.addWidget(self.canvas)
        self.PlotGrid.addWidget(self.canvas_2)
        self.series_1.currentTextChanged.connect(self.connected_box)
        self.series_2.currentTextChanged.connect(self.connected_box)
        self.experiment_intersect_list = None
        self.fill_combobox_with_series()
        self.comboBox.currentIndexChanged.connect(self.retrieve_raw_data_series)
        self.pushButton_3.clicked.connect(self.initialize_data_merge)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        
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
        sweep_tables_series_name_1 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText()) if self.comboBox.currentText() in i] 
        sweep_tables_series_name_2 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_2.currentText()) if self.comboBox.currentText() in i] 
        sweep_table_1 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_1[0])
        sweep_table_2 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_2[0])
        self.draw_plots_series_1(sweep_table_1)
        self.draw_plots_series_2(sweep_table_2)
        return sweep_table_1, sweep_table_2
        
    def draw_plots_series_1(self, sweep_table):
        """_summary_

        Args:
            sweep_table (_type_): _description_
        """
        self.ax.clear()
        sns.lineplot(data = sweep_table, 
                     ax = self.ax, 
                     legend = False, 
                     color = "black", 
                     estimator= None, 
                     errorbar = "se",
                     palette = "tab20")
        self.canvas.draw_idle()
        
    def draw_plots_series_2(self,sweep_table):
        """_summary_

        Args:
            sweep_table (_type_): _description_
        """
        self.ax_2.clear()
        sns.lineplot(data = sweep_table, 
                     ax = self.ax_2, 
                     legend = False, 
                     color = "black", 
                     estimator=None, 
                     errorbar = "se",
                     palette = "tab20")
        self.canvas_2.draw_idle()
        
    def retrieve_sweep_table_iterator(self, experiment_name):
        """_summary: Should retrieve the Analysis Functions
        """
        sweep_tables_series_name_1 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText()) if experiment_name in i] 
        sweep_tables_series_name_2 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_2.currentText()) if experiment_name in i] 
        sweep_table_1 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_1[0])
        sweep_table_2 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_2[0])
        self.draw_plots_series_1(sweep_table_1)
        self.draw_plots_series_2(sweep_table_2)
        return sweep_table_1, sweep_table_2
        
    def initialize_data_merge(self):
        for experiment_name in self.experiment_intersect_list:
            sweep_table_1, sweep_table_2 = self.retrieve_sweep_table_iterator(experiment_name)
            print(sweep_table_1.shape)
            print(sweep_table_2.shape)
            


        
