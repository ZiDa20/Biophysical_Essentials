from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtCore import *
from functools import partial

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from QT_GUI.OfflineAnalysis.CustomWidget.load_previous_discarded_flags_designer import Ui_Dialog
from Backend.treeview_manager import TreeViewManager

from Offline_Analysis.error_dialog_class import CustomErrorDialog

from CustomWidget.Pandas_Table import PandasTable
import copy

class LoadPreviousDiscardedFlagsHandler(QDialog, Ui_Dialog):
    """_summary_: Handler for the dialog to load previously performed flagging of discarded series and experiments
    Args:
        QDialog (_type_): _description_
        Ui_Dialog (_type_): _description_
    """
    def __init__(self,database_handler, frontend_style, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.frontend_style = frontend_style
        self.selected_id = None
        self.update_was_executed = None
        self.id_to_show.setText(str(self.database_handler.analysis_id))
        self.cancel_button.clicked.connect(self.cancel)
        
        self.comboBox.setStyleSheet("QComboBox QAbstractItemView { color: black; }")

        self.update_combobox()

    def update_combobox(self):
        """_summary_: fill the combo box with available analysis id items
        """
        # get all unique id's 
        unique_ids = self.database_handler.database.execute('select distinct analysis_id from experiment_analysis_mapping').fetchdf()
        analysis_id_list = unique_ids["analysis_id"].values.tolist()
       
        for i in range(len(analysis_id_list)):
            analysis_id_list[i] = str(analysis_id_list[i])

      
        sorted_ids = sorted(analysis_id_list, key=int,reverse=True)
        self.comboBox.addItems(sorted_ids) #unique_ids["analysis_id"].values
        # Set the font color to black
        

        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        self.combobox_changed()
        
        


    def combobox_changed(self):
        """_summary_: update the data preview according the selected analysis id 
        """
        current_text = self.comboBox.currentText()

        if current_text == "Default":
            self.selected_id = self.database_handler.analysis_id
        else:
            self.selected_id = current_text
        
        print("preparing id", self.selected_id)

        # backup the initial selection as it was before the dialog was opened 
        if not self.update_was_executed:
            self.original_df = self.database_handler.get_analysis_mapping_for_id(self.database_handler.analysis_id)

        # reset to the initial selection
        if self.update_was_executed:
            self.database_handler.overwrite_analysis_mapping(self.original_df,self.database_handler.analysis_id,reset=True) 
        
        # get the flags from a previous analysis via the previous selected analyis id
        previous_df = self.database_handler.get_analysis_mapping_for_id(self.selected_id)
        
        # update the initial selection
        self.database_handler.overwrite_analysis_mapping(previous_df,self.database_handler.analysis_id, reset = False)
        
        # rise the update flag
        self.update_was_executed = 1
        
        # (self.database_handler, self.treebuild, self.show_sweeps_radio, frontend = self.frontend_style)
        tvm = TreeViewManager(self.database_handler,None, QRadioButton(), frontend=self.frontend_style)
        tvm.show_discarded_flag_dialog_trees(self.selected_data_treeview, self.discarded_data_treeview)
        
        self.selected_data_treeview.setStyleSheet("QTreeView::item { color: black; }")
        self.discarded_data_treeview.setStyleSheet("QTreeView::item { color: black; }")
            
    def cancel(self):
        # reset to the initial selection
        if self.update_was_executed:
            self.database_handler.overwrite_analysis_mapping(self.original_df,self.database_handler.analysis_id,reset=True) 
        self.close()