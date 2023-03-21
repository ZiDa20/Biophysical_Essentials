from PySide6.QtCore import QSize
from PySide6.QtWidgets import QGraphicsView
from matplotlib.backends.backend_qt5agg import FigureCanvas

class MyFigureCanvas(FigureCanvas):
    """ Subclass canvas to catch the resize event """
    def __init__(self, figure):
        self.lastEvent = False # store the last resize event's size here
        super().__init__(figure)

    def resizeEvent(self, event):
        if not self.lastEvent:
            # at the start of the app, allow resizing to happen.
            print("donot enter again")
            super().resizeEvent(event)
            self.draw()
            # flush the GUI events
        # store the event size for later use
        self.lastEvent = (event.size().width(),event.size().height())
        self.do_resize_now(event)
    
    def do_resize_now(self, event):
        # recall last resize event's size
        newsize = QSize(self.lastEvent[0],self.lastEvent[1] )
        # create new event from the stored size
        print("Now I let you resize.")
        # and propagate the event to let the canvas resize.
        super().resizeEvent(event)
