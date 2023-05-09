
####################################################################
### UnitTest Class to check the Gui is build properly after pushing
####################################################################
import sys
import unittest
import os
import numpy as np
sys.path.append(os.getcwd())
from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest
import duckdb
import io
import pandas as pd
from pytestqt import qtbot
from database.data_db import DuckDBDatabaseHandler
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp


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
        sys.stdout = sys.__stdout__
        # constructor of the mainwindow
        test_db = cls.set_database()
        cls.database_handler = test_db
        
    @classmethod
    def set_database(cls):
        """_summary_: Sets up the database for the testing purpose!
        """
        return DuckDBDatabaseHandler(None,
                                    db_file_name = "test_db.db",
                                    database_path = "./Tests/",
                                    in_memory = False)
    @classmethod
    def tearDownClass(cls):
        """Close the App later"""
        cls.database_handler.database.close()

    def test_database_handler_attribute(self):
        """ Assert the initialization of the DuckDB Database handler"""
        self.assertTrue(hasattr(self.database_handler, "logger"), "no logger")
        self.assertTrue(hasattr(self.database_handler, "db_file_name"), "no db file name")
        self.assertTrue(hasattr(self.database_handler, "database_path"), "no database path")

    def test_get_values_from_database(self):
        """ Checks if the data retrieved is of right type"""
        liste_data = self.database_handler.get_data_from_database(self.database_handler.database,"SHOW TABLES;")
        numpy_data = self.database_handler.get_data_from_database(self.database_handler.database,"SHOW TABLES;",fetch_mode = 1)
        dataframe_data = self.database_handler.get_data_from_database(self.database_handler.database,"SHOW TABLES;",fetch_mode = 2)
        self.assertIsInstance(liste_data, list)
        self.assertIsInstance(dataframe_data, pd.DataFrame)
        
    def test_writing_database(self):
        data = self.database_handler.database.execute("Show Tables;").fetchdf()
        self.assertEqual(data.shape[0], 63, "nope not true")

    def test_check_database_initiated(self):
        """ Check if database if properly assigned constructed"""
        show_tables = self.database_handler.database.execute("Select * from offline_analysis;").fetchdf()
        all_tables = self.database_handler.database.execute("SHOW TABLES;").fetchdf()
        self.assertEqual(show_tables.shape[0], 2 , "no database")
        self.assertEqual(all_tables.shape[0], 63 , "no database")
        # should be a property of the database_hanlder instead of a open variable

    def test_get_sweep_table_return(self):
        # here we retrieve the sweep table for two experiment
        # 140206_02, 201228_03
        data_table_1 = self.database_handler.get_sweep_table_name("220315_01", "Series2")
        data_table_2 = self.database_handler.get_sweep_table_name("220315_02", "Series2")
        self.assertRaises(TypeError, self.database_handler.get_sweep_table_name, 1, "Series_2")
        self.assertEqual(data_table_1, "imon_signal_220315_01_Series2", "Wrong table identified")
        self.assertEqual(data_table_2, "imon_signal_220315_02_Series2", "Wrong table identified")

    def test_get_meta_data_group_experiment(self):
        """_summary_:
        """
        meta_1 = self.database_handler.get_meta_data_group_of_specific_experiment("220315_01")
        meta_2 = self.database_handler.get_meta_data_group_of_specific_experiment("220315_02")
        self.assertRaises(TypeError, self.database_handler.get_meta_data_group_of_specific_experiment,1)
        self.assertEqual(meta_1, 'None', "Wrong metadata type check if TestDatabase is correct")
        self.assertEqual(meta_2, 'None', "Wrong metadata type check if TestDatabase is correct")

    def test_get_cslow_value(self):
        """_summary_
        """
        cslow = self.database_handler.get_cslow_value_for_sweep_table("imon_signal_220315_02_Series2")
        self.assertEqual(cslow, 1.4535422426504894e-11 , "not true")
        self.assertIsInstance(cslow, float, "wrong type returned")

    def test_metadata_files(self):
        metadata = self.database_handler.database.execute("SELECT * from global_meta_data").fetchdf()
        self.assertEqual(metadata.shape[0], 2)
        self.assertEqual(metadata["condition"].tolist()[0], "None")
        self.assertEqual(metadata["condition"].tolist()[1], "None")
        self.assertEqual(metadata["experiment_name"].tolist(), ["220315_01", "220315_02"])

    def test_result_table(self):
        result = self.database_handler.database.execute("SELECT * from results").fetchdf()
        self.assertEqual(result.shape[0], 0)

    def test_get_experiment_name_by_label(self):
        #
        # here only condition is checked which makes not a lot of sense @toDO
        #experiment_names = self.database_handler.get_experiment_names_by_experiment_label("Aps")
        pass

    def test_series_per_experiment(self):
        """ Test the series per experiment"""
        series_1 = self.database_handler.database.execute("SELECT * from experiment_series WHERE experiment_name = (?)", ["220315_01"]).fetchdf()
        series_2 = self.database_handler.database.execute("SELECT * from experiment_series WHERE experiment_name = (?)", ["220315_02"]).fetchdf()
        self.assertEqual(series_1.shape[0], 13)
        self.assertEqual(series_2.shape[0], 4)

    def test_get_ymin_from_table(self):
        """test metadata with ymin from the metadata table"""
        sweep_1 = self.database_handler.get_ymin_from_metadata_by_sweep_table_name("imon_signal_220315_01_Series2","sweep_1")
        sweep_2 = self.database_handler.get_ymin_from_metadata_by_sweep_table_name("imon_signal_220315_01_Series2","sweep_2")
        sweep_3 = self.database_handler.get_ymin_from_metadata_by_sweep_table_name("imon_signal_220315_01_Series2","sweep_3")
        sweep_4 = self.database_handler.get_ymin_from_metadata_by_sweep_table_name("imon_signal_220315_01_Series2","sweep_4")
        self.assertEqual(sweep_1, (-1.2481343958370417e-08, 1.7513712702310613e-09))
        self.assertEqual(sweep_2, (-1.2238209556869606e-08, 1.6921087864218975e-09))
        self.assertEqual(sweep_3, (-1.22723475826092e-08, 1.689834494555953e-09))
        self.assertEqual(sweep_4, (-1.2198881904623704e-08, 1.6889497578276291e-09))

    
        
if __name__ == '__main__':
    unittest.main()
