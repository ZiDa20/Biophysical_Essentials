import sys
import os
from loggers.start_logger import start_logger
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
from QT_GUI.MainWindow.ui_py.main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from functools import partial
from qt_material import QtStyleTools
from StyleFrontend.frontend_style import Frontend_Style
from database.data_db import DuckDBDatabaseHandler
from StyleFrontend.animated_ap import LoadingAnimation
import webbrowser

class MainWindow(QMainWindow, QtStyleTools):

    def __init__(self, testing_db = None,  parent = None):
        """Initialize the MainWindow class for starting the Application

        Args:
            parent (QWidget, optional): Can Add a widget here as a parent. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1600,800)
        self.setCentralWidget(self.ui.centralwidget)
        self.center() #place the MainWindow in the center
        self.setWindowTitle("BiophysicalEssentials (BPE)")
        self.logger= start_logger # set the logger
        self.logger.info("Starting the Biophysical Essentials Program!")
        self.frontend_style = Frontend_Style(self)

        # Create the frontend style for the app

        self.ui.offline.stackedWidget.setCurrentIndex(1)
        self.ui.offline.object_splitter = QSplitter(Qt.Horizontal)
        self.ui.offline.gridLayout.addWidget(self.ui.offline.object_splitter)
        self.ui.offline.object_splitter.addWidget(self.ui.offline.SeriesItems_2)

    
        self.check_already_executed  = None

        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        if testing_db:
            self.local_database_handler = testing_db
        else:
            self.local_database_handler = DuckDBDatabaseHandler(self.frontend_style)

        self.online_database = DuckDBDatabaseHandler(self.frontend_style,
                                                    db_file_name = "online_db",
                                                    in_memory = True)
        if self.local_database_handler:
            self.statusBar().showMessage("Database Connection Loaded")
        # share the object with offline analysis and database viewer
        self.ui.offline.update_database_handler_object(self.local_database_handler, self.frontend_style, self.ui.notebook)
        self.ui.online.update_database_handler(self.online_database, self.local_database_handler)
        self.ui.offline.add_splitter()
        self.ui.database.update_database_handler(self.local_database_handler, self.frontend_style)
        self.ui.config.update_database_handler(self.local_database_handler, self.frontend_style)
        self.ui.online.frontend_style = self.frontend_style
        self.ui.config.online_analysis = self.ui.online

        self.ui.side_left_menu.hide()
        # this should be later be triggered by  a button click
        self.connect_buttons_start()
        self.ui.config.ui_notebook = self.ui.notebook

    def connect_buttons_start(self) -> None:
        """ Connects all the necessary buttons at the start"""
        self.ui.configuration_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 1))
        self.ui.online_analysis_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 2))
        self.ui.database_viewer_home_2.clicked.connect(self.initialize_database)
        self.ui.home_logo.clicked.connect(self.open_bpe_webside)
        self.ui.toolButton_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 5))
        self.ui.offline_analysis_home_2.clicked.connect(self.insert_row_of_buttons)
        self.ui.offline.go_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.database.HomeButton.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.online.go_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.config.go_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.config.go_to_online.clicked.connect(partial(self.ui.notebook.setCurrentIndex,2))
        self.ui.online.batch_config.clicked.connect(partial(self.ui.notebook.setCurrentIndex,1))


    def insert_row_of_buttons(self) -> None:
        """
        Function to insert a row of buttons to the start up grid
        """
        if self.ui.side_left_menu.isHidden():

            #self.ui.side_left_menu.show()
            button_txt = ["New Analysis From Directory", "New Analysis From Database", "Open Existing Analysis", "Continue"]

            amount_of_buttons = 4 if self.ui.offline.canvas_grid_layout.count()>0 else 3
            for col in range(amount_of_buttons):

                new_button = QToolButton()
                new_button.setText(button_txt[col])
                icon = QIcon()

                if col == 0:
                    new_button.clicked.connect(self.start_new_offline_analysis_from_dir)
                    if self.frontend_style.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_dir.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_dir_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 1:
                    new_button.clicked.connect(self.start_new_offline_analysis_from_db)
                    if self.frontend_style.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/db.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/db_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 2:
                    new_button.clicked.connect(self.open_analysis)
                    if self.frontend_style.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_existing_results.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_exisiting_results_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 3:
                    new_button.clicked.connect(self.go_to_offline_analysis)
                    if self.frontend_style.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/light_mode/offline_analysis/go_right.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/dark_mode/offline_analysis/go_right.png", QSize(), QIcon.Normal, QIcon.Off)

                if self.frontend_style.default_mode == 1:
                    new_button.setStyleSheet(u"QToolButton{ background-color: transparent; border: 0px; color: black} QToolButton:hover{background-color: grey;}")
                else:
                    new_button.setStyleSheet(u"QToolButton{ background-color: transparent; border: 0px; color: white} QToolButton:hover{background-color: grey;}")

                new_button.setIcon(icon)
                new_button.setIconSize(QSize(200, 200))
                new_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                self.ui.gridLayout_3.addWidget(new_button, 0, col)
                self.ui.side_left_menu.show()
        else:
            self.ui.side_left_menu.hide()

    def open_analysis(self) -> None:
        """Should open a already performed analysis
        """
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(2)
        # here we need a new dialog pop up that shows the offline analysis table and a select box to select the
        self.check_already_executed = self.ui.offline.show_open_analysis_dialog()
        QTest.mouseClick(self.ui.offline_analysis_home_2, Qt.LeftButton)

    def go_to_offline_analysis(self) -> None:
        """This opens the notebook page that has the Offline Analysis integrated
        """
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(0)
        self.ui.notebook.setCurrentIndex(3)
        QTest.mouseClick(self.ui.offline_analysis_home_2, Qt.LeftButton)

    def start_new_offline_analysis_from_dir(self)-> None:
        "start new offline analysis, therefore let the user choose a directory and add the data to the database"
        #self.go_to_offline_analysis()
        if self.check_already_executed:
            self.ui.offline.reset_class()
        self.ui.offline.open_directory()

    def start_new_offline_analysis_from_db(self)-> None:
        "start new offline analysis, therefore let the user choose a data from the database"
        
        if self.check_already_executed:
            self.ui.offline.reset_class()
        self.check_already_executed = self.ui.offline.load_treeview_from_database()
        self.go_to_offline_analysis()
        
    def open_bpe_webside(self)-> None:
        """open the webside of BPE"""
        url = "https://github.com/ZiDa20/Biophysical_Essentials"
        webbrowser.open(url, new=0, autoraise=True)

    def initialize_database(self)-> None:
        """Initialization of the DataBase using the duckdbhandler"""
        self.ui.notebook.setCurrentIndex(4)
        #self.local_database_handler.open_connection()
        self.ui.database.show_basic_tables(self.local_database_handler)

    def center(self)-> None:
        """Function to center the application at the start into the middle of the screen"""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    """Main function to start the application"""
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    os.environ["QT_SCALE_FACTOR"] = '1'
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    #app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    apply_stylesheet(app, theme="dark_cyan.xml")
    window = MainWindow()
    window.show()
    app.exec()

