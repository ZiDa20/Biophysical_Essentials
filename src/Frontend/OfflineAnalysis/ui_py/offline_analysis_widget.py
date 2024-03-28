
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtTest import QTest
import numpy as np
import csv
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from functools import partial
import picologging
import debugpy
import os
from Backend.OfflineAnalysis.offline_analysis_manager import OfflineManager
from Backend.OfflineAnalysis.ResultHandler.offline_analysis_result_visualizer import OfflineAnalysisResultVisualizer
from Backend.OfflineAnalysis.offline_analysis_manager import OfflineManager
from Backend.OfflineAnalysis.ResultHandler.offline_analysis_result_table_model import OfflineAnalysisResultTableModel
from Backend.OfflineAnalysis.ResultHandler.FinalResultHolder import ResultHolder
from Backend.ExperimentTree.treeview_manager import TreeViewManager
from Backend.PlotHandler.plot_widget_manager import PlotWidgetManager
from Backend.Threading.Worker import Worker
from Backend.tokenmanager import InputDataTypes
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from database.DatabaseAdapter.PostSql_Handler import PostSqlHandler

from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from Frontend.OfflineAnalysis.CustomWidget.load_data_from_database_popup_handler import Load_Data_From_Database_Popup_Handler
from Frontend.OfflineAnalysis.CustomWidget.drag_and_drop_list_view import DragAndDropListView
from Frontend.OfflineAnalysis.CustomWidget.select_analysis_functions_handler import Select_Analysis_Functions
from Frontend.OfflineAnalysis.CustomWidget.load_previous_discarded_flags_handler import LoadPreviousDiscardedFlagsHandler
from Frontend.OfflineAnalysis.CustomWidget.choose_existing_analysis_handler import ChooseExistingAnalysis
from Frontend.OfflineAnalysis.CustomWidget.statistics_function_table_handler import StatisticsTablePromoted
from Frontend.OfflineAnalysis.CustomWidget.select_statistics_meta_data_handler import StatisticsMetaData_Handler
from Frontend.OfflineAnalysis.ui_py.offline_analysis_designer_object import Ui_Offline_Analysis
from Frontend.OfflineAnalysis.ui_py.SeriesItemTreeManager import SeriesItemTreeWidget
from Frontend.OfflineAnalysis.ui_py.OfflineDialogs import OfflineDialogs
from Frontend.OfflineAnalysis.ui_py.analysis_function_selection_manager import AnalysisFunctionSelectionManager
from Frontend.OfflineAnalysis.CustomWidget.filter_pop_up_handler import Filter_Settings
from Frontend.OfflineAnalysis.CustomWidget.change_series_name_handler import ChangeSeriesName
from Frontend.OfflineAnalysis.CustomWidget.second_layer_analysis_handler import Second_Layor_Analysis_Functions
from Frontend.OfflineAnalysis.CustomWidget.construction_side_handler import ConstrcutionSideDialog   
from StyleFrontend.animated_ap import LoadingAnimation

class Offline_Analysis(QWidget, Ui_Offline_Analysis):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.added_stacked_layout = QGridLayout()
        self.added_stacked_layout.setContentsMargins(0, 0, 0, 0)
        self.add_stacked_widget = QWidget()
        self.add_stacked_widget.setLayout(self.added_stacked_layout)
        # make he ribbon bar components to attach at the same height
        # self.gridLayout_32.setContentsMargins(3, -1, 10, 0.9)
        
       
        self.status_label = None
        self.loaded_function_run: bool = False
        self.threadpool = QThreadPool()
        # style object of class type Frontend_Style that will be int
        # produced and set by start.py and shared between all subclasses
        self.frontend_style = None
        self.database_handler = None
        self.object_splitter = None
        self.final_result_holder = ResultHolder()
        self.offline_manager = OfflineManager()
        self.selected_series_combo.view().setFixedWidth(100)
     
        self.offline_analysis_widgets.setCurrentIndex(0)
        self.offline_analysis_widgets.currentChanged.connect(self.ribbon_bar_handler)        # might be set during blank analysis
        self.blank_analysis_page_1_tree_manager = None
        self.blank_analysis_plot_manager = None
        self.ap = None 
        self.input_data_type = None
        self.parent_count = 0
        #self.offline_tree.current_tab_visualization = self.offline_tree.current_tab_visualization
        #self.offline_tree.current_tab_tree_view_manager = self.offline_tree.current_tab_tree_view_manager

        self.tree_widget_index_count = 0  # save the current maximal index of the tree
        # animation of the side dataframe
        self.notebook = None # variable for hodling the main stacked widget describing the program
        #self.blank_analysis_button.clicked.connect(self.start_blank_analysis)
        # blank analysis menu
        #self.select_directory_button.clicked.connect(self.open_directory)
        #self.load_from_database.clicked.connect(self.load_treeview_from_database)

        # open a dialog to select discarded flag experiments and series from previous analysis 
        self.load_selected_discarded.clicked.connect(self.load_discarded_selected_from_database)
        # forward and backward button
        self.go_back_button.clicked.connect(self.go_backwards)
        self.fo_forward_button.clicked.connect(self.go_forwards)
        #self.load_meta_data.clicked.connect(self.load_and_assign_meta_data)
        self.start_analysis.clicked.connect(self.start_analysis_offline)
        
        self.show_sweeps_radio.toggled.connect(self.update_gui_treeviews)
        # this should be transfer to the plot manager
        # and called with the connected elements

        self.add_filter_button.clicked.connect(self.open_filter_dialog)#
        self.make_screenshot.clicked.connect(self.save_data_trace_as_image)
        self.filter_dialog = None

        self.change_series_name.clicked.connect(self.open_change_series_name_dialog)
        self.clear.clicked.connect(self.clear_meta_data)
        self.turn_off_grid.clicked.connect(partial(self.grid_button_clicked, True))
        self.show_pgf_trace.clicked.connect(partial( self.grid_button_clicked, False))
        self.show_in_3d.clicked.connect(partial(self.show_in_3d_clicked))

        self.logger = picologging.getLogger(__name__)
        self.logger.info("init finished")

        self.advanced_analysis.clicked.connect(self.show_second_layor_analysis)
        self.configure_report_button.clicked.connect(self.show_constructions_side_dialog)
        self.create_report_button.clicked.connect(self.show_constructions_side_dialog)

    def show_constructions_side_dialog(self):
        ConstrcutionSideDialog(self.frontend_style)

    def show_second_layor_analysis(self):
        """_summary_: This function opens the second layer analysis dialog which handles all the user input itself
        """
        d = Second_Layor_Analysis_Functions(self.database_handler,self.result_visualizer,self.frontend_style)
        self.frontend_style.set_pop_up_dialog_style_sheet(d)
        d.exec()
    

    def get_current_tm_pm(self):
        """
        get_current_tm_pm 
        """
        if self.offline_analysis_widgets.currentIndex() == 0:
            tm = self.blank_analysis_tree_view_manager # ptm = tree manager
            pm = self.blank_analysis_plot_manager # pm = plot manager
        else:
            #have to find the corect widget first
            c = self.offline_analysis_widgets.currentIndex()
            current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
            tm = self.offline_tree.current_tab_tree_view_manager[current_index]
            pm = self.offline_tree.current_tab_visualization[current_index]
        return tm, pm

    def grid_button_clicked(self, grid:bool):
        """either show or turn off the grid in the plot or show or turn off the pgf plot
        """
        tm,pm = self.get_current_tm_pm()

        if grid: # grid button was clicked
            pm.show_plot_grid =  not pm.show_plot_grid
        else: # pgf button was clicked
            if pm.make_3d_plot:
                CustomErrorDialog(f'Please deactivate the 3D feature to view the PGF plot',self.frontend_style)
                return
            else:
                pm.show_pgf_plot = not pm.show_pgf_plot 

        self.reclick_tree_item(tm)

    def show_in_3d_clicked(self):
        """
        show_in_3d_clicked: switch the current plot to 3d view
        3d view will only show recording data without pgf, otherwise its too crowded
        """
        tm,pm = self.get_current_tm_pm()

        pm.make_3d_plot = not pm.make_3d_plot
        if pm.make_3d_plot:
            pm.show_pgf_plot = False
        else:
            pm.show_pgf_plot = True
        self.reclick_tree_item(tm)

    def reclick_tree_item(self, treeview_manager:TreeViewManager):
            """
            reclick the current tree object to update the plot
            """   
            try:
                index = treeview_manager.tree_build_widget.selected_tree_view.selectedIndexes()[1]
                rect = treeview_manager.tree_build_widget.selected_tree_view.visualRect(index)
            
            except IndexError:
                # if there was some discarding/reinsertion procedire before, it might happen that no treeelement is clicked
                # Find the QModelIndex of the first child of the first parent
                parent_index = treeview_manager.tree_build_widget.selected_tree_view.model().index(0, 0,  QModelIndex())  # Row 0, Column 0
                child_index = treeview_manager.tree_build_widget.selected_tree_view.model().index(0, 0, parent_index)  # Row 0, Column 0, under parent_index
                rect = treeview_manager.tree_build_widget.selected_tree_view.visualRect(child_index)
            
            # on click (handled in treeview manager) plot compartments will be evaluated
            QTest.mouseClick(treeview_manager.tree_build_widget.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())
    
    def clear_meta_data(self):
        """clear the meta data from the database"""
        self.database_handler.database.execute(f"DELETE FROM selected_meta_data WHERE offline_analysis_id = {self.database_handler.analysis_id} AND analysis_function_id = -1")    
        self.update_gui_treeviews()

    def load_discarded_selected_from_database(self):
        self.s_d_dialog = LoadPreviousDiscardedFlagsHandler(self.database_handler,self.frontend_style)
        self.s_d_dialog.apply_selection.clicked.connect(partial(self.update_treeview_with_previous_selection,self.s_d_dialog ))

        self.frontend_style.set_pop_up_dialog_style_sheet(self.s_d_dialog )
        self.s_d_dialog.show()

    def update_treeview_with_previous_selection(self,dialog):
        """_summary_

        Args:
            dialog (_type_): _description_
        """
        dialog.close()
        self.update_gui_treeviews()
                                            
    def open_change_series_name_dialog(self):
        """Open the dialog for the user to select one of the existign series names and change it to a custom one
        """

        # dialog needs to be self to be accessible in the unittest
        self.change_series_name_dialog = ChangeSeriesName(self.database_handler)
        self.change_series_name_dialog.apply.clicked.connect(self.update_after_series_change)
        self.frontend_style.set_pop_up_dialog_style_sheet(self.change_series_name_dialog)
        self.change_series_name_dialog.show()

    def update_after_series_change(self):
        """Actually executes the change of the series name 
        Args:
            dialog (_type_): _description_
        """
        self.change_series_name_dialog.excecute_rename()
        self.update_gui_treeviews()
        self.change_series_name_dialog.close()
        self.ap.stop_and_close_animation()
        
    def open_filter_dialog(self):
        """
        open the filter dialog.
        dialog is safed global to be reused for the whole analysis
        """

        #print("add filter button clicked")
        #if self.filter_dialog is None:
            # if none, the dialog is created initially
        if self.offline_analysis_widgets.currentIndex() ==1:
            self.filter_dialog = Filter_Settings(self.frontend_style,self.database_handler,self.offline_tree)
        
        else:
            self.filter_dialog = Filter_Settings(self.frontend_style,self.database_handler,
                                                    self.blank_analysis_tree_view_manager)
        
        self.filter_dialog.apply_filter_button.clicked.connect(partial(self.apply_filter_selection))

        #self.filter_dialog.tabWidget.setCurrentIndex(self.offline_analysis_widgets.currentIndex())
        self.filter_dialog.show()

    def save_data_trace_as_image(self):
        if self.offline_analysis_widgets.currentIndex() ==1:
            current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
            plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]
        else:
            plot_widget_manager = self.blank_analysis_plot_manager
        
        file_filter = "Portable Document Format (*.pdf);;Scalable Vector Graphics (*.svg);;Portable Network Graphics (*.png)"
        result_path = QFileDialog.getSaveFileName(filter=file_filter)[0]
        plot_widget_manager.canvas.print_figure(result_path)
        self.logger.info("Saved plot as image succesfully")


    def apply_filter_selection(self):

        #if self.filter_dialog.DISCARD_DATA:
        # for now, mark all the experiments as discarded
        self.filter_dialog.apply_filters()
        # @todo: double check whether it might be more clever to remove the from offline analysis mapping table
        if self.offline_analysis_widgets.currentIndex() ==1:
            current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
            plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]
            tree_manager = self.offline_tree.current_tab_tree_view_manager[current_index]
            current_tab = self.offline_tree.tab_list[current_index]

            tree_manager.update_treeviews(plot_widget_manager,current_tab.series_name)
        else:
            self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
        self.filter_dialog.close()
        # make a proper rest
        self.filter_dialog = None

    def update_gui_treeviews(self,signal= None, meta=None):
        """toDO add Docstrings!

        Args:
            signal (_type_): _description_
        """
    
        self.ap.make_widget()
        try:
            if self.offline_analysis_widgets.currentIndex()==0:
                
                if meta: 
                    self.OfflineDialogs.select_tree_view_meta_data(self.blank_analysis_tree_view_manager, self.blank_analysis_plot_manager)
                else:
                    self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)

            if self.offline_analysis_widgets.currentIndex() ==1: #@toDO check toggle notebook ind
                current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
                plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]
                current_tree = self.offline_tree.current_tab_tree_view_manager[current_index]
                series_name = self.offline_tree.tab_list[current_index].objectName()
                 
                if meta:
                    self.OfflineDialogs.select_tree_view_meta_data(current_tree, plot_widget_manager,series_name)
                else:
                    current_tree.update_treeviews(plot_widget_manager,series_name)

        except Exception as e:
           print(e)
           CustomErrorDialog("Please select load an Experiment First", self.frontend_style)

        self.ap.stop_and_close_animation()
 
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
         self.object_splitter.addWidget(self.add_stacked_widget)
         self.offline_tree.add_widget_to_splitter(self.added_stacked_layout)


    def update_database_handler_object(self, updated_object, frontend_style, notebook, reconnect = None):
        """_summary_: This function updates the object connections to the offline analysis widget


        Args:
            updated_object (DuckDBHandler): DuckDB Database Handler Class
        """
        self.database_handler = updated_object
        self.frontend_style = frontend_style
        self.notebook = notebook
        self.offline_manager.database = updated_object
        self.final_result_holder.database_handler = updated_object



        if not reconnect:
            self.blank_analysis_plot_manager = PlotWidgetManager(self.canvas_grid_layout, self.database_handler, None, False,  self.frontend_style)
            self.ap = LoadingAnimation("Preparing your data: Please Wait", self.frontend_style)

        else:
            self.blank_analysis_plot_manager.database_handler = self.database_handler
            self.edit_meta.clicked.disconnect()
            self.edit_series_meta_data.clicked.disconnect()
            self.append.clicked.disconnect()
            self.add_meta_data_to_treeview.clicked.disconnect() 
            self.compare_series.clicked.disconnect()
            self.series_to_csv.clicked.disconnect()
            self.experiment_to_csv.clicked.disconnect()

        self.blank_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.treebuild, self.show_sweeps_radio, frontend = self.frontend_style)
        


        self.offline_tree = SeriesItemTreeWidget(self.SeriesItems_2,
                                                 [self.plot_home, self.plot_zoom, self.plot_move],
                                                 self.frontend_style,
                                                 self.database_handler,
                                                 self.offline_manager,
                                                 self.show_sweeps_radio,
                                                 self.blank_analysis_tree_view_manager,
                                                 self.frame)


        self.offline_tree.SeriesItems.clear()
        self.offline_tree.create_top_level_items()

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

        # this handling is important to avoid that we are dealing with the wrong object
        
        
        self.edit_meta.clicked.connect(self.OfflineDialogs.edit_metadata_analysis_id)
        self.edit_series_meta_data.clicked.connect(self.OfflineDialogs.edit_series_meta_data_popup)
        self.append.clicked.connect(self.OfflineDialogs.new_series_creation)
        self.add_meta_data_to_treeview.clicked.connect(partial(self.update_gui_treeviews, None, True)) 
        self.compare_series.clicked.connect(partial(self.OfflineDialogs.choose_series, self.selected_series_combo))
        #current_tab.pushButton_3.clicked.connect(self.OfflineDialogs.add_filter_to_offline_analysis)

        
        # csv files can be written from treeview when this button is clicked. the frontend style is set in update_database_handler function
        self.series_to_csv.clicked.connect(partial(self.blank_analysis_tree_view_manager.write_series_to_csv, self.blank_analysis_plot_manager))   
        self.experiment_to_csv.clicked.connect(self.extract_experiment_to_csv)
    
    def extract_experiment_to_csv(self):
        """write an entire experiment to csv file. therefore have a small animation"""
        self.ap.make_widget()
        self.blank_analysis_tree_view_manager.write_experiment_to_csv(self.blank_analysis_plot_manager)
        self.ap.stop_and_close_animation()
 
    def show_open_analysis_dialog(self):
        d = ChooseExistingAnalysis(self.database_handler, self.frontend_style)
        d.submit.clicked.connect(partial(self.open_analysis_results,d))
        d.exec()
        return d.loaded_function_run

    @Slot()
    def open_analysis_results(self, dialog:ChooseExistingAnalysis):
        """
        Open an existing analysis from the database
        :return:
        """
        

        if self.loaded_function_run:
            self.reset_class(new_analysis = False)
     
        dialog.close()

        self.ap.make_widget()

        # deprecated ? 
        dialog.loaded_function_run = True
        self.loaded_function_run = True

        id_ = dialog.offline_analysis_id # change this to a new name
        #self.logger.info("opening existing analysis from database. requested id = ", id_)
   
 
        # static offline analysis number
        self.database_handler.analysis_id = int(id_)
        self.blank_analysis_tree_view_manager.offline_analysis_id = int(id_)
     
        QApplication.processEvents()
        self.load_page_1_tree_view(id_)
        QApplication.processEvents()
        
        #@todo THREADING
        series_names_list = self.database_handler.get_analysis_series_names_for_specific_analysis_id()
        for i in range(len(series_names_list)):
            QApplication.processEvents()
            series_names_list[i] = series_names_list[i][0]
        
        self.offline_tree.built_analysis_specific_tree(series_names_list,
                                                       self.select_analysis_functions,
                                                       self.offline_analysis_widgets,
                                                       reload = True)
        QApplication.processEvents()
       
        #@todo DZ write the reload of the analyis function grid properly and then choose to display plots only when start analysis button is enabled
        
        for parent_pos, series_n in zip(range(len(series_names_list)), series_names_list):
           
            QApplication.processEvents()
            #bugfix: we always have to load toplevelitem 0 here (max count = 2)
            self.offline_tree.offline_tree.SeriesItems.setCurrentItem(self.offline_tree.SeriesItems.topLevelItem(0).child(parent_pos).child(0))
            self.offline_tree.offline_analysis_result_tree_item_clicked()

            # should check if an analysis exist if not than skip addition of the treeview elements
            if not self.database_handler.get_series_specific_analysis_functions(series_n):
                continue
            self.finished_result_thread(reload=True)
        
        self.ap.stop_and_close_animation()
        self.offline_analysis_widgets.setCurrentIndex(1)
        self.notebook.setCurrentIndex(3)
        
    # outdated ? dz 13.11.2023
    #@Slot()
    #def start_blank_analysis(self):
    #    """starts a blank analysis by changing qstacked tab to blank analysis view ( at index 1) where the user gets
    #    new button interactions offered """
    #    self.offline_analysis_widgets.setCurrentIndex(1)

    # outdated ? dz 13.11.2023
    #@Slot()
    #def go_to_main_page(self):
    #    self.offline_analysis_widgets.setCurrentIndex(1)

    @Slot()
    def load_treeview_from_database(self, test = None):
        """_summary_: Should load the treeview from the analysis

        Args:
            reload (bool, optional): _description_. If this is a reloaded offline analysis or a newly created
        """
        # already initialized in in updated_data_object
        self.ap.make_widget()
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
        self.load_data_from_database_dialog.load_data_2.clicked.connect(self.load_page_1_tree_view)
        

        #self.load_data_from_database_dialog.checkbox_checked(self.load_data_from_database_dialog.all_cb,"All",2)
        self.load_data_from_database_dialog.all_cb.setChecked(True)

        if not test:
            if self.ap: 
                self.ap.stop_and_close_animation()
            self.load_data_from_database_dialog.exec_()

        #self.load_data_from_database_dialog.all_cb.setChecked(True)
        #self.notebook.setCurrentIndex(3)
        return True
    
    
    def load_page_1_tree_view(self, existing_id = None):
        """
        this function will be executed when the button 'load selection' was clicked after 
        data to be analyzed were selected fro mthe db dashboard dialog
        @return:
        """
        # switch to the first page of the offline analysis 
        self.notebook.setCurrentIndex(3)

        # load an exsiting analysis from a given id
        if existing_id:
            q = f'select experiment_name from experiment_analysis_mapping where analysis_id = {existing_id}'
            experiment_list = self.database_handler.database.execute(q).fetchdf()
            experiment_list = experiment_list["experiment_name"].values
            #@bugfix
            #self.logger.info("experiment list found for analysis id ", str(self.database_handler.analysis_id))
              
        else:
            # get the experiment names that were selected by the user within the db dashboard # 
            experiment_list = self.load_data_from_database_dialog.get_experiment_names()   
            self.load_data_from_database_dialog.close()   

            # ! important ! map_data_to_analysis_id() will link the selected data to an unique offline analysis id:
            # from this point, all db searches, discardings and reinsertions are related to the mapping tables with exception of series raw data (trace data, pgf data, meta_data)
            self.blank_analysis_tree_view_manager.map_data_to_analysis_id(experiment_list)
        
        self.blank_analysis_tree_view_manager.update_treeviews(self.blank_analysis_plot_manager)
        self.offline_tree.blank_analysis_tree_view_manager = self.blank_analysis_tree_view_manager
        self.OfflineDialogs.blank_analysis_tree_view_manager = self.blank_analysis_tree_view_manager

        self.treebuild.directory_tree_widget.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(0)

        # click the first row, first column item in the selected treeview of page 1
        index =  self.treebuild.selected_tree_view.model().index(0, 0, self.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
        self.treebuild.selected_tree_view.setCurrentIndex(index)
        # Get the rect of the index
        rect = self.treebuild.selected_tree_view.visualRect(index)
        QTest.mouseClick(self.treebuild.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())
        self.stackedWidget.setCurrentIndex(0)
        
    """ deprecated ? dz 06092023
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
    """

    @Slot()
    def open_directory(self,data_type:InputDataTypes):
        '''Opens a filedialog where a user can select a desired directory. After the selection, a dialog will open and ask
        the user to enter meta data groups. The popup will be closed after the user clicked the concerning button.
        The function will be continued in function continue_open_directory

        test_path = is for testing_purposes of the function
        '''
        # set the data type here for later use in continue open directory
        # this is to avoid handing it over from one function to another without using it
        self.input_data_type = data_type

        if dir_path := QFileDialog.getExistingDirectory():
            #self.select_directory_button.setText("Change")

            # save the path in the manager class
            # calls the offlinedialogs class to open the metadata editing popup
            self.offline_manager._directory_path = dir_path
            
            #make the file check here: make sure HEKA is bundled, .dat files are read as heka and .abf files are read as abf
            match data_type:
                case InputDataTypes.BUNDLED_HEKA_DATA: 
                    data_list = os.listdir(dir_path)
                    dat_list = [i for i in data_list if ".dat" in i]
                    dat_bundle = self.blank_analysis_tree_view_manager.qthread_heka_unbundled_reading(dat_list,dir_path,None)[0]
                    for b in dat_bundle:
                        if b[0].pul == None:
                            CustomErrorDialog("Unbundled HEKA data detected ! \n Unbundled HEKA data are outdated and currently not supported. \n However, Patchmaster allows to convert the old data format into the new bundled file format. \n On our Website we show you how to convert the data. Please have a look at https://biophysical-essentials.i-med.ac.at/bpe_doku", self.frontend_style)
                            return
                case InputDataTypes.ABF_DATA:
                    experiment_names = [i.split(".")[0] for i in dat_list]
                    abf_list = [i for i in data_list if ".abf" in i]
            
            self.OfflineDialogs.create_meta_data_template(self.save_meta_data_to_template_and_continue,
                                                        self.make_list)
            


    def continue_open_directory(self, meta_data_group_assignment_list=None, test = None):
        '''
        Function will continue the function open directory after any continue button in the meta data group dialog has
        been clicked. At first the popup will be closed, all data will be loaded immediately into the databse
        :param pop_up_dialog:
        :param meta_data_group_assignment_list: list of tuples of experiment name and assigned meta data group
        :return:
        '''


        self.ap.make_widget() # shows the AP Animation Waiting Dialog
        self.offline_analysis_widgets.setCurrentIndex(0)

        # read the directory data into the database
        self.offline_manager.ap = self.ap

        self.blank_analysis_tree_view_manager = self.offline_manager.read_data_from_experiment_directory(self.ap,self.input_data_type,
                                                                                           self.blank_analysis_tree_view_manager, 
                                                                                           meta_data_group_assignment_list)
        
        
        # assign meta data
        if not meta_data_group_assignment_list:
            meta_data_group_assignment_list = []

        else:
            for n in meta_data_group_assignment_list:
                print("adding meta data to existing experiment ", n)
                self.database_handler.add_meta_data_group_to_existing_experiment(n)
                #self.database_handler.global_meta_data_table.add_meta_data_group_to_existing_experiment(n)

        #self.add_filter_button.setEnabled(True)
        self.blank_analysis_tree_view_manager.data_read_finished.finished_signal.connect(partial(self.load_treeview_from_database, test))
        #ap.stop_and_close_animation()

    def make_list(self,popup,treeview_model):
        m_list = treeview_model.model()._data.values.tolist()
        popup.close()
        self.blank_analysis_tree_view_manager.experiment_name_mapping=popup.experiment_name_dict
        self.continue_open_directory(m_list)

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
        self.logger.info(f"Series to be analyzed: {self.OfflineDialogs.series_dialog.final_series}")
        
        self.offline_tree.built_analysis_specific_tree(self.OfflineDialogs.series_dialog.final_series,
                                                       self.select_analysis_functions,
                                                       self.offline_analysis_widgets)
        
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
        self.worker.signals.progress.connect(self.ap.progress_bar_update_analysis)
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
    def select_analysis_functions(self):
        """ open a popup dialog for the user to select available analysis functions """

        # 1) create dialog
        current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
        current_tab = self.offline_tree.tab_list[current_index]

        dialog = Select_Analysis_Functions(self.database_handler,current_tab.series_name)
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

        current_tab_tree_view_manager = self.offline_tree.current_tab_tree_view_manager[current_index]
        plot_widget_manager  = self.offline_tree.current_tab_visualization[current_index]
        self.analysis_function_selection_manager = AnalysisFunctionSelectionManager(self.database_handler, current_tab_tree_view_manager, plot_widget_manager , current_tab, dialog.selected_analysis_functions, self.frontend_style)

        # this needs to be performed to ensure only one connection nper analysis
        try:
            self.run_analysis_functions.clicked.disconnect()#
        except Exception as e:
            self.logger.info("No connection to disconnect here, probably the first connect")
            
        self.run_analysis_functions.clicked.connect(partial(self.start_offline_analysis_of_single_series,current_tab))

        # set the size of the table
        w = self.analysis_function_selection_manager.widget_with + 50
        current_tab.analysis_functions.groupBox.setMinimumSize(w, 0)
        current_tab.analysis_functions.groupBox.show()
        current_tab.show_and_tile()
        # click the resize button of the data view !!!!!
        #QTest.mouseClick(current_tab.tile_button, Qt.LeftButton)

    def start_offline_analysis_of_single_series(self, current_tab):
        '''
        Performs analysis according to the selected analysis functions, cursor bounds, pgf segment and normalization method.
        Before the analysis starts, the selected criteria will be stored in the database
        :param current_tab:
        :return:
        '''

        self.database_handler.database.close()
        self.ap.make_widget()
        self.worker = Worker(self.run_database_thread, current_tab)
        self.worker.signals.finished.connect(self.finished_result_thread)
        self.worker.signals.progress.connect(self.ap.progress_bar_update_analysis)
        self.threadpool.start(self.worker)


    def run_database_thread(self, current_tab,  progress_callback = None):
        """ This function will run the analysis in a separate thread, that is selected
        by the analysis function
        :param current_tab:
        :param progress_callback:
        """

        
        self.database_handler.open_connection()
        self.multiple_interval_analysis = self.analysis_function_selection_manager.write_table_widget_to_database()
        self.logger.info(f"finished: {self.multiple_interval_analysis}")
        self.logger.info(f"executing single series analysis: {current_tab.objectName()}")
        self.offline_manager.execute_single_series_analysis(current_tab.objectName(), progress_callback)

        self.logger.info(f"Finished the Series {current_tab.objectName()}")
        self.database_handler.database.close()

        # Process events to allow the update
        #@todo remove the widget from the layout in case of rerun 
        current_tab.stackedWidget.setCurrentIndex(0)


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


    def finished_result_thread(self, write_data = True, reload=False):
        """
        Once all the reuslt have been calculated, an offline tab is created.
        This tab visualizes all calculated results.
        Therefore, a new plot child is inserted to the related series name analysis.
        Furthermore, a table, a  statistics and an advanced analysis child are added for further processing steps
        @return:
        """
        if not reload:
            self.ap.stop_and_close_animation()

        try:
            #@todo fallback to make sure its always closed, otherwise open connection might fail
            self.database_handler.database.close()
        except Exception as e:
            pass

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

        self.logger.info(parent_item.text(0))

        try:
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
        except Exception as e:
            self.logger.error(f'finished_result_thread: occured while creating the offline tab: {e}')
            CustomErrorDialog(f'Error occured while creating the offline tab: {e}',self.frontend_style)
            

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
            equation_components = related_intervals["func"].values[0].split(" ")
            
            try:
                equation_components.remove("")
            except Exception as e:
                print(e)
                

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
            print("starting the recursive function")
            print(equation_components)
            self.recursive_pop(equation_components,0, 0)

            # if everything worked correctly, only the first func to remove should still exist in the analysis functions table
            # the name here needs to be adapted too

            print("finished recursive function")

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
            print(tbl_1, tbl_2)
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
                table_name = tbl_1 #"results_analysis_function_"+str(func_1)+"_"+  #str(data_1["Sweep_Table_Name"].values[0])

                self.database_handler.database.register(table_name, data_1)
                self.database_handler.database.execute(f'CREATE TABLE {table_name} AS SELECT * FROM {table_name}')

        # delete the id from the analysis functions table
        self.database_handler.database.execute(f'delete from analysis_functions where analysis_function_id == {func_2}')

        if equation_components == []:
            print("my job is done")
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


    def ribbon_bar_handler(self):
        """Handler for the last two fields of the ribbon bar. Specific functions for each analysis step are provided.
        """

        # current index can be either 0 (blank start), 1 (selectded sereis to be analyzed) and 2 (results panel)
        current_index = self.offline_analysis_widgets.currentIndex()
        # update the stacked widget to show the correct button
        self.ribbon_analysis.setCurrentIndex(current_index)
        self.ribbon_series_normalization.setCurrentIndex(current_index)


    def reset_class(self, new_analysis = True, path_to_database = None):
        """resets the class to its orignal point and adds a new 
        offline analysis id"""
        #reset the complete offline_stages
        # reset the objects interacting with the offline_widget_class
        #reset the variables to the default value
     
        if new_analysis: 
            self.database_handler.database.close()
            self.database_handler = DuckDBDatabaseHandler(self.frontend_style, database_path = path_to_database)
        self.blank_analysis_tree_view_manager.clear_tree()
        self.blank_analysis_plot_manager.canvas.figure.clf()
        self.blank_analysis_plot_manager.canvas.draw_idle()
        self.tree_widget_index_count = 0
        self.filter_dialog = None
        self.final_result_holder = ResultHolder()
        self.offline_manager = OfflineManager()
        try: # important if initial loading did not wo  rk out properly
            self.offline_tree.hierachy_stacked.deleteLater()
            self.offline_tree.analysis_stacked.deleteLater()
        except AttributeError:
            self.logger.info("No hierachy widget yet defined")
    
        self.update_database_handler_object(self.database_handler, self.frontend_style, self.notebook, reconnect = True)
        self.add_splitter()
        self.loaded_function_run = True
        
      

    
        



