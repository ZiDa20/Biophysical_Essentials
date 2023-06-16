from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.change_series_name_designer import Ui_Dialog
from functools import partial

class ChangeSeriesName(QDialog, Ui_Dialog):

    def __init__(self,database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.series_names= [i[0] for i in self.database_handler.get_distinct_non_discarded_series_names()]
        completer = QCompleter(self.series_names)
        self.new_name_field.setCompleter(completer)
        self.fill_combobox()

    def fill_combobox(self) -> None:
        """This fills the combobox with the series that 
        are found in the current analysis
        """
        self.series_names_combobox.clear()
        self.series_names_combobox.addItems(self.series_names)
        
    def excecute_rename(self) -> None:
        """This function is called when the user clicks on the rename button
        and thereby the renaming of a specific series is executed but only
        temporary for this analysis
        """
        new_name = self.new_name_field.text()
        series_name_to_change = self.series_names_combobox.currentText()
        if new_name == '':
            print("empty name found")
            return

        # @todo dz: make all renamed_series_name = series name and call the select_series_to_be_analyted function on
        # series_analysis mapping table
        q = f'update series_analysis_mapping set renamed_series_name = \'{new_name}\' where series_name = \'{series_name_to_change}\' and analysis_id = {self.database_handler.analysis_id}'
        self.database_handler.database.execute(q)
            


