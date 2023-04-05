import os
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import logging
import pandas as pd
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from QT_GUI.OnlineAnalysis.ui_py.online_analysis_designer_object import Ui_Online_Analysis
from Backend.online_analysis_manager import OnlineAnalysisManager
from Backend.treeview_manager import TreeViewManager
from Backend.plot_widget_manager import PlotWidgetManager
from pathlib import Path
from functools import partial
from CustomWidget.Pandas_Table import PandasTable
from QT_GUI.OnlineAnalysis.ui_py.RedundantDialog import RedundantDialog
from DataReader.ABFclass import AbfReader
from Offline_Analysis.error_dialog_class import CustomErrorDialog

import numpy as np

class Online_Analysis(QWidget, Ui_Online_Analysis):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # initialize the OnlineAnalysis Manager
        self.online_analysis_plot_manager = None
        self.online_manager = OnlineAnalysisManager()
        self.online_analysis.setCurrentIndex(0)
        self.online_analysis.setTabPosition(QTabWidget.East)

        # check if video matrix is there, image is there and initialize the video calls
        self.video_mat = None
        self.image = None
        self.video_call = 0  # number of frames went through

        # set the video Graphic Scence
        self.online_video = QGraphicsScene(self)
        self.online_video.addText("Load the Video if recorded from Experiment")
        self.graphicsView.setScene(self.online_video)
        self.online_analysis.setTabEnabled(1, False)
        self.online_analysis.setTabEnabled(2,False)
        ##########
        self.canvas_live_plot = FigureCanvas(Figure(figsize=(5, 3)))
        
        #self.verticalLayout_6.addWidget(self.canvas_live_plot)
        # Connect the buttons, connect the logger
        self.connections_clicked()
        self.logger_connection()
        self.drawing()

        self.database_handler = None
        self.offline_database = None
        self.online_analysis_plot_manager = None
        self.online_analysis_tree_view_manager = None
        self.labbook_table = None
        self.frontend_style = None
        self.data_model_list = None
        self.transferred = False
        self._experiment_name = None

    @property
    def experiment_name(self):
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, value: str):
        if isinstance(value, str):
            self._experiment_name = value
        else:
            self.logger.error(f"Wrong name indicated please use a string ant not {value}")

    def enable_plot_options(self):
        """ switch the tab of the online analysis """
        if self.online_analysis_plot_manager:
            navigation = NavigationToolbar(self.online_analysis_plot_manager.canvas, self)
            self.plot_move.clicked.connect(navigation.pan)
            self.plot_zoom.clicked.connect(navigation.zoom)
            self.plot_home.clicked.connect(navigation.home)

  
    def update_database_handler(self, database_handler, offline_database):
        self.database_handler = database_handler
        self.offline_database = offline_database

    def connections_clicked(self):
        """ connect the buttons to the corresponding functions """
        self.button_select_data_file.clicked.connect(self.open_single_dat_file)
        self.online_analysis.currentChanged.connect(self.online_analysis_tab_changed)
        self.pushButton_2.clicked.connect(self.video_show)
        self.transfer_to_offline_analysis.clicked.connect(self.start_db_transfer)
        self.transfer_into_db_button.clicked.connect(self.transfer_file_and_meta_data_into_db)
        self.show_sweeps_radio.toggled.connect(self.show_sweeps_toggled)

    def logger_connection(self):
        # logger settings
        self.logger = logging.getLogger()  # introduce the logger
        self.logger.setLevel(logging.ERROR)
        #file_handler = logging.FileHandler('../Logs/online_analysis.log')
        #formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        #file_handler.setFormatter(formatter)
        #self.logger.addHandler(file_handler)
        self.logger.debug('Online Analysis Widget Debugger')


    def transfer_file_and_meta_data_into_db(self):
        """ This function is responsible from transfering and in memory database
        to a written local database from duckDB for the offline analysis"""

        table_offline = self.offline_database.database.execute("SHOW TABLES").fetchdf()["name"].values
        table_online = self.database_handler.database.execute("SHOW TABLES").fetchdf()["name"].values
        non_intersected = [i for i in table_online if i not in table_offline]
        intersected = [i for i in table_online if i in table_offline]
        self.add_meta_pgf_data_to_offline(non_intersected, intersected)
 
    def add_meta_pgf_data_to_offline(self, non_intersected, intersected):

        #create the non-intersected tables with a prior step creating the table
        try:
            for table, data in zip(["global_meta_data", "experiment_series"], self.data_model_list):
                self.offline_database.database.append(f"{table}",data._data)
        except Exception as e:
            CustomErrorDialog("Something is wrong with duplication", self.frontend_style)
            return None
        
        for tab in non_intersected:
            if tab != "df_1":
                table_df = self.database_handler.database.execute(f"Select * from {tab}").fetchdf()
                self.offline_database.database.execute(f"CREATE TABLE {tab} as SELECT * FROM table_df;")
        # append the intersected table that are same without creating
        for tab in intersected:
            if tab not in ["offline_analysis", "global_meta_data", "experiment_series"]:
                table = self.database_handler.database.execute(f"Select * from {tab}").fetchdf()
                self.offline_database.database.append(f"{tab}", table)
        
        
        self.logger.info("Successfully transferred all the data to the OfflineAnalysis")
        CustomErrorDialog("Successfully transferred all Data to the Online Analysis",self.frontend_style)

    def start_db_transfer(self):
        """
        transfer the experiment (must only be one) into the database
        """
        self.online_analysis.setCurrentIndex(2)

        self.data_model_list = []
        # display and update global_meta_data and experiment_series table
        for table in ["global_meta_data", "experiment_series"]:

            if table == "global_meta_data":
                q = "select * from global_meta_data"
                df = self.database_handler.database.execute(q).fetchdf()
                template_table_view = self.experiment_treeview
            else:
                q = "select * from experiment_series"
                df = self.database_handler.database.execute(q).fetchdf()
                template_table_view = self.series_treeview

            content_model = PandasTable(df)
            self.data_model_list.append(content_model)
            template_table_view.setModel(content_model)
            content_model.resize_header(template_table_view)

            template_table_view.show()


    @Slot()
    def online_analysis_tab_changed(self):
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        #if self.online_analysis.currentIndex() == 0:
        #    self.gridLayout_18.addWidget(self.online_treeview)
        if self.online_analysis.currentIndex() == 2:
            self.start_db_transfer()

    def show_sweeps_toggled(self):
        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)

    def open_single_dat_file(self, file_name=None):
        """ open a single experiment file (.abf or .dat), write it into the database and create a tree view from this
        recording. Since this is online analysis, the experiment is labeled "OFFLINE_ANALYSIS" in the experiment_label
        column in the global meta data table. If the file was not "transfered" to the database, the user will be asked
        to do an action when a new online analysis file will be loaded "
        """

        # open selection and retake users file selection
        self.online_analysis.setCurrentIndex(0)
        #self.online_analysis_tabs.setCurrentIndex(0)

        if file_name is False:
            #file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.dat")[0]
            #file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.abf")[0]
            file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "")[0]

            treeview_name = file_name.split("/")
            treeview_name = treeview_name[len(treeview_name) - 1].split(".")[0]
        else:
            treeview_name = file_name

        # save the path in the manager class
        self.online_manager._dat_file_name = file_name
        # check if this file is already within the database. if yes, the file name will be renamed copy-
        q = f'select * from experiments where experiment_name = \'{treeview_name}\''
        df = self.offline_database.database.execute(q).fetchdf()
        
        self.logger.info("This is the current name of the file: {treeview_name}")
        if not df.empty:
            self.logger.info("file already exists within the offline analysis database, Start redundancy check")
            redundant = RedundantDialog(self.offline_database)
            self.frontend_style.set_pop_up_dialog_style_sheet(redundant)
            redundant.exec_()
            treeview_name = redundant.lineEdit.text() + treeview_name

        self.experiment_name = treeview_name
        self.show_single_file_in_treeview(file_name, treeview_name)

    def transfer_experiment_from_previous_online_analysis(self,dialog):
        dialog.close()
        self.start_db_transfer()

    def show_single_file_in_treeview(self, file_name, treeview_name):
        """
        load the new file into the database and create a treeview from it
        """
        # create treeview of this .dat file
        if self.online_analysis_tree_view_manager is None:
            self.online_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.online_treeview)

        # connect with a new plot manager to handle item clicks within the treeview
        if self.online_analysis_plot_manager is None:
            self.online_analysis_plot_manager = PlotWidgetManager(self.plot_layout, self.database_handler, None,
                                                         False, self.frontend_style)

        # give the experiment (name provided by treeview_name) the experiment_label ONLINE_ANALYSIS to be identified
        self.online_analysis_tree_view_manager.meta_data_assignment_list = [
            ['Experiment_name', 'Experiment_label', 'Species', 'Genotype', 'Sex', 'Condition', 'Individuum_id'],
            [treeview_name, 'None', 'None', 'None', 'None', 'None', 'None', 'None']]

        self.online_analysis_tree_view_manager.meta_data_assigned_experiment_names = ['Experiment_name', treeview_name]

        # file type identification
        file_type = file_name.split(".")
        file_type = file_type[1]

        # if .dat file: run dat file specific bundle reading and insertion into db
        if file_type =="dat":
            #print("found dat file")
            bundle = self.online_analysis_tree_view_manager.open_bundle_of_file(file_name)
            pgf_data_frame = self.online_analysis_tree_view_manager.read_series_specific_pgf_trace_into_df([], bundle, [], None,
                                                                                                  None, None)
            # write this file into the database
            self.online_analysis_tree_view_manager.single_file_into_db([], bundle, treeview_name, self.database_handler,
                                                              [0, -1, 0, 0], pgf_data_frame)

        # if .abf file: run abf file specific bundle creation and insertion into db
        elif file_type == "abf":

            # read only files that have the same idenfier as the selected one
            abf_identifier = os.path.basename(file_name).split("_")
            abf_identifier = abf_identifier[0]
            abf_file_list = os.listdir(os.path.dirname(file_name))

            abf_file_data = []
            for abf in abf_file_list: 

                if abf_identifier in abf:
                    abf_file = os.path.dirname(file_name) + "/" + abf
                    abf_file = AbfReader(abf_file)
                    data_file = abf_file.get_data_table()
                    meta_data = abf_file.get_metadata_table()
                    pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                    experiment_name = [abf_file.get_experiment_name(),'None', 'None', 'None', 'None', 'None', 'None', 'None']
                    series_name = abf_file.get_series_name()
                    abf_file_data.append((data_file, meta_data, pgf_tuple_data_frame, series_name, ".abf"))
            
            if abf_file_data:
                bundle = [abf_file_data, experiment_name]
                self.online_analysis_tree_view_manager.single_abf_file_into_db(bundle, self.database_handler)
        else:
            #  an error dialog shown to the user
            dialog = QDialog()
            dialog_grid = QGridLayout()
            error_message = QLabel("The selected file type is not supported. Supported file types are .dat files and .abf files")
            dialog_grid.addWidget(error_message)
            dialog.setLayout(dialog_grid)
            dialog.exec()
            print("this file type is not supported yet")
            return
        

        # add the option to also display sweep level for each series
        self.online_analysis_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio
        # only display the one file with experiment_label online analysis.
        self.online_analysis_tree_view_manager.selected_meta_data_list = ["None"]
        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)
        self.logger.info("Finished the loading of the file!")
        self.online_analysis.setTabEnabled(1,True)
        self.online_analysis.setTabEnabled(2,True)
        self.online_analysis_tree_view_manager.click_top_level()
        self.enable_plot_options()
        self.get_columns_data_to_table()

    def video_show(self):
        """ show the video in the graphics view
        Generate the Qtimer for the function"""
        if self.video_mat is not None:
            self.start_video = QTimer()  # create a timer
            self.start_video.timeout.connect(self.run_video)  # connect the timer to the start camera function
            self.start_video.start(250)

    def run_video(self):
        """Should play the recorded video/gif in the labbook
        """
        self.video_call += 1 
        item = self.video_mat[self.video_call]
        self.online_video.clear()  # clear the scene
        self.online_video.addPixmap(item)
        print(self.video_call, len(self.video_mat))
        if len(self.video_mat) - 1 == self.video_call:
            self.start_video.stop()
            self.video_call = 0

    def get_columns_data_to_table(self):
        """ This retrieves information from the recording which can 
        be used in a Labbook like table.
        In addition a comment section is added where comments to specific experimental conditions 
        can be made"""
        final_pandas = self.online_treeview.selected_tree_view.model()._data
        final_pandas = final_pandas.drop(columns = ["identifier", "level","parent"]).iloc[1:, :]
        list_cslow = [] # need to change this to support more metadata
        list_rs = [] # need to change also
        for i in final_pandas["item_name"].values:
            cslow, rs = self.retrieve_cslow_rs(i)
            list_cslow.append(cslow)
            list_rs.append(rs)
        final_pandas["condition"] = final_pandas.shape[0] * [""]
        final_pandas["RsValue"] = list_rs
        final_pandas["Cslow"] = list_cslow
        final_pandas["comments"] = final_pandas.shape[0] * [""]
        final_pandas["ids"] = final_pandas.shape[0] * [""]
        self.draw_table(final_pandas)

    def retrieve_cslow_rs(self, series_name):
        """this returns the searchable metadata parameter that one wants to add to the notebook
        This function should be added to the database reader"""
        table_name = self.database_handler.database.execute("Select series_identifier FROM experiment_series WHERE experiment_name = (?) AND series_name = (?)", (self.experiment_name, series_name)).fetchall()[0][0]
        series_meta_table = self.database_handler.database.execute(f"Select * from imon_meta_data_{self.experiment_name}_{table_name}").fetchdf()
        series_meta = series_meta_table.set_index("Parameter").T
        return np.mean(series_meta["CSlow"].astype(float).values), np.mean(series_meta["RsValue"].astype(float).values)

    def draw_table(self, data):
        """ draws the table of the .dat metadata as indicated by the .pul Bundle file """
        try:
            if self.labbook_table is None:
                self.labbook_table = QTableView()
                self.table_layout.addWidget(self.labbook_table)

            labbook_model = PandasTable(data)
            self.labbook_table.setModel(labbook_model)
            self.tableView.setModel(labbook_model)
            labbook_model.resize_header(self.labbook_table)
            labbook_model.resize_header(self.tableView)

            self.labbook_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            print(e)

    def draw_live_plot(self,data_x = None):
        """ this is necessary to draw the plot which is plotted to the self.configuration window
        this will further projected to the online-anaysis """
        print(data_x)
        # print(data_x[0], print(data_x[1]))
        self.canvas_live_plot.figure.clf()

        self.drawing()
        self.ax1.plot(data_x[0], data_x[1], c = "k")
        # self.pyqt_graph.setData(data_x[0], data_x[1])
        print("try to give an updated view of the data")

        print("no error occured here but also not drawn")
        self.canvas_live_plot.draw_idle()

    def drawing(self):
        """ redraws the graph into online analysis """

        self.ax1 = self.canvas_live_plot.figure.subplots()
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)

        # @todo can we get the y unit here ???
        """      
        if self.y_unit == "V":
            self.ax1.set_ylabel('Voltage [mV]')
            self.ax2.set_ylabel('Current [pA]')
        else:
            self.ax1.set_ylabel('Current [nA]')
            self.ax2.set_ylabel('Voltage [mV]')
        """
        # self.canvas_live_plot.draw()
        print("initialized")

    def draw_scene(self, image):

        """ draws the image into the self.configuration window

        args:
            image type: QImage: the image to be drawn
        returns:
            None

        """
        self.online_scence = QGraphicsScene(self)
        self.image_experiment.setScene(self.online_scence)  # set the scene to the image
        item = QGraphicsPixmapItem(image)
        self.image_experiment.scene().addItem(item)  #
