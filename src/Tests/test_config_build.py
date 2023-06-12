import sys

import unittest
import os
sys.path.append(os.getcwd())
from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
import duckdb
import io
import qbstyles
from pathlib import Path


class TestFrontPage(unittest.TestCase):
    """ Author MZ --> test the Start Page for validity and for functionality using unittests
    unittests """
    # this will run on a separate thread.
    @classmethod
    def setUpClass(cls):
        """Setup an instance of the App running """
      
        #You suppress here:
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 

        if not QApplication.instance(): # check if app is already and instance if not then build
            cls.app = QApplication(sys.argv)
        else:# else use the already established instance
            cls.app = QApplication.instance()

        sys.stdout = sys.__stdout__

        # constructor of the mainwindow
        testing_db = cls.set_database()
        
        cls.ui = MainWindow(testing_db=testing_db)
        cls.database_handler = cls.ui.local_database_handler
        df = cls.database_handler.database.execute("SHOW TABLES;").fetch_df()

        cls.configuration = cls.ui.ui.configuration_home_2 #check the 
        cls.online_analysis = cls.ui.ui.online_analysis_home_2
        cls.database_viewer = cls.ui.ui.database_viewer_home_2
        cls.offline_analysis = cls.ui.ui.offline_analysis_home_2

    @classmethod
    def set_database(cls):
        """_summary_: Sets up the database for the testing purpose!
        """
        path_db = os.getcwd() + "/Tests/"
        path_db = str(Path(path_db)) 
        return DuckDBDatabaseHandler(None,
                                    db_file_name = "test_db.db",
                                    database_path = path_db,
                                    in_memory = False)
    
    @classmethod
    def tearDownClass(cls):
        """Close the App later"""
        cls.database_handler.database.close()
        cls.app.deleteLater()
        


    def test_menu_buttons(self):
        """Check if the buttons are clickable in the menu and if the notebook is switching appropriately"""
        
        # we should add the statistics window here too 
        print(f"current index of the notebook: {self.ui.ui.notebook.currentIndex()}")
        QTest.mouseClick(self.configuration, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 1, "Windows are not properly attached")
        QTest.mouseClick(self.online_analysis, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 2, "Windows are not properly attached")
        QTest.mouseClick(self.offline_analysis, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 2, "Windows are not properly attached")
        QTest.mouseClick(self.database_viewer, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 4, "Windows are not properly attached")

    def test_build_gui(self):
        """Test the building of the GUI, also the location and the naming of the Buttons are tested
        """
        self.assertEqual(self.configuration.text(),"Configuration","Online Button not ordered properly")
        self.assertEqual(self.online_analysis.text(),"Online Analysis","Online Button not ordered properly")
        self.assertEqual(self.offline_analysis.text(),"Offline Analysis","Online Button not ordered properly")
    
    def test_tab_widgets(self):
        """check the number of tabs that are build for each tabWidget,
        can be changed if the number of tabs are changed"""
        self.assertEqual(self.ui.ui.config.experiment_control_stacked.count(),2, "Wrong number of Stacked Widgets in configuration")
        self.assertEqual(self.ui.ui.online.online_analysis.count(), 3, "Wrong number of Tabs in online analysis")
     
    def test_check_notebook_widgets_exist(self):
        """ Check if the object are initialized"""
        self.assertIsNotNone(self.ui.ui.config, "config Widget not build")
        self.assertIsNotNone(self.ui.ui.online, "Online Analysis is not build")
        self.assertIsNotNone(self.ui.ui.offline, "OFfline Analysis is not build")
        self.assertIsNotNone(self.ui.ui.home, "Home is not build")
        self.assertIsNotNone(self.ui.ui.settings, "Setting App is not build")
   
    def test_check_current_window_open(self):
        """ Check if the right notebook index opened directed to the home position of the application"""
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 0, "Wrong Notebook Side opened")

    def test_check_current_index_exp(self):
        "Checks that the right page is loaded at the beginning in the experimentator"
        self.assertEqual(self.ui.ui.config.experiment_control_stacked.currentIndex(), 0, "Wrong page loaded pls check the files")
    
    
