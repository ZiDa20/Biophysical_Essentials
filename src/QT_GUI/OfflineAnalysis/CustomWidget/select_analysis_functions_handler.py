
from PySide6.QtWidgets import *  # type: ignore

from QT_GUI.OfflineAnalysis.CustomWidget.select_analysis_functions_desginer import Ui_Dialog
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import AnalysisFunctionRegistration

from functools import partial

class Select_Analysis_Functions(QDialog, Ui_Dialog):

    def __init__(self, database_handler, series_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.fill_dialog(database_handler, series_name)
        self.sub_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, " - "))
        self.div_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, " / "))
        self.l_bracket_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, " ( "))
        self.r_bracket_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, " ) "))

        self.remove_last_analysis.clicked.connect(self.remove_last_analysis_function)
        
        self.add_combined.clicked.connect(self.add_text_label_to_selection)
        self.clear_all.clicked.connect(self.selection_list_widget.clear)

    def fill_dialog(self,database_handler, series_name):

        
        # 2) get recording mode of the specific series
        recording_mode = database_handler.get_recording_mode_from_analysis_series_table(series_name)

        # 3) request recording mode specific analysis functions
        analysis_function_names = AnalysisFunctionRegistration.get_elements(recording_mode)

        # 4) create dialog checkboxes
        checkbox_list = []
        for f in analysis_function_names:
                c1 = QPushButton(f)
                c1.clicked.connect(partial(self.add_item_to_selected_grid,f))
                c2 = QPushButton(f)
                self.single_interval_grid.addWidget(c1,analysis_function_names.index(f), 0)
                self.verticalLayout.addWidget(c2)
                c2.clicked.connect(partial(self.add_text_to_analysis_syntax,f))

    def add_text_label_to_selection(self):
        value = self.analysis_syntax.text()
        self.add_item_to_selected_grid(value)
        self.analysis_syntax.setText("")

    def add_item_to_selected_grid(self,input_string):
        self.selection_list_widget.addItem(QListWidgetItem(input_string))
    
    def add_text_to_analysis_syntax(self,input_string):
        value = self.analysis_syntax.text()

        value = value + "  " + input_string
        self.analysis_syntax.setText(value)
    
    def remove_last_analysis_function(self):

        value = self.analysis_syntax.text().split(" ")
        value = value[:-1]
        text_value = ""
        for i in value:
            text_value = text_value + " " + i

        self.analysis_syntax.setText(text_value)

        """
            c = QCheckBox()
            checkbox_list.append(c)
            l = QLabel(f)
            dialog_grid.addWidget(c, analysis_function_names.index(f), 0)
            dialog_grid.addWidget(l, analysis_function_names.index(f), 1)

            # 5) add button to the dialog, since it's in the dialog only the button can be of local type
            confirm_selection_button = QPushButton("Confirm Selected Analysis Functions", dialog)
            confirm_selection_button.clicked.connect(
                partial(self.update_selected_analysis_function_table, checkbox_list, analysis_function_names, dialog))

            # 6) Add button widget to correct grid position, finally execute the dialog
            dialog_grid.addWidget(confirm_selection_button, len(analysis_function_names), 0 , 1 , 2)

            dialog.setWindowTitle("Available Analysis Functions for Series " + series_name)
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

        """