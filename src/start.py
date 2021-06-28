
import sys
import os
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
from offline_analysis_widget import Ui_Offline_Analysis

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        buttons = (self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics)
        for i, button in enumerate(buttons):
            button.setProperty('class', 'big_button')
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))

        self.ui.offline_analysis.clicked.connect(self.init_offline_analysis)

    def init_offline_analysis(self):
        self.offline_analizer = Ui_Offline_Analysis()
        self.offline_analizer.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    stylesheet = app.styleSheet()
    with open('Menu_button.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    
