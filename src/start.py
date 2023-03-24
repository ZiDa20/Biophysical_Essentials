import sys
import os
from loggers.start_logger import start_logger
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
from QT_GUI.MainWindow.ui_py.main_window import Ui_MainWindow
from qt_material import apply_stylesheet
from CustomWidget.EventSplitter import MySplitter
from functools import partial
import logging
from qt_material import QtStyleTools
from Backend.self_configuration import *
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_widget import Offline_Analysis
from QT_GUI.Settings.ui_py.settings_dialog import *
from StyleFrontend.frontend_style import Frontend_Style
from database.data_db import DuckDBDatabaseHandler
from StyleFrontend.animated_ap import AnimatedAP
import matplotlib.animation as animation
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure



class MainWindow(QMainWindow, QtStyleTools):

    def __init__(self, parent = None):
        """Initialize the MainWindow class for starting the Application

        Args:
            parent (QWidget, optional): Can Add a widget here as a parent. Defaults to None.
        """
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1600,800)
        wait_widget = QWidget()
        wait_widget_layout = QGridLayout()


        self.ui.progressBar = QProgressBar()
        self.ui.progressBar.setFixedWidth(250)
        self.ui.progressBar.setAlignment(Qt.AlignLeft)


        new_label = QLabel()
        new_label.setText("Loading... \n Please Wait, your data is getting prepared ")
        font = QFont()
        font.setPointSize(15)
        new_label.setFont(font)
        new_label.setAlignment(Qt.AlignCenter)

        wait_widget_layout.addWidget(new_label,0, 0, 1, 3)

        canvas_widget = QWidget()
        wait_widget_layout.addWidget(canvas_widget,1,1)

        fig = Figure(figsize=(2,2))
        canvas = FigureCanvas(fig)
        canvas.setParent(canvas_widget)

        # Create a plot on the figure
        ax = fig.add_subplot(111)

        ap = AnimatedAP(ax)
        # Create the animation using the update function and the time points as frames
        anim = animation.FuncAnimation(fig, ap.anim_update, frames=len(ap.time), blit=True)

        # Show the plot on the QWidget
        # Create a QTimer
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(lambda: anim.event_source.start())
        canvas.draw_idle()

        #wait_widget_layout.addWidget(self.ui.progressBar,2,1)
        status_label = QLabel("Staus Default")
        status_label.setAlignment(Qt.AlignCenter)
        font.setPointSize(12)
        wait_widget_layout.addWidget(status_label,3,1)
        #wait_widget_layout.addWidget(statusbar,3,0)
        wait_widget_layout.addWidget(self.ui.progressBar,2,1)
        wait_widget.setLayout(wait_widget_layout)
        self.ui.offline.animation_layout.addWidget(wait_widget)

        #self.ui.notebook.setCurrentIndex(3)
        self.ui.offline.stackedWidget.setCurrentIndex(1)
        #self.ui.offline.offline_analysis_widgets.setCurrentIndex(0)
        # offline analysis

        self.ui.offline.object_splitter = QSplitter(Qt.Horizontal)



        self.ui.offline.gridLayout.addWidget(self.ui.offline.object_splitter)
        self.ui.offline.object_splitter.addWidget(self.ui.offline.SeriesItems_2)
        self.ui.offline.ap_timer = self.timer
        self.ui.offline.status_label = status_label

        self.ui.offline.offline_manager.set_status_and_progress_bar(status_label, self.ui.progressBar)

        # Check if the program is launched to avoid resize event
        self._not_launched = True
        self.center() #place the MainWindow in the center
        self.setWindowTitle("Biophysical Essentials")

        # set the window geometry to the screen size
        self.desktop = self.screen()
        self.screenRect = self.desktop.availableGeometry()
        self.setCentralWidget(self.ui.centralwidget)
        # Logger for the Main function called start
        self.logger=start_logger

        #darkmode implementation 0 = white, 1 = dark
        self.default_mode = 1
        self.frontend_style = Frontend_Style()
        self.change_to_lightmode()
        # distribute this style object to all other classes to be used
        # whenever the style will be changed, all classes share the same style object and adapt it's appearance
        self.ui.offline.wait_widget = wait_widget
        self.ui.offline.progressbar = self.ui.progressBar

        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        self.local_database_handler = DuckDBDatabaseHandler(self.frontend_style)
        if self.local_database_handler:
            self.statusBar().showMessage("Database Connection Loaded")
        # share the object with offline analysis and database viewer
        self.ui.offline.update_database_handler_object(self.local_database_handler, self.frontend_style, self.ui.notebook)
        self.ui.offline.add_splitter()
        self.ui.database.update_database_handler(self.local_database_handler, self.frontend_style)
        self.ui.online.update_database_handler(self.local_database_handler)
        self.ui.online.frontend_style = self.frontend_style
        self.ui.config.online_analysis = self.ui.online

        self.ui.side_left_menu.hide()
        # this should be later be triggered by  a button click
        self.ui.configuration_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 1))
        self.ui.online_analysis_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 2))
        self.ui.database_viewer_home_2.clicked.connect(self.initialize_database)
        self.ui.home_logo.clicked.connect(self.open_bpe_webside)
        self.ui.toolButton_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 5))
        self.ui.offline_analysis_home_2.clicked.connect(self.insert_row_of_buttons)

        self.ui.offline.go_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.database.HomeButton.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.online.online_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))
        self.ui.config.config_home.clicked.connect(partial(self.ui.notebook.setCurrentIndex,0))

        self.ui.config.go_to_online.clicked.connect(partial(self.ui.notebook.setCurrentIndex,2))
        self.ui.online.batch_config.clicked.connect(partial(self.ui.notebook.setCurrentIndex,1))
        self.ui.config.ui_notebook = self.ui.notebook
        self.ui.config.transfer_to_online_analysis_button.clicked.connect(self.transfer_file_to_online)

    def insert_row_of_buttons(self,grid_layout: QGridLayout):
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
                    if self.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_dir.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_dir_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 1:
                    new_button.clicked.connect(self.start_new_offline_analysis_from_db)
                    if self.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/db.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/db_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 2:
                    new_button.clicked.connect(self.open_analysis)
                    if self.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_existing_results.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/Menu/open_exisiting_results_dark.png", QSize(), QIcon.Normal, QIcon.Off)
                elif col == 3:
                    new_button.clicked.connect(self.go_to_offline_analysis)
                    if self.default_mode == 1:
                        icon.addFile(u"../QT_GUI/Button/light_mode/offline_analysis/go_right.png", QSize(), QIcon.Normal, QIcon.Off)
                    else:
                        icon.addFile(u"../QT_GUI/Button/dark_mode/offline_analysis/go_right.png", QSize(), QIcon.Normal, QIcon.Off)


                if self.default_mode == 1:
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


    def open_analysis(self):
        """_summary_
        """
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(2)
        # here we need a new dialog pop up that shows the offline analysis table and a select box to select the
        self.ui.offline.show_open_analysis_dialog()
        QTest.mouseClick(self.ui.offline_analysis_home_2, Qt.LeftButton)

    def go_to_offline_analysis(self):
        """_summary_
        """
        self.ui.offline.offline_analysis_widgets.setCurrentIndex(0)
        self.ui.notebook.setCurrentIndex(3)
        QTest.mouseClick(self.ui.offline_analysis_home_2, Qt.LeftButton)

    def start_new_offline_analysis_from_dir(self):
        "start new offline analysis, therefore let the user choose a directory and add the data to the database"
        #self.go_to_offline_analysis()
        self.ui.offline.open_directory()

    def start_new_offline_analysis_from_db(self):
        "start new offline analysis, therefore let the user choose a data from the database"
        self.go_to_offline_analysis()
        self.ui.offline.load_treeview_from_database()

    def open_bpe_webside(self):
        """
        open the webside of BPE
        """
        import webbrowser
        url = "https://www.google.com/"
        webbrowser.open(url, new=0, autoraise=True)

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


    def transfer_file_to_online(self):
        """Function to transfer the Patchmaster generated .Dat file to the online Analysis
        for further analysis
        """
        file_path = self.ui.config.get_file_path()
        self.ui.config.set_dat_file_name(self.ui.config.experiment_type_desc.text())
        self.ui.online.open_single_dat_file(str(file_path))

    def quit_application(self):
        """ Function to quit the app"""
        QCoreApplication.quit()

    def change_to_lightmode(self):
        """DarkMode LightMode Switch
        """

        if self.get_darkmode() == 1:
            self.set_darkmode(0)
            #self.apply_stylesheet(self, "light_blue.xml", invert_secondary=True)
            self.apply_stylesheet(self, 'dark_mode.xml', invert_secondary=False)
            # open the extension from the css file
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button.css") as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
                #self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_light())
                #self.frontend_style.change_canvas_bright()
            #self.ui.database_viewer_home_2.setIcon(QIcon("../QT_GUI/Button/welcome_page/db_welcome_dark.png"))

        else:
            self.set_darkmode(1) # set the darkmode back to 1 for the switch
            self.apply_stylesheet(self, f"{os.getcwd()}/StyleFrontend/white_mode.xml", invert_secondary=False)
            with open(f"{os.getcwd()}/QT_GUI/LayoutCSS/Menu_button_white.css") as file:
                self.setStyleSheet(self.styleSheet() +file.read().format(**os.environ))
                #self.ui.side_left_menu.setStyleSheet(self.frontend_style.get_sideframe_dark())
                #self.frontend_style.change_canvas_dark()

        self.ui.config.set_darkmode(self.default_mode)
        self.ui.config.setting_appearance()
        #  make sure to have all popups  in the same changed theme color
        self.frontend_style.current_style=self.default_mode

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
    app.setStyle("Fusion")
    #app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    apply_stylesheet(app, theme="dark_cyan.xml")
    window = MainWindow()
    window.show()
    app.exec()

