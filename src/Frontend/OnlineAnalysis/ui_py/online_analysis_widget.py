import os
import re
from functools import partial
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
import picologging
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from Backend.DataReader.ABFclass import AbfReader
from Backend.DataReader.read_data_directory import ReadDataDirectory
from Backend.ExperimentTree.treeview_manager import TreeViewManager
from Backend.PlotHandler.plot_widget_manager import PlotWidgetManager
from Backend.tokenmanager import InputDataTypes
from database.DatabaseHandler.DuckDBInitalizer import DuckDBInitializer
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from Frontend.CustomWidget.Pandas_Table import PandasTable
from Frontend.CustomWidget.user_notification_dialog import UserNotificationDialog
from Frontend.OfflineAnalysis.CustomWidget.construction_side_handler import (
    ConstrcutionSideDialog,
)
from Frontend.OnlineAnalysis.ui_py.online_analysis_designer_object import (
    Ui_Online_Analysis,
)
from Frontend.OnlineAnalysis.ui_py.RedundantDialog import RedundantDialog
from StyleFrontend.animated_ap import LoadingAnimation

if TYPE_CHECKING:
    from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
    from StyleFrontend.frontend_style import Frontend_Style


class Labbook:
    def __init__(self, parent=None) -> None:
        """Initialize the Labbook class."""
        self._labbook_table: pd.DataFrame | None = None
        self.logger = picologging.getLogger(__name__)

    @property
    def labbook_table(self) -> pd.DataFrame | None:
        return self._labbook_table

    @labbook_table.setter
    def labbook_table(self, value: pd.DataFrame) -> None:
        """This should set a new QTableView to the labbook table"""
        self._labbook_table = value
        self.logger.info(
            f"Successfully set the labbook table for {self.experiment_name}"
        )


    def create_labbook_name(self) -> None:
        self.labbook_name = f"labbook_{self.experiment_name}"

    def get_columns_data_to_table(self, tree_view_manager: TreeViewManager) -> None:
        """This retrieves information from the recording which can
        be used in a Labbook like table.
        In addition a comment section is added where comments to specific experimental conditions
        can be made"""
        final_pandas = (
            tree_view_manager.tree_build_widget.selected_tree_view.model()._data
        )
        final_pandas = final_pandas.drop(columns=["identifier", "level", "parent"])
        self.experiment_name = final_pandas["item_name"].values[0]
        self.logger.info(f"Creating labbook for file {self.experiment_name}")
        list_cslow = []  # need to change this to support more metadata
        list_rs = []  # need to change also
        for i in final_pandas["item_name"].values[1:]:
            cslow, rs = self.retrieve_cslow_rs(i)
            self.logger.info(
                f"Retrieved Cslow: {cslow}, and Rseries: {rs} for {self.experiment_name}"
            )
            list_cslow.append(cslow)
            list_rs.append(rs)

        final_pandas = final_pandas.iloc[1:, :]
        final_pandas["condition"] = final_pandas.shape[0] * [""]
        final_pandas["RsValue"] = list_rs
        final_pandas["Cslow"] = list_cslow
        final_pandas["comments"] = final_pandas.shape[0] * [""]
        final_pandas["ids"] = final_pandas.shape[0] * [""]
        self.labbook_table = final_pandas

    def retrieve_cslow_rs(self, series_name: str) -> tuple[float | None, float | None]:
        """Retrieve Cslow and Rs values for a given series name.

        Args:
            series_name (str): The name of the series to retrieve data for.

        Returns:
            tuple: A tuple containing the mean Cslow and Rs values, or None if an error occurs.
        """
        try:
            table = self.database_handler.database.execute(
                "Select * from experiment_series;"
            ).fetchdf()
            table_name = self.database_handler.database.execute(
                "Select series_identifier FROM experiment_series WHERE experiment_name = (?) AND series_name = (?)",
                (self.experiment_name, series_name),
            ).fetchall()[0][0]
            series_meta_table = self.database_handler.database.execute(
                f"Select * from imon_meta_data_{self.experiment_name}_{table_name}"
            ).fetchdf()
            series_meta = series_meta_table.set_index("Parameter").T
            return np.mean(series_meta["CSlow"].astype(float).values), np.mean(
                series_meta["RsValue"].astype(float).values
            )
        except Exception:
            print("This is the error!")
            return None, None


class ImageHandler:
    def __init__(self, parent=None) -> None:
        """Initialize the ImageHandler class."""
        self._video_mat: np.ndarray | None = None
        self._image: QImage | None = None
        self.video_call: int = 0

    def video_show(self) -> None:
        if self.video_mat is not None:
            self.start_video = QTimer()  # create a timer
            self.start_video.timeout.connect(
                self.run_video
            )  # connect the timer to the start camera function
            self.start_video.start(250)

    def run_video(self) -> None:
        """Play the recorded video/gif in the labbook."""
        self.video_call += 1
        item = self.video_mat[self.video_call]
        self.online_video.clear()  # clear the scene
        self.online_video.addPixmap(item)
        print(self.video_call, len(self.video_mat))
        if len(self.video_mat) - 1 == self.video_call:
            self.start_video.stop()
            self.video_call = 0

    def draw_scene(self, image) -> None:
        """Draw the image into the configuration window.

        Args:
            image (QImage): The image to be drawn.
        """
        self.online_scence = QGraphicsScene(self)
        self.image_experiment.setScene(self.online_scence)  # set the scene to the image
        item = QGraphicsPixmapItem(image)
        self.image_experiment.scene().addItem(item)


class Online_Analysis(QWidget, Ui_Online_Analysis):
    def __init__(self, parent=None) -> None:
        """Initialize the Online_Analysis class."""
        QWidget.__init__(self, parent)
        self.setupUi(self)

        # initialize the OnlineAnalysis Manager
        self.logger = picologging.getLogger(__name__)
        self.online_analysis_plot_manager = None

        # TODO: can this savely be removed?=
        # self.online_manager = OnlineAnalysisManager()
        self.online_analysis.setCurrentIndex(0)
        self.online_analysis.setTabPosition(QTabWidget.East)

        # check if video matrix is there, image is there and initialize the video calls

        self.video_call: int = 0  # number of frames went through
        self.online_video = QGraphicsScene(self)  # set the video Graphic Scence
        self.online_video.addText("Load the Video if recorded from Experiment")
        self.graphicsView.setScene(self.online_video)
        self.online_analysis.setTabEnabled(1, False)
        self.online_analysis.setTabEnabled(2, False)
        self.database_handler: DuckDBDatabaseHandler | None = None  # online db
        self.offline_database: DuckDBDatabaseHandler | None = None  # offline db
        self.online_analysis_config: OnlineAnalysisConfig | None = None
        self.online_analysis_plot_manager: PlotWidgetManager | None = None
        self.online_analysis_tree_view_manager: TreeViewManager | None = None
        self.frontend_style: Frontend_Style | None = None
        self.labbook: Labbook = Labbook()
        self.data_model_list: list[PandasTable] | None = None
        self.transferred: bool = False
        self._experiment_name: str | None = None
        self.file_queue: list[str] = []

    @property
    def experiment_name(self) -> str | None:
        """retrieve the experiment name"""
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, value: str) -> None:
        """sets the experiment name"""
        if isinstance(value, str):
            self._experiment_name = value
        else:
            self.logger.error(
                f"Wrong name indicated please use a string ant not {value}"
            )

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value) -> None:
        self._image = value

    @property
    def video_mat(self):
        return self._video_mat

    @video_mat.setter
    def video_mat(self, value) -> None:
        self._video_mat = value

    def update_database_handler(
        self,
        database_handler,
        offline_database,
        frontend_style,
    ) -> None:
        """Update the database handler of the class.

        Args:
            database_handler: The handler for the online database.
            offline_database: The handler for the offline database.
            frontend_style: The frontend style configuration.
        """

        self.database_handler = database_handler
        self.offline_database = offline_database
        self.frontend_style = frontend_style

        self.initialize_tree_view_manager()
        self.initialize_plot_manager()
        self.configure_online_analysis()

    def initialize_tree_view_manager(self) -> None:
        """Initialize the tree view manager."""
        if self.online_analysis_tree_view_manager is None:
            self.online_analysis_tree_view_manager = TreeViewManager(
                database=self.database_handler,
                treebuild_widget=self.online_treeview,
                frontend=self.frontend_style,
            )
            self.logger.info("Successfully loaded the Online Analysis TreeViewManager")

    def initialize_plot_manager(self) -> None:
        """Initialize the plot manager."""
        if self.online_analysis_plot_manager is None:
            self.online_analysis_plot_manager = PlotWidgetManager(
                self.plot_layout,
                self.database_handler,
                None,
                False,
                self.frontend_style,
            )
            self.logger.info(
                "Successfully loaded the Online Analysis PlotWidgetManager"
            )

    def configure_online_analysis(self) -> None:
        """Configure the online analysis."""
        self.online_analysis_config = OnlineAnalysisConfig(
            self, self.online_analysis_plot_manager
        )
        self.online_analysis_config.connections_clicked()

    def transfer_file_and_meta_data_into_db(self) -> None:
        """This function is responsible from transfering from in memory database
        to a written local database from duckDB for the offline analysis"""

        # write the current labbook table to the online in memory database
        # here  maybe a sanity check would be worthwhile
        self.labbook.create_labbook_name()
        labbook_table = self.labbook.labbook_table
        self.database_handler.database.execute(
            """UPDATE experiments
                                      SET labbook_table_name = (?)
                                      WHERE experiment_name = (?)
                                      """,
            (self.labbook.labbook_name, self.experiment_name),
        )
        self.database_handler.database.execute(
            f"CREATE TABLE {self.labbook.labbook_name} AS SELECT * FROM labbook_table"
        )

        # Finally retrieve the intersections from the tables between online and offline analysis
        table_offline = (
            self.offline_database.database.execute("SHOW TABLES")
            .fetchdf()["name"]
            .values
        )
        table_online = (
            self.database_handler.database.execute("SHOW TABLES")
            .fetchdf()["name"]
            .values
        )
        non_intersected = [i for i in table_online if i not in table_offline]
        intersected = [i for i in table_online if i in table_offline]
        self.add_meta_pgf_data_to_offline(non_intersected, intersected)

    def add_meta_pgf_data_to_offline(
        self, non_intersected: list, intersected: list
    ) -> None:
        """Add metadata and PGF data to the offline database.

        Args:
            non_intersected (list): Tables only found in the online analysis database.
            intersected (list): Tables found in both databases.
        """
        foreign_key_dependency_list = ["experiments"]
        for tab in foreign_key_dependency_list:
            self.logger.info(f"Adding {tab} which is in both databases via appending")
            table = self.database_handler.database.execute(
                f"Select * from {tab}"
            ).fetchdf()
            try:
                self.offline_database.database.append(f"{tab}", table)
            except Exception as e:
                print(str(e))

        try:
            for table, data in zip(
                ["global_meta_data", "experiment_series"], self.data_model_list
            ):
                self.offline_database.database.append(f"{table}", data._data)
        except Exception as e:
            CustomErrorDialog(
                f"Something is wrong with duplication {e}", self.frontend_style
            )
            self.logger.error(
                f"There were duplicated values found in the database please chec if {table} exist"
            )
            return None

        # here more error prone processsing need to be operated
        for tab in non_intersected:
            self.logger.info(
                f"Adding {tab} that are not similiar between the two databases"
            )
            if tab != "df_1":
                table_df = self.database_handler.database.execute(
                    f"Select * from {tab}"
                ).fetchdf()
                self.offline_database.database.execute(
                    f"CREATE TABLE {tab} as SELECT * FROM table_df;"
                )
        # append the intersected table that are same without creating
        for tab in intersected:
            if tab not in ["offline_analysis", "global_meta_data", "experiment_series"]:
                self.logger.info(
                    f"Adding {tab} which is in both databases via appending"
                )
                table = self.database_handler.database.execute(
                    f"Select * from {tab}"
                ).fetchdf()
                try:
                    self.offline_database.database.append(f"{tab}", table)
                except Exception as e:
                    print(str(e))
                    print("error detected")

        self.logger.info("Successfully transferred all the data to the OfflineAnalysis")
        self.online_analysis_config.reset_class()
        UserNotificationDialog(
            "Successfully transferred the recording into the permanent database. \n You can load this file now into offline analysis",
            self.frontend_style,
        )

    def start_db_transfer(self) -> None:
        """
        transfer the experiment (must only be one) into the database
        """
        self.logger.info(
            "Start database transfer into the offline database by switching notebook sides"
        )
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
    def online_analysis_tab_changed(self) -> None:
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        # if self.online_analysis.currentIndex() == 0:
        #    self.gridLayout_18.addWidget(self.online_treeview)
        if self.online_analysis.currentIndex() == 2:
            self.start_db_transfer()

    def show_sweeps_toggled(self) -> None:
        """Update tree views when sweeps are toggled."""
        self.online_analysis_tree_view_manager.update_treeviews(
            self.online_analysis_plot_manager
        )

    def open_single_dat_file(self, file_name: str = None) -> None:
        """open a single experiment file (.abf or .dat), write it into the database and create a tree view from this
        recording. Since this is online analysis, the experiment is labeled "OFFLINE_ANALYSIS" in the experiment_label
        column in the global meta data table. If the file was not "transfered" to the database, the user will be asked
        to do an action when a new online analysis file will be loaded "
        """

        self.online_analysis_config.reset_class()

        self.ap = LoadingAnimation(
            "Preparing your data: Please Wait", self.frontend_style
        )

        # open selection and retake users file selection
        # self.online_analysis.setCurrentIndex(0)
        # self.online_analysis_tabs.setCurrentIndex(0)

        if file_name is False:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("Data Files (*.dat *.abf)")
            # Get the selected file
            file_name = file_dialog.getOpenFileName(
                self, "Open File", "", "Data Files (*.dat *.abf)"
            )[0]
            self.logger.info(f"Open {file_name}")
            treeview_name = file_name.split("/")

            # regexps in the file name will make the database handler crash
            if self.regexp_check(treeview_name[-1]):
                CustomErrorDialog(
                    f"The file name {treeview_name[-1]} contains disallowed characters. \n Not allowed are whitespace, dashes, hyphens and hashtags. \n Please rename the file !",
                    self.frontend_style,
                )
                self.logger.error(
                    f"The file name {treeview_name[-1]} contains disallowed characters."
                )
                return

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
        # self.online_manager._dat_file_name = file_name
        # check if this file is already within the database. if yes, the file name will be renamed copy-
        if not self.check_if_experiments_exist_online(treeview_name).empty:
            self.logger.info(f"""file already exists within the offline analysis
                                database with name {treeview_name}, Start redundancy check""")
            redundant = RedundantDialog(
                self.offline_database, treeview_name, self.logger
            )
            self.frontend_style.set_pop_up_dialog_style_sheet(redundant)
            result = redundant.exec_()
            if result == 0:
                return None
            treeview_name = redundant.new_treeview_name
            self.logger.info(f"Data was renamed to {treeview_name}")

        self.show_single_file_in_treeview(file_name, treeview_name)
        self.ap.stop_and_close_animation()

    def regexp_check(self, file_name):
        """
        Check if the file name contains disallowed characters: whitespace, dashes, hyphens, and hashtags.

        Args:
        file_name (str): The file name to be checked.

        Returns:
        bool: True if the file name contains disallowed characters, False otherwise.
        """
        pattern = r"[ \-#]"

        # Search for disallowed characters in the file name
        if re.search(pattern, file_name):
            # If a match is found, return True
            return True
        else:
            # If no match is found, return False
            return False

    def check_if_experiments_exist_online(self, treeview_name: str) -> pd.DataFrame:
        """Check if there is an existing table in the database with the same name as the new experiment.

        Args:
            treeview_name (str): The initial name of the experiment.

        Returns:
            pd.DataFrame: DataFrame holding all experiments with the same name.
        """

        q = f"select * from experiments where experiment_name = '{treeview_name}'"
        df = self.offline_database.database.execute(q).fetchdf()
        self.logger.info("This is the current name of the file: {treeview_name}")
        return df

    def show_single_file_in_treeview(self, file_name: str, treeview_name: str) -> None:
        """Load a new file into the database and create a tree view from it.

        Args:
            file_name (str): The name of the file to load.
            treeview_name (str): The name for the tree view.
        """
        self.logger.info(f"Online Analysis: show_single_file_in_treeview: Loading Single File {treeview_name}")
        self.experiment_name = treeview_name

        read_directory_handler = self.initialize_read_directory_handler(treeview_name)

        # file type identification
        pathname, filename_with_extension = os.path.split(file_name)
        _, extension = os.path.splitext(filename_with_extension)

        if extension == InputDataTypes.HEKA_DATA_FILE_ENDING.value:
            self.handle_heka_file(read_directory_handler, filename_with_extension, pathname)
        elif extension == InputDataTypes.ABF_FILE_ENDING.value:
            self.handle_abf_file(read_directory_handler, file_name)
        else:
            self.show_file_type_error()

        self.finalize_tree_view_setup()

    def initialize_read_directory_handler(self, treeview_name: str) -> ReadDataDirectory:
        """Initialize the ReadDataDirectory handler with metadata assignment."""
        read_directory_handler = ReadDataDirectory(self.database_handler)
        read_directory_handler.meta_data_assignment_list = [
            [
                "Experiment_name",
                "Experiment_label",
                "Species",
                "Genotype",
                "Sex",
                "Condition",
                "Individuum_id",
            ],
            [treeview_name, "None", "None", "None", "None", "None", "None", "None"],
        ]
        read_directory_handler.meta_data_assigned_experiment_names = [
            "Experiment_name",
            treeview_name,
        ]
        return read_directory_handler

    def handle_heka_file(self, read_directory_handler: ReadDataDirectory, filename_with_extension: str, pathname: str) -> None:
        """Handle loading of HEKA data files."""
        bundle_list = read_directory_handler.single_dat_file_handling(
            filename_with_extension, pathname, InputDataTypes.BUNDLED_HEKA_DATA, []
        )

        if not bundle_list:
            bundle_list = read_directory_handler.single_dat_file_handling(
                filename_with_extension,
                pathname,
                InputDataTypes.UNBUNDLED_HEKA_DATA,
                [],
            )

        self.process_bundle_list(bundle_list, read_directory_handler)

    def process_bundle_list(self, bundle_list: list, read_directory_handler: ReadDataDirectory) -> None:
        """Process the bundle list for HEKA files."""
        match len(bundle_list):
            case 0:
                CustomErrorDialog("Unknown Heka file format", self.frontend_style)
            case 1:
                read_directory_handler.single_file_into_db(
                    [],
                    bundle_list[0][0],
                    self.experiment_name,
                    self.database_handler,
                    bundle_list[0][2],
                    bundle_list[0][3],
                )
            case _:
                CustomErrorDialog(
                    "More than one experiment was detected in your dat file. \n Currently, only single experiments are accepted for online analysis. \n You can read the data in the offline analysis module to continue.",
                    self.frontend_style,
                )

    def handle_abf_file(self, read_directory_handler: ReadDataDirectory, file_name: str) -> None:
        """Handle loading of ABF data files."""
        self.logger.info("ABF File Reading Online Analysis")
        pathname, filename_with_extension = os.path.split(file_name)
        abf_file_list = os.listdir(os.path.dirname(file_name))
        abf_identifier = os.path.basename(file_name).split("_")[0]
        abf_file_data = []

        for abf in abf_file_list:
            if abf_identifier in abf:
                file_2 = os.path.join(pathname, abf)
                abf_file = AbfReader(file_2)
                data_file = abf_file.get_data_table()
                meta_data = abf_file.get_metadata_table()
                pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                experiment_name = [
                    abf_file.get_experiment_name(),
                    "None",
                    "None",
                    "None",
                    "None",
                    "None",
                    "None",
                    "None",
                ]
                series_name = abf_file.get_series_name()
                abf_file_data.append(
                    (data_file, meta_data, pgf_tuple_data_frame, series_name, InputDataTypes.ABF_FILE_ENDING)
                )

        if abf_file_data:
            bundle = [abf_file_data, experiment_name]
            read_directory_handler.single_abf_file_into_db(bundle, self.database_handler)

    def show_file_type_error(self) -> None:
        """Show an error dialog for unsupported file types."""
        CustomErrorDialog(
            "The selected file type is not supported. Supported file types are .dat files and .abf files",
            self.frontend_style,
        )

    def finalize_tree_view_setup(self) -> None:
        """Finalize the setup of the tree view after loading the file."""
        self.online_analysis_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio
        self.online_analysis_tree_view_manager.selected_meta_data_list = ["None"]
        self.online_analysis_tree_view_manager.map_data_to_analysis_id([self.experiment_name])
        self.online_analysis_tree_view_manager.update_treeviews(self.online_analysis_plot_manager)
        self.logger.info("Finished the loading of the file!")
        self.online_analysis.setTabEnabled(1, True)
        self.online_analysis.setTabEnabled(2, True)
        self.online_analysis_tree_view_manager.click_top_level()
        self.online_analysis_config.enable_plot_options()
        self.online_analysis_config.set_enabled_button(True)
        self.labbook.get_columns_data_to_table(self.online_analysis_tree_view_manager)
        self.draw_table(self.labbook.labbook_table)
        self.stackedWidget.setCurrentIndex(0)
        self.logger.info(f"Successfully transferred to online analysis db the file {self.experiment_name}")

    def video_show(self) -> None:
        """Show the video in the graphics view."""

        if self.video_mat is not None:
            self.start_video = QTimer()  # create a timer
            self.start_video.timeout.connect(
                self.run_video
            )  # connect the timer to the start camera function
            self.start_video.start(250)

    def run_video(self) -> None:
        """Play the recorded video/gif in the labbook."""

        self.video_call += 1
        item = self.video_mat[self.video_call]
        self.online_video.clear()  # clear the scene
        self.online_video.addPixmap(item)
        print(self.video_call, len(self.video_mat))
        if len(self.video_mat) - 1 == self.video_call:
            self.start_video.stop()
            self.video_call = 0

    def draw_scene(self, image) -> None:
        """Draw the image into the configuration window.

        Args:
            image (QImage): The image to be drawn.
        """

        self.online_scence = QGraphicsScene(self)
        self.image_experiment.setScene(self.online_scence)  # set the scene to the image
        item = QGraphicsPixmapItem(image)
        self.image_experiment.scene().addItem(item)  #

    # thats refactored
    def draw_table(self, data: pd.DataFrame) -> None:
        """Draw the table of the .dat metadata.

        Args:
            data (pd.DataFrame): The data to be displayed in the table.
        """

        try:
            if self.labbook_table is None:
                self.labbook_table = QTableView()
                self.table_layout.addWidget(self.labbook_table)

            self.labbook_model = PandasTable(data)
            self.labbook_table.setModel(self.labbook_model)
            self.tableView.setModel(self.labbook_model)
            self.labbook_model.resize_header(self.labbook_table)
            self.labbook_model.resize_header(self.tableView)
            self.logger.info(
                f"Successfully generated labbook table for {self.experiment_name}"
            )
        except Exception as e:
            print(f"There is an error in draw_table(online_analysis) {e}")
            self.logger.error(f"""There is an error in draw_table(online_analysis)
                                  for the labbook: {e}  for experiment: {self.experiment_name}
                              """)


class OnlineAnalysisConfig:
    def __init__(
        self,
        online_widget: Online_Analysis,
        online_analysis_plot_manager: PlotWidgetManager,
    ) -> None:
        """Initialize the OnlineAnalysisConfig class."""
        self.online_widget: Online_Analysis = online_widget
        self.online_analysis_plot_manager: PlotWidgetManager = (
            online_analysis_plot_manager
        )
        self.logger = picologging.getLogger(__name__)

    def connections_clicked(self) -> None:
        """Connect the buttons to the corresponding functions."""
        self.logger.info("Connecting the buttons to the corresponding functions")
        button_connections = {
            self.online_widget.button_select_data_file: self.online_widget.open_single_dat_file,
            self.online_widget.online_analysis.currentChanged: self.online_widget.online_analysis_tab_changed,
            self.online_widget.start_video_button: self.online_widget.video_show,
            self.online_widget.transfer_to_offline_analysis: self.online_widget.start_db_transfer,
            self.online_widget.transfer_into_db_button: self.online_widget.transfer_file_and_meta_data_into_db,
            self.online_widget.show_sweeps_radio.toggled: self.online_widget.show_sweeps_toggled,
            self.online_widget.classifier_stream: partial(ConstrcutionSideDialog, self.online_widget.frontend_style),
        }

        for button, method in button_connections.items():
            try:
                button.clicked.connect(method)
            except AttributeError as e:
                button.connect(method)

        self.logger.info("Successfully connected all the appropriate button calls")
        self.set_enabled_button()

    def enable_plot_options(self) -> None:
        """Enable plot options in the online analysis."""
        if self.online_widget.online_analysis_plot_manager:
            self.logger.info("Enabling the plot options")
            navigation = NavigationToolbar(
                self.online_widget.online_analysis_plot_manager.canvas,
                self.online_widget,
            )
            self.online_widget.plot_move.clicked.connect(navigation.pan)
            self.online_widget.plot_zoom.clicked.connect(navigation.zoom)
            self.online_widget.plot_home.clicked.connect(navigation.home)

    def set_enabled_button(self, enabled: bool = False) -> None:
        """Set the enabled state of various buttons."""
        self.logger.info("Setting the enabled button")
        buttons = [
            self.online_widget.plot_move,
            self.online_widget.plot_home,
            self.online_widget.plot_zoom,
            self.online_widget.save_image,
            self.online_widget.classifier_stream,
            self.online_widget.add_metadata_button,
            self.online_widget.save_labbook_button,
            self.online_widget.start_video_button,
            self.online_widget.edit_meta,
            self.online_widget.renameSeries,
            self.online_widget.show_pgf_file,
            self.online_widget.transfer_to_offline_analysis,
            self.online_widget.save_plot_online,
        ]

        for button in buttons:
            button.setEnabled(enabled)

    def reset_class(self) -> None:
        """Reset the class to its base state for reuse."""
        self.logger.info(
            f"Resetting class after submitting {self.online_widget.experiment_name} to Offline DB"
        )
        self._clear_file_queue()
        self._reset_database()
        self._clear_table_layout()
        self._reset_widget_states()

        if self.online_widget.file_queue:
            self.logger.info("Updating the View using the next member in the viewing list")
            self.online_widget.open_single_dat_file(self.online_widget.file_queue[0])
            self.logger.info("Successfully updated the view")
        else:
            self.online_widget.stackedWidget.setCurrentIndex(1)
            self.online_widget.online_analysis_config.set_enabled_button()

    def _clear_file_queue(self) -> None:
        """Clear the file queue."""
        try:
            self.online_widget.file_queue.pop(0)
        except IndexError:
            self.logger.warning("No data was found in the queue list, it was empty")

    def _reset_database(self) -> None:
        """Reset the database connection."""
        try:
            self.online_widget.database_handler.database.close()
            self.online_widget.database_handler.database, _ = DuckDBInitializer(
                self.logger,
                "online_analysis",
                in_memory=True,
                database_path="./database/",
            ).init_database()
            self._clear_tree_view_and_plot_manager()
        except Exception as e:
            self.logger.error("Error in reset class function: %s", str(e))

    def _clear_tree_view_and_plot_manager(self) -> None:
        """Clear the tree view and plot manager."""
        if self.online_widget.online_analysis_tree_view_manager is not None:
            self.online_widget.online_analysis_tree_view_manager.clear_tree()
        if self.online_widget.online_analysis_plot_manager is not None:
            self.online_widget.online_analysis_plot_manager.canvas.figure.clf()
            self.online_widget.online_analysis_plot_manager.canvas.draw_idle()

    def _clear_table_layout(self) -> None:
        """Clear the table layout."""
        for i in reversed(range(self.online_widget.table_layout.count())):
            self.online_widget.table_layout.itemAt(i).widget().deleteLater()

    def _reset_widget_states(self) -> None:
        """Reset the widget states to their original state."""
        self.online_widget.labbook_table = None
        self.online_widget.data_model_list = None
        self.online_widget.transferred = False
        self.online_widget.experiment_name = "no_name"
        self.online_widget.video_mat = None
        self.online_widget.image = None
        self.online_widget.video_call = 0  # number of frames went through

        if self.online_widget.online_analysis.currentIndex() != 0:
            self.online_widget.online_analysis.setCurrentIndex(0)

        # Disable the labbook tabs as long as no new analysis is loaded
        self.online_widget.online_analysis.setTabEnabled(1, False)
        self.online_widget.online_analysis.setTabEnabled(2, False)
