# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'online_analysis_notebook.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Online_Analysis(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(974, 679)
        self.online_analysis = QTabWidget(Form)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis.setGeometry(QRect(20, 20, 931, 621))
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        self.select_dat = QPushButton(self.online_analysis_window)
        self.select_dat.setObjectName(u"select_dat")
        self.select_dat.setGeometry(QRect(10, 10, 141, 31))
        self.labbook_button = QPushButton(self.online_analysis_window)
        self.labbook_button.setObjectName(u"labbook_button")
        self.labbook_button.setGeometry(QRect(160, 10, 141, 31))
        self.line = QFrame(self.online_analysis_window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 921, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.online_analysis_window)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 520, 921, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.treeview_widget = QWidget(self.online_analysis_window)
        self.treeview_widget.setObjectName(u"treeview_widget")
        self.treeview_widget.setGeometry(QRect(0, 60, 241, 461))
        self.mpl_canvas = QWidget(self.online_analysis_window)
        self.mpl_canvas.setObjectName(u"mpl_canvas")
        self.mpl_canvas.setGeometry(QRect(250, 60, 421, 461))
        self.button_toolbar_online = QWidget(self.online_analysis_window)
        self.button_toolbar_online.setObjectName(u"button_toolbar_online")
        self.button_toolbar_online.setGeometry(QRect(680, 60, 241, 461))
        self.transfer_bar_online = QWidget(self.online_analysis_window)
        self.transfer_bar_online.setObjectName(u"transfer_bar_online")
        self.transfer_bar_online.setGeometry(QRect(10, 540, 371, 51))
        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.image_experiment = QGraphicsView(self.labbook_window)
        self.image_experiment.setObjectName(u"image_experiment")
        self.image_experiment.setGeometry(QRect(680, 30, 241, 192))
        self.labbook_experiment = QTableView(self.labbook_window)
        self.labbook_experiment.setObjectName(u"labbook_experiment")
        self.labbook_experiment.setGeometry(QRect(260, 30, 411, 451))
        self.treeview_experiment = QTreeView(self.labbook_window)
        self.treeview_experiment.setObjectName(u"treeview_experiment")
        self.treeview_experiment.setGeometry(QRect(10, 30, 241, 181))
        self.treeview_experiment_discarded = QTreeView(self.labbook_window)
        self.treeview_experiment_discarded.setObjectName(u"treeview_experiment_discarded")
        self.treeview_experiment_discarded.setGeometry(QRect(10, 300, 241, 181))
        self.discard_button = QPushButton(self.labbook_window)
        self.discard_button.setObjectName(u"discard_button")
        self.discard_button.setGeometry(QRect(70, 220, 121, 31))
        self.retrieve_button = QPushButton(self.labbook_window)
        self.retrieve_button.setObjectName(u"retrieve_button")
        self.retrieve_button.setGeometry(QRect(70, 260, 121, 31))
        self.label = QLabel(self.labbook_window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 16))
        self.label_2 = QLabel(self.labbook_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 10, 121, 16))
        self.label_3 = QLabel(self.labbook_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(680, 10, 121, 16))
        self.add_metadata_button = QPushButton(self.labbook_window)
        self.add_metadata_button.setObjectName(u"add_metadata_button")
        self.add_metadata_button.setGeometry(QRect(680, 240, 241, 31))
        self.save_labbook_button = QPushButton(self.labbook_window)
        self.save_labbook_button.setObjectName(u"save_labbook_button")
        self.save_labbook_button.setGeometry(QRect(680, 280, 241, 31))
        self.online_analysis.addTab(self.labbook_window, "")

        self.retranslateUi(Form)

        self.online_analysis.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.select_dat.setText(QCoreApplication.translate("Form", u"Select a .Dat File:", None))
        self.labbook_button.setText(QCoreApplication.translate("Form", u"Switch to Labbook", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Form", u"Online Analysis", None))
        self.discard_button.setText(QCoreApplication.translate("Form", u"Discard", None))
        self.retrieve_button.setText(QCoreApplication.translate("Form", u"Retrieve", None))
        self.label.setText(QCoreApplication.translate("Form", u"Treeview of Experiment", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Labbook of Experiment", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image of the Experiment", None))
        self.add_metadata_button.setText(QCoreApplication.translate("Form", u"Add Metadata to Labbook", None))
        self.save_labbook_button.setText(QCoreApplication.translate("Form", u"Save Labbook", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Form", u"Labbook", None))
    # retranslateUi


class Online_Analysis(QWidget,Ui_Online_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

