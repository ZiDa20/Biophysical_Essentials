
from PySide6.QtWidgets import *  # type: ignore

from assign_meta_data_group_dialog import Ui_Dialog
from BlurWindow.blurWindow import GlobalBlur


class Assign_Meta_Data_PopUp(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #GlobalBlur(self.winId(), Acrylic=True)


