from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, 
    QHeaderView, QCheckBox, QPushButton, QHBoxLayout, QWidget, QLineEdit
)
from PySide6.QtCore import Qt

class FileSelectionPopup(QDialog):
    def __init__(self, data_list,frontend):
        super().__init__()
        self.setWindowTitle("File Selection")
        self.setMinimumSize(600, 400)
        self.frontend_style = frontend
        self.frontend_style.set_pop_up_dialog_style_sheet(self)

        self.data_list = data_list
        self.selection_results = []

        # Layouts
        layout = QVBoxLayout(self)

        # Table Widget
        self.table = QTableWidget(len(data_list), 4, self)
        self.table.setHorizontalHeaderLabels(["Select", "Path", "Filename", "Specific Name"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row, (path, filename) in enumerate(data_list):
            # Column 1: Checkbox
            checkbox = QCheckBox(self)
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row, 0, checkbox_widget)

            # Column 2: Path
            self.table.setItem(row, 1, QTableWidgetItem(path))
            
            # Column 3: Filename
            self.table.setItem(row, 2, QTableWidgetItem(filename))
            
            # Column 4: User Input
            specific_name_input = QLineEdit(self)
            self.table.setCellWidget(row, 3, specific_name_input)

        # Add the table to the layout
        layout.addWidget(self.table)

        # Select All / Unselect All Buttons
        button_layout = QHBoxLayout()
        self.select_all_button = QPushButton("Select All", self)
        self.select_all_button.clicked.connect(self.select_all)
        self.unselect_all_button = QPushButton("Unselect All", self)
        self.unselect_all_button.clicked.connect(self.unselect_all)
        button_layout.addWidget(self.select_all_button)
        button_layout.addWidget(self.unselect_all_button)
        layout.addLayout(button_layout)

        # Button to confirm selection
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.collect_user_selection)
        layout.addWidget(self.submit_button)

    def select_all(self):
        for row in range(self.table.rowCount()):
            checkbox_widget = self.table.cellWidget(row, 0)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            checkbox.setChecked(True)

    def unselect_all(self):
        for row in range(self.table.rowCount()):
            checkbox_widget = self.table.cellWidget(row, 0)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            checkbox.setChecked(False)

    def collect_user_selection(self):
        """
        Collects the user selections from the table.
        """

        self.selection_results = []
        for row in range(self.table.rowCount()):
            checkbox_widget = self.table.cellWidget(row, 0)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            is_selected = checkbox.isChecked()

            path = self.table.item(row, 1).text()
            filename = self.table.item(row, 2).text()
            specific_name_input = self.table.cellWidget(row, 3)
            specific_name = specific_name_input.text()

            self.selection_results.append({
                "selected": is_selected,
                "path": path,
                "filename": filename,
                "specific_name": specific_name
            })

        # Close the popup and print results (optional)
        print(self.selection_results)  # You can process the results here
        self.accept()