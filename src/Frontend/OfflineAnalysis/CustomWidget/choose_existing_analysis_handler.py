from PySide6.QtWidgets import *  # type: ignore
from Frontend.OfflineAnalysis.CustomWidget.choose_existing_analysis_dialog import Ui_MetadataPopup
from functools import partial
from Frontend.CustomWidget.Pandas_Table import PandasTable
import duckdb
from pathlib import Path
from natsort import natsorted

class ChooseExistingAnalysis(QDialog, Ui_MetadataPopup):

    def __init__(self,database_handler, frontend,  parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.frontend_style = frontend
        self.database_handler = database_handler
        self.tableView = QTableView()
        self.final_table_layout.addWidget(self.tableView)
        self.loaded_function_run = None
        
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.popup_stacked.setCurrentIndex(0)
        data = self.get_analysis_function_id_dataset()
        self.table_model = PandasTable(data)
        self.tableView.setModel(self.table_model)
        self.table_model.resize_header(self.tableView)



        self.SelectDB.clicked.connect(self.open_path_dialog)
        self.OfflineAnalysisID.setMinimumWidth(100)
        self.OfflineAnalysisID.activated.connect(self.change_current_offline_analysis_id)

    def change_current_offline_analysis_id(self):
        self.offline_analysis_id = int(self.OfflineAnalysisID.currentText())

    @property
    def offline_analysis_id(self):
        """_summary_: Getter for the offlne_analysis

        Returns:
            int: OfflineAnalysisID
        """
        print("This is the current offline_analysis_id: ", self._offline_analysis_id)
        return self._offline_analysis_id
    
    @offline_analysis_id.setter
    def offline_analysis_id(self, value):
        """_summary_: Offline_Analysis_ID setter

        Args:
            value (int): new offline_analysis_id
        """
        print("setting offline_analysis id to: ", value)
        self._offline_analysis_id = value

    def get_analysis_function_id_dataset(self):
        """_summary_: This should retrieve the analysis_function data as well as the offline_analysis IDs for selection!
        """
        data = self.database_handler.database.execute("""SELECT * FROM analysis_functions LEFT JOIN analysis_series ON 
                                                        (analysis_functions.analysis_id = analysis_series.analysis_id AND 
                                                        analysis_functions.analysis_series_name = analysis_series.analysis_series_name)""").fetchdf()
        

        trial = self.database_handler.database.execute("Select * from analysis_series").fetchdf()
        data = data.drop(["time", "analysis_series_name_2","analysis_function_id","analysis_id_2","lower_bound","upper_bound"], axis = 1)
        ids = natsorted(list({str(i) for i in data["analysis_id"].tolist()}), reverse = True)

        self.OfflineAnalysisID.clear()
        self.OfflineAnalysisID.addItems(ids)

        try:
            self.offline_analysis_id = int(self.OfflineAnalysisID.currentText())
        except ValueError as e:
            self.offline_analysis_id = self.database_handler.analysis_id

        return data

    def open_path_dialog(self):
        """_summary_: Sets the path for the new exported database
        """
        filename, _ = QFileDialog.getOpenFileName(None, "Open file", "", "DB files (*.db)")
        self.filename = str(Path(filename))
        self.open_database()
        

    def open_database(self):
        """_summary_:Opens the newly selected database and sets it to be the main database of the data db class
        """
        self.import_db = duckdb.connect(self.filename, read_only=False)
        self.database_handler.database = self.import_db
        self.database_handler.database_path = self.filename
        data = self.get_analysis_function_id_dataset()
        self.table_model.update_data(data)

    
        
    
