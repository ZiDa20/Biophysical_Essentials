from PySide6.QtWidgets import * 
from QT_GUI.ConfigWidget.ui_py.ui_solutions_dialog import Ui_SolutionsDialog


class SolutionsDialog(QDialog, Ui_SolutionsDialog):

    def __init__(self, database = None,  parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database
        self.add_ions.clicked.connect(self.add_ions_to_solution)
        self.solutions_name.textChanged.connect(self.check_solutions)
        self.all_tables = self.get_current_tables_database()
        self.exec()

    def get_current_tables_database(self):
        """_summary_: This function gets all the tables in the database

        Returns:
            _type_: _description_
        """
        return self.database_handler.get_tables()["name"].tolist()

    def add_ions_to_solution(self) -> None:
        """_summary_: This function adds a new LineEdit for ions to the solution
        Dialog
        """
        row_count = self.gridLayout_3.rowCount()
        self.add_new_edit(row_count)

    def add_new_edit(self, row_count):
        """_summary_: Adds a new LineEdit to the last row

        Args:
            row_count (int): Number of rows in grid layout -> corresponding to ions
        """
        self.gridLayout_3.addWidget(QLineEdit(), row_count, 1)
        self.gridLayout_3.addWidget(QLineEdit(), row_count, 3)

    def check_solutions(self, text:str) -> None:
        """_summary_

        Args:
            text (str): Checks if solutions name is already a table in db
        """
        if text in self.all_tables:
            self.solutions_name.setStyleSheet("background-color: red;")
        else:
            self.solutions_name.setStyleSheet("background-color: green;")

    def add_solution_to_database(self):
        """_summary_: This adds a table to the database
        with the solution names and the solutions
        """
