# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self_config_notebook_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(961, 651)
        self.Notebook = QTabWidget(Config_Widget)
        self.Notebook.setObjectName(u"Notebook")
        self.Notebook.setGeometry(QRect(20, 0, 931, 621))
        self.Notebook.setTabShape(QTabWidget.Rounded)
        self.experiment_initialization = QWidget()
        self.experiment_initialization.setObjectName(u"experiment_initialization")
        self.Notebook.addTab(self.experiment_initialization, "")
        self.batch_communication = QWidget()
        self.batch_communication.setObjectName(u"batch_communication")
        self.Notebook.addTab(self.batch_communication, "")
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.Notebook.addTab(self.camera, "")

        self.retranslateUi(Config_Widget)

        self.Notebook.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.Notebook.setTabText(self.Notebook.indexOf(self.experiment_initialization), QCoreApplication.translate("Config_Widget", u"Experiment Initialization", None))
        self.Notebook.setTabText(self.Notebook.indexOf(self.batch_communication), QCoreApplication.translate("Config_Widget", u"Batch Communication", None))
        self.Notebook.setTabText(self.Notebook.indexOf(self.camera), QCoreApplication.translate("Config_Widget", u"Camera", None))
    # retranslateUi


class Config_Widget(QWidget,Ui_Config_Widget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)


