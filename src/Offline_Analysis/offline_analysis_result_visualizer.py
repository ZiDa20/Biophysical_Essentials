from src.data_db import DuckDBDatabaseHandler
from PySide6.QtWidgets import *
import pyqtgraph as pg

class OfflineAnalysisResultVisualizer():

    def __init__(self, visualization_tab_widget: QTabWidget, database: DuckDBDatabaseHandler):
        # pyqt tab widget object
        self.visualization_tab_widget = visualization_tab_widget
        self.database_handler = database


    def show_results_for_current_analysis(self,analysis_id: int):
        """
        1) Identify the number of series and create tabs for each analyzed series
        :param analysis_id:
        :return:
        """
        # print("Plotting results for analysis id " + str(analysis_id))

        q = """select analysis_series_name from analysis_series where analysis_id = (?)"""
        list_of_series = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                        [analysis_id])
        print(list_of_series)
        for series in list_of_series:
            # create visualization for each specific series in specific tabs
            # print("running analysis")
            self.analysis_function_specific_visualization(series[0],analysis_id)


    def analysis_function_specific_visualization(self,series,analysis_id):
        """
        2) identify the amount of analysis functions (different functions OR different boundaries) per series ( = plots per tab)
        :param series:
        :return:
        """
        q = """select distinct analysis_function_id from analysis_functions where analysis_id = (?) and analysis_series_name =(?)"""
        list_of_analysis=self.database_handler.get_data_from_database(self.database_handler.database, q, (analysis_id,series))

        print("series= " + series)
        print("list of analysis")
        print(list_of_analysis)
        # e.g. [(43,), (45,), (47,)]

        main_layout = QHBoxLayout()

        for analysis in list_of_analysis:
            print(str(analysis))
            updated_layout = self.single_analysis_visualization(main_layout,analysis_id,analysis[0])

        # after all plots have been added
        all_plots = QWidget()
        all_plots.setLayout(main_layout)
        self.visualization_tab_widget.addTab(all_plots,series)



    def single_analysis_visualization(self,main_layout,analysis_id,analysis_function_id):
        """
        3) for each specific function -> create plot from available results
        :return:
        """
        # tuple -> analysis function id at pos 0
        graph_n_layout = QVBoxLayout()
        analysis_specific_plot_widget = pg.PlotWidget()
        graph_n_layout.addWidget(analysis_specific_plot_widget)
        main_layout.addLayout(graph_n_layout,stretch=1)

        # iterate results table, select all results according to analysis_id and function_id,

        q="""select  result_value,sweep_number,sweep_table_name from results where analysis_id =(?) and analysis_function_id =(?) order by sweep_table_name,sweep_number"""
        result_list = self.database_handler.get_data_from_database(self.database_handler.database, q, [analysis_id, analysis_function_id])

        print(result_list)

        # result list ordered by sweep numbers  -> get the number of series by checking table names

        number_of_series = 0
        current_series_name = ""

        for i in result_list:
                if i[2] != current_series_name:
                    current_series_name = i[2]
                    number_of_series +=1

        print("found series = " + str(number_of_series))

        # group the results by equal sweep numbers
        # plot to the visualization tab

        number_of_sweeps= int(len(result_list) / number_of_series)
        print("calculated_sweep_number = " + str(number_of_sweeps))

        y_data = []
        x_data = []

        for a in range (0,len(result_list),number_of_sweeps):
                series_y_data = []
                series_x_data = []
                for b in range(number_of_sweeps):
                    series_y_data.append(result_list[a+b][0])
                    series_x_data.append(result_list[a+b][1])


                y_data.append(series_y_data)
                x_data.append(series_x_data)

        for a in range(len(x_data)):
                analysis_specific_plot_widget.plot(x_data[a], y_data[a])


