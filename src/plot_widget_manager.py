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
    def __init__(self,vertical_layout_widget,offline_manager,tree_view):



        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setStyleSheet('dark_blue.xml')
        vertical_layout_widget.takeAt(0)
        vertical_layout_widget.insertWidget(0,self.plot_widget)
        self.tree_view = tree_view
        self.offline_manager = offline_manager
        self.time = None
        # neccessary ?
        super().__init__()
        self.left_bound_changed = CursorBoundSignal()


    def sweep_clicked(self,item):
        self.plot_widget.clear()
        if not item.checkState(1):
            item.setCheckState(1, Qt.Checked)
            db_request_data = item.data(3,0)
            self.offline_analysis_canvas = pg.PlotWidget()

            self.offline_analysis_canvas.setBackground("#282629")
            db = self.offline_manager.get_database()
            data = db.get_single_sweep_data_from_database(db_request_data)
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

        # reset the time array -> will be created new from the first sweep
        self.time = None
        if not item.checkState(1):
            # go through the tree and uncheck all
            db = self.offline_manager.get_database()
            TreeViewManager(db).uncheck_entire_tree(self.tree_view)
            item.setCheckState(1, Qt.Checked)

            for c in range(0,children):

                item.child(c).setCheckState(1, Qt.Checked)
                database_search_data = item.child(c).data(3,0)
                data = db.get_single_sweep_data_from_database(database_search_data)
                meta_data_array = db.get_single_sweep_meta_data_from_database(database_search_data)

                # only calc the time once for all sweeps
                if self.time is None:
                    self.time = self.get_time_from_meta_data(meta_data_array)

                self.plot_widget.plot(self.time, data)
                self.plot_widget.plotItem.setMouseEnabled(x=True, y=True)

        else:
            item.setCheckState(1,Qt.Unchecked)
            for c in range(0, children):
                item.child(c).setCheckState(1, Qt.Unchecked)

    def get_time_from_meta_data(self,meta_data_array):
        meta_dict = dict(meta_data_array)
        print(meta_dict)
        x_start = float(meta_dict.get('XStart'))
        x_interval = float(meta_dict.get('XInterval'))
        number_of_datapoints = int(meta_dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def tree_view_click_handler(self, item):
        print('Text of first column in item is ', item.text(0))

        if "Sweep" in item.text(0):
            self.sweep_clicked(item)
        else:
            if ".dat" in item.text(0):
                print("To see data traces, click on a sweep or a series")
            else:
             self.series_clicked(item)

    def show_draggable_lines(self):
        left_val =  0.2*max(self.time)
        right_val = 0.8*max(self.time)

        self.left_coursor = pg.InfiniteLine(movable=True)
        self.left_coursor.setValue(left_val)
        self.right_cursor = pg.InfiniteLine(movable=True)
        self.right_cursor.setValue(right_val)

        self.left_coursor.sigPositionChangeFinished.connect(self.draggable_left_cursor_moved)
        self.plot_widget.addItem(self.left_coursor)
        self.plot_widget.addItem(self.right_cursor)
        self.left_coursor.sigPositionChangeFinished.connect(self.draggable_right_cursor_moved)
        return left_val,right_val


    def draggable_left_cursor_moved(self):
        print("the line was moved ", self.left_coursor.value())

        # update labels, therefore return a signal to the main offline analysis widget which will be connected to an update function there
        self.left_bound_changed.cursor_bound_signal.emit(self.left_coursor.value())

    def draggable_right_cursor_moved(self):
        print("the line was moved ", self.left_coursor.value())
        # update labels

# needed to use an instance of this signal class in the offline main widget
class CursorBoundSignal(QtCore.QObject):
    cursor_bound_signal = QtCore.Signal(float)