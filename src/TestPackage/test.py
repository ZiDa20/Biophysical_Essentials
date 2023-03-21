

import matplotlib.pyplot as plt

# Create a figure and set the title
fig, ax = plt.subplots()
#fig.canvas.set_window_title('Click on a rectangle')

# Create three white rectangles with grey frames and labels
rect1 = plt.Rectangle((0.1, 0.7), 0.2, 0.1, facecolor='w', edgecolor='grey', alpha=1,label='Section 1')
rect2 = plt.Rectangle((0.4, 0.7), 0.2, 0.1, facecolor='w', edgecolor='grey', alpha=1,label='Section 2')
rect3 = plt.Rectangle((0.7, 0.7), 0.2, 0.1, facecolor='w', edgecolor='grey', alpha=1,label='Section 3')

# Add the rectangles to the plot
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)

# Add the labels as text inside the rectangles
text1 = ax.text(0.2, 0.75, 'Section 1', fontsize=10, ha='center', va='center')
text2 = ax.text(0.5, 0.75, 'Section 2', fontsize=10, ha='center', va='center')
text3 = ax.text(0.8, 0.75, 'Section 3', fontsize=10, ha='center', va='center')



# Variable to keep track of the currently clicked rectangle
clicked_rect = None

# Function to be called when a rectangle is clicked
def onclick(event):
    global clicked_rect
    # Find which rectangle was clicked
    for rect, text in [[rect1, text1], [rect2, text2], [rect3, text3]]:

        if rect.contains(event)[0]:
            # Set the color of the clicked rectangle to red and the others to white
            print(rect1.get_label())
            rect1.set_facecolor('w')
            rect2.set_facecolor('w')
            rect3.set_facecolor('w')
            rect.set_facecolor('red')
            plt.draw()
            print(f'Clicked on rectangle with label: {text.get_text()}')
            break

# Connect the onclick function to the figure
fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()


"""
import random
from PySide2 import QtCore, QtGui, QtWidgets


class SlidingStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(SlidingStackedWidget, self).__init__(parent)

        self.m_direction = QtCore.Qt.Horizontal
        self.m_speed = 500
        self.m_animationtype = QtCore.QEasingCurve.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False

    def setDirection(self, direction):
        self.m_direction = direction

    def setSpeed(self, speed):
        self.m_speed = speed

    def setAnimation(self, animationtype):
        self.m_animationtype = animationtype

    def setWrap(self, wrap):
        self.m_wrap = wrap

    @QtCore.Slot()
    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)

    @QtCore.Slot()
    def slideInNext(self):
        now = self.currentIndex()
        if self.m_wrap or now < (self.count() - 1):
            self.slideInIdx(now + 1)

    def slideInIdx(self, idx):
        if idx > (self.count() - 1):
            idx = idx % self.count()
        elif idx < 0:
            idx = (idx + self.count()) % self.count()
        self.slideInWgt(self.widget(idx))

    def slideInWgt(self, newwidget):
        if self.m_active:
            return

        self.m_active = True

        _now = self.currentIndex()
        _next = self.indexOf(newwidget)

        if _now == _next:
            self.m_active = False
            return

        offsetx, offsety = self.frameRect().width(), self.frameRect().height()
        self.widget(_next).setGeometry(self.frameRect())

        if not self.m_direction == QtCore.Qt.Horizontal:
            if _now < _next:
                offsetx, offsety = 0, -offsety
            else:
                offsetx = 0
        else:
            if _now < _next:
                offsetx, offsety = -offsetx, 0
            else:
                offsety = 0

        pnext = self.widget(_next).pos()
        pnow = self.widget(_now).pos()
        self.m_pnow = pnow

        offset = QtCore.QPoint(offsetx, offsety)
        self.widget(_next).move(pnext - offset)
        self.widget(_next).show()
        self.widget(_next).raise_()

        anim_group = QtCore.QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
            (_now, _next), (pnow, pnext - offset), (pnow + offset, pnext)
        ):
            animation = QtCore.QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.m_speed,
                easingCurve=self.m_animationtype,
                startValue=start,
                endValue=end,
            )
            anim_group.addAnimation(animation)

        self.m_next = _next
        self.m_now = _now
        self.m_active = True
        anim_group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

    @QtCore.Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.m_next)
        self.widget(self.m_now).hide()
        self.widget(self.m_now).move(self.m_pnow)
        self.m_active = False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        slidingStacked = SlidingStackedWidget()
        for i in range(10):
            label = QtWidgets.QLabel(
                "Qt is cool " + i * "!", alignment=QtCore.Qt.AlignCenter
            )
            color = QtGui.QColor(*random.sample(range(255), 3))
            label.setStyleSheet(
                "QLabel{ background-color: %s; color : white; font: 40pt}"
                % (color.name(),)
            )
            slidingStacked.addWidget(label)

        button_prev = QtWidgets.QPushButton(
            "Previous", pressed=slidingStacked.slideInPrev
        )
        button_next = QtWidgets.QPushButton(
            "Next", pressed=slidingStacked.slideInNext
        )

        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(button_prev)
        hlay.addWidget(button_next)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addLayout(hlay)
        lay.addWidget(slidingStacked)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())
"""