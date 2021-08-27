import sys
import os
import time

sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsBlurEffect
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve, QSize
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
import logging
from qt_material import QtStyleTools
from self_configuration import *
from offline_analysis_widget import Offline_Analysis
from settings_dialog import *
from tkinter_camera import *

class MainWindow(QMainWindow, QtStyleTools):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.settings_button.clicked.connect(self.open_settings)

        # Logger for the Main function called start
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/start.log')
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s') #Check formatting
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info('A trial message if the logger is working')


        #darkmode implementation
        self.default_mode = 1

        #make button
        buttons = (self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics)
        for i, button in enumerate(buttons):
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))

        

        #self.configuration_elements = Config_Widget()

        #self.ui.statistics_2.setProperty("class", "big_button")
        #print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        
        self.ui.hamburger_button.clicked.connect(lambda: self.animate_menu())
        self.ui.konsole_button.clicked.connect(lambda:self.konsole_menu())
        self.ui.darkmode_button.clicked.connect(self.change_to_lightmode)

        #testing
        self.ui.config.transfer_to_online_analysis_button.clicked.connect(self.transfer_file_to_online)
        # connect settings button
        

        self.write_button_text()
        self.test_blurring()
        self.ui.side_left_menu.setMinimumSize(300, 1000)
        self.ui.side_left_menu.setMaximumSize(300, 1800)

    def transfer_file_to_online(self):
        file_path = self.ui.config.get_file_path()
        self.ui.online.open_single_dat_file(str(file_path))

    def open_settings(self):

        self.settings = SettingsWindow()
        self.settings.show()

    def animate_menu(self):
        width = self.ui.side_left_menu.width()
        print(width)
        if width >= 300:
            print("yeah")
            newWidth = 51
            self.erase_button_text()
            newWidth = 51
        else:
            print("hello")
            newWidth = 300
            self.write_button_text()

        self.ui.side_left_menu.setMinimumSize(0,0)
        self.animation = QPropertyAnimation(self.ui.side_left_menu, b"size")
        self.animation.setDuration(2000)
        self.animation.setStartValue(QSize(width,self.ui.side_left_menu.height()))
        self.animation.setEndValue(QSize(newWidth,self.ui.side_left_menu.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        self.ui.side_left_menu.setMaximumSize(newWidth, 1500)
        self.ui.side_left_menu.setMinimumSize(newWidth, self.ui.side_left_menu.height())


    def konsole_menu(self):
        height = self.ui.frame.height()
        position = self.ui.frame.pos()
        self.ui.frame.setStyleSheet("background:transparent")
        self.ui.frame.setStyleSheet("QFrame:hover{\n"
                                                    "	background-color: \"#ff8117\";\n"
                                                    "}")
        print(position)
        print(height)
        if height > 351:
            print("changed_console_height")
            newHeight = 21
        else:
            print("changed_console_height_to_351")
            newHeight = 500

        if position.y() == 600:
            newPosition = 1500

        else:
            newPosition = 600

        self.ui.frame.setMinimumSize(0, 0)
        self.ui.frame.setMaximumSize(1500, 1500)
        self.animation = QPropertyAnimation(self.ui.frame, b"size")
        self.position = QPropertyAnimation(self.ui.frame, b"pos")
        self.animation.setDuration(500)
        self.position.setDuration(100)
        self.position.setStartValue(QPoint(self.ui.frame.pos().x(), position.y()))
        self.position.setEndValue(QPoint(self.ui.frame.pos().x(), newPosition))
        self.position.start()
        self.animation.setStartValue(QSize(self.ui.frame.width(), height))
        self.animation.setEndValue(QSize(self.ui.frame.width(), newHeight))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def erase_button_text(self):
        self.ui.self_configuration.setText("")
        self.ui.online_analysis.setText("")
        self.ui.offline_analysis.setText("")
        self.ui.statistics.setText("")
        self.ui.darkmode_button.setText("")
        self.ui.konsole_button.setText("")
        self.ui.settings_button.setText("")

    def write_button_text(self):
        self.ui.self_configuration.setText("Self Configuration")
        self.ui.online_analysis.setText("Online Analysis")
        self.ui.offline_analysis.setText("Offline Analysis")
        self.ui.statistics.setText("Statistics")
        self.ui.darkmode_button.setText("Change Theme")
        self.ui.konsole_button.setText("Terminal")
        self.ui.settings_button.setText("Settings")


    def change_to_lightmode(self):
        print("entered the function")
        print(self.default_mode)
        print(self.style().metaObject().className())
        if self.get_darkmode() == 1:
            self.set_darkmode(0)
            self.apply_stylesheet(self, "light_red.xml", invert_secondary=True)
            with open('Menu_button_white.css') as file:
                print(file)
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))

            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/darkmode_button.png);background-repeat: None;")
            self.ui.side_left_menu.setStyleSheet(u"QFrame{\n"
                                                    "	background-color: \"#e6e6e6\";\n"
                                                    "\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton{\n"
                                                    "	padding: 5px 10px;\n"
                                                    "	border: none;\n"
                                                    "	border-radius:5px;\n"
                                                    "	background-color: \"#e6e6e6\";\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover{\n"
                                                    "	background-color: \"#ff8117\";\n"
                                                    "}") 
           
            
        else:
            self.apply_stylesheet(self, "dark_red.xml")
            with open('Menu_button.css') as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/Lightmode_button.png);background-repeat: None;")
            self.ui.side_left_menu.setStyleSheet(u"QFrame{\n"
                                                            "	background-color: \"#232629\";\n"
                                                            "\n"
                                                            "}\n"
                                                            "\n"
                                                            "QPushButton{\n"
                                                            "	padding: 5px 10px;\n"
                                                            "	border: none;\n"
                                                            "	border-radius:5px;\n"
                                                            "	background-color: \"#232629\";\n"
                                                            "}\n"
                                                            "\n"
                                                            "QPushButton:hover{\n"
                                                            "	background-color: \"#54545a\";\n"
                                                            "}") 
 
            self.set_darkmode(1)

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()

        
        self.ui.offline_analysis.clicked.connect(self.init_offline_analysis)

    def init_offline_analysis(self):
        self.offline_analizer = Offline_Analysis()#Ui_Offline_Analysis()
        #self.offline_analizer.setupUi(self)

    def set_darkmode(self, default_mode):
        self.default_mode = default_mode

    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode

    def test_blurring(self):
        """currently not working at all"""
        effect = QGraphicsBlurEffect(blurRadius= 2000)
        effect.setEnabled(True)
        #effect.setBlurRadius(50)
        self.ui.side_left_menu.setGraphicsEffect(effect)
        print(effect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')
    stylesheet = app.styleSheet()
    with open('Menu_button.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)