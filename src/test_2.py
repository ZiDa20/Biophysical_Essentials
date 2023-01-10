from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        # Create a button and a hidden widget
        self.button = QPushButton("Show Widget", self)
        self.hidden_widget = QLabel("This is a hidden widget", self)
        self.hidden_widget.hide()

        # Connect the button's clicked signal to the show_widget slot
        self.button.clicked.connect(self.show_widget)

        # Create a layout and add the button and hidden widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.hidden_widget)

    def show_widget(self):
        self.hidden_widget.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())