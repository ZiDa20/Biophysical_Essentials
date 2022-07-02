
from PySide6.QtWidgets import *  # type: ignore

from add_new_meta_data_group_pop_up import Ui_Dialog


class Add_New_Meta_Data_Group_Pop_Up_Handler(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
