
from PySide6.QtWidgets import *  # type: ignore
<<<<<<< HEAD:src/QT_GUI/OfflineAnalysis/CustomWidget/assign_meta_data_dialog_popup.py
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_group_dialog import Ui_Dialog
=======
from assign_meta_data_group_dialog import Ui_assign_meta_data_group
>>>>>>> origin/meta_data_and_statistics:QT_GUI/OfflineAnalysis/CustomWidget/assign_meta_data_dialog_popup.py

class Assign_Meta_Data_PopUp(QDialog, Ui_assign_meta_data_group):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



