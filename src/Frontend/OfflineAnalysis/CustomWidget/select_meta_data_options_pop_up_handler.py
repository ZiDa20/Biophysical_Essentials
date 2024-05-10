
from PySide6.QtWidgets import *  # type: ignore

from Frontend.OfflineAnalysis.CustomWidget.select_meta_data_options_pop_up import Ui_Dialog


class Select_Meta_Data_Options_Pop_Up(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
