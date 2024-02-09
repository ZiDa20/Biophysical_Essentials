from Frontend.CustomWidget.ui_LoadingDialog import Ui_LoadingDialog
from PySide6.QtWidgets import *  # type: ignore

class LoadingDialog(Ui_LoadingDialog):
    
    def __init__(self,wait_widget, frontend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.wait_widget = wait_widget
        self.frontend_style = frontend
        self.loading_dialog.addWidget(self.wait_widget)
        self.loading_dialog.addWidget(QPushButton("hello"))
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.show()
    