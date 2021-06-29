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
        self.notebook.setGeometry(QRect(299, 10, 1591, 801))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        self.notebook.addWidget(self.online)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 830, 161, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 241, 231))
        self.label.setPixmap(QPixmap(u"../Logo/New_LOGO_2.png"))
        self.label.setScaledContents(True)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(299, 850, 1481, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1479, 99))
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, -10, 1491, 111))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Command Line", None))
        self.label.setText("")
    # retranslateUi

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)