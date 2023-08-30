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
from database.data_db import DuckDBDatabaseHandler
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from pathlib import Path

import sys
import io
import os
from start import *
import pytest
import unittest

from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp

    

def test_default_offline_analysis_page_1_treeview_model(qtbot):
    """ Test 1: check the default treeview after loading data from the database: 
    only experiment and sweeps must be displayed, no sweeps and no metadata label 
    Args:
        qtbot (_type_): clickbot
    """
    test_db,app = load_demo_dat_data_into_database(qtbot)
    
    # check that the selected treeview is not none
    stv = app.ui.offline.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view
    unittest.TestCase.assertIsNotNone(stv,"selected treeview should not be empty anymore")
        
    # check that the default selected treeview does only show experiment and series level data
    selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    print("got this table back")
    res = selected_treeview_table["type"].unique().tolist()
    valid_types = ["Experiment","Series"]
    
    assert res == valid_types #,"the expected types in the treeview are not correct ")
   
    # close it to run another test with the same setdb function
    test_db.database.close()


def test_sweeps_offline_analysis_page_1_treeview_model(qtbot):
    """_summary_
    Test 2: Click on the sweeps button in the ribbon bar which should add the sweeps to the treeview
    The sweep level must be part of the treeview df
    Args:
        qtbot (_type_): _description_
    """
    
    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot)


    # click the sweeps button to add the extra sweep level in the treeview 
    qtbot.mouseClick(app.ui.offline.show_sweeps_radio, Qt.LeftButton)
        
    selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    print("got this table back")
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

def test_change_series_renaming(qtbot):
    """Test: Click on the change series name button in the ribbon bar, change the series name of an IV to TEST123.
    Make sure, that the string "IV" is not present anymore in the treeview while TEST123 is present 
    """
    
    # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot)

    app.ui.offline.ap.stop_and_close_animation()

    initial_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table

    # click the button to change the series name, this should open a dialog
    qtbot.mouseClick(app.ui.offline.change_series_name, Qt.LeftButton, delay = 1)
    # wait for the opening dialog
    
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "change_series_name_dialog"), timeout = 2000)

    dialog= app.ui.offline.change_series_name_dialog

    dialog.new_name_field.setText("TEST123")
    
    qtbot.mouseClick(dialog.apply, Qt.LeftButton)
    
    updated_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
    
    # Find the corresponding rows for the old and new item names
    old_row = initial_treeview_table[initial_treeview_table["item_name"] == "Block Pulse"].index.tolist()
    new_row = updated_treeview_table[updated_treeview_table["item_name"] == "TEST123"].index.tolist()

    # Assert that the change has occurred
    assert len(old_row) > 0, "The list is empty"    # Ensure the old item was found
    assert len(new_row) > 0, "The list is empty"    # Ensure the old item was found
    assert old_row  == new_row  # Ensure the row indices are different

    test_db.database.close()


def test_load_discarded_flags_dialog(qtbot):
      # assumes that the default treeview test before worked 
    test_db,app = load_demo_dat_data_into_database(qtbot)

    app.ui.offline.ap.stop_and_close_animation()

    # click the button to change the series name, this should open a dialog
    qtbot.mouseClick(app.ui.offline.load_selected_discarded, Qt.LeftButton, delay = 1)

    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "s_d_dialog"), timeout = 2000)
    qtbot.mouseClick(app.ui.offline.s_d_dialog.apply_selection, Qt.LeftButton)

    #dialog= app.ui.offline.s_d_dialog

    #dialog.new_name_field.setText("TEST123")
    
    #dialog.close()

    

# def test meta data 
#def test sweeps AND meta data


# functions 

def set_database():
            #_summary_: Sets up the database for the testing purpose!
            
            path_db = os.getcwd() + "/Tests/"
            path_db = str(Path(path_db)) 
            return DuckDBDatabaseHandler(None,
                                        db_file_name = "test_treeview_db.db",
                                        database_path = path_db,
                                        in_memory = False)

def load_demo_dat_data_into_database(qtbot):
    
    test_db = set_database()
    app = MainWindow(testing_db = test_db)
    app.database_handler = app.local_database_handler
    app.ui.offline.offline_manager._directory_path = "./Tests/Test_Files/"
    template = Assign_Meta_Data_PopUp(app.database_handler,
                            app.ui.offline.offline_manager,
                            app.frontend_style)

    template.map_metadata_to_database()
    app.template_df = template.template_dataframe.values.tolist()
    # continue open directory writes the data from the selected directory into the database,
    # opens the wait dialog and opens the Load_Data_From_Database_Popup_Handler when the 
    # finished signal is emtitted 
    app.ui.offline.continue_open_directory(app.template_df, test = True)
    # qtbot.wait until waits until the load_data_from_database_dialog.. variable was initialized as an instance of 
    # Load_Data_From_Database_Popup_Handler
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout = 20000)
    qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    
    return test_db,app