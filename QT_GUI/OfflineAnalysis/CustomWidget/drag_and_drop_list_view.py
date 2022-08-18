import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class DragAndDropListView(QListWidget):

    fileDropped = Signal(str)

    def __init__(self, type, initial_list, parent=None):
        super(DragAndDropListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QSize(72, 72))
        self.initial_list = initial_list


    def dragEnterEvent(self, event):
        if not event.mimeData().hasText():
            print(self.initial_list.currentIndex().data())
            event.mimeData().setText(self.initial_list.currentIndex().data())
            print("added text")
            #print(self.currentIndex().data())
        event.accept()


    def dragMoveEvent(self, event):
        if event.mimeData().hasText():
            #print("drag move found text")
            #print(event.mimeData().text())
            #self.insertPlainText(text)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            #print("drop event found text")
            #print(event.mimeData().text())
            event.accept()
            self.fileDropped.emit(event.mimeData().text())
        else:
            event.ignore()