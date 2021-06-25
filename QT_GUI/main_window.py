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
        MainWindow.resize(1813, 1234)
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
        self.user_communication_frame = QFrame(self.centralwidget)
        self.user_communication_frame.setObjectName(u"user_communication_frame")
        self.user_communication_frame.setGeometry(QRect(300, 740, 1131, 80))
        self.user_communication_frame.setFrameShape(QFrame.StyledPanel)
        self.user_communication_frame.setFrameShadow(QFrame.Raised)
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        self.notebook.setGeometry(QRect(290, 10, 1600, 1000))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        self.notebook.addWidget(self.online)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 241, 221))
        self.label.setPixmap(QPixmap(u"../Logo/New_LOGO_2.png"))
        self.label.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1813, 21))
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
    # retranslateUi

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)