from PySide6 import QtCore
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from treeview_manager import *
import pyqtgraph as pg
import numpy as np
from scipy.signal import find_peaks

from draggable_lines import DraggableLines
sys.path.append(os.path.dirname(os.getcwd()) + "/src/Offline_Analysis")
from DavesSuperPersonalCustomToolbar import *
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from mpl_interactions import ioff, panhandler, zoom_factory

from PySide6.QtCore import Signal
# inheritage from qobject required for use of signal


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

        #vertical_layout_widget = QVBoxLayout()

        self.detection_mode = detection

        try:
            print("removed old widget")
            vertical_layout_widget.takeAt(0)

        except Exception as e:
            print(e)

        self.canvas = FigureCanvas(Figure(figsize=(3,3)))
        self.navbar = DavesSuperPersonalCustomToolbar(self.canvas,parent = toolbar_widget) #self.navbar_widget)

        """
        self.navbar.clear()

        # Adds Buttons
        a = self.navbar.addAction(self.navbar._icon("home.png"), "Home", self.navbar.home)
        # a.setToolTip('returns axes to original position')
        a = self.navbar.addAction(self.navbar._icon("move.png"), "Pan", self.navbar.pan)

        # Fixed with, otherwise navigation bar resize arbitrary
        self.navbar.setFixedWidth(40)
        """

        self.navbar.setOrientation(QtCore.Qt.Vertical)
        #self.navbar.setStyleSheet("background-color:White; border : 0px; ")

        #self.navbar.resize(50,500)
        vertical_layout_widget.addWidget(self.canvas)
        print("toolbar")
        try:
            print("toolbar horizontal space")
            #toolbar_layout.addWidget(toolbar_widget, Qt.AlignCenter)
        except Exception as e:
            print(e)


        #new = QPushButton(toolbar_widget)
        #
        #toolbar_layout.setAlignment(QtCore.Qt.AlignTop)
        self.navbar.show()


        print("added new widget")

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

    def sweep_clicked(self,item):
        """Whenever a sweep is clicked, this handler will be executed to handle the clicked item"""
        self.plot_widget.clear()
        if not item.checkState(1):
            item.setCheckState(1, Qt.Checked)

            # get the data of the clicked sweep
            # data can be either information about the database request if mode == offline analysis
            # data can be an array of the position in the bundle to read the data
            data_request_information = item.data(3,0)
            self.offline_analysis_canvas = pg.PlotWidget()



            self.offline_analysis_canvas.setBackground("#282629")

            if self.analysis_mode == 0:
                data = self.online_manager.get_sweep_data_array_from_dat_file(data_request_information)
                meta_data = item.data(5,0)
            else:
                db = self.offline_manager.get_database()
                data = db.get_single_sweep_data_from_database(data_request_information)

            self.time = np.linspace(0, len(data) - 1, len(data))

            # modified
            self.plot_widget.plot(self.time,data)
            self.plot_widget.plotItem.setMouseEnabled(x=True,y=True)

        else:
            item.setCheckState(1, Qt.Unchecked)

    def series_clicked_load_from_database(self,item):
        """
        When a series was clicked, data arrays all of its sweeps signal traces will be plotted.
        The data therefore will be loaded live from the database.
        :param item:
        :return:
        :author: dz, 29.06.2022
        """
        print("%s series was clicked", item.text(0))
        split_view = True
        series_name = item.text(0)

        # The data table will be pulled from the database from table 'experiment_series'.
        # the correct table name is identified by the tuple (experiment_name, series_identifier)
        # stored in the series item at position 3

        data_request_information = item.data(3, 0)

        db = self.offline_manager.get_database()
        series_df = db.get_sweep_table_for_specific_series(data_request_information[0],data_request_information[1])

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
            pan_handler = panhandler(self.canvas.figure)
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

        print(pgf_table_df)

        protocol_steps = self.plot_pgf_signal(pgf_table_df,data)
        print(protocol_steps)
        for x in range(0,len(protocol_steps)):

            x_pos =  int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            self.ax1.axvline(x_pos, c = 'tab:gray')

        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)
        self.ax2.spines['top'].set_visible(False)
        self.ax2.spines['right'].set_visible(False)
        self.ax2.set_xlabel('Time [ms]')
        if self.y_unit == "V":
            self.ax1.set_ylabel('Voltage [mV]')
            self.ax2.set_ylabel('Current [pA]')
        else:
            self.ax1.set_ylabel('Current [nA]')
            self.ax2.set_ylabel('Voltage [mV]')
        self.canvas.draw_idle()

        #self.canvas.show()

    def plot_pgf_signal(self,pgf_table_df,data):
        """
        Function to decide whether step protocol or simple protocol needs to be created
        @param pgf_table_df:
        @param data:
        @return:
        """
        increments = pgf_table_df['increment'].values.tolist()
        increments = np.array(increments, dtype=float)

        if np.all(increments ==0):
            return self.plot_pgf_simple_protocol(pgf_table_df,data)
        else:
            return self.plot_pgf_step_protocol(pgf_table_df,data)

    def plot_pgf_step_protocol(self,pgf_table_df,data):

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


            self.ax2.plot(self.time, pgf_signal, c = 'k')
            print("finished sweep %s", sweep_number)
        return protocol_steps
    def plot_pgf_simple_protocol(self,pgf_table_df, data):
        """
        create a simple pgf trace signal
        @param pgf_table_df:
        @param data:
        @return:
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

    # deprecated dz 30.06.2022
    def series_clicked(self,item):
        self.plot_widget.clear()
        print("series clicked")
        children = item.childCount()
        series_name = item.text(0)
        # reset the time array -> will be created new from the first sweep
        self.time = None
        if not item.checkState(1):
            # go through the tree and uncheck all

            if self.analysis_mode == 0:
                db = None
            else:
                db = self.offline_manager.get_database()

            # tree view manager can handle none db object
            TreeViewManager(db).uncheck_entire_tree(self.tree_view)
            item.setCheckState(1, Qt.Checked)

            for c in range(0,children):

                child = item.child(c)
                child.setCheckState(1, Qt.Checked)
                data_request_information = child.data(3,0)

                if self.analysis_mode == 0:
                    data = self.online_manager.get_sweep_data_array_from_dat_file(data_request_information)
                    meta_data_array = child.data(5,0)
                else:
                    # get data as numpy array
                    data = db.get_single_sweep_data_from_database(data_request_information)

                    # get meta data as dict {'key':['value'], .. .}
                    meta_data_array = db.get_single_sweep_meta_data_from_database(data_request_information)
                    debug  = 0


                # only calc the time once for all sweeps
                if self.time is None:
                    self.time = self.get_time_from_meta_data(meta_data_array)
                    recording_mode = self.get_recording_mode(meta_data_array)
                    '''
                    if self.analysis_mode:
                        self.offline_manager.write_ms_spaced_time_array_to_analysis_series_table(self.time,series_name)
                        self.offline_manager.write_recording_mode_to_analysis_series_table(recording_mode,series_name)
                    '''
                    self.y_unit = self.get_y_unit_from_meta_data(meta_data_array)

                if self.y_unit == "V":
                    y_min,y_max=self.get_y_min_max_meta_data_values(meta_data_array)
                    data = np.interp(data, (data.min(), data.max()), (y_min,y_max))

                self.plot_widget.plot(self.time, data)
                self.plot_widget.plotItem.setMouseEnabled(x=True, y=True)
                #y_axis_item = pg.AxisItem(orientation='left',units = self.y_unit)
                #y_axis_item.enableAutoSIPrefix(True)
                #self.plot_widget.addItem(y_axis_item)
                self.plot_widget.setLabel(axis='left', text=self.y_unit)
                self.plot_widget.setLabel(axis='bottom', text='Time (ms)')




        else:
            item.setCheckState(1,Qt.Unchecked)
            for c in range(0, children):
                item.child(c).setCheckState(1, Qt.Unchecked)

    def get_recording_mode(self,meta_data):
        meta_dict = self.get_dict(meta_data)
        print(meta_dict)
        byte_repr = meta_dict.get('RecordingMode')
        print("found", byte_repr)
        if byte_repr == b'\x03':
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

    def get_y_unit_from_meta_data(self,meta_data_frame):
        """
        YUnit is equal for all sweeps
        :param meta_data:
        :return:
        """
        ind = meta_data_frame['Parameter'].tolist().index('YUnit')
        return meta_data_frame['sweep_1'].tolist()[ind]


    def get_time_from_meta_data(self,meta_data_frame):
        x_start_pos = meta_data_frame['Parameter'].tolist().index('XStart')
        x_interval_pos = meta_data_frame['Parameter'].tolist().index('XInterval')
        number_of_points_pos = meta_data_frame['Parameter'].tolist().index('DataPoints')

        x_start= float(meta_data_frame['sweep_1'].tolist()[x_start_pos])
        x_interval = float(meta_data_frame['sweep_1'].tolist()[x_interval_pos])
        number_of_datapoints = int(meta_data_frame['sweep_1'].tolist()[number_of_points_pos])
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def tree_view_click_handler(self, item):

        print(f'Text of first column in item is {item.text(0)}')

        try:
            if "Sweep" in item.text(0):
                self.sweep_clicked(item)
            else:
                if ".dat" in item.text(0):
                    print("To see data traces, click on a sweep or a series")
                else:
                 self.series_clicked_load_from_database(item)
                 #self.series_clicked(item)
        except Exception as e:
            print(e)
            print("experiment or sweep was clicked which is not implemented yet")

    def show_draggable_lines(self,row_number):

        try:
            coursor_tuple = self.coursor_bound_tuple_dict.get(str(row_number))
            left_val = round(coursor_tuple[0].XorY,2)
            right_val = round(coursor_tuple[1].XorY,2)
        except:
            # default
            left_val =  0.2*max(self.time)
            right_val = 0.8*max(self.time)

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

        try:
            coursor_tuple = self.coursor_bound_tuple_dict.get(str(row))
            self.ax1.lines.remove(coursor_tuple[0].line)
            self.ax1.lines.remove(coursor_tuple[1].line)

            self.coursor_bound_tuple_dict.pop(str(row))

            self.canvas.draw_idle()
        except Exception as e:
            print("all good")
            print(e)

        #self.plot_widget.removeItem(self.left_coursor)
        #self.plot_widget.removeItem(self.right_cursor)


# from QCore
class CursorBoundSignal(QObject):
    cursor_bound_signal = Signal(tuple)