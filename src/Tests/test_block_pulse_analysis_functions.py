import sys
import os
import io
import time
import unittest
import pytest
from pathlib import Path
import uuid

sys.path.append(os.getcwd())

from start import *
from matplotlib.figure import Figure
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *   # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtTest import QTest

import duckdb
from pytestqt import qtbot

from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from Backend.tokenmanager import InputDataTypes

####################
# A test that simulates a basic offline analysis (OFA) workflow:
#  1) Load data from a directory
#  2) On the first page of OFA, select all series to be analyzed -> The second page of OFA will open
#  3) analysis functions for Block Pulse Series will be selected: max, min, mean, time-to-min, time-to-max and area under the curve
#  4) Analysis will be executed
#  5) third page of OFA will open and should display 6 widgets with one plot for each analysis functions respectively  
####################

def set_database(db_path):
    """Sets up the database for the testing purpose."""
    return DuckDBDatabaseHandler(
        None,
        db_file_name=str(db_path.name),
        database_path=str(db_path.parent),
        in_memory=False
    )

def load_demo_dat_data_into_database(qtbot, tmp_path):
    """Load demo data into a temporary database."""
    # each test gets a unique DB file
    db_file = tmp_path / f"block_pulse_analysis_test_{uuid.uuid4().hex}.db"
    test_db = set_database(db_file)

    app = MainWindow(testing_db=test_db)
    app.database_handler = app.local_database_handler
    app.ui.offline.offline_manager._directory_path = "./Tests/Test_Files/"

    template = Assign_Meta_Data_PopUp(
        app.database_handler,
        app.ui.offline.offline_manager,
        app.frontend_style
    )
    template.map_metadata_to_database(InputDataTypes.BUNDLED_HEKA_DATA)
    app.template_df = template.template_dataframe.values.tolist()

    app.ui.offline.continue_open_directory(app.template_df, test=True)
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout=10000)
    qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)

    return test_db, app

@pytest.fixture
def setup_test_environment(qtbot, tmp_path):
    test_db, app = load_demo_dat_data_into_database(qtbot, tmp_path)
    yield test_db, app
    # Teardown code, runs after the test
    test_db.database.close()

# Test 1: load the data
def test_default_offline_analysis_page_1_treeview_model(qtbot, setup_test_environment):
    """ Test 1: 
        1. Load files from the directory into the database 
        2. Select the imported data in the data selection dialog 
        3. This should open the first page of OFA showing a treeview 
        4. This treeview MUST hold only experiment and series 
        5. But no sweeps and no metadata label
    """
    print("running test_default_offline_analysis_page_1_treeview_model")
    test_db, app = setup_test_environment

    tables = test_db.database.execute("SHOW TABLES").fetchdf()
    a = tables.shape[0]
    print(a)

    try:
        assert a == 65, f"Expected 65 rows, but found {a} rows."

        stv = app.ui.offline.blank_analysis_tree_view_manager.tree_build_widget.selected_tree_view
        unittest.TestCase.assertIsNotNone(stv, "selected treeview should not be empty anymore")

        selected_treeview_table = app.ui.offline.blank_analysis_tree_view_manager.selected_tree_view_data_table
        res = selected_treeview_table["type"].unique().tolist()
        valid_types = ["Experiment", "Series"]

        assert res == valid_types

    finally:
        test_db.database.close()
        # wait to allow any open popups to finish
        print("waiting 9s to allow gui events, signals, timers and threads to keep executing until finished")
        qtbot.wait(9000)