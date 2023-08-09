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
    def __init__(self,database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.selected_id = None

        self.update_combobox()

    def update_combobox(self):
        """_summary_: fill the combo box with available analysis id items
        """
        # get all unique id's 
        unique_ids = self.database_handler.database.execute('select distinct analysis_id from experiment_analysis_mapping').fetchdf()
        analysis_id_list = unique_ids["analysis_id"].values.tolist()
        #self.comboBox.setMaximumHeight(200)
        view = self.comboBox.view()
        #view.setMinimumHeight(200)
        #view.setMaximumHeight(200)
       
        for i in range(len(analysis_id_list)):
            analysis_id_list[i] = str(analysis_id_list[i])
        self.comboBox.addItems(analysis_id_list) #unique_ids["analysis_id"].values
        
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        


    def combobox_changed(self):
        """_summary_: update the data preview according the selected analysis id 
        """
        current_text = self.comboBox.currentText()
        if current_text == "Default":
            print("nothing to do here")
        else:
            self.selected_id = current_text
            print("preparing id", self.selected_id)
            self.database_handler.update_discarded_selected_series(self.selected_id, self.database_handler.analysis_id)
            # (self.database_handler, self.treebuild, self.show_sweeps_radio, frontend = self.frontend_style)
            tvm = TreeViewManager(self.database_handler,None, False, None)
            tvm.show_discarded_flag_dialog_trees(self.selected_data_treeview, self.discarded_data_treeview)
            self.selected_data_treeview.setStyleSheet("QTreeView { color: black; }")
            print("have to prepare the treeviews")

            