
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up import Ui_FilterSettings

class Filter_Settings(QDialog, Ui_FilterSettings):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        
