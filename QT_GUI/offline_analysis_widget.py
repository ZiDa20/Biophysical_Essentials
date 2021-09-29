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
from assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from frontend_style import Frontend_Style
pg.setConfigOption('foreground','#448aff')

class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        self.blank_analysis_button.clicked.connect(self.start_blank_analysis)
        self.select_directory_button.clicked.connect(self.open_directory)
        self.compare_series.clicked.connect(self.select_series_to_be_analized)


        self.offline_manager = OfflineManager()
        self.offline_analysis_widgets.setCurrentIndex(0)

        self.theme_mode = 1 # per default the dark theme will be started, 0 = light theme


    @Slot()
    def start_blank_analysis(self):
        """starts a blank analysis by changing qstacked tab to blank analysis view ( at index 1) where the user gets
        new button interactions offered """
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

        self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout,self.offline_manager,self.experiments_tree_view,1)

        self.experiments_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.outfiltered_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)

        # show selected tree_view
        self.directory_tree_widget.setCurrentIndex(0)
        self.experiments_tree_view.expandToDepth(0)

        self.experiments_tree_view.setCurrentItem(self.experiments_tree_view.topLevelItem(0))
        print(self.experiments_tree_view.topLevelItem(0).child(0).text(0))
        #self.experiments_tree_view.setCurrentItem(self.experiments_tree_view.topLevelItem(0).child(0).setCheckState(1,Qt.Checked))

        self.blank_analysis_plot_manager.tree_view_click_handler(self.experiments_tree_view.topLevelItem(0).child(0))

        self.display_select_meta_data_group_dialog(False)


    @Slot()
    def select_series_to_be_analized(self):
        # get_series_from_datbase
        db = self.offline_manager.get_database()

        # get available series (by name) inside the selected experiments for this specific analysis.
        # A distinct list will be saved
        series_names_string_list = db.get_distinct_non_discarded_series_names()
        print (series_names_string_list)
        # create a pop-up-window to allow user selection of series to be analyzed
        self.display_select_series_dialog(series_names_string_list)
        # create a new tabwidget with equal tabs according to the selected series

    def display_select_series_dialog(self,series_names_string_list):
        """
        Opens a popup and displays available series to be analyzed in the selected experiments
        :param series_names_string_list: list comes as list of tuples
        :return:
        """
        dialog = QDialog()
        dialog_grid = QGridLayout(dialog)
        #series_names_string_list = ["Block Pulse", "IV"]
        checkbox_list = []
        name_list = []
        for s in  series_names_string_list:
            name = s[0]
            c = QCheckBox()
            checkbox_list.append(c)
            l = QLabel(name)
            dialog_grid.addWidget(c,series_names_string_list.index(s),0)
            dialog_grid.addWidget(l,series_names_string_list.index(s),1)
            name_list.append(name)

        confirm_series_selection_button = QPushButton("Compare Series", dialog)
        confirm_series_selection_button.clicked.connect(partial(self.compare_series_clicked,checkbox_list,name_list,dialog))
        dialog_grid.addWidget(confirm_series_selection_button,len(name_list),0)
        dialog.setWindowTitle("Available Series To Be Analyzed")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def display_select_meta_data_group_dialog(self, meta_data_groups_in_db):
        """
        Opens a new popup and displays buttons to select an action: button 1: load meta data groups from template, button 2: assign all experiments to the same meta data group,
        button 3: read values from database
        :param meta_data_groups_in_db: true if for at least each experiment meta data groups are available in the database, false if not
        :return:
        """

        dialog = QDialog()

        dialog_grid = QGridLayout(dialog)
        dialog.setWindowTitle("Load Meta Data Groups")
        self.set_correct_stylesheet(dialog)
        text_label = QLabel("Please choose an action for the meta data annotation: \n ",dialog)

        select_from_database_button = QPushButton("Load From Database", dialog)
        load_template_button = QPushButton("Load From Template", dialog)
        create_template_button = QPushButton("Assign Now", dialog)
        assign_one_group_to_all = QPushButton("Assign Later", dialog)


        #confirm_series_selection_button.clicked.connect(partial(self.compare_series_clicked,checkbox_list,name_list,dialog))
        dialog_grid.addWidget(text_label, 0, 0)
        dialog_grid.addWidget(select_from_database_button,1,0)
        dialog_grid.addWidget(load_template_button, 2, 0)
        dialog_grid.addWidget(create_template_button, 3, 0)
        dialog_grid.addWidget(assign_one_group_to_all, 4, 0)

        assign_one_group_to_all.clicked.connect(partial(TreeViewManager().assign_meta_data_group_identifiers_to_top_level_items,self.experiments_tree_view,dialog))

        create_template_button.clicked.connect(partial(self.create_meta_data_template,dialog))


        if not meta_data_groups_in_db:
            select_from_database_button.setDisabled(True)

        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def create_meta_data_template(self,old_dialog):
        '''
        Creates a new dialog popup to create a new meta data template. The created template can be saved or not
        :param dialog: open dialog object
        :return:
        '''
        # close the open dialog
        old_dialog.close()

        # open a new dialog with a tree view representation of the selected directory - only on experiment and series level
        meta_data_popup = Assign_Meta_Data_PopUp()
        self.set_correct_stylesheet(meta_data_popup)
        directory = self.offline_manager._directory_path
        tmp_tree_manager = TreeViewManager()
        tmp_tree_manager.meta_data_group_column = 1
        tmp_tree_manager.checkbox_column = 3
        tmp_tree_manager.create_treeview_from_directory(meta_data_popup.meta_data_tree_widget,None,self.offline_manager.package_list(directory),directory,0,None,2)
        meta_data_popup.meta_data_tree_widget.setColumnWidth(0,250)
        meta_data_popup.meta_data_tree_widget.setColumnWidth(1,25)

        # meta_data_popup.save_to_template_button
#        meta_data_popup.close_and_continue_button.clicked.connect(partial(self.continue_open_directory,meta_data_popup))
        meta_data_popup.exec_()

    def set_correct_stylesheet(self,popup_dialog):
        '''
        According to the global value of self.theme_mode the correct style sheet for a given popup dialog will be set.
        :param popup_dialog: dialog object which stylesheet will be set
        :return:
        '''
        if self.theme_mode == 1:
            popup_dialog.setStyleSheet(Frontend_Style().get_dark_style())
        else:
            popup_dialog.setStyleSheet(Frontend_Style().get_light_style())


    '''
    def write_assigned_meta_data_group_to_database(self):

        # write to database

        # write to treeview
        self.write_assigned_meta_data_group_to_treeview(self)

    def write_assigned_meta_data_group_to_treeview(self):
    '''

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

        # add selection to database
        self.offline_manager.write_analysis_series_types_to_database(series_names_list)

        self.tab_list = []
        self.tabWidget.removeTab(0)
        for s in series_names_list:

            # create a new tab from default tab for each series
            new_tab_widget=SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(self.select_analysis_functions,s))
            new_tab_widget.setObjectName(s)
            self.tabWidget.insertTab(series_names_list.index(s),new_tab_widget,s)
            self.tab_list.append(new_tab_widget)
            self.plot_widgets= []

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
        current_tab.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        # set the text of the head label as series name - customized to the selected tab
        # current_tab.headline.setText(series_name + " Specific Analysis Functions")

        db = self.offline_manager.get_database()
        directory = self.offline_manager._directory_path
        dat_files = self.offline_manager.package_list(directory)

        # clear needed fpr promoted widget - otherwise trees will be appended instead of replaced
        self.clear_promoted_tab_items(current_tab)

        TreeViewManager(db).get_series_specific_treeviews(current_tab.selected_tree_widget,current_tab.discarded_tree_widget,dat_files,directory,series_name)

        # create a specific plot manager - this plot manager needs to be global to be visible all the time
        self.current_tab_plot_manager = None

        self.current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.offline_manager,
                                                                  self.experiments_tree_view, 1)

        current_tab.discarded_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)
        current_tab.selected_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)

        current_tab.tabWidget.setCurrentIndex(0)
        current_tab.selected_tree_widget.expandToDepth(0)

        current_tab.selected_tree_widget.setCurrentItem(current_tab.selected_tree_widget.topLevelItem(0))
        self.current_tab_plot_manager.tree_view_click_handler(current_tab.selected_tree_widget.topLevelItem(0).child(0))


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

        # remove initial widgets
        current_tab.function_selection_grid.removeWidget(current_tab.column_1_row_1)
        current_tab.column_1_row_1.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.column_2_row_2)
        current_tab.column_2_row_2.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.column_3_row_3)
        current_tab.column_3_row_3.deleteLater()
        current_tab.function_selection_grid.removeWidget(current_tab.select_series_analysis_functions)
        current_tab.select_series_analysis_functions.deleteLater()

        #current_tab.function_selection_grid.removeWidget(current_tab.label_2)
        #current_tab.label_2.deleteLater()

        # add new labels
        print("indexes", current_tab.function_selection_grid.count())
        print("rows", current_tab.function_selection_grid.rowCount())
        print("columns", current_tab.function_selection_grid.columnCount())

        print("selected_analysis functions",selected_analysis_functions)
        for f in selected_analysis_functions:

            l = QLabel(f)
            l2 = QLabel("None")
            l3 = QLabel("None")
            add_specific_boundaries = QPushButton("Add")

            row =  selected_analysis_functions.index(f) + 5
            print("writing to row", row)
            # add the name of the function to column 0
            current_tab.function_selection_grid.addWidget(l,row, 0, Qt.AlignCenter)
            # add left cursor bound to column 1
            current_tab.function_selection_grid.addWidget(l2, row, 1, Qt.AlignCenter)
            # add right cursor bound to column 2
            current_tab.function_selection_grid.addWidget(l3, row, 2, Qt.AlignCenter)
            # add button for specific to column 3
            current_tab.function_selection_grid.addWidget(add_specific_boundaries,row,3, Qt.AlignCenter)

            # write analysis series into database


        change_series_selection = QPushButton("Change")
        current_tab.function_selection_grid.addWidget(change_series_selection,len(selected_analysis_functions)+5,0)
        #change_series_selection.clicked.connect(partial(self.select_analysis_functions(current_tab.objectName())))

        add_common_boundaries = QPushButton("Add")
        add_common_boundaries.clicked.connect(self.add_common_coursor_bounds)
        current_tab.function_selection_grid.addWidget(add_common_boundaries, len(selected_analysis_functions) + 5, 1, 1, 2)

        #content_margins = current_tab.function_selection_grid.getContentsMargins()


    @Slot(float)
    def add_common_coursor_bounds(self):
        """
        This function will add 2 dragable lines to the plot which will be provided by the global plot manager object
        :return:
        """
        # 1) insert dragable coursor bounds into pyqt graph
        left_val, right_val = self.current_tab_plot_manager.show_draggable_lines()

        #2) connect to the signal taht will be emitted when cursor bounds are moved by user
        self.current_tab_plot_manager.left_bound_changed.cursor_bound_signal.connect(self.update_left_common_labels)
        self.current_tab_plot_manager.right_bound_changed.cursor_bound_signal.connect(self.update_right_common_labels)

        #3) update the function selection grid
        self.update_left_common_labels(left_val)
        self.update_right_common_labels(right_val)


    def update_left_common_labels(self,value):
        self.update_cursor_bound_labels(value, 1)

    def update_right_common_labels(self,value):
        self.update_cursor_bound_labels(value, 2)

    def update_cursor_bound_labels(self,value,column):
        current_index = self.tabWidget.currentIndex()
        current_tab = self.tab_list[current_index]

        # get the number of analysis functions
        nr_of_functions = current_tab.function_selection_grid.rowCount()-5-1
        print(nr_of_functions)
        # get the number of already defined coursor bounds
        nr_of_common_cursors = 0 #self.offline_manager.get_number_of_common_coursor_bounds

        for f in range(0,nr_of_functions):
            row = 5+f

            w = current_tab.function_selection_grid.itemAtPosition(row, column).widget()

            current_tab.function_selection_grid.removeWidget(w)
            w.deleteLater()

            l = QLabel(str(round(value,3)))
            current_tab.function_selection_grid.addWidget(l,row,column, Qt.AlignCenter)

            #current_tab.function_selection_grid.removeWidget(widget)

        self.check_ready_for_analysis(current_tab)

    def check_ready_for_analysis(self,current_tab):
        row_count = current_tab.function_selection_grid.rowCount()-5-1

        for r in range(5,row_count+5):

            # check left common bounds (column 1) to be not none
            t1= current_tab.function_selection_grid.itemAtPosition(r, 1).widget().text()
            # check right common bounds (column 2) to be not none
            t2= current_tab.function_selection_grid.itemAtPosition(r, 2).widget().text()
            if "None" in t1 or "None" in t2:
                print("not ready for analysis")
                return


        # when not returned - all required fields are filled with data
        self.start_analysis_button = QPushButton("Start Analysis")
        current_tab.function_selection_grid.addWidget(self.start_analysis_button,row_count +5 ,3)
        self.start_analysis_button.clicked.connect(partial(self.start_offline_analysis_of_single_series,current_tab))
        print("ready for analysis")

    def start_offline_analysis_of_single_series(self,current_tab):
        self.write_function_grid_values_into_database(current_tab)
        self.offline_manager.execute_single_series_analysis(current_tab.objectName())

    def write_function_grid_values_into_database(self,current_tab):
        """
        When the Start Single Series Analysis Button will be pressed, data from the function selection grid in the
        current tab will be written into the database.
        :param current_tab: tab object from which the function selection grid will be written to the database
        :return:
        """
        row_count = current_tab.function_selection_grid.rowCount()
        db = self.offline_manager.get_database()
        analysis_series_name = current_tab.objectName()
        column_count =current_tab.function_selection_grid.columnCount()
        it_len = int(column_count/2) # there will be always an even
        print("column count", column_count)
        print(it_len)

        for r in range(5,row_count-1):

                for c in range(0,it_len+1,2):
                    print (c)
                    analysis_function = current_tab.function_selection_grid.itemAtPosition(r, 0).widget().text()
                    print("analysis function ", analysis_function)
                    lower_bound = self.get_cursor_bound_value_from_grid(r, c+1, current_tab)
                    upper_bound = self.get_cursor_bound_value_from_grid(r, c+2, current_tab)
                    db.write_analysis_function_name_and_cursor_bounds_to_database(analysis_function,analysis_series_name,lower_bound,upper_bound )


    def get_cursor_bound_value_from_grid(self,row,column,current_tab):
        """
        reads a grid cell defined by column and row and returnsit's float value
        :param row: integer of the row index in the grid
        :param column: integer of column index in the grid
        :param current_tab: the current tab object which is providing the grid
        :return: value in the specified cell as float
        """
        try:
            r = float(current_tab.function_selection_grid.itemAtPosition(row, column).widget().text())
            return r
        except Exception as e:
            print(e)
            return -1


