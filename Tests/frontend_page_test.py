
####################################################################
### UnitTest Class to check the Gui is build properly after pushing
####################################################################

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/src")
from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
import duckdb
import io


class TestFrontPage(unittest.TestCase):
    """ Author MZ --> test the Start Page for validity and for functionality using unittests
    unittests """
    # this will run on a separate thread.

    def setUp(self):
        """Setup an instance of the App running """
        print("setup test case")

        #You suppress here:
        suppress_text = io.StringIO()
        sys.stdout = suppress_text 

        if not QApplication.instance(): # check if app is already and instance if not then build
            self.app = QApplication(sys.argv)
        else:# else use the already established instance
            self.app = QApplication.instance()

        sys.stdout = sys.__stdout__

        # constructor of the mainwindow
        self.ui = MainWindow()
        self.ui.local_database_handler.database.close()
        
    def tearDown(self):
        """Close the App later"""
        self.app.deleteLater()

    def test_menu_buttons(self):
        """Check if the buttons are clickable in the menu and if the notebook is switching appropriately"""
        menu = self.ui.buttons
        home = menu[0] #cjeck the configuration window
        configuration = menu[1] #check the 
        online_analysis = menu[2]
        offline_analysis = menu[3]

        # we should add the statistics window here too 
        statistics = menu[3]
        print(f"current index of the notebook: {self.ui.ui.notebook.currentIndex()}")
        QTest.mouseClick(home, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 0, "Windows are not properly attached")
        QTest.mouseClick(configuration, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 1, "Windows are not properly attached")
        QTest.mouseClick(online_analysis, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 2, "Windows are not properly attached")
        QTest.mouseClick(offline_analysis, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 3, "Windows are not properly attached")
        self.ui.local_database_handler.database.close()
        

    def test_build_gui(self):
        """Test the building of the GUI, also the location and the naming of the Buttons are tested
        """
        menu = self.ui.buttons
        print("testing_approached")
        print(menu[0].text())
        message = "First value and second value are not equal !"
        self.assertEqual(len(menu),6,message)
        self.assertEqual(menu[0].text(),"  Home","Configuration Button not ordered properly")
        self.assertEqual(menu[1].text(),"  Configuration","Online Button not ordered properly")
        self.assertEqual(menu[2].text()," Online Analysis","Online Button not ordered properly")
        self.assertEqual(menu[3].text()," Offline Analysis","Online Button not ordered properly")
        self.ui.local_database_handler.database.close()

    def test_menu_moving(self):
        """Here we test the hamburger Menu when clicked if it opens or closes"""
        self.assertEqual(self.ui.ui.side_left_menu.width(), 100)
        self.ui.local_database_handler.database.close()


    def test_tab_widgets(self):
        """check the number of tabs that are build for each tabWidget,
        can be changed if the number of tabs are changed"""
        self.assertEqual(self.ui.ui.config.self_configuration_notebook.count(),3, "Wrong number of Tabs in configuration")
        self.assertEqual(self.ui.ui.online.online_analysis.count(), 2, "Wrong number of Tabs in online analysis")
        self.ui.local_database_handler.database.close()

    def test_darkmode_switch(self):
        """ Check if the mode opens the darkmode"""
        QTest.mouseClick(self.ui.ui.darkmode_button, Qt.LeftButton)
        self.assertEqual(self.ui.default_mode, 0, "Switch to lightmode not working")
        self.assertEqual(self.ui.ui.side_left_menu.palette().color(self.ui.ui.side_left_menu.backgroundRole()).name(), "#04071a", "wrong color")
        QTest.mouseClick(self.ui.ui.darkmode_button, Qt.LeftButton)
        self.assertEqual(self.ui.ui.side_left_menu.palette().color(self.ui.ui.side_left_menu.backgroundRole()).name(), "#232629", "wrong color")
        print(self.ui.ui.side_left_menu.palette().color(QPalette.Base).name())
        self.assertEqual(self.ui.default_mode, 1, "Switch to darkmod not working")
        self.ui.local_database_handler.database.close()

    def test_check_maximize(self):
        """Check Window functionality when using the maximize button
        """
        QTest.mouseClick(self.ui.ui.pushButton_3,Qt.LeftButton)
        self.assertEqual(self.ui.height(), 1040, "Maximizing does not work properly")
        self.assertEqual(self.ui.width(), 1920, "width not set properly")

        QTest.mouseClick(self.ui.ui.pushButton_3,Qt.LeftButton)
        self.assertEqual(self.ui.height(), 950, "Maximizing does not work properly")
        self.assertEqual(self.ui.width(), 1537, "width not set properly")
        self.ui.local_database_handler.database.close()

    def test_check_notebook_widgets_exist(self):
        """ Check if the object are initialized"""
        self.assertIsNotNone(self.ui.ui.config, "config Widget not build")
        self.assertIsNotNone(self.ui.ui.online, "Online Analysis is not build")
        self.assertIsNotNone(self.ui.ui.offline, "OFfline Analysis is not build")
        self.assertIsNotNone(self.ui.ui.home, "Home is not build")
        self.assertIsNotNone(self.ui.ui.settings, "Setting App is not build")
        self.ui.local_database_handler.database.close()

    def test_check_current_window_open(self):
        """ Check if the right notebook index opened directed to the home position of the application"""
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 0, "Wrong Notebook Side opened")
        self.ui.local_database_handler.database.close()
        

    def test_check_database_initiated(self):
        """ Check if database if properly assigned constructed"""
        self.ui.local_database_handler.init_database()
        analysis_table = self.ui.local_database_handler.database.execute("Select ANALYSIS_ID from offline_analysis")
        experiment = self.ui.local_database_handler.database.execute("Select * from experiments")
        self.assertEqual(analysis_table.fetchall()[0][0], 1 , "no database")
        self.assertEqual(experiment.fetchall(), 1 , "no database")
       

    """
    def test_check_database_table_generated(self):
        self.ui.local_database_handler.init_database()
        analysis_table = self.ui.local_database_handler.database.execute("select * from experiments")
        #experiment = self.ui.local_database_handler.database.execute("Select * from experiments")
        self.assertEqual(analysis_table.fetchall()[0][0], 1 , "no database")
        #self.assertEqual(experiment.fetchall(), 1 , "no database")
        self.ui.local_database_handler.database.close()
    """   

if __name__ == '__main__':
    unittest.main()
