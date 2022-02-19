from src.data_db import DuckDBDatabaseHandler
from PySide6.QtWidgets import *
import pyqtgraph as pg

class OfflineAnalysisResultVisualizer():

    def __init__(self, visualization_tab_widget: QTabWidget, database: DuckDBDatabaseHandler):
        # pyqt tab widget object
        self.visualization_tab_widget = visualization_tab_widget
        self.database_handler = database


    def show_results_for_current_analysis(self,analysis_id: int):
        print("Plotting results for analysis id " + str(analysis_id))

        # 1)
        # identify the number of series and create tabs for each analyzed series

        # 2)
        # identify the amount of analysis functions (different functions OR different boundaries) per series ( = plots per tab)

        q = """select distinct analysis_function_id from results where analysis_id = (?)"""
        list_of_analysis=self.database_handler.get_data_from_database(self.database_handler.database, q, [analysis_id])

        # e.g. [(43,), (45,), (47,)]

        # 3)
        # for each specific function -> create plot from available results

        main_layout = QHBoxLayout()
        for analysis in list_of_analysis:
            # tuple -> analysis function id at pos 0
            graph_n_layout = QVBoxLayout()
            analysis_specific_plot_widget = pg.PlotWidget()
            graph_n_layout.addWidget(analysis_specific_plot_widget)
            main_layout.addLayout(graph_n_layout,stretch=1)

            analysis_function_id = analysis[0]

            # go through the results table
            # select all results according to analysis_id and function_id,

            q="""select  result_value,sweep_number from results where analysis_id =(?) and analysis_function_id =(?) order by sweep_number"""
            result_list = self.database_handler.get_data_from_database(self.database_handler.database, q, [analysis_id, analysis_function_id])

            print(result_list)
            # ordered list -> get the number of series by checking for duplicate sweep numbers
            number_of_series = 0
            current_sweep_number = 0

            for i in result_list:
                if [1] != current_sweep_number:
                    current_sweep_number = i[1]
                    number_of_series +=1
                else:
                    break

            print("found series = " + str(number_of_series))
            # group the results by equal sweep numbers
            # plot to the visualization tab


            #self.visualization_tab_widget.setCurrentWidget(analysis_specific_plot_widget)



            y_data = []
            x_data = []
            for i in result_list:
                y_data.append(i[0])
                x_data.append(i[1])

            analysis_specific_plot_widget.plot(x_data,y_data)

        # after all 3 plots have been added
        all_plots = QWidget()
        all_plots.setLayout(main_layout)
        self.visualization_tab_widget.addTab(all_plots, "Test")
