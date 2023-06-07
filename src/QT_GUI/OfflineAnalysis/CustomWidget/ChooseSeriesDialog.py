from PySide6.QtWidgets import *  # type: ignore
from functools import partial


class SeriesDialog(QDialog):
    
    def __init__(self,database_handler, frontend_style, series_combo, parent=None) -> None:
        super().__init__(parent)
        self.database_handler = database_handler
        self.frontend_style = frontend_style
        self.series_combo = series_combo
        self.final_series = []
        self.setup_ui()
        
        
    def setup_ui(self):
            """
            Opens a popup and displays available series to be analyzed in the selected experiments
            :param series_names_string_list: list comes as list of tuples
            :return:
            """
            series_names_string_list = self.select_series_to_be_analized()
            self.dialog_grid = QGridLayout(self)
            # series_names_string_list = ["Block Pulse", "IV"]
            self.checkbox_list = []
            self.name_list = []
            for s in series_names_string_list:
                c = QCheckBox()
                self.checkbox_list.append(c)
                c.setText(s[0])
                self.dialog_grid.addWidget(c, series_names_string_list.index(s) + 2, 0)
                self.name_list.append(s[0])

            self.confirm_series = QPushButton("Compare Series", self)
            self.quit = QPushButton("Cancel", self)
            
            self.dialog_grid.addWidget(self.confirm_series, len(self.name_list) + 2, 0)
            self.dialog_grid.addWidget(self.quit,len(self.name_list) + 2, 1)
            self.confirm_series.clicked.connect(self.compare_series_clicked)
            self.quit.clicked.connect(self.close)
            self.setWindowTitle("Available Series To Be Analyzed")
            self.frontend_style.set_pop_up_dialog_style_sheet(self)
            self.exec()
            
    def select_series_to_be_analized(self):
        """
        executed after all experiment files have been loaded
        :return:
        """
        return self.database_handler.get_distinct_non_discarded_series_names()

    def compare_series_clicked(self):
        """Handler for a click on the button confirm_series_selection in a pop up window"""

        self.series_to_analyze = self.get_selected_checkboxes()
        self.series_combo.addItems(self.series_to_analyze)
        self.final_series.extend(self.series_to_analyze)
        self.close()
        
    def get_selected_checkboxes(self):
        """From two lists of checkboxes and labels one list of checked labels (string) will be returned"""
        return [self.name_list[self.checkbox_list.index(c)] for c in self.checkbox_list if c.isChecked()]