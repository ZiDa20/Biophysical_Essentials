
"""
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
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTreeView, QVBoxLayout, QAbstractItemView, QHeaderView, QPushButton)
from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide6.QtGui import QStyledItemDelegate


class TreeModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data

    def columnCount(self, parent=QModelIndex()):
        return 4

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self.data[row][col]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return ['Column 1', 'Column 2', 'Column 3', 'Column 4'][section]

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column, None)

    def parent(self, index):
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        button = QPushButton("Button", parent)
        return button

class Window(QWidget):
    def __init__(self):
        super().__init__()

        data = [
            ['Row 1 - Column 1', 'Row 1 - Column 2', 'Row 1 - Column 3', 'Row 1 - Column 4'],
            ['Row 2 - Column 1', 'Row 2 - Column 2', 'Row 2 - Column 3', 'Row 2 - Column 4'],
            ['Row 3 - Column 1', 'Row 3 - Column 2', 'Row 3 - Column 3', 'Row 3 - Column 4'],
        ]

        model = TreeModel(data)

        treeview = QTreeView(self)
        treeview.setModel(model)
        treeview.setItemDelegateForColumn(3, ButtonDelegate(treeview))
        treeview.setSelectionBehavior(QAbstractItemView.SelectRows)
        treeview.setSelectionMode(QAbstractItemView.SingleSelection)
        treeview.setAlternatingRowColors(True)
        treeview.setUniformRowHeights(True)
        treeview.setSortingEnabled(True)
        treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        treeview.setHeader(QHeaderView(Qt.Horizontal))
        treeview.setRootIsDecorated(False)
        treeview.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        treeview.header().setStretchLastSection(False)
        treeview.header().setSortIndicator(0, Qt.AscendingOrder)
        treeview.header().setSortIndicatorShown(True)

        layout = QVBoxLayout(self)
        layout.addWidget(treeview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
