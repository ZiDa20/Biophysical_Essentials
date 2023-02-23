from re import T
from PySide6 import QtCore
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from treeview_manager import *
import pyqtgraph as pg
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

from draggable_lines import DraggableLines
sys.path.append(os.path.dirname(os.getcwd()) + "/src/Offline_Analysis")
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from PySide6.QtCore import Signal
# inheritage from qobject required for use of signal
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import  AnalysisFunctionRegistration

class PlotWidgetManager(QRunnable):
    """ A class to handle a specific plot widget and it'S appearance, subfunctions, cursor bounds, .... """

    def __init__(self,vertical_layout_widget,database,tree_view,detection,toolbar_widget = None, toolbar_layout = None):
        """
        INIT:
        :param vertical_layout_widget: layout to be filled with the plotwidget created by this class
        :param manager_object: can be either online or offline analysis manager object
        :param tree_view:
        :param mode: can be either 0 (online analysis) or 1 (offline analysis)
        mode 0: values will be read directly from the .dat file
        mode 1: values will be read from the database provided from the offline manager object
        """
        pg.setConfigOption('foreground', 'k')
        self.plot_widget = pg.PlotWidget()
        self.detection_mode = detection

        try:
            print("removed old widget")
            vertical_layout_widget.takeAt(0)

        except Exception as e:
            print(e)

        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        self.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.vertical_layout = vertical_layout_widget

        self.toolbar_widget = toolbar_widget

        self.tree_view = tree_view

        self.database_handler = database



        self.time = None

        # neccessary for succesfull signal emitting
        super().__init__()

        self.left_bound_changed = CursorBoundSignal()
        self.right_bound_changed = CursorBoundSignal()


        # all tuples of left and right bounds that will be plotted .. identified by its row number as a key
        self.coursor_bound_tuple_dict = {}

        # slot for the analysis function table widget: might be assigned to allow live plots
        # e.g. max_current | 1 | 10 | change | configure | checkbox
        self.analysis_functions_table_widget = None

        self.default_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']
     
        self.live_analysis_info = None


    def set_analysis_functions_table_widget(self,analysis_functions_table_widget):
        self.analysis_functions_table_widget = analysis_functions_table_widget
        print("table widget was set")


    """ @deprecated dz 30.11.2022
    def tree_view_click_handler(self, item):
        
        #handle all incoming clicks in the treeview related to plotting
        #@param item: treeviewitem
        #@return:
        #:author: dz, 21.07.2022
        
        print(f'Text of first column in item is {item.text(0)}')

        try:
            if "Sweep" in item.text(0) or "sweep" in item.text(0):
                self.sweep_in_treeview_clicked(item)
            else:
                if ".dat" in item.text(0):
                    print("To see data traces, click on a sweep or a series")
                else:
                 self.series_in_treeview_clicked(item)
                 #self.series_clicked(item)
        except Exception as e:
            print(e)
            print("experiment was clicked")
            self.series_in_treeview_clicked(item.child(0))
    """

    """
    def sweep_in_treeview_clicked(self,item):
            self.sweep_clicked_load_from_dat_database(item)
            self.check_live_analysis_plot(item,"sweep")

    def series_in_treeview_clicked(self,item):
            self.series_clicked_load_from_database(item)
            self.check_live_analysis_plot(item,"series")

    """

    def update_live_analysis_info(self,live_analysis_info):
        """
        update from extern functions and classes, such as analysis function seletion manager
        """
        #self.live_plot_info = pd.DataFrame(columns=["page", "col", "func_name", "left_cursor", "right_cursor"])
        self.live_analysis_info = live_analysis_info

    def check_live_analysis_plot(self, experiment_name, identifier, sweep_number = None):
        """
        calculate values to be plotted in the "live plot" feature during analysis
        @param item:
        @param table_widget:
        @return:
        @author: dz, 29.09.2022
        """
        print("checking live analysis")

        if  self.live_analysis_info is not None:
            
            #self.show_pgf_segment_buttons(experiment_name, identifier)

            for index,row in  self.live_analysis_info.iterrows():
                
                row_nr = row["page"]
                column = row["col"]
                fct = row["func_name"]
                lower_bound = row["left_cursor"]
                upper_bound = row["right_cursor"]
                live_plot = row["live_plot"]
                cursor_bound  = row["cursor_bound"]

                if cursor_bound:

                    self.show_draggable_lines((row_nr,column))
                    

                    # only show live plot if also cursor bounds were selected                
                    if live_plot:

                        analysis_class_object = AnalysisFunctionRegistration().get_registered_analysis_class(fct)

                        x_y_tuple = analysis_class_object.live_data(lower_bound, upper_bound, experiment_name,identifier, self.database_handler)
                        
                        if sweep_number:
                            sweep_number = sweep_number.split("_")
                            sweep_number = int(sweep_number[1])
                            x_y_tuple = [x_y_tuple[sweep_number-1]]

                        if x_y_tuple is not None:
                                    for tuple in x_y_tuple:
                                        if isinstance(tuple[1],list):
                                            y_val_list = [item * self.plot_scaling_factor for item in tuple[1]]
                                            self.ax1.plot(tuple[0], y_val_list , c=self.default_colors[row_nr+column], linestyle='dashed')
                                        else:
                                            self.ax1.plot(tuple[0], tuple[1]*self.plot_scaling_factor, c=self.default_colors[row_nr+column], marker="o")
                        else:
                                    print("Tuple was None: is live plot function for", fct, " already implemented ? ")
                else:
                    self.remove_dragable_lines(row_nr)

            """
             if level == "series":
                       
                    else:
                        x_y_tuple = analysis_class_object.live_data(lower_bound, upper_bound,experiment_name,identifier,self.database_handler, item_text)
            """

    def show_pgf_segment_buttons(self, experiment_name, series_identifier):

        
        # get the upper and most right ax value (lowest y and smallest x at [0])
        current_ax_height = self.ax1.get_ylim()[1]
        current_ax_length = self.ax1.get_xlim()[1]

        pgf_table = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name, series_identifier)
        pgf_table = pgf_table[pgf_table["selected_channel"] == "1"]
        self.rect_list = []
        self.text_list = []
        total_duration = 0
        for d in range(len(pgf_table['duration'].values)):
            max_len = float(pgf_table['duration'].values[d]) * 1000
            
            rect = plt.Rectangle((total_duration+1/5*max_len, current_ax_height),  3/5*max_len , 3, facecolor='w', edgecolor='grey', alpha=1,label='Section 1')
            text = self.ax1.text(total_duration+0.5*max_len, current_ax_height + 1.5, f'Seg. {d+1}', fontsize=10, ha='center', va='center')
            
            self.rect_list.append(rect)
            self.text_list.append(text)

            self.ax1.add_patch(rect)
            total_duration += max_len

        # Variable to keep track of the currently clicked rectangle
        clicked_rect = None
        self.canvas.draw_idle()
    
    def onclick(self,event):
        global clicked_rect
        # Find which rectangle was clicked
        for rect, text in zip(self.rect_list, self.text_list):

            if rect.contains(event)[0]:
               
                # Set the color of the clicked rectangle to red and the others to white
                for r in self.rect_list:
                    r.set_facecolor('w')

                rect.set_facecolor('red')
                
                self.canvas.draw_idle()
                print(f'Clicked on rectangle with label: {text.get_text()}')
                break
    """
    def sweep_clicked_load_from_dat_file(self,item):
        
        Whenever a sweep is clicked in online analysis, this handler will be executed to plot the selected sweep
        @param item: treeviewitem
        :author: dz, 21.07.2022
        @return:

        
        self.time = None

        split_view = 1

        fig = self.canvas.figure
        fig.clf()


        data_request_information = item.data(3, 0)
        self.data = self.online_manager.get_sweep_data_array_from_dat_file(data_request_information)

        print(self.data)
        meta_data_dict = item.data(5, 0)
        print(meta_data_dict)

        if self.time is None:
            self.time = self.get_time_from_dict(meta_data_dict)
            # recording_mode = self.get_recording_mode(meta_data_array)

            self.y_unit = self.get_y_unit_from_meta_data_dict(meta_data_dict)

            print(self.y_unit)

            if self.y_unit == "V":
                y_min, y_max = self.get_y_min_max_meta_data_dict_values(meta_data_dict)
                self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))
                self.plot_scaling_factor = 1000
            else:
                # data scaling to nA
                self.plot_scaling_factor = 1e9


        self.ax1.plot(self.time, self.data * self.plot_scaling_factor, c='yellow', alpha = 0.5)

        print("plotting sweep")
        print(item.text(0))

        sweep_number = item.text(0).split("Sweep")
        sweep_number = int(sweep_number[1])
        # plot pgf traces
        protocol_steps = self.plot_pgf_signal(item.parent().data(5, 0), self.data,sweep_number)


        #@todo: fix this asap : len(protocol_steps)
        for x in range(0, 3):
            x_pos = int(protocol_steps[x] + sum(protocol_steps[0:x]))
            self.ax1.axvline(x_pos, c='tab:gray')

        self.vertical_layout.addWidget(self.canvas)
        self.handle_plot_visualization()
    """
    """
    def series_clicked_load_from_dat_file(self,item):
        
        plots trace data and pgf data after a series was clicked in the online analysis
        @param item:
        @return:
        :author: dz, 21.07.2022
        
        print("online analysis %s series was clicked", item.text(0))
        children = item.childCount()
        split_view = 1

        # reset the time array -> will be created new from the first sweep
        self.time = None
        self.y_unit = None


        fig = self.canvas.figure
        fig.clf()

        if split_view:
            # initialise the figure. here we share X and Y axis
            axes = self.canvas.figure.subplots(nrows=2, ncols=1, sharex=True, sharey=False)

            self.ax1 = axes[0]
            self.ax2 = axes[1]
        else:
            self.ax1 = self.canvas.figure.subplots()
            self.ax2 = self.ax1.twinx()

        # plot data traces for this series
        for c in range(0, children):

            child = item.child(c)
            #child.setCheckState(1, Qt.Checked)
            data_request_information = child.data(3, 0)
            self.data = self.online_manager.get_sweep_data_array_from_dat_file(data_request_information)
            meta_data_dict = child.data(5, 0)

            if self.time is None:
                self.time = self.get_time_from_dict(meta_data_dict)
                #recording_mode = self.get_recording_mode(meta_data_array)

                self.y_unit = self.get_y_unit_from_meta_data_dict(meta_data_dict)

                print(self.y_unit)

            if self.y_unit == "V":
                y_min, y_max = self.get_y_min_max_meta_data_dict_values(meta_data_dict)
                self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))
                self.plot_scaling_factor = 1000
            else:
                # data scaling to nA
                self.plot_scaling_factor = 1e9

            self.ax1.plot(self.time,self.data*self.plot_scaling_factor, c='k')

        # plot pgf traces

        protocol_steps = self.plot_pgf_signal(item.data(5, 0), self.data)
        for x in range(0, len(protocol_steps)):
            x_pos = int(protocol_steps[x] + sum(protocol_steps[0:x]))
            self.ax1.axvline(x_pos, c='tab:gray')

        self.vertical_layout.addWidget(self.canvas)
        self.handle_plot_visualization()

    """
    """
    def series_clicked_load_from_dat_file(self,item):
        
        plots trace data and pgf data after a series was clicked in the online analysis
        @param item:
        @return:
        :author: dz, 21.07.2022
         
        print("online analysis %s series was clicked", item.text(0))
        children = item.childCount()
        split_view = 1

        # reset the time array -> will be created new from the first sweep
        self.time = None
        self.y_unit = None


        fig = self.canvas.figure
        fig.clf()

        if split_view:
            # initialise the figure. here we share X and Y axis
            axes = self.canvas.figure.subplots(nrows=2, ncols=1, sharex=True, sharey=False)

            self.ax1 = axes[0]
            self.ax2 = axes[1]
        else:
            self.ax1 = self.canvas.figure.subplots()
            self.ax2 = self.ax1.twinx()

        # plot data traces for this series
        for c in range(0, children):

            child = item.child(c)
            #child.setCheckState(1, Qt.Checked)
            data_request_information = child.data(3, 0)
            self.data = self.online_manager.get_sweep_data_array_from_dat_file(data_request_information)
            meta_data_dict = child.data(5, 0)

            if self.time is None:
                self.time = self.get_time_from_dict(meta_data_dict)
                #recording_mode = self.get_recording_mode(meta_data_array)

                self.y_unit = self.get_y_unit_from_meta_data_dict(meta_data_dict)

                print(self.y_unit)

            if self.y_unit == "V":
                y_min, y_max = self.get_y_min_max_meta_data_dict_values(meta_data_dict)
                self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))
                self.plot_scaling_factor = 1000
            else:
                    # data scaling to nA
                self.plot_scaling_factor = 1e9

            self.ax1.plot(self.time,self.data*self.plot_scaling_factor, c='k')

        # plot pgf traces

        protocol_steps = self.plot_pgf_signal(item.data(5,0),self.data)
        for x in range(0, len(protocol_steps)):
            x_pos = int(protocol_steps[x] + sum(protocol_steps[0:x]))
            self.ax1.axvline(x_pos, c='tab:gray')

        self.vertical_layout.addWidget(self.canvas)
        self.handle_plot_visualization()

    """


    def table_view_sweep_clicked_load_from_database(self, experiment_name, series_identifier, sweep_name):
        """
        visualizes the sweep when clicked on it in the treeview
        @param item: treeview item, contains text at pos 0 and data request information at pos 3,0
        @return:
        :author: dz, modified 29.09.2022
        """
        print("sweep clicked")
        print(experiment_name)
        print(series_identifier)
        print(sweep_name)
        split_view = 1

        experiment_name = experiment_name.split("::")
        experiment_name = experiment_name[len(experiment_name)-1]
        series_identifier = series_identifier.split("::")
        series_identifier = series_identifier[len(series_identifier)-1]
        series_df = self.database_handler.get_sweep_table_for_specific_series(experiment_name, series_identifier)
        print(series_df)
        # get the meta data to correctly display y values of traces
        meta_data_df = self.database_handler.get_meta_data_table_of_specific_series(experiment_name,
                                                                 series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)

        self.time = self.get_time_from_meta_data(meta_data_df)

        self.create_new_subplots(split_view)

        data = series_df[sweep_name].values.tolist()
        data = np.array(data)

        if self.y_unit == "V":
            y_min, y_max = self.get_y_min_max_meta_data_values(meta_data_df, sweep_name)
            data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
            # data scaling to mV
            self.plot_scaling_factor = 1000
        else:
            # data scaling to nA
            self.plot_scaling_factor = 1e9

        self.ax1.plot(self.time, data * self.plot_scaling_factor, 'black')

        self.handle_plot_visualization()

        pgf_table_df = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name,
                                                                                        series_identifier)

        sweep_number = sweep_name.split("_")
        sweep_number = int(sweep_number[1])

        protocol_steps = self.plot_pgf_signal(pgf_table_df, data, sweep_number)

        print("Protocol Steps")
        print(protocol_steps)

        # @todo fix this asap replace 3 by len(protocol_steps)
        for x in range(0, 3):
            x_pos = int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            self.ax1.axvline(x_pos, c='tab:gray')

        self.handle_plot_visualization()

    def table_view_series_clicked_load_from_database(self,experiment_name, series_identifier):

        """new function"""

        print("plotting started")

        experiment_name = experiment_name.split("::")
        experiment_name = experiment_name[len(experiment_name)-1]
        print(experiment_name)

        series_identifier = series_identifier.split("::")
        series_identifier = series_identifier[len(series_identifier)-1]
        print(series_identifier)
        split_view = 1


        series_df = self.database_handler.get_sweep_table_for_specific_series(experiment_name, series_identifier)

        #print("requested series dataframe")
        #print(series_df)

        #self.time = db.get_time_in_ms_of_analyzed_series(data_request_information[0],data_request_information[1])

        # get the meta data to correctly display y values of traces
        meta_data_df = self.database_handler.get_meta_data_table_of_specific_series(experiment_name, series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)
        self.time = self.get_time_from_meta_data(meta_data_df)

        column_names = series_df.columns.values.tolist()

        self.create_new_subplots(split_view)

        # plot for each sweep
        for name in column_names:
            data = series_df[name].values.tolist()
            data = np.array(data)

            if self.y_unit == "V":
                y_min, y_max = self.get_y_min_max_meta_data_values(meta_data_df,name)
                data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
                # data scaling to mV
                self.plot_scaling_factor = 1000
            else:
                # data scaling to nA
                self.plot_scaling_factor = 1e9

            self.ax1.plot(self.time, data * self.plot_scaling_factor, 'k')

            """
            if self.detection_mode:
                peaks, _ = find_peaks(data, height = 0.00,distance=200)
                print('peaks')
                print(peaks)
                self.plot_widget.plot(self.time[peaks], data[peaks],pen=None, symbol='o')
            """

        # finally also the pgf file needs to be added to the plot
        # load the table
        pgf_table = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name, series_identifier)
        pgf_table = pgf_table[pgf_table["selected_channel"] == "1"]

        protocol_steps = self.plot_pgf_signal(pgf_table,data)
    
        for x in range(0,len(protocol_steps)):

            x_pos =  int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            self.ax1.axvline(x_pos, c = 'tab:gray')
        
        self.vertical_layout.addWidget(self.canvas)
        self.handle_plot_visualization()

    def create_new_subplots(self, split_view):
        """
        create new subplots for data and pgf view
        """
        fig = self.canvas.figure
        fig.clf()

        if split_view:
            # initialise the figure. here we share X and Y axis
            axes = self.canvas.figure.subplots(nrows=2, ncols=1, sharex=True, sharey=False)

            self.ax1 = axes[0]
            self.ax2 = axes[1]
        else:
            self.ax1 = self.canvas.figure.subplots()
            self.ax2 = self.ax1.twinx()         
 
    def handle_plot_visualization(self):
        """
        handle visualizations of the data and pgf plot
        @return:
        @author: dz, 21.07.2022
        """
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)
        self.ax2.spines['top'].set_visible(False)
        self.ax2.spines['right'].set_visible(False)
        #self.ax1.patch.set_alpha(0)
        #self.ax2.patch.set_alpha(0)


        # todo check for white or dakr mode
        ax_color = 'black'
        self.ax1.spines['bottom'].set_color(ax_color)
        self.ax1.spines['left'].set_color(ax_color)
        self.ax1.xaxis.label.set_color(ax_color)
        self.ax1.yaxis.label.set_color(ax_color)
        self.ax1.tick_params(axis='x', colors=ax_color)
        self.ax1.tick_params(axis='y', colors=ax_color)


        self.ax2.spines['bottom'].set_color(ax_color)
        self.ax2.spines['left'].set_color(ax_color)
        self.ax2.xaxis.label.set_color(ax_color)
        self.ax2.yaxis.label.set_color(ax_color)
        self.ax2.tick_params(axis='x', colors=ax_color)
        self.ax2.tick_params(axis='y', colors=ax_color)
        
        #plt.subplots_adjust(left=0.8, right=0.9, bottom=0.8, top=0.9)
        #self.ax1.autoscale()
        #self.ax2.autoscale()
        #self.canvas.figure.tight_layout()

        #self.canvas.figure.patch.set_alpha(0)
        #self.canvas.figure.tight_layout()
        self.ax2.set_xlabel('Time [ms]')
        if self.y_unit == "V":
            self.ax1.set_ylabel('Voltage [mV]')
            self.ax2.set_ylabel('Current [pA]')
        else:
            self.ax1.set_ylabel('Current [nA]')
            self.ax2.set_ylabel('Voltage [mV]')

        self.canvas.draw_idle()

    def plot_pgf_signal(self,pgf_table_df,data,sweep_number=None):
        """
        Function to decide whether step protocol or simple protocol needs to be created
        @param pgf_table_df:
        @param data:
        @return:
        @author: dz, 21.07.2022
        """
        increments = pgf_table_df['increment'].values.tolist()
        increments = np.array(increments, dtype=float)

        if np.all(increments ==0):
            return self.plot_pgf_simple_protocol(pgf_table_df,data)
        else:
            return self.plot_pgf_step_protocol(pgf_table_df,data,sweep_number)

    def plot_pgf_step_protocol(self,pgf_table_df,data, sweep_number_of_interest = None):
        """
        Create plots for multiple single traces according to information from the pgf dataframe
        @param pgf_table_df:
        @param data:
        @return:
        @author: dz, 21.07.2022
        """

        if sweep_number_of_interest is not None:
            # @todo: better bugfix ?
            sweep_number_of_interest = sweep_number_of_interest - 1

        # is there one step interval or are there multiple ones ?
        increments = pgf_table_df['increment'].values.tolist()
        increments = np.array(increments, dtype=float)

        # according to the number n of intervals sweep_number * n signals need to be created
        increment_intervals = np.where(increments>0)[0]
        increment_interval_amount = len(increment_intervals)

        durations = pgf_table_df['duration'].values.tolist()
        voltages = pgf_table_df['voltage'].values.tolist()
        holding = pgf_table_df['holding_potential'].values.tolist()


        number_of_sweeps = pgf_table_df['sweep_number'].values.tolist()

        for sweep_number in range(0,int(number_of_sweeps[0])):

            pgf_signal = np.zeros(len(data))
            total_duration = 0
            start_pos = 0
            protocol_steps = []

            for n in range(0, len(durations)):
                #  nothign changes in the duration
                d = 1000 * float(durations[n])
                total_duration += d
                protocol_steps.append(d)
                try:
                    end_pos = np.where(self.time > total_duration)[0][0]
                except IndexError:
                    # print("index error")
                    end_pos = len(data)

                print(n)
                print(start_pos)
                print(end_pos)

                if increments[n]>0:
                    print(1000 * float(voltages[n]) + sweep_number *  1000 * float(increments[n]))
                    pgf_signal[start_pos:end_pos] = 1000 * float(voltages[n]) + sweep_number *  1000 * float(increments[n])
                else:
                    if float(voltages[n]) == 0:
                        pgf_signal[start_pos:end_pos] = 1000 * float(holding[n])
                        print(1000 * float(holding[n]))
                    else:
                        pgf_signal[start_pos:end_pos] = 1000 * float(voltages[n])
                        print(1000*float(voltages[n]))

                start_pos = end_pos

            if sweep_number_of_interest is not None:
                if sweep_number != sweep_number_of_interest:
                    self.ax2.plot(self.time, pgf_signal, c='tab:gray')
                else:
                    self.ax2.plot(self.time, pgf_signal, c='r')
            else:
                self.ax2.plot(self.time, pgf_signal, c='k')
            print("finished sweep %s", sweep_number)

        return protocol_steps

    def plot_pgf_simple_protocol(self,pgf_table_df, data):
        """
        create a simple pgf trace signal
        @param pgf_table_df: df containign pgf information
        @param data:
        @return:
        @author: dz, 21.07.2022
        """

        # concat the y points where in the data plot slight grey lines should be drawn do indicate start of a pulse
        protocol_steps = []

        pgf_signal = np.zeros(len(data))

        try:
            # create traces

            durations = pgf_table_df['duration'].values.tolist()
            voltages = pgf_table_df['voltage'].values.tolist()
            holding = pgf_table_df['holding_potential'].values.tolist()
            total_duration = 0
            start_pos = 0
            for n in range(0,len(durations)):
                d = 1000 * float(durations[n])
                total_duration += d
                protocol_steps.append(d)

                try:
                    end_pos = np.where(self.time > total_duration)[0][0]
                except IndexError:
                    #print("index error")
                    end_pos = len(data)
                print(end_pos)
                if float(voltages[n])==0:
                    pgf_signal[start_pos:end_pos] = 1000 * float(holding[n])
                else:
                    pgf_signal[start_pos:end_pos] = 1000 * float(voltages[n])
                start_pos = end_pos

        except Exception as e:
            print(e)

        self.ax2.plot(self.time, pgf_signal, c = 'k')

        return protocol_steps

    def get_recording_mode(self,meta_data):
        meta_dict = self.get_dict(meta_data)
        print(meta_dict)
        byte_repr = meta_dict.get('RecordingMode')
        print("found", byte_repr)
        if byte_repr == 3:
            print("recording mode : Voltage Clamp")
            return "Voltage Clamp"
        else:
            print("recording mode : Current Clamp")
            return "Current Clamp"

    def get_y_min_max_meta_data_values(self,meta_data_frame,sweep_name):
        """
        Return specific ymin and ymax for each sweep
        :param meta_data_frame:
        :param sweep_name:
        :return:
        """
        pos = meta_data_frame['Parameter'].tolist().index('Ymin')
        y_min = meta_data_frame[sweep_name].tolist()[pos]

        pos = meta_data_frame['Parameter'].tolist().index('Ymax')
        y_max = meta_data_frame[sweep_name].tolist()[pos]

        return float(y_min), float(y_max)

    def get_dict(self,meta_data):
        """ checks type of meta_data and returns anyway the dictionary of the meta data array"""
        if not isinstance(meta_data, dict):
            return dict(meta_data)
        else:
           return meta_data

    def get_y_min_max_meta_data_dict_values(self,meta_data_dict):

        y_min = float(meta_data_dict.get('Ymin'))
        y_max = float(meta_data_dict.get('Ymax'))

        return y_min,y_max

    def get_y_unit_from_meta_data_dict(self,meta_data_dict):
        return meta_data_dict.get('YUnit')

    def get_y_unit_from_meta_data(self,meta_data_frame):
        """
        YUnit is equal for all sweeps
        :param meta_data:
        :return:
        """
        ind = meta_data_frame['Parameter'].tolist().index('YUnit')
        return meta_data_frame['sweep_1'].tolist()[ind]

    def get_time_from_dict(selfself,dict):
        x_start = float(dict.get('XStart'))
        x_interval = float(dict.get('XInterval'))
        number_of_datapoints = int(dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def get_time_from_meta_data(self,meta_data_frame):
        """
        handle database loading with a data frame
        @param meta_data_frame:
        @return:
        """
        x_start_pos = meta_data_frame['Parameter'].tolist().index('XStart')

        x_interval_pos = meta_data_frame['Parameter'].tolist().index('XInterval')

        number_of_points_pos = meta_data_frame['Parameter'].tolist().index('DataPoints')


        x_start= float(meta_data_frame['sweep_1'].tolist()[x_start_pos])
        x_interval = float(meta_data_frame['sweep_1'].tolist()[x_interval_pos])
        number_of_datapoints = int(meta_data_frame['sweep_1'].tolist()[number_of_points_pos])
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        print("Xinterval = %d", x_start)
        print("Xinterval = %d", x_interval)
        print("Xinterval = %d", number_of_datapoints)
        return time

    def create_dragable_lines(self,row_col_tuple):
        """
        """

        print("creating new dragable lines")
        left_val =  0.2*max(self.time) +  5* (row_col_tuple[0] + row_col_tuple[1])
 
        right_val = 0.8*max(self.time) +  5 * (row_col_tuple[0] + row_col_tuple[1])

        left_coursor = DraggableLines(self.ax1, "v", left_val, self.canvas, self.left_bound_changed,row_col_tuple, self.plot_scaling_factor)
        right_coursor  = DraggableLines(self.ax1, "v", right_val, self.canvas, self.right_bound_changed,row_col_tuple, self.plot_scaling_factor)

        self.left_coursor = left_coursor
        self.right_coursor = right_coursor

        print("adding", row_col_tuple, " to the dict")
        self.coursor_bound_tuple_dict[row_col_tuple] = (self.left_coursor,self.right_coursor)
        print(self.coursor_bound_tuple_dict.keys())

    
        self.canvas.draw_idle()

        return left_val,right_val

    def show_draggable_lines(self,row_col_tuple,positions = None):
        """
        showing existing courspr bounds
        @param row_number:
        @return:
        """
        coursor_tuple = self.coursor_bound_tuple_dict.get(row_col_tuple)
                
        left_val = coursor_tuple[0].XorY
        right_val = coursor_tuple[1].XorY

        self.left_coursor  =  DraggableLines(self.ax1, "v", left_val, self.canvas, self.left_bound_changed,row_col_tuple, self.ax1.get_ylim())
        self.right_coursor  = DraggableLines(self.ax1, "v", right_val, self.canvas, self.right_bound_changed,row_col_tuple, self.ax1.get_ylim())

        self.coursor_bound_tuple_dict.pop(row_col_tuple)
        self.coursor_bound_tuple_dict[row_col_tuple] = (self.left_coursor,self.right_coursor)

        # coursor_tuple[0]# 
        # coursor_tuple[1] # 

        #left_coursor.c = self.canvas
        #left_coursor.draw_line_on_ax(self.ax1)
        #left_coursor.redraw()
        #right_coursor.redraw()

        self.canvas.draw_idle()


                
    def on_press(self,event):
        self.left_coursor.clickonline(event)
        self.right_coursor.clickonline(event)

    def remove_dragable_lines(self,row):
        print("row number")
        print(row)
        print(self.coursor_bound_tuple_dict)
        try:

            tuples_to_remove = []
            for k in self.coursor_bound_tuple_dict.keys():
                if k[0]==row:
                    tuples_to_remove.append(k)

            for t in tuples_to_remove:

                coursor_tuple = self.coursor_bound_tuple_dict.get(t)
                self.ax1.lines.remove(coursor_tuple[0].line)
                self.ax1.lines.remove(coursor_tuple[1].line)
                #self.coursor_bound_tuple_dict.pop(t)

            self.canvas.draw_idle()
        except Exception as e:
            print("all good")
            print(e)



# from QCore
class CursorBoundSignal(QObject):
    cursor_bound_signal = Signal(tuple)