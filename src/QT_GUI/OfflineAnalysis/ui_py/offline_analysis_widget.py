
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform

from PySide6.QtTest import QTest
from Offline_Analysis.offline_analysis_manager import OfflineManager
from Backend.treeview_manager import TreeViewManager
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_designer_object import Ui_Offline_Analysis
from Backend.treeview_manager import TreeViewManager
from Backend.plot_widget_manager import PlotWidgetManager

import numpy as np
from Threading.Worker import Worker

import csv
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from functools import partial
import operator
import itertools


from database.PostSql_Handler import PostSqlHandler
from Offline_Analysis.offline_analysis_result_visualizer import OfflineAnalysisResultVisualizer

from Offline_Analysis.offline_analysis_manager import OfflineManager
from Offline_Analysis.error_dialog_class import CustomErrorDialog
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup_handler import Load_Data_From_Database_Popup_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.drag_and_drop_list_view import DragAndDropListView
from QT_GUI.OfflineAnalysis.CustomWidget.select_analysis_functions_handler import Select_Analysis_Functions
#from QT_GUI.OfflineAnalysis.CustomWidget.analysis_table_widget import Analysis_Table_Widget

from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_handler import ChooseExistingAnalysis
from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import StatisticsTablePromoted
from QT_GUI.OfflineAnalysis.CustomWidget.select_statistics_meta_data_handler import StatisticsMetaData_Handler

from Offline_Analysis.offline_analysis_result_table_model import OfflineAnalysisResultTableModel
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import AnalysisFunctionRegistration
from QT_GUI.OfflineAnalysis.ui_py.SeriesItemTreeManager import SeriesItemTreeWidget
from Offline_Analysis.FinalResultHolder import ResultHolder
from QT_GUI.OfflineAnalysis.ui_py.OfflineDialogs import OfflineDialogs

from QT_GUI.OfflineAnalysis.ui_py.analysis_function_selection_manager import AnalysisFunctionSelectionManager
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up_handler import Filter_Settings

from QT_GUI.OfflineAnalysis.CustomWidget.change_series_name_handler import ChangeSeriesName


class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.progressbar = None
        self.statusbar = None
        self.status_label = None
    
        self.threadpool = QThreadPool()
        # style object of class type Frontend_Style that will be int
        # produced and set by start.py and shared between all subclasses
        self.frontend_style = None
        self.database_handler = None
        self.object_splitter = None
        self.final_result_holder = ResultHolder()
        self.offline_manager = OfflineManager()
        self.selected_series_combo.view().setFixedWidth(100)
        self.wait_widget = None
        self.ap_timer = None
        self.offline_analysis_widgets.setCurrentIndex(0)
        # might be set during blank analysis
        self.blank_analysis_page_1_tree_manager = None
        self.blank_analysis_plot_manager = None
        
        self.parent_count = 0
        #self.offline_tree.current_tab_visualization = self.offline_tree.current_tab_visualization
        #self.offline_tree.current_tab_tree_view_manager = self.offline_tree.current_tab_tree_view_manager

        self.tree_widget_index_count = 0  # save the current maximal index of the tree
        # animation of the side dataframe
        self.final_series = []
        self.notebook = None # variable for hodling the main stacked widget describing the program
        #self.blank_analysis_button.clicked.connect(self.start_blank_analysis)
        # blank analysis menu
        self.select_directory_button.clicked.connect(self.open_directory)
        self.load_from_database.clicked.connect(self.load_treeview_from_database)
        
        # forward and backward button
        self.go_back_button.clicked.connect(self.go_backwards)
        self.fo_forward_button.clicked.connect(self.go_forwards)
        #self.load_meta_data.clicked.connect(self.load_and_assign_meta_data)
        self.start_analysis.clicked.connect(self.start_analysis_offline)
        #self.experiment_to_csv.clicked.connect(self.write_experiment_to_csv)
        self.show_sweeps_radio.toggled.connect(self.update_gui_treeviews)
        # this should be transfer to the plot manager 
        # and called with the connected elements

        self.add_filter_button.clicked.connect(self.open_filter_dialog)
        self.filter_dialog = None

        self.change_series_name.clicked.connect(self.open_change_series_name_dialog)

    
    def open_change_series_name_dialog(self):
        dialog = ChangeSeriesName(self.database_handler)
        dialog.apply.clicked.connect(partial(self.update_after_series_change,dialog))
        dialog.exec_()
        

    def update_after_series_change(self,dialog):
        dialog.excecute_rename()
        self.update_gui_treeviews()
        dialog.close()



    def open_filter_dialog(self):
        """
        open the filter dialog.
        dialog is safed global to be reused for the whole analysis
        """
        if self.filter_dialog is None:
            # if none, the dialog is created initially
            self.filter_dialog = Filter_Settings(self.frontend_style,self.database_handler)
            self.filter_dialog.apply_filter_button.clicked.connect(partial(self.apply_filter_selection))

        # dialog contains a tab widget which holds filter functions for experiments (0) and series (1)
        # experiment filters can be applied on series level to, but not the other way round
    
        if self.offline_analysis_widgets.currentIndex() ==1:
            # get the index of the tab (e.g. tabe name might be IV, IV-40)
            self.filter_dialog.SeriesItems = self.offline_tree.SeriesItems
            self.filter_dialog.current_tab_visualization = self.offline_tree.current_tab_visualization
            self.filter_dialog.current_tab_tree_view_manager = self.offline_tree.current_tab_tree_view_manager
            self.filter_dialog.make_cslow_plot()

        self.filter_dialog.tabWidget.setCurrentIndex(self.offline_analysis_widgets.currentIndex())
        self.filter_dialog.exec()

    def apply_filter_selection(self):
        
        if self.filter_dialog.DISCARD_DATA:
            # for now, mark all the experiments as discarded
            # @todo: double check whether it might be more clever to remove the from offline analysis mapping table
            if self.filter_dialog.contains_series_list is not []:               

                # only keep experiment_names with 2 and more counts
                q = f'select experiment_name from experiment_analysis_mapping where analysis_id == {self.database_handler.analysis_id}'
                list_of_all_experiments = self.database_handler.database.execute(q).fetchall()
                list_of_all_experiments = self.extract_first_elements(list_of_all_experiments)


                # prepare the sql expression:
                q1 = ""
                for pos in range(len(self.filter_dialog.contains_series_list)):

                        q1 = q1 + f' series_name == \'{self.filter_dialog.contains_series_list[pos]}\' '

                        if pos < len(self.filter_dialog.contains_series_list) - 1:
                            q1 += " or "

                for experiment_name in list_of_all_experiments:
                     q = f' select series_identifier from experiment_series where experiment_name == \'{experiment_name}\' and ({q1})'
                     occurency_cnts = self.database_handler.database.execute(q).fetchall()
                     if len(self.extract_first_elements(occurency_cnts))<2:
                        
                        # discard
                        q = f"update experiment_series set discarded = 1 where experiment_name == \'{experiment_name}\'"
                        self.database_handler.database.execute(q).fetchall()

                self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
                               
   

                #update experiment_series set discarded = True 

                print(self.filter_dialog.contains_series_list)

        self.filter_dialog.close()

    def update_gui_treeviews(self,signal=None):
        """toDO add Docstrings!

        Args:
            signal (_type_): _description_
        """
        print("update treeviewsd for index" , self.offline_analysis_widgets.currentIndex())
        try:
            if self.offline_analysis_widgets.currentIndex()==0:
                self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
            if self.offline_analysis_widgets.currentIndex() ==1: #@toDO check toggle notebook ind
                 current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
                 plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]
                 self.offline_tree.current_tab_tree_view_manager[current_index].update_treeviews(plot_widget_manager)
        
        except Exception as e:
           print(e)
           CustomErrorDialog("Please select load an Experiment First", self.frontend_style)
           
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

    def add_splitter(self):
         self.offline_tree.add_widget_to_splitter(self.object_splitter)


    def update_database_handler_object(self, updated_object, frontend_style, notebook):
        """_summary_: Should add the Database Handler Singleton

        Args:
            updated_object (database_handler): DuckDB Database Handler Class
        """
        self.database_handler = updated_object
        self.frontend_style = frontend_style
        self.notebook = notebook
        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild, self.show_sweeps_radio)
        self.offline_manager.database = updated_object
        self.final_result_holder.database_handler = updated_object
        
        self.blank_analysis_plot_manager = PlotWidgetManager(self.canvas_grid_layout, self.database_handler, None, False,  self.frontend_style)
        self.offline_tree = SeriesItemTreeWidget(self.SeriesItems_2, 
                                                 [self.plot_home, self.plot_zoom, self.plot_move],
                                                 self.frontend_style,
                                                 self.database_handler,
                                                 self.offline_manager,
                                                 self.show_sweeps_radio,
                                                 self.blank_analysis_tree_view_manager)
        
       
        self.offline_tree.SeriesItems.clear()

        #self.delete_selected.clicked.connect(partial(self.offline_tree.add_analysis_tree_selection, self.offline_analysis_widgets.currentIndex()))
        
        self.result_visualizer = OfflineAnalysisResultVisualizer(self.offline_tree, 
                                                                 self.database_handler, 
                                                                 self.final_result_holder,
                                                                 self.frontend_style,
                                                                 self.plot_meta,
                                                                 self.object_splitter)

        self.plot_meta.clicked.connect(self.result_visualizer.open_meta_data)
        self.OfflineDialogs = OfflineDialogs(self.database_handler, 
                                             self.offline_manager, 
                                             self.frontend_style,
                                             self.blank_analysis_plot_manager,
                                             self.blank_analysis_tree_view_manager)
        
        self.edit_meta.clicked.connect(self.OfflineDialogs.edit_metadata_analysis_id)
        self.edit_series_meta_data.clicked.connect(self.OfflineDialogs.edit_series_meta_data_popup)
        self.append.clicked.connect(self.OfflineDialogs.new_series_creation)
        self.add_meta_data_to_treeview.clicked.connect(self.OfflineDialogs.select_tree_view_meta_data)
        self.compare_series.clicked.connect(partial(self.OfflineDialogs.choose_series, self.selected_series_combo))
        #current_tab.pushButton_3.clicked.connect(self.OfflineDialogs.add_filter_to_offline_analysis)
        
    def show_open_analysis_dialog(self):
        dialog = ChooseExistingAnalysis(self.database_handler, self.frontend_style, self.open_analysis_results)
        
    @Slot()
    def open_analysis_results(self, dialog):
        """
        Open an existing analysis from the database
        :return:
        """
        id_ = dialog.offline_analysis_id # change this to a new name
        dialog.close()

        self.load_treeview_from_database()
        
        #loading_dialog = LoadingDialog(self.wait_widget, self.frontend_style)
        # static offline analysis number
        self.database_handler.analysis_id = int(id_)
        series_names_list = self.database_handler.get_analysis_series_names_for_specific_analysis_id()
        print(series_names_list)

        for i in range(len(series_names_list)):
            series_names_list[i] = series_names_list[i][0]
        #    self.result_visualizer.show_results_for_current_analysis(9,name)
        #self.selected_meta_data_list = self.database_handler.retrieve_selected_meta_data_list()
        
        self.offline_tree.built_analysis_specific_tree(series_names_list, 
                                                       self.select_analysis_functions, 
                                                       self.offline_analysis_widgets, 
                                                       self.selected_meta_data_list, 
                                                       reload = True)
        
        #print("displaying to analysis results: ", self.database_handler.analysis_id)
        #print(self.offline_tree.SeriesItems.topLevelItemCount())

        # @todo DZ write the reload of the analyis function grid properly and then choose to display plots only when start analysis button is enabled
        
        for parent_pos, series_n in zip(range(self.offline_tree.SeriesItems.topLevelItemCount()), series_names_list):

            self.offline_tree.offline_tree.SeriesItems.setCurrentItem(self.offline_tree.SeriesItems.topLevelItem(parent_pos).child(0))
            self.offline_tree.offline_analysis_result_tree_item_clicked()

            # should check if an analysis exist if not than skip addition of the treeview elements
            if not self.database_handler.get_series_specific_analysis_functions(series_n):
                continue
            self.finished_result_thread()

        self.offline_analysis_widgets.setCurrentIndex(1)
        self.notebook.setCurrentIndex(3)

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
        """_summary_: Should load the treeview from the analysis

        Args:
            reload (bool, optional): _description_. If this is a reloaded offline analysis or a newly created
        """
        # already initialized in in updated_data_object
        navigation = NavigationToolbar(self.blank_analysis_plot_manager.canvas, None)
        self.plot_home.clicked.connect(navigation.home)
        self.plot_move.clicked.connect(navigation.pan)
        self.plot_zoom.clicked.connect(navigation.zoom)
        self.blank_analysis_plot_manager.canvas.setStyleSheet("background-color: rgba(0,0,0,0);")
        # open a popup to allow experiment label selection by the user
        # the dialog handler has further implementations to handle displayed lists etc
        self.load_data_from_database_dialog = Load_Data_From_Database_Popup_Handler(self.database_handler, self.frontend_style)
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
        self.selected_meta_data_list = []

        for cb in self.load_data_from_database_dialog.checkbox_list:
            if cb.isChecked():
                pos = self.load_data_from_database_dialog.checkbox_list.index(cb)
                self.selected_meta_data_list.append(self.load_data_from_database_dialog.available_labels[pos][0])
        
        # is alread initialized in update_database_handler_object
        #self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)
        self.series_to_csv.clicked.connect(partial(self.blank_analysis_tree_view_manager.write_series_to_csv, self.frontend_style))
        self.blank_analysis_tree_view_manager.selected_meta_data_list = self.selected_meta_data_list

        self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
        self.offline_tree.blank_analysis_tree_view_manager = self.blank_analysis_tree_view_manager
        self.OfflineDialogs.blank_analysis_tree_view_manager = self.blank_analysis_tree_view_manager

        self.treebuild.directory_tree_widget.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(0)
        index =  self.treebuild.selected_tree_view.model().index(0, 0, self.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
        self.treebuild.selected_tree_view.setCurrentIndex(index)
        # Get the rect of the index
        rect = self.treebuild.selected_tree_view.visualRect(index)
        QTest.mouseClick(self.treebuild.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())
        self.stackedWidget.setCurrentIndex(0)
        self.load_data_from_database_dialog.close()
        

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

    """
    def finished_database_loading(self):
        The finish signal which is emitted after after treeview filling and database reading
        

        print("here we finish the database")
        self.database_handler.open_connection()
        for experiment in self.blank_analysis_page_1_tree_manager.not_discard_experiments_stored_in_db:
            self.database_handler.create_mapping_between_experiments_and_analysis_id(experiment)
        print("finished loading")
        # show selected tree_view
    """

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

        # calls the offlinedialogs class to open the metadata editing popup
        self.OfflineDialogs.create_meta_data_template(self.save_meta_data_to_template_and_continue,
                                                      self.make_list)

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
        self.animation_layout.addWidget(QPushButton("Sit tight we are currenly updating the database with your files!"))
        self.notebook.setCurrentIndex(3)
        self.offline_analysis_widgets.setCurrentIndex(0)
        # show animation
        #for i in range(self.canvas_grid_layout.count()): 
        #        self.canvas_grid_layout.itemAt(i).widget().deleteLater()
        
        # create a new treeview manager 
        # isalread initialized in updated_database_object
        #self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild)

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

        data_frame = meta_data_popup.content_model._data
        file_name = f"{self.offline_manager._directory_path}/automatic_template.csv"
        data_frame.to_csv(file_name, index = False)
        """
        self.continue_open_directory(meta_data_popup, tmp_tree_manager.meta_data_option_list,
                                     tmp_tree_manager.get_meta_data_group_assignments())
        """
        m_list = data_frame.values.tolist()
        self.continue_open_directory(meta_data_popup,m_list)


    def start_analysis_offline(self):
        """Starts the analysis of the selected series"""

        print(self.OfflineDialogs.final_series)
        self.offline_tree.built_analysis_specific_tree(self.OfflineDialogs.final_series, 
                                                       self.select_analysis_functions,
                                                       self.offline_analysis_widgets,
                                                       self.selected_meta_data_list)
        
        self.offline_analysis_widgets.setCurrentIndex(1)
        self.OfflineDialogs.final_series = []
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
            self.statistics_list_view.insertItem(last_row, f"{existing_text} vs. ")

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
            QListWidgetItem(f"{existing_text}_{item_text}", self.statistics_list_view)

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
        self.offline_tree.hierachy_stacked_list[parent_stacked].setCurrentIndex(0)

    def view_table_clicked(self, parent_stacked:int):
        """
        specific function to display result tables that are stored within the related plot widget
        @param parent_stacked: position of the stacked widget
        @return:
        """
        self.analysis_stacked.setCurrentIndex(parent_stacked)
        self.offline_tree.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

        result_plot_widget = self.offline_tree.hierachy_stacked_list[parent_stacked].currentWidget()

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
                            new_column_names.append(f"{res[6]}_{res[7]}")
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

        self.offline_tree.hierachy_stacked_list[parent_stacked].insertWidget(2, table_tab_widget)
        self.offline_tree.hierachy_stacked_list[parent_stacked].setCurrentIndex(2)

    @Slot()
    def go_backwards(self):
        """_summary_
        """
        index = self.offline_analysis_widgets.currentIndex()
        if index > 0:
            self.offline_analysis_widgets.setCurrentIndex(index - 1)
            self.fo_forward_button.setEnabled(True)
            if index == 1:
                self.go_back_button.setEnabled(False)


    def go_forwards(self):
        """_summary_
        """
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
        current_tab = self.offline_tree.tab_list[current_index]
        plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]

        # all the analysis setup clicks and cursor bound drag and drops will be handled from the analysis function selection manager
        self.analysis_function_selection_manager = AnalysisFunctionSelectionManager(self.database_handler, plot_widget_manager , current_tab, dialog.selected_analysis_functions, self.frontend_style)

        self.analysis_function_selection_manager.run_analysis_functions.clicked.connect(partial(self.start_offline_analysis_of_single_series,current_tab))

    def start_offline_analysis_of_single_series(self, current_tab):
        '''
        Performs analysis according to the selected criteria.
        Before the analysis starts, the selected criteria will be stored in the database
        :param current_tab:
        :return:
        '''

        self.database_handler.database.close()
        self.worker = Worker(self.run_database_thread, current_tab)
        self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.progress_bar_update_analysis)
        self.threadpool.start(self.worker)
        

    def run_database_thread(self, current_tab,  progress_callback = None):
        """ This function will run the analysis in a separate thread, that is selected
        by the analysis function
        :param current_tab:
        :param progress_callback:
        """

        print("writing analysis to database")
        #current_tab.stackedWidget.setCurrentIndex(1)
        #current_tab.calc_animation_layout.addWidget(self.wait_widget,0,0)

       
        self.database_handler.open_connection()
        #self.analysis_function_selection_manager.database_handler = self.database_handler
        
        self.multiple_interval_analysis = self.analysis_function_selection_manager.write_table_widget_to_database()

        
        #self.analysis_function_selection_manager.database_handler = self.database_handler

        print("finished: ", self.multiple_interval_analysis)

        # self.write_function_grid_values_into_database(current_tab)
        print("executing single series analysis")

        self.offline_manager.execute_single_series_analysis(current_tab.objectName(), progress_callback)
        
        print("finished single series analysis")
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
        

    def finished_result_thread(self, write_data = True):
        """
        Once all the reuslt have been calculated, an offline tab is created.
        This tab visualizes all calculated results.
        Therefore, a new plot child is inserted to the related series name analysis.
        Furthermore, a table, a statistics and an advanced analysis child are added for further processing steps
        @return:
        """

        self.database_handler.open_connection()

        try: 
            if not self.multiple_interval_analysis.empty:

                self.finish_multiple_interval_analysis()
                
            else:
                print("postprocessing not needed")
        except AttributeError as e:
            print("No attribute self.multiple_interval_analysis")
            
        self.offline_tree.add_new_analysis_tree_children()

        if self.offline_tree.SeriesItems.currentItem().child(0):
            parent_item = self.offline_tree.SeriesItems.currentItem()
        else:
            parent_item = self.offline_tree.SeriesItems.currentItem().parent()

        print(parent_item.text(0))

        offline_tab = self.result_visualizer.show_results_for_current_analysis(self.database_handler.analysis_id,
                                                                                   parent_item.data(6, Qt.UserRole))

        """add the results at position 1 of the stacked widget ( position 0  is the analysis config ) """
        self.offline_tree.hierachy_stacked_list[parent_item.data(7, Qt.UserRole)].insertWidget(1,offline_tab)
        analysis_function_tuple = self.database_handler.get_series_specific_analysis_functions(self.offline_tree.SeriesItems.currentItem().parent().data(6,Qt.UserRole))
        analysis_function_tuple = tuple(i[1] for i in analysis_function_tuple)
        self.offline_tree.SeriesItems.currentItem().parent().setData(8, Qt.UserRole,analysis_function_tuple)
        """simulate click on  "Plot" children """
        self.offline_tree.SeriesItems.setCurrentItem(parent_item.child(1))

        if write_data:
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
    
