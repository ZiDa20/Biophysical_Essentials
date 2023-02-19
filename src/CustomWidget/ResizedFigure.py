
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class ResizeFigure(FigureCanvas):
    """ Subclass canvas to catch the resize event """
    def __init__(self, figure):
        self.lastEvent = False # store the last resize event's size here
        super.__init__()

    def resizeEvent(self, event):
        if not self.lastEvent:
            # at the start of the app, allow resizing to happen.
            super().resizeEvent(event)
        # store the event size for later use
        self.lastEvent = (event.size().width(),event.size().height())
        print("try to resize, I don't let you.")

    def do_resize_now(self):
        # recall last resize event's size
        newsize = QSize(self.lastEvent[0],self.lastEvent[1] )
        # create new event from the stored size
        event = QResizeEvent(newsize, QSize(1, 1))
        # and propagate the event to let the canvas resize.
        super().resizeEvent(event)
