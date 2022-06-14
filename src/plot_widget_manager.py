from PySide6 import QtCore
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from treeview_manager import *
import pyqtgraph as pg
import numpy as np
from PySide6.QtCore import Signal
# inheritage from qobject required for use of signal
class PlotWidgetManager(QtCore.QRunnable):
    """ A class to handle a specific plot widget and it'S appearance, subfunctions, cursor bounds, .... """

    def __init__(self,vertical_layout_widget,manager_object,tree_view,mode):
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



        print("removed old widget")
        vertical_layout_widget.takeAt(0)

        # add the new plot widget
        vertical_layout_widget.insertWidget(0,self.plot_widget)

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
        self.plot_widget.setBackground("#232629")
        self.plot_widget.setBackground('e6e6e6')
        self.plot_widget.getAxis('left').setPen('#f57505')
        self.plot_widget.getAxis('bottom').setPen('#f57505')
        self.plot_widget.getAxis('left').setTextPen('#f57505')
        self.plot_widget.getAxis('bottom').setTextPen('#f57505')



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

    def get_y_min_max_meta_data_values(self,meta_data):
        meta_dict= self.get_dict(meta_data)
        y_min = float(meta_dict.get('Ymin'))
        y_max = float(meta_dict.get('Ymax'))
        return y_min,y_max

    def get_dict(self,meta_data):
        """ checks type of meta_data and returns anyway the dictionary of the meta data array"""
        if not isinstance(meta_data, dict):
            return dict(meta_data)
        else:
           return meta_data

    def get_y_unit_from_meta_data(self,meta_data):
        meta_dict = self.get_dict(meta_data)
        return meta_dict.get('YUnit')

    def get_time_from_meta_data(self,meta_data):
        meta_dict = self.get_dict(meta_data)
        x_start = float(meta_dict.get('XStart'))
        x_interval = float(meta_dict.get('XInterval'))
        number_of_datapoints = int(meta_dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def tree_view_click_handler(self, item):
        print(f'Text of first column in item is {item.text(0)}')

        if "Sweep" in item.text(0):
            self.sweep_clicked(item)
        else:
            if ".dat" in item.text(0):
                print("To see data traces, click on a sweep or a series")
            else:
             self.series_clicked(item)

    def show_draggable_lines(self,row_number):
        left_val =  0.2*max(self.time)
        right_val = 0.8*max(self.time)

        self.left_coursor = pg.InfiniteLine(movable=True)
        self.left_coursor.setValue(left_val)
        self.right_cursor = pg.InfiniteLine(movable=True)
        self.right_cursor.setValue(right_val)

        self.row_number = row_number

        self.left_coursor.sigPositionChangeFinished.connect(self.draggable_left_cursor_moved)
        self.plot_widget.addItem(self.left_coursor)
        self.plot_widget.addItem(self.right_cursor)
        self.right_cursor.sigPositionChangeFinished.connect(self.draggable_right_cursor_moved)



        return left_val,right_val

    def remove_dragable_lines(self):
        self.plot_widget.removeItem(self.left_coursor)
        self.plot_widget.removeItem(self.right_cursor)
        self.left_coursor.clearMarkers()
        self.right_cursor.clearMarkers()

    def draggable_left_cursor_moved(self):
        print("the line was moved ", self.left_coursor.value())
        # update labels, therefore return a signal to the main offline analysis widget which will be connected to an update function there
        emit_tuple = (round(self.left_coursor.value(),2),self.row_number)
        print(emit_tuple)
        self.left_bound_changed.cursor_bound_signal.emit(emit_tuple)

    def draggable_right_cursor_moved(self):
        print("the line was moved ", self.right_cursor.value())
        emit_tuple = (round(self.right_cursor.value(),2),self.row_number)
        print(emit_tuple)
        self.right_bound_changed.cursor_bound_signal.emit(emit_tuple)

# needed to use an instance of this signal class in the offline main widget
class CursorBoundSignal(QtCore.QObject):
    cursor_bound_signal = QtCore.Signal(tuple)