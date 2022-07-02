import sys
import os

#Path import
################################################################################
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/ConfigWidget/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/MainWindow/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/DatabaseViewer/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/OfflineAnalysis/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/OnlineAnalysis/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/Settings/ui_py")
sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI/OfflineAnalysis/CustomWidget")
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
import logging
from qt_material import QtStyleTools
from self_configuration import *
from offline_analysis_widget import Offline_Analysis
from settings_dialog import *
from frontend_style import Frontend_Style
from data_db import DuckDBDatabaseHandler
from BlurWindow.blurWindow import GlobalBlur

class MainWindow(QMainWindow, QtStyleTools):


    def __init__(self, parent = None):
        """Initialize the MainWindow class for starting the Application

        Args:
            parent (QWidget, optional): Can Add a widget here as a parent. Defaults to None.
        """        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._not_launched = True # Check if the program is launched to avoid resize event
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center() # center

        
        #self.progressBar.setValue()

        print(self.ui.notebook.currentIndex())
        self.setCentralWidget(self.ui.centralwidget)

        # introduce style sheet to be used by start .py
        self.frontend_style = Frontend_Style()
        # distribute this style object to all other classes to be used
        # whenever the style will be changed, all classes share the same style object and adapt it's appearance
        self.ui.offline.frontend_style = self.frontend_style

        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        self.local_database_handler = DuckDBDatabaseHandler()

        if self.local_database_handler:
            self.statusBar().showMessage("Database Connection Loaded")
        
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
        self.buttons = (self.ui.home_window, self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics, self.ui.settings_button)
        self.home_buttons = (self.ui.configuration_home_2, self.ui.online_analysis_home_2, self.ui.offline_analysis_home_2, self.ui.database_viewer_home_2)

        for i, button in enumerate(self.buttons):
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))


        for i, button in enumerate(self.home_buttons):
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i+1))
        #self.configuration_elements = Config_Widget()

        #self.ui.statistics_2.setProperty("class", "big_button")
        #print(self.ui.config.Load_meta_data_experiment_12)

        # connect to the metadata file path 
        #self.ui.hamburger_button.clicked.connect(self.animate_menu)
        self.ui.darkmode_button.clicked.connect(self.change_to_lightmode)

        #testing
        self.ui.config.transfer_to_online_analysis_button.clicked.connect(self.transfer_file_to_online)

        # connect settings button
        self.write_button_text()
        self.ui.minimize_button.clicked.connect(self.minimize) # button to minimize
        self.ui.pushButton_3.clicked.connect(self.maximize) # button to maximize 
        self.ui.maximize_button.clicked.connect(self.quit_application)
        #GlobalBlur(self.winId(), Acrylic=True)

    def center(self):
        """Function to center the application at the start into the middle of the screen
        """        
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        """Function to detect mouse press

        Args:
            event (event): is a mouse Press Event
        """        
        self.oldPos = event.globalPos()
        print(self.oldPos)


    def mouseMoveEvent(self, event):
        """Function to get the mouse moving events

        Args:
            event (event): retrieve the mouse move event
        """        
        if (event.y()) < 60:
            #GlobalBlur(self.winId(), Acrylic=False)
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """Function to detect the mouse release event

        Args:
            event (event): Mouse release
        """      

        #GlobalBlur(self.winId(), Acrylic=True)

    def resizeEvent(self, event):
        """resizing of MainWindow

        Args:
            event (event): Retrieve resizing events of the main window
        """        

        #check this flag to avoid overriding of acrylic effect at start since resize is triggered
        if self._not_launched:
            self._not_launched = False
            return
        # during resize change to aero effect to avoid lag
        #GlobalBlur(self.winId(), Acrylic=False)
       
        
    def transfer_file_to_online(self):
        """Function to transfer the Patchmaster generated .Dat file to the online Analysis
        for further analysis
        """        
        file_path = self.ui.config.get_file_path()
        self.ui.config.set_dat_file_name(self.ui.config.experiment_type_desc.text()) # set the name of the .Dat file
        self.ui.online.open_single_dat_file(str(file_path)) # open the .Dat file in the UI window


    def minimize(self):
        """ Function to minimize the window"""
        self.showMinimized()

    def maximize(self):
        """Function to maximize of to retrive the original window state"""
        if (self.height() == 1040) and (self.width() == 1920):
            self.setGeometry(self.window_geometry)
            
        else:
            print("yes")
            self.window_geometry = self.geometry()
            self.setGeometry(0,0,1920,1040) # maximize the window
            

    def quit_application(self):
        """ Function to quit the app"""
        QCoreApplication.quit()


    def erase_button_text(self):
        """ Set the Menu button text to noting"""
        self.ui.self_configuration.setText("")
        self.ui.online_analysis.setText("")
        self.ui.offline_analysis.setText("")
        self.ui.statistics.setText("")
        self.ui.darkmode_button.setText("")
        self.ui.konsole_button.setText("")
        self.ui.settings_button.setText("")

    def write_button_text(self):
        """ Add names to the buttons"""
        self.ui.home_window.setText("  Home")
        self.ui.self_configuration.setText("  Configuration")
        self.ui.online_analysis.setText(" Online Analysis")
        self.ui.offline_analysis.setText(" Offline Analysis")
        self.ui.statistics.setText("Database View")
        #self.ui.darkmode_button.setText("Change Theme")
        #self.ui.konsole_button.setText("Terminal")
        self.ui.settings_button.setText("Settings")


    def change_to_lightmode(self):
        # @toDO should be added to the designer class 

        if self.get_darkmode() == 1:
            self.set_darkmode(0)
            self.apply_stylesheet(self, "light_blue.xml", invert_secondary=True)
            with open(os.path.dirname(os.getcwd()) + "/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                print(file)
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))

            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/darkmode_button.png);background-repeat: None; \n"
                                                    "color: #d2691e;\n"
                                                    "padding: 5px 10px;\n"
                                                    "background-position: left;\n"
                                                    "border: none;\n"
                                                    "border-radius: 5px;\n"
                                                    "\n"
                                                        "\n")
                                                 
            print(self.frontend_style.get_sideframe_dark())
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_light())
           
            
        else:
            self.set_darkmode(1) # set the darkmode back to 1 for the switch
            self.apply_stylesheet(self, "dark_red.xml")
            with open(os.path.dirname(os.getcwd()) + "/QT_GUI/LayoutCSS/Menu_button.css") as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.darkmode_button.setStyleSheet("background-image : url(../QT_GUI/Button/Logo/Lightmode_button.png);background-repeat: None; \n"
                                                    "background-repeat:None;\n"
                                                    "color: #d2691e;\n"
                                                    "padding: 5px 10px;\n"
                                                    "background-position: left;\n"
                                                    "border: none;\n"
                                                    "border-radius: 5px;\n"
                                                    "\n"
                                                        "\n")
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_dark())
 
            

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()

        #  make sure to have all popups  in the same changed theme color
        self.frontend_style.current_style=self.default_mode

    def init_offline_analysis(self):
        """Function to initialize the offline analysis"""
        self.offline_analizer = Offline_Analysis()#Ui_Offline_Analysis()
        #self.offline_analizer.setupUi(self)

    def set_darkmode(self, default_mode):
        """Is important for setting the dark mode and white mode

        Args:
            default_mode (int): 0 or 1 for dark or light mode
        """        
        self.default_mode = default_mode

    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode


if __name__ == "__main__":
    """Main function to start the application"""
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')
    stylesheet = app.styleSheet()
    with open(os.path.dirname(os.getcwd()) + "/QT_GUI/LayoutCSS/Menu_button.css") as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    app.exec()

