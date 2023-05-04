
from PySide6.QtWidgets import *  # type: ignore

from QT_GUI.OfflineAnalysis.CustomWidget.normalization_dialog import Ui_Dialog

from CustomWidget.Pandas_Table import PandasTable
from Offline_Analysis.error_dialog_class import CustomErrorDialog

from functools import partial
import re
import pandas as pd

class Normalization_Dialog(QDialog, Ui_Dialog):

    
    def __init__(self, current_tab, treeview_model,database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.current_tab = current_tab
        self.treeview_model = treeview_model
        self.database_handler = database_handler
        self.pushButton.clicked.connect(self.close)
        self.normalization_method.currentTextChanged.connect(self.prepare_data_view)
        self.normalization_method.addItems(["CSlow Auto", "CSlow Manual", "Tau"])
    
    def prepare_data_view(self):

        input = self.normalization_method.currentText()
        if input=="CSlow Auto":
            self.stackedWidget.setCurrentIndex(0)
            self.get_cslow_from_db()
            self.prepare_table_view()

        elif input=="CSlow Manual":
            self.stackedWidget.setCurrentIndex(0)
            self.get_cslow_from_db()
            self.current_tab.normalization_values["cslow"]=1
            self.prepare_table_view()
        
        elif input=="Tau":        
            self.stackedWidget.setCurrentIndex(1)

    def get_cslow_from_db(self):

        

        # get the series level and extract the identifier which is unique as experiment::series_identifier
        identifier = self.treeview_model[self.treeview_model["type"]=="Series"]["identifier"].values
        # request the cslow value for it
        df_list = []
        for i in identifier:
            s = i.split("::")
            cslow, sweep_table_name = self.database_handler.get_cslow_value_from_experiment_name_and_series_identifier(s[0],s[1])
            df_list.append([0,0,sweep_table_name,cslow])

        db_df = pd.DataFrame(df_list,columns=["offline_analysis_id", "function_id","sweep_table_name", "cslow"])        
        self.current_tab.normalization_values = db_df



    def prepare_table_view(self):
        self.model = PandasTable(self.current_tab.normalization_values)
                 
        # Creating a QTableView
        table_view = QTableView()
        table_view.setModel(self.model)
        #self.model.resize_header(table_view)

        for l in range(self.table_grid_layout.count()):
            item = self.table_grid_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.table_grid_layout.removeItem(item)
            
        self.table_grid_layout.addWidget(table_view)

    def close_dialog(self):
         self.current_tab.normalization_values =self.model._data
         self.close()

        
        
