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
from Offline_Analysis.offline_analysis_manager import OfflineManager
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
from add_new_meta_data_group_pop_up_handler import Add_New_Meta_Data_Group_Pop_Up_Handler
from select_meta_data_options_pop_up_handler import Select_Meta_Data_Options_Pop_Up
pg.setConfigOption('foreground','#448aff')
import csv
from filter_pop_up_handler import Filter_Settings
from Offline_Analysis.offline_analysis_result_visualizer import OfflineAnalysisResultVisualizer
from PySide6.QtCore import QThreadPool
from Worker import Worker
from BlurWindow.blurWindow import GlobalBlur


class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self,progress, status, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.progressbar = progress
        self.statusbar = status
        # start page of offline analysis
        self.blank_analysis_button.clicked.connect(self.start_blank_analysis)

        self.open_analysis_results_button.clicked.connect(self.open_analysis_results)

        # blank analysis menu
        self.select_directory_button.clicked.connect(self.open_directory)
        self.load_from_database.clicked.connect(self.load_treeview_from_database)
        self.go_back_button.clicked.connect(self.go_to_main_page)

        self.compare_series.clicked.connect(self.select_series_to_be_analized)
        
        self.add_filter_button.setEnabled(False)
        # style object of class type Frontend_Style that will be introduced and set by start.py and shared between all subclasses
        self.frontend_style = None
        self.database_handler = None

        self.offline_manager = OfflineManager(progress, status)
        self.offline_analysis_widgets.setCurrentIndex(0)

        self.result_visualizer = OfflineAnalysisResultVisualizer(self.SeriesItems, self.database_handler)

        # might be set during blank analysis
        self.blank_analysis_page_1_tree_manager = None
        self.analysis_stacked = QStackedWidget()
        self.WidgetAnalysis.addWidget(self.analysis_stacked)
        self.hierachy_stacked_list = []
        self.tab_list = []
        self.series_list = []
        self.SeriesItems.clear()
        self.parent_count = 0
        self.current_tab_visualization = []
        self.tree_widget_index_count = 0 # save the current maximal index of the tree

        # animation of the side dataframe
        self.series_selection.clicked.connect(self.animate_tree_view)


    def animate_tree_view(self):
        """Resize the Widget """
        rect = self.SeriesItems.frameGeometry() # get the width of the menu
        print(rect)
        width = self.SeriesItems.width()
        print(width)
        if width == 300:
            new_rect = QRect(9,53,0,self.SeriesItems.height())
            final_width = 0
        else:
            new_rect = QRect(9,53,300,self.SeriesItems.height())
            final_width = 300


        self.SeriesItems.setMinimumSize(0,780)
        self.SeriesItems.sizePolicy().setHorizontalStretch(50)
        self.animation = QPropertyAnimation(self.SeriesItems, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(rect)
        self.animation.setEndValue(new_rect)
        self.animation.setEasingCurve(QEasingCurve.InOutSine)# set the Animation
        self.animation.start()
        self.SeriesItems.setMaximumSize(final_width, 1666666)
        self.SeriesItems.setMinimumSize(final_width, 780)
        


    def update_database_handler_object(self,updated_object):
        self.database_handler = updated_object
        self.offline_manager.database = updated_object
        self.result_visualizer.database_handler = updated_object

    @Slot()
    def open_analysis_results(self):
        """
        Open an existing analysis from the database
        :return:
        """

        #@TODO write a popup to look to the database first or enter an analysis id immediately,
        # maybe also give a filter function to browse by date or username

        # for now, analysis is static number ->
        self.Offline_Analysis_Notebook.setCurrentIndex(1)

        # static offline analysis number
        self.result_visualizer.show_results_for_current_analysis(12)



    @Slot()
    def start_blank_analysis(self):
        """starts a blank analysis by changing qstacked tab to blank analysis view ( at index 1) where the user gets
        new button interactions offered """
        self.offline_analysis_widgets.setCurrentIndex(1)


    @Slot()
    def go_to_main_page(self):
        self.offline_analysis_widgets.setCurrentIndex(1)

    @Slot()
    def load_treeview_from_database(self):
        """

        :return:

        :author: dz, 01.07.2022
        """

        # open a popup to allow experiment label selection by the user
        # from the popup get the label
        experiment_label = ""
        self.experiments_tree_view.clear()
        self.outfiltered_tree_view.clear()
        self.blank_analysis_page_1_tree_manager = TreeViewManager(self.database_handler)
        self.blank_analysis_page_1_tree_manager.create_treeview_from_database(self.experiments_tree_view,
                                                                     self.outfiltered_tree_view,experiment_label, None)

        self.experiments_tree_view.setColumnWidth(0, 100)
        self.experiments_tree_view.setColumnWidth(1, 25)
        self.experiments_tree_view.setColumnWidth(2, 100)
        self.experiments_tree_view.setColumnWidth(3, 25)

        self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout,self.offline_manager,self.experiments_tree_view,1,False)

        self.experiments_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.outfiltered_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)

        # show selected tree_view
        self.directory_tree_widget.setCurrentIndex(0)

    @Slot()
    def open_directory(self):
        '''Opens a filedialog where a user can select a desired directory. After the selection, a dialog will open and ask
        the user to enter meta data groups. The popup will be closed after the user clicked the concerning button.
        The function will be continued in function continue_open_directory
        '''
        # open the directory
        dir_path =QFileDialog.getExistingDirectory()
        self.selected_directory.setText(dir_path)

        if dir_path:
            self.select_directory_button.setText("Change")

        # save the path in the manager class
        self.offline_manager._directory_path = dir_path

        self.display_select_meta_data_group_dialog(False)


    def continue_open_directory(self,enter_meta_data_dialog,meta_data_option_list=None,meta_data_group_assignment_list=None):
        '''
        Function will continue the function open directory after any continue button in the meta data group dialog has
        been clicked. At first the popup will be closed, all data will be loaded immediately into the databse
        :param pop_up_dialog:
        :param meta_data_option_list: list of options in the combo box dropdown menu
        :param meta_data_group_assignment_list: list of tuples of experiment name and assigned meta data group
        :return:
        '''

        if not (meta_data_option_list and meta_data_group_assignment_list):
            meta_data_group_assignment_list = []
            meta_data_option_list = []

        # close the dialog
        enter_meta_data_dialog.close()

        # make sure to always clear the tree - needed when reloading a new directory
        self.experiments_tree_view.clear()
        self.outfiltered_tree_view.clear()


        self.blank_analysis_page_1_tree_manager = self.offline_manager.read_data_from_experiment_directory(
            self.experiments_tree_view,
            self.outfiltered_tree_view, meta_data_option_list, meta_data_group_assignment_list)

        
        self.blank_analysis_page_1_tree_manager.frontend_style = self.frontend_style

        self.blank_analysis_page_1_tree_manager.assign_meta_data_groups_from_list(self.experiments_tree_view,
                                                                                  meta_data_group_assignment_list)

        self.blank_analysis_page_1_tree_manager.update_experiment_meta_data_in_database(self.experiments_tree_view)

        # display settings for the tree view in the blank analysis
        self.experiments_tree_view.setColumnWidth(0, 100)
        self.experiments_tree_view.setColumnWidth(1, 25)
        self.experiments_tree_view.setColumnWidth(2, 100)
        self.experiments_tree_view.setColumnWidth(3, 25)

        # write the meta data to the tree


        self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout,self.offline_manager,self.experiments_tree_view,1,False)

        self.experiments_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.outfiltered_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)

        # show selected tree_view
        self.directory_tree_widget.setCurrentIndex(0)
        self.experiments_tree_view.expandToDepth(0)

        self.experiments_tree_view.setCurrentItem(self.experiments_tree_view.topLevelItem(0))
        #print(self.experiments_tree_view.topLevelItem(0).child(0).text(0))
        #self.experiments_tree_view.setCurrentItem(self.experiments_tree_view.topLevelItem(0).child(0).setCheckState(1,Qt.Checked))

        #self.blank_analysis_plot_manager.tree_view_click_handler(self.experiments_tree_view.topLevelItem(0).child(0))

        self.add_filter_button.setEnabled(True)


    @Slot()
    def select_series_to_be_analized(self):
        """
        executed after all experiment files have been loaded
        :return:
        """
        # get_series_from_datbase
        db = self.offline_manager.get_database()

        # get available series (by name) inside the selected experiments for this specific analysis.
        # A distinct list will be saved
        series_names_string_list = db.get_distinct_non_discarded_series_names()
        print (series_names_string_list)

        # create a pop-up-window to allow user selection of series to be analyzed
        self.display_select_series_dialog(series_names_string_list)

        # -> this will create a new tab widget with equal tabs according to the selected series

        # the meta data groups need to be updated in the database
        self.blank_analysis_page_1_tree_manager.update_experiment_meta_data_in_database(self.experiments_tree_view)



    def display_select_series_dialog(self,series_names_string_list):
        """
        Opens a popup and displays available series to be analyzed in the selected experiments
        :param series_names_string_list: list comes as list of tuples
        :return:
        """
        dialog = QDialog()
        dialog.setWindowFlags(Qt.FramelessWindowHint)

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
        dialog_quit = QPushButton("Cancel", dialog)
        confirm_series_selection_button.clicked.connect(partial(self.compare_series_clicked,checkbox_list,name_list,dialog))
        dialog_quit.clicked.connect(partial(self.close_dialog,dialog))
        dialog_grid.addWidget(confirm_series_selection_button,len(name_list),0)
        dialog.setWindowTitle("Available Series To Be Analyzed")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def close_dialog(self, dialog):
        """ closes the dialog """
        dialog.close()

    def add_filter_to_offline_analysis(self):
        '''will be called when the add filter button is clicked. function will open a filter popup. '''

        filter_dialog = Filter_Settings()

        self.set_meta_data_filter_combobox_options(filter_dialog.meta_data_combo_box)

        self.frontend_style.set_pop_up_dialog_style_sheet(filter_dialog)
        filter_dialog.exec_()

    def set_meta_data_filter_combobox_options(self,combo_box):
        '''go through all series metadata of the tree and find all common meta data information

        '''
    def display_select_meta_data_group_dialog(self, meta_data_groups_in_db):
        """
        Opens a new popup and displays buttons to select an action: button 1: load meta data groups from template, button 2: assign all experiments to the same meta data group,
        button 3: read values from database
        :param meta_data_groups_in_db: true if for at least each experiment meta data groups are available in the database, false if not
        :return:
        """

        dialog =  Select_Meta_Data_Options_Pop_Up()
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)

        # assign later button will close the dialog without any additional assignments
        dialog.assign_one_group_to_all.clicked.connect(partial(self.continue_open_directory,dialog))

        # Create Template button will open a new popup to assign different meta data groups
        dialog.assign_now_button.clicked.connect(partial(self.create_meta_data_template,dialog))

        # Load Template button will open a filedialog to select a template
        dialog.load_template_button.clicked.connect(partial(self.open_meta_data_template_file,dialog))

        dialog.assign_one_group_to_all.setAccessibleName("big_square")
        dialog.assign_now_button.setAccessibleName("big_square")
        dialog.load_template_button.setAccessibleName("big_square")
        dialog.select_from_database_button.setAccessibleName("big_square")

        if not meta_data_groups_in_db:
            dialog.select_from_database_button.setDisabled(True)


        dialog.exec_()

    def open_meta_data_template_file(self, dialog):
        meta_data_assignments = []
        option_list = []
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile',"","*.csv")[0]
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    meta_data_assignments.append((row[0], row[1]))
                    option_list.append(row[1])
            csv_file.close()

            #@todo : start a new tab here ?
            self.continue_open_directory(dialog,option_list,meta_data_assignments)

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
        self.frontend_style.set_pop_up_dialog_style_sheet(meta_data_popup)

        directory = self.offline_manager._directory_path
        tmp_tree_manager = TreeViewManager(self.database_handler)
        tmp_tree_manager.meta_data_group_column = 1
        tmp_tree_manager.checkbox_column = 3
        tmp_tree_manager.analysis_mode = 1
        tmp_tree_manager.frontend_style = self.frontend_style

        tmp_tree_manager.create_treeview_from_directory(meta_data_popup.meta_data_tree_widget, None,
                                                        self.offline_manager.package_list(directory), directory, 0,
                                                        None, 2)

        meta_data_popup.meta_data_tree_widget.setColumnWidth(0,250)
        meta_data_popup.meta_data_tree_widget.setColumnWidth(1,25)

        # meta_data_popup.save_to_template_button
        meta_data_popup.close_and_continue_button.clicked.connect(partial(self.continue_open_directory,meta_data_popup,
                                                                          tmp_tree_manager.meta_data_option_list,
                                                                          tmp_tree_manager.get_meta_data_group_assignments()))

        meta_data_popup.save_to_template_button.clicked.connect(partial(self.save_meta_data_to_template_and_continue,
                                                                        meta_data_popup,tmp_tree_manager))
        meta_data_popup.exec_()

    def save_meta_data_to_template_and_continue(self,meta_data_popup,tmp_tree_manager):
        '''
        Save the template first and than continue directory opening.
        :param meta_data_popup:
        :param tmp_tree_manager:
        :return:
        '''
        tmp_tree_manager.write_tuple_list_to_csv_file()
        self.continue_open_directory(meta_data_popup, tmp_tree_manager.meta_data_option_list,
                                     tmp_tree_manager.get_meta_data_group_assignments())

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
        self.database_handler.write_analysis_series_types_to_database(series_names_list)

        
        for index, s in enumerate(series_names_list):

            # create a new tab from default tab for each series
            """
            new_tab_widget=SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(self.select_analysis_functions,s))
            new_tab_widget.setObjectName(s)
            
            self.tabWidget.insertTab(series_names_list.index(s),new_tab_widget,s)
            self.tab_list.append(new_tab_widget)
            self.plot_widgets= []
            """
            # add the tab
            index += self.tree_widget_index_count
            new_tab_widget=SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(self.select_analysis_functions,s))
            new_tab_widget.setObjectName(s)
            self.tab_list.append(new_tab_widget)
            self.tab_changed(index,s)
            self.new_analysis.clicked.connect(self.go_to_offline_analysis_page_2)

            # fill the treetabwidgetitems
            parent = QTreeWidgetItem()
            self.SeriesItems.addTopLevelItem(parent)


            # set the child items of the widget
            plot = QTreeWidgetItem(parent)
            tables = QTreeWidgetItem(parent)
            statistics = QTreeWidgetItem(parent)
            plot.setText(0, "Plot")
            tables.setText(0, "Tables")
            statistics.setText(0, "Statistics")
            parent.setText(0, s + " Analysis Configurator")
            self.series_list.append(s)

            # child stacked notebook per parent node
            self.hierachy_stacked = QStackedWidget()
            self.hierachy_stacked.addWidget(QWidget())
            self.hierachy_stacked.addWidget(QWidget())
            self.hierachy_stacked.addWidget(QWidget())
            self.hierachy_stacked.addWidget(QWidget())
            self.hierachy_stacked.addWidget(QWidget())
            self.analysis_stacked.addWidget(self.hierachy_stacked)

            
            # set important data to the parent
            parent.setData(1, Qt.UserRole, "parent") # check if parent
            parent.setData(2, Qt.UserRole, new_tab_widget) # save the widget
            parent.setData(4, Qt.UserRole, self.hierachy_stacked) # save the child notebook
            parent.setData(5, Qt.UserRole, 0)
            parent.setData(6, Qt.UserRole, s) # specific series name
            parent.setData(7, Qt.UserRole, index) # save the index 
           

            # set the data for each of the child items
            # remove and use for loop
            plot.setData(4, Qt.UserRole, self.hierachy_stacked)
            plot.setData(5, Qt.UserRole, 1)
            plot.setData(6, Qt.UserRole, self.parent_count)
            #parent.setData(0, Qt.UserRole, new_tab_widget)
            self.hierachy_stacked_list.append(self.hierachy_stacked)
            self.plot_widgets= []
            self.parent_count += 1
            # add this selection to table
            #  series in the database
            self

        # connect the treewidgetsitems
        self.SeriesItems.itemClicked.connect(self.onItemClicked)

        #set the analysis notebook as index
        self.offline_analysis_widgets.setCurrentIndex(3)
        self.tree_widget_index_count = index +1
        
    def onItemClicked(self, it, col):
        """should be commented properly
        toDO MZ"""
       

        if self.SeriesItems.currentItem().data(1, Qt.UserRole) is not None:
            
            # retrieve the parent on click
            
            parent_stacked = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            stacked_widget = self.SeriesItems.currentItem().data(4, Qt.UserRole)
            stacked_index = self.SeriesItems.currentItem().data(5, Qt.UserRole)
            new_widget = self.SeriesItems.currentItem().data(2, Qt.UserRole)
            
            # insert the windget
            stacked_widget.insertWidget(stacked_index, new_widget)
            stacked_widget.setCurrentIndex(stacked_index)
            self.analysis_stacked.setCurrentIndex(parent_stacked)
            
        else:
            parent_stacked = self.SeriesItems.currentItem().data(6, Qt.UserRole)
            stacked_widget_index = self.SeriesItems.currentItem().data(5, Qt.UserRole)
            self.analysis_stacked.setCurrentIndex(parent_stacked)
            self.hierachy_stacked_list[parent_stacked].setCurrentIndex(stacked_widget_index)
            
    @Slot()
    def go_to_offline_analysis_page_2(self):
        self.offline_analysis_widgets.setCurrentIndex(1)

    @Slot()
    def tab_changed(self,index, series_name):
        """Function tab changed will be called whenever a tab in the notebook of the selected series for analysis is
        changed. Index is the tab number correlating with a global list of tab objects self.tab_list
        @author dz, 20.07.2021"""

        print(series_name)
        current_tab = self.tab_list[index]
        series_name = series_name


        #current_tab.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        # set the text of the head label as series name - customized to the selected tab
        # current_tab.headline.setText(series_name + " Specific Analysis Functions")

        db = self.offline_manager.get_database()
        directory = self.offline_manager._directory_path
        dat_files = self.offline_manager.package_list(directory)

        # clear needed fpr promoted widget - otherwise trees will be appended instead of replaced
        self.clear_promoted_tab_items(current_tab)

        # deprecated dz 29.06.2022
        #TreeViewManager(db).get_series_specific_treeviews(current_tab.selected_tree_widget,current_tab.discarded_tree_widget,dat_files,directory,series_name)
        TreeViewManager(db).create_treeview_from_database(current_tab.selected_tree_widget,current_tab.discarded_tree_widget,"",series_name)


        # create a specific plot manager - this plot manager needs to be global to be visible all the time
        self.current_tab_plot_manager = None

        if series_name != "RheoRamp":
            current_tab.turn_on_peak_detection.setVisible(False)
        else:
            current_tab.turn_on_peak_detection.setVisible(True)

        self.current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.offline_manager,
                                                                  self.experiments_tree_view, 1, current_tab.turn_on_peak_detection.isVisible())

        current_tab.discarded_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)
        current_tab.selected_tree_widget.itemClicked.connect(self.current_tab_plot_manager.tree_view_click_handler)

        #current_tab.tabWidget.setCurrentIndex(0)
        current_tab.selected_tree_widget.expandToDepth(0)

        current_tab.selected_tree_widget.setCurrentItem(current_tab.selected_tree_widget.topLevelItem(0))

        self.current_tab_plot_manager.tree_view_click_handler(current_tab.selected_tree_widget.topLevelItem(0).child(0))

        self.current_tab_visualization.append(self.current_tab_plot_manager)


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
        recording_mode = self.database_handler.get_recording_mode_from_analysis_series_table(series_name)

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
        confirm_selection_button.clicked.connect(partial(self.update_selected_analysis_function_table,checkbox_list,analysis_function_names,dialog))

        # 6) Add button widget to correct grid position, finally execute the dialog
        dialog_grid.addWidget(confirm_selection_button,len(analysis_function_names),0)
        dialog.setWindowTitle("Available Analysis Functions for Series " + series_name)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def update_selected_analysis_function_table(self,checkbox_list,analysis_function_name_list,dialog):
        '''enters data into the analysis table after the dialog has been closed'''
        dialog.close()
        
        # read from database - if no settings have been made before execute initalization

        self.selected_analysis_functions = self.get_selected_checkboxes(checkbox_list,analysis_function_name_list)
        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        current_tab = self.tab_list[current_index]
        current_tab.analysis_function.addWidget(current_tab.analysis_table_widget)
        current_tab.analysis_table_widget.analysis_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        current_tab.analysis_table_widget.analysis_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        existing_row_numbers = current_tab.analysis_table_widget.analysis_table_widget.rowCount()
        current_tab.pushButton_3.clicked.connect(self.add_filter_to_offline_analysis)
    
        if existing_row_numbers == 0:
            

            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
            current_tab.analysis_table_widget.analysis_table_widget.setColumnCount(5)
            current_tab.analysis_table_widget.analysis_table_widget.setRowCount(len(self.selected_analysis_functions))
            self.table_buttons = [0] * len(self.selected_analysis_functions)
        else:
            current_tab.analysis_table_widget.analysis_table_widget.setRowCount(existing_row_numbers + len(self.selected_analysis_functions))
            self.table_buttons = self.table_buttons +  [0]*len(self.selected_analysis_functions)

        for row in range(len(self.selected_analysis_functions)):
                row_to_insert = row + existing_row_numbers
                value = self.selected_analysis_functions[row]
                print(str(value))
                current_tab.analysis_table_widget.analysis_table_widget.setItem(row_to_insert,0,QTableWidgetItem(str(value)))
                self.table_buttons[row_to_insert] = QPushButton("Add")
                self.c = QPushButton("Configure")
                current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert,3,self.table_buttons[row_to_insert])
                current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 4, self.c)

                self.table_buttons[row_to_insert].clicked.connect(partial(self.add_coursor_bounds,row_to_insert,current_tab))

        current_tab.analysis_table_widget.analysis_table_widget.show()


    def remove_existing_dragable_lines(self,row_number,current_tab):
        number_of_rows = current_tab.analysis_table_widget.rowCount()

        for r in range(0,number_of_rows):
            if current_tab.analysis_table_widget.item(r,1) is not None:
                current_tab.analysis_table_widget.removeCellWidget (r, 3)
                self.b= QPushButton("Change")
                current_tab.analysis_table_widget.setCellWidget(r, 3, self.b)

                self.b.clicked.connect(partial(self.add_coursor_bounds,r,current_tab))

                self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines(row_number)
            try:
                self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines()
            except:
                print("nothing to delete")

    def add_coursor_bounds(self,row_number,current_tab):
        """
        This function will add 2 dragable lines to the plot which will be provided by the global plot manager object
        :return:
        """

      
        self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines(row_number)

        # 1) insert dragable coursor bounds into pyqt graph
        left_val, right_val = self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].show_draggable_lines(row_number)

        #2) connect to the signal taht will be emitted when cursor bounds are moved by user
        self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].left_bound_changed.cursor_bound_signal.connect(self.update_left_common_labels)
        self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].right_bound_changed.cursor_bound_signal.connect(self.update_right_common_labels)


        #3) update the function selection grid
        self.update_left_common_labels((left_val,row_number))
        self.update_right_common_labels((right_val,row_number))

        current_tab.analysis_table_widget.analysis_table_widget.removeCellWidget(row_number, 3)
        self.b = QPushButton("Change")
        current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_number, 3, self.b)
        self.b.clicked.connect(partial(self.add_coursor_bounds, row_number, current_tab))

    @Slot(tuple)
    def update_left_common_labels(self,tuple_in):
        row_number = tuple_in[1]
        value = tuple_in[0]
        self.update_cursor_bound_labels(value, 1, row_number)

    @Slot(tuple)
    def update_right_common_labels(self,tuple_in):
        row_number = tuple_in[1]
        value = tuple_in[0]
        self.update_cursor_bound_labels(value, 2,row_number)

    def update_cursor_bound_labels(self,value,column_number,row_number):
        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        current_tab = self.tab_list[current_index]
        print("updating: row = " + str(row_number) + " column=" + str(column_number) + " value= " + str(value))


        current_tab.analysis_table_widget.analysis_table_widget.setItem(row_number,column_number,QTableWidgetItem(str(value)))

        self.check_ready_for_analysis(current_tab)

    def check_ready_for_analysis(self,current_tab):
        """
        function that checks for coursor bounds in all selected functions in this tab to be not empty.
        if this is the case the start analysis button becomes clickable
        :param current_tab:
        :return:
        """
        #print("Checking ready  for analysis")
        for row in range(0,(current_tab.analysis_table_widget.analysis_table_widget.rowCount())):
            if current_tab.analysis_table_widget.analysis_table_widget.item(row,1) is None or current_tab.analysis_table_widget.analysis_table_widget.item(row,2) is None:
                return

        # make sure to connect start_analysis_button only once  .. otherwise a loop gets created # BUGFIX
        if current_tab.start_analysis_button.isEnabled() is False:
            current_tab.start_analysis_button.setEnabled(True)
            current_tab.start_analysis_button.clicked.connect(partial(self.start_offline_analysis_of_single_series,current_tab))


    def start_offline_analysis_of_single_series(self,current_tab):
        '''
        Performs analysis according to the selected criteria.
        Before the analysis starts, the selected criteria will be stored in the database
        :param current_tab:
        :return:
        '''

        # store analysis parameter in the database
        self.database_handler.database.close()
        self.threadpool = QThreadPool()
        self.worker = Worker(self.run_database_thread, current_tab)
        self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.progress_bar_update_analysis)
        self.threadpool.start(self.worker)


    def run_database_thread(self, current_tab, progress_callback):
        """ This function will run the analysis in a separate thread, that is selected
        by the analysis function
        :param current_tab:
        :param progress_callback:
        
        """
        print("Qthread is running")
        self.database_handler.open_connection()
        self.write_function_grid_values_into_database(current_tab)
        self.offline_manager.execute_single_series_analysis(current_tab.objectName(), progress_callback)
        self.database_handler.database.close()

    def progress_bar_update_analysis(self,data):
        """ This function will update the progress bar in the analysis tab
        :param data:
        
        """
        self.progressbar.setValue(data[0])
        self.statusbar.showMessage("Analyzing: " + str(data[1]) + "%")

    def finished_result_thread(self):
        # switch to the visualization tab
        print("here we are!")
        #self.Offline_Analysis_Notebook.setCurrentIndex(1)
        # plot the calculated results
        self.database_handler.open_connection()
        print(self.SeriesItems.currentItem().data(0,Qt.DisplayRole))
        self.offline_tab = self.result_visualizer.show_results_for_current_analysis(self.database_handler.analysis_id, self.SeriesItems.currentItem().data(6, Qt.UserRole))
        self.analysis_stacked.setCurrentIndex(self.SeriesItems.currentItem().data(7,Qt.UserRole))
        print(self.SeriesItems.currentItem().data(6,Qt.UserRole))
        self.hierachy_stacked_list[self.SeriesItems.currentItem().child(0).data(6,Qt.UserRole)].insertWidget(1,self.offline_tab)
        self.hierachy_stacked_list[self.SeriesItems.currentItem().child(0).data(6,Qt.UserRole)].setCurrentIndex(1)
        self.SeriesItems.currentItem().child(0).setSelected(True) # for sure not usable
        

    def write_function_grid_values_into_database(self,current_tab):
        """
        When the Start Single Series Analysis Button will be pressed, data from the function selection table in the
        current tab will be written into the database.
        :param current_tab: tab object from which the function selection grid will be written to the database
        :return:
        """
        row_count = current_tab.analysis_table_widget.analysis_table_widget.rowCount()
        analysis_series_name = current_tab.objectName()
        column_count =current_tab.analysis_table_widget.analysis_table_widget.columnCount()
        self.database_handler.open_connection()
        

        ### to be continued here
        print(row_count)
        for r in range(0,row_count):
            analysis_function = current_tab.analysis_table_widget.analysis_table_widget.item(r, 0).text()
            #print("analysis function ", analysis_function)
            lower_bound = round(float(current_tab.analysis_table_widget.analysis_table_widget.item(r,1).text()),2)
            upper_bound = round(float(current_tab.analysis_table_widget.analysis_table_widget.item(r,2).text()),2)
            #print(lower_bound)
            #print(upper_bound)
            self.database_handler.write_analysis_function_name_and_cursor_bounds_to_database(analysis_function, analysis_series_name, lower_bound, upper_bound)


        print("finished")

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


