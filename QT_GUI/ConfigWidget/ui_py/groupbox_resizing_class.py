
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class GroupBoxSize(QGroupBox):
    """This class provides an interface for resizing GroupBoxes"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.startPos = self.section = None
        self.rects = {section:QtCore.QRect() for section in self.sections}

        # mandatory for cursor updates
        self.setMouseTracking(True)

    def updateCursor(self, pos):
        for section, rect in self.rects.items():
        if pos in rect:
            self.setCursor(self.cursors[section])
            self.section = section
            return section
        self.unsetCursor()

    def adjustSize(self):
            del self._sizeHint
            super().adjustSize()

    def minimumSizeHint(self):
        try:
            return self._sizeHint
        except:
            return super().minimumSizeHint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.updateCursor(event.pos()):
                self.startPos = event.pos()
                return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            delta = event.pos() - self.startPos
            if self.section & Left:
                delta.setX(-delta.x())
            elif not self.section & (Left|Right):
                delta.setX(0)
            if self.section & Top:
                delta.setY(-delta.y())
            elif not self.section & (Top|Bottom):
                delta.setY(0)
            newSize = QtCore.QSize(self.width() + delta.x(), self.height() + delta.y())
            self._sizeHint = newSize
            self.startPos = event.pos()    
            self.updateGeometry()
        elif not event.buttons():
            self.updateCursor(event.pos())
        super().mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.updateCursor(event.pos())
        self.startPos = self.section = None
        self.setMinimumSize(0, 0)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        outRect = self.rect()
        inRect = self.rect().adjusted(self.resizeMargin, self.resizeMargin, -self.resizeMargin, -self.resizeMargin)
        self.rects[Left] = QtCore.QRect(outRect.left(), inRect.top(), self.resizeMargin, inRect.height())
        self.rects[TopLeft] = QtCore.QRect(outRect.topLeft(), inRect.topLeft())
        self.rects[Top] = QtCore.QRect(inRect.left(), outRect.top(), inRect.width(), self.resizeMargin)
        self.rects[TopRight] = QtCore.QRect(inRect.right(), outRect.top(), self.resizeMargin, self.resizeMargin)
        self.rects[Right] = QtCore.QRect(inRect.right(), self.resizeMargin, self.resizeMargin, inRect.height())
        self.rects[BottomRight] = QtCore.QRect(inRect.bottomRight(), outRect.bottomRight())
        self.rects[Bottom] = QtCore.QRect(inRect.left(), inRect.bottom(), inRect.width(), self.resizeMargin)
        self.rects[BottomLeft] = QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized()
    