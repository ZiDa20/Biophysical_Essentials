
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

        self.ui.statistics_2.setProperty("class", "big_button")


        #print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        self.ui.config.Load_meta_data_experiment_12.clicked.connect(self.ui.config.meta_open_directory) # initialize meta data sheet opening boehringer special

        #connect to the camera control
        self.ui.config.pushButton.clicked.connect(self.ui.config.initialize_camera) # initalize the camera 
        self.ui.config.button_start_camera.clicked.connect(self.ui.config.start_camera_timer) # intialize 
        self.ui.config.button_stop_camera.clicked.connect(self.ui.config.stop_camera)
        self.ui.config.button_take_snapshot.clicked.connect(self.ui.config.show_snapshot)

        #connect to the function for the batch communication
        self.ui.config.button_batch_1.clicked.connect(self.ui.config.open_batch_path)
        self.ui.config.button_control_1.clicked.connect(self.ui.config.generate_control_file)
        self.ui.config.button_submit_command.clicked.connect(self.ui.config.get_commands_from_textinput)
        self.ui.config.button_clear_window.clicked.connect(self.ui.config.end_communication_control)
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


    
