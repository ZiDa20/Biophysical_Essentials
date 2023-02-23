
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform

from PySide6.QtTest import QTest

from Offline_Analysis.offline_analysis_manager import OfflineManager
from Offline_Analysis.error_dialog_class import CustomErrorDialog
from treeview_manager import TreeViewManager
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_designer_object import Ui_Offline_Analysis
from treeview_manager import TreeViewManager
from plot_widget_manager import PlotWidgetManager

import numpy as np
from scipy import stats
from Worker import Worker

import csv
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from functools import partial
import operator
import itertools


from PostSql_Handler import PostSqlHandler
from Pandas_Table import PandasTable
from Offline_Analysis.offline_analysis_result_visualizer import OfflineAnalysisResultVisualizer
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up_handler import Filter_Settings
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_options_pop_up_handler import Select_Meta_Data_Options_Pop_Up
from Offline_Analysis.offline_analysis_manager import OfflineManager
from Offline_Analysis.error_dialog_class import CustomErrorDialog
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup_handler import Load_Data_From_Database_Popup_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.drag_and_drop_list_view import DragAndDropListView
from QT_GUI.OfflineAnalysis.CustomWidget.ui_metadata_analysis_popup import MetadataPopupAnalysis
from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_handler import ChooseExistingAnalysis
from QT_GUI.OfflineAnalysis.CustomWidget.select_analysis_functions_handler import Select_Analysis_Functions
from QT_GUI.OfflineAnalysis.CustomWidget.analysis_table_widget import Analysis_Table_Widget

from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import StatisticsTablePromoted
from QT_GUI.OfflineAnalysis.CustomWidget.select_statistics_meta_data_handler import StatisticsMetaData_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog

from Offline_Analysis.offline_analysis_result_table_model import OfflineAnalysisResultTableModel
from animated_ap import AnimatedAP
from Offline_Analysis.tree_model_class import TreeModel

from QT_GUI.OfflineAnalysis.ui_py.SideBarTreeParentItem import SideBarParentItem, SideBarConfiguratorItem, SideBarAnalysisItem
from QT_GUI.OfflineAnalysis.ui_py.SeriesItemTreeManager import SeriesItemTreeWidget
from Offline_Analysis.FinalResultHolder import ResultHolder


from QT_GUI.OfflineAnalysis.ui_py.analysis_function_selection_manager import AnalysisFunctionSelectionManager


class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.progressbar = None
        self.statusbar = None
        self.status_label = None
        self.add_filter_button.setEnabled(False)

        
        self.threadpool = QThreadPool()
        self.final_series = []

        # style object of class type Frontend_Style that will be int
        # produced and set by start.py and shared between all subclasses
        self.frontend_style = None
        self.database_handler = None
        self.offline_tree = SeriesItemTreeWidget(self.SeriesItems_2)
        self.final_result_holder = ResultHolder()
      
        self.offline_manager = OfflineManager()
        self.offline_tree.offline_manager = self.offline_manager
        self.offline_tree.show_sweeps_radio = self.show_sweeps_radio

        self.wait_widget = None
        self.ap_timer = None
        self.offline_tree.splitter = None
        

        self.offline_analysis_widgets.setCurrentIndex(0)

        self.result_visualizer = OfflineAnalysisResultVisualizer(self.offline_tree, 
                                                                 self.database_handler, 
                                                                 self.final_result_holder)

        # might be set during blank analysis
        self.blank_analysis_page_1_tree_manager = None
        self.blank_analysis_plot_manager = None
        self.hierachy_stacked_list = self.offline_tree.hierachy_stacked_list
        self.tab_list = self.offline_tree.tab_list
        self.series_list = self.offline_tree.series_list
    
        self.offline_tree.SeriesItems.clear()

        self.parent_count = 0
        self.current_tab_visualization = self.offline_tree.current_tab_visualization
        self.current_tab_tree_view_manager = self.offline_tree.current_tab_tree_view_manager

        self.tree_widget_index_count = 0  # save the current maximal index of the tree

        # animation of the side dataframe
        
        #self.blank_analysis_button.clicked.connect(self.start_blank_analysis)
       
        self.compare_series.clicked.connect(self.select_series_to_be_analized)

        # blank analysis menu
        self.select_directory_button.clicked.connect(self.open_directory)
        self.load_from_database.clicked.connect(self.load_treeview_from_database)
        self.edit_meta.clicked.connect(self.edit_metadata_analysis_id)
        self.edit_series_meta_data.clicked.connect(self.edit_series_meta_data_popup)
        self.go_back_button.clicked.connect(self.go_backwards)
        self.fo_forward_button.clicked.connect(self.go_forwards)
        #self.load_meta_data.clicked.connect(self.load_and_assign_meta_data)
        self.start_analysis.clicked.connect(self.start_analysis_offline)
        self.navigation_list = []

        self.series_to_csv.clicked.connect(self.write_series_to_csv)
        #self.experiment_to_csv.clicked.connect(self.write_experiment_to_csv)
        

        self.show_sweeps_radio.toggled.connect(self.show_sweeps_toggled)
        self.add_meta_data_to_treeview.clicked.connect(self.select_tree_view_meta_data)
        self.parent_stacked = self.offline_tree.parent_stacked

        self.plot_home.clicked.connect(partial(self.navigation_rules, self.plot_home, "home"))
        self.plot_move.clicked.connect(partial(self.navigation_rules, self.plot_move, "move"))
        self.plot_zoom.clicked.connect(partial(self.navigation_rules, self.plot_zoom, "zoom"))


    def write_series_to_csv(self):
        file_name = QFileDialog.getSaveFileName(self,'SaveFile')[0]
        index = self.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view.currentIndex()
        tree_item_list = self.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view.model().get_data_row(index, Qt.DisplayRole)
        if tree_item_list[1][4] == "Series":
            q = f'select sweep_table_name from experiment_series where experiment_name = \'{tree_item_list[1][5]}\' and series_identifier = \'{tree_item_list[1][3]}\''
            table_name = self.database_handler.database.execute(q).fetchdf()
            table_name = table_name["sweep_table_name"].values[0]
            df = self.database_handler.database.execute(f'select * from {table_name}').fetchdf()
            df.to_csv(file_name)


        print("hello from the other side")

    def set_splitter(self, splitter):
        self.offline_tree.splitter = splitter
        self.offline_tree.add_widget_to_splitter()

    def navigation_rules(self, plot_button, action):
        """_summary_

        Args:
            plot_button (_type_): _description_
            action (_type_): _description_
        """
        print("clicking initalized")
        print(self.parent_stacked)
        navigation = NavigationToolbar(self.blank_analysis_plot_manager.canvas, self)
        if action == "home":
            plot_button.clicked.connect(navigation.home)
        elif action == "move":
            plot_button.clicked.connect(navigation.pan)
        elif action == "zoom":
            plot_button.clicked.connect(navigation.zoom)
        
        

    def select_tree_view_meta_data(self):

        # Create the Dialog to be shown to the user: The user will be allowed to check/uncheck desired labels
        dialog = SelectMetaDataForTreeviewDialog(self.database_handler, self.blank_analysis_tree_view_manager, self.blank_analysis_plot_manager)
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
        #dialog.finish_button.clicked.connect(
        #    partial(self.add_meta_data_to_tree_view,checkbox_list, name_list, dialog))

        dialog.cancel_button.clicked.connect(partial(self.close_dialog, dialog))

        dialog.setWindowTitle("Available Meta Data Label")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


    def show_sweeps_toggled(self,signal):
        """toDO add Docstrings!

        Args:
            signal (_type_): _description_
        """
        print("toggle" , self.offline_analysis_widgets.currentIndex())
        try:
            if self.offline_analysis_widgets.currentIndex()==1:
                self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
            if self.offline_analysis_widgets.currentIndex() ==2:
                 current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
                 plot_widget_manager  = self.current_tab_visualization[current_index]
                 self.current_tab_tree_view_manager[current_index].update_treeviews(plot_widget_manager)
        
        except Exception as e:
           print(e)
           CustomErrorDialog("Please select load an Experiment First")
           
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
        """_summary_: Should add the Database Handler Singleton

        Args:
            updated_object (database_handler): DuckDB Database Handler Class
        """
        self.database_handler = updated_object
        self.offline_manager.database = updated_object
        self.result_visualizer.database_handler = updated_object
        self.offline_tree.database_handler = updated_object
        self.final_result_holder.database_handler = updated_object
        
    def edit_metadata_analysis_id(self):
        """ Popup Dialog to edit the metadata of the selected experiments 
        """
        edit_data = MetadataPopupAnalysis()
        self.frontend_style.set_pop_up_dialog_style_sheet(edit_data)
        edit_data.quit.clicked.connect(edit_data.close)
        metadata_table = QTableView()
        q = f'select * from global_meta_data where experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})'
        table_handling = self.database_handler.get_data_from_database(self.database_handler.database, q, fetch_mode = 2)
        table_model = PandasTable(table_handling)
        metadata_table.setModel(table_model)
        edit_data.final_table_layout.addWidget(metadata_table)
        edit_data.exec()
        
    def edit_series_meta_data_popup(self):
        """ 
            Popup Dialog to edit the metadata of the related series
        """
        edit_data = MetadataPopupAnalysis()
        self.frontend_style.set_pop_up_dialog_style_sheet(edit_data)
        edit_data.quit.clicked.connect(edit_data.close)
        metadata_table = QTableView()
        q = f'select * from experiment_series where experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})'
        table_handling = self.database_handler.get_data_from_database(self.database_handler.database, q, fetch_mode = 2)
        table_model = PandasTable(table_handling)
        metadata_table.setModel(table_model)
        edit_data.final_table_layout.addWidget(metadata_table)
        edit_data.submit.clicked.connect(partial(self.submit_table_into_db, edit_data, q))
        edit_data.exec()
    
    def submit_table_into_db(self, dialog, query):
        old_df = self.database_handler.get_data_from_database(self.database_handler.database, query, fetch_mode = 2)
        new_df = dialog.final_table_layout.itemAtPosition(0,0).widget().model()._data
        df = pd.merge(new_df, old_df, on=['experiment_name','series_identifier', 'series_meta_data'], how="left", indicator=True
              ).query('_merge=="left_only"')

        for index, row in df.iterrows():
            q = f'update experiment_series set series_meta_data = \'{row["series_meta_data"]}\' where experiment_name = \'{row["experiment_name"]}\' and series_identifier = \'{row["series_identifier"]}\''
            self.database_handler.database.execute(q)

        dialog.close()

    def show_open_analysis_dialog(self):
        dialog = ChooseExistingAnalysis()
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
        data = self.database_handler.database.execute('select * from offline_analysis').fetchdf()
        table_model = PandasTable(data)
        dialog.tableView.setModel(table_model)
        dialog.submit.clicked.connect(partial(self.open_analysis_results, dialog))
        dialog.exec()
        
    @Slot()
    def open_analysis_results(self, dialog):
        """
        Open an existing analysis from the database
        :return:
        """

        id = dialog.lineEdit.text() # change this to a new name
        dialog.close()

        # static offline analysis number
        self.database_handler.analysis_id = int(id)
        series_names_list = self.database_handler.get_analysis_series_names_for_specific_analysis_id()
        print(series_names_list)

        for i in range(len(series_names_list)):
            series_names_list[i] = series_names_list[i][0]
        #    self.result_visualizer.show_results_for_current_analysis(9,name)

        self.offline_tree.built_analysis_specific_tree(series_names_list, self.select_analysis_functions, self.offline_analysis_widgets, self.selected_meta_data_list)
        print("displaying to analysis results: ", self.database_handler.analysis_id)

        print(self.offline_tree.SeriesItems.topLevelItemCount())


        # @todo DZ write the reload of the analyis function grid properly and then choose to display plots only when start analysis button is enabled
        for parent_pos in range(self.offline_tree.SeriesItems.topLevelItemCount()):

            self.offline_tree.offline_tree.SeriesItems.setCurrentItem(self.offline_tree.SeriesItems.topLevelItem(parent_pos).child(0))
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
        
        navigation = NavigationToolbar(self.blank_analysis_plot_manager.canvas, self)
        self.plot_home.clicked.connect(navigation.home)
        self.plot_move.clicked.connect(navigation.pan)
        self.plot_zoom.clicked.connect(navigation.zoom)
        self.blank_analysis_plot_manager.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        # open a popup to allow experiment label selection by the user
        # the dialog handler has further implementations to handle displayed lists etc
        self.load_data_from_database_dialog = Load_Data_From_Database_Popup_Handler(self.database_handler)
        # set light or dark mode
        self.frontend_style.set_pop_up_dialog_style_sheet(self.load_data_from_database_dialog)
 
        self.load_data_from_database_dialog.load_data.clicked.connect(self.load_page_1_tree_view)
        #self.load_data_from_database_dialog.checkbox_checked(self.load_data_from_database_dialog.all_cb,"All",2)
        self.load_data_from_database_dialog.all_cb.setChecked(True)
        self.load_data_from_database_dialog.exec_()
        
        
        #self.load_data_from_database_dialog.all_cb.setChecked(True)

    def load_page_1_tree_view(self):
        """

        @return:
        """
        self.canvas_grid_layout.addWidget(self.wait_widget)

        self.selected_meta_data_list = []

        for cb in self.load_data_from_database_dialog.checkbox_list:
            if cb.isChecked():
                pos = self.load_data_from_database_dialog.checkbox_list.index(cb)
                self.selected_meta_data_list.append(self.load_data_from_database_dialog.available_labels[pos][0])
        
        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)
        self.blank_analysis_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio

        self.blank_analysis_tree_view_manager.selected_meta_data_list = self.selected_meta_data_list

        self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
        self.offline_tree.blank_analysis_tree_view_manager = self.blank_analysis_tree_view_manager

        self.load_data_from_database_dialog.close()
        self.treebuild.directory_tree_widget.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(1)
        index =  self.treebuild.selected_tree_view.model().index(0, 0, self.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
        self.treebuild.selected_tree_view.setCurrentIndex(index)
        # Get the rect of the index
        rect = self.treebuild.selected_tree_view.visualRect(index)
        QTest.mouseClick(self.treebuild.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())

    def load_recordings(self, progress_callback):
        """_summary_

        Args:
            progress_callback (_type_): _description_
        """

        self.progress_callback = progress_callback
        self.database_handler.open_connection(read_only=True)
        experiment_label = ""
        self.blank_analysis_page_1_tree_manager.selected_meta_data_list = self.selected_meta_data_list
        self.offline_tree.selected_meta_data_list = self.selected_meta_data_list
        self.blank_analysis_page_1_tree_manager.create_treeview_from_database(experiment_label, None,
                                                                              self.progress_callback)

    def finished_database_loading(self):
        """The finish signal which is emitted after after treeview filling and database reading
        """

        print("here we finish the database")
        self.database_handler.open_connection()
        for experiment in self.blank_analysis_page_1_tree_manager.not_discard_experiments_stored_in_db:
            self.database_handler.create_mapping_between_experiments_and_analysis_id(experiment)
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

    def continue_open_directory(self, enter_meta_data_dialog, meta_data_group_assignment_list=None):
        '''
        Function will continue the function open directory after any continue button in the meta data group dialog has
        been clicked. At first the popup will be closed, all data will be loaded immediately into the databse
        :param pop_up_dialog:
        :param meta_data_group_assignment_list: list of tuples of experiment name and assigned meta data group
        :return:
        '''

        # close the dialog
        enter_meta_data_dialog.close()

        # show animation
        #for i in range(self.canvas_grid_layout.count()): 
        #        self.canvas_grid_layout.itemAt(i).widget().deleteLater()

        self.canvas_grid_layout.addWidget(self.wait_widget)

        # create a new treeview manager 
        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)

        # read the directory data into the database
        self.blank_analysis_tree_view_manager = self.offline_manager.read_data_from_experiment_directory(self.blank_analysis_tree_view_manager, meta_data_group_assignment_list)
        
        # assign meta data 
        if not meta_data_group_assignment_list:
            meta_data_group_assignment_list = []
        
        else:
            for n in meta_data_group_assignment_list:
                print("adding meta data to existing experiment ", n)
                self.database_handler.add_meta_data_group_to_existing_experiment(n)
                #self.database_handler.global_meta_data_table.add_meta_data_group_to_existing_experiment(n)

        

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
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
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

        self.create_meta_data_template()

        """
        dialog = Select_Meta_Data_Options_Pop_Up()



        # fill the layout with a default table

        
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
        """

    def open_meta_data_template_file(self,template_table_view):
        meta_data_assignments = []
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.csv")[0]

        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            meta_data_assignments = list(reader)

        if len(meta_data_assignments[0]) <= 7:
            CustomErrorDialog().show_dialog("The template needs at least 8 columns which were not found in the specified template.")

        else:
            df = pd.DataFrame(meta_data_assignments[1:], columns=meta_data_assignments[0])
            # create two models one for the table show and a second for the data visualizations
            content_model = PandasTable(df)
            template_table_view.setModel(content_model)
            template_table_view.show()
        #self.data_base_content.clicked.connect(self.retrieve_column)

    def create_meta_data_template(self):
        '''
        Creates a new dialog popup to create a new meta data template. The created template can be saved or not
        :param dialog: open dialog object
        :return:
        '''

        # open a new dialog with a tree view representation of the selected directory - only on experiment and series level
        meta_data_popup = Assign_Meta_Data_PopUp()
        self.frontend_style.set_pop_up_dialog_style_sheet(meta_data_popup)

        directory = self.offline_manager._directory_path

        column_names = ["Experiment_name", "Experiment_label", "Species", "Genotype", "Sex", "Celltype","Condition",
                        "Individuum_id"]

        template_data_frame = pd.DataFrame(columns=column_names)

        print(self.offline_manager.package_list(directory))

        for dat_file in self.offline_manager.package_list(directory):
            
            if isinstance(dat_file, list):
                splitted_name = "_".join(dat_file[0].split("_")[:2])
                self.database_handler.add_experiment_to_experiment_table(splitted_name)
            else:
                splitted_name = dat_file.split(".")
                self.database_handler.add_experiment_to_experiment_table(splitted_name[0])
            print(dat_file)
            if isinstance(dat_file, list):
                self.database_handler.create_mapping_between_experiments_and_analysis_id(splitted_name)
                template_data_frame = template_data_frame.append({"Experiment_name":splitted_name,"Experiment_label":"None","Species":"None",
                                        "Genotype":"None","Sex":"None","Celltype":"None","Condition":"None","Individuum_id":"None"}, ignore_index=True)
            else:
                self.database_handler.create_mapping_between_experiments_and_analysis_id(splitted_name)
                template_data_frame = template_data_frame.append({"Experiment_name":splitted_name[0],"Experiment_label":"None","Species":"None",
                                        "Genotype":"None","Sex":"None","Celltype":"None","Condition":"None","Individuum_id":"None"}, ignore_index=True)



        '''make a table with editable data '''

        # set the TableView and the Model
        template_table_view = QTableView()
        template_table_view.setObjectName("meta_data_template")
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


        meta_data_popup.save_to_template_button.clicked.connect(partial(self.save_meta_data_to_template_and_continue,
                                                                        meta_data_popup))


        meta_data_popup.load_template.clicked.connect(partial(self.open_meta_data_template_file,template_table_view))


        meta_data_popup.continue_loading.clicked.connect(partial(self.make_list,meta_data_popup,template_table_view))


        meta_data_popup.exec_()
        
    def make_list(self,popup,treeview_model):
        m_list = treeview_model.model()._data.values.tolist()

        self.continue_open_directory(popup,m_list)


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
        data_frame.to_csv(file_name, index = False)
        """
        self.continue_open_directory(meta_data_popup, tmp_tree_manager.meta_data_option_list,
                                     tmp_tree_manager.get_meta_data_group_assignments())
        """


        m_list = data_frame.values.tolist()
        self.continue_open_directory(meta_data_popup,m_list)

    def get_selected_checkboxes(self, checkboxes, labels):
        """From two lists of checkboxes and labels one list of checked labels (string) will be returned"""
        return [labels[checkboxes.index(c)] for c in checkboxes if c.isChecked()]

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

        self.offline_tree.built_analysis_specific_tree(self.final_series, 
                                                       self.select_analysis_functions,
                                                       self.offline_analysis_widgets,
                                                       self.selected_meta_data_list)
        
        self.offline_analysis_widgets.setCurrentIndex(2)
        self.final_series = []
        self.selected_series_combo.clear()
        self.offline_tree.click_top_level_item()

    def start_worker(self):
        """Starts the Postgres Sql Worker to upload the tables 
        as background thread
        toDO rename
        """
        self.worker = Worker(partial(PostSqlHandler, self.database_handler))
        #self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.progress_bar_update_analysis)
        self.threadpool.start(self.worker)
        
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
        meta_data_selection = [
            self.statistics_list_view.item(n)
            for n in range(self.statistics_list_view.count())
        ]
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
        for n in range(self.statistics_list_view.count()):
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
        for n in range(self.statistics_list_view.count()):
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
        stacked_widget = self.offline_tree.SeriesItems.currentItem().parent().data(4, Qt.UserRole)
        config_widget = self.offline_tree.SeriesItems.currentItem().parent().child(0).data(2, Qt.UserRole)

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

            for r in range(result_plot_widget.OfflineResultGrid.rowCount()):

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
    def select_analysis_functions(self, series_name):
        """ open a popup dialog for the user to select available analysis functions """

        # 1) create dialog
        dialog = Select_Analysis_Functions(self.database_handler,series_name)
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
        dialog.continue_with_selection.clicked.connect(partial(self.update_selected_analysis_function_table,dialog))
        dialog.exec_()
        
    def update_selected_analysis_function_table(self, dialog):
        """
        takes the user made input from the select analysis function dialog and creates a visualization allowing further configuration
        such as cursor bound drag and drop, pgf segment selection and live result visualization 
        """

        #enters data into the analysis table after the dialog has been closed
        dialog.close()

        #get the user made selections: can be either single interval or multiple interval analysis """
        #stored within a list of tuples: first item is either 'single' or 'multiple', second is a list of lists with analysis functions and operands """
        self.selected_analysis_functions = dialog.selected_analysis_functions

        # get the index of the tab (e.g. tabe name might be IV, IV-40)
        current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
        current_tab = self.tab_list[current_index]
        plot_widget_manager  = self.current_tab_visualization[current_index]

        # all the analysis setup clicks and cursor bound drag and drops will be handled from the analysis function selection manager
        self.analysis_function_selection_manager = AnalysisFunctionSelectionManager(self.database_handler, plot_widget_manager , current_tab, dialog.selected_analysis_functions)

        self.analysis_function_selection_manager.run_analysis_functions.clicked.connect(partial(self.start_offline_analysis_of_single_series,current_tab))

    def start_offline_analysis_of_single_series(self, current_tab):
        '''
        Performs analysis according to the selected criteria.
        Before the analysis starts, the selected criteria will be stored in the database
        :param current_tab:
        :return:
        '''

        self.worker = Worker(self.run_database_thread, current_tab)
        self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.progress_bar_update_analysis)
        self.threadpool.start(self.worker)
    
    def show_ap_simulation(self):

        ap = AnimatedAP()

        # Create the animation using the update function and the time points as frames
        ani = animation.FuncAnimation(ap.fig, ap.anim_update, frames=len(ap.time), blit=True)

        # Add labels to the x- and y-axes
        #ax.set_xlabel('Time (ms)')
        #ax.set_ylabel('Membrane Potential (mV)')
        plt.show()
        # Display the animation
        #ap.show_dialog()


    def run_database_thread(self, current_tab, progress_callback):
        """ This function will run the analysis in a separate thread, that is selected
        by the analysis function
        :param current_tab:
        :param progress_callback:
        """

        current_tab.stackedWidget.setCurrentIndex(1)
        current_tab.calc_animation_layout.addWidget(self.wait_widget,0,0)

        self.database_handler.open_connection()

        print("writing analysis to database")
        self.multiple_interval_analysis = self.analysis_function_selection_manager.write_table_widget_to_database()

        print("finished: ", self.multiple_interval_analysis)

        # self.write_function_grid_values_into_database(current_tab)

        self.offline_manager.execute_single_series_analysis(current_tab.objectName(), progress_callback)
        self.database_handler.database.close()

        #@todo remove the widget from the layout
        current_tab.stackedWidget.setCurrentIndex(0)


    def progress_bar_update_analysis(self, data):
        """ This function will update the progress bar in the analysis tab
        :param data:
        
        """
        self.progressbar.setValue(data[0])
        #self.statusbar.showMessage("Analyzing: " + str(data[1]) + "%")
        self.status_label.setText(f"Analyzing: {str(data[1])}%")
    
    def solve_calculation(self, equation_components):
        """
        input = list of components
        """
        # evaluate content from brackets first
        l_brack_pos = []
        r_brack_pos = []
        for i, item in enumerate(equation_components):
            if item == Select_Analysis_Functions.L_BRACK:
                l_brack_pos.append(i)
            if item == Select_Analysis_Functions.R_BRACK:
                r_brack_pos.append(i)
        

    def finished_result_thread(self):
        """
        Once all the reuslt have been calculated, an offline tab is created.
        This tab visualizes all calculated results.
        Therefore, a new plot child is inserted to the related series name analysis.
        Furthermore, a table, a statistics and an advanced analysis child are added for further processing steps
        @return:
        """

        self.database_handler.open_connection()

        if not self.multiple_interval_analysis.empty:

            self.finish_multiple_interval_analysis()
            
        else:
            print("postprocessing not needed")
        
        self.offline_tree.add_new_analysis_tree_children()

        if self.offline_tree.SeriesItems.currentItem().child(0):
            parent_item = self.offline_tree.SeriesItems.currentItem()
        else:
            parent_item = self.offline_tree.SeriesItems.currentItem().parent()

        print(parent_item.text(0))

        offline_tab = self.result_visualizer.show_results_for_current_analysis(self.database_handler.analysis_id,
                                                                                   parent_item.data(6, Qt.UserRole))

        """add the results at position 1 of the stacked widget ( position 0  is the analysis config ) """
        self.hierachy_stacked_list[parent_item.data(7, Qt.UserRole)].insertWidget(1,offline_tab)
        analysis_function_tuple = self.database_handler.get_series_specific_analysis_functions(self.offline_tree.SeriesItems.currentItem().parent().data(6,Qt.UserRole))
        analysis_function_tuple = tuple(i[1] for i in analysis_function_tuple)
        self.offline_tree.SeriesItems.currentItem().parent().setData(8, Qt.UserRole,analysis_function_tuple)
        """simulate click on  "Plot" children """
        self.offline_tree.SeriesItems.setCurrentItem(parent_item.child(1))
        self.offline_tree.offline_analysis_result_tree_item_clicked()

    def finish_multiple_interval_analysis(self):
        """
        run the post processing of multiple interval analysis:
        so far, each interval was calculated in a separate thread
        now, single intervals needs to be subtracted/divided according the selected analysis syntax
        """

        # this dataframe has been filled before single interval analysis started
        self.multiple_interval_analysis = self.multiple_interval_analysis.reset_index()
        
        print(self.multiple_interval_analysis)
        print("postprocessing started .. hang tight ")

        page_ids = self.multiple_interval_analysis['page'].unique()

        for page in page_ids:

            related_intervals = self.multiple_interval_analysis[self.multiple_interval_analysis['page'] == page]
            print("have to calculate this: ")

            # this is the calculation equation 
            print(related_intervals["func"].values[0])
            
            # split string into list, e.g. max_current - min_current
            # @todo: can this be done better ? 
            equation_components = related_intervals["func"].values[0].split(" \n ")
            equation_components.remove("")

            #reconstrcut the text before pop
            db_text = ""
            for c in equation_components:
                db_text = db_text + c + " "

            # replace function name by related analysis_function_id
            func_counter = 0
            func_to_remove = []

            for i in range(len(equation_components)):

                if equation_components[i] not in ["+", "-", "*", "/", "(", ")"]: 

                    equation_components[i] = related_intervals["id"].values[func_counter]
                    func_to_remove.append(equation_components[i])
                    func_counter += 1

            

            # stat recursive function
            self.recursive_pop(equation_components,0, 0)

            # if everything worked correctly, only the first func to remove should still exist in the analysis functions table
            # the name here needs to be adapted too 
         

            q = f'update analysis_functions set function_name = \'{db_text}\' where analysis_function_id == {func_to_remove[0]}'
            self.database_handler.database.execute(q)

            print(func_to_remove)

    def recursive_pop(self, equation_components,func_pos, pop_count, eval_dict = None):
        """take 3 elements from the list: an operand and the expression left to it and right to it, either expression are 
            a unevaluated analysis function ids or an evaluated result.
            Calculation results are pushed to the list and the function continues until list is empty """
        
        # per default read tables from db (==1), if preprocessing was performed, read the preprocessed data table (==0)
        read_data_1_from_db = 1
        read_data_2_from_db = 1

        if eval_dict is None:
            eval_dict = {}

        # check for brackets and evaluate the bracket term first
        if "(" in equation_components:
            i1 = equation_components.index("(")
            i2 = equation_components.index(")") 
            op_index = self.get_operand_index(equation_components[i1:i2]) + i1

            # make sure to check for brackets to be removed
            if equation_components[op_index-2] == "(" and equation_components[op_index+2] == ")":
                equation_components.pop(op_index-2)
                equation_components.pop(op_index+1)
                op_index -= 1
        else:
            op_index = self.get_operand_index(equation_components)
        
        # take the operand and the item left to it (-1) and right to it (+1)
        func_1 = equation_components[op_index-1]
        func_2 = equation_components[op_index+1]
        operand = equation_components[op_index]

        # remove the selected items from the list
        equation_components.pop(op_index)
        equation_components.pop(op_index)
        equation_components.pop(op_index-1)


        if func_1 in eval_dict.keys():
            data_1_table_names = eval_dict[func_1]
            read_data_1_from_db = 0
        else:
            q = f'select specific_result_table_name from results where analysis_function_id == {func_1}'
            data_1_table_names = self.database_handler.database.execute(q).fetchall()
            data_1_table_names = self.extract_first_elements(data_1_table_names)

        if func_2 in eval_dict.keys():
            data_2_table_names = eval_dict[func_2]
            read_data_2_from_db = 0
        else:
            q = f'select specific_result_table_name from results where analysis_function_id == {func_2}'
            data_2_table_names = self.database_handler.database.execute(q).fetchall()
            data_2_table_names = self.extract_first_elements(data_2_table_names)
        
        sub_results = []
        for tbl_1, tbl_2 in zip(data_1_table_names, data_2_table_names):
                if read_data_1_from_db:
                    try:
                        data_1 = self.database_handler.database.execute(f'select * from {tbl_1}').fetchdf()
                        # remove table 1
                        self.database_handler.database.execute(f'drop table {tbl_1}')
                    except Exception as e:
                        print(e)
                else:
                    data_1 = tbl_1
                
                if read_data_2_from_db:
                    try:
                        data_2 = self.database_handler.database.execute(f'select * from {tbl_2}').fetchdf()
                        # remove table 2
                        self.database_handler.database.execute(f'drop table {tbl_2}')
                    except Exception as e:
                        print(e)
                else:
                    data_2 = tbl_2

                if operand == "-":
                    try:
                        res = data_1["Result"] - data_2["Result"]
                    except Exception as e:
                        print(e)
                if operand == "/":
                        res = data_1["Result"] / data_2["Result"]

                # override table 1 and append for further processing
                data_1["Result"] = res
                sub_results.append(data_1)
                
                if equation_components == []:
                    # register only if finished, sub results dont need to be stored in the db
                    table_name = "results_analysis_function_"+str(func_1)+"_"+ str(data_1["Sweep_Table_Name"].values[0])
                    
                    self.database_handler.database.register(table_name, data_1)
                    self.database_handler.database.execute(f'CREATE TABLE {table_name} AS SELECT * FROM {table_name}')
        
        # delete the id from the analysis functions table
        self.database_handler.database.execute(f'delete from analysis_functions where analysis_function_id == {func_2}')

        if equation_components == []:
            print("my job is done")
            #q = f'update analysis_functions set function_text = {dummy text} where analysis_function_id == {func_1}'
            self.database_handler.database.execute(q)
            return
        else:
            eval_dict[func_1]=sub_results
            equation_components.insert(op_index-1,func_1)
            self.recursive_pop(equation_components,func_pos, pop_count,eval_dict)

    def get_operand_index(self,equation_components):

        # consider mathematical rang of operands and evaluate * and / first
        if "/" in equation_components:
           op_index = equation_components.index("/")            
        elif "*" in equation_components:
            op_index = equation_components.index("*")
        else:
            for c in equation_components:
                if c in ["+", "-", "*", "/"]:
                    return equation_components.index(c)

        return op_index


    def extract_first_elements(self,lst):
        return [t[0] for t in lst]
    
