

import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/OfflineAnalysis/CustomWidget")



from data_db import DuckDBDatabaseHandler
from specific_visualization_plot import ResultPlotVisualizer
from functools import partial
import numpy as np
from PySide6.QtWidgets import *
import pyqtgraph as pg
from collections import OrderedDict

import pandas as pd
from PySide6 import QtCore

import matplotlib
#import matplotlib.backends.backend_tkagg

from matplotlib.backends.qt_compat import QtWidgets
#from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import *


class OfflineAnalysisResultVisualizer():

    def __init__(self, visualization_tab_widget: QTabWidget, database: DuckDBDatabaseHandler):
        # pyqt tab widget object
        self.visualization_tab_widget = visualization_tab_widget
        self.database_handler = database
        self.split_data_functions =[ "No Split", "Split By Meta Data"]
        self.plot_type = ["Overlay All", "Line Plot Means", "Boxplot" ]
        self.plot_colors = ['b', 'g','r','c','m','y','k','w']
        self.result_directory = ""
        self.default_colors = ['k','b','r','g','c']


        #@todo maybe more clever to have an extra table in the database where to save this information
        self.function_plot_type = "sweep_wise"
        self.series_wise_function_list = ["Single_AP_Amplitude [mV]", "Single_AP_Threshold_Amplitude[mV]",
                    "Single_AP_Afterhyperpolarization_Amplitude [mV]", "Single_AP_Afterhyperpolarization_time[ms], Rheobase_Detection"]


        # one main dict that provides all standard evaluation functions. gives also rise to the option to implement a specific function
        # @todo write this to an extra class to provide these information all over the code

        self.specific_analysis_functions = {
            "max_current": self.visualize_sweep_wise,
            "min_current": self.visualize_sweep_wise,
            "mean_current": self.visualize_sweep_wise,
            "area_current": self.visualize_sweep_wise,
            "mean_voltage": self.visualize_series_wise,
            "Single_AP_Amplitude [mV]": self.visualize_series_wise,
            "Single_AP_Threshold_Amplitude[mV]": self.visualize_series_wise,
            "Single_AP_Afterhyperpolarization_Amplitude [mV]":self.visualize_series_wise,
            "Single_AP_Afterhyperpolarization_time[ms]": self.visualize_series_wise,
            "Rheobase_Detection" : self.rheobase_visualization,
            "Rheoramp_Analysis":self.visualize_sweep_wise #self.rheoramp_analysis
        }



        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.black_pen = pg.mkPen(color=(0, 0, 0))

    def show_results_for_current_analysis(self,analysis_id: int, series_name = None):
        """
        1) Identify the number of series and create tabs for each analyzed series
        :param analysis_id:
        :return:
        """
        # print("Plotting results for analysis id " + str(analysis_id))

        # @todo check if the tab already existis:

        q = """select analysis_series_name from analysis_series where analysis_id = (?)"""

        list_of_series = self.database_handler.get_data_from_database(self.database_handler.database, q,
                                                                        [analysis_id])
        print(list_of_series)


        for series in list_of_series:
            # create visualization for each specific series in specific tabs
            print("running analysis")

            print(series[0])
            print(analysis_id)

            self.analysis_function_specific_visualization(series[0],analysis_id)

        if self.visualization_tab_widget.tabText(0)=='Tab 1':
            self.visualization_tab_widget.removeTab(0)

        if series_name:
            self.visualization_tab_widget.setCurrentIndex(list_of_series.index((series_name,)))

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

        main_layout = QGridLayout()

        for analysis in list_of_analysis:
            print(str(analysis))
            # create new custom plot visualizer and parametrize data
            custom_plot_widget = ResultPlotVisualizer()

            custom_plot_widget.analysis_id = analysis_id
            custom_plot_widget.analysis_function_id = analysis[0]

            analysis_name = self.database_handler.get_analysis_function_name_from_id(analysis[0])
            custom_plot_widget.analysis_name = analysis_name

            custom_plot_widget.analysis_name = analysis_name

            """
            if analysis_name in self.series_wise_function_list:
                print("Analyzing")
                print(analysis_name)
                self.function_plot_type = "series_wise"
            else:
                print("Analyzing")
                print(analysis_name)
                self.function_plot_type = "sweep_wise"
            """

            custom_plot_widget.specific_plot_box.setTitle("Analysis: " + analysis_name)
            custom_plot_widget.save_plot_button.clicked.connect(partial(self.save_plot_as_image, custom_plot_widget))
            custom_plot_widget.export_data_button.clicked.connect(partial(self.export_plot_data,custom_plot_widget))

            self.single_analysis_visualization(custom_plot_widget,analysis_id,analysis[0])

            # widgets per row = 2

            widget_x_pos = list_of_analysis.index(analysis) // 2 # 2 widgets per row
            widgte_y_pos = list_of_analysis.index(analysis) % 2 # 2 widgets per row

            main_layout.addWidget(custom_plot_widget, widget_x_pos, widgte_y_pos)

        # after all plots have been added
        all_plots = QWidget()
        all_plots.setLayout(main_layout)

        existing_tab_names = []
        for existing_tab in range(self.visualization_tab_widget.count()):
            existing_tab_names.append( self.visualization_tab_widget.tabText(existing_tab) )

        # to handle going forth and back between single analysis and result visualizer
        if series in existing_tab_names:
            # in case the tab was already created
            self.visualization_tab_widget.removeTab(existing_tab_names.index(series))
            self.visualization_tab_widget.insertTab(existing_tab_names.index(series),all_plots,series)

        else:
            # if the tab was not created it will be appended at the end
            self.visualization_tab_widget.addTab(all_plots,series)

    def single_analysis_visualization(self,parent_widget,analysis_id,analysis_function_id,meta_data_list = None):
        """
        for each specific analysis function -> create plot from available results
        :param parent_widget: widget where to put the plot widget into
        :param analysis_id: offline analysis identification number of this analysis
        :param analysis_function_id: specific number of the used analysis function with the specific coursor bounds
        :return:
        """

        canvas = self.handle_plot_widget_settings(parent_widget)

        print("calling result list for")
        print(analysis_id)
        print(analysis_function_id)

        # get the class object name for this analysis
        class_object = AnalysisFunctionRegistration().get_registered_analysis_class(parent_widget.analysis_name)

        class_object.visualize_results(parent_widget, canvas, "Split by Meta Data")
        #class_object.visualize_results(parent_widget,canvas,"No Split")

        # here should the series specific plotting start
        """
        if meta_data_list:
            self.plot_meta_data_wise(canvas, result_list, number_of_series,meta_data_list)
        else:
            series_name = self.database_handler.get_analysis_function_name_from_id(analysis_function_id)
            self.simple_plot(parent_widget, canvas, result_list, number_of_series,series_name)
        """


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

            canvas = FigureCanvas(Figure(figsize=(5, 3)))
            parent_widget.plot_layout.addWidget(canvas)


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

            return canvas

        except Exception as e:
            print(str(e))

    def export_plot_data(self,parent_widget:ResultPlotVisualizer):

        result_directory = QFileDialog.getExistingDirectory()
        try:
            parent_widget.export_data_frame.to_csv(result_directory+"/result_export_analysis_function_id_"
                                                   + str(parent_widget.analysis_function_id) + ".csv")
            print("file stored successfully")
        except Exception as e:
            print("Results were not stored successfully")
            print(e)


    def save_plot_as_image(self,parent_widget:ResultPlotVisualizer):

        result_path = QFileDialog.getSaveFileName()[0]

        canvas= parent_widget.plot_layout.itemAt(0).widget()
        canvas.print_figure(result_path)
        print("saved plot in " + result_path)

    def plot_rheoramp_event_counts(self,parent_widget,result_list,number_of_sweeps):
        canvas = self.handle_plot_widget_settings(parent_widget)
        meta_data_groups = self.get_meta_data_groups_for_results(result_list, number_of_sweeps)
        meta_data_types = list(dict.fromkeys(meta_data_groups))
        plot_matrix = []

        for meta_type in meta_data_types:
                type_specific_series_pos = [i for i, x in enumerate(meta_data_groups) if x == meta_type]
                sweep_1 = []
                sweep_2 = []
                sweep_3 = []
                sweep_4 = []
                for pos in type_specific_series_pos:

                    sweep_1.append(result_list[pos*4][0])
                    sweep_2.append(result_list[pos*4+1][0])
                    sweep_3.append(result_list[pos * 4 + 2][0])
                    sweep_4.append(result_list[pos * 4 + 3][0])

                sweep_1 = [0 if i is None else i for i in sweep_1]
                sweep_2 = [0 if i is None else i for i in sweep_2]
                sweep_3 = [0 if i is None else i for i in sweep_3]
                sweep_4 = [0 if i is None else i for i in sweep_4]

                plot_matrix.append(sweep_1)
                plot_matrix.append(sweep_2)
                plot_matrix.append(sweep_3)
                plot_matrix.append(sweep_4)
                #for pos in type_specific_series_pos:
        ax = canvas.figure.subplots()

        plot = ax.boxplot(plot_matrix,  # notch=True,  # notch shape
                          vert=True,  # vertical box alignment
                          patch_artist=True)

    def plot_type_changed(self,parent_widget,new_text):
        """
        will be called when the plot type in the related combo box will be changed by the user
        :param parent_widget:
        :param new_text: text of the combo box e.g. 'overlay all', 'boxplot'
        :return:
        """
        if new_text == self.plot_type[0]: # == overlay all
            self.split_data_changed(parent_widget,parent_widget.split_data_combo_box.currentText())

        result_list = self.get_list_of_results(parent_widget.analysis_id, parent_widget.analysis_function_id)

        number_of_series = self.get_number_of_series(result_list)
        number_of_sweeps = int(len(result_list) / number_of_series)

        if parent_widget.analysis_name == 'Rheoramp_Analysis':
            self.plot_rheoramp_event_counts(parent_widget,result_list,number_of_sweeps)

        if new_text == self.plot_type[1]: # plot means

            # check whether meta data groups need to be taken into consideration
            if parent_widget.split_data_combo_box.currentText() == self.split_data_functions[0]: # no split

                  # calculate one mean for all and plot it
                  self.calculate_and_plot_mean_over_all(parent_widget,number_of_sweeps,number_of_series,result_list)

            else: # split by meta data group
                 canvas  = self.handle_plot_widget_settings(parent_widget)

                 #calculate mean trace per meta data group

                 # get the group per series
                 meta_data_groups = self.get_meta_data_groups_for_results(result_list, number_of_sweeps)

                 # get the total number of different groups
                 meta_data_types = list(dict.fromkeys(meta_data_groups))

                 # data will be appended to this list whenever a series of the meta data group was processed
                 meta_data_numbers = []

                 ax = canvas.figure.subplots()

                 # pandas dataframe to store plotted results to be exported easily
                 parent_widget.export_data_frame = pd.DataFrame()

                 # calculate mean per group
                 for i in meta_data_types:

                    # count the amount of series for this meta data group
                    meta_data_numbers.append(meta_data_groups.count(i))

                    group_mean = []
                    group_std = []
                    if self.function_plot_type == "sweep_wise":

                        for a in range(number_of_sweeps):
                            sweep_mean = []

                            for b in range(number_of_series):

                                pos = int((a + b*number_of_sweeps)/number_of_sweeps)
                                #print(str(i))
                                #print(str(pos))
                                if meta_data_groups[pos] == i:

                                        #print(result_list[a + b*number_of_sweeps])
                                        sweep_mean.append(result_list[a + b*number_of_sweeps][0])


                            group_mean.append(np.mean(sweep_mean))
                            group_std.append(np.std(sweep_mean))
                    else:
                        # not impelemented because this a scenario that might be not used
                        print("debug")


                    x = list(range(0, len(group_mean)))

                    ax.errorbar(x,group_mean, yerr=group_std, fmt='--o')
                    #ax.errorplot(y=group_mean, yerr= group_std) #self.default_colors[meta_data_types.index(i)], label='i')
                    parent_widget.export_data_frame.insert(0,i,group_mean)

                 custom_legend = []
                 for i in range(0,len(meta_data_types)):
                    custom_legend.append(meta_data_types[i] + " : n=" + str(meta_data_numbers[i]) )

                 ax.legend(custom_legend)
                 print(parent_widget.export_data_frame)

        if new_text == self.plot_type[2]:  # boxplots

                canvas = self.handle_plot_widget_settings(parent_widget)
                meta_data_groups = self.get_meta_data_groups_for_results(result_list, number_of_sweeps)
                meta_data_types = list(dict.fromkeys(meta_data_groups))
                ax = canvas.figure.subplots()

                box_plot_matrix = np.empty((number_of_series,len(meta_data_types)))
                box_plot_matrix[:] = np.nan

                group_sizes = []

                #plot a box for each metadata type
                for type in meta_data_types:

                    type_counter = 0
                    # get the positions of the series names
                    type_specific_series_pos = [i for i, x in enumerate(meta_data_groups) if x==type]
                    insert_at_pos_x = meta_data_types.index(type)

                    if len(type_specific_series_pos)> 0 :

                        for pos in type_specific_series_pos:

                            # calc mean for this series
                            try:
                                insert_at_pos_y = np.argwhere(np.isnan(box_plot_matrix[:,insert_at_pos_x]))[0][0]

                                series_sweep_values = []

                                for sweep_pos in range(pos*number_of_sweeps,(pos +1)*number_of_sweeps):
                                    series_sweep_values.append(result_list[sweep_pos][0])

                                if parent_widget.analysis_name == 'Rheobase_Detection':
                                    # needs no else since box_plot_matrix is already initialized with nans
                                    if not all(v is None for v in series_sweep_values):
                                        first_rheobase_current_index = next(x[0] for x in enumerate(series_sweep_values) if x[1] != None)
                                        mean_val = series_sweep_values [first_rheobase_current_index]
                                        type_counter+=1
                                        box_plot_matrix[insert_at_pos_y][insert_at_pos_x] = mean_val
                                else:
                                    # plot for sweep wise
                                    none_free_y_data = []
                                    for i in series_sweep_values:
                                        if i is not None:
                                            none_free_y_data.append(i)

                                    if len(none_free_y_data) > 0:
                                        mean_val = np.mean(series_sweep_values)
                                        box_plot_matrix[insert_at_pos_y][insert_at_pos_x] = mean_val
                                        type_counter += 1

                            except Exception as e:
                                print("Error - this should not happen")
                                print(e)
                        group_sizes.append(type_counter)
                    else:
                        try:
                            insert_at_pos_y = np.argwhere(np.isnan(box_plot_matrix[insert_at_pos_x,]))[0][0]
                            box_plot_matrix[insert_at_pos_x][insert_at_pos_y] = np.mean(
                                result_list[type_specific_series_pos:type_specific_series_pos + number_of_sweeps][0])

                        except Exception as e:
                            print("Error - this should not happen" )
                            print(e)

                false_true_mask = ~np.isnan(box_plot_matrix)
                filtered_box_plot_data=[d[m] for d, m in zip(box_plot_matrix.T, false_true_mask.T)]

                custom_labels = []
                for i in range(0,len(meta_data_types)):
                    custom_labels.append(meta_data_types[i] + ": " + str(group_sizes[i]))

                plot = ax.boxplot(filtered_box_plot_data,#notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True)

                #ax.violinplot(filtered_box_plot_data)
                ax.set_xticks(np.arange(1, len(meta_data_types) + 1), labels=meta_data_types)
                ax.set_xlim(0.25, len(meta_data_types) + 0.75)


                for patch, color in zip(plot['boxes'], self.default_colors[0:len(plot['boxes'])]):
                        patch.set_facecolor(color)

                ax.legend(plot['boxes'],custom_labels)

                parent_widget.export_data_frame = pd.DataFrame(box_plot_matrix, columns=meta_data_types)
                print(parent_widget.export_data_frame)





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

        canvas = self.handle_plot_widget_settings(parent_widget)
        ax = canvas.figure.subplots()
        ax.plot(mean_trace,'k', label = 'Mean')
        ax.legend()

        #@todo add standard deviation to the plot too !

    def plot_meta_data_wise(self,canvas: pg.PlotWidget, result_list,number_of_series,meta_data_groups):
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



        ax = canvas.figure.subplots()

        # for each data trace ( = a sub list) create the plot in the correct color according to meta data group
        for a in range(len(x_data)):

                meta_data_group = meta_data_groups[a]

                for m in meta_data_types:
                    if m == meta_data_group:
                        pos = meta_data_types.index(m)
                        if self.function_plot_type == "sweep_wise":
                            ax.plot(x_data[a], y_data[a],self.default_colors[pos], label=series_names[a])
                        else:
                            ax.plot(1,sum(y_data[a]) / len(y_data[a]), marker="o", markerfacecolor=self.default_colors[pos], label=series_names[a])

                        ax.legend()

    def simple_plot(self,parent_widget,canvas, result_list,number_of_series,series_name):
        """
        Plot all data together into one specific analysis plot widget without any differentiation between meta data groups
        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :return:
        """
        number_of_sweeps= int(len(result_list) / number_of_series)
        print("calculated_sweep_number = " + str(number_of_sweeps))

        parent_widget.export_data_frame = pd.DataFrame()
        # each sub list represents the results of a single series
        x_data, y_data, series_names = self.fetch_x_and_y_data(result_list, number_of_sweeps)

        # analysis_specific_plot_widget is the figure
        ax = canvas.figure.subplots()

        '''
        for a in range(len(x_data)):
                if self.function_plot_type == "sweep_wise":
                    ax.plot(x_data[a],y_data[a], 'k', label=series_names[a])
                    parent_widget.export_data_frame.insert(0, series_names[a],y_data[a])
                else:
                    ax.plot(1,sum(y_data[a]) / len(y_data[a]), marker="o", markerfacecolor='k', label=series_names[a])
        '''

        # experiment: have a dict with a specific analysis function for each series
        # e.g. analize_sweep_wise , analize_series_wise, specific_rheobase_analysis

        for a in range(len(x_data)):
            try:
                self.specific_analysis_functions.get(series_name)(ax,x_data,y_data,series_names,parent_widget,a)
            except Exception as e:
                print(e)
                print(series_names)
                print(f'Error in dict call for series with series name {series_name}')
        # @todo: add shade of stde
        ax.legend()
        canvas.show()

       # analysis_specific_plot_widget.setHtml(fig.to_html(include_plotlyjs='cdn'))

    def visualize_sweep_wise(self,ax,x_data,y_data,series_names,parent_widget,a):
        ax.plot(x_data[a], y_data[a], 'k', label=series_names[a])
        parent_widget.export_data_frame.insert(0, series_names[a], y_data[a])

    def visualize_series_wise(self,ax,x_data,y_data,series_names,parent_widget,a):
        '''

        :param ax:
        :param x_data:
        :param y_data:
        :param series_names:
        :param parent_widget:
        :param a:
        :return:
        '''
        none_free_y_data = []
        for i in y_data[a]:
            if i is not None:
                none_free_y_data.append(i)

        if len(none_free_y_data)>0:
            ax.plot(1, sum(none_free_y_data) / len(none_free_y_data), marker="o", markerfacecolor='k', label=series_names[a])

    def rheoramp_analysis(self):
        print("not implemented")

    def rheobase_visualization(self,ax,x_data,y_data,series_names,parent_widget,a):
        '''

        :param ax:
        :param x_data:
        :param y_data: result values : list of lists: each sublist presents one series, contains None if no AP was detected
        :param series_names:
        :param parent_widget:
        :param a:
        :return:
        '''

        # plot the first value unequal none

        # if there was no action potential in the rheobase, all y values will be none and will be therefore not further analized
        if not all(v is None for v in y_data[a]):
            first_rheobase_current_index = next(x[0] for x in enumerate(y_data[a]) if x[1] != None)
            ax.plot(1, y_data[a][first_rheobase_current_index], marker="o", markerfacecolor='k', label=series_names[a])
        else:
            return

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
                try:
                    series_y_data.append(result_list[a + b][0])
                    series_x_data.append(result_list[a + b][1])
                except Exception as e:
                    print(e)

            
            try:
                y_data.append(series_y_data)
                x_data.append(series_x_data)
                names.append(self.database_handler.get_experiment_name_for_given_sweep_table_name(result_list[a + b][2]))
            except Exception as e:
                print(len(result_list))
                print(e)


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


