import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class PlotClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.plotWidget = pg.PlotWidget()
        


    
