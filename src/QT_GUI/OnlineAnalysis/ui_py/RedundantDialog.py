
from PySide6.QtWidgets import QDialog  # type: ignore
from QT_GUI.OnlineAnalysis.ui_py.ui_RedundantDialog import Ui_RedundantDialog


class RedundantDialog(QDialog, Ui_RedundantDialog):
    def __init__(self, offline_database, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.offline_database = offline_database

