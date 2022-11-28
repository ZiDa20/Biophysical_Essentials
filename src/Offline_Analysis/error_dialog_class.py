from PySide6.QtCore import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from functools import partial
class CustomErrorDialog():

    def show_dialog(self, message):
        # @todo: make this a reusable function: show_error_dialog(message)
        dialog = QDialog()
        # dialog.setWindowFlags(Qt.FramelessWindowHint)
        dialog_grid = QGridLayout(dialog)
        # series_names_string_list = ["Block Pulse", "IV"]
        dialog_quit = QPushButton("Cancel", dialog)
        dialog_message = QLabel(dialog)
        dialog_message.setText(message)
        dialog_grid.addWidget(dialog_message)
        dialog_grid.addWidget(dialog_quit)
        dialog_quit.clicked.connect(partial(self.quit_error_dialog, dialog))
        dialog.setWindowTitle("Error")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def quit_error_dialog(self,dialog):
        dialog.close()