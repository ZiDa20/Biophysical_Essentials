from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter,QColor, QStyle
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionButton, QPushButton, QTreeView

class CancelButtonDelegate(QStyledItemDelegate):
    
    def __init__(self, parent=None):
        super(CancelButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 2:  # assuming the pixmap will be in the last column
            pixmap = QPixmap(r"../QT_GUI/Button/light_mode/offline_analysis/treeview_delete.png")
            if not pixmap.isNull():
                #painter.save()
                size = pixmap.size().scaled(20, 20, Qt.KeepAspectRatio)
                x = option.rect.x() + (option.rect.width() - size.width()) / 2
                y = option.rect.y() + (option.rect.height() - size.height()) / 2
                if option.state & QStyle.State_MouseOver:
                    painter.save()
                    painter.setBrush(QColor("#5b6e8b"))
                    painter.setPen(Qt.NoPen)
                    painter.drawRect(option.rect)
                    painter.restore()

                painter.drawPixmap(x, y, size.width(), size.height(), pixmap.scaled(size, Qt.KeepAspectRatio))
                #painter.restore()
        else:
            super(CancelButtonDelegate, self).paint(painter, option, index)

    def sizeHint(self, option, index):
        if index.column() == 2:
            return QSize(20, 20)
        else:
            return super(CancelButtonDelegate, self).sizeHint(option, index)