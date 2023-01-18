from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import logging
import pandas as pd
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from QT_GUI.OnlineAnalysis.ui_py.online_analysis_designer_object import Ui_Online_Analysis
from online_analysis_manager import OnlineAnalysisManager
from treeview_manager import TreeViewManager
from plot_widget_manager import PlotWidgetManager
from pathlib import Path
from functools import partial
from Pandas_Table import PandasTable
from ABFclass import AbfReader
import os

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
        self.online_analysis_plot_manager = None
        self.online_analysis_tree_view_manager = None

        self.frontend_style = None

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
        self.transfer_into_db_button.clicked.connect(self.transfer_file_and_meta_data_into_db)
        #
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
        q = 'select * from global_meta_data where experiment_label = \'ONLINE_ANALYSIS\''
        db_experiment_data_frame = self.database_handler.database.execute(q).fetchdf()
        gui_experiment_data_frame = self.experiment_treeview.model()._data

        # check for the experiment_name to be changed by user input into the gui and therefore update the db
        if not db_experiment_data_frame["experiment_name"].equals(gui_experiment_data_frame["experiment_name"]):
            old_experiment_name = db_experiment_data_frame["experiment_name"].values[0]
            new_experiment_name = gui_experiment_data_frame["experiment_name"].values[0]

            for table in ["global_meta_data", "experiments"]:
                q = f'update {table} set experiment_name = \'{new_experiment_name}\' where experiment_name = \'{old_experiment_name}\''
                self.database_handler.database.execute(q)

            q =  f'select * from experiment_series where experiment_name = \'{old_experiment_name}\''
            experiment_series_df = self.database_handler.database.execute(q).fetchdf()

            for index,row in experiment_series_df.iterrows():
                new_sweep_table_name = "imon_signal_"+new_experiment_name+"_"+row["series_identifier"]
                new_meta_data_table_name = "imon_meta_data_"+new_experiment_name+"_"+row["series_identifier"]
                new_pgf_data_table_name = "pgf_table_"+new_experiment_name+"_"+row["series_identifier"]

                q = f'alter table {row["sweep_table_name"]} rename to {new_sweep_table_name}'
                self.database_handler.database.execute(q)

                q = f'alter table {row["meta_data_table_name"]} rename to {new_meta_data_table_name}'
                self.database_handler.database.execute(q)

                q = f'alter table {row["pgf_data_table_name"]} rename to {new_pgf_data_table_name}'
                self.database_handler.database.execute(q)

                q = f'update experiment_series set sweep_table_name = \'{new_sweep_table_name}\',' \
                    f' meta_data_table_name = \'{new_meta_data_table_name}\',' \
                    f' pgf_data_table_name = \'{new_pgf_data_table_name}\', experiment_name = \'{new_experiment_name}\'' \
                    f' where series_identifier = \'{row["series_identifier"]}\' and ' \
                    f'experiment_name = \'{old_experiment_name}\' '

                self.database_handler.database.execute(q)

            # update treeviews
            self.start_db_transfer()

        # check for duplicates and ask the user to change the name
        for index,row in gui_experiment_data_frame.iterrows():
            if "copy_" in row["experiment_name"]:
                dialog = QDialog()
                dialog_layout = QGridLayout()
                error_msg = f'An experiment with name {row["experiment_name"]}  already exists in the database. Please rename or discard'
                dialog_label = QLabel(error_msg)
                rename_button = QPushButton("Rename")
                rename_button.clicked.connect(dialog.close)
                discard_button = QPushButton("Discard")
                # discard_button.clicked.connect(self.discard_online_analysis_file)
                dialog_layout.addWidget(dialog_label)
                dialog_layout.addWidget(rename_button)
                dialog_layout.addWidget(discard_button)
                dialog.setLayout(dialog_layout)
                dialog.exec_()
            else:
                q = f'update global_meta_data set ' \
                    f'experiment_label = \'{row["experiment_label"]}\', species = \'{row["species"]}\', ' \
                    f'genotype = \'{row["genotype"]}\',' \
                    f'sex = \'{row["sex"]}\', condition = \'{row["condition"]}\', individuum_id = \'{row["individuum_id"]}\' ' \
                    f'where experiment_name = \'{row["experiment_name"]}\''
                self.database_handler.database.execute(q)

                series_data_frame = self.series_treeview.model()._data

                print("writing series into db", series_data_frame)

                for index,series_row in series_data_frame.iterrows():
                    q = f'update experiment_series set ' \
                        f'series_meta_data = \'{series_row["series_meta_data"]}\', experiment_name = \'{series_row["experiment_name"]}\' ' \
                        f'where experiment_name = \'{series_row["experiment_name"]}\' and series_identifier = \'{series_row["series_identifier"]}\' '

        print("Transfer succeeded")
        self.start_db_transfer()

    def start_db_transfer(self):
        """
        transfer the experiment (must only be one) into the database
        """
        self.online_analysis.setCurrentIndex(2)

        # display and update global_meta_data and experiment_series table
        for table in ["global_meta_data", "experiment_series"]:

            if table == "global_meta_data":
                q = f'select * from global_meta_data where experiment_label = \'ONLINE_ANALYSIS\''
                df = self.database_handler.database.execute(q).fetchdf()
                template_table_view = self.experiment_treeview

                # overwrite "ONLINE_ANALYSIS" to make sure this label will not be used by the user
                df["experiment_label"] = "None"
            else:
                q = f'select * from experiment_series where experiment_name = ' \
                    f'(select experiment_name from global_meta_data where experiment_label = \'ONLINE_ANALYSIS\')'
                df = self.database_handler.database.execute(q).fetchdf()
                template_table_view = self.series_treeview

            content_model = PandasTable(df)
            print(df)
            template_table_view.setModel(content_model)

            template_table_view.show()

            # transfer_into_db_button will be displayed and will call self.transfer_file_and_meta_data_into_db when
            # clicked


    @Slot()
    def online_analysis_tab_changed(self):
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        if self.online_analysis.currentIndex() == 0:
            #self.tree_layouting_change.addWidget(self.tree_tab_widget)
            self.gridLayout_18.addWidget(self.online_treeview)
        if self.online_analysis.currentIndex() == 1:
            self.gridLayout_6.addWidget(self.online_treeview)
            self.get_columns_data_to_table()
            #self.verticalLayout.addWidget(self.tree_tab_widget)
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
        self.online_analysis_tabs.setCurrentIndex(0)

        if file_name is False:
            #file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.dat")[0]
            #file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.abf")[0]
            file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "")[0]

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

            # check if this file is already within the database. if yes, the file name will be renamed copy-
            q = f'select * from experiments where experiment_name = \'{treeview_name}\''
            df = self.database_handler.database.execute(q).fetchdf()
            print(treeview_name)
            print("fetched df", df)
            if not df.empty:
                print("file already exists within the database")
                treeview_name = "copy_" + treeview_name
            self.show_single_file_in_treeview(file_name, treeview_name)
        else:
            dialog = QDialog()
            self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
            old_file_name = old_file_df["experiment_name"].values.tolist()[0]
            text = f'You have non-transfered experiments from previous online analysis \n ' \
                   f'experiment name: {old_file_name} \n ' \
                   f'Do you want to transfer it to the database or discard ?'
            dialog_label = QLabel(text)
            transfer_button = QPushButton("Transfer")
            transfer_button.clicked.connect(partial(self.transfer_experiment_from_previous_online_analysis,dialog))

            discard_button = QPushButton("Discard")
            discard_button.clicked.connect(partial(self.discard_online_analysis_file, old_file_name,
                                                   treeview_name, file_name, dialog))
            layout = QGridLayout()
            layout.addWidget(dialog_label)
            layout.addWidget(transfer_button)
            layout.addWidget(discard_button)
            dialog.setLayout(layout)
            dialog.exec_()

    def transfer_experiment_from_previous_online_analysis(self,dialog):
        dialog.close()
        self.start_db_transfer()

    def discard_online_analysis_file(self, old_file_name, treeview_name, file_name, dialog):
        """
        remove an experiment by its name and all related entries in global_meta_data, experiments and experiment_series
        tables
        """
        dialog.close()
        self. remove_table_from_db(old_file_name)

        # load the new file into the database and create a treeview from it
        self.show_single_file_in_treeview(file_name, treeview_name)

    def remove_table_from_db(self,old_file_name):

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
                                                         False)

        # give the experiment (name provided by treeview_name) the experiment_label ONLINE_ANALYSIS to be identified
        self.online_analysis_tree_view_manager.meta_data_assignment_list = [
            ['Experiment_name', 'Experiment_label', 'Species', 'Genotype', 'Sex', 'Condition', 'Individuum_id'],
            [treeview_name, 'ONLINE_ANALYSIS', 'None', 'None', 'None', 'None', 'None', 'None']]

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
                    experiment_name = [abf_file.get_experiment_name(),'ONLINE_ANALYSIS', 'None', 'None', 'None', 'None', 'None', 'None']
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
        self.online_analysis_tree_view_manager.selected_meta_data_list = ["ONLINE_ANALYSIS"]



        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)
        print("finished.3")

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
        #toDO add the documentation here
        """Should put the labbook with selecte metadata into the 
        Retrievable Labbook
        """

        """
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
        """
        final_pandas = self.online_treeview.selected_tree_view.model()._data
        final_pandas = final_pandas.drop(columns = ["identifier", "level","parent"])

        final_pandas["condition"] = final_pandas.shape[0] * [""]
        final_pandas["RsValue"] = final_pandas.shape[0] * [""]
        final_pandas["Cslow"] = final_pandas.shape[0] * [""]
        final_pandas["comments"] = final_pandas.shape[0] * [""]

        self.draw_table(final_pandas)

    def draw_table(self, data):
        """ draws the table of the .dat metadata as indicated by the .pul Bundle file """
        try:
            labbook_table = QTableView()
            table_model = PandasTable(data)
            labbook_table.setModel(table_model)
            self.table_layout.addWidget(labbook_table)
            labbook_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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
