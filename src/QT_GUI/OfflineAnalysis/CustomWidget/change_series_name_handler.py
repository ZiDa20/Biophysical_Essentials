from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.change_series_name_designer import Ui_Dialog
from functools import partial

class ChangeSeriesName(QDialog, Ui_Dialog):

    def __init__(self,database_handler, frontend, parent=None):

        self.database_handler = database_handler
        self.frontned = frontend

        self.fill_combobox()


    def fill_combobox(self):
    