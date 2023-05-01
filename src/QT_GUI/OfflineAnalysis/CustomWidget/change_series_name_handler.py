from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.change_series_name_designer import Ui_Dialog
from functools import partial

class ChangeSeriesName(QDialog, Ui_Dialog):

    def __init__(self,database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        1
        self.database_handler = database_handler

        self.fill_combobox()

    def fill_combobox(self):
        series_names  =self.database_handler.get_distinct_non_discarded_series_names()

        for s in series_names:
            self.series_names_combobox.addItem(s[0])

    def excecute_rename(self):

        new_name = self.new_name_field.text()
        series_name_to_change = self.series_names_combobox.currentText()

        if new_name == '':
            print("empty name found")
            return
        
        if self.permanent.isChecked():
            # @todo dz: make all renamed_series_name = series name and call the select_series_to_be_analyted function on
            # series_analysis mapping table
            q = f'update series_analysis_mapping set renamed_series_name = \'{new_name}\' where series_name = \'{series_name_to_change}\''
            self.database_handler.database.execute(q)

        else:

            print("not implemented yet")



