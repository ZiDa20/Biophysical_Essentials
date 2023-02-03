from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_dialog import Ui_MetadataPopup
from functools import partial
from Pandas_Table import PandasTable
class ChooseExistingAnalysis(QDialog, Ui_MetadataPopup):

    def __init__(self, frontend,function_call, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        data = self.database_handler.database.execute('select * from offline_analysis').fetchdf()
        table_model = PandasTable(data)
        self.tableView.setModel(table_model)
        self.submit.clicked.connect(partial(function_call, self))
        
    
