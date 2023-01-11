from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PySide6.QtCore import QEasingCurve

def insert_row_of_buttons(grid_layout: QGridLayout) -> None:
    # Get the number of rows and columns in the grid
    rows = grid_layout.rowCount()
    cols = grid_layout.columnCount()

    # move old columns to new row

    for col in range(0,2):
        button =  grid_layout.itemAtPosition(rows - 1, col).widget()

        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(button.geometry())
        animation.setEndValue(grid_layout.cellRect(rows, col))
        easing_curve = QEasingCurve(QEasingCurve.Linear)
        animation.setEasingCurve(easing_curve)
        grid_layout.addWidget(button, rows,col)
        animation.start()


    # Insert a new row at index 1 (between the first and second rows)
    grid_layout.addWidget(QPushButton("new Button 1 "), rows-1, 0)
    grid_layout.addWidget(QPushButton("new Button 2"), rows-1, 1)

app = QApplication()
window = QMainWindow()

# Create a grid layout with 2 rows and 2 columns
grid_layout = QGridLayout()
grid_layout.addWidget(QPushButton("Button 1"), 0, 0)
grid_layout.addWidget(QPushButton("Button 2"), 0, 1)
grid_layout.addWidget(QPushButton("Button 3"), 1, 0)
grid_layout.addWidget(QPushButton("Button 4"), 1, 1)

# Wrap the grid layout in a QWidget and set it as the central widget of the main window
central_widget = QWidget()
central_widget.setLayout(grid_layout)
window.setCentralWidget(central_widget)

# Connect the clicked signal of the first button to the insert_row_of_buttons function
button1 = grid_layout.itemAtPosition(0, 0).widget()
button1.clicked.connect(lambda: insert_row_of_buttons(grid_layout))

window.show()
app.exec_()

