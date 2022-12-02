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

    def __init__(self,vertical_layout_widget,manager_object,tree_view,mode,detection,toolbar_widget = None, toolbar_layout = None):
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

        """
        print("toolbar")
        try:
            print("toolbar horizontal space")
        except Exception as e:
            print(e)

       
        self.navbar.clear()

        # Adds Buttons
        a = self.navbar.addAction(self.navbar._icon("home.png"), "Home", self.navbar.home)
        # a.setToolTip('returns axes to original position')
        a = self.navbar.addAction(self.navbar._icon("move.png"), "Pan", self.navbar.pan)

        # Fixed with, otherwise navigation bar resize arbitrary
        self.navbar.setFixedWidth(40)
        
        """
        self.tree_view = tree_view
        self.analysis_mode = mode

        if self.analysis_mode == 0:
            self.online_manager = manager_object
        else:
            self.offline_manager = manager_object

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

        self.default_colors = ['white', 'g', 'c','r']

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
    def sweep_in_treeview_clicked(self,item):
        if self.analysis_mode == 0:
            self.sweep_clicked_load_from_dat_file(item)
        else:
            self.sweep_clicked_load_from_dat_database(item)
            self.check_live_analysis_plot(item,"sweep")

    def series_in_treeview_clicked(self,item):
        print("Item was clicked ", item.text(0))
        if self.analysis_mode == 0: # online analysis
            self.series_clicked_load_from_dat_file(item)
        else:
            self.series_clicked_load_from_database(item)
            self.check_live_analysis_plot(item,"series")


    def check_live_analysis_plot(self,item_text,experiment_name,identifier, level):
        """
        calculate values to be plotted in the "live plot" feature during analysis
        @param item:
        @param table_widget:
        @return:
        @author: dz, 29.09.2022
        """
        print("checking live analysis for item ", item_text)
        print(experiment_name)
        print(identifier)
        if self.analysis_functions_table_widget is not None:
            row_count = self.analysis_functions_table_widget.rowCount()
            # iterate through the rows of the table,
            print(row_count)
            for row in range(0,row_count):
                # check which checkboxes are selected
                fct_name = self.analysis_functions_table_widget.item(row, 0).text()
                print(fct_name)
                if self.analysis_functions_table_widget.cellWidget(row, 5).isChecked():
                    # calculate realted results and visualize
                    lower_bound = float(self.analysis_functions_table_widget.item(row, 1).text())
                    upper_bound = float(self.analysis_functions_table_widget.item(row, 2).text())
                    analysis_class_object = AnalysisFunctionRegistration().get_registered_analysis_class(fct_name)
                    db = self.offline_manager.get_database()
                    if level == "series":
                        x_y_tuple = analysis_class_object.live_data(lower_bound, upper_bound,experiment_name,identifier, db)
                    else:
                        x_y_tuple = analysis_class_object.live_data(lower_bound, upper_bound,experiment_name,identifier,db, item_text)

                    print(x_y_tuple)  # only works if parent = experiment
                    self.plot_scaling_factor = 1e9
                    if x_y_tuple is not None:
                        for tuple in x_y_tuple:
                            if isinstance(tuple[1],list):
                                y_val_list = [item * self.plot_scaling_factor for item in tuple[1]]
                                self.ax1.plot(tuple[0], y_val_list , c=self.default_colors[row], linestyle='dashed')
                            else:
                                self.ax1.plot(tuple[0], tuple[1]*self.plot_scaling_factor, c=self.default_colors[row], marker="o")
                    else:
                        print("Tuple was None: is live plot function for", fct_name, " already implemented ? ")
                else:
                    print("nothing to check in row %i", row)
        else:
            print("analysis_functions_table_widget was None ")


    def sweep_clicked_load_from_dat_file(self,item):
        """
        Whenever a sweep is clicked in online analysis, this handler will be executed to plot the selected sweep
        @param item: treeviewitem
        :author: dz, 21.07.2022
        @return:

        """
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

    def series_clicked_load_from_dat_file(self,item):
        """
        plots trace data and pgf data after a series was clicked in the online analysis
        @param item:
        @return:
        :author: dz, 21.07.2022
        """
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


    def series_clicked_load_from_dat_file(self,item):
        """
        plots trace data and pgf data after a series was clicked in the online analysis
        @param item:
        @return:
        :author: dz, 21.07.2022
        """
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
        db = self.offline_manager.get_database()
        series_df = db.get_sweep_table_for_specific_series(experiment_name, series_identifier)
        print(series_df)
        # get the meta data to correctly display y values of traces
        meta_data_df = db.get_meta_data_table_of_specific_series(experiment_name,
                                                                 series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)

        self.time = self.get_time_from_meta_data(meta_data_df)

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


        print("error here")
        print(series_df)
        print(sweep_name)

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

        self.ax1.plot(self.time, data * self.plot_scaling_factor, 'yellow', alpha=0.5)

        pgf_table_df = db.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name,
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

    """ @deprecated DZ 01.12.2022
    def series_clicked_load_from_database(self,item):
        
        When a series was clicked, data arrays all of its sweeps signal traces will be plotted.
        The data therefore will be loaded live from the database.
        :param item:
        :return:
        :author: dz, 29.06.2022
        
        print("%s series was clicked", item.text(0))
        split_view = True

        #self.navbar.setStyleSheet('align:center; background:#fff5cc;')
        self.vertical_layout.addWidget(self.canvas)

        series_name = item.text(0)


        # The data table will be pulled from the database from table 'experiment_series'.
        # the correct table name is identified by the tuple (experiment_name, series_identifier)
        # stored in the series item at position 3

        data_request_information = item.data(3, 0)


        db = self.offline_manager.get_database()
        series_df = db.get_sweep_table_for_specific_series(data_request_information[0],data_request_information[1])

        print("requested series dataframe")
        print(series_df)

        #self.time = db.get_time_in_ms_of_analyzed_series(data_request_information[0],data_request_information[1])

        # get the meta data to correctly display y values of traces
        meta_data_df = db.get_meta_data_table_of_specific_series(data_request_information[0],data_request_information[1])
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)
        self.time = self.get_time_from_meta_data(meta_data_df)

        column_names = series_df.columns.values.tolist()

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

            self.ax1.plot(self.time, data * self.plot_scaling_factor, 'k', label=name)

            if self.detection_mode:
                peaks, _ = find_peaks(data, height = 0.00,distance=200)
                print('peaks')
                print(peaks)
                self.plot_widget.plot(self.time[peaks], data[peaks],pen=None, symbol='o')


        # finally also the pgf file needs to be added to the plot
        # load the table
        pgf_table_df = db.get_entire_pgf_table_by_experiment_name_and_series_identifier(data_request_information[0],data_request_information[1])

        #print(pgf_table_df)

        protocol_steps = self.plot_pgf_signal(pgf_table_df,data)
        print("Protocol Steps")
        print(protocol_steps)
        for x in range(0,len(protocol_steps)):

            x_pos =  int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            #self.ax1.axvline(x_pos, c = 'tab:gray')

        self.handle_plot_visualization()
    """


    def table_view_series_clicked_load_from_database(self,experiment_name, series_identifier):

        """new function"""

        print("plotting started")
        print(experiment_name)
        print(series_identifier)

        split_view = 1

        db = self.offline_manager.get_database()
        series_df = db.get_sweep_table_for_specific_series(experiment_name, series_identifier)

        print("requested series dataframe")
        print(series_df)

        #self.time = db.get_time_in_ms_of_analyzed_series(data_request_information[0],data_request_information[1])

        # get the meta data to correctly display y values of traces
        meta_data_df = db.get_meta_data_table_of_specific_series(experiment_name, series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)
        self.time = self.get_time_from_meta_data(meta_data_df)

        column_names = series_df.columns.values.tolist()

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

            self.ax1.plot(self.time, data * self.plot_scaling_factor, 'k', label=name)

            if self.detection_mode:
                peaks, _ = find_peaks(data, height = 0.00,distance=200)
                print('peaks')
                print(peaks)
                self.plot_widget.plot(self.time[peaks], data[peaks],pen=None, symbol='o')


        # finally also the pgf file needs to be added to the plot
        # load the table
        pgf_table_df = db.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name, series_identifier)

        #print(pgf_table_df)

        protocol_steps = self.plot_pgf_signal(pgf_table_df,data)
        print("Protocol Steps")
        print(protocol_steps)
        for x in range(0,len(protocol_steps)):

            x_pos =  int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            #self.ax1.axvline(x_pos, c = 'tab:gray')

        self.handle_plot_visualization()
        self.vertical_layout.addWidget(self.canvas)

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
        self.ax1.patch.set_alpha(0)
        self.ax2.patch.set_alpha(0)

        self.ax1.spines['bottom'].set_color('white')
        self.ax1.spines['left'].set_color('white')
        self.ax1.xaxis.label.set_color('white')
        self.ax1.yaxis.label.set_color('white')
        self.ax1.tick_params(axis='x', colors='white')
        self.ax1.tick_params(axis='y', colors='white')

        self.ax2.spines['bottom'].set_color('white')
        self.ax2.spines['left'].set_color('white')
        self.ax2.xaxis.label.set_color('white')
        self.ax2.yaxis.label.set_color('white')
        self.ax2.tick_params(axis='x', colors='white')
        self.ax2.tick_params(axis='y', colors='white')

        plt.subplots_adjust(left=0.3, right=0.9, bottom=0.3, top=0.9)
        self.ax1.autoscale()
        self.ax2.autoscale()
        self.canvas.figure.tight_layout()

        self.canvas.figure.patch.set_alpha(0)
        self.canvas.figure.tight_layout()
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

    def show_draggable_lines(self,row_number,positions = None):
        """
        showing existing courspr bounds
        @param row_number:
        @return:
        """

        if positions is not None:
            print(row_number)
            print(self.coursor_bound_tuple_dict)

            left_val = positions[0]
            right_val = positions[1]

        else:

            try:
                coursor_tuple = self.coursor_bound_tuple_dict.get(str(row_number))
                left_val = round(coursor_tuple[0].XorY,2)
                right_val = round(coursor_tuple[1].XorY,2)

            except:
                # default
                print("not found")
                left_val =  0.2*max(self.time) +  5* row_number
                right_val = 0.8*max(self.time) +  5 * row_number

        left_coursor = DraggableLines(self.ax1, "v", left_val,self.canvas, self.left_bound_changed,row_number, self.plot_scaling_factor)
        right_coursor  = DraggableLines(self.ax1, "v", right_val,self.canvas, self.right_bound_changed,row_number, self.plot_scaling_factor)

        self.coursor_bound_tuple_dict[str(row_number)] = (left_coursor,right_coursor)

        self.left_coursor = left_coursor
        self.right_coursor = right_coursor

        self.canvas.draw_idle()

        return left_val,right_val

    def on_press(self,event):
        self.left_coursor.clickonline(event)
        self.right_coursor.clickonline(event)

    def remove_dragable_lines(self,row):
        print("row number")
        print(row)
        print(self.coursor_bound_tuple_dict)
        try:
            coursor_tuple = self.coursor_bound_tuple_dict.get(str(row))
            self.ax1.lines.remove(coursor_tuple[0].line)
            self.ax1.lines.remove(coursor_tuple[1].line)

            self.coursor_bound_tuple_dict.pop(str(row))

            self.canvas.draw_idle()
        except Exception as e:
            print("all good")
            print(e)



# from QCore
class CursorBoundSignal(QObject):
    cursor_bound_signal = Signal(tuple)