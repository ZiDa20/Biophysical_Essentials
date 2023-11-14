# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dz_08012023_main_window_new_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QWidget)

from Backend.self_configuration import Config_Widget
from QT_GUI.OnlineAnalysis.ui_py.online_analysis_widget import Online_Analysis
from QT_GUI.OfflineAnalysis.ui_py.offline_analysis_widget import Offline_Analysis
from QT_GUI.Settings.ui_py.settings_dialog import SettingsWindow
from QT_GUI.DatabaseViewer.ui_py.database_viewer_widget import Database_Viewer


import Figures_rc
from StyleFrontend.frontend_style import Frontend_Style

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
        background_image_path = "C:/Users/davee/Desktop/SP/Biophysical_Essentials/QT_GUI/Button/Logo/welcome_page_background_logo.png"  # Replace with the actual path to your PNG file

        # Set background image #  \"background-color: grey;" \
        style_sheet = u"QWidget {"\
               "background-image: url(../QT_GUI/Button/Logo/welcome_page_background_logo.png);" \
               "background-repeat: no-repeat;" \
               "background-position: center;" \
               "}"
        #MainWindow.setStyleSheet(style_sheet)
        #MainWindow.setStyleSheet(u"QMainWindow{\n"
        #"border-radius: 10px\n"
        #"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.centralwidget.setStyleSheet(style_sheet)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.notebook = QStackedWidget(self.centralwidget)
        self.notebook.setObjectName(u"notebook")
        sizePolicy.setHeightForWidth(self.notebook.sizePolicy().hasHeightForWidth())
        self.notebook.setSizePolicy(sizePolicy)
        self.notebook.setMinimumSize(QSize(1100, 900))
        self.notebook.setMaximumSize(QSize(16777215, 2000))
        #self.notebook.setStyleSheet(style_sheet)
        
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
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 7, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 3)

        self.home_logo = QToolButton(self.frame)
        self.home_logo.setObjectName(u"home_logo")
        sizePolicy.setHeightForWidth(self.home_logo.sizePolicy().hasHeightForWidth())
        self.home_logo.setSizePolicy(sizePolicy)
        self.home_logo.setMinimumSize(QSize(240, 80))
        self.home_logo.setMaximumSize(QSize(200, 100))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.home_logo.setFont(font1)
        self.home_logo.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon = QIcon()
        icon.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/online_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_logo.setIcon(icon)
        self.home_logo.setIconSize(QSize(200, 200))
        self.home_logo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.home_logo, 6, 3, 1, 1)

        self.online_analysis_home_2 = QToolButton(self.frame)
        self.online_analysis_home_2.setObjectName(u"online_analysis_home_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.online_analysis_home_2.sizePolicy().hasHeightForWidth())
        self.online_analysis_home_2.setSizePolicy(sizePolicy1)
        self.online_analysis_home_2.setMinimumSize(QSize(240, 80))
        self.online_analysis_home_2.setMaximumSize(QSize(200, 100))
        self.online_analysis_home_2.setFont(font1)
        self.online_analysis_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon1 = QIcon()
        icon1.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/online_analysis_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.online_analysis_home_2.setIcon(icon1)
        self.online_analysis_home_2.setIconSize(QSize(200, 200))
        self.online_analysis_home_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.online_analysis_home_2, 5, 2, 1, 1)

        self.offline_analysis_home_2 = QToolButton(self.frame)
        self.offline_analysis_home_2.setObjectName(u"offline_analysis_home_2")
        sizePolicy.setHeightForWidth(self.offline_analysis_home_2.sizePolicy().hasHeightForWidth())
        self.offline_analysis_home_2.setSizePolicy(sizePolicy)
        self.offline_analysis_home_2.setMinimumSize(QSize(240, 80))
        self.offline_analysis_home_2.setMaximumSize(QSize(200, 100))
        self.offline_analysis_home_2.setFont(font1)
        self.offline_analysis_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon2 = QIcon()
        icon2.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/offline_analysis_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.offline_analysis_home_2.setIcon(icon2)
        self.offline_analysis_home_2.setIconSize(QSize(200, 200))
        self.offline_analysis_home_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.offline_analysis_home_2, 5, 3, 1, 1)

        self.configuration_home_2 = QToolButton(self.frame)
        self.configuration_home_2.setObjectName(u"configuration_home_2")
        sizePolicy.setHeightForWidth(self.configuration_home_2.sizePolicy().hasHeightForWidth())
        self.configuration_home_2.setSizePolicy(sizePolicy)
        self.configuration_home_2.setMinimumSize(QSize(240, 80))
        self.configuration_home_2.setMaximumSize(QSize(200, 100))
        self.configuration_home_2.setFont(font1)
        self.configuration_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon3 = QIcon()
        icon3.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/configure_experiment_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.configuration_home_2.setIcon(icon3)
        self.configuration_home_2.setIconSize(QSize(200, 200))
        self.configuration_home_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.configuration_home_2, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 3, 1, 1, 3)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.database_viewer_home_2 = QToolButton(self.frame)
        self.database_viewer_home_2.setObjectName(u"database_viewer_home_2")
        sizePolicy.setHeightForWidth(self.database_viewer_home_2.sizePolicy().hasHeightForWidth())
        self.database_viewer_home_2.setSizePolicy(sizePolicy)
        self.database_viewer_home_2.setMinimumSize(QSize(240, 80))
        self.database_viewer_home_2.setMaximumSize(QSize(200, 100))
        self.database_viewer_home_2.setFont(font1)
        self.database_viewer_home_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon4 = QIcon()
        icon4.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/database_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.database_viewer_home_2.setIcon(icon4)
        self.database_viewer_home_2.setIconSize(QSize(200, 200))
        self.database_viewer_home_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.database_viewer_home_2, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.frame)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QSize(240, 80))
        self.toolButton_2.setMaximumSize(QSize(10, 100))
        self.toolButton_2.setFont(font1)
        self.toolButton_2.setStyleSheet(u"QToolButton{ min-width: 15em; min-height: 5em; background-color: transparent; border: 0px; } \n"
"\n"
"QToolButton:hover{background-color: grey;}")
        icon5 = QIcon()
        icon5.addFile(u"../../../../Desktop/SP/Biophysical_Essentials/QT_GUI/Button/welcome_page/settings_welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setIconSize(QSize(200, 200))
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_4.addWidget(self.toolButton_2, 6, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.side_left_menu = QWidget(self.frame)
        self.side_left_menu.setObjectName(u"side_left_menu")
        self.side_left_menu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.side_left_menu.sizePolicy().hasHeightForWidth())
        self.side_left_menu.setSizePolicy(sizePolicy)
        self.side_left_menu.setMinimumSize(QSize(0, 20))
        self.side_left_menu.setMaximumSize(QSize(16777215, 250))
        self.side_left_menu.setBaseSize(QSize(61, 1000))
        self.side_left_menu.setContextMenuPolicy(Qt.PreventContextMenu)
        self.side_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_left_menu.setAutoFillBackground(False)
        self.side_left_menu.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.side_left_menu)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.side_left_menu, 1, 0, 1, 1)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Biophysical Essentials", None))
        self.home_logo.setText(QCoreApplication.translate("MainWindow", u"BPE Online", None))
        self.online_analysis_home_2.setText(QCoreApplication.translate("MainWindow", u"Online Analysis", None))
        self.offline_analysis_home_2.setText(QCoreApplication.translate("MainWindow", u"Offline Analysis", None))
        self.configuration_home_2.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Patch Clamp Module", None))
        self.database_viewer_home_2.setText(QCoreApplication.translate("MainWindow", u"Database Viewer", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(accessibility)
        self.side_left_menu.setAccessibleName(QCoreApplication.translate("MainWindow", u"additional_function_menu", None))
#endif // QT_CONFIG(accessibility)
    # retranslateUi

