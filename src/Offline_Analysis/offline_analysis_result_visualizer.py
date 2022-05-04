from src.data_db import DuckDBDatabaseHandler
from QT_GUI.update_dave.specific_visualization_plot import ResultPlotVisualizer
from functools import partial
from PySide6.QtWidgets import *
import pyqtgraph as pg
import pyqtgraph.exporters
from PySide6 import QtWebEngineWidgets
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import PySide6.QtWebEngineWidgets


class OfflineAnalysisResultVisualizer():

    def __init__(self, visualization_tab_widget: QTabWidget, database: DuckDBDatabaseHandler):
        # pyqt tab widget object
        self.visualization_tab_widget = visualization_tab_widget
        self.database_handler = database
        self.split_data_functions =[ "No Split", "Split By Meta Data"]
        self.plot_type = ["Overlay All", "Line Plot Means", "Boxplot" ]
        self.plot_colors = ['b', 'g','r','c','m','y','k','w']
        self.result_directory = ""


        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.black_pen = pg.mkPen(color=(0, 0, 0))

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
            # create new custom plot visualizer and parametrize data
            custom_plot_widget = ResultPlotVisualizer()

            custom_plot_widget.analysis_id = analysis_id
            custom_plot_widget.analysis_function_id = analysis[0]

            custom_plot_widget.specific_plot_box.setTitle("Analysis" + str(analysis))
            self.single_analysis_visualization(custom_plot_widget,analysis_id,analysis[0])


            main_layout.addWidget(custom_plot_widget)

        # after all plots have been added
        all_plots = QWidget()
        all_plots.setLayout(main_layout)
        self.visualization_tab_widget.addTab(all_plots,series)



    def single_analysis_visualization(self,parent_widget,analysis_id,analysis_function_id,meta_data_list = None):
        """
        for each specific analysis function -> create plot from available results
        :param parent_widget: widget where to put the plot widget into
        :param analysis_id: offline analysis identification number of this analysis
        :param analysis_function_id: specific number of the used analysis function with the specific coursor bounds
        :return:
        """

        analysis_specific_plot_widget = self.handle_plot_widget_settings(parent_widget)

        # self.browser = QtWebEngineWidgets.QWebEngineView(self)


        result_list = self.get_list_of_results(analysis_id,analysis_function_id)

        number_of_series = self.get_number_of_series(result_list)

        if meta_data_list:
            self.plot_meta_data_wise(analysis_specific_plot_widget, result_list, number_of_series,meta_data_list)
        else:
            self.simple_plot(analysis_specific_plot_widget, result_list, number_of_series)



    def handle_plot_widget_settings(self,parent_widget:ResultPlotVisualizer):
        """
        Handle the setting of the plot widget, which is inside a custom made widget called parent widget.
        The plot needs to be cleared and combo boxes might need to be initialized.
        :param parent_widget:
        :return:
        """
        try:

            print("overriding existing plot widget")
            # remove the old plot if there is one already existing
            parent_widget.plot_layout.takeAt(0)

            # create a new plot and insert it into the already exsiting plot layout
            #analysis_specific_plot_widget = pg.PlotWidget()
            #parent_widget.plot_layout.addWidget(analysis_specific_plot_widget)

            browser = QtWebEngineWidgets.QWebEngineView()
            parent_widget.plot_layout.addWidget(browser)


            parent_widget.save_plot_button.clicked.connect(partial(self.save_plot_as_image,parent_widget))
            # add options only once
            try:
                if parent_widget.split_data_combo_box.currentText() not in self.split_data_functions:
                    parent_widget.split_data_combo_box.addItems(self.split_data_functions)
                    parent_widget.split_data_combo_box.currentTextChanged.connect(
                        partial(self.split_data_changed, parent_widget))
                    parent_widget.plot_type_combo_box.addItems(self.plot_type)
                    parent_widget.plot_type_combo_box.currentTextChanged.connect(
                        partial(self.plot_type_changed, parent_widget))
            except Exception as e:
                print(str(e))

            '''
            return analysis_specific_plot_widget
            '''

            return browser

        except Exception as e:
            print(str(e))

    def save_plot_as_image(self,parent_widget:ResultPlotVisualizer):

        result_path = QFileDialog.getSaveFileName()[0]

        analysis_specif_widget= parent_widget.plot_layout.itemAt(0).widget()

        exporter = pg.exporters.ImageExporter(analysis_specif_widget.plotItem)

        print(result_path)
        exporter.export(result_path)

        print("saved plot in " + result_path)


    def plot_type_changed(self,parent_widget,new_text):
        """
        will be called when the plot type in the related combo box will be changed by the user
        :param parent_widget:
        :param new_text:
        :return:
        """
        if new_text == self.plot_type[0]: # == overlay all
            self.split_data_changed(parent_widget,parent_widget.split_data_combo_box.currentText())

        if new_text == self.plot_type[1]: # plot means

            result_list = self.get_list_of_results(parent_widget.analysis_id,parent_widget.analysis_function_id)

            number_of_series = self.get_number_of_series(result_list)
            number_of_sweeps = int(len(result_list) / number_of_series)

            # check whether meta data groups need to be taken into consideration
            if parent_widget.split_data_combo_box.currentText() == self.split_data_functions[0]: # no split

                  # calculate one mean for all and plot it
                  self.calculate_and_plot_mean_over_all(parent_widget,number_of_sweeps,number_of_series,result_list)

            else:
                 analysis_specific_plot_widget = self.handle_plot_widget_settings(parent_widget)
                 #analysis_specific_plot_widget.addLegend()

                 #calculate mean trace per meta data group
                 # get the group per series
                 meta_data_groups = self.get_meta_data_groups_for_results(result_list, number_of_sweeps)

                 # get the total number of different groups
                 meta_data_types = list(dict.fromkeys(meta_data_groups))

                 fig = go.Figure()

                 # calculate mean per group
                 for i in meta_data_types:

                    group_mean = []

                    for a in range(number_of_sweeps):
                        sweep_mean = []

                        for b in range(number_of_series):

                            pos = int((a + b*number_of_sweeps)/number_of_sweeps)
                            print(str(i))
                            print(str(pos))
                            if meta_data_groups[pos] == i:
                                print(result_list[a + b*number_of_sweeps])
                                sweep_mean.append(result_list[a + b*number_of_sweeps][0])


                        group_mean.append(sum(sweep_mean)/(len(sweep_mean)))

                    fig.add_trace(go.Scatter(y=group_mean, mode='lines', name=i ))



                    # go through each series

                        # check if the meta data group matches the current one in i

                            # if so, calculate

                 fig.update_layout(
                     autosize=False,
                     width=500,
                     height=400)

                 analysis_specific_plot_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

        if new_text == self.plot_type[2]:  # boxplots
            print("not implemented yet")

    def calculate_and_plot_mean_over_all(self,parent_widget, number_of_sweeps, number_of_series, result_list):
        """
        calculates one mean trace from all available results and plots it
        :param parent_widget:
        :param number_of_sweeps:
        :param number_of_series:
        :param result_list:
        :return:
        """
        mean_trace = []

        for a in range(number_of_sweeps):
            mean_sweep = []
            for b in range(number_of_series):
                #print(result_list[a + b * number_of_sweeps])
                mean_sweep.append(result_list[a + b * number_of_sweeps][0])

            mean_trace.append(sum(mean_sweep) / len(mean_sweep))

        analysis_specific_plot_widget = self.handle_plot_widget_settings(parent_widget)

        analysis_specific_plot_widget.plot(mean_trace)
        #@todo add standard deviation to the plot too !

    def plot_meta_data_wise(self,analysis_specific_plot_widget: pg.PlotWidget, result_list,number_of_series,meta_data_groups):
        """
        rearrange the plot to color each trace according to it's meta data group.

        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :param meta_data_groups:
        :return:
        """
        number_of_sweeps= int(len(result_list) / number_of_series)
        meta_data_types = list(dict.fromkeys(meta_data_groups))

        x_data,y_data, series_names = self.fetch_x_and_y_data( result_list, number_of_sweeps)

        #analysis_specific_plot_widget.addLegend()

        default_colors = ["Black","Blue","Red","Orange","Green"]

        fig = go.Figure()

        # for each data trace ( = a sub list) create the plot in the correct color according to meta data group
        for a in range(len(x_data)):

                meta_data_group = meta_data_groups[a]



                for m in meta_data_types:
                    if m == meta_data_group:
                        pos = meta_data_types.index(m)
                        #print(self.plot_colors[pos])
                        #analysis_specific_plot_widget.plot(x_data[a], y_data[a], pen=pg.mkPen(self.plot_colors[pos], width=3), name=m)

                        fig.add_trace(go.Scatter(x=x_data[a], y=y_data[a],
                                                 mode='lines',
                                                 name=m + ": " + series_names[a], line=dict(color=default_colors[pos])))

        fig.update_layout(
                        autosize=False,
                        width=500,
                        height=400)
        analysis_specific_plot_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))


    def simple_plot(self,analysis_specific_plot_widget, result_list,number_of_series):
        """
        Plot all data together into one specific analysis plot widget without any differentiation between meta data groups
        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :return:
        """
        number_of_sweeps= int(len(result_list) / number_of_series)
        print("calculated_sweep_number = " + str(number_of_sweeps))

        x_data, y_data, series_names = self.fetch_x_and_y_data(result_list, number_of_sweeps)

        fig = go.Figure()
        for a in range(len(x_data)):
                #analysis_specific_plot_widget.plot(x_data[a], y_data[a], pen = self.black_pen)
                fig.add_trace(go.Scatter(x=x_data[a], y=y_data[a],
                                         mode='lines',
                                         name=series_names[a],line=dict(color='Black')))

        fig.update_layout(
            autosize=False,
            width=500,
            height=400)

        analysis_specific_plot_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def get_list_of_results(self,analysis_id,analysis_function_id):
        """
         Helper function to iterate results table in the database, select all results according the analysis_id and function_id
        :param analysis_id: Id of the current offline analysis
        :param analysis_function_id: id of the current function
        :return: list of triples : [(result_value, sweep_number, sweep_table_name)]
        """
        q = """select  result_value,sweep_number,sweep_table_name from results where analysis_id =(?) and analysis_function_id =(?) order by sweep_table_name,sweep_number"""
        result_list = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                   [analysis_id, analysis_function_id])

        #print(result_list)
        # result list ordered by sweep numbers  -> get the number of series by checking table names
        return result_list


    def fetch_x_and_y_data(self,result_list,number_of_sweeps):
        """
        helper function to create a list of lists: each sub list represents the results of a single series
        :param result_list: list of triples [(result_value, sweep_number, sweep_table_name)]
        :param number_of_sweeps: number of sweeps per series
        :return: x data and y data : list of lists
        """

        y_data = []
        x_data = []
        names =  []
        # create a list of lists for each series
        for a in range(0, len(result_list), number_of_sweeps):
            series_y_data = []
            series_x_data = []
            for b in range(number_of_sweeps):
                series_y_data.append(result_list[a + b][0])
                series_x_data.append(result_list[a + b][1])

            y_data.append(series_y_data)
            x_data.append(series_x_data)
            names.append(self.database_handler.get_experiment_name_for_given_sweep_table_name(result_list[a + b][2]))

        return x_data, y_data, names

    def split_data_changed(self,parent_widget,new_text):
        """
        will be called when the text in a combo box changes
        :param parent_widget: plot widget where the change needs to be made : QWidget
        :param new_text: String of the new text
        :return:
        """
        print("split data in " + parent_widget.specific_plot_box.title())

        if new_text == "Split By Meta Data":
            self.plot_data_splitted_by_meta_data(parent_widget)

        if new_text == "No Split":
            self.single_analysis_visualization(parent_widget,parent_widget.analysis_id,parent_widget.analysis_function_id)


    def plot_data_splitted_by_meta_data(self, parent_widget: ResultPlotVisualizer):
        """

        :param parent_widget:
        :return:
        """

        analysis_id = parent_widget.analysis_id
        analysis_function_id = parent_widget.analysis_function_id

        q = """select result_value,sweep_number,sweep_table_name from results where analysis_id =(?) and analysis_function_id =(?) order by sweep_table_name,sweep_number"""
        result_list = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                   [analysis_id, analysis_function_id])

        # print(result_list)

        number_of_series = self.get_number_of_series(result_list)
        number_of_sweeps = int(len(result_list) / number_of_series)

        sweep_table_meta_data_mapping = self.get_meta_data_groups_for_results(result_list,number_of_sweeps)

        self.single_analysis_visualization(parent_widget,analysis_id,analysis_function_id,sweep_table_meta_data_mapping)

    def get_meta_data_groups_for_results(self,result_list, number_of_sweeps):
        """

        :param result_list:
        :param number_of_sweeps:
        :return:
        """
        sweep_table_meta_data_mapping = []
        for i in range(0, len(result_list), number_of_sweeps):
            # select sweep table name of this series
            table_name = result_list[i][2]

            # find the database associated experiment meta data for this series

            q = """select meta_data_group from experiments where experiment_name = (select experiment_name from experiment_series where sweep_table_name = (?))"""
            sweep_table_meta_data_mapping.append(
                self.database_handler.get_data_from_database(self.database_handler.database, q, [table_name])[0][0])

        return sweep_table_meta_data_mapping

    def get_number_of_series(self,result_list):
        """
        result list looks like: (5.27e-10, 1, 'imon_signal_201229_011_Series1')
        :return:
        """
        number_of_series = 0
        current_series_name = ""

        for i in result_list:
            if i[2] != current_series_name:
                current_series_name = i[2]
                number_of_series += 1

        print("found series = " + str(number_of_series))
        return number_of_series