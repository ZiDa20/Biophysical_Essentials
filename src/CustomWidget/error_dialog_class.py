from PySide6.QtCore import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from functools import partial

class CustomErrorDialog():

    def __init__(self, message, frontend_style):
        self.dialog_grid = None
        self.frontend_style = frontend_style
        self.show_dialog(message)

    def show_dialog(self, message):
        # @todo: make this a reusable function: show_error_dialog(message)
        dialog = QDialog()
        # dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.dialog_grid = QGridLayout(dialog)
        # series_names_string_list = ["Block Pulse", "IV"]
        dialog_quit = QPushButton("Cancel", dialog)
        dialog_message = QLabel(dialog)
        dialog_message.setText(message)
        self.dialog_grid.addWidget(dialog_message)
        self.dialog_grid.addWidget(dialog_quit)
        dialog_quit.clicked.connect(partial(self.quit_error_dialog, dialog))
        dialog.setWindowTitle("Error")
        dialog.setWindowModality(Qt.ApplicationModal)
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)
        dialog.exec_()

    def quit_error_dialog(self,dialog):
        dialog.close()