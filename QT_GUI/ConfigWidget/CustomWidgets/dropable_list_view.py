from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class ListView(QListView):
    """Class to promote a List Widget where you can drop something in
    Author:"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setModel(QStandardItemModel(0, 1))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(ListView, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(ListView, self).dragMoveEvent(event)

    def dropEvent(self, event):
        #global itemModel
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.path()[-5:]==".pcap":
                    if itemModel.findItems(url.path()[1:].replace("/","\\")):
                        pass
                    else:
                        item=QStandardItem(url.path()[1:].replace("/","\\"))
                        item.setCheckable(True)
                        itemModel.appendRow(item)
                else:
                    pass
            event.acceptProposedAction()
            self.setModel(itemModel)
        else:
            super(ListView,self).dropEvent(event)