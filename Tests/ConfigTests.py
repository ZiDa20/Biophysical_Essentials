####################################################################
### UnitTest Class to check the Gui is build properly after pushing
####################################################################

import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/src")


####################################################################
# Import Modules
####################################################################
from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
import duckdb
import io
import pathlib as pl


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        """Is asserting if a file exists

        Args:
            path (string): A String with the location of the file

        Raises:
            AssertionError: Should be evoked if file is not exisiting
        """        
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))


class TestConfigWidget(TestCaseBase):
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
    
    
    def test_batch_file(self):
        """Checks for the proper building of the E9Batch.In File
        since the out file is builded by the Patchmaster
        """        
        QTest.mouseClick(self.ui.ui.self_configuration, Qt.LeftButton)
        self.ui.ui.config.batch_path = os.getcwd() # retrieve the batch path
        self.ui.ui.config.backend_manager._batch_path = os.getcwd()
        QTest.mouseClick(self.ui.ui.config.establish_connection_button,Qt.LeftButton)
        self.assertIsFile(self.ui.ui.config.batch_path + "\\E9Batch.In")

    def test_loading_of_setup_files(self):
        """Tests if the setup_files (pgf, protocol, online-analysis files)
        are loaded properly. 
        Can only be tested if patchmaster is active and communication is working
         """        
        QTest.mouseClick(self.ui.ui.self_configuration, Qt.LeftButton) # open the batch communication
        self.ui.ui.config.batch_path = os.getcwd() # retrieve the batch path
        self.ui.ui.config.pgf_file = os.getcwd() +"\\setup_files\\Excitability_02.pgf" # load testfiles
        self.ui.ui.config.pro_file = os.getcwd() +"\\setup_files\\Excitability_02.pro" 
        self.ui.ui.config.onl_file = os.getcwd() +"\\setup_files\\Excitability_02.onl"
        self.ui.ui.config.backend_manager._batch_path = os.getcwd() 
        QTest.mouseClick(self.ui.ui.config.establish_connection_button,Qt.LeftButton) # click established connection
        
        itemsTextList =  [str(self.ui.ui.config.SeriesWidget.model().item(i).text()) for i in range(self.ui.ui.config.SeriesWidget.model().rowCount())]
        protocolText =  [str(self.ui.ui.config.protocol_widget.model().item(i).text()) for i in range(self.ui.ui.config.protocol_widget.model().rowCount())]
        self.assertEqual(itemsTextList[0:4], ["Block Pulse","IV","IV-120","IV-40"], "PGF file is not properly opened")
        self.assertEqual(protocolText[0:4], ["Test Pulse","IV & Rheo","2xRheo&Ramp","Heat Ramp"], "Protocol file is not properly opened")


    
    
if __name__ == '__main__':
    unittest.main()
