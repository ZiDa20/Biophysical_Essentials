import unittest
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/src")
#sys.path.append(os.path.dirname(os.getcwd()) + "/QT_GUI")
from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
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
        configuration = menu[0] #cjeck the configuration window
        online = menu[1] #check the 
        offline = menu[2]

        # we should add the statistics window here too 
        statistics = menu[3]
        print(f"current index of the notebook: {self.ui.ui.notebook.currentIndex()}")
        QTest.mouseClick(configuration, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 0, "Windows are not properly attached")
        QTest.mouseClick(online, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 1, "Windows are not properly attached")
        QTest.mouseClick(offline, Qt.LeftButton)
        self.assertEqual(self.ui.ui.notebook.currentIndex(), 2, "Windows are not properly attached")
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

    

if __name__ == '__main__':
    unittest.main()
