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
        MainWindow.resize(1866, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1700, 1000))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1430, 940, 411, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setAcceptDrops(False)
        self.frame.setStyleSheet(u"QFrame{\n"
"	gackground: transparent\n"
"	border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"\n"
"	background-color:white\n"
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 31, 400, 300))
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(400, 300))
        self.textEdit.setMaximumSize(QSize(400, 300))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 338, 400, 20))
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(400, 20))
        self.lineEdit.setMaximumSize(QSize(400, 20))
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 365, 80, 23))
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(80, 23))
        self.pushButton.setMaximumSize(QSize(80, 23))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 11, 150, 13))
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(150, 13))
        self.label_2.setMaximumSize(QSize(150, 13))
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        self.notebook.setGeometry(QRect(68, 1, 1771, 901))
        sizePolicy.setHeightForWidth(self.notebook.sizePolicy().hasHeightForWidth())
        self.notebook.setSizePolicy(sizePolicy)
        self.notebook.setMinimumSize(QSize(0, 0))
        self.notebook.setMaximumSize(QSize(16777215, 16777215))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        self.notebook.addWidget(self.online)
        self.offline = Offline_Analysis()
        self.offline.setObjectName(u"offline")
        self.notebook.addWidget(self.offline)
        self.side_left_menu = QFrame(self.centralwidget)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setGeometry(QRect(1, 1, 61, 981))
        sizePolicy1.setHeightForWidth(self.side_left_menu.sizePolicy().hasHeightForWidth())
        self.side_left_menu.setSizePolicy(sizePolicy1)
        self.side_left_menu.setMinimumSize(QSize(0, 0))
        self.side_left_menu.setMaximumSize(QSize(16777215, 100000))
        self.side_left_menu.setBaseSize(QSize(61, 1000))
        self.side_left_menu.setContextMenuPolicy(Qt.PreventContextMenu)
        self.side_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_left_menu.setAutoFillBackground(False)
        self.side_left_menu.setStyleSheet(u"QFrame{\n"
"	background-color: \"#232629\";\n"
"	border-radius:5px;\n"
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
        self.gridLayout_3 = QGridLayout(self.side_left_menu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.statistics = QPushButton(self.side_left_menu)
        self.statistics.setObjectName(u"statistics")
        sizePolicy1.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy1)
        self.statistics.setMinimumSize(QSize(301, 0))
        self.statistics.setMaximumSize(QSize(301, 70))
        font1 = QFont()
        font1.setPointSize(12)
        self.statistics.setFont(font1)
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

        self.gridLayout_3.addWidget(self.statistics, 7, 0, 1, 1)

        self.darkmode_button = QPushButton(self.side_left_menu)
        self.darkmode_button.setObjectName(u"darkmode_button")
        sizePolicy1.setHeightForWidth(self.darkmode_button.sizePolicy().hasHeightForWidth())
        self.darkmode_button.setSizePolicy(sizePolicy1)
        self.darkmode_button.setMinimumSize(QSize(301, 0))
        self.darkmode_button.setMaximumSize(QSize(301, 70))
        self.darkmode_button.setFont(font1)
        self.darkmode_button.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/Lightmode_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")

        self.gridLayout_3.addWidget(self.darkmode_button, 10, 0, 1, 1)

        self.settings_button = QPushButton(self.side_left_menu)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy1.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy1)
        self.settings_button.setMinimumSize(QSize(301, 0))
        self.settings_button.setMaximumSize(QSize(301, 70))
        self.settings_button.setFont(font1)
        self.settings_button.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"\n"
"background-image:url(../QT_GUI/Button/Logo/setting_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding-left: 30px;\n"
"background-position:left;\n"
"}")

        self.gridLayout_3.addWidget(self.settings_button, 8, 0, 1, 1)

        self.offline_analysis = QPushButton(self.side_left_menu)
        self.offline_analysis.setObjectName(u"offline_analysis")
        sizePolicy1.setHeightForWidth(self.offline_analysis.sizePolicy().hasHeightForWidth())
        self.offline_analysis.setSizePolicy(sizePolicy1)
        self.offline_analysis.setMinimumSize(QSize(301, 0))
        self.offline_analysis.setMaximumSize(QSize(301, 70))
        self.offline_analysis.setFont(font1)
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
        self.offline_analysis.setIconSize(QSize(16, 20))

        self.gridLayout_3.addWidget(self.offline_analysis, 4, 0, 1, 1)

        self.konsole_button = QPushButton(self.side_left_menu)
        self.konsole_button.setObjectName(u"konsole_button")
        sizePolicy1.setHeightForWidth(self.konsole_button.sizePolicy().hasHeightForWidth())
        self.konsole_button.setSizePolicy(sizePolicy1)
        self.konsole_button.setMinimumSize(QSize(301, 0))
        self.konsole_button.setMaximumSize(QSize(301, 70))
        self.konsole_button.setFont(font1)
        self.konsole_button.setStyleSheet(u"\n"
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

        self.gridLayout_3.addWidget(self.konsole_button, 5, 0, 1, 1)

        self.online_analysis = QPushButton(self.side_left_menu)
        self.online_analysis.setObjectName(u"online_analysis")
        sizePolicy1.setHeightForWidth(self.online_analysis.sizePolicy().hasHeightForWidth())
        self.online_analysis.setSizePolicy(sizePolicy1)
        self.online_analysis.setMinimumSize(QSize(301, 0))
        self.online_analysis.setMaximumSize(QSize(301, 70))
        self.online_analysis.setFont(font1)
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

        self.gridLayout_3.addWidget(self.online_analysis, 3, 0, 1, 1)

        self.self_configuration = QPushButton(self.side_left_menu)
        self.self_configuration.setObjectName(u"self_configuration")
        sizePolicy1.setHeightForWidth(self.self_configuration.sizePolicy().hasHeightForWidth())
        self.self_configuration.setSizePolicy(sizePolicy1)
        self.self_configuration.setMinimumSize(QSize(301, 0))
        self.self_configuration.setMaximumSize(QSize(301, 70))
        self.self_configuration.setFont(font1)
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

        self.gridLayout_3.addWidget(self.self_configuration, 2, 0, 1, 1)

        self.hamburger_button = QPushButton(self.side_left_menu)
        self.hamburger_button.setObjectName(u"hamburger_button")
        sizePolicy1.setHeightForWidth(self.hamburger_button.sizePolicy().hasHeightForWidth())
        self.hamburger_button.setSizePolicy(sizePolicy1)
        self.hamburger_button.setMinimumSize(QSize(301, 0))
        self.hamburger_button.setMaximumSize(QSize(301, 70))
        self.hamburger_button.setStyleSheet(u"background-image:url(../QT_GUI/Button/Logo/hamburger_menu.png);\n"
"background-repeat:None;\n"
"padding-left: 30px;\n"
"background-position: left;")

        self.gridLayout_3.addWidget(self.hamburger_button, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.notebook.raise_()
        self.frame.raise_()
        self.side_left_menu.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pro Mode Konsole Mode", None))
        self.statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.darkmode_button.setText(QCoreApplication.translate("MainWindow", u"   Appearance", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.offline_analysis.setText(QCoreApplication.translate("MainWindow", u"    Offline Analysis", None))
        self.konsole_button.setText(QCoreApplication.translate("MainWindow", u"Open Console", None))
        self.online_analysis.setText(QCoreApplication.translate("MainWindow", u"   Online Analysis", None))
        self.self_configuration.setText(QCoreApplication.translate("MainWindow", u"      Self Configuration", None))
        self.hamburger_button.setText("")
    # retranslateUi

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
