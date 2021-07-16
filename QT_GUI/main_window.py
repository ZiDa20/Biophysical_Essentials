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

from self_configuration import Config_Widget
from online_analysis_widget import Online_Analysis
from offline_analysis_widget import Offline_Analysis

import Figures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1906, 1033)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        self.notebook.setGeometry(QRect(110, 30, 1711, 961))
        self.notebook.setMinimumSize(QSize(0, 0))
        self.notebook.setMaximumSize(QSize(16777215, 16777215))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        self.notebook.addWidget(self.online)
        self.side_left_menu = QFrame(self.centralwidget)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setGeometry(QRect(0, 0, 71, 1000))
        self.side_left_menu.setMinimumSize(QSize(50, 0))
        self.side_left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.side_left_menu.setStyleSheet(u"QFrame{\n"
"	background-color: \"#232629\";\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	background-color: \"#232629\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}")
        self.side_left_menu.setFrameShape(QFrame.StyledPanel)
        self.side_left_menu.setFrameShadow(QFrame.Raised)
        self.self_configuration = QPushButton(self.side_left_menu)
        self.self_configuration.setObjectName(u"self_configuration")
        self.self_configuration.setGeometry(QRect(10, 130, 281, 71))
        self.self_configuration.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        self.self_configuration.setFont(font)
        self.self_configuration.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/SC_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position: left;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.online_analysis = QPushButton(self.side_left_menu)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis.setGeometry(QRect(10, 240, 281, 71))
        self.online_analysis.setMinimumSize(QSize(0, 0))
        self.online_analysis.setFont(font)
        self.online_analysis.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Ona_button.png);\n"
"background-repeat:none;\n"
"color: #d2691e;\n"
"padding-left:30px;\n"
"background-position:left;\n"
"\n"
"}\n"
"")
        self.offline_analysis = QPushButton(self.side_left_menu)
        self.offline_analysis.setObjectName(u"offline_analysis")
        self.offline_analysis.setGeometry(QRect(10, 350, 281, 71))
        self.offline_analysis.setMinimumSize(QSize(0, 0))
        self.offline_analysis.setFont(font)
        self.offline_analysis.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/Ofa_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")
        self.statistics = QPushButton(self.side_left_menu)
        self.statistics.setObjectName(u"statistics")
        self.statistics.setGeometry(QRect(10, 460, 281, 71))
        self.statistics.setMinimumSize(QSize(0, 0))
        self.statistics.setFont(font)
        self.statistics.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/St_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")
        self.statistics_2 = QPushButton(self.side_left_menu)
        self.statistics_2.setObjectName(u"statistics_2")
        self.statistics_2.setGeometry(QRect(10, 560, 311, 81))
        self.statistics_2.setMinimumSize(QSize(0, 0))
        self.statistics_2.setFont(font)
        self.statistics_2.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/konsole_button.png);\n"
"color: #d2691e;\n"
"background-repeat:None;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"\n"
"}")
        self.label = QLabel(self.side_left_menu)
        self.offline = Offline_Analysis()
        self.offline.setObjectName(u"offline")
        self.notebook.addWidget(self.offline)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 121, 111))
        self.label.setPixmap(QPixmap(u"../../../.designer/Logo/New_LOGO_2.png"))
        self.label.setScaledContents(True)
        self.hamburger_button = QPushButton(self.side_left_menu)
        self.hamburger_button.setObjectName(u"hamburger_button")
        self.hamburger_button.setGeometry(QRect(10, 20, 51, 81))
        self.hamburger_button.setStyleSheet(u"background-image:url(../QT_GUI/Button/Logo/Hamburger.png);\n"
"background-repeat:None;\n"
"padding-left: 30px;\n"
"background-position: left;")
        self.offline_analysis_2 = QPushButton(self.side_left_menu)
        self.offline_analysis_2.setObjectName(u"offline_analysis_2")
        self.offline_analysis_2.setGeometry(QRect(10, 860, 281, 71))
        self.offline_analysis_2.setMinimumSize(QSize(0, 0))
        self.offline_analysis_2.setFont(font)
        self.offline_analysis_2.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/Lightmode_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")
        self.offline_analysis_3 = QPushButton(self.side_left_menu)
        self.offline_analysis_3.setObjectName(u"offline_analysis_3")
        self.offline_analysis_3.setGeometry(QRect(10, 760, 281, 71))
        self.offline_analysis_3.setMinimumSize(QSize(0, 0))
        self.offline_analysis_3.setFont(font)
        self.offline_analysis_3.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/setting_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1906, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.self_configuration.setText(QCoreApplication.translate("MainWindow", u"             Self Configuration", None))
        self.online_analysis.setText(QCoreApplication.translate("MainWindow", u"         Online Analysis", None))
        self.offline_analysis.setText(QCoreApplication.translate("MainWindow", u"        Offline Analysis", None))
        self.statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.statistics_2.setText(QCoreApplication.translate("MainWindow", u"Open Console", None))
        self.label.setText("")
        self.hamburger_button.setText("")
        self.offline_analysis_2.setText(QCoreApplication.translate("MainWindow", u"   Appearance", None))
        self.offline_analysis_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)