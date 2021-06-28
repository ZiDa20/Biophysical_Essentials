# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from self_config_notebook_widget import Config_Widget
from online_analysis_widget import Online_Analysis
from offline_analysis_widget import Offline_Analysis

import Figures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1792, 1008)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.self_configuration = QPushButton(self.centralwidget)
        self.self_configuration.setObjectName(u"self_configuration")
        self.self_configuration.setGeometry(QRect(20, 270, 241, 101))
        self.online_analysis = QPushButton(self.centralwidget)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis.setGeometry(QRect(20, 390, 241, 101))
        self.offline_analysis = QPushButton(self.centralwidget)
        self.offline_analysis.setObjectName(u"offline_analysis")
        self.offline_analysis.setGeometry(QRect(20, 510, 241, 101))
        self.statistics = QPushButton(self.centralwidget)
        self.statistics.setObjectName(u"statistics")
        self.statistics.setGeometry(QRect(20, 630, 241, 101))
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        self.notebook.setGeometry(QRect(290, 10, 1600, 801))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        self.notebook.addWidget(self.online)
        self.offline = Offline_Analysis()
        self.offline.setObjectName(u"offline")
        self.notebook.addWidget(self.offline)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 241, 221))
        self.label.setPixmap(QPixmap(u"../Logo/New_LOGO_2.png"))
        self.label.setScaledContents(True)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(280, 840, 1501, 111))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 820, 161, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1792, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.self_configuration.setText(QCoreApplication.translate("MainWindow", u"Self Configuration", None))
        self.online_analysis.setText(QCoreApplication.translate("MainWindow", u"Online Analysis", None))
        self.offline_analysis.setText(QCoreApplication.translate("MainWindow", u"Offline Analysis", None))
        self.statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Command Line", None))
    # retranslateUi

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)