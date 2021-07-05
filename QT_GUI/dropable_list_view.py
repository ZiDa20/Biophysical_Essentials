from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class ListView(QListView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setModel(QStandardItemModel(0, 1))

    def dragEnterEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()

    def dragMoveEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            self.model().appendRow(QStandardItem(event.mimeData().text()))
            event.accept()
        else:
            event.ignore()
