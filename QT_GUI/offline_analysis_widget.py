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
import pyqtgraph as pg
import numpy as np
from offline_analysis_designer_object import Ui_Offline_Analysis
from functools import partial
from specififc_analysis_tab import *
from plot_widget_manager import PlotWidgetManager
from raw_analysis import AnalysisRaw

pg.setConfigOption('foreground','#448aff')

class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        self.blank_analysis_button.clicked.connect(self.start_another_function)
        self.select_directory_button.clicked.connect(self.open_directory)
        self.compare_series.clicked.connect(self.select_series_to_be_analized)


        self.offline_manager = OfflineManager()
        self.offline_analysis_widgets.setCurrentIndex(0)

    @Slot()
    def start_another_function(self):
        print("noch cooler")
        self.offline_analysis_widgets.setCurrentIndex(1)



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

        self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout,self.offline_manager,self.experiments_tree_view)

        self.experiments_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.outfiltered_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)

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
        checkbox_list = []
        for s in series_names_string_list:
            c = QCheckBox()
            checkbox_list.append(c)
            l = QLabel(s)
            dialog_grid.addWidget(c,series_names_string_list.index(s),0)
            dialog_grid.addWidget(l,series_names_string_list.index(s),1)

        confirm_series_selection_button = QPushButton("Compare Series", dialog)
        confirm_series_selection_button.clicked.connect(partial(self.compare_series_clicked,checkbox_list,series_names_string_list,dialog))
        dialog_grid.addWidget(confirm_series_selection_button,len(series_names_string_list),0)
        dialog.setWindowTitle("Available Series To Be Analyzed")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


    def get_selected_checkboxes(self,checkboxes,labels):
        """From two lists of checkboxes and labels one list of checked labels (string) will be returned"""

        # empty list to be filled
        checked_labels = []
        for c in checkboxes:
            if c.isChecked():
                checked_labels.append(labels[checkboxes.index(c)])

        # return filled list, can be empty too
        return checked_labels


    def compare_series_clicked(self,checkboxes,series_names,dialog):
        """Handler for a click on the button confirm_series_selection in a pop up window"""

        series_to_analize = self.get_selected_checkboxes(checkboxes,series_names)
        self.built_analysis_specific_notebook(series_to_analize)
        self.offline_analysis_widgets.setCurrentIndex(2)
        dialog.close()

    def built_analysis_specific_notebook(self,series_names_list):
        self.tab_list = []
        for s in series_names_list:

            # create a new tab from default tab for each series
            new_tab_widget=SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(self.select_analysis_functions,s))
            new_tab_widget.setObjectName(s)
            self.tabWidget.insertTab(series_names_list.index(s),new_tab_widget,s)
            self.tab_list.append(new_tab_widget)

            # add this selection to table series in the database

        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)

    @Slot()
    def tab_changed(self,index):
        """Function tab changed will be called whenever a tab in the notebook of the selected series for analysis is changed. Index is the tab number correlating with a global list of tab objects self.tab_list
        @author dz, 20.07.2021"""

        current_tab = self.tab_list[index]
        series_name = current_tab.objectName()

        # set the text of the head label as series name - customized to the selected tab
        current_tab.headline.setText(series_name + " Specific Analysis Functions")

        db = self.offline_manager.get_database()
        directory = self.offline_manager._directory_path
        dat_files = self.offline_manager.package_list(directory)

        # clear needed fpr promoted widget - otherwise trees will be appended instead of replaced
        self.clear_promoted_tab_items(current_tab)

        TreeViewManager(db).get_series_specific_treeviews(current_tab.selected_tree_widget,current_tab.discarded_tree_widget,dat_files,directory,series_name)

        # create a specific plot manager - this plot manager needs to be global to be visible all the time
        self.current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.offline_manager,
                                                             self.experiments_tree_view)

        current_tab.discarded_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)
        current_tab.selected_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)

        current_tab.tabWidget.setCurrentIndex(0)
        current_tab.selected_tree_widget.expandAll()

    def clear_promoted_tab_items(self,unclean_tab):
        unclean_tab.selected_tree_widget.clear()
        unclean_tab.discarded_tree_widget.clear()

    @Slot()
    def select_analysis_functions(self,series_name):
        """ open a popup dialog for the user to select available analysis functions """

        # 1) create dialog
        dialog = QDialog()
        dialog_grid = QGridLayout(dialog)

        # 2) get recording mode of the specific series
        recording_mode = "Voltage Clamp"

        # 3) request recording mode specific analysis functions
        analysis_function_names = AnalysisRaw().get_elements(recording_mode)

        # 4) create dialog checkboxes
        checkbox_list = []
        for f in analysis_function_names:
            c = QCheckBox()
            checkbox_list.append(c)
            l = QLabel(f)
            dialog_grid.addWidget(c, analysis_function_names.index(f), 0)
            dialog_grid.addWidget(l, analysis_function_names.index(f), 1)

        # 5) add button to the dialog, since it's in the dialog only the button can be of local type
        confirm_selection_button = QPushButton("Confirm Selected Analysis Functions", dialog)
        confirm_selection_button.clicked.connect(partial(self.update_selected_analysis_function_grid,checkbox_list,analysis_function_names,dialog))

        # 6) Add button widget to correct grid position, finally execute the dialog
        dialog_grid.addWidget(confirm_selection_button,len(analysis_function_names),0)
        dialog.setWindowTitle("Available Analysis Functions for Series " + series_name)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def update_selected_analysis_function_grid(self,checkbox_list,analysis_function_name_list,dialog):
        dialog.close()

        # read from database - if no settings have been made before execute initalization


        selected_analysis_functions = self.get_selected_checkboxes(checkbox_list,analysis_function_name_list)
        current_index = self.tabWidget.currentIndex()
        current_tab = self.tab_list[current_index]

        # remove the big start button


        current_tab.function_selection_grid.removeWidget(current_tab.coloumn_1_row_1)
        current_tab.coloumn_1_row_1.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.coloumn_2_row_2)
        current_tab.coloumn_2_row_2.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.coloumn_3_row_3)
        current_tab.coloumn_3_row_3.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.select_series_analysis_functions)
        current_tab.select_series_analysis_functions.deleteLater()


        # add new labels
        for f in selected_analysis_functions:

            l = QLabel(f)
            l2 = QLabel("None")
            l3 = QLabel("None")
            add_specific_boundaries = QPushButton("Add")

            row =  selected_analysis_functions.index(f) + 5
            print(row)
            # add the name of the function to column 0
            current_tab.function_selection_grid.addWidget(l,row, 0, Qt.AlignCenter)
            # add left cursor bound to column 1
            current_tab.function_selection_grid.addWidget(l2, row, 1)
            # add right cursor bound to column 2
            current_tab.function_selection_grid.addWidget(l3, row, 2)
            # add button for specific to column 3
            current_tab.function_selection_grid.addWidget(add_specific_boundaries,row,3)

            # write analysis series into database


        change_series_selection = QPushButton("Change")
        current_tab.function_selection_grid.addWidget(change_series_selection,len(selected_analysis_functions)+5,0)

        add_common_boundaries = QPushButton("Add")
        add_common_boundaries.clicked.connect(self.add_common_coursor_bounds)
        current_tab.function_selection_grid.addWidget(add_common_boundaries, len(selected_analysis_functions) + 5, 1, 1, 2)

    @Slot(float)
    def add_common_coursor_bounds(self):
        # 1) insert dragable coursor bounds into pyqt graph
        self.current_tab_plot_manager.show_draggable_lines()
        self.current_tab_plot_manager.left_bound_changed.cursor_bound_signal.connect(self.update_left_common_labels)
        self.current_tab_plot_manager.left_bound_changed.cursor_bound_signal.connect(self.update_left_common_labels)

    def update_left_common_labels(self,value):
        print("have to update the labels", value)

        current_index = self.tabWidget.currentIndex()
        current_tab = self.tab_list[current_index]

        # get the number of analysis functions
        nr_of_functions = 3 #self.offline_manager.get_number_of_analysis_functions()
        # get the number of already defined coursor bounds
        nr_of_common_cursors = 0 #self.offline_manager.get_number_of_common_coursor_bounds

        for f in range(0,nr_of_functions):

            row = 5+f
            print(row)
            w = current_tab.function_selection_grid.itemAtPosition(row, 1).widget()

            current_tab.function_selection_grid.removeWidget(w)
            w.deleteLater()

            l = QLabel(str(round(value,3)))
            current_tab.function_selection_grid.addWidget(l,row,1)

            #current_tab.function_selection_grid.removeWidget(widget)


