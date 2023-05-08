
####################################################################
### UnitTest Class to check the Gui is build properly after pushing
####################################################################
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

        if not QApplication.instance(): # check if app is already and instance if not then build
            cls.app = QApplication(sys.argv)
        else:# else use the already established instance
            cls.app = QApplication.instance()

        sys.stdout = sys.__stdout__
        # constructor of the mainwindow
        test_db = cls.set_database()
        cls.ui = MainWindow(testing_db = test_db)
        cls.database_handler = cls.ui.local_database_handler
        cls.configuration = cls.ui.ui.configuration_home_2 #check the
        cls.online_analysis = cls.ui.ui.online_analysis_home_2
        cls.database_viewer = cls.ui.ui.database_viewer_home_2
        cls.offline_analysis = cls.ui.ui.offline_analysis_home_2


    @classmethod
    def set_database(cls):
        """_summary_: Sets up the database for the testing purpose!
        """
        return DuckDBDatabaseHandler(None,
                                    db_file_name = "test_db.db",
                                    in_memory = False)
    def tearDown(self):
        """Close the App later"""
        self.app.deleteLater()

    def test_writing_database(self):
        data = self.database_handler.database.execute("Show Tables;").fetchdf()
        self.assertEqual(data.shape[0], 63, "nope not true")

    def test_check_database_initiated(self):
        """ Check if database if properly assigned constructed"""
        show_tables = self.database_handler.database.execute("Select * from offline_analysis;").fetchdf()
        all_tables = self.database_handler.database.execute("SHOW TABLES;").fetchdf()
        self.assertEqual(show_tables.shape[0], 10 , "no database")
        self.assertEqual(all_tables.shape[0], 25 , "no database")
        # should be a property of the database_hanlder instead of a open variable
        self.assertEqual(self.database_handler.analysis_id, 1)

    def test_menu_buttons(self):
        """Check if the buttons are clickable in the menu and if the notebook is switching appropriately"""
        # we should add the statistics window here too
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
        self.assertEqual(self.ui.ui.config.self_configuration_notebook.count(),3, "Wrong number of Tabs in configuration")
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

    ###############################################################
    # Check Database function that read from database
    ###############################################################

    def test_sweep_tables_return(self):
        sweep_tables = self.database_handler.get_sweep_table_names_for_offline_analysis("IV")
        self.assertEqual(len(sweep_tables), 23, "There are side effects which changed the database")

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

    def test_get_experiment_name_by_label(self):
        #
        # here only condition is checked which makes not a lot of sense @toDO
        #experiment_names = self.database_handler.get_experiment_names_by_experiment_label("Aps")
        pass

    def test_get_analysis_id_from_analysis_function_id(self):
        """_summary_
        """
        iden = self.database_handler.get_analysis_function_name_from_id(1)
        iden_2 = self.database_handler.get_analysis_function_name_from_id(2)
        self.assertEqual(iden, "max_current", "not true")
        self.assertIsInstance(iden, str, f"Should be a analysis function name with type str not {type(iden)}")
        self.assertEqual(iden_2, None, "This analysis function id is not mapped here")

    def test_get_analysis_id_from_analysis_function_id(self):
        iden = self.database_handler.get_analysis_series_name_by_analysis_function_id(2)
        iden2 = self.database_handler.get_analysis_series_name_by_analysis_function_id(3)
        self.assertEqual(iden, "Rheobase", f"Should be Rheobase and not {iden2}")
        self.assertEqual(iden2, "Rheobase", f"Should be RheoRamp and not {iden2}")

    def test_get_cursor_bounds_from_analysis_id(self):
        cursor_bounds = self.database_handler.get_cursor_bounds_of_analysis_function(1, "Peak-Detection")
        self.assertIsInstance(cursor_bounds, list, f"Should be a list(tuple), and not a {type(cursor_bounds)}")
        self.assertEqual(cursor_bounds, [])

    def test_get_analysis_series_names_for_specific_analysis_id(self):
        analysis_series_names = self.database_handler.get_analysis_series_names_for_specific_analysis_id()
        self.assertEqual(analysis_series_names, [('Rheobase',), ('5xRheo',)], """Should be of type list(tuple),
                                                                           holding IV and Cclamp and not {analysis_series_name}""")

if __name__ == '__main__':
    unittest.main()
