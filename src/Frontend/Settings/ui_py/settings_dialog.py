import sys
import os
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from Backend.DeviceAPI.BCamera import * 
from Frontend.Settings.ui_py.settings_designer import Ui_Form
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from functools import partial
from Frontend.CustomWidget.user_notification_dialog import UserNotificationDialog
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from Backend.Settings.SettingsFileHandler import SettingsFileHandler
from StyleFrontend.frontend_style import Frontend_Style

class SettingsWindow(QWidget,Ui_Form):
    """
    SettingsWindow Handler for frontend interactions with the settings menu

    Args:
        QWidget (_type_): _description_
        Ui_Form (_type_): _description_
    """
    def __init__(self,parent = None):
        self.parent = parent
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.page_headline.setStyleSheet("font-size:20pt;")
        self.label_3.setStyleSheet("font-size:12pt;")
        self.local_database_handler = None
        self.frontend_style = None
        self.settings_file_handler = None
        self.connect_database_buttons()
        
    def connect_database_buttons(self):
        """
        connect_database_buttons: connect the buttons with a function
        """
        self.select_db_path_button.clicked.connect(self.change_db_path)
        self.create_database_button.clicked.connect(self.create_new_database)
        self.search_existing_db_button.clicked.connect(self.search_existing_db)
        self.connect_to_existing_db_button.clicked.connect(self.connect_to_existing_db)
        self.restore_db_defaults_button.clicked.connect(self.restore_db_defaults)

    def update_displayed_data(self,EXE_LOCATION:str):
        """
        update_displayed_data function will be called from external and fills the data to be displayed/updated

        Args:
            EXE_LOCATION (str): the absolute path of start.py file
        """
        self.EXE_LOCATION = EXE_LOCATION
        self.fill_database_data()

    def update_object_handlers(self, local_database_handler:DuckDBDatabaseHandler, 
                               frontend_style:Frontend_Style,
                               settings_file_handler:SettingsFileHandler,
                               scheduled_restart):
        """
        update_object_handlers overrides the global objects initialized in start.py

        Args:
            local_database_handler (DuckDBDatabaseHandler): _description_
            frontend_style (Frontend_Style): _description_
            settings_file_handler (SettingsFileHandler): _description_
            scheduled_restart (_type_): _description_
        """
        self.local_database_handler = local_database_handler
        self.frontend_style = frontend_style
        self.settings_file_handler = settings_file_handler
        self.scheduled_restart = scheduled_restart

    def change_db_path(self):
        """
        change_db_path: opens on button click, displays a file dialog and allows the user to select a directory
        """
        new_path = QFileDialog.getExistingDirectory(self, "Select Directory", QDir.currentPath())
        if new_path:
            # Update the UI to reflect the new directory
            self.db_path_lineEdit.setText(new_path)

    def fill_database_data(self):
        """
        fill_database_data: set the text of the labels in the database
        """
        path = self.settings_file_handler.get_bpe_database_path()
        if not os.path.isabs(path):
               path = os.path.join(self.EXE_LOCATION,path)
        path = os.path.join(path, self.settings_file_handler.get_bpe_database_name())
        self.current_database_label.setText(path)

    def create_new_database(self):
        """
        create_new_database: overrides the config file parameter values and restarts BPE.
        Error checks are performed for empty line edits
        """
        path = self.db_path_lineEdit.text()
        if path == "":
            CustomErrorDialog("The path must not be empty",self.frontend_style)
            return
        name = self.db_name_line_edit.text()
        if name == "":
            CustomErrorDialog("The name must not be empty",self.frontend_style)
            return

        # if the user didnt enter the db file extension, add it manually
        if ".db" not in name:
            name = name + ".db"
            
        self.settings_file_handler.set_bpe_database_path(path)
        self.settings_file_handler.set_bpe_database_name(name)

        self.shutdown_app()
        
    def search_existing_db(self):
        """
        search_existing_db: opens a file dialog and allows the user to search for a file with the .db extension
        Updates the label to the selected 
        """
        db_file,_ = QFileDialog.getOpenFileName(self,"Select exisiting BPE database file", "","*.db")
        self.existing_db_lineEdit.setText(db_file)

    def connect_to_existing_db(self):
        """
        connect_to_existing_db: overwrites the database path and name in the config file before shutting down the app
        """
        input_string = self.existing_db_lineEdit.text()
        if input_string == "":
            CustomErrorDialog("The db file name must not be empty",self.frontend_style)
            return

        directory_path, filename = os.path.split(input_string)
        self.settings_file_handler.set_bpe_database_path(directory_path)
        self.settings_file_handler.set_bpe_database_name(filename)

        self.shutdown_app()

    def restore_db_defaults(self):
        """
        restore_db_defaults: reset database path and database name settings to default
        """
        self.settings_file_handler.reset_bpe_database_path()
        self.settings_file_handler.reset_bpe_database_name()
        #self.SCHEDULED_RESTART = True
        self.shutdown_app()

    def shutdown_app(self):
        """
        shutdown_app: showing a user notifcation which must be closed and upon closing the app becomes shutdown
        """
        UserNotificationDialog("Done. The app will now shut down to ensure the database change will be acknowledged by all modules. \n Afterwords you can restart the program as usual.", self.frontend_style)

        """Restart the application."""
        python_executable = sys.executable
        os.execl(python_executable, python_executable, *sys.argv)


    # old version: might be useful to be upcycled
    """"   
        settings_buttons = [self.Set_default_user, self.initialize_devices, self.plot_appearance, self.save_location, self.connect_to_webserver]
        for index, button in enumerate(settings_buttons):
            button.clicked.connect(partial(self.stackedWidget_4.setCurrentIndex, index))
        self.pushButton_13.clicked.connect(self.initialize_camera)
    
    def switch_modes(self):
        with open('Menu_button.css') as file:
            self.setStyleSheet(self.start.styleSheet() +file.read().format(**os.environ))

    def initialize_camera(self):
        #""" 
        #Basler camera initalizing  
        #ToDO: Error handling, add multiple camera possibilites for capturing in the dropdown menu
        #"""

        #self.camera = BayerCamera()
        #initialize the camera 
        #camera_status = self.camera.init_camera()
        #self.scence_trial = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        #print("stuff worked")
        
    #def quit(self):
        #self.close()
    
    #"""

    

