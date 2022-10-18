

from PySide6.QtWidgets import *  # type: ignore

from load_data_from_database_popup import Ui_Dialog

class Load_Data_From_Database_Popup_Handler(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #GlobalBlur(self.winId(), Acrylic=True)
