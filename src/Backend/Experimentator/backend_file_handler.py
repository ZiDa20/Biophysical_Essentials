import picologging
from typing import Optional
from PySide6.QtWidgets import QFileDialog # type: ignore


class ExperimentatorFileHandler:
    def __init__(self, line_edit, file_type: str):
        self.logger = picologging.getLogger(__name__)
        self.handler = ExperimentatorFileHandler
        self.file_type = file_type
        self.line_edit = line_edit
        self.file_name_setter()
     
    def file_name_setter(self) -> None:
        """set the pgf file that is used for the patchmaster"""
        self.logger.info("Setted Fily Type")
        self.meta_open_directory()
     
    def meta_open_directory(self) -> str:
        '''opens a filedialog where a user can select a desired directory. Once the directory has been choosen,
        it's data will be loaded immediately into the databse'''
        dir_path = QFileDialog.getOpenFileName()
        dir_path = str(dir_path[0]).replace("/","\\")
        if self.check_file_path_validity(dir_path):
            self.line_edit.setText(dir_path)
            self.logger.info("File path is valid")
        else:
            self.logger.error("File path is not valid")
            self.line_edit.setText("File path is not valid")
    
    def check_file_path_validity(self, dir_path: str) -> None:
        """check if the file path is valid,
        this should also check if the file type is correct"""
        if dir_path.endswith(self.file_type):
            self.logger.info("File path is valid")
            return True
        else:
            self.logger.info("File path is not valid")
            return False
            