# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_new_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

from database_viewer_widget import Database_Viewer
from offline_analysis_widget import Offline_Analysis
from online_analysis_widget import Online_Analysis
from self_configuration import Config_Widget
from settings_dialog import SettingsWindow
import Figures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1537, 950)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 950))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 2, 0, 0)
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        sizePolicy.setHeightForWidth(self.notebook.sizePolicy().hasHeightForWidth())
        self.notebook.setSizePolicy(sizePolicy)
        self.notebook.setMinimumSize(QSize(956, 500))
        self.notebook.setMaximumSize(QSize(16777215, 1000))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.notebook.addWidget(self.home)
        self.online = Online_Analysis()
        self.config = Config_Widget(self.online)
        self.config.setObjectName(u"config")
        sizePolicy.setHeightForWidth(self.config.sizePolicy().hasHeightForWidth())
        self.config.setSizePolicy(sizePolicy)
        self.notebook.addWidget(self.config)
        
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

        self.gridLayout.addWidget(self.notebook, 1, 0, 1, 1)

        self.side_left_menu = QWidget(self.centralwidget)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_left_menu.sizePolicy().hasHeightForWidth())
        self.side_left_menu.setSizePolicy(sizePolicy)
        self.side_left_menu.setMinimumSize(QSize(0, 60))
        self.side_left_menu.setMaximumSize(QSize(16777215, 100))
        self.side_left_menu.setBaseSize(QSize(61, 1000))
        self.side_left_menu.setContextMenuPolicy(Qt.PreventContextMenu)
        self.side_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_left_menu.setAutoFillBackground(False)
        self.side_left_menu.setStyleSheet(u"QWidget{\n"
"	background-color: \"#232629\";\n"
"	border-radius:10\n"
"px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 1px 5px;\n"
"	border: none;\n"
"	border-radius:5px;\n"
"	background-color: \"#232629\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.side_left_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_window = QPushButton(self.side_left_menu)
        self.home_window.setObjectName(u"home_window")
        sizePolicy.setHeightForWidth(self.home_window.sizePolicy().hasHeightForWidth())
        self.home_window.setSizePolicy(sizePolicy)
        self.home_window.setMinimumSize(QSize(80, 0))
        self.home_window.setMaximumSize(QSize(200, 16777215))
        self.home_window.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../Logo/new_logo_final.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: center;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.home_window)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.self_configuration = QPushButton(self.side_left_menu)
        self.self_configuration.setObjectName(u"self_configuration")
        self.self_configuration.setEnabled(True)
        sizePolicy.setHeightForWidth(self.self_configuration.sizePolicy().hasHeightForWidth())
        self.self_configuration.setSizePolicy(sizePolicy)
        self.self_configuration.setMinimumSize(QSize(200, 0))
        self.self_configuration.setMaximumSize(QSize(300, 80))
        font = QFont()
        font.setPointSize(12)
        self.self_configuration.setFont(font)
        self.self_configuration.setContextMenuPolicy(Qt.PreventContextMenu)
        self.self_configuration.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/SC_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
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

        self.horizontalLayout.addWidget(self.self_configuration)

        self.online_analysis = QPushButton(self.side_left_menu)
        self.online_analysis.setObjectName(u"online_analysis")
        sizePolicy.setHeightForWidth(self.online_analysis.sizePolicy().hasHeightForWidth())
        self.online_analysis.setSizePolicy(sizePolicy)
        self.online_analysis.setMinimumSize(QSize(200, 0))
        self.online_analysis.setMaximumSize(QSize(300, 80))
        self.online_analysis.setFont(font)
        self.online_analysis.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Ona_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.online_analysis)

        self.offline_analysis = QPushButton(self.side_left_menu)
        self.offline_analysis.setObjectName(u"offline_analysis")
        sizePolicy.setHeightForWidth(self.offline_analysis.sizePolicy().hasHeightForWidth())
        self.offline_analysis.setSizePolicy(sizePolicy)
        self.offline_analysis.setMinimumSize(QSize(200, 0))
        self.offline_analysis.setMaximumSize(QSize(300, 80))
        self.offline_analysis.setFont(font)
        self.offline_analysis.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Ofa_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")
        self.offline_analysis.setIconSize(QSize(16, 20))

        self.horizontalLayout.addWidget(self.offline_analysis)

        self.statistics = QPushButton(self.side_left_menu)
        self.statistics.setObjectName(u"statistics")
        sizePolicy.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy)
        self.statistics.setMinimumSize(QSize(200, 0))
        self.statistics.setMaximumSize(QSize(300, 80))
        self.statistics.setFont(font)
        self.statistics.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/St_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.statistics)

        self.settings_button = QPushButton(self.side_left_menu)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QSize(200, 0))
        self.settings_button.setMaximumSize(QSize(300, 80))
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/setting_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.settings_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.darkmode_button = QPushButton(self.side_left_menu)
        self.darkmode_button.setObjectName(u"darkmode_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.darkmode_button.sizePolicy().hasHeightForWidth())
        self.darkmode_button.setSizePolicy(sizePolicy1)
        self.darkmode_button.setMinimumSize(QSize(20, 0))
        self.darkmode_button.setMaximumSize(QSize(60, 80))
        self.darkmode_button.setFont(font)
        self.darkmode_button.setStyleSheet(u"QPushButton {\n"
"\n"
"\n"
"background-image: url(../QT_GUI/Button/Logo/Lightmode_button.png);\n"
"background-repeat:None;\n"
"color: #d2691e;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border: none;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.darkmode_button)

        self.minimize_button = QPushButton(self.side_left_menu)
        self.minimize_button.setObjectName(u"minimize_button")

        self.horizontalLayout.addWidget(self.minimize_button)

        self.pushButton_3 = QPushButton(self.side_left_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.maximize_button = QPushButton(self.side_left_menu)
        self.maximize_button.setObjectName(u"maximize_button")

        self.horizontalLayout.addWidget(self.maximize_button)


        self.gridLayout.addWidget(self.side_left_menu, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.notebook.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_window.setText("")
        self.online_analysis.setText("")
        self.offline_analysis.setText("")
        self.statistics.setText("")
        self.settings_button.setText("")
        self.darkmode_button.setText("")
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

