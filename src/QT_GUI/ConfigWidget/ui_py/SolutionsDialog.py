from PySide6.QtWidgets import * 
from QT_GUI.ConfigWidget.ui_py.ui_solutions_dialog import Ui_SolutionsDialog
from database.data_db import DuckDBDatabaseHandler
from StyleFrontend.frontend_style import Frontend_Style
import pandas as pd
from CustomWidget.error_dialog_class import CustomErrorDialog

class SolutionsDialog(QDialog, Ui_SolutionsDialog):
    """A dialog for adding new solutions to the database"""

    def __init__(self, database: DuckDBDatabaseHandler = None, 
                 frontend: Frontend_Style = None,  
                 parent: QDialog = None) -> None:
        """
        Initialize the dialog.

        Args:
            database: The database handler object.
            frontend: The frontend object.
            parent: The parent widget.

        Returns:
            None.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database
        self.frontend_style = frontend
        self.solution_type.addItems(["Extracellular", "Intracellular"])
        self.add_ions.clicked.connect(self.add_ions_to_solution)
        self.solutions_name.textChanged.connect(self.check_solutions)
        self.database_save.clicked.connect(self.add_solution_to_database)
        self.all_tables = self.get_current_tables_database()
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.exec_()

    def get_current_tables_database(self) -> list[str]:
        """
        Get all the tables in the database.

        Returns:
            A list of table names.
        """
        return self.database_handler.get_tables()["name"].tolist()

    def add_ions_to_solution(self) -> None:
        """
        Add a new LineEdit for ions to the solution Dialog.

        Returns:
            None.
        """
        row_count = self.gridLayout_3.rowCount()
        self.add_new_edit(row_count)

    def add_new_edit(self, row_count: int) -> None:
        """
        Add a new LineEdit to the last row.

        Args:
            row_count: The current number of rows in the grid layout.

        Returns:
            None.
        """
        self.gridLayout_3.addWidget(QLineEdit(), row_count, 1)
        self.gridLayout_3.addWidget(QLineEdit(), row_count, 3)

    def check_solutions(self, text: str) -> None:
        """
        Check if solutions name is already a table in db.

        Args:
            text: The text in the solutions name QLineEdit.

        Returns:
            None.
        """
        if text in self.all_tables:
            self.solutions_name.setStyleSheet("background-color: red;")
        else:
            self.solutions_name.setStyleSheet("background-color: green;")

    def add_solution_to_database(self) -> None:
        """
        Add a table to the database with the solution names and the solutions.

        Returns:
            None.
        """
        ions = []
        concentrations = []
        for i in range(1,self.gridLayout_3.rowCount()):
            ion = self.gridLayout_3.itemAtPosition(i, 1).widget().text()
            concentration = self.gridLayout_3.itemAtPosition(i, 3).widget().text()
            if ion and concentration:
                ions.append(ion)
                concentrations.append(concentration)
                
        if ions and concentrations:
            solutions_dataframe = pd.DataFrame({"ions": ions, "concentrations": concentrations})
            table_name = f"solution_{self.solutions_name.text()}".lower()
            solution_type = self.solution_type.currentText()
            self.database_handler.create_table_for_database(solutions_dataframe,table_name)
            self.database_handler.add_solution_table_to_mapping(table_name, solution_type)
            self.reset_form()
            
        else:
            CustomErrorDialog("Please fill in all the fields.")
            
            
    def reset_form(self):
        """
        Reset the form to its original state.

        Returns:
            None.
        """
        self.solutions_name.clear()
        self.solution_type.setCurrentIndex(0)
        for i in reversed(range(1, self.gridLayout_3.rowCount())):
            ion_edit = self.gridLayout_3.itemAtPosition(i, 1).widget()
            concentration_edit = self.gridLayout_3.itemAtPosition(i, 3).widget()
            self.gridLayout_3.removeWidget(ion_edit)
            self.gridLayout_3.removeWidget(concentration_edit)
            ion_edit.deleteLater()
            concentration_edit.deleteLater()
        self.gridLayout_3.addWidget(QLineEdit(), 1, 1)
        self.gridLayout_3.addWidget(QLineEdit(), 1, 3)
        self.all_tables = self.get_current_tables_database()
            
        