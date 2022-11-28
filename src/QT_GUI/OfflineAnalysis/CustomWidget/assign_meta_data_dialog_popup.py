
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_group_dialog import Ui_assign_meta_data_group

class Assign_Meta_Data_PopUp(QDialog, Ui_assign_meta_data_group):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



