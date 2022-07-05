
from PySide6.QtWidgets import *  # type: ignore

from filter_pop_up import Ui_FilterSettings
from BlurWindow.blurWindow import GlobalBlur


class Filter_Settings(QDialog, Ui_FilterSettings):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        GlobalBlur(self.winId(), Acrylic=True)
        
