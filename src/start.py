import sys
import os
from PySide6.QtWidgets import QMainWindow, QGraphicsBlurEffect
from PySide6.QtCore import Qt, QPoint, QRect
from QT_GUI.MainWindow.ui_py.main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
import logging
from qt_material import QtStyleTools
from QT_GUI.ConfigWidget.ui_py.self_configuration import *
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_widget import Offline_Analysis
from QT_GUI.Settings.ui_py.settings_dialog import *
from frontend_style import Frontend_Style
from database.data_db import DuckDBDatabaseHandler
if sys.platform != "darwin":
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
        # Check if the program is launched to avoid resize event
        self._not_launched = True 
        self.center() #place the MainWindow in the center
        self.setWindowTitle("Biophysical Essentials")
        
        # Check the current OS
        if sys.platform != "darwin":
            print("Non Darwin Platform initialized")
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.setWindowFlag(Qt.FramelessWindowHint)
            GlobalBlur(self.winId(), Acrylic=False,QWidget=self)
        
        # set the window geometry to the screen size
        self.desktop = self.screen()
        self.screenRect = self.desktop.availableGeometry()
        self.setCentralWidget(self.ui.centralwidget)
        # Logger for the Main function called start
        self.logger=logging.getLogger() 
        self.establish_logger()
        self.frontend_style = Frontend_Style()
        
        # distribute this style object to all other classes to be used
        # whenever the style will be changed, all classes share the same style object and adapt it's appearance
        self.ui.offline.frontend_style = self.frontend_style
        self.ui.offline.result_visualizer.frontend_style = self.frontend_style

        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        self.local_database_handler = DuckDBDatabaseHandler()
        
        #self.local_database_handler.database.execute("SET external_threads=1")
        if self.local_database_handler:
            self.statusBar().showMessage("Database Connection Loaded")
        
        # share the object with offline analysis and database viewer
        self.ui.offline.update_database_handler_object(self.local_database_handler)
        self.ui.database.update_database_handler(self.local_database_handler)
        self.ui.online.update_database_handler(self.local_database_handler)

        #darkmode implementation 0 = white, 1 = dark
        self.default_mode = 1
        self.button_connections()

        self.change_to_lightmode()
      
    def button_connections(self):
        self.buttons = (self.ui.home_window, self.ui.self_configuration, self.ui.online_analysis, self.ui.offline_analysis, self.ui.statistics, self.ui.toolButton_2)
        
        for i, button in enumerate(self.buttons):
            button.clicked.connect(partial(self.ui.notebook.setCurrentIndex, i))

        # home buttons 
        self.ui.configuration_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 1))
        self.ui.online_analysis_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 2))
        self.ui.database_viewer_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 4))
        self.ui.home_logo.clicked.connect(self.open_bpe_webside)
        self.ui.offline_analysis_home_2.clicked.connect(self.insert_row_of_buttons)

        self.ui.statistics.clicked.connect(self.initialize_database)
        self.ui.darkmode_button.clicked.connect(self.change_to_lightmode)
        self.ui.config.transfer_to_online_analysis_button.clicked.connect(self.transfer_file_to_online)
        self.ui.minimize_button.clicked.connect(self.minimize) # button to minimize
        self.ui.pushButton_3.clicked.connect(self.maximize) # button to maximize 
        self.ui.maximize_button.clicked.connect(self.quit_application)
        

    def insert_row_of_buttons(self,grid_layout: QGridLayout):
        """
        Function to insert a row of buttons to the start up grid
        """
        # Get the number of rows and columns in the grid
        grid_layout = self.ui.gridLayout_4
        button_txt = ["New Analysis From Directory", "New Analysis From Database", "Open Existing Analysis"]
        r = grid_layout.rowCount()
        # new buttons will be inserted in row 6
        rows = 6
        cols = grid_layout.columnCount()

        if  grid_layout.itemAtPosition(rows, 1).widget().text() == button_txt[0]:
            #remove the item
            for col in range(1,cols):
                widget_to_remove = grid_layout.itemAtPosition(rows, col).widget()
                grid_layout.removeWidget(widget_to_remove)
                widget_to_remove.deleteLater()
                
                widget_to_remove = grid_layout.itemAtPosition(rows+1, col).widget()
                widget_to_add = widget_to_remove
                grid_layout.removeWidget(widget_to_remove) 
                #widget_to_remove.deleteLater() 
                grid_layout.addWidget(widget_to_add,rows,col)            

            self.ui.offline_analysis_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 15em; background-color: transparent; border: 0px; }  QToolButton:hover{background-color: grey;}")
    
                 
        else:
            # move old columns to new row
            for col in range(1,cols):
                button =  grid_layout.itemAtPosition(rows, col).widget()

                animation = QPropertyAnimation(button, b"geometry")
                animation.setDuration(500)
                animation.setStartValue(button.geometry())
                animation.setEndValue(grid_layout.cellRect(rows, col))
                easing_curve = QEasingCurve(QEasingCurve.Linear)
                animation.setEasingCurve(easing_curve)
                grid_layout.addWidget(button, rows + 1 ,col)
                animation.start()
                new_button = QToolButton()
                new_button.setText(button_txt[col-1])
                icon = QIcon()
        
                if col == 1:
                    new_button.clicked.connect(self.start_new_offline_analysis_from_dir)
                    icon.addFile(u"../QT_GUI/Button/OnlineAnalysis/open_dir.png", QSize(), QIcon.Normal, QIcon.Off)
                if col == 2:
                    new_button.clicked.connect(self.start_new_offline_analysis_from_db)
                    icon.addFile(u"../QT_GUI/Button/OnlineAnalysis/db.png", QSize(), QIcon.Normal, QIcon.Off)
                if col == 3:
                    new_button.clicked.connect(partial(self.ui.notebook.setCurrentIndex,3))
                    icon.addFile(u"../QT_GUI/Button/OnlineAnalysis/open_existing_results.png", QSize(), QIcon.Normal, QIcon.Off)
                
                
                new_button.setStyleSheet(u"QToolButton{ background-color: #d9d9d9; border: 0px; } QToolButton:hover{background-color: grey;}")
                new_button.setIcon(icon)
                new_button.setIconSize(QSize(100, 100))
                new_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                grid_layout.addWidget(new_button, rows, col)

            self.ui.offline_analysis_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 15em; background-color: #d9d9d9; border: 0px; }  QToolButton:hover{background-color: grey;}")
    
    def start_new_offline_analysis_from_dir(self):
        "start new offline analysis, therefore let the user choose a directory and add the data to the database"
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(1)
        self.ui.notebook.setCurrentIndex(3)
        self.ui.offline.open_directory()

    def start_new_offline_analysis_from_db(self):
        "start new offline analysis, therefore let the user choose a data from the database"
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(1)
        self.ui.notebook.setCurrentIndex(3)
        self.ui.offline.load_treeview_from_database()
        

    def open_bpe_webside(self):
        """
        open the webside of BPE
        """
        import webbrowser
        url = "https://www.google.com/"
        webbrowser.open(url, new=0, autoraise=True)
        
    def establish_logger(self):
        """Connect and establish the Logging during StartUp Process
        """
        file_handler = logging.FileHandler('../Logs/start.log')
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s') #Check formatting
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info('A trial message if the logger is working')
        self.logger.setLevel(logging.ERROR)

    def initialize_database(self):
        """Initialization of the DataBase using the duckdbhandler
        """
        self.ui.notebook.setCurrentIndex(4)
        self.ui.database.show_basic_tables(self.local_database_handler)

    def center(self):
        """Function to center the application at the start into the middle of the screen
        """        
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        """Function to detect mouse press

        Args:
            event (event): is a mouse Press Event
        """        
        self.oldPos = event.globalPosition().toPoint()
    

    def mouseMoveEvent(self, event: QMouseEvent):
        """Function to get the mouse moving events

        Args:
            event (event): retrieve the mouse move event
        """        
        if (event.pos().y()) < 60:
            if sys.platform != "darwin":
               GlobalBlur(self.winId(), Acrylic=False,QWidget=self)
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

        if event.globalPosition().y() < 12:
            window_size = self.geometry()
            self.maximize(window_size)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """Function to detect the mouse release event

        Args:
            event (event): Mouse release
        """      
        if sys.platform != "darwin":   
            GlobalBlur(self.winId(), Acrylic=True,QWidget=self)

    def resizeEvent(self, even: QResizeEvent):
        """resizing of MainWindow

        Args:
            event (event): Retrieve resizing events of the main window
        """        

        #check if program is launched to avoid resizing
        if self._not_launched:
            self._not_launched = False
            return
        # during resize change to aero effect to avoid lag
        if sys.platform != "darwin":
            GlobalBlur(self.winId(), Acrylic=False,QWidget=self)
    
    def transfer_file_to_online(self):
        """Function to transfer the Patchmaster generated .Dat file to the online Analysis
        for further analysis
        """        
        file_path = self.ui.config.get_file_path()
        self.ui.config.set_dat_file_name(self.ui.config.experiment_type_desc.text()) 
        self.ui.online.open_single_dat_file(str(file_path)) 

    def minimize(self):
        """ Function to minimize the window"""
        self.showMinimized()

    def maximize(self, window_size: QRect):
        """Function to maximize of to retrive the original window state,
        
        args:
            window_size (QRect): the size of the window
        """
        if window_size:
            self.first_geometry = window_size

        if self.geometry() == self.screenRect:
            self.animate_resizing(size = True)
            
        else:
            self.animate_resizing()

    def animate_resizing(self, size = None):
        """Function to animate the resizing of the window
        args:
            size (bool): if true the window is maximized, if false the window is minimized
        """  
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(50)
        if size is None:      
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(self.screenRect)
            self.animation.start()
        else:
            self.animation.setStartValue(self.geometry())
            self.animation.setEndValue(QRect(320, 45, 1280, 950))
            self.animation.start()

    def quit_application(self):
        """ Function to quit the app"""
        QCoreApplication.quit()

    def change_to_lightmode(self):
        """DarkMode LightMode Switch
        """

        if self.get_darkmode() == 1:
            self.set_darkmode(0)
            self.apply_stylesheet(self, "light_blue.xml", invert_secondary=True)
            
            # open the extension from the css file
            with open(os.getcwd() + "/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_light())
            self.frontend_style.change_canvas_bright()
           
            
        else:
            self.set_darkmode(1) # set the darkmode back to 1 for the switch
            self.apply_stylesheet(self, "hello.xml")
            with open(os.getcwd() + "/QT_GUI/LayoutCSS/Menu_button_mac.css") as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
            self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_dark())
            self.frontend_style.change_canvas_dark()
            

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()
        #  make sure to have all popups  in the same changed theme color
        self.frontend_style.current_style=self.default_mode

    def init_offline_analysis(self):
        """Function to initialize the offline analysis"""
        self.offline_analizer = Offline_Analysis()#Ui_Offline_Analysis()
        #self.offline_analizer.setupUi(self)

    def set_darkmode(self, default_mode: bool):
        """Is important for setting the dark mode and white mode

        Args:
            default_mode (int): 0 or 1 for dark or light mode
        """        
        self.default_mode = default_mode

    def get_darkmode(self):
        "returns the darkmode state"
        return self.default_mode


if __name__ == "__main__":
    """Main function to start the application"""
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='hello.xml')
    stylesheet = app.styleSheet()
    stylesheet_loaded = "Menu_button.css"
    if sys.platform == "darwin":
        stylesheet_loaded = "Menu_button_mac.css" 
    with open(os.getcwd() + f"/QT_GUI/LayoutCSS/{stylesheet_loaded}") as file:
        app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    window = MainWindow()
    window.show()
    app.exec()

