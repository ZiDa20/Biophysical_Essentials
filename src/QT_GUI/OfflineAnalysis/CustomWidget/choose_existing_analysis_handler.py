from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_dialog import Ui_MetadataPopup
from functools import partial
from CustomWidget.Pandas_Table import PandasTable
class ChooseExistingAnalysis(QDialog, Ui_MetadataPopup):

    def __init__(self,database_handler, frontend, function_call,  parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.frontend_style = frontend
        self.database_handler = database_handler
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
       
        self.stackedWidget.setCurrentIndex(0)
        data = self.database_handler.database.execute("""SELECT * FROM analysis_functions LEFT JOIN analysis_series ON 
                                                        (analysis_functions.analysis_id = analysis_series.analysis_id AND 
                                                        analysis_functions.analysis_series_name = analysis_series.analysis_series_name)""").fetchdf()
        
        data = data.drop(["time", "analysis_series_name_2","analysis_function_id","analysis_id_2","lower_bound","upper_bound"], axis = 1)
        print(data)
        table_model = PandasTable(data)
        self.tableView.setModel(table_model)
        table_model.resize_header(self.tableView)
        self.submit.clicked.connect(partial(function_call, self))
        self.exec()
        
    
