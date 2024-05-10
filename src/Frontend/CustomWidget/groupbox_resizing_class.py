from PySide6.QtCore import *
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class GroupBoxSize(QGroupBox):
    def __init__(self, parent=None):
    
        super(GroupBoxSize, self).__init__(parent)
        self.__mouseMovePos = None
        self.setMouseTracking(True)
        self._triangle = QPolygon()
        self.start_pos = None

    def _recalculate_triangle(self):
        """Function to draw the button triangle to the groupbox"""
        p = QPoint(self.width() - 20, self.height() - 10)
        q = QPoint(self.width() - 10, self.height() - 20)
        r = QPoint(self.width() - 10, self.height() - 10)
        self._triangle = QPolygon([p, q, r])
        self.update()

    def resizeEvent(self, event):
        """should initialized the resizing after the event"""
        self._recalculate_triangle()
        super().resizeEvent(event)
        

    def paintEvent(self, event):
        super(GroupBoxSize, self).paintEvent(event)
        qp = QPainter(self)
        qp.setPen(Qt.white)
        qp.setBrush(Qt.red)
        qp.drawPolygon(self._triangle)

    """"
    def minimumSizeHint(self):
        try:
            #self.adjustSize()
            #self._sizeHint = QSize(50,50)
            return self._sizeHint
        
        except Exception as e:
            return super().minimumSizeHint()
    """
    def adjustSize(self):
        del self._sizeHint
        super().adjustSize()

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:

            if event.button() == Qt.LeftButton and self._triangle.containsPoint(
                    event.pos(), Qt.OddEvenFill
            ):
                self.setCursor(Qt.SizeFDiagCursor)
                self.start_pos = event.pos()

        super().mousePressEvent(event)
        
    def mouseMoveEvent(self, event):
        if self._triangle.containsPoint(event.pos(), Qt.OddEvenFill):
            self.setCursor(Qt.SizeFDiagCursor)

        else:
            self.unsetCursor()

        if event.buttons() == Qt.LeftButton:

            if event.buttons() == Qt.LeftButton and self.start_pos is not None:

                self.setCursor(Qt.SizeFDiagCursor)

                delta = event.pos() - self.start_pos

                self._sizeHint = QSize(self.width() + delta.x(), self.height() + delta.y())
                self.resize(self.width() + delta.x(), self.height() + delta.y())
                self.start_pos = event.pos()
                self.updateGeometry()

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        self.start_pos = None
        super().mouseReleaseEvent(event)