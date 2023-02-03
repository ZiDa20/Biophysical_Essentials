from PySide6.QtWidgets import *  # type: ignore

from QT_GUI.OfflineAnalysis.CustomWidget.ui_substract_dialog import Ui_CreateNewSeries


class SubstractDialog(Ui_CreateNewSeries):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


    