from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_dialog import Ui_MetadataPopup
from functools import partial
from CustomWidget.Pandas_Table import PandasTable
import os
from database.ExportAnalysis import ExportOfflineAnalysis
from Offline_Analysis.error_dialog_class import CustomErrorDialog


class ExportOfflineDialog(QDialog, Ui_MetadataPopup):

    def __init__(self,database_handler, frontend, export = False,  parent=None):
        """_summary_

        Args:
            database_handler (_type_): _description_
            frontend (_type_): _description_
            export (bool, optional): _description_. Defaults to False.
            parent (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.frontend_style = frontend
        self.file_name: str = os.getcwd()
        self.database_handler = database_handler
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.offline_analysis_id = None
        self.stackedWidget.setCurrentIndex(1)
        # show here the appropriate table
        data = self.database_handler.database.execute('SELECT * FROM analysis_functions LEFT JOIN analysis_series ON (analysis_functions.analysis_id = analysis_series.analysis_id AND analysis_functions.analysis_series_name = analysis_series.analysis_series_name)').fetchdf()
        data = data.drop(["time", "analysis_series_name_2","analysis_function_id","analysis_id_2","lower_bound","upper_bound"], axis = 1)
        ids = {str(i) for i in data["analysis_id"].tolist()}
        self.comboBox.addItems(ids)
        table_model = PandasTable(data)
        self.tableView_2.setModel(table_model)
        table_model.resize_header(self.tableView_2)
        self.SetPath.clicked.connect(self.open_path_dialog)
        self.ExportDb.clicked.connect(self.export_database)
        self.exec()

    def open_path_dialog(self):
        """_summary_: Sets the path for the new exported database
        """
        self.file_name = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.Path.setText(self.file_name)

    def export_database(self):
        """_summary_: Controller to export the selected Offline Analysis ID as own DuckDB database for sharing
        """
        text = int(self.comboBox.currentText())
        export = ExportOfflineAnalysis(self.database_handler, text, self.file_name)
        export.create_new_database()
        export.add_tables_to_database()
        CustomErrorDialog("The Offline Analysis ID was successfully exported!", self.frontend_style)
        

    
