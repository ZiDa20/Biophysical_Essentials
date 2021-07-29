
import sys
import os
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve, QSize
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
import logging
from qt_material import QtStyleTools
from self_configuration import *
from offline_analysis_widget import Offline_Analysis
import pyqtgraph as pg
class MainWindow(QMainWindow, QtStyleTools):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        

        self.configuration_elements = Config_Widget()

        self.ui.statistics_2.setProperty("class", "big_button")
        #print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        
        self.ui.hamburger_button.clicked.connect(lambda: self.animate_menu())
        self.ui.offline_analysis_2.clicked.connect(self.change_to_lightmode)
        

    def animate_menu(self):
        width = self.ui.side_left_menu.width()
        print(width)
        if width == 300:
            print("yeah")
            newWidth = 71
        else:
            print("hello")
            newWidth = 300
        self.ui.side_left_menu.setMinimumSize(0,0)
        self.ui.side_left_menu.setMaximumSize(1500,1500)
        self.animation = QPropertyAnimation(self.ui.side_left_menu, b"size")
        self.animation.setDuration(500)
        self.animation.setStartValue(QSize(width,self.ui.side_left_menu.height()))
        self.animation.setEndValue(QSize(newWidth,self.ui.side_left_menu.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def change_to_lightmode(self):
        print("entered the function")
        print(self.default_mode)
        print(self.style().metaObject().className())
        if self.default_mode == 1:
            self.default_mode = 0
            self.apply_stylesheet(self, "light_red.xml", invert_secondary=True)
            with open('Menu_button.css') as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))

            self.ui.offline_analysis_2.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/darkmode_button.png);background-repeat: None;") 
            self.ui.side_left_menu.setStyleSheet(u"QFrame{\n"
                                                    "	background-color: \"#414141\";\n"
                                                    "\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton{\n"
                                                    "	padding: 5px 10px;\n"
                                                    "	border: none;\n"
                                                    "	border-radius:5px;\n"
                                                    "	background-color: \"#414141\";\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover{\n"
                                                    "	background-color: \"#414141\";\n"
                                                    "}")

        else:
            self.apply_stylesheet(self, "dark_red.xml")
            with open('Menu_button.css') as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.offline_analysis_2.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/Lightmode_button.png);background-repeat: None;") 
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


            self.default_mode = 1

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()

        
        self.ui.offline_analysis.clicked.connect(self.init_offline_analysis)

    def init_offline_analysis(self):
        self.offline_analizer = Offline_Analysis()#Ui_Offline_Analysis()
        #self.offline_analizer.setupUi(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')
    stylesheet = app.styleSheet()
    with open('Menu_button.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    
