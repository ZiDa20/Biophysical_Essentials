# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_new_layout.ui'
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
from settings_dialog import SettingsWindow
from database_viewer_widget import Database_Viewer

import Figures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 950)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 950))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"border-radius: 10px\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.side_left_menu = QWidget(self.centralwidget)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_left_menu.sizePolicy().hasHeightForWidth())
        self.side_left_menu.setSizePolicy(sizePolicy)
        self.side_left_menu.setMinimumSize(QSize(0, 60))
        self.side_left_menu.setMaximumSize(QSize(60, 16777215))
        self.side_left_menu.setBaseSize(QSize(61, 1000))
        self.side_left_menu.setContextMenuPolicy(Qt.PreventContextMenu)
        self.side_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_left_menu.setAutoFillBackground(False)
        self.side_left_menu.setStyleSheet(u"QWidget{\n"
"	background-color:rgba(4,7,26, 180) ;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 1px 5px;\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	background-color: rgba(4,7,26, 0);\n"
"	background-position: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}")
        self.verticalLayout = QVBoxLayout(self.side_left_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.maximize_button = QPushButton(self.side_left_menu)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMinimumSize(QSize(20, 0))
        self.maximize_button.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Papyrus"])
        self.maximize_button.setFont(font)

        self.gridLayout_3.addWidget(self.maximize_button, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.side_left_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(20, 16777215))
        self.pushButton_3.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.minimize_button = QPushButton(self.side_left_menu)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(20, 0))
        self.minimize_button.setMaximumSize(QSize(16777215, 20))
        self.minimize_button.setFont(font)

        self.gridLayout_3.addWidget(self.minimize_button, 0, 2, 1, 1, Qt.AlignTop)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.home_window = QPushButton(self.side_left_menu)
        self.home_window.setObjectName(u"home_window")
        sizePolicy.setHeightForWidth(self.home_window.sizePolicy().hasHeightForWidth())
        self.home_window.setSizePolicy(sizePolicy)
        self.home_window.setMinimumSize(QSize(30, 0))
        self.home_window.setMaximumSize(QSize(200, 70))
        self.home_window.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../Logo/new_logo_final.png);\n"
"background-repeat:None;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.home_window)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.self_configuration = QPushButton(self.side_left_menu)
        self.self_configuration.setObjectName(u"self_configuration")
        self.self_configuration.setEnabled(True)
        sizePolicy.setHeightForWidth(self.self_configuration.sizePolicy().hasHeightForWidth())
        self.self_configuration.setSizePolicy(sizePolicy)
        self.self_configuration.setMinimumSize(QSize(30, 0))
        self.self_configuration.setMaximumSize(QSize(300, 80))
        font1 = QFont()
        font1.setPointSize(12)
        self.self_configuration.setFont(font1)
        self.self_configuration.setContextMenuPolicy(Qt.PreventContextMenu)
        self.self_configuration.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/SC_button.png);\n"
"background-repeat:None;\n"
"color: #fff5cc;\n"
"border: none;\n"
"border-radius: 5px;\n"
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

        self.verticalLayout.addWidget(self.self_configuration)

        self.online_analysis = QPushButton(self.side_left_menu)
        self.online_analysis.setObjectName(u"online_analysis")
        sizePolicy.setHeightForWidth(self.online_analysis.sizePolicy().hasHeightForWidth())
        self.online_analysis.setSizePolicy(sizePolicy)
        self.online_analysis.setMinimumSize(QSize(30, 0))
        self.online_analysis.setMaximumSize(QSize(300, 80))
        self.online_analysis.setFont(font1)
        self.online_analysis.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Ona_button.png);\n"
"background-repeat:None;\n"
"color: #fff5cc;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.online_analysis)

        self.offline_analysis = QPushButton(self.side_left_menu)
        self.offline_analysis.setObjectName(u"offline_analysis")
        sizePolicy.setHeightForWidth(self.offline_analysis.sizePolicy().hasHeightForWidth())
        self.offline_analysis.setSizePolicy(sizePolicy)
        self.offline_analysis.setMinimumSize(QSize(30, 0))
        self.offline_analysis.setMaximumSize(QSize(300, 80))
        self.offline_analysis.setFont(font1)
        self.offline_analysis.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Ofa_button.png);\n"
"background-repeat:None;\n"
"color: #fff5cc;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")
        self.offline_analysis.setIconSize(QSize(16, 20))

        self.verticalLayout.addWidget(self.offline_analysis)

        self.statistics = QPushButton(self.side_left_menu)
        self.statistics.setObjectName(u"statistics")
        sizePolicy.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy)
        self.statistics.setMinimumSize(QSize(30, 0))
        self.statistics.setMaximumSize(QSize(300, 80))
        self.statistics.setFont(font1)
        self.statistics.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/St_button.png);\n"
"background-repeat:None;\n"
"color: #fff5cc;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.statistics)

        self.settings_button = QPushButton(self.side_left_menu)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QSize(30, 0))
        self.settings_button.setMaximumSize(QSize(300, 80))
        self.settings_button.setFont(font1)
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/setting_button.png);\n"
"background-repeat:None;\n"
"color: #fff5cc;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.settings_button)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.darkmode_button = QPushButton(self.side_left_menu)
        self.darkmode_button.setObjectName(u"darkmode_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.darkmode_button.sizePolicy().hasHeightForWidth())
        self.darkmode_button.setSizePolicy(sizePolicy1)
        self.darkmode_button.setMinimumSize(QSize(30, 0))
        self.darkmode_button.setMaximumSize(QSize(100, 80))
        self.darkmode_button.setFont(font1)
        self.darkmode_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Lightmode_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.darkmode_button)


        self.gridLayout.addWidget(self.side_left_menu, 0, 0, 2, 1)

        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        sizePolicy.setHeightForWidth(self.notebook.sizePolicy().hasHeightForWidth())
        self.notebook.setSizePolicy(sizePolicy)
        self.notebook.setMinimumSize(QSize(956, 500))
        self.notebook.setMaximumSize(QSize(16777215, 1000))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_5 = QGridLayout(self.home)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setFont(font1)

        self.gridLayout_14.addWidget(self.label_3, 1, 0, 1, 1)

        self.Logo_home_2 = QLabel(self.frame)
        self.Logo_home_2.setObjectName(u"Logo_home_2")
        sizePolicy1.setHeightForWidth(self.Logo_home_2.sizePolicy().hasHeightForWidth())
        self.Logo_home_2.setSizePolicy(sizePolicy1)
        self.Logo_home_2.setMinimumSize(QSize(200, 200))
        self.Logo_home_2.setStyleSheet(u"background-image: url(../QT_GUI/Button/Logo/logo3.png)")

        self.gridLayout_14.addWidget(self.Logo_home_2, 0, 0, 1, 1)

        self.titlebar_home_2 = QLabel(self.frame)
        self.titlebar_home_2.setObjectName(u"titlebar_home_2")

        self.gridLayout_14.addWidget(self.titlebar_home_2, 1, 1, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.online_analysis_home_2 = QPushButton(self.frame)
        self.online_analysis_home_2.setObjectName(u"online_analysis_home_2")
        self.online_analysis_home_2.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.online_analysis_home_2, 2, 0, 1, 1)

        self.database_viewer_home_2 = QPushButton(self.frame)
        self.database_viewer_home_2.setObjectName(u"database_viewer_home_2")
        sizePolicy1.setHeightForWidth(self.database_viewer_home_2.sizePolicy().hasHeightForWidth())
        self.database_viewer_home_2.setSizePolicy(sizePolicy1)
        self.database_viewer_home_2.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.database_viewer_home_2, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.pushButton_2, 5, 0, 1, 1)

        self.offline_analysis_home_2 = QPushButton(self.frame)
        self.offline_analysis_home_2.setObjectName(u"offline_analysis_home_2")
        self.offline_analysis_home_2.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.offline_analysis_home_2, 3, 0, 1, 1)

        self.configuration_home_2 = QPushButton(self.frame)
        self.configuration_home_2.setObjectName(u"configuration_home_2")
        self.configuration_home_2.setMinimumSize(QSize(200, 0))

        self.gridLayout_15.addWidget(self.configuration_home_2, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_15, 2, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.module_home_2 = QLabel(self.frame)
        self.module_home_2.setObjectName(u"module_home_2")
        self.module_home_2.setFont(font1)

        self.gridLayout_16.addWidget(self.module_home_2, 3, 0, 1, 1, Qt.AlignHCenter)

        self.title_home_2 = QLabel(self.frame)
        self.title_home_2.setObjectName(u"title_home_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.title_home_2.setFont(font2)

        self.gridLayout_16.addWidget(self.title_home_2, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_14.addLayout(self.gridLayout_16, 0, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_13, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_11, 1, 1, 1, 1)

        self.notebook.addWidget(self.home)
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
        self.database = Database_Viewer()
        self.database.setObjectName(u"database")
        self.notebook.addWidget(self.database)
        self.settings = SettingsWindow()
        self.settings.setObjectName(u"settings")
        self.notebook.addWidget(self.settings)

        self.gridLayout.addWidget(self.notebook, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.notebook.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.home_window.setText("")
        self.online_analysis.setText("")
        self.offline_analysis.setText("")
        self.statistics.setText("")
        self.settings_button.setText("")
        self.darkmode_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Patch Modules:", None))
        self.Logo_home_2.setText("")
        self.titlebar_home_2.setText("")
        self.online_analysis_home_2.setText(QCoreApplication.translate("MainWindow", u"Online Analysis", None))
        self.database_viewer_home_2.setText(QCoreApplication.translate("MainWindow", u"Database Viewer", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.offline_analysis_home_2.setText(QCoreApplication.translate("MainWindow", u"Offline Analysis", None))
        self.configuration_home_2.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.module_home_2.setText(QCoreApplication.translate("MainWindow", u"Patch Clamp Module", None))
        self.title_home_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Biophysical Essentials Software", None))
    # retranslateUi

