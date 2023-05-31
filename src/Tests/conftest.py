import shutil
import pytest
import os

def pytest_sessionfinish(session, exitstatus):
    path = os.getcwd()
    file_path = os.path.join(path, "Tests", "test_db.db")
    if os.path.exists(file_path):
        os.remove(file_path)
        
