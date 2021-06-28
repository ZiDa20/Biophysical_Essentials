# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_main_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from offline_analysis_manager import OfflineManager



class Ui_Offline_Analysis(object):

    def __init__(self):

        # init managers
        self.offline_manager = None

    @Slot()
    def open_directory(self):
        '''opens a filedialog where a user can select a desired directory. Once the directory has been choosen,
        it's data will be loaded immediately into the databse'''
        # open the directory
        dir_path =QFileDialog.getExistingDirectory()
        self.selected_directory.setText(dir_path)

        # save the path in the manager class
        self.offline_manager._directory_path = dir_path

        # read all the data in the specified directory
        # -> read directory data into database
        # @todo: display a reading animation
        self.offline_manager.read_data_from_experiemnt_directory()

        # create treeview
        # filter options need to be selected
        # plot the first data available


    @Slot()
    def start_offline_analysis(self, notebook):
        #self.ui.notebook.setCurrentIndex(2)
        print("cool")

    @Slot()
    def start_another_function(self):
        print("noch cooler")
        self.offline_analysis_widgets.setCurrentIndex(1)


    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(1792, 1008)
        self.Offline_Analysis_Notebook = QTabWidget(Offline_Analysis)
        self.Offline_Analysis_Notebook.setObjectName(u"Offline_Analysis_Notebook")
        self.Offline_Analysis_Notebook.setGeometry(QRect(0, 0, 931, 621))
        self.Offline_Analysis_Notebook.setTabShape(QTabWidget.Rounded)
        self.Start_Analysis = QWidget()
        self.Start_Analysis.setObjectName(u"Start_Analysis")
        self.offline_analysis_widgets = QStackedWidget(self.Start_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setGeometry(QRect(0, 0, 931, 590))
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.new_analysis_with_template = QPushButton(self.start_page)
        self.new_analysis_with_template.setObjectName(u"new_analysis_with_template")
        self.new_analysis_with_template.setGeometry(QRect(180, 260, 181, 61))
        self.view_analysis_from_db = QPushButton(self.start_page)
        self.view_analysis_from_db.setObjectName(u"view_analysis_from_db")
        self.view_analysis_from_db.setGeometry(QRect(180, 330, 181, 61))
        self.start_label = QLabel(self.start_page)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setGeometry(QRect(320, 100, 251, 41))
        font = QFont()
        font.setPointSize(20)
        self.start_label.setFont(font)
        self.blank_analysis_button = QPushButton(self.start_page)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setGeometry(QRect(180, 190, 181, 61))

        self.blank_analysis_button.clicked.connect(self.start_another_function)

        self.user_feedback_label = QLabel(self.start_page)
        self.user_feedback_label.setObjectName(u"user_feedback_label")
        self.user_feedback_label.setGeometry(QRect(440, 190, 321, 201))
        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.experiments_tree_view = QTreeView(self.blank_analysis)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")
        self.experiments_tree_view.setGeometry(QRect(70, 150, 241, 161))
        self.compare_series = QPushButton(self.blank_analysis)
        self.compare_series.setObjectName(u"compare_series")
        self.compare_series.setGeometry(QRect(70, 530, 811, 41))
        self.series_plot_frame = QFrame(self.blank_analysis)
        self.series_plot_frame.setObjectName(u"series_plot_frame")
        self.series_plot_frame.setGeometry(QRect(350, 150, 531, 341))
        self.series_plot_frame.setFrameShape(QFrame.StyledPanel)
        self.series_plot_frame.setFrameShadow(QFrame.Raised)
        self.widget_sepcific_label = QLabel(self.blank_analysis)
        self.widget_sepcific_label.setObjectName(u"widget_sepcific_label")
        self.widget_sepcific_label.setGeometry(QRect(310, 40, 281, 41))
        self.widget_sepcific_label.setFont(font)
        self.select_directory_button = QPushButton(self.blank_analysis)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setGeometry(QRect(70, 100, 93, 28))
        self.select_directory_button.clicked.connect(self.open_directory)
        self.selected_directory = QLabel(self.blank_analysis)
        self.selected_directory.setObjectName(u"selected_directory")
        self.selected_directory.setGeometry(QRect(180, 100, 131, 21))
        self.outfiltered_tree_view = QTreeView(self.blank_analysis)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")
        self.outfiltered_tree_view.setGeometry(QRect(70, 330, 241, 161))
        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.Offline_Analysis_Notebook.addTab(self.Start_Analysis, "")
        self.visualization = QWidget()
        self.visualization.setObjectName(u"visualization")
        self.Offline_Analysis_Notebook.addTab(self.visualization, "")

        self.retranslateUi(Offline_Analysis)

        self.Offline_Analysis_Notebook.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.new_analysis_with_template.setText(QCoreApplication.translate("Offline_Analysis", u"New Analysis using \n"
" previous analysis as template", None))
        self.view_analysis_from_db.setText(QCoreApplication.translate("Offline_Analysis", u"View Analysis From Database", None))
        self.start_label.setText(QCoreApplication.translate("Offline_Analysis", u"Select your Analysis", None))
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"New Blank Analysis", None))
        self.user_feedback_label.setText(QCoreApplication.translate("Offline_Analysis", u"Further Information about your selected analysis", None))
        self.compare_series.setText(QCoreApplication.translate("Offline_Analysis", u"Select Series To Be Analyzed", None))
        self.widget_sepcific_label.setText(QCoreApplication.translate("Offline_Analysis", u"Configure your Analysis", None))
        self.select_directory_button.setText(QCoreApplication.translate("Offline_Analysis", u"Select Directory", None))
        self.selected_directory.setText(QCoreApplication.translate("Offline_Analysis", u"TextLabel", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.Start_Analysis), QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.visualization), QCoreApplication.translate("Offline_Analysis", u"Visualization", None))
    # retranslateUi


class Offline_Analysis(QWidget,Ui_Offline_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.offline_manager = OfflineManager()