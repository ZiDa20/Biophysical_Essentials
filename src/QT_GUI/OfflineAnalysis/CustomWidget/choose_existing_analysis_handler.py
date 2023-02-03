from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.choose_existing_analysis_dialog import Ui_MetadataPopup

class ChooseExistingAnalysis(QDialog, Ui_MetadataPopup):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
