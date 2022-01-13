
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class BlurLabel(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        print("setting widget color")
        self.setAttribute(Qt.WA_StyledBackground)

       