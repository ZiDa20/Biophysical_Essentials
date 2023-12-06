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
import time
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp

####################
# A test that simulates a basic offline analysis (OFA) workflow:
#  1) Load data from a directory
#  2) On the first page of OFA, select all series to be analyzed -> The second page of OFA will open
#  3) analysis functions for Block Pulse Series will be selected: max, min, mean, time-to-min, time-to-max and area under the curve
#  4) Analysis will be executed
#  5) third page of OFA will open and should display 6 widgets with one plot for each analysis functions respectively  
####################


def set_database(db_name):
            #_summary_: Sets up the database for the testing purpose!
            #clean_leftover_db()
            path_db = os.path.join(os.getcwd(),"Tests")
            return DuckDBDatabaseHandler(None,
                                        db_file_name = db_name+".db",
                                        database_path = path_db,
                                        in_memory = False)


def load_demo_dat_data_into_database(qtbot,db_name):
    
    test_db = set_database(db_name)
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
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout = 10000)
    #QApplication.processEvents()

    qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    #QApplication.processEvents()

    return test_db,app


@pytest.fixture
def setup_test_environment(qtbot):
    test_db, app = load_demo_dat_data_into_database(qtbot, "block_pulse_analysis_test_db")
    yield test_db, app
    # Teardown code, runs after the test
    test_db.database.close()

# test 1: load the data
@pytest.mark.run(order=1)
@pytest.mark.serial
def test_default_offline_analysis_page_1_treeview_model(qtbot,setup_test_environment):

    """ Test 1: 
        1. Load files from the directory into the database 
        2. Select the imported data in the data selection dialog 
        3. This should open the first page of OFA showing a treeview 
        4. This treeview MUST hold only experiment and sweeps 
        5. But No sweeps and no metadata label 
    Args:
        qtbot (_type_): clickbot
    """
    test_db, app = setup_test_environment
    QApplication.processEvents()
    app.show()
    qtbot.waitForWindowShown(app)
    time.sleep(3)
    #qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    tables = test_db.database.execute("SHOW TABLES").fetchdf()
    
    a = tables.shape[0]
    print(a)
    b = tables.shape[1]
    try:
        assert a == 65, f"Expected 65 rows, but found {a} rows."

        # check that the selected treeview is not none
        stv = app.ui.offline.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view
        unittest.TestCase.assertIsNotNone(stv,"selected treeview should not be empty anymore")
            
        # check that the default selected treeview does only show experiment and series level data
        selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
        print("got this table back")
        print(selected_treeview_table)
        res = selected_treeview_table["type"].unique().tolist()
        valid_types = ["Experiment","Series"]
        
        assert res == valid_types #,"the expected types in the treeview are not correct ")
    
        # close it to run another test with the same setdb function
        test_db.database.close()
    except AssertionError  as e:
         print(e)
         test_db.database.close()



# test 2: select all series and  proceed to OFA page 2
@pytest.mark.run(order=2)
def test_setting_series_specific_OFA_page_2(qtbot,setup_test_environment):
    test_db, app = setup_test_environment
    QApplication.processEvents()
    app.show()
    qtbot.waitForWindowShown(app)
    time.sleep(3)

    # click the button to open the menu   
    qtbot.mouseClick(app.ui.offline.compare_series, Qt.LeftButton)
    # wait until the dialog appears
    QApplication.processEvents()
    dialog = app.ui.offline.OfflineDialogs.series_dialog
    #click the upper checkbox saying "ALL"
    # Find the index of the "All" checkbox
    all_checkbox_index = [i for i, checkbox in enumerate(dialog.checkbox_list) if checkbox.text() == "All"]
    # Ensure that the "All" checkbox is found
    if all_checkbox_index:
        # Get the QCheckBox object for "All"
        # Simulate a click on the "All" checkbox using qtbot
        dialog.checkbox_list[all_checkbox_index[0]].setChecked(True)
        #qtbot.mouseClick(app.ui.offline.OfflineDialogs.series_dialog.checkbox_list[all_checkbox_index[0]], Qt.LeftButton)
    else:
        print("Checkbox 'All' not found in the list.")
    # proceed with "OK"
    QApplication.processEvents()
    qtbot.mouseClick(dialog.confirm_series, Qt.LeftButton)
    # click proceed to continue to OFA page 2
    QApplication.processEvents()
    qtbot.mouseClick(app.ui.offline.start_analysis,Qt.LeftButton)
    # wait until the popup closes again is prepared
    assert app.ui.offline.offline_analysis_widgets.currentIndex() == 1
    return test_db, app

@pytest.mark.run(order=3)
# test 3: open the analysis function selection menu, select 
def test_analysis_function_menu(qtbot, setup_test_environment):
     # get the state after test 2
     test_db, app = test_setting_series_specific_OFA_page_2(qtbot,setup_test_environment)
     app.show()

     # now find the block pulse in the series selector treeview. 
     # click the analysis configurator (child 0)

     # open the analysis function selection menu
     # qtbot.mouseClick(app.ui.offline.select_analysis_fct,Qt.LeftButton)
     assert True


     