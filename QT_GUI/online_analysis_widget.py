from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from online_analysis_designer_object import Ui_Online_Analysis
from online_analysis_manager import OnlineAnalysisManager
from treeview_manager import TreeViewManager


class Online_Analysis(QWidget, Ui_Online_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        self.online_manager = OnlineAnalysisManager()

        self.button_select_data_file.clicked.connect(self.open_single_dat_file)


    def open_single_dat_file(self):

        # open selection and retake users file selection
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        print(file_name)
        self.label_selected_directory.setText(file_name)

        # save the path in the manager class
        self.online_manager._dat_file_name = file_name

        # create treeview of this .dat file
        bundle= TreeViewManager().open_bundle_of_file(file_name)
        TreeViewManager().create_treeview_from_single_dat_file([], bundle, "", [],self.treeWidget, self.treeWidget_2,"SingleExperiment",[],0,None)

        # set the same widget in the labbook


        # print first series into a plot widget