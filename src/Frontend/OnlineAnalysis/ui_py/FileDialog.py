import re
from typing import TYPE_CHECKING

import pandas as pd
import picologging
from PySide6.QtWidgets import (  # type: ignore
    QDialog,
    QFileDialog,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QTableView,
    QGroupBox,
    QHeaderView,
    QLabel,
)

from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from Frontend.CustomWidget.Pandas_Table import CheckableTableModel
from Frontend.OnlineAnalysis.ui_py.RedundantDialog import RedundantDialog

if TYPE_CHECKING:
    from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
    from StyleFrontend.frontend_style import Frontend_Style


class FileDialog_Base():
    def setup_ui(self, FileDialog: QDialog) -> None:
        FileDialog.setWindowTitle("File Selection")
        # Set minimum size
        FileDialog.setMinimumSize(800, 400)
        self.grid_layout: QGridLayout = QGridLayout()
        self.horizontal_layout: QHBoxLayout = QHBoxLayout()
        
        # Add spacing between the button and input field
        self.selectFileButton: QPushButton = QPushButton("Select a File")
        self.label = QLabel("File Path:")
        self.openFileButton: QPushButton = QPushButton("Proceed to Viewer")
        self.fileNameInput: QLineEdit = QLineEdit()
        self.horizontal_layout.addWidget(self.label)
        self.horizontal_layout.addWidget(self.fileNameInput)
        self.horizontal_layout.addWidget(self.selectFileButton)
        self.horizontal_layout.addSpacing(10)  # Add spacing of 10 pixels

        # Create a table widget and add it to the layout
        self.table_layout = QVBoxLayout()
        self.group_box = QGroupBox("Existing Experiments")
        self.table_widget = QTableView()
        self.table_layout.addWidget(self.table_widget)# Create the table widget
        self.group_box.setLayout(self.table_layout)
        self.grid_layout.addLayout(self.horizontal_layout, 0, 0)  # Add horizontal layout to grid layout at row 0, column 0
        self.grid_layout.addWidget(self.group_box, 1, 0)
        self.grid_layout.addWidget(self.openFileButton, 2, 0)
        FileDialog.setLayout(self.grid_layout)


class FileDialog(QDialog, FileDialog_Base):
    def __init__(
        self,
        database_handler: "DuckDBDatabaseHandler",
        frontend_style: "Frontend_Style",
        parent=None,
    ):
        super().__init__(parent)
        self.setup_ui(self)
        self.logger: picologging.Logger = picologging.getLogger(__name__)
        self.database_handler: "DuckDBDatabaseHandler" = database_handler
        #self.online_widget: "OnlineAnalysisWidget" = online_widget
        self.frontend_style: "Frontend_Style" = frontend_style
        self.table_model = CheckableTableModel(self.database_handler.database.execute("select * from experiments").fetchdf())
        self.table_widget.setModel(self.table_model)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        # Connect buttons to their respective methods
        self._file_path: str | None = None
        self._treeview_name : str | None = None
        self._file_name : str | None = None

        # Layout setup
        self.selectFileButton.clicked.connect(self.select_file) 
        self.openFileButton.clicked.connect(self.open_file) 
  
        
    @property
    def treeview_name(self):
        return self._treeview_name
    
    @treeview_name.setter
    def treeview_name(self, treeview_name: str):
        self._treeview_name = treeview_name
        
    @property
    def file_name(self):
        return self._file_name
    
    @file_name.setter
    def file_name(self, file_name: str):
        self._file_name = file_name
        
    @property
    def file_path(self):
        return self._file_path
    
    @file_path.setter
    def file_path(self, file_path: str):
        self._file_path = file_path
        
    def select_file(self):
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
        
        self.file_path = file_name
        self.treeview_name = treeview_name
        self.fileNameInput.setText(file_name)


    def open_file(self, file_name: str | None = None):
        # Logic to open a file from a path
        if self.treeview_name is not None and not self.check_if_experiments_exist_online(self.treeview_name).empty:
            self.logger.info(f"""file already exists within the offline analysis
                                database with name {self.treeview_name}, Start redundancy check""")
            redundant = RedundantDialog(
                self.database_handler, self.treeview_name, self.logger
            )
            self.frontend_style.set_pop_up_dialog_style_sheet(redundant)
            result = redundant.exec_()
            if result == 0:
                return None
            self.treeview_name = redundant.new_treeview_name
            self.logger.info(f"Data was renamed to {self.treeview_name}")

        if file_name:
            self.treeview_name = file_name
            
        self.close()

    def check_if_experiments_exist_online(self, treeview_name: str) -> pd.DataFrame:
        """Check if there is an existing table in the database with the same name as the new experiment.

        Args:
            treeview_name (str): The initial name of the experiment.

        Returns:
            pd.DataFrame: DataFrame holding all experiments with the same name.
        """

        q = f"select * from experiments where experiment_name = '{treeview_name}'"
        df = self.database_handler.database.execute(q).fetchdf()
        self.logger.info("This is the current name of the file: {treeview_name}")
        return df
    
    
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


    def openDatabase(self):
        # Logic to open a database and select an experiment
        print("here we open the database")


