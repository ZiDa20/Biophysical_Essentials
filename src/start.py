
import sys
import os
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        buttons = (self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics)
        for i, button in enumerate(buttons):
            button.setProperty('class', 'big_button')
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))


        print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        self.ui.config.Load_meta_data_experiment_12.clicked.connect(self.ui.config.open_directory)
        self.ui.config.pushButton.clicked.connect(self.ui.config.initialize_camera)
        self.ui.config.button_start_camera.clicked.connect(self.ui.config.start_camera_timer)
        self.ui.config.button_stop_camera.clicked.connect(self.ui.config.stop_camera)
        self.ui.config.button_take_snapshot.clicked.connect(self.ui.config.show_snapshot)
        # initialize the camera module

    #def select_file(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    stylesheet = app.styleSheet()
    with open('Menu_button.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    
