
from PySide6.QtWidgets import *  # type: ignore

from Frontend.OfflineAnalysis.CustomWidget.select_analysis_functions_desginer import Ui_Dialog
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import AnalysisFunctionRegistration
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog

from functools import partial
import re

class Select_Analysis_Functions(QDialog, Ui_Dialog):

    def __init__(self, database_handler, series_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.selected_analysis_functions = []
        self.ADD = "+"
        self.SUB = "-"
        self.DIV = "/"
        self.MUL = "*"
        self.L_BRACK = "("
        self.R_BRACK = ")"
        self.interval_operands = [self.ADD, self.SUB, self.DIV, self.MUL, self.L_BRACK, self.R_BRACK]

        self.OPERAND = "operand"
        self.BRACKET = "bracket"
        self.FUNCTION = "function"


        self.fill_dialog(database_handler, series_name)
        self.sub_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, self.SUB))
        self.div_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, self.DIV))
        self.l_bracket_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, self.L_BRACK))
        self.r_bracket_analysis.clicked.connect(partial(self.add_text_to_analysis_syntax, self.R_BRACK))

        self.remove_last_analysis.clicked.connect(self.remove_last_analysis_function)
        
        self.add_combined.clicked.connect(self.add_text_label_to_selection)
        self.clear_all.clicked.connect(self.clear_all_fct)

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
        if self.valid_syntax_check(value) and value is not []:
            self.add_item_to_selected_grid(value)
            self.analysis_syntax.setText("")


    def valid_syntax_check(self,value):
        value = value.split()
        open_bracket = False
        close_bracket = False

        for pos in range(len(value)):
            
            # needed since act expression and the following are evaluated
            if pos < len(value)-1:
            
                if self.expression_type(value[pos]) == self.OPERAND and self.expression_type(value[pos+1])==self.OPERAND:
                    CustomErrorDialog("Syntax Error: Between two operands, there must be a function expression")
                    return False
                
                if self.expression_type(value[pos]) == self.FUNCTION and self.expression_type(value[pos+1])==self.FUNCTION:
                    CustomErrorDialog("Syntax Error: Between two functions, there must be an operator")
                    return False

            if value[pos] == self.L_BRACK:
                if not open_bracket:
                    open_bracket = True
                else:
                    CustomErrorDialog("Syntax Error: Please close the first bracket before opening a new one.")
                    return False
            
            if value[pos] == self.R_BRACK:
                if not close_bracket:
                    # check if a bracket was already opened and if yes - reset to allow new bracket expression
                    if open_bracket:
                        open_bracket = False
                    else:
                        CustomErrorDialog("Syntax Error: You have to place an opening bracket first.")
                        return False
        

        if open_bracket and not close_bracket:
            CustomErrorDialog("Syntax Error: Opening but no closing bracket detected")
            return False
        if not open_bracket and close_bracket:
            CustomErrorDialog("Syntax Error: Closing but no opening brachet detected.")
            return False
        
        return True
            
    def expression_type(self,value:str):
        """
        check the expression type
        """
        if value in [self.ADD, self.SUB, self.DIV, self.MUL]:
            return self.OPERAND
        
        if value in [self.L_BRACK, self.R_BRACK]:
            return self.BRACKET
        
        return self.FUNCTION

    def clear_all_fct(self):
        self.selected_analysis_functions = []
        self.selection_list_widget.clear()

    def add_item_to_selected_grid(self,input_string):
        self.selection_list_widget.addItem(QListWidgetItem(input_string))
        self.selected_analysis_functions.append(input_string.split())


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
        self.analysis_syntax.clear()
        self.analysis_syntax.setText(text_value)

    
    def get_selected_analysis_functions_count(self):
        cnt = 0
        for item in self.selected_analysis_functions:
            if len(item) ==1:
                cnt +=1 
            else:
                for n in item:
                    if n not in self.interval_operands:
                        cnt +=1 
        return cnt