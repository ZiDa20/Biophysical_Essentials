# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pyqtgraph
from PySide6 import QtCore
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from offline_analysis_manager import OfflineManager
from data_db import *
from treeview_manager import *
from PySide6 import QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import numpy as np
from offline_analysis_designer_object import *

pg.setConfigOption('foreground','#448aff')

class Offline_Analysis(QWidget,offline_analysis_designer_object):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        self.blank_analysis_button.clicked.connect(self.start_another_function)
        self.select_directory_button.clicked.connect(self.open_directory)
        self.compare_series.clicked.connect(self.select_series_to_be_analized)

        self.offline_manager = OfflineManager()

    @Slot()
    def start_another_function(self):
        print("noch cooler")
        self.offline_analysis_widgets.setCurrentIndex(1)

    def sweep_clicked(self,item):
        self.plot_widget.clear()
        if not item.checkState(1):
            item.setCheckState(1, Qt.Checked)
            db_request_data = item.data(3,0)
            self.offline_analysis_canvas = pg.PlotWidget()
            self.offline_analysis_canvas.setBackground("#282629")
            db = self.offline_manager.get_database()
            data = db.get_single_sweep_data_from_database(db_request_data)
            time = np.linspace(0, len(data) - 1, len(data))

            # modified
            self.plot_widget.plot(time,data)
            self.plot_widget.plotItem.setMouseEnabled(x=True,y=True)

        else:
            item.setCheckState(1, Qt.Unchecked)


    def series_clicked(self,item):
        self.plot_widget.clear()
        print("series clicked")
        children = item.childCount()

        if not item.checkState(1):
            # go through the tree and uncheck all
            db = self.offline_manager.get_database()
            TreeViewManager(db).uncheck_entire_tree(self.experiments_tree_view)
            item.setCheckState(1, Qt.Checked)
            for c in range(0,children):
                item.child(c).setCheckState(1, Qt.Checked)
                db = self.offline_manager.get_database()
                data = db.get_single_sweep_data_from_database(item.child(c).data(3,0))
                time = np.linspace(0, len(data) - 1, len(data))
                self.plot_widget.plot(time, data)
                self.plot_widget.plotItem.setMouseEnabled(x=True, y=True)

        else:
            item.setCheckState(1,Qt.Unchecked)
            for c in range(0, children):
                item.child(c).setCheckState(1, Qt.Unchecked)

    def tree_view_click_handler(self, item):
        print('Text of first column in item is ', item.text(0))

        if "Sweep" in item.text(0):
            self.sweep_clicked(item)
        else:
            if ".dat" in item.text(0):
                print("To see data traces, click on a sweep or a series")
            else:
             self.series_clicked(item)

    @Slot()
    def open_directory(self):
        """opens a filedialog where a user can select a desired directory. Once the directory has been choosen,
        it's data will be loaded immediately into the databse"""
        # open the directory
        dir_path =QFileDialog.getExistingDirectory()
        self.selected_directory.setText(dir_path)

        # save the path in the manager class
        self.offline_manager._directory_path = dir_path

        # read all the data in the specified directory
        # -> read directory data into database
        # @todo: display a reading animation
        self.offline_manager.init_database()
        self.experiments_tree_view, self.outfiltered_tree_view = self.offline_manager.read_data_from_experiment_directory(self.experiments_tree_view, self.outfiltered_tree_view)
        #self.experiments_tree_view.expandToDepth(-1)
        self.experiments_tree_view.setColumnWidth(0,130)
        self.experiments_tree_view.setColumnWidth(1, 60)
        self.experiments_tree_view.setColumnWidth(2, 50)
        #self.experiments_tree_view.show()
        print("treeview_created")

        self.experiments_tree_view.itemClicked.connect(self.tree_view_click_handler)
        self.outfiltered_tree_view.itemClicked.connect(self.tree_view_click_handler)

    @Slot()
    def select_series_to_be_analized(self):
        # get_series_from_datbase
            # db = self.offline_manager.get_database()
            # series_names_string_list = db.get_distinct_non_discarded_series_names()
        # create a pop-up-window to allow user selection of series to be analyzed
            self.display_select_series_dialog()
        # create a new tabwidget with equal tabs according to the selected series

    def display_select_series_dialog(self):
        dialog = QDialog()
        dialog_grid = QGridLayout(dialog)
        series_names_string_list = ["Block Pulse", "IV"]
        for s in series_names_string_list:
            c = QCheckBox()
            l = QLabel(s)
            dialog_grid.addWidget(c,series_names_string_list.index(s),0)
            dialog_grid.addWidget(l,series_names_string_list.index(s),1)

        confirm_series_selection_button = QPushButton("Compare Series", dialog)
        dialog_grid.addWidget(confirm_series_selection_button,len(series_names_string_list),0)
        dialog.setWindowTitle("Available Series To Be Analyzed")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()