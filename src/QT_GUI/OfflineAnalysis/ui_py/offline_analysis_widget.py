###############################################################################
## Form generated from reading UI file 'offline_analysis_main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import numpy as np
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from Offline_Analysis.offline_analysis_manager import OfflineManager
from Offline_Analysis.error_dialog_class import CustomErrorDialog
from treeview_manager import TreeViewManager
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_designer_object import Ui_Offline_Analysis
from functools import partial
from QT_GUI.OfflineAnalysis.CustomWidget.specififc_analysis_tab import SpecificAnalysisTab
from plot_widget_manager import PlotWidgetManager
from raw_analysis import AnalysisRaw
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_options_pop_up_handler import Select_Meta_Data_Options_Pop_Up
import csv
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up_handler import Filter_Settings
from Offline_Analysis.offline_analysis_result_visualizer import OfflineAnalysisResultVisualizer
from PySide6.QtCore import QThreadPool
from Worker import Worker
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup_handler import Load_Data_From_Database_Popup_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.drag_and_drop_list_view import DragAndDropListView
from PostSql_Handler import PostSqlHandler
from Offline_Analysis.offline_analysis_result_table_model import OfflineAnalysisResultTableModel
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from QT_GUI.OfflineAnalysis.CustomWidget.ui_metadata_analysis_popup import MetadataPopupAnalysis
from Pandas_Table import PandasTable
import pandas as pd
from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import StatisticsTablePromoted
from QT_GUI.OfflineAnalysis.CustomWidget.select_statistics_meta_data_handler import StatisticsMetaData_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog

import copy

from Offline_Analysis.tree_model_class import TreeModel


class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self, progress, status, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.progressbar = progress
        self.statusbar = status
        self.add_filter_button.setEnabled(False)

        
        self.threadpool = QThreadPool()
        self.final_series = []

        # style object of class type Frontend_Style that will be int
        # produced and set by start.py and shared between all subclasses
        self.frontend_style = None
        self.database_handler = None

        self.offline_manager = OfflineManager(progress, status)
        self.offline_analysis_widgets.setCurrentIndex(0)

        self.result_visualizer = OfflineAnalysisResultVisualizer(self.SeriesItems, self.database_handler, self)

        # might be set during blank analysis
        self.blank_analysis_page_1_tree_manager = None
        self.blank_analysis_plot_manager = None
        self.analysis_stacked = QStackedWidget()
        self.WidgetAnalysis.addWidget(self.analysis_stacked)
        self.hierachy_stacked_list = []
        self.tab_list = []
        self.series_list = []

        self.SeriesItems.clear()

        self.parent_count = 0
        self.current_tab_visualization = []
        self.tree_widget_index_count = 0  # save the current maximal index of the tree

        # animation of the side dataframe
        self.series_selection.clicked.connect(self.animate_tree_view)
        self.blank_analysis_button.clicked.connect(self.start_blank_analysis)
        self.open_analysis_results_button.clicked.connect(self.open_analysis_results)
        self.compare_series.clicked.connect(self.select_series_to_be_analized)

        # blank analysis menu
        self.select_directory_button.clicked.connect(self.open_directory)
        self.load_from_database.clicked.connect(self.load_treeview_from_database)
        self.edit_meta.clicked.connect(self.edit_metadata_analysis_id)
        self.go_back_button.clicked.connect(self.go_backwards)
        self.fo_forward_button.clicked.connect(self.go_forwards)
        self.load_meta_data.clicked.connect(self.load_and_assign_meta_data)
        self.start_analysis.clicked.connect(self.start_analysis_offline)
        self.navigation_list = []

        self.show_sweeps_radio.toggled.connect(self.show_sweeps_toggled)
        self.show_colum.clicked.connect(self.select_tree_view_meta_data)

    def select_tree_view_meta_data(self):

        # Create the Dialog to be shown to the user: The user will be allowed to check/uncheck desired labels
        dialog = SelectMetaDataForTreeviewDialog(self.database_handler, self.blank_analysis_tree_view_manager, self.blank_analysis_plot_manager)

        #dialog.finish_button.clicked.connect(
        #    partial(self.add_meta_data_to_tree_view,checkbox_list, name_list, dialog))

        dialog.cancel_button.clicked.connect(partial(self.close_dialog, dialog))

        dialog.setWindowTitle("Available Meta Data Label")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


    def show_sweeps_toggled(self,signal):
        print("toggle" , self.offline_analysis_widgets.currentIndex())
        try:
            if self.offline_analysis_widgets.currentIndex()==1:
                self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
            if self.offline_analysis_widgets.currentIndex() ==2:
                print("not implemented yet")
        except Exception as e:
           print("sweep error", e)
           dialog = QDialog()
           dialog_grid = QGridLayout(dialog)
           dialog_error = QLabel("Dear looser ! Please load your data first",dialog)
           dialog_quit = QPushButton("Cancel", dialog)
           dialog_grid.addWidget(dialog_error,0,0)
           dialog_grid.addWidget(dialog_quit, 1, 0)
           dialog_quit.clicked.connect(partial(self.close_dialog,dialog))
           dialog.setWindowTitle("Please Revise your Action")
           dialog.exec_()

    def animate_tree_view(self):
        """Resize the Widget """
        rect = self.SeriesItems.frameGeometry()  # get the width of the menu
        print(rect)
        width = self.SeriesItems.width()
        print(width)
        if width == 300:
            new_rect = QRect(9, 53, 0, self.SeriesItems.height())
            final_width = 0
        else:
            new_rect = QRect(9, 53, 300, self.SeriesItems.height())
            final_width = 300

        self.SeriesItems.setMinimumSize(0, 780)
        self.SeriesItems.sizePolicy().setHorizontalStretch(50)
        self.animation = QPropertyAnimation(self.SeriesItems, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(rect)
        self.animation.setEndValue(new_rect)
        self.animation.setEasingCurve(QEasingCurve.InOutSine)  # set the Animation
        self.animation.start()
        self.SeriesItems.setMaximumSize(final_width, 1666666)
        self.SeriesItems.setMinimumSize(final_width, 780)

    def load_and_assign_meta_data(self):
        """
        To play around with the data you may want to load or assign new meta data - here one can do this
        @return: 
        """

        # @todo: multithreading ?
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.csv")[0]
        with open(file_name, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row:
                    try:
                        self.database_handler.add_meta_data_group_to_existing_experiment(row[0], row[1])
                        print("assigned %s to recording %s ", row[0], row[1])
                    except Exception as e:
                        print("load_and_assign_meta_data: error when assigning meta_data_types")
            csv_file.close()

    def update_database_handler_object(self, updated_object):
        self.database_handler = updated_object
        self.offline_manager.database = updated_object
        self.result_visualizer.database_handler = updated_object
        
        
    def edit_metadata_analysis_id(self):
        """ Popup Dialog to edit the metadata used for the offline analysis
        """
        edit_data = MetadataPopupAnalysis()
        edit_data.quit.clicked.connect(edit_data.close)
        metadata_table = QTableView()
        q = 'Select * from offline_analysis'
        table_handling = self.database_handler.get_data_from_database(self.database_handler.database, q, fetch_mode = 2)
        table_model = PandasTable(table_handling)
        metadata_table.setModel(table_model)
        edit_data.final_table_layout.addWidget(metadata_table)
        edit_data.exec()
        
    
    @Slot()
    def open_analysis_results(self):
        """
        Open an existing analysis from the database
        :return:
        """

        # @TODO write a popup to look to the database first or enter an analysis id immediately,
        # maybe also give a filter function to browse by date or username

        # for now, analysis is static number ->
        # self.Offline_Analysis_Notebook.setCurrentIndex(1)

        # static offline analysis number
        self.database_handler.analysis_id = 8
        series_names_list = self.database_handler.get_analysis_series_names_for_specific_analysis_id()
        print(series_names_list)

        for i in range(0,len(series_names_list)):
            series_names_list[i] = series_names_list[i][0]
        #    self.result_visualizer.show_results_for_current_analysis(9,name)

        self.built_analysis_specific_tree(series_names_list)
        print("displaying to analysis results: ", str(self.database_handler.analysis_id))

        print(self.SeriesItems.topLevelItemCount())


        # @todo DZ write the reload of the analyis function grid properly and then choose to display plots only when start analysis button is enabled
        for parent_pos in range(0,self.SeriesItems.topLevelItemCount()):

            self.SeriesItems.setCurrentItem(self.SeriesItems.topLevelItem(parent_pos).child(0))
            self.offline_analysis_result_tree_item_clicked()
            self.finished_result_thread()

        self.offline_analysis_widgets.setCurrentIndex(2)

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
        self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout, self.database_handler, None ,  False)
        # open a popup to allow experiment label selection by the user
        self.dialog = Load_Data_From_Database_Popup_Handler()
        #self.database_handler.open_connection()
        available_labels = self.database_handler.get_available_experiment_label()

        print(available_labels)
        label_list = []
        for i in available_labels:
            if i[0] is None:
                QListWidgetItem('nan', self.dialog.available_labels_list)
            else:
                QListWidgetItem(i[0], self.dialog.available_labels_list)

        grid = QGridLayout()
        self.list_view = DragAndDropListView(self, self.dialog.available_labels_list)
        self.list_view.setAcceptDrops(True)
        self.list_view.fileDropped.connect(self.experiment_label_dropped)
        grid.addWidget(self.list_view)
        self.dialog.selected_labels.setLayout(grid)



        self.dialog.load_data.clicked.connect(self.load_page_1_tree_view)
        self.dialog.exec_()

    def load_page_1_tree_view(self):
        """

        @return:
        """
        self.selected_meta_data_list = []
        for n in range(0, self.list_view.count()):
            self.selected_meta_data_list.append(self.list_view.item(n).text())

        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)
        self.blank_analysis_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio
        self.blank_analysis_tree_view_manager.selected_meta_data_list = self.selected_meta_data_list

        self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)

        self.dialog.close()
        self.treebuild.directory_tree_widget.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(1)

    def load_recordings(self, progress_callback):

        self.progress_callback = progress_callback
        self.database_handler.open_connection(read_only=True)
        experiment_label = ""
        self.blank_analysis_page_1_tree_manager.selected_meta_data_list = self.selected_meta_data_list
        self.blank_analysis_page_1_tree_manager.create_treeview_from_database(experiment_label, None,
                                                                              self.progress_callback)

    def finished_database_loading(self):

        print("here we finish the database")
        self.database_handler.open_connection()
        for experiment in self.blank_analysis_page_1_tree_manager.not_discard_experiments_stored_in_db:
            self.database_handler.create_mapping_between_experiments_and_analysis_id(experiment)
        #self.blank_analysis_plot_manager = PlotWidgetManager(self.verticalLayout,self.offline_manager,self.treebuild.experiments_tree_view,1,False)
        navigation = NavigationToolbar(self.blank_analysis_plot_manager.canvas, self)
        self.treebuild.experiments_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.treebuild.outfiltered_tree_view.itemClicked.connect(self.blank_analysis_plot_manager.tree_view_click_handler)
        self.plot_home.clicked.connect(navigation.home)
        self.plot_move.clicked.connect(navigation.pan)
        self.plot_zoom.clicked.connect(navigation.zoom)
        self.blank_analysis_plot_manager.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.treebuild.directory_tree_widget.setCurrentIndex(0)
        print("finished loading")
        # show selected tree_view

    @Slot()
    def experiment_label_dropped(self, item_text):
        print(item_text)
        QListWidgetItem(item_text, self.list_view)

        distinct_meta_data = self.database_handler.get_distinct_meta_data_groups_for_specific_experiment_label(
            [item_text])
        print(distinct_meta_data)

        for i in distinct_meta_data:
            QListWidgetItem(i[0], self.dialog.meta_data_list).setCheckState(Qt.CheckState.Checked)

        print("added new item")

    @Slot()
    def open_directory(self):
        '''Opens a filedialog where a user can select a desired directory. After the selection, a dialog will open and ask
        the user to enter meta data groups. The popup will be closed after the user clicked the concerning button.
        The function will be continued in function continue_open_directory
        '''
        # open the directory
        dir_path = QFileDialog.getExistingDirectory()
        # self.selected_directory.setText(dir_path)

        if dir_path:
            self.select_directory_button.setText("Change")

        # save the path in the manager class
        self.offline_manager._directory_path = dir_path

        self.display_select_meta_data_group_dialog(False)

    def continue_open_directory(self, enter_meta_data_dialog, meta_data_option_list=None,
                                meta_data_group_assignment_list=None):
        '''
        Function will continue the function open directory after any continue button in the meta data group dialog has
        been clicked. At first the popup will be closed, all data will be loaded immediately into the databse
        :param pop_up_dialog:
        :param meta_data_option_list: list of options in the combo box dropdown menu
        :param meta_data_group_assignment_list: list of tuples of experiment name and assigned meta data group
        :return:
        '''

        # close the dialog
        enter_meta_data_dialog.close()

        if not (meta_data_option_list and meta_data_group_assignment_list):
            meta_data_group_assignment_list = []
            meta_data_option_list = []
        else:
            for n in meta_data_group_assignment_list:
                print(n)
                self.database_handler.add_meta_data_group_to_existing_experiment(n)
                #self.database_handler.global_meta_data_table.add_meta_data_group_to_existing_experiment(n)

        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)

        self.blank_analysis_tree_view_manager = self.offline_manager.read_data_from_experiment_directory(self.blank_analysis_tree_view_manager, meta_data_option_list, meta_data_group_assignment_list)


        #self.add_filter_button.setEnabled(True)

        self.blank_analysis_tree_view_manager.data_read_finished.finished_signal.connect(self.load_treeview_from_database)


    @Slot()
    def select_series_to_be_analized(self):
        """
        executed after all experiment files have been loaded
        :return:
        """
        # get_series_from_datbase

        db = self.database_handler

        # get available series (by name) inside the selected experiments for this specific analysis.
        # A distinct list will be saved
        series_names_string_list = db.get_distinct_non_discarded_series_names()
        print(series_names_string_list)

        # create a pop-up-window to allow user selection of series to be analyzed
        self.display_select_series_dialog(series_names_string_list)

        # -> this will create a new tab widget with equal tabs according to the selected series

        # the meta data groups need to be updated in the database
        #self.blank_analysis_page_1_tree_manager.update_experiment_meta_data_in_database(self.treebuild.experiments_tree_view)

    def display_select_series_dialog(self, series_names_string_list):
        """
        Opens a popup and displays available series to be analyzed in the selected experiments
        :param series_names_string_list: list comes as list of tuples
        :return:
        """
        dialog = QDialog()
        dialog.setWindowFlags(Qt.FramelessWindowHint)

        dialog_grid = QGridLayout(dialog)
        # series_names_string_list = ["Block Pulse", "IV"]
        dialog_quit = QPushButton("Cancel", dialog)
        dialog_grid.addWidget(dialog_quit, 0, 0)

        checkbox_list = []
        
        name_list = []
        for s in series_names_string_list:
            name = s[0]
            c = QCheckBox()
            checkbox_list.append(c)
            l = QLabel(name)
            dialog_grid.addWidget(c, series_names_string_list.index(s) + 2, 0)
            dialog_grid.addWidget(l, series_names_string_list.index(s) + 2, 1)
            name_list.append(name)

        confirm_series_selection_button = QPushButton("Compare Series", dialog)
        print(checkbox_list)
        confirm_series_selection_button.clicked.connect(
            partial(self.compare_series_clicked, checkbox_list, name_list, dialog))
        dialog_quit.clicked.connect(partial(self.close_dialog, dialog))
        dialog_grid.addWidget(confirm_series_selection_button, len(name_list) + 2, 0)
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

    def set_meta_data_filter_combobox_options(self, combo_box):
        '''go through all series metadata of the tree and find all common meta data information

        '''

    def display_select_meta_data_group_dialog(self, meta_data_groups_in_db):
        """
        Opens a new popup and displays buttons to select an action: button 1: load meta data groups from template, button 2: assign all experiments to the same meta data group,
        button 3: read values from database
        :param meta_data_groups_in_db: true if for at least each experiment meta data groups are available in the database, false if not
        :return:
        """

        dialog = Select_Meta_Data_Options_Pop_Up()
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)

        # assign later button will close the dialog without any additional assignments
        dialog.assign_one_group_to_all.clicked.connect(partial(self.continue_open_directory, dialog))

        # Create Template button will open a new popup to assign different meta data groups
        dialog.assign_now_button.clicked.connect(partial(self.create_meta_data_template, dialog))

        # Load Template button will open a filedialog to select a template
        dialog.load_template_button.clicked.connect(partial(self.open_meta_data_template_file, dialog))

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
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.csv")[0]

        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            meta_data_assignments = list(reader)

        if len(meta_data_assignments[0]) <= 6:
            CustomErrorDialog().show_dialog("The template needs at least 7 columns which were not found in the specified template.")

        else:
            print("results from the template file")
            print(meta_data_assignments)
            option_list.append("dummy")
            self.continue_open_directory(dialog, option_list, meta_data_assignments)

    def create_meta_data_template(self, old_dialog):
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

        column_names = ["Experiment_name", "Experiment_label", "Species", "Genotype", "Sex", "Condition",
                        "Individuum_id"]

        template_data_frame = pd.DataFrame(columns=column_names)

        print(self.offline_manager.package_list(directory))

        for dat_file in self.offline_manager.package_list(directory):
            
            splitted_name = dat_file.split(".")
            print(dat_file)
            self.database_handler.add_experiment_to_experiment_table(splitted_name[0])
            self.database_handler.create_mapping_between_experiments_and_analysis_id(splitted_name[0])
            template_data_frame = template_data_frame.append({"Experiment_name":splitted_name[0],"Experiment_label":"None","Species":"None",
                                        "Genotype":"None","Sex":"None","Condition":"None","Individuum_id":"None"}, ignore_index=True)

        '''make a table with editable data '''

        # set the TableView and the Model
        template_table_view = QTableView()
        template_table_view.setObjectName("meta_data_tenplate")
        template_table_view.setMinimumHeight(300)
        template_table_view.horizontalHeader().setSectionsClickable(True)

        # create two models one for the table show and a second for the data visualizations
        content_model = PandasTable(template_data_frame)
        print(template_data_frame)
        template_table_view.setModel(content_model)

        # self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        template_table_view.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        meta_data_popup.meta_data_template_layout.addWidget(template_table_view)
        template_table_view.setGeometry(20, 20, 691, 581)

        # show and retrieve the selected columns
        template_table_view.show()
        #self.data_base_content.clicked.connect(self.retrieve_column)

        """
        tmp_tree_manager = TreeViewManager(self.database_handler)
        tmp_tree_manager.meta_data_group_column = 1
        tmp_tree_manager.checkbox_column = 3
        tmp_tree_manager.analysis_mode = 1
        tmp_tree_manager.frontend_style = self.frontend_style

        tmp_tree_manager.create_treeview_from_directory(meta_data_popup.meta_data_tree_widget, None,
                                                        self.offline_manager.package_list(directory), directory, 0,
                                                        None, 2)

        meta_data_popup.meta_data_tree_widget.setColumnWidth(0, 250)
        meta_data_popup.meta_data_tree_widget.setColumnWidth(1, 25)
        
        
        # meta_data_popup.save_to_template_button
        

        meta_data_popup.close_and_continue_button.clicked.connect(partial(self.continue_open_directory, meta_data_popup,
                                                                          tmp_tree_manager.meta_data_option_list,
                                                                          tmp_tree_manager.get_meta_data_group_assignments()))
        """
        meta_data_popup.save_to_template_button.clicked.connect(partial(self.save_meta_data_to_template_and_continue,
                                                                        meta_data_popup))

        meta_data_popup.exec_()

    def save_meta_data_to_template_and_continue(self, meta_data_popup):
        '''
        Save the template first and than continue directory opening.
        :param meta_data_popup:
        :param tmp_tree_manager:
        :return:
        '''
        data_frame = meta_data_popup.meta_data_template_layout.itemAtPosition(0,0).widget().model()._data
            #data(0,0).toString()
        print(data_frame)
        file_name = self.offline_manager._directory_path + "/automatic_template.csv"
        print(file_name)
        data_frame.to_csv(file_name)
        """
        self.continue_open_directory(meta_data_popup, tmp_tree_manager.meta_data_option_list,
                                     tmp_tree_manager.get_meta_data_group_assignments())
        """
    def get_selected_checkboxes(self, checkboxes, labels):
        """From two lists of checkboxes and labels one list of checked labels (string) will be returned"""
        # empty list to be filled
        checked_labels = []
        for c in checkboxes:
            if c.isChecked():
                checked_labels.append(labels[checkboxes.index(c)])
        # return filled list, can be empty too
        return checked_labels

    def compare_series_clicked(self, checkboxes, series_names, dialog):
        """Handler for a click on the button confirm_series_selection in a pop up window"""

        self.series_to_analyze = self.get_selected_checkboxes(checkboxes, series_names)
        for i in self.series_to_analyze:
            self.selected_series_combo.addItem(i)
        self.final_series.extend(self.series_to_analyze)
        dialog.close()

    def start_analysis_offline(self):
        """Starts the analysis of the selected series"""
        print(self.final_series)
        self.built_analysis_specific_tree(self.final_series)
        self.offline_analysis_widgets.setCurrentIndex(2)
        self.final_series = []
        self.selected_series_combo.clear()

    def built_analysis_specific_tree(self, series_names_list):
        """
        Function to built series name (e.g. IV, 5xRheo) specific tree. Each series get's a parent item for 3 childs:
        1) Plot - Result Visualization).
        2) Tables - Numerical Data shown in the result visualization)
        3) Statistics - Statistical Test Performed on the results
        @param series_names_list:
        @return:
        """
        # add selection to database
        self.database_handler.write_analysis_series_types_to_database(series_names_list)

        # make new tree parent elements and realted childs for ech specific series
        for index, s in enumerate(series_names_list):
            index += self.tree_widget_index_count

            # Custom designer widget: contains treeview, plot, analysis function table ...
            new_tab_widget = SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(self.select_analysis_functions, s))

            """will be filled with the related data for the treeview table"""

            new_tab_widget.setObjectName(s)

            self.tab_list.append(new_tab_widget)
            self.tab_changed(index, s)
            # fill the treetabwidgetitems
            parent = QTreeWidgetItem()
            self.SeriesItems.addTopLevelItem(parent)

            # set the child items of the widget
            configurator = QTreeWidgetItem(parent)
            configurator.setText(0,"Simple Analysis Configuration")


            self.series_list.append(s)

            # child stacked notebook per parent node
            self.hierachy_stacked = QStackedWidget()
            self.hierachy_stacked.addWidget(QWidget())
            self.analysis_stacked.addWidget(self.hierachy_stacked)

            # set important data to the parent
            parent.setText(0, s + " Analysis")
            parent.setData(1, Qt.UserRole, "parent")  # check if parent
            parent.setData(2, Qt.UserRole, new_tab_widget)  # save the widget
            parent.setData(4, Qt.UserRole, self.hierachy_stacked)  # save the child notebook
            parent.setData(5, Qt.UserRole, 0)
            parent.setData(6, Qt.UserRole, s)  # specific series name
            parent.setData(7, Qt.UserRole, index)  # save the index

            configurator.setData(2, Qt.UserRole, new_tab_widget)  # save the widget
            configurator.setData(4, Qt.UserRole, self.hierachy_stacked)  # save the child notebook
            configurator.setData(5, Qt.UserRole, 1)
            configurator.setData(6, Qt.UserRole, self.parent_count)  # specific series name
            configurator.setData(7, Qt.UserRole, index)
            self.hierachy_stacked_list.append(self.hierachy_stacked)
            self.plot_widgets = []
            self.parent_count += 1


        # connect the treewidgetsitems
        self.SeriesItems.itemClicked.connect(self.offline_analysis_result_tree_item_clicked)
        self.postgresql_upload.clicked.connect(self.start_worker)        
        #set the analysis notebook as index
        self.offline_analysis_widgets.setCurrentIndex(3)
        self.SeriesItems.expandToDepth(2)
        self.tree_widget_index_count = index +1

    def start_worker(self):
    
        self.worker = Worker(partial(PostSqlHandler, self.database_handler))
        #self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.progress_bar_update_analysis)
        self.threadpool.start(self.worker)
        

    def offline_analysis_result_tree_item_clicked(self):
        """
        Whenever an item within the result tree view is clicked, this function is called
        @return:
        @author:DZ
        @todo restructure this and move it maybe into a new class with the related functions ?
        """

        if self.SeriesItems.currentItem().data(1, Qt.UserRole) is not None:
            #self.result_analysis_parent_clicked()
            self.SeriesItems.setCurrentItem(self.SeriesItems.currentItem().child(0))
            self.offline_analysis_result_tree_item_clicked()
        else:
            """identifiy the parent"""
            if self.SeriesItems.currentItem().child(0):
                parent_stacked = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            else:
                parent_stacked = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)

            if self.SeriesItems.currentItem().text(0) == "Simple Analysis Configuration":
                self.simple_analysis_configuration_clicked(parent_stacked)

            if self.SeriesItems.currentItem().text(0) == "Plot":
                self.analysis_stacked.setCurrentIndex(parent_stacked)
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

            if self.SeriesItems.currentItem().text(0) == "Tables":
                self.view_table_clicked(parent_stacked)

            if self.SeriesItems.currentItem().text(0) == "Statistics":



                # uic the designer object
                # create in the py file an additional class named StatisticalTableWidget
                statistics_table_widget = StatisticsTablePromoted()

                self.hierachy_stacked_list[parent_stacked].insertWidget(3,statistics_table_widget)
                #statistics_table_widget.statistics_table_widget.setColumnCount(6)
                #statistics_table_widget.statistics_table_widget.setRowCount(2)
                #statistics_table_widget.statistics_table_widget.show()
                statistics_table_widget.statistics_table_widget.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                statistics_table_widget.statistics_table_widget.verticalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(3)

                series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")
                analysis_functions = self.database_handler.get_analysis_functions_for_specific_series(series_name[0])


                # -------------------
                existing_row_numbers = statistics_table_widget.statistics_table_widget.rowCount()


                if existing_row_numbers == 0:

                    # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
                    statistics_table_widget.statistics_table_widget.setColumnCount(6)
                    statistics_table_widget.statistics_table_widget.setRowCount(
                        len(analysis_functions))
                    self.statistics_table_buttons = [0] * len(analysis_functions)
                #else:
                #    current_tab.analysis_table_widget.analysis_table_widget.setRowCount(
                #        existing_row_numbers + len(self.selected_analysis_functions))
                #    self.table_buttons = self.table_buttons + [0] * len(self.selected_analysis_functions)

                self.statistics_add_meta_data_buttons = [0]*len(analysis_functions)

                for i in analysis_functions:
                    # prepare a row for each analysis
                    analysis_function = i[0]
                    print(analysis_function)
                    row_to_insert = analysis_functions.index(i) + existing_row_numbers

                    self.statistics_add_meta_data_buttons[row_to_insert] =  QPushButton("Choose")
                    self.select_checkbox = QCheckBox()
                    self.data_dist  = QComboBox()
                    self.data_dist.addItems(["Normal Distribution", "Bernoulli Distribution", "Binomial Distribution", "Poisson Distribution" ])
                    self.data_dist.setCurrentIndex(0)
                    self.stat_test = QComboBox()
                    self.stat_test.addItems(["t-Test", "Wilcoxon Test", "GLM"])
                    self.stat_test.setCurrentIndex(0)
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 0,self.select_checkbox)
                    statistics_table_widget.statistics_table_widget.setItem(row_to_insert, 1,
                                                                            QTableWidgetItem(str(analysis_function)))
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 2, self.statistics_add_meta_data_buttons[row_to_insert])

                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 3, self.data_dist)
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 4, self.stat_test)

                    self.statistics_add_meta_data_buttons[row_to_insert].clicked.connect(partial(self.select_statistics_meta_data, statistics_table_widget, row_to_insert))

                    #current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 5,
                    #                                                                      self.live_result)

                    #self.statistics_table_buttons[row_to_insert].clicked.connect(
                    #    partial(self.open_statistics_meta_data_selection,row_to_insert))
                    #self.live_result.clicked.connect(
                    #    partial(self.show_live_results_changed, row_to_insert, current_tab, self.live_result))
                    statistics_table_widget.statistics_table_widget.show()

                self.plot_home.clicked.connect(self.navigation_list[parent_stacked].home)
                self.plot_move.clicked.connect(self.navigation_list[parent_stacked].pan)
                self.plot_zoom.clicked.connect(self.navigation_list[parent_stacked].zoom)
                start_statistics = QPushButton("Run Statistic Test")
                statistics_table_widget.verticalLayout_2.addWidget(start_statistics)

                start_statistics.clicked.connect(partial(self.calculate_statistics,statistics_table_widget.statistics_table_widget))

    def calculate_statistics(self,statistics_table:QTableWidget):
        print("calculating statistic")
        for row in range(0,statistics_table.rowCount()):

            # get the test to be performed from the combo box (position 4)
            test_type = statistics_table.cellWidget(row,4).currentText()
            print(statistics_table.item(row, 1).text())
            if test_type == "t_Test":

                # get the number of comparissons (m1 vs m2)
                meta_data_comparissons = []

                for comparison in range(0,statistics_table.cellWidget(row,2).count()):

                    meta_data_comparissons.append(comparison)

                    # read the related results

                # add to the new "t-test child" if it does not exist yet

                # add to the database

            else:
                print("not implemented yet")




    def select_statistics_meta_data(self, statistics_table_widget:StatisticsTablePromoted, row_to_insert):

        # honig
        dialog = StatisticsMetaData_Handler()

        global_meta_data_table = self.database_handler.get_analysis_id_specific_global_meta_data_table_part()
        already_existing_list_widgets = [dialog.sex_list,dialog.condition_list, dialog.individuum_list]

        # n column names: the first two column names are hard coded and well known. Therefore start with the third element
        # Index(['analysis_id', 'experiment_name', 'experiment_label', 'species', 'genotype', 'sex', 'condition', 'individuum_id']
        col_cnt = 0
        for i in range(2,len(global_meta_data_table.columns)):

            unique_labels = np.unique(global_meta_data_table[global_meta_data_table.columns[i]].tolist())
            print(global_meta_data_table.columns[i], " - ", unique_labels)

            if len(unique_labels)>1:
                list_widget = already_existing_list_widgets[col_cnt]
                print(type(list_widget))
                for n in unique_labels:
                    new_list_item = QListWidgetItem(list_widget)
                    new_list_item.setText(n)

                col_cnt = col_cnt+1
                print(col_cnt)

        print("first box title = ", dialog.groupBox.title())

        grid = QGridLayout()
        self.statistics_list_view = DragAndDropListView(self, dialog.sex_list)  # dialog.sex_list)
        vs_button = QPushButton("vs")
        add_button = QPushButton("Add")
        clear_button = QPushButton("Clear Last Row")
        finish_button = QPushButton("Finish")

        self.statistics_list_view.setAcceptDrops(True)
        self.statistics_list_view.fileDropped.connect(self.meta_data_label_dropped)

        grid.addWidget(self.statistics_list_view)
        grid.addWidget(vs_button)
        grid.addWidget(add_button)
        grid.addWidget(clear_button)
        grid.addWidget(finish_button)

        dialog.groupBox_4.setLayout(grid)

        dialog.sex_list.pressed.connect(partial(self.test,dialog.sex_list,self.statistics_list_view))
        dialog.condition_list.pressed.connect(partial(self.test,dialog.condition_list,self.statistics_list_view))

        vs_button.clicked.connect(self.add_vs)
        add_button.clicked.connect(self.add_new_statistics_meta_data_row)
        clear_button.clicked.connect(self.clear_last_row)
        finish_button.clicked.connect(partial(self.finish_statistics_meta_data_popup,dialog,statistics_table_widget,row_to_insert))

        dialog.exec()

    def finish_statistics_meta_data_popup(self, dialog:StatisticsMetaData_Handler, statistics_table_widget:StatisticsTablePromoted, row_to_insert:int):
        meta_data_selection = []
        for n in range(0, self.statistics_list_view.count()):
            meta_data_selection.append(self.statistics_list_view.item(n))

        dialog.close()

        list_and_button_widget = QWidget()

        statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 2, self.statistics_list_view)
        # remove the button



    def clear_last_row(self):
        if self.statistics_list_view.count() > 0:
            self.statistics_list_view.takeItem(self.statistics_list_view.count()-1)

    def add_vs(self):
        existing_text = None
        last_item = None
        # select only the last row !!!
        last_row = 0
        for n in range(0, self.statistics_list_view.count()):
            last_item = self.statistics_list_view.item(n)
            existing_text = last_item.text()
            last_row = n
            print(last_row)

        if existing_text is None:
            # @todo add dialog
            print("error dialog: please drag and drop meta data first")
        else:
            self.statistics_list_view.takeItem(last_row)
            #self.statistics_list_view.removeItemWidget(last_item)
            self.statistics_list_view.insertItem(last_row, existing_text + " vs. " )

    def avoid_drop(self):
        print("avoiding")

    def add_new_statistics_meta_data_row(self):
        QListWidgetItem("",self.statistics_list_view)

    def test(self, widget, statistics_list_view,event):
        statistics_list_view.initial_list = widget
        print("success")
    @Slot()
    def meta_data_label_dropped(self, item_text):
        print("new label dropped = ", item_text)
        existing_text = None
        last_item = None
        last_row = 0
        for n in range(0, self.statistics_list_view.count()):
            last_item = self.statistics_list_view.item(n)
            existing_text = last_item.text()
            last_row = n
            print(last_row)

        if existing_text is None:
            QListWidgetItem(item_text, self.statistics_list_view)
        else:
            print("Last Row dropped = ", last_row)
            self.statistics_list_view.takeItem(last_row)
            QListWidgetItem(existing_text + "_" + item_text, self.statistics_list_view)

    def open_statistics_meta_data_selection(self):
        print("not implemented yet")
        
    def simple_analysis_configuration_clicked(self,parent_stacked:int):
        """
        load its parent configuration widget and display it
        @param parent_stacked:
        @return:
        """
        stacked_widget = self.SeriesItems.currentItem().parent().data(4, Qt.UserRole)
        config_widget = self.SeriesItems.currentItem().parent().child(0).data(2, Qt.UserRole)

        # insert the windget
        stacked_widget.insertWidget(0, config_widget)
        stacked_widget.setCurrentIndex(0)

        self.analysis_stacked.setCurrentIndex(parent_stacked)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(0)

    def view_table_clicked(self, parent_stacked:int):
        """
        specific function to display result tables that are stored within the related plot widget
        @param parent_stacked: position of the stacked widget
        @return:
        """
        self.analysis_stacked.setCurrentIndex(parent_stacked)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

        result_plot_widget = self.hierachy_stacked_list[parent_stacked].currentWidget()

        """create a table view within a tab widget: each tab will become one plot/one specific analysis """

        table_tab_widget = QTabWidget()

        # works only    if results are organized row wise
        print("column count =", result_plot_widget.OfflineResultGrid.columnCount())
        if result_plot_widget.OfflineResultGrid.columnCount() == 1:
            print("row count =", result_plot_widget.OfflineResultGrid.rowCount())

            for r in range(0, result_plot_widget.OfflineResultGrid.rowCount()):

                qwidget_item = result_plot_widget.OfflineResultGrid.itemAtPosition(r, 0)
                custom_plot_widget = qwidget_item.widget()
                data = custom_plot_widget.export_data_frame
                # print(data)

                if custom_plot_widget.plot_type_combo_box.currentText() == "No Split":
                    new_column_names = []
                    print(data.columns.values.tolist())

                    try:
                        for column_name in data.columns.values.tolist():
                            res = column_name.split("_")
                            new_column_names.append(res[6] + "_" + res[7])
                        data.columns = new_column_names

                    except Exception:
                        print("all ok .. nothing to split here")

                if data.empty:
                    print("Data to be displayed in the table are None. Fill the table first !")
                else:
                    print("creating the table")
                    self.model = OfflineAnalysisResultTableModel(data)
                    # Creating a QTableView
                    self.table_view = QTableView()
                    self.table_view.setModel(self.model)
                    print("setting the model")
                    horizontal_header = self.table_view.horizontalHeader()
                    horizontal_header.setSectionResizeMode(
                        QHeaderView.ResizeToContents
                    )
                    table_tab_widget.insertTab(1, self.table_view, custom_plot_widget.analysis_name)
        else:
            print("More than one column of analysis results is not implemented yet")

        self.hierachy_stacked_list[parent_stacked].insertWidget(2, table_tab_widget)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(2)

    @Slot()
    def go_backwards(self):

        index = self.offline_analysis_widgets.currentIndex()
        if index > 0:
            self.offline_analysis_widgets.setCurrentIndex(index - 1)
            self.fo_forward_button.setEnabled(True)
            if index == 1:
                self.go_back_button.setEnabled(False)


    def go_forwards(self):
        index = self.offline_analysis_widgets.currentIndex()
        if index < self.offline_analysis_widgets.count():
            self.offline_analysis_widgets.setCurrentIndex(index + 1)
            self.go_back_button.setEnabled(True)
            if index == 2:
                self.fo_forward_button.setEnabled(True)

            
    @Slot()
    def tab_changed(self, index, series_name):
        """Function tab changed will be called whenever a tab in the notebook of the selected series for analysis is
        changed. Index is the tab number correlating with a global list of tab objects self.tab_list
        @author dz, 20.07.2021, updated 02.12.2022"""

        print(series_name)
        current_tab = self.tab_list[index]
        series_name = series_name

        current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.database_handler, None, False)
        self.current_tab_visualization.append(current_tab_plot_manager)

        current_tab_tree_view_manager = TreeViewManager(self.database_handler, current_tab.widget)
        current_tab_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio

        current_tab_tree_view_manager.selected_meta_data_list = self.selected_meta_data_list

        # make a deepcopy to be able to slize the copied item without changing its parent
        current_tab_tree_view_manager.selected_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.selected_tree_view_data_table)
        current_tab_tree_view_manager.discarded_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.discarded_tree_view_data_table)

        # slice out all series names that are not related to the specific chosen one
        current_tab_tree_view_manager.create_series_specific_tree(series_name,current_tab_plot_manager)

    @Slot()
    def select_analysis_functions(self, series_name):
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
        confirm_selection_button.clicked.connect(
            partial(self.update_selected_analysis_function_table, checkbox_list, analysis_function_names, dialog))

        # 6) Add button widget to correct grid position, finally execute the dialog
        dialog_grid.addWidget(confirm_selection_button, len(analysis_function_names), 0)
        dialog.setWindowTitle("Available Analysis Functions for Series " + series_name)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def update_selected_analysis_function_table(self, checkbox_list, analysis_function_name_list, dialog):
        '''enters data into the analysis table after the dialog has been closed'''
        dialog.close()

        # read from database - if no settings have been made before execute initalization

        self.selected_analysis_functions = self.get_selected_checkboxes(checkbox_list, analysis_function_name_list)
        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)

        current_tab = self.tab_list[current_index]

        current_tab.analysis_function.addWidget(current_tab.analysis_table_widget)
        current_tab.analysis_table_widget.analysis_table_widget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        current_tab.analysis_table_widget.analysis_table_widget.verticalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        existing_row_numbers = current_tab.analysis_table_widget.analysis_table_widget.rowCount()
        #current_tab.pushButton_3.clicked.connect(self.add_filter_to_offline_analysis)

        if existing_row_numbers == 0:

            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
            current_tab.analysis_table_widget.analysis_table_widget.setColumnCount(6)
            current_tab.analysis_table_widget.analysis_table_widget.setRowCount(len(self.selected_analysis_functions))
            self.table_buttons = [0] * len(self.selected_analysis_functions)
        else:
            current_tab.analysis_table_widget.analysis_table_widget.setRowCount(
                existing_row_numbers + len(self.selected_analysis_functions))
            self.table_buttons = self.table_buttons + [0] * len(self.selected_analysis_functions)

        for row in range(len(self.selected_analysis_functions)):
            row_to_insert = row + existing_row_numbers
            value = self.selected_analysis_functions[row]
            print(str(value))
            current_tab.analysis_table_widget.analysis_table_widget.setItem(row_to_insert, 0,
                                                                            QTableWidgetItem(str(value)))

            self.table_buttons[row_to_insert] = QPushButton("Add")
            self.c = QPushButton("Configure")
            self.live_result = QCheckBox()

            current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 3,
                                                                                  self.table_buttons[row_to_insert])
            current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 4, self.c)
            current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 5, self.live_result)

            self.table_buttons[row_to_insert].clicked.connect(
                partial(self.add_coursor_bounds, row_to_insert, current_tab))
            self.live_result.clicked.connect(
                partial(self.show_live_results_changed, row_to_insert, current_tab, self.live_result))
            current_tab.analysis_table_widget.analysis_table_widget.show()

        plot_widget_manager  = self.current_tab_visualization[current_index]
        plot_widget_manager.set_analysis_functions_table_widget(
            current_tab.analysis_table_widget.analysis_table_widget)

    def show_live_results_changed(self, row_number, current_tab, checkbox_object: QCheckBox):
        """
        Function to handle activation of an analysis function specific checkbox in the analysis table. It checks if
        cursor bounds were set correctly (if not error dialog is displayed). In the analysis function objects specified
        points used for the related analysis will be added or removed within the trace plot.
        @param row_number: row of the checkbox in the analysis function table
        @param current_tab: current tab
        @param checkbox_object: QCheckbox
        @return:
        @author: dz, 01.10.2022
        """
        if checkbox_object.isChecked():
            # check if cursor bounds are not empty otherwise print dialog and unchecke the checkbox again
            try:
                lower_bound = float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 1).text())
                upper_bound = float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 2).text())
            except Exception as e:
                dialog_message = "Please select cursor bounds first and activate live plot afterwords"
                CustomErrorDialog().show_dialog(dialog_message)
                checkbox_object.setCheckState(Qt.CheckState.Unchecked)

        print("I have to make the liveplot")
       # artificial click will replot and add or delete the newly checked or unchecked analysis function
       # item = current_tab.selected_tree_widget.currentItem()
       # self.current_tab_visualization[self.SeriesItems.currentItem().data(7,
       #                                                                    Qt.UserRole)].analysis_functions_table_widget = current_tab.analysis_table_widget.analysis_table_widget
       # self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].tree_view_click_handler(
       #     item)

    #def quit_error_dialog(self, dialog: QDialog):
    #    dialog.close()

    def analysis_table_cell_changed(self, item):
        print("a cell changed")
        print(item.text())

    def remove_existing_dragable_lines(self, row_number, current_tab):
        number_of_rows = current_tab.analysis_table_widget.rowCount()

        for r in range(0, number_of_rows):
            if current_tab.analysis_table_widget.item(r, 1) is not None:
                current_tab.analysis_table_widget.removeCellWidget(r, 3)
                self.b = QPushButton("Change")
                current_tab.analysis_table_widget.setCellWidget(r, 3, self.b)

                self.b.clicked.connect(partial(self.add_coursor_bounds, r, current_tab))

                self.current_tab_visualization[
                    self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines(row_number)
            try:
                self.current_tab_visualization[
                    self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines()
            except:
                print("nothing to delete")

    def add_coursor_bounds(self, row_number, current_tab):
        """
        This function will add 2 dragable lines to the plot which will be provided by the global plot manager object
        :return:
        """

        self.current_tab_visualization[self.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines(
            row_number)

        try:
            print("read")
            left_cb_val = round(
                float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 1).text()), 2)
            right_cb_val = round(
                float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 2).text()), 2)

            # 1) insert dragable coursor bounds into pyqt graph
            left_val, right_val = self.current_tab_visualization[
                self.SeriesItems.currentItem().data(7, Qt.UserRole)].show_draggable_lines(row_number,
                                                                                          (left_cb_val, right_cb_val))


        except Exception as e:
            print(e)
            # 1) insert dragable coursor bounds into pyqt graph
            left_val, right_val = self.current_tab_visualization[
                self.SeriesItems.currentItem().data(7, Qt.UserRole)].show_draggable_lines(row_number)

        # 2) connect to the signal taht will be emitted when cursor bounds are moved by user
        self.current_tab_visualization[
            self.SeriesItems.currentItem().data(7, Qt.UserRole)].left_bound_changed.cursor_bound_signal.connect(
            self.update_left_common_labels)
        self.current_tab_visualization[
            self.SeriesItems.currentItem().data(7, Qt.UserRole)].right_bound_changed.cursor_bound_signal.connect(
            self.update_right_common_labels)

        # 3) update the function selection grid
        self.update_left_common_labels((left_val, row_number))
        self.update_right_common_labels((right_val, row_number))

        current_tab.analysis_table_widget.analysis_table_widget.removeCellWidget(row_number, 3)
        self.b = QPushButton("Change")
        current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_number, 3, self.b)
        self.b.clicked.connect(partial(self.add_coursor_bounds, row_number, current_tab))

    @Slot(tuple)
    def update_left_common_labels(self, tuple_in):
        row_number = tuple_in[1]
        value = tuple_in[0]
        self.update_cursor_bound_labels(value, 1, row_number)

    @Slot(tuple)
    def update_right_common_labels(self, tuple_in):
        row_number = tuple_in[1]
        value = tuple_in[0]
        self.update_cursor_bound_labels(value, 2, row_number)

    def update_cursor_bound_labels(self, value, column_number, row_number):
        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        current_tab = self.tab_list[current_index]
        print("updating: row = " + str(row_number) + " column=" + str(column_number) + " value= " + str(value))

        current_tab.analysis_table_widget.analysis_table_widget.setItem(row_number, column_number,
                                                                        QTableWidgetItem(str(value)))

        self.check_ready_for_analysis(current_tab)

    def check_ready_for_analysis(self, current_tab):
        """
        function that checks for coursor bounds in all selected functions in this tab to be not empty.
        if this is the case the start analysis button becomes clickable
        :param current_tab:
        :return:
        """
        # print("Checking ready  for analysis")
        for row in range(0, (current_tab.analysis_table_widget.analysis_table_widget.rowCount())):
            if current_tab.analysis_table_widget.analysis_table_widget.item(row,
                                                                            1) is None or current_tab.analysis_table_widget.analysis_table_widget.item(
                    row, 2) is None:
                return

        # make sure to connect start_analysis_button only once  .. otherwise a loop gets created # BUGFIX
        if current_tab.start_analysis_button.isEnabled() is False:
            current_tab.start_analysis_button.setEnabled(True)
            current_tab.start_analysis_button.clicked.connect(
                partial(self.start_offline_analysis_of_single_series, current_tab))

    def start_offline_analysis_of_single_series(self, current_tab):
        '''
        Performs analysis according to the selected criteria.
        Before the analysis starts, the selected criteria will be stored in the database
        :param current_tab:
        :return:
        '''

        # store analysis parameter in the database

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

    def progress_bar_update_analysis(self, data):
        """ This function will update the progress bar in the analysis tab
        :param data:
        
        """
        self.progressbar.setValue(data[0])
        self.statusbar.showMessage("Analyzing: " + str(data[1]) + "%")

    def finished_result_thread(self):
        """
        Once all the reuslt have been calculated, an offline tab is created.
        This tab visualizes all calculated results.
        Therefore, a new plot child is inserted to the related series name analysis.
        Furthermore, a table, a statistics and an advanced analysis child are added for further processing steps
        @return:
        """
        self.database_handler.open_connection()
        self.add_new_analysis_tree_children()

        if self.SeriesItems.currentItem().child(0):
            parent_item = self.SeriesItems.currentItem()
        else:
            parent_item = self.SeriesItems.currentItem().parent()

        print(parent_item.text(0))

        offline_tab = self.result_visualizer.show_results_for_current_analysis(self.database_handler.analysis_id,
                                                                                   parent_item.data(6, Qt.UserRole))



        """add the results at position 1 of the stacked widget ( position 0  is the analysis config ) """
        self.hierachy_stacked_list[parent_item.data(7, Qt.UserRole)].insertWidget(1,offline_tab)

        """simulate click on  "Plot" children """
        self.SeriesItems.setCurrentItem(parent_item.child(1))
        self.offline_analysis_result_tree_item_clicked()

    def add_new_analysis_tree_children(self):
        """
        add tree items to the analysis
            - plot for the result grpahics
            - table for the data from the result plots
            - statistics ..
            - advanced
        @param offline_tab:
        @return:
        """
        if self.SeriesItems.currentItem().data(5, Qt.UserRole) == 0: # thats the parent which is clicked
            parent_tree_item = self.SeriesItems.currentItem()
            parent_stacked_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            parent_stacked_widget = self.SeriesItems.currentItem().data(4, Qt.UserRole)
            #parent_count = parent_tree_item.child(0).data(6, Qt.UserRole)

        else: # child is clicked
            parent_tree_item = self.SeriesItems.currentItem().parent()
            parent_stacked_index = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)
            parent_stacked_widget = self.SeriesItems.currentItem().parent().data(4, Qt.UserRole)
            #parent_count = self.SeriesItems.currentItem().parent().data(6, Qt.UserRole)

        print(parent_stacked_widget.__class__.__name__)

        # add new children within the tree:
        simple_analaysis_plot = QTreeWidgetItem(parent_tree_item)
        simple_analysis_tables = QTreeWidgetItem(parent_tree_item)
        simple_analysis_statistics = QTreeWidgetItem(parent_tree_item)
        adavanced_analysis = QTreeWidgetItem(parent_tree_item)

        simple_analaysis_plot.setText(0, "Plot")
        simple_analysis_tables.setText(0, "Tables")
        simple_analysis_statistics.setText(0, "Statistics")
        adavanced_analysis.setText(0, "Advanced Analysis")

        # add new pages to the stacked widget
        parent_stacked_widget.addWidget(QWidget())
        parent_stacked_widget.addWidget(QWidget())
        parent_stacked_widget.addWidget(QWidget())
        parent_stacked_widget.addWidget(QWidget())

        # set the data for each of the child items
        # remove and use for loop
        simple_analaysis_plot.setData(4, Qt.UserRole, self.hierachy_stacked)
        simple_analaysis_plot.setData(5, Qt.UserRole, 1)
        simple_analaysis_plot.setData(6, Qt.UserRole, 0)

        simple_analysis_tables.setData(4, Qt.UserRole, self.hierachy_stacked)
        simple_analysis_tables.setData(5, Qt.UserRole, 1)
        simple_analysis_tables.setData(6, Qt.UserRole,0)

        print("added new childs")

        # overwrite the old stacked widget with the new extended stacked widget
        self.hierachy_stacked_list[parent_stacked_index] = parent_stacked_widget


    def write_function_grid_values_into_database(self, current_tab):
        """
        When the Start Single Series Analysis Button will be pressed, data from the function selection table in the
        current tab will be written into the database.
        :param current_tab: tab object from which the function selection grid will be written to the database
        :return:
        """
        row_count = current_tab.analysis_table_widget.analysis_table_widget.rowCount()
        analysis_series_name = current_tab.objectName()
        column_count = current_tab.analysis_table_widget.analysis_table_widget.columnCount()
        self.database_handler.open_connection()

        ### to be continued here
        print(row_count)
        for r in range(0, row_count):
            analysis_function = current_tab.analysis_table_widget.analysis_table_widget.item(r, 0).text()
            # print("analysis function ", analysis_function)
            lower_bound = round(float(current_tab.analysis_table_widget.analysis_table_widget.item(r, 1).text()), 2)
            upper_bound = round(float(current_tab.analysis_table_widget.analysis_table_widget.item(r, 2).text()), 2)
            # print(lower_bound)
            # print(upper_bound)
            self.database_handler.write_analysis_function_name_and_cursor_bounds_to_database(analysis_function,
                                                                                             analysis_series_name,
                                                                                             lower_bound, upper_bound)

        print("finished")

    def get_cursor_bound_value_from_grid(self, row, column, current_tab):
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
