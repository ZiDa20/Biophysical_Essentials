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
from frontend_style import Frontend_Style
from data_db import DuckDBDatabaseHandler

class MainWindow(QMainWindow, QtStyleTools):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.settings_button.clicked.connect(self.open_settings)

        self.setCentralWidget(self.ui.centralwidget)

        # introduce style sheet to be used by start .py
        self.frontend_style = Frontend_Style()
        # distribute this style object to all other classes to be used
        # whenever the style will be changed, all classes share the same style object and adapt it's appearance
        self.ui.offline.frontend_style = self.frontend_style

        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        self.local_database_handler = DuckDBDatabaseHandler()

        # share the object with offline analysis and database viewer
        self.ui.offline.update_database_handler_object(self.local_database_handler)
        self.ui.database.update_database_handler(self.local_database_handler)





        #self.ui.online.frontend_style = self.frontend_style

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
        self.buttons = (self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics)
        for i, button in enumerate(self.buttons):
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))

        #self.configuration_elements = Config_Widget()

        #self.ui.statistics_2.setProperty("class", "big_button")
        #print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        #self.ui.hamburger_button.clicked.connect(self.animate_menu)
        self.ui.konsole_button.clicked.connect(self.konsole_menu)
        self.ui.darkmode_button.clicked.connect(self.change_to_lightmode)

        #testing
        self.ui.config.transfer_to_online_analysis_button.clicked.connect(self.transfer_file_to_online)

        # connect settings button
        self.write_button_text()
        #self.test_blurring()
        #self.ui.side_left_menu.setMinimumSize(300, 1000)
        #self.ui.side_left_menu.setMaximumSize(300, 1800)

    def transfer_file_to_online(self):
        """ transfer the self.configuration data to the online analysis """
        file_path = self.ui.config.get_file_path()
        self.ui.online.open_single_dat_file(str(file_path))

    def open_settings(self):
        """ This should be changed to the main settings"""
        self.settings = SettingsWindow()
        self.settings.show()

    """
    not used anymore
    def animate_menu(self):
        animation of the side-bar for open and close animation,
        @toDO should change animation speed for smoother animation 
        width = self.ui.side_left_menu.width() # get the width of the menu
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
        self.animation.setDuration(4000)
        self.animation.setStartValue(QSize(width,self.ui.side_left_menu.height()))
        self.animation.setEndValue(QSize(newWidth,self.ui.side_left_menu.height()))
        self.animation.setEasingCurve(QEasingCurve.InOutQuart) # set the Animation
        self.animation.start()
        self.ui.side_left_menu.setMaximumSize(newWidth, 1500)
        self.ui.side_left_menu.setMinimumSize(newWidth, self.ui.side_left_menu.height())
    """

        
    def konsole_menu(self):
        """ toDO: still opens every time whne layout is changing--> bugfix better integratin into the layout
         """
        height = self.ui.frame.height()
        position = self.ui.frame.pos()
        self.ui.frame.setStyleSheet("background:transparent")
        self.ui.frame.setStyleSheet("QFrame:hover{\n"
                                                    "	background-color: \"#ff8117\";\n"
                                                    "}")
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

        # sets the minimum and maximum size of the konsole model
        self.ui.frame.setMinimumSize(0, 0)
        self.ui.frame.setMaximumSize(300, 300)

        #get the size of the konsole
        self.animation = QPropertyAnimation(self.ui.frame, b"size")
        #get the position of the konsole       
        self.position = QPropertyAnimation(self.ui.frame, b"pos")
        print(f"size of the konsole is: {self.animation} and position of the konsole is: {position}")
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
        self.ui.self_configuration.setText("  Configuration")
        self.ui.online_analysis.setText(" Online Analysis")
        self.ui.offline_analysis.setText(" Offline Analysis")
        self.ui.statistics.setText("Statistics")
        #self.ui.darkmode_button.setText("Change Theme")
        #self.ui.konsole_button.setText("Terminal")
        self.ui.settings_button.setText("Settings")


    def change_to_lightmode(self):
        # @toDO should be added to the designer class 

        if self.get_darkmode() == 1:
            self.set_darkmode(0)
            self.apply_stylesheet(self, "light_red.xml", invert_secondary=True)
            with open('Menu_button_white.css') as file:
                print(file)
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))

            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/darkmode_button.png);background-repeat: None;")
            print(self.frontend_style.get_sideframe_dark())
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_light())
           
            
        else:
            self.set_darkmode(1) # set the darkmode back to 1 for the switch
            self.apply_stylesheet(self, "dark_red.xml")
            with open('Menu_button.css') as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/Lightmode_button.png);background-repeat: None;")
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_dark())
 
            

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()

        #  make sure to have all popups  in the same changed theme color
        self.frontend_style.current_style=self.default_mode

    def init_offline_analysis(self):
        self.offline_analizer = Offline_Analysis()#Ui_Offline_Analysis()
        #self.offline_analizer.setupUi(self)

    def set_darkmode(self, default_mode):
        """ Function to retrieve the current state of the design
        default_mode -> boolean (1 if light and 0 if darkmode)""" 
        self.default_mode = default_mode

    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode

    """
    def test_blurring(self):
        currently not working at all
        effect = BlurEffect()
        self.ui.side_left_menu.setGraphicsEffect(effect)
        effect.setEnabled(False)
        effect.setBlurRadius(50)
        print("intialized blurring")
        effect.setBlurRadius(20)
    """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')
    stylesheet = app.styleSheet()
    with open('Menu_button.css') as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

