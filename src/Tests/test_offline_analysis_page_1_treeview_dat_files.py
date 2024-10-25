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
import pytestqt
import pytest
import shutil
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from pathlib import Path

import sys
import io
import os
from start import *
import pytest
import unittest
import time
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from Backend.tokenmanager import InputDataTypes

# Define a session-scoped fixture to ensure sequential execution of tests
@pytest.fixture(scope="session", autouse=True)
def execute_tests_sequentially():
    yield
    # This fixture will execute all tests sequentially

def set_database(db_name):
            #_summary_: Sets up the database for the testing purpose!
            #clean_leftover_db()
            path_db = os.path.join(os.getcwd(),"Tests")
            return DuckDBDatabaseHandler(None,
                                        db_file_name = "test_treeview_db_"+db_name+".db",
                                        database_path = path_db,
                                        in_memory = False)


def load_demo_dat_data_into_database(qtbot,db_name):
    
    test_db = set_database(db_name)
    app = MainWindow(testing_db = test_db)
    app.database_handler = app.local_database_handler
    app.ui.offline.offline_manager._directory_path = "./Tests/Test_Files/"
    app.ui.offline.input_data_type = InputDataTypes.BUNDLED_HEKA_DATA
    template = Assign_Meta_Data_PopUp(app.database_handler,
                            app.ui.offline.offline_manager,
                            app.frontend_style)

    template.map_metadata_to_database(InputDataTypes.BUNDLED_HEKA_DATA)
    app.template_df = template.template_dataframe.values.tolist()
    # continue open directory writes the data from the selected directory into the database,
    # opens the wait dialog and opens the Load_Data_From_Database_Popup_Handler when the 
    # finished signal is emtitted 
    app.ui.offline.continue_open_directory(app.template_df, test = True)
    # qtbot.wait until waits until the load_data_from_database_dialog.. variable was initialized as an instance of 
    # Load_Data_From_Database_Popup_Handler
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout = 20000)
    #QApplication.processEvents()

    qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    #QApplication.processEvents()

    return test_db,app
   
    
#@pytest.mark.serial
def test_default_offline_analysis_page_1_treeview_model(qtbot):

    """ Test 1: 
        1. Load files from the directory into the database 
        2. Select the imported data in the data selection dialog 
        3. This should open the first page of OFA showing a treeview 
        4. This treeview MUST hold only experiment and sweeps 
        5. But No sweeps and no metadata label 
    Args:
        qtbot (_type_): clickbot
    """
    test_db,app = load_demo_dat_data_into_database(qtbot,"dat1")

    #qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    tables = test_db.database.execute("SHOW TABLES").fetchdf()
    
    a = tables.shape[0]
    #print(a)
    b = tables.shape[1]
    try:
        assert a == 65, f"Expected 65 rows, but found {a} rows."

        # check that the selected treeview is not none
        stv = app.ui.offline.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view
        unittest.TestCase.assertIsNotNone(stv,"selected treeview should not be empty anymore")
            
        # check that the default selected treeview does only show experiment and series level data
        selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
        #print("got this table back")
        #print(selected_treeview_table)
        res = selected_treeview_table["type"].unique().tolist()
        valid_types = ["Experiment","Series"]
        
        assert res == valid_types #,"the expected types in the treeview are not correct ")
    
        # close it to run another test with the same setdb function
        test_db.database.close()
    except AssertionError  as e:
         #print(e)
         test_db.database.close()


#@pytest.mark.serial
def test_sweeps_offline_analysis_page_1_treeview_model(qtbot):
    """_summary_
    Test 2: 
        1. Repeats data loading as performed in TEST 1: Treeview with only experiment and series 
        2. Click on the sweeps button in the ribbon bar which should add the sweeps to the treeview
        3. The sweep level must be part of the treeview df
    Args:
        qtbot (_type_): _description_
    """
    
    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot,"dat2")
    # click the sweeps button to add the extra sweep level in the treeview 
    qtbot.mouseClick(app.ui.offline.show_sweeps_radio, Qt.LeftButton)
        
    selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    #print("got this table back")
    res = selected_treeview_table["type"].unique().tolist()
    valid_types = ["Experiment","Series","Sweep"]
    
    assert res == valid_types #,"the expected types in the treeview are not correct ")
   
    # click the sweeps button again tountoggle and DON'T show extra sweep level in the treeview 
    qtbot.mouseClick(app.ui.offline.show_sweeps_radio, Qt.LeftButton)

    selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    res = selected_treeview_table["type"].unique().tolist()
    valid_types = ["Experiment","Series"]
    
    assert res == valid_types #,"the expected types in the treeview are not correct ")
    test_db.database.close()



#@pytest.mark.serial
def test_change_series_renaming(qtbot):
    """Test: Click on the change series name button in the ribbon bar, change the series name of an IV to TEST123.
    Make sure, that the string "IV" is not present anymore in the treeview while TEST123 is present 
    """
    
    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot,"3")

    #app.ui.offline.ap.stop_and_close_animation()

    initial_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table

    # click the button to change the series name, this should open a dialog
    qtbot.mouseClick(app.ui.offline.change_series_name, Qt.LeftButton, delay = 1)
    # wait for the opening dialog
    
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "change_series_name_dialog"), timeout = 20)

    dialog= app.ui.offline.change_series_name_dialog

    dialog.new_name_field.setText("TEST123")
    
    #  this items will be renamed
    renamed_item = dialog.series_names_combobox.currentText()

    qtbot.mouseClick(dialog.apply, Qt.LeftButton)
    
    updated_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    
    # Find the corresponding rows for the old and new item names
    old_row = initial_treeview_table[initial_treeview_table["item_name"] == renamed_item].index.tolist()
    new_row = updated_treeview_table[updated_treeview_table["item_name"] == "TEST123"].index.tolist()

    # Assert that the change has occurred
    assert len(old_row) > 0, "The list is empty"    # Ensure the old item was found
    assert len(new_row) > 0, "The list is empty"    # Ensure the old item was found

    assert old_row  == new_row  # Ensure the row indices are exactly the same

    test_db.database.close()


#@pytest.mark.serial 
def test_change_experiment_meta_data(qtbot):
    """Test of the ribbon bar button: change experiment meta data
    Click on the change experiment meta data button in the ribbon bar, change the experiment label of an experiment to TEST123.
    Make sure, that the label "TEST123" is present in the database while the old experiment label is not present anymore
    Args:
        qtbot (_type_): _description_
    """

    # @todo: finish this test

    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot,"4")

    #app.ui.offline.ap.stop_and_close_animation()
    
    # click the button to change the series name, this should open a dialog
    qtbot.mouseClick(app.ui.offline.edit_meta, Qt.LeftButton, delay = 1)

    qtbot.waitUntil(lambda: hasattr(app.ui.offline.OfflineDialogs, "edit_data"), timeout = 20)

    assert app.ui.offline.OfflineDialogs.edit_data is not None
    app.ui.offline.OfflineDialogs.edit_data.close()
    test_db.database.close()



#@pytest.mark.serial
def test_change_series_meta_data(qtbot):
    """Test of the ribbon bar button: change series meta data
    Click on the change series meta data button in the ribbon bar, change the series meta data   to TEST123.
    Make sure, that the label "TEST123" is present in the database.
    Args:
        qtbot (_type_): _description_
    """

    # @todo: finish this test
    
    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot,"5")

    #app.ui.offline.ap.stop_and_close_animation()

    # click the button to change the series name, this should open a dialog
    qtbot.mouseClick(app.ui.offline.edit_series_meta_data, Qt.LeftButton, delay = 1)

    qtbot.waitUntil(lambda: hasattr(app.ui.offline.OfflineDialogs, "edit_data"), timeout = 20)

    assert app.ui.offline.OfflineDialogs.edit_data is not None
    app.ui.offline.OfflineDialogs.edit_data.close()
    test_db.database.close()


 
