
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
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from pathlib import Path
import pytest

