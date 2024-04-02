import os
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from functools import partial
import pandas as pd
from matplotlib.backends.backend_qtagg import (NavigationToolbar2QT as NavigationToolbar)
from Frontend.OnlineAnalysis.ui_py.online_analysis_designer_object import Ui_Online_Analysis
from Backend.online_analysis_manager import OnlineAnalysisManager
from Backend.ExperimentTree.treeview_manager import TreeViewManager
from Backend.PlotHandler.plot_widget_manager import PlotWidgetManager
from Backend.DataReader.heka_reader import Bundle
from Backend.DataReader.new_unbundled_reader import BundleFromUnbundled
from Backend.DataReader.read_data_directory import ReadDataDirectory
from Backend.tokenmanager import InputDataTypes
from StyleFrontend.animated_ap import LoadingAnimation
from Frontend.CustomWidget.Pandas_Table import PandasTable
from Frontend.OnlineAnalysis.ui_py.RedundantDialog import RedundantDialog
from Backend.DataReader.ABFclass import AbfReader
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from Frontend.CustomWidget.user_notification_dialog import UserNotificationDialog
from database.DatabaseHandler.DuckDBInitalizer import DuckDBInitializer
import picologging
import numpy as np
from Frontend.OfflineAnalysis.CustomWidget.construction_side_handler import ConstrcutionSideDialog   

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
        self._video_mat = None
        self._image = None
        self.video_call = 0  # number of frames went through
        self.online_video = QGraphicsScene(self)  # set the video Graphic Scence
        self.online_video.addText("Load the Video if recorded from Experiment")
        self.graphicsView.setScene(self.online_video)
        self.online_analysis.setTabEnabled(1, False)
        self.online_analysis.setTabEnabled(2,False)
        self.database_handler = None # online db
        self.offline_database = None # offline db
        self.online_analysis_plot_manager = None
        self.online_analysis_tree_view_manager = None
        self._labbook_table = None
        self.frontend_style = None
        self.data_model_list = None
        self.transferred = False
        self._experiment_name = None
        self.file_queue = []
        
        # Connect the buttons, connect the logger
        self.logger = picologging.getLogger(__name__)
        self.connections_clicked()
        self.logger.info("Succesfully initialized Online Analysis Module")

    @property
    def experiment_name(self) -> str:
        """retrieve the experiment name"""
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, value: str) -> None:
        """sets the experiment name"""
        if isinstance(value, str):
            self._experiment_name = value
        else:
            self.logger.error(f"Wrong name indicated please use a string ant not {value}")
    @property
    def labbook_table(self) -> str:
        return self._labbook_table

    @labbook_table.setter
    def labbook_table(self, value):
        """This should set a new QTableView to the labbook table"""
        self._labbook_table = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value) -> None:
        self._image = value

    @property
    def video_mat(self):
        return self._video_mat

    @image.setter
    def video_mat(self, value) -> None:
        self._video_mat = value

    def enable_plot_options(self) -> None:
        """ switch the tab of the online analysis """
        if self.online_analysis_plot_manager:
            navigation = NavigationToolbar(self.online_analysis_plot_manager.canvas, self)
            self.plot_move.clicked.connect(navigation.pan)
            self.plot_zoom.clicked.connect(navigation.zoom)
            self.plot_home.clicked.connect(navigation.home)

    def update_database_handler(self, database_handler, offline_database) -> None:
        """should update the database handler of the class"""
        self.database_handler = database_handler
        self.offline_database = offline_database

    def connections_clicked(self) -> None:
        """ connect the buttons to the corresponding functions """
        self.button_select_data_file.clicked.connect(self.open_single_dat_file)
        self.online_analysis.currentChanged.connect(self.online_analysis_tab_changed)
        self.start_video_button.clicked.connect(self.video_show)
        self.transfer_to_offline_analysis.clicked.connect(self.start_db_transfer)
        self.transfer_into_db_button.clicked.connect(self.transfer_file_and_meta_data_into_db)
        self.show_sweeps_radio.toggled.connect(self.show_sweeps_toggled)
        self.classifier_stream.clicked.connect(partial(ConstrcutionSideDialog,self.frontend_style))
        self.logger.info("Successfully connected all the appropiates button calls")
        self.set_enabled_button()

    def set_enabled_button(self, enabled: bool = False) -> None:
        self.plot_move.setEnabled(enabled)
        self.plot_home.setEnabled(enabled)
        self.plot_zoom.setEnabled(enabled)
        self.save_image.setEnabled(enabled)
        self.classifier_stream.setEnabled(enabled)
        self.add_metadata_button.setEnabled(enabled)
        self.save_labbook_button.setEnabled(enabled)
        self.start_video_button.setEnabled(enabled)
        self.edit_meta.setEnabled(enabled)
        self.renameSeries.setEnabled(enabled)
        self.show_pgf_file.setEnabled(enabled)
        self.transfer_to_offline_analysis.setEnabled(enabled)
        self.save_plot_online.setEnabled(enabled)


    def transfer_file_and_meta_data_into_db(self) -> None:
        """ This function is responsible from transfering from in memory database
        to a written local database from duckDB for the offline analysis"""

        # write the current labbook table to the online in memory database
        # here  maybe a sanity check would be worthwhile
        table_name = self.create_labbook_name(self.experiment_name)
        labbook_table = self.labbook_model._data
        self.database_handler.database.execute(f"""UPDATE experiments
                                      SET labbook_table_name = (?)
                                      WHERE experiment_name = (?)
                                      """, (table_name,self.experiment_name))
        self.database_handler.database.execute(f"CREATE TABLE {table_name} AS SELECT * FROM labbook_table")

        # Finally retrieve the intersections from the tables between online and offline analysis
        table_offline = self.offline_database.database.execute("SHOW TABLES").fetchdf()["name"].values
        table_online = self.database_handler.database.execute("SHOW TABLES").fetchdf()["name"].values
        non_intersected = [i for i in table_online if i not in table_offline]
        intersected = [i for i in table_online if i in table_offline]
        self.add_meta_pgf_data_to_offline(non_intersected, intersected)

    def add_meta_pgf_data_to_offline(self, non_intersected :list, intersected: list) -> None:
        #' intersected' : name of tables that can be found in both databases
        #' non-intersected' name of tables that are only found in the online analysis db and need to be transfered
        #  since some parameters are foreign keys from other tables, the order of writing is very important

        print(intersected)
        
        print(non_intersected)

        foreign_key_dependency_list = ["experiments"]
        for tab in foreign_key_dependency_list:
            self.logger.info(f"Adding {tab} which is in both databases via appending")
            table = self.database_handler.database.execute(f"Select * from {tab}").fetchdf()
            try:
                self.offline_database.database.append(f"{tab}", table)
                print("success")
            except Exception as e:
                print(str(e))
                print("error detected")

        try:
            for table, data in zip(["global_meta_data", "experiment_series"], self.data_model_list):
                t = table 
                d = data._data
                self.offline_database.database.append(f"{table}",data._data)
        except Exception as e:
            CustomErrorDialog(f"Something is wrong with duplication {e}", self.frontend_style)
            self.logger.error(f"There were duplicated values found in the database please chec if {table} exist")
            return None
        
        # here more error prone processsing need to be operated
        for tab in non_intersected:
            self.logger.info(f"Adding {tab} that are not similiar between the two databases")
            if tab != "df_1":
                table_df = self.database_handler.database.execute(f"Select * from {tab}").fetchdf()
                self.offline_database.database.execute(f"CREATE TABLE {tab} as SELECT * FROM table_df;")
        # append the intersected table that are same without creating
        for tab in intersected:
            if tab not in ["offline_analysis", "global_meta_data", "experiment_series"]:
                self.logger.info(f"Adding {tab} which is in both databases via appending")
                table = self.database_handler.database.execute(f"Select * from {tab}").fetchdf()
                try:
                    self.offline_database.database.append(f"{tab}", table)
                except Exception as e:
                    print(str(e))
                    print("error detected")
                    
        self.logger.info("Successfully transferred all the data to the OfflineAnalysis")
        self.reset_class()
        UserNotificationDialog("Successfully transferred the recording into the permanent database. \n You can load this file now into offline analysis",self.frontend_style)

    def start_db_transfer(self) -> None:
        """
        transfer the experiment (must only be one) into the database
        """
        self.logger.info("Start database transfer into the offline database by switching notebook sides")
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

    def create_labbook_name(self, experiment_name: str) -> str:
        return f"labbook_{experiment_name}"

    @Slot()
    def online_analysis_tab_changed(self) -> None:
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        #if self.online_analysis.currentIndex() == 0:
        #    self.gridLayout_18.addWidget(self.online_treeview)
        if self.online_analysis.currentIndex() == 2:
            self.start_db_transfer()

    def show_sweeps_toggled(self) -> None:
        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)

    def open_single_dat_file(self, file_name: str=None) -> None:
        """ open a single experiment file (.abf or .dat), write it into the database and create a tree view from this
        recording. Since this is online analysis, the experiment is labeled "OFFLINE_ANALYSIS" in the experiment_label
        column in the global meta data table. If the file was not "transfered" to the database, the user will be asked
        to do an action when a new online analysis file will be loaded "
        """

        self.reset_class()

        self.ap = LoadingAnimation("Preparing your data: Please Wait", self.frontend_style)
        
        # open selection and retake users file selection
        # self.online_analysis.setCurrentIndex(0)
        # self.online_analysis_tabs.setCurrentIndex(0)

        if file_name is False:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("Data Files (*.dat *.abf)")
            # Get the selected file
            file_name = file_dialog.getOpenFileName(self, 'Open File', "", "Data Files (*.dat *.abf)")[0]
            self.logger.info(f"Open {file_name}")
            treeview_name = file_name.split("/")

            if ".dat" in treeview_name[-1]:
                treeview_name = treeview_name[-1].split(".")[0]
                self.logger.info("Open .dat file {file_name}")
            else:
                treeview_name = "_".join(treeview_name[-1].split("_")[:2])
                self.logger.info("Open .abf file {file_name}")
        else:
            treeview_name = file_name

        self.ap.make_widget()
        # save the path in the manager class
        self.online_manager._dat_file_name = file_name
        # check if this file is already within the database. if yes, the file name will be renamed copy-
        if not self.check_if_experiments_exist_online(treeview_name).empty:
            self.logger.info(f"""file already exists within the offline analysis
                                database with name {treeview_name}, Start redundancy check""")
            redundant = RedundantDialog(self.offline_database, treeview_name, self.logger)
            self.frontend_style.set_pop_up_dialog_style_sheet(redundant)
            result = redundant.exec_()
            if result == 0:
                return None
            treeview_name = redundant.new_treeview_name
            self.logger.info(f"Data was renamed to {treeview_name}")

        
        self.show_single_file_in_treeview(file_name, treeview_name)
        self.ap.stop_and_close_animation()

    def check_if_experiments_exist_online(self, treeview_name: str) -> pd.DataFrame:
        """ This should initally check if there is already an exisiting table in the database
        that is named like the new experiment submitted
        args:
            treeview_name (str) -> the inital name of the experiment inferred from the .dat file
        returns
            pd.DataFrame -> holding all the experiment that are named equally so we can check for emptyness
        """
        q = f'select * from experiments where experiment_name = \'{treeview_name}\''
        df = self.offline_database.database.execute(q).fetchdf()
        self.logger.info("This is the current name of the file: {treeview_name}")
        return df

    def show_single_file_in_treeview(self, file_name: str, treeview_name: str) -> None:
        """
        load the new file into the database and create a treeview from it
        """
        # to allow mapping of the current experiment with the analysis id
        self.logger.info("Online Analysis: show_single_file_in_treeview: Loading Single File" + treeview_name)
        self.experiment_name = treeview_name

        # create treeview of this .dat file
        if self.online_analysis_tree_view_manager is None:
            self.online_analysis_tree_view_manager = TreeViewManager(database = self.database_handler,
                                                                     treebuild_widget = self.online_treeview,
                                                                     frontend = self.frontend_style)
            self.logger.info("Successfully loaded the Online Analysis TreeViewManager")

        # connect with a new plot manager to handle item clicks within the treeview
        if self.online_analysis_plot_manager is None:
            self.online_analysis_plot_manager = PlotWidgetManager(self.plot_layout, self.database_handler, None,
                                                         False, self.frontend_style)
            self.logger.info("Successfully loaded the Online Analysis PlotWidgetManager")

        # give the experiment (name provided by treeview_name) the experiment_label ONLINE_ANALYSIS to be identified
        read_directory_handler = ReadDataDirectory(self.database_handler)
        read_directory_handler.meta_data_assignment_list = [
            ['Experiment_name', 'Experiment_label', 'Species', 'Genotype', 'Sex', 'Condition', 'Individuum_id'],
            [treeview_name, 'None', 'None', 'None', 'None', 'None', 'None', 'None']]

        read_directory_handler.meta_data_assigned_experiment_names = ['Experiment_name', treeview_name]

        # file type identification
        pathname, filename_with_extension = os.path.split(file_name)
        filename, extension = os.path.splitext(filename_with_extension)
       

        # if .dat file: run dat file specific bundle reading and insertion into db
        if extension == InputDataTypes.HEKA_DATA_FILE_ENDING.value:
            
            bundle = Bundle(file_name) # open heka reader
            if bundle.pgf is None:
                bundle = BundleFromUnbundled(pathname + "/",filename).generate_bundle()
                if bundle.pgf is None:
                    CustomErrorDialog("Unsupported File Format", self.frontend_style)
                    self.logger.error("Unsupported File Format detected" + file_name)
                    return
                else:
                    self.logger.info("UNBUNDLED HEKA FILE detected")
            else:
                self.logger.info("BUNDLED HEKA FILE detected")    

            pgf_data_frame = read_directory_handler.read_series_specific_pgf_trace_into_df(
                    [], bundle, [], None, None, None)
            
            self.logger.info(f"successfully generated pgf_dataframe from file {file_name}")
            # write this file into the database
            read_directory_handler.single_file_into_db([], bundle, treeview_name, self.database_handler,
                                                              [0, -1, 0, 0], pgf_data_frame)

        # if .abf file: run abf file specific bundle creation and insertion into db
        elif extension == InputDataTypes.ABF_FILE_ENDING.value:
            self.logger.info("ABF FIle Reading Online Analysis")
            
           
            pathname, filename_with_extension = os.path.split(file_name)
            filename, extension = os.path.splitext(filename_with_extension)
            abf_file_list = os.listdir(os.path.dirname(file_name))
            self.logger.info(abf_file_list)
            
                        # read only files that have the same idenfier as the selected one
            abf_identifier = os.path.basename(file_name).split("_")
            abf_identifier = abf_identifier[0]
            
            abf_file_data = []



            for abf in abf_file_list:

                if abf_identifier in abf:
                    print(abf)
                    file_2 = pathname + "/" + abf
                    abf_file = AbfReader(file_2)
                    data_file = abf_file.get_data_table()
                    meta_data = abf_file.get_metadata_table()
                    pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                    experiment_name = [abf_file.get_experiment_name(), "None", "None", "None", "None", "None", "None", "None"]
                    series_name = abf_file.get_series_name()
                    abf_file_data.append((data_file, meta_data, pgf_tuple_data_frame, series_name, InputDataTypes.ABF_FILE_ENDING))
            if abf_file_data:
                bundle = [abf_file_data, experiment_name]
                read_directory_handler.single_abf_file_into_db(bundle, self.database_handler)
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
        self.online_analysis_tree_view_manager.map_data_to_analysis_id([self.experiment_name])
        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)
        self.logger.info("Finished the loading of the file!")
        self.online_analysis.setTabEnabled(1,True)
        self.online_analysis.setTabEnabled(2,True)
        self.online_analysis_tree_view_manager.click_top_level()
        self.enable_plot_options()
        self.set_enabled_button(True)
        self.get_columns_data_to_table()
        self.stackedWidget.setCurrentIndex(0)
        self.logger.info(f"Successfully transferred to online analysis db the file {self.experiment_name}")

    def video_show(self) -> None:
        """ show the video in the graphics view
        Generate the Qtimer for the function"""
        if self.video_mat is not None:
            self.start_video = QTimer()  # create a timer
            self.start_video.timeout.connect(self.run_video)  # connect the timer to the start camera function
            self.start_video.start(250)

    def run_video(self) -> None:
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

    def get_columns_data_to_table(self) -> None:
        """ This retrieves information from the recording which can
        be used in a Labbook like table.
        In addition a comment section is added where comments to specific experimental conditions
        can be made"""
        self.logger.info(f"Creating labbook for file {self.experiment_name}")
        final_pandas = self.online_analysis_tree_view_manager.tree_build_widget.selected_tree_view.model()._data 
        final_pandas = final_pandas.drop(columns = ["identifier", "level","parent"])
        self.experiment_name  = final_pandas["item_name"].values[0]
        list_cslow = [] # need to change this to support more metadata
        list_rs = [] # need to change also
        for i in final_pandas["item_name"].values[1:]:
            cslow, rs = self.retrieve_cslow_rs(i)
            self.logger.info(f"Retrieved Cslow: {cslow}, and Rseries: {rs} for {self.experiment_name}")
            list_cslow.append(cslow)
            list_rs.append(rs)
        
        final_pandas = final_pandas.iloc[1:,:]
        final_pandas["condition"] = final_pandas.shape[0] * [""]
        final_pandas["RsValue"] = list_rs
        final_pandas["Cslow"] = list_cslow
        final_pandas["comments"] = final_pandas.shape[0] * [""]
        final_pandas["ids"] = final_pandas.shape[0] * [""]
        self.draw_table(final_pandas)

    def retrieve_cslow_rs(self, series_name: str) -> None:
        """this returns the searchable metadata parameter that one wants to add to the notebook
        This function should be added to the database reader"""
        try: 
            table = self.database_handler.database.execute("Select * from experiment_series;").fetchdf()
            print(table)
            table_name = self.database_handler.database.execute("Select series_identifier FROM experiment_series WHERE experiment_name = (?) AND series_name = (?)", (self.experiment_name, series_name)).fetchall()[0][0]
            series_meta_table = self.database_handler.database.execute(f"Select * from imon_meta_data_{self.experiment_name}_{table_name}").fetchdf()
            series_meta = series_meta_table.set_index("Parameter").T
            return np.mean(series_meta["CSlow"].astype(float).values), np.mean(series_meta["RsValue"].astype(float).values)
        except Exception as e:
            print("This is the error!")

    def draw_table(self, data: pd.DataFrame) -> None:
        """ draws the table of the .dat metadata as indicated by the .pul Bundle file """
        try:
            if self.labbook_table is None:
                self.labbook_table = QTableView()
                self.table_layout.addWidget(self.labbook_table)

            self.labbook_model = PandasTable(data)
            self.labbook_table.setModel(self.labbook_model)
            self.tableView.setModel(self.labbook_model)
            self.labbook_model.resize_header(self.labbook_table)
            self.labbook_model.resize_header(self.tableView)
            self.logger.info(f"Successfully generated labbook table for {self.experiment_name}")
        except Exception as e:
            print(f"There is an error in draw_table(online_analysis) {e}")
            self.logger.error(f"""There is an error in draw_table(online_analysis)
                                  for the labbook: {e}  for experiment: {self.experiment_name}
                              """)

    def draw_scene(self, image) -> None:
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

    def reset_class(self) -> None:
        """This should reset the class to the base state so that we can use it for more """
        self.logger.info(f"Resetting class after submitting {self.experiment_name} to Offline DB")
        try:
            self.file_queue.pop(0)
        except IndexError:
            self.logger.warning("No data was found in the queue list, it was empty")

        
        try:
            self.database_handler.database.close()
            # maybe we need to assure that the closing is finished ? but should be the default way in python ?
            self.database_handler.database, _ = DuckDBInitializer(self.logger,
                                                              "online_analysis",
                                                              in_memory = True,
                                                              database_path = "./database/").init_database()
           
            # initially set as none
            if self.online_analysis_tree_view_manager is not None:
                self.online_analysis_tree_view_manager.clear_tree()
            if self.online_analysis_plot_manager is not None:
                self.online_analysis_plot_manager.canvas.figure.clf()
                self.online_analysis_plot_manager.canvas.draw_idle()
        except Exception as e:
            print(e)
            self.logger.error("Error in reset class function:" + str(e))

        for i in reversed(range(self.table_layout.count())):
                self.table_layout.itemAt(i).widget().deleteLater()
        # reset the variables to the original state
        self.labbook_table = None
        self.data_model_list = None
        self.transferred = False
        self.experiment_name = "no_name"
        self.video_mat = None
        self.image = None
        self.video_call = 0  # number of frames went through
        #self.graphicsView.clear()

        if self.online_analysis.currentIndex() != 0:
            self.online_analysis.setCurrentIndex(0)

        # this disables the labbook tabs as long as the no new analysis is loaded
        self.online_analysis.setTabEnabled(1, False)
        self.online_analysis.setTabEnabled(2,False)
        if self.file_queue:
            self.logger.info("Updating the View using the next member in the viewing list")
            self.open_single_dat_file(self.file_queue[0])
            self.logger.info("Successfully updated the view")
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.set_enabled_button()



