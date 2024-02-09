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
import time

def clean_leftover_db():
     test_dir = os.path.join(os.getcwd(),"Tests")
     for filename in os.listdir(test_dir):
        if filename.endswith(".db") or filename.endswith(".wal"):
            filepath = os.path.join(test_dir, filename)
            try:
                os.remove(filepath)
                print(f"Deleted: {filepath}")
            except Exception as e:
                print(f"Error deleting {filepath}: {e}")


@pytest.mark.order(1)
@pytest.mark.serial
def test_clean():
     clean_leftover_db()


#### i have no clue why and i am happy for feedbacl: the first test with the db interaction is always failing  #####
#### thats why i have this always true test in here #####
@pytest.mark.order(2)
@pytest.mark.serial
def test_true(qtbot):
    test_db = set_database()  
    app = MainWindow(testing_db = test_db)
    app.database_handler = app.local_database_handler
    app.ui.offline.offline_manager._directory_path = "./Tests/Test_Files/"
    template = Assign_Meta_Data_PopUp(test_db,
                            app.ui.offline.offline_manager,
                            app.frontend_style)

    template.map_metadata_to_database()
    app.template_df = template.template_dataframe.values.tolist()
    # continue open directory writes the data from the selected directory into the database,
    # opens the wait dialog and opens the Load_Data_From_Database_Popup_Handler when the 
    # finished signal is emtitted 
    app.ui.offline.continue_open_directory(app.template_df, test = True)
    # qtbot.wait until waits until the load_data_from.. variable was initialized as an instance of 
    # Load_Data_From_Database_Popup_Handler
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout = 20000)


    #qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    tables = test_db.database.execute("SHOW TABLES").fetchdf()
    a = tables.shape[0]

    assert True
    test_db.database.close()

@pytest.mark.order(3)
@pytest.mark.serial
def test_long_computation(qtbot):

    test_db = set_database()  
    app = MainWindow(testing_db = test_db)
    app.database_handler = app.local_database_handler
    app.ui.offline.offline_manager._directory_path = "./Tests/Test_Files/"
    template = Assign_Meta_Data_PopUp(test_db,
                            app.ui.offline.offline_manager,
                            app.frontend_style)

    template.map_metadata_to_database()
    app.template_df = template.template_dataframe.values.tolist()
    # continue open directory writes the data from the selected directory into the database,
    # opens the wait dialog and opens the Load_Data_From_Database_Popup_Handler when the 
    # finished signal is emtitted 
    app.ui.offline.continue_open_directory(app.template_df, test = True)
    # qtbot.wait until waits until the load_data_from.. variable was initialized as an instance of 
    # Load_Data_From_Database_Popup_Handler
    qtbot.waitUntil(lambda: hasattr(app.ui.offline, "load_data_from_database_dialog"), timeout = 20000)


    #qtbot.mouseClick(app.ui.offline.load_data_from_database_dialog.load_data, Qt.LeftButton)
    tables = test_db.database.execute("SHOW TABLES").fetchdf()


    a = tables.shape[0]

    assert a == 65, f"Expected 65 rows, but found {a} rows."
    
    test_db.database.close()

    # Watch for the app.worker.finished signal, then start the worker.



def set_database():
        """_summary_: Sets up the database for the testing purpose!
        """
        path_db = os.getcwd() + "/Tests/"
        path_db = str(Path(path_db)) 
        return DuckDBDatabaseHandler(None,
                                    db_file_name = "test_db_new.db",
                                    database_path = path_db,
                                    in_memory = False)