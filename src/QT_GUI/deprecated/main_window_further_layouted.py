# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_further_layouted.ui'
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
from offline_analysis import Offline_Analysis

import Figures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 1024)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 1024))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        sizePolicy.setHeightForWidth(self.notebook.sizePolicy().hasHeightForWidth())
        self.notebook.setSizePolicy(sizePolicy)
        self.notebook.setMinimumSize(QSize(956, 986))
        self.notebook.setMaximumSize(QSize(16777215, 1200))
        self.config = Config_Widget()
        self.config.setObjectName(u"config")
        sizePolicy.setHeightForWidth(self.config.sizePolicy().hasHeightForWidth())
        self.config.setSizePolicy(sizePolicy)
        self.notebook.addWidget(self.config)
        self.online = Online_Analysis()
        self.online.setObjectName(u"online")
        sizePolicy.setHeightForWidth(self.online.sizePolicy().hasHeightForWidth())
        self.online.setSizePolicy(sizePolicy)
        self.notebook.addWidget(self.online)
        self.offline = Offline_Analysis()
        self.offline.setObjectName(u"offline")
        sizePolicy.setHeightForWidth(self.offline.sizePolicy().hasHeightForWidth())
        self.offline.setSizePolicy(sizePolicy)
        self.notebook.addWidget(self.offline)

        self.gridLayout_2.addWidget(self.notebook, 0, 2, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(300, 10))
        self.frame.setMaximumSize(QSize(300, 500))
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
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(150, 13))
        font = QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(400, 300))

        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(400, 20))

        self.gridLayout_3.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(80, 23))

        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 2, 1, 1)

        self.side_left_menu = QWidget(self.centralwidget)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side_left_menu.sizePolicy().hasHeightForWidth())
        self.side_left_menu.setSizePolicy(sizePolicy3)
        self.side_left_menu.setMinimumSize(QSize(80, 0))
        self.side_left_menu.setMaximumSize(QSize(300, 1200))
        self.side_left_menu.setBaseSize(QSize(61, 1000))
        self.side_left_menu.setContextMenuPolicy(Qt.PreventContextMenu)
        self.side_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_left_menu.setAutoFillBackground(False)
        self.side_left_menu.setStyleSheet(u"QWidget{\n"
"	background-color: \"#232629\"\n"
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
        self.gridLayout = QGridLayout(self.side_left_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.konsole_button = QPushButton(self.side_left_menu)
        self.konsole_button.setObjectName(u"konsole_button")
        sizePolicy.setHeightForWidth(self.konsole_button.sizePolicy().hasHeightForWidth())
        self.konsole_button.setSizePolicy(sizePolicy)
        self.konsole_button.setMinimumSize(QSize(80, 0))
        self.konsole_button.setMaximumSize(QSize(200, 70))
        font1 = QFont()
        font1.setPointSize(12)
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

        self.gridLayout.addWidget(self.konsole_button, 4, 0, 1, 1)

        self.settings_button = QPushButton(self.side_left_menu)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QSize(80, 0))
        self.settings_button.setMaximumSize(QSize(200, 70))
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

        self.gridLayout.addWidget(self.settings_button, 6, 0, 1, 1)

        self.hamburger_button = QPushButton(self.side_left_menu)
        self.hamburger_button.setObjectName(u"hamburger_button")
        sizePolicy.setHeightForWidth(self.hamburger_button.sizePolicy().hasHeightForWidth())
        self.hamburger_button.setSizePolicy(sizePolicy)
        self.hamburger_button.setMinimumSize(QSize(80, 0))
        self.hamburger_button.setMaximumSize(QSize(200, 70))
        self.hamburger_button.setStyleSheet(u"background-image:url(../QT_GUI/Button/Logo/hamburger_menu.png);\n"
"background-repeat:None;\n"
"padding-left: 30px;\n"
"background-position: left;")

        self.gridLayout.addWidget(self.hamburger_button, 0, 0, 1, 1)

        self.offline_analysis = QPushButton(self.side_left_menu)
        self.offline_analysis.setObjectName(u"offline_analysis")
        sizePolicy.setHeightForWidth(self.offline_analysis.sizePolicy().hasHeightForWidth())
        self.offline_analysis.setSizePolicy(sizePolicy)
        self.offline_analysis.setMinimumSize(QSize(80, 0))
        self.offline_analysis.setMaximumSize(QSize(200, 70))
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

        self.gridLayout.addWidget(self.offline_analysis, 3, 0, 1, 1)

        self.statistics = QPushButton(self.side_left_menu)
        self.statistics.setObjectName(u"statistics")
        sizePolicy.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy)
        self.statistics.setMinimumSize(QSize(80, 0))
        self.statistics.setMaximumSize(QSize(200, 70))
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

        self.gridLayout.addWidget(self.statistics, 5, 0, 1, 1)

        self.darkmode_button = QPushButton(self.side_left_menu)
        self.darkmode_button.setObjectName(u"darkmode_button")
        sizePolicy.setHeightForWidth(self.darkmode_button.sizePolicy().hasHeightForWidth())
        self.darkmode_button.setSizePolicy(sizePolicy)
        self.darkmode_button.setMinimumSize(QSize(80, 0))
        self.darkmode_button.setMaximumSize(QSize(200, 70))
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

        self.gridLayout.addWidget(self.darkmode_button, 7, 0, 1, 1)

        self.self_configuration = QPushButton(self.side_left_menu)
        self.self_configuration.setObjectName(u"self_configuration")
        self.self_configuration.setEnabled(True)
        sizePolicy.setHeightForWidth(self.self_configuration.sizePolicy().hasHeightForWidth())
        self.self_configuration.setSizePolicy(sizePolicy)
        self.self_configuration.setMinimumSize(QSize(80, 0))
        self.self_configuration.setMaximumSize(QSize(200, 70))
        self.self_configuration.setFont(font1)
        self.self_configuration.setContextMenuPolicy(Qt.PreventContextMenu)
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
        self.self_configuration.setText(u"")
        self.self_configuration.setFlat(False)

        self.gridLayout.addWidget(self.self_configuration, 1, 0, 1, 1)

        self.online_analysis = QPushButton(self.side_left_menu)
        self.online_analysis.setObjectName(u"online_analysis")
        sizePolicy.setHeightForWidth(self.online_analysis.sizePolicy().hasHeightForWidth())
        self.online_analysis.setSizePolicy(sizePolicy)
        self.online_analysis.setMinimumSize(QSize(80, 0))
        self.online_analysis.setMaximumSize(QSize(200, 70))
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

        self.gridLayout.addWidget(self.online_analysis, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.side_left_menu, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.notebook.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pro Mode Konsole Mode", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.konsole_button.setText("")
        self.settings_button.setText("")
        self.hamburger_button.setText("")
        self.offline_analysis.setText("")
        self.statistics.setText("")
        self.darkmode_button.setText("")
        self.online_analysis.setText("")
    # retranslateUi

