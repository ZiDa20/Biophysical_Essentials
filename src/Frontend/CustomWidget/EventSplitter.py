
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class MySplitter(QSplitter):
    def __init__(self, orientation):
        super().__init__(orientation)

    def eventFilter(self, obj, event):
        print(self.size())
        print(event.type())
        if event.type() == QEvent.Type.MouseButtonRelease:
            # do something with the mouse release event here
            print("Mouse released on splitter")

            # return True to filter the event and prevent it from being propagated
            return True

        # return False to allow the event to be propagated
        return False
