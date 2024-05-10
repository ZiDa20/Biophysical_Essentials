
from PySide6.QtWidgets import *  # type: ignore

from Frontend.OfflineAnalysis.CustomWidget.select_statistics_meta_data_dialog import StatisticsMetaData_Dialog


class StatisticsMetaData_Handler(QDialog, StatisticsMetaData_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
