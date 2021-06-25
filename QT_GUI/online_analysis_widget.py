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
        Form.resize(1675, 875)
        self.online_analysis = QTabWidget(Form)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis.setGeometry(QRect(-10, 10, 1600, 770))
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        self.button_select_data_file = QPushButton(self.online_analysis_window)
        self.button_select_data_file.setObjectName(u"button_select_data_file")
        self.button_select_data_file.setGeometry(QRect(10, 10, 181, 31))
        self.button_switch_to_labbook = QPushButton(self.online_analysis_window)
        self.button_switch_to_labbook.setObjectName(u"button_switch_to_labbook")
        self.button_switch_to_labbook.setGeometry(QRect(200, 10, 181, 31))
        self.horizontalLayoutWidget = QWidget(self.online_analysis_window)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 80, 1411, 501))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mpl_canvas = QWidget(self.horizontalLayoutWidget)
        self.mpl_canvas.setObjectName(u"mpl_canvas")

        self.horizontalLayout.addWidget(self.mpl_canvas)

        self.button_toolbar_online = QWidget(self.horizontalLayoutWidget)
        self.button_toolbar_online.setObjectName(u"button_toolbar_online")

        self.horizontalLayout.addWidget(self.button_toolbar_online)

        self.treeview_widget = QWidget(self.horizontalLayoutWidget)
        self.treeview_widget.setObjectName(u"treeview_widget")

        self.horizontalLayout.addWidget(self.treeview_widget)

        self.line = QFrame(self.online_analysis_window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 50, 1431, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.online_analysis_window)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 700, 1431, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_2 = QWidget(self.online_analysis_window)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(770, 600, 651, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.horizontalLayoutWidget_2)
        self.widget.setObjectName(u"widget")
        self.button_transfer_to_offline = QWidget(self.widget)
        self.button_transfer_to_offline.setObjectName(u"button_transfer_to_offline")
        self.button_transfer_to_offline.setGeometry(QRect(0, 0, 211, 80))
        self.button_discard_series = QWidget(self.widget)
        self.button_discard_series.setObjectName(u"button_discard_series")
        self.button_discard_series.setGeometry(QRect(240, 0, 191, 80))
        self.widget_4 = QWidget(self.button_discard_series)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(230, 0, 191, 80))
        self.button_save_current_trace = QWidget(self.button_discard_series)
        self.button_save_current_trace.setObjectName(u"button_save_current_trace")
        self.button_save_current_trace.setGeometry(QRect(220, 0, 191, 80))
        self.widget_5 = QWidget(self.button_save_current_trace)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(230, 0, 191, 80))

        self.horizontalLayout_2.addWidget(self.widget)

        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.verticalLayoutWidget = QWidget(self.labbook_window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 271, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.treeview_experiment = QTreeView(self.verticalLayoutWidget)
        self.treeview_experiment.setObjectName(u"treeview_experiment")

        self.verticalLayout.addWidget(self.treeview_experiment)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.retrieve_button = QPushButton(self.verticalLayoutWidget)
        self.retrieve_button.setObjectName(u"retrieve_button")

        self.verticalLayout.addWidget(self.retrieve_button)

        self.discard_button = QPushButton(self.verticalLayoutWidget)
        self.discard_button.setObjectName(u"discard_button")

        self.verticalLayout.addWidget(self.discard_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.treeview_experiment_discarded = QTreeView(self.verticalLayoutWidget)
        self.treeview_experiment_discarded.setObjectName(u"treeview_experiment_discarded")

        self.verticalLayout.addWidget(self.treeview_experiment_discarded)

        self.verticalLayoutWidget_2 = QWidget(self.labbook_window)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1100, 20, 311, 681))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.image_experiment = QGraphicsView(self.verticalLayoutWidget_2)
        self.image_experiment.setObjectName(u"image_experiment")

        self.verticalLayout_2.addWidget(self.image_experiment)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_9)

        self.add_metadata_button = QPushButton(self.verticalLayoutWidget_2)
        self.add_metadata_button.setObjectName(u"add_metadata_button")

        self.verticalLayout_2.addWidget(self.add_metadata_button)

        self.save_labbook_button = QPushButton(self.verticalLayoutWidget_2)
        self.save_labbook_button.setObjectName(u"save_labbook_button")

        self.verticalLayout_2.addWidget(self.save_labbook_button)

        self.verticalLayoutWidget_3 = QWidget(self.labbook_window)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(300, 20, 791, 681))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.online_analysis.addTab(self.labbook_window, "")

        self.retranslateUi(Form)

        self.online_analysis.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_select_data_file.setText(QCoreApplication.translate("Form", u"Select a .Dat File:", None))
        self.button_switch_to_labbook.setText(QCoreApplication.translate("Form", u"Switch to Labbook", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Form", u"Online Analysis", None))
        self.label.setText(QCoreApplication.translate("Form", u"Treeview of Experiment", None))
        self.retrieve_button.setText(QCoreApplication.translate("Form", u"Retrieve", None))
        self.discard_button.setText(QCoreApplication.translate("Form", u"Discard", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image of the Experiment", None))
        self.add_metadata_button.setText(QCoreApplication.translate("Form", u"Add Metadata to Labbook", None))
        self.save_labbook_button.setText(QCoreApplication.translate("Form", u"Save Labbook", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Labbook of Experiment", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Form", u"Labbook", None))
    # retranslateUi

class Online_Analysis(QWidget,Ui_Online_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)