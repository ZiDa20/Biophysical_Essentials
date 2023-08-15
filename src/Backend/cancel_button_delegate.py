from PySide6.QtCore import QSize
from PySide6.QtWidgets import QStyledItemDelegate, QTreeView, QStyle
from PySide6.QtGui import QPixmap, QColor, Qt
from PySide6.QtCore import QSize

class CancelButtonDelegate(QStyledItemDelegate):
    """_summary_
    Class handler to create the remove and reinsert icon within the treeview
    Args:
        QStyledItemDelegate (_type_): _description_
    """
    def __init__(self, parent:QTreeView, delete:bool, col_count:int, frontend_style:int):
        self.delete = delete
        self.col_count = col_count
        self.frontend_style = frontend_style

        super(CancelButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == self.col_count:  # assuming the pixmap will be in the last column
            if self.delete & self.frontend_style == 1:
                pixmap = QPixmap(r"../QT_GUI/Button/light_mode/offline_analysis/treeview_delete.png")
            if self.delete & self.frontend_style == 0:
                pixmap = QPixmap(r"../QT_GUI/Button/dark_mode/offline_analysis/treeview_delete.png")
            if self.delete==False & self.frontend_style == 1:
                pixmap = QPixmap(r"../QT_GUI/Button/light_mode/offline_analysis/treeview_reinsert.png")
            if self.delete==False & self.frontend_style == 0:
                pixmap = QPixmap(r"../QT_GUI/Button/dark_mode/offline_analysis/treeview_reinsert.png")

            if not pixmap.isNull():
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
        if index.column() == self.col_count:
            return QSize(20, 20)
        else:
            return super(CancelButtonDelegate, self).sizeHint(option, index)