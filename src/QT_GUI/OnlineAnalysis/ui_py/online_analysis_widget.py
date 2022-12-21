from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import logging
import pandas as pd
from Pandas_Table import *
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

from QT_GUI.OnlineAnalysis.ui_py.online_analysis_designer_object import Ui_Online_Analysis
from online_analysis_manager import OnlineAnalysisManager
from treeview_manager import TreeViewManager
from plot_widget_manager import PlotWidgetManager
from pathlib import Path
from functools import partial


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

        ##########
        self.canvas_live_plot = FigureCanvas(Figure(figsize=(5, 3)))
        self.online_analysis_tabs.currentChanged.connect(self.tab_switched)

        self.verticalLayout_6.addWidget(self.canvas_live_plot)
        # Connect the buttons, connect the logger
        self.connections_clicked()
        self.logger_connection()
        self.drawing()

        self.database_handler = None

    def tab_switched(self, i):
        """ switch the tab of the online analysis """
        if i == 0:
            if self.online_analysis_plot_manager:
                navigation = NavigationToolbar(self.online_analysis_plot_manager.canvas, self)
                self.plot_move.clicked.connect(navigation.pan)
                self.plot_zoom.clicked.connect(navigation.zoom)
                self.plot_home.clicked.connect(navigation.home)

            else:
                print("No Canvas yet")
        else:
            if i == 1:
                navigation = NavigationToolbar(self.canvas_live_plot, self)
                self.plot_move.clicked.connect(navigation.pan)
                self.plot_zoom.clicked.connect(navigation.zoom)
                self.plot_home.clicked.connect(navigation.home)
            else:
                print("Canvas not established yet!")

    def update_database_handler(self, database_handler):
        self.database_handler = database_handler

    def connections_clicked(self):
        """ connect the buttons to the corresponding functions """
        self.button_select_data_file.clicked.connect(self.open_single_dat_file)
        self.online_analysis.currentChanged.connect(self.online_analysis_tab_changed)
        self.pushButton_2.clicked.connect(self.video_show)
        self.transfer_to_offline_analysis.clicked.connect(self.start_db_transfer)

    def logger_connection(self):
        # logger settings
        self.logger = logging.getLogger()  # introduce the logger
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler('../Logs/online_analysis.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.debug('Online Analysis Widget Debugger')

    def start_db_transfer(self):

        file_path = self.online_manager._dat_file_name
        bundle = TreeViewManager().open_bundle_of_file(file_path)
        pgf_data = TreeViewManager().read_series_specific_pgf_trace_into_df([], bundle, [], None, None,
                                                                            None)  # retrieve pgf data

        file_name = Path(file_path).name
        file_name = file_name.split(".")
        file_name = file_name[0]

        TreeViewManager().single_file_into_db([], bundle, file_name, self.database_handler, [0, -1, 0, 0], pgf_data)

        print("Successfull import")

    @Slot()
    def online_analysis_tab_changed(self):
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        if self.online_analysis.currentIndex() == 0:
            self.tree_layouting_change.addWidget(self.tree_tab_widget)
        else:
            self.verticalLayout.addWidget(self.tree_tab_widget)

    def open_single_dat_file(self, file_name=None):
        """ open a single experiment file (.abf or .dat), write it into the database and create a tree view from this
        recording. Since this is online analysis, the experiment is labeled "OFFLINE_ANALYSIS" in the experiment_label
        column in the global meta data table. If the file was not "transfered" to the database, the user will be asked
        to do an action when a new online analysis file will be loaded "
        """

        # open selection and retake users file selection

        if file_name is False:
            file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.dat")[0]
            treeview_name = file_name.split("/")
            treeview_name = treeview_name[len(treeview_name) - 1].split(".")[0]
        else:
            treeview_name = file_name

        print("treeview_name", treeview_name)

        # save the path in the manager class
        self.online_manager._dat_file_name = file_name

        # check for old online analysis and let the user decide whether to import to the database or remove it
        q = f'select experiment_name from global_meta_data where experiment_label = \'ONLINE_ANALYSIS\' '
        old_file_df = self.database_handler.database.execute(q).fetchdf()
        print("old_file", old_file_df)

        if old_file_df["experiment_name"].values.tolist() == []:
            self.show_single_file_in_treeview(file_name, treeview_name)
        else:
            dialog = QDialog()
            old_file_name = old_file_df["experiment_name"].values.tolist()[0]
            text = f'You have non-transfered experiments from previous online analysis \n ' \
                   f'experiment name: {old_file_name} \n ' \
                   f'Do you want to transfer it to the database or discard ?'
            dialog_label = QLabel(text)
            transfer_button = QPushButton("Transfer")
            discard_button = QPushButton("Discard")
            discard_button.clicked.connect(partial(self.discard_online_analysis_file, old_file_name,
                                                   treeview_name, file_name, dialog))

            layout = QGridLayout()
            layout.addWidget(dialog_label)
            layout.addWidget(transfer_button)
            layout.addWidget(discard_button)
            dialog.setLayout(layout)
            dialog.exec_()

    def discard_online_analysis_file(self, old_file_name, treeview_name, file_name, dialog):
        """
        remove an experiment by its name and all related entries in global_meta_data, experiments and experiment_series
        tables
        """
        dialog.close()

        # get the experiment series table since this holds 3 more table names that need to be completely deleted
        q = f'select * from experiment_series where experiment_name = \'{old_file_name}\''
        experiment_series = self.database_handler.database.execute(q).fetchdf()
        for column in ["sweep_table_name", "meta_data_table_name", "pgf_data_table_name"]:
            for table in experiment_series[column].values.tolist():
                q = f'drop table {table} '
                self.database_handler.database.execute(q)

        # remove from global_meta_data, experiments, experiment_series
        for table in ["global_meta_data", "experiments", "experiment_series"]:
            q = f'delete from {table} where experiment_name = \'{old_file_name}\''
            self.database_handler.database.execute(q)

        # load the new file into the database and create a treeview from it
        self.show_single_file_in_treeview(file_name, treeview_name)

    def show_single_file_in_treeview(self, file_name, treeview_name):
        """
        load the new file into the database and create a treeview from it
        """
        # create treeview of this .dat file
        online_analysis_tree_view_manager = TreeViewManager(self.database_handler, self.online_treeview)
        bundle = online_analysis_tree_view_manager.open_bundle_of_file(file_name)
        pgf_data_frame = online_analysis_tree_view_manager.read_series_specific_pgf_trace_into_df([], bundle, [], None,
                                                                                                  None, None)

        # give the experiment (name provided by treeview_name) the experiment_label ONLINE_ANALYSIS to be identified
        online_analysis_tree_view_manager.meta_data_assignment_list = [
            ['Experiment_name', 'Experiment_label', 'Species', 'Genotype', 'Sex', 'Condition', 'Individuum_id'],
            [treeview_name, 'ONLINE_ANALYSIS', 'None', 'None', 'None', 'None', 'None']]
        online_analysis_tree_view_manager.meta_data_assigned_experiment_names = ['Experiment_name', treeview_name]

        # write this file into the database
        online_analysis_tree_view_manager.single_file_into_db([], bundle, treeview_name, self.database_handler,
                                                              [0, -1, 0, 0], pgf_data_frame)

        # add the option to also display sweep level for each series
        self.show_sweeps_radio = QRadioButton()
        online_analysis_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio

        # only display the one file with experiment_label online analysis.
        online_analysis_tree_view_manager.selected_meta_data_list = ["ONLINE_ANALYSIS"]

        # connect with a new plot manager to handle item clicks within the treeview
        online_analysis_plot_manager = PlotWidgetManager(self.tree_plot_widget_layout, self.database_handler, None,
                                                         False)
        online_analysis_tree_view_manager.update_treeviews(online_analysis_plot_manager)

    def video_show(self):
        """ show the video in the graphics view 
        Generate the Qtimer for the function"""
        if self.video_mat is not None:
            self.start_video = QTimer()  # create a timer
            self.start_video.timeout.connect(self.run_video)  # connect the timer to the start camera function
            self.start_video.start(250)

    def run_video(self):
        self.video_call += 1
        item = self.video_mat[self.video_call]
        self.online_video.clear()  # clear the scene
        self.online_video.addPixmap(item)
        print(self.video_call, len(self.video_mat))
        if len(self.video_mat) - 1 == self.video_call:
            self.start_video.stop()
            self.video_call = 0

    def get_columns_data_to_table(self):
        # toDO add the documentation here
        count = self.treeWidget.topLevelItemCount()
        list_rows = []
        final_pandas = pd.DataFrame()
        for i in range(count):
            top_item = self.treeWidget.topLevelItem(i)  # toplevel item
            child_amount = top_item.childCount()
            trial = top_item.child(i).child(0).data(5, 0)
            print(trial)

            for t in range(child_amount):
                list_rows.append(top_item.child(t).text(0))
                grand_child = top_item.child(t).child(0)
                data = grand_child.data(5, 0)
                df = pd.DataFrame(data, index=[0])
                final_pandas = pd.concat([final_pandas, df])
                # final_pandas = final_pandas.append(df)

        final_pandas.index = pd.Series(list_rows)
        final_pandas = final_pandas[["Label", "RsValue", "CSlow"]]
        final_pandas["comments"] = final_pandas.shape[0] * [""]

        self.draw_table(final_pandas)

    def draw_table(self, data):
        """ draws the table of the .dat metadata as indicated by the .pul Bundle file """
        try:
            self.table_model = PandasTable(data)
            print(self.table_model)
            # self.tableWidget.setStyleSheet("background-color:#232629; ")
            self.tableWidget.setModel(self.table_model)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            print(e)

    def draw_live_plot(self, data_x=None):
        """ this is necessary to draw the plot which is plotted to the self.configuration window
        this will further projected to the online-anaysis """
        print(data_x)
        # print(data_x[0], print(data_x[1]))
        self.canvas_live_plot.figure.clf()

        self.drawing()
        self.ax1.plot(data_x[0], data_x[1])
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
