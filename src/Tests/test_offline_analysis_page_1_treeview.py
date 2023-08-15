from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
from database.data_db import DuckDBDatabaseHandler
from pathlib import Path
sys.path.append(os.getcwd())
import unittest
import sys
import io
import os


class TestFrontPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup an instance of the App running """

        #You suppress here:
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        sys.stdout = sys.__stdout__
        # constructor of the mainwindow
        test_db = cls.set_database()
        cls.database_handler = test_db
        
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

    # check for default: no sweeps, no metadata label
    def test_default_offline_analysis_page_1_treeview_model(self):
        # query the model and check the size 
        print("valid")

    
    # click on the sweeps button and see if the sweep level is part of the df
    def test_sweeps_offline_analysis_page_1_treeview_model(self):
        # query the model and check the size 
        print("valid")

    
    # def test meta data 
    #def test sweeps AND meta data