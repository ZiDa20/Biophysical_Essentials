from PySide6.QtCore import QSize, Qt, QDir
from PySide6.QtGui import QIcon # type: ignore
from PySide6.QtWidgets import QSplitter, QMainWindow, QToolButton, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel
from PySide6.QtTest import QTest# type: ignore
from qt_material import QtStyleTools
from qt_material import apply_stylesheet
import sys
import os
from functools import partial
import webbrowser
import picologging
from StyleFrontend.frontend_style import Frontend_Style
from Frontend.MainWindow.ui_py.main_window import Ui_MainWindow
from Frontend.OfflineAnalysis.CustomWidget.construction_side_handler import ConstrcutionSideDialog  
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from Backend.tokenmanager import InputDataTypes
import resources

# this is important for pyinstaller to find the right parts of the program
if getattr(sys, 'frozen', False):
    EXE_LOCATION = sys._MEIPASS
else:
    EXE_LOCATION = os.path.dirname( os.path.realpath( __file__ ) )


class MainWindow(QMainWindow, QtStyleTools):

    def __init__(self, testing_db: DuckDBDatabaseHandler = None,  parent = None):
        """Initialize the MainWindow class for starting the Application

        Args:
            parent (QWidget, optional): Can Add a widget here as a parent. Defaults to None.
        """
        super().__init__(parent)
        self.ui: QMainWindow = Ui_MainWindow()
        
        self.ui.setupUi(self)
        self.set_background_logo()
        self.setup_ui()
        self.logger= picologging.getLogger(__name__) # set the logger
        self.logger.info(EXE_LOCATION)
        self.logger.info("Starting the Biophysical Essentials Program!")
        # Create the frontend style for the app
        self.frontend_style = Frontend_Style(self, path = EXE_LOCATION)
        self.frontend_style.change_to_lightmode(self.ui.switch_dark_light_mode)

        self.check_already_executed: bool  = None
        # set the custom app icon
        custom_icon = QIcon(r':Frontend/Button/light_mode/offline_analysis/bpe_logo_small.png')
        self.setWindowIcon(custom_icon)
  
        # handler functions for the database and the database itself
        # only one handler with one database will be used in this entire program
        if testing_db:
            self.local_database_handler = testing_db
        else:
            self.local_database_handler = DuckDBDatabaseHandler(self.frontend_style, database_path = os.path.join( EXE_LOCATION, "database" ))

        self.online_database = DuckDBDatabaseHandler(self.frontend_style,
                                                    db_file_name = "online_db",
                                                    in_memory = True,
                                                    )
        if self.local_database_handler:
            self.statusBar().showMessage("Program Started and Database Connected:")
        # share the object with offline analysis and database viewer

        
        self.setup_offline_style() # connects to the offline analysis
        self.setup_config_online_style() # connects to the online analysis and database viewer
        self.ui.side_left_menu.hide()
        self.connect_buttons_start()
    
    def dark_light_mode_switch_handling(self):
        "switch the mode of the app upon button click"
        # make sure offline analysis page 1 was visited only
        # list l has entires for every selected series to be analyzed
        l = len(self.ui.offline.offline_tree.tab_list) 
        if l <= 0: 
            self.ui.side_left_menu.hide()
            # clear the button layout to make sure they are relaoded in the correct color 
            layout = self.ui.gridLayout_3
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            tm, pm = self.ui.offline.get_current_tm_pm() # gets the treeivewmanager and plotwidgetmanager of page. 
            self.frontend_style.change_to_lightmode(self.ui.switch_dark_light_mode)
            tm.update_treeviews(pm) # update the treeviews to redraw the delegates in the correct color (if opened once)
        else:
            CustomErrorDialog("Switching between the modes is not allowed after specific series in offline analysis were selected. \n You could start a new offline analysis and switch the color mode before selecting the series to analyze.",self.frontend_style)

    def set_background_logo(self):
        """Set the background logo on the start page only
        """
        style_sheet = (
            "QFrame#frame {"
            "background-image: url(:/Frontend/Button/Logo/welcome_page_background_logo.png);"
            "background-repeat: no-repeat;"
            "background-position: center;"
            "}"
        )

        self.ui.frame.setStyleSheet(style_sheet)

    def setup_ui(self) -> None:
        """Set up the user interface"""
        self.setMinimumSize(1600,800)
        self.setCentralWidget(self.ui.centralwidget)
        self.center() #place the MainWindow in the center
        self.setWindowTitle("BiophysicalEssentials (BPE)")
        
    def setup_offline_style(self) -> None:
        """Connects the start with the offline analysis 
        that all the necessary objects are connected"""
        self.ui.offline.stackedWidget.setCurrentIndex(1)
        self.ui.offline.object_splitter = QSplitter(Qt.Horizontal)
        self.ui.offline.gridLayout.addWidget(self.ui.offline.object_splitter)
        self.ui.offline.object_splitter.addWidget(self.ui.offline.SeriesItems_2)
        self.ui.offline.update_database_handler_object(self.local_database_handler, self.frontend_style, self.ui.notebook)
        self.ui.offline.add_splitter()
        
    def setup_config_online_style(self)-> None:
        """Connects the start with the online analysis and database viewer
        That all the necessary objects are connected"""
        self.ui.online.update_database_handler(self.online_database, self.local_database_handler)
        self.ui.database.update_database_handler(self.local_database_handler, self.frontend_style)
        self.ui.config.update_database_handler(self.local_database_handler, self.frontend_style)
        self.ui.online.frontend_style = self.frontend_style
        self.ui.config.online_analysis = self.ui.online
        self.ui.config.ui_notebook = self.ui.notebook

    def connect_buttons_start(self) -> None:
        """ Connects all the necessary buttons at the start"""
        self.ui.configuration_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 1))
        self.ui.online_analysis_home_2.clicked.connect(partial(self.ui.notebook.setCurrentIndex, 2))
        self.ui.database_viewer_home_2.clicked.connect(self.initialize_database)
        self.ui.home_logo.clicked.connect(self.open_bpe_webside)
        
        self.ui.toolButton_2.clicked.connect(self.handle_settings_page)

        self.ui.offline_analysis_home_2.clicked.connect(self.insert_row_of_buttons)
        self.ui.offline.home_button.clicked.connect(self.show_bpe_home_page)
        self.ui.database.HomeButton.clicked.connect(self.show_bpe_home_page)
        self.ui.online.go_home.clicked.connect(self.show_bpe_home_page)
        self.ui.config.go_home.clicked.connect(self.show_bpe_home_page)
        self.ui.config.go_to_online.clicked.connect(partial(self.ui.notebook.setCurrentIndex,2))
        self.ui.online.batch_config.clicked.connect(partial(self.ui.notebook.setCurrentIndex,1))
        self.ui.switch_dark_light_mode.clicked.connect(self.dark_light_mode_switch_handling)

    def show_bpe_home_page(self):
        """
        show_bpe_home_page: go to the home page and make sure the side left menu becomes hidden: it will becone updated if it needs to be reopened
        """
        if not self.ui.side_left_menu.isHidden():
            self.ui.side_left_menu.hide()
        self.ui.notebook.setCurrentIndex(0)
    def handle_settings_page(self):
        """@todo: implement settings needs
        """
        ConstrcutionSideDialog(self.frontend_style)
        #artial(self.ui.notebook.setCurrentIndex, 5)
        
    def create_button(self, text, image, image_dark, function, param=None):
        """Creates a single button"""
        new_button = QToolButton()
        new_button.setText(text)
        icon = QIcon()
        if self.frontend_style.default_mode == 1:
            new_button.setStyleSheet(u"QToolButton{ background-color: transparent; border: 0px; color: black} QToolButton:hover{background-color: grey;}")
            icon.addFile(f":/Frontend/Button/Menu/{image}", QSize(), QIcon.Normal, QIcon.Off)
        else:
            new_button.setStyleSheet(u"QToolButton{ background-color: transparent; border: 0px; color: white} QToolButton:hover{background-color: grey;}")
            icon.addFile(f":Frontend/Button/Menu/{image_dark}", QSize(), QIcon.Normal, QIcon.Off)
        if param is None:
            new_button.clicked.connect(function)
        else:
            new_button.clicked.connect(partial(function,param))
        new_button.setIcon(icon)
        new_button.setIconSize(QSize(30,30))
        # set the vertical spacing between the icon and the text
        new_button.setFixedSize(200,75)
        new_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        return new_button
    
    def insert_row_of_buttons(self) -> None:
        """
        Function to insert a row of buttons to the start up grid
        """
        
        if self.ui.side_left_menu.isHidden():

            if self.ui.gridLayout_3.count() == 0:
                horizontal_layout = QHBoxLayout()
                buttons = [
                    {"text": "New Analysis From Directory", "image": "open_dir.png", "image_dark": "open_dir_dark.png", "function": self.insert_load_data_buttons},
                    {"text": "New Analysis From Database", "image": "db.png", "image_dark": "db_dark.png", "function": self.start_new_offline_analysis_from_db},
                    {"text": "Open Existing Analysis", "image": "open_existing_results.png", "image_dark": "open_existing_results_dark.png", "function": self.open_analysis},
                    {"text": "Continue", "image": "go_right.png", "image_dark": "go_right_dark.png", "function": self.go_to_offline_analysis}
                ]
                amount_of_buttons = 4 if self.ui.offline.canvas_grid_layout.count()>0 else 3
                for col in range(amount_of_buttons):
                    button = self.create_button(**buttons[col])
                    horizontal_layout.addWidget(button)
        
                self.zero_row_widget = QWidget()
                self.zero_row_widget.setLayout(horizontal_layout)

                # Limit the width of the widget to 75% of the available width
                desired_width = 0.75*self.width()
                self.zero_row_widget.setMinimumWidth(desired_width)
                self.zero_row_widget.setStyleSheet("background-color: transparent")

                # Add the container widget to row 1 of self.ui.gridLayout_3
                self.ui.gridLayout_3.addWidget(self.zero_row_widget, 0, 0, 1, horizontal_layout.count())

                # Center the widget horizontally within the layout
                self.ui.gridLayout_3.setAlignment(Qt.AlignHCenter)

                # make a new row widget 
                self.first_row_widget = None

            self.ui.side_left_menu.show()
        else:
            self.ui.side_left_menu.hide()
    
    def insert_load_data_buttons(self) -> None:
        
  # Create a thin white line QLabel
        line_label = QLabel()
        line_label.setStyleSheet("background-color: white;")
        line_label.setFixedHeight(1)  # Adjust the thickness as needed
        self.ui.gridLayout_3.addWidget(line_label, 1, 0, 1,4)

        if self.first_row_widget is None:

            # Create a new vertical layout
            horizontal_layout = QHBoxLayout()

            # Create buttons
            buttons = [
                #{"text": "Load Unbundled Heka", 
                # "image": "open_heka_unbundled_light.png", 
                # "image_dark": "open_dir_dark.png", 
                # "function": self.start_new_offline_analysis_from_dir,
                # "param": InputDataTypes.UNBUNDLED_HEKA_DATA}, 
                {"text": "Load Bundled Heka", 
                 "image": "open_heka_unbundled_light.png", 
                 "image_dark": "db_dark.png", 
                 "function": self.start_new_offline_analysis_from_dir,
                 "param": InputDataTypes.BUNDLED_HEKA_DATA}, 
                {"text": "Load ABF", 
                 "image": "open_heka_unbundled_light.png", 
                 "image_dark": "open_existing_results_dark.png", 
                 "function": self.start_new_offline_analysis_from_dir,
                 "param": InputDataTypes.ABF_DATA}, 
                {"text": "Load Nanion", 
                 "image": "open_heka_unbundled_light.png", 
                 "image_dark": "go_right_dark.png", 
                 "function": self.start_new_offline_analysis_from_dir,
                 "param": InputDataTypes.NANION_DATA}
            ]

            for col in range(len(buttons)):  # Loop through the buttons list up to amount_of_buttons
                button = self.create_button(**buttons[col])
                horizontal_layout.addWidget(button)

            # Set the vertical layout as the layout for a new QWidget
            self.first_row_widget = QWidget()
            self.first_row_widget.setLayout(horizontal_layout)
            # Add the container widget to row 1 of self.ui.gridLayout_3
            self.first_row_widget.setStyleSheet("background-color: transparent")

            self.ui.gridLayout_3.addWidget(self.first_row_widget, 2, 0, 1, self.ui.gridLayout_3.columnCount())


            # Show the side_left_menu widget
            self.ui.side_left_menu.show()
        else:
            if self.first_row_widget.isHidden():
                self.first_row_widget.show()
            else:
                self.first_row_widget.hide()
        

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

    def start_new_offline_analysis_from_dir(self,data_type)-> None:
        "start new offline analysis, therefore let the user choose a directory and add the data to the database"
        #self.go_to_offline_analysis()
        if self.check_already_executed:
            self.ui.offline.reset_class(path_to_database = os.path.join( EXE_LOCATION, "database" ))
        self.ui.offline.open_directory(data_type)

    def start_new_offline_analysis_from_db(self)-> None:
        "start new offline analysis, therefore let the user choose a data from the database"
        
        if self.check_already_executed:
            self.ui.offline.reset_class(path_to_database = os.path.join( EXE_LOCATION, "database" ))
        self.check_already_executed = self.ui.offline.load_treeview_from_database()
        #self.go_to_offline_analysis()
        
    def open_bpe_webside(self)-> None:
        """open the webside of BPE"""
        url = "https://biophysical-essentials.i-med.ac.at/"
        webbrowser.open(url, new=0, autoraise=True)

    def initialize_database(self)-> None:
        """Initialization of the DataBase using the duckdbhandler"""
        self.ui.notebook.setCurrentIndex(4)
        self.ui.database.show_basic_tables()

    def center(self)-> None:
        """Function to center the application at the start into the middle of the screen"""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    """Main function to start the application"""
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = '1'
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QDir.addSearchPath('button', os.path.join(EXE_LOCATION, 'Frontend/Buttons'))
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    apply_stylesheet(app, theme="dark_cyan.xml")
    window = MainWindow()
    window.show()
    app.exec()

