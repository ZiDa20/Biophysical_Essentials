# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window_designer_object.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(1771, 980)
        self.gridLayout_4 = QGridLayout(Settings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Settings)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.Set_default_user = QPushButton(self.frame)
        self.Set_default_user.setObjectName(u"Set_default_user")

        self.verticalLayout.addWidget(self.Set_default_user)

        self.initialize_devices = QPushButton(self.frame)
        self.initialize_devices.setObjectName(u"initialize_devices")

        self.verticalLayout.addWidget(self.initialize_devices)

        self.plot_appearance = QPushButton(self.frame)
        self.plot_appearance.setObjectName(u"plot_appearance")

        self.verticalLayout.addWidget(self.plot_appearance)

        self.save_location = QPushButton(self.frame)
        self.save_location.setObjectName(u"save_location")

        self.verticalLayout.addWidget(self.save_location)

        self.connect_to_webserver = QPushButton(self.frame)
        self.connect_to_webserver.setObjectName(u"connect_to_webserver")

        self.verticalLayout.addWidget(self.connect_to_webserver)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget_4 = QStackedWidget(Settings)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setStyleSheet(u"")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_11 = QLabel(self.page_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 10, 261, 31))
        font = QFont()
        font.setPointSize(25)
        self.label_11.setFont(font)
        self.label_16 = QLabel(self.page_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 131, 62, 17))
        self.label_17 = QLabel(self.page_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 79, 56, 20))
        self.lineEdit_4 = QLineEdit(self.page_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(78, 79, 371, 20))
        self.checkBox_7 = QCheckBox(self.page_7)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(78, 131, 371, 17))
        self.checkBox_8 = QCheckBox(self.page_7)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(78, 180, 371, 17))
        self.label_18 = QLabel(self.page_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 180, 49, 17))
        self.stackedWidget_4.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_7 = QGridLayout(self.page_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox = QGroupBox(self.page_8)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 700, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_5.addWidget(self.comboBox_3, 2, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_5.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_5.addWidget(self.pushButton_13, 0, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_5.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_5.addWidget(self.pushButton_15, 2, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(700, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_8)
        self.Set_plot_appearance = QWidget()
        self.Set_plot_appearance.setObjectName(u"Set_plot_appearance")
        self.stackedWidget_4.addWidget(self.Set_plot_appearance)
        self.set_file_locations = QWidget()
        self.set_file_locations.setObjectName(u"set_file_locations")
        self.stackedWidget_4.addWidget(self.set_file_locations)
        self.connect_to_database = QWidget()
        self.connect_to_database.setObjectName(u"connect_to_database")
        self.label_20 = QLabel(self.connect_to_database)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 191, 16))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_20.setFont(font1)
        self.label_21 = QLabel(self.connect_to_database)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 80, 91, 16))
        self.label_22 = QLabel(self.connect_to_database)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 140, 111, 16))
        self.label_23 = QLabel(self.connect_to_database)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 210, 101, 16))
        self.lineEdit_3 = QLineEdit(self.connect_to_database)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 70, 251, 31))
        self.lineEdit_5 = QLineEdit(self.connect_to_database)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(130, 130, 251, 31))
        self.lineEdit_6 = QLineEdit(self.connect_to_database)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(300, 250, 251, 31))
        self.pushButton_16 = QPushButton(self.connect_to_database)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(410, 140, 131, 23))
        self.pushButton_17 = QPushButton(self.connect_to_database)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(410, 80, 131, 23))
        self.label_24 = QLabel(self.connect_to_database)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(180, 260, 101, 16))
        self.label_25 = QLabel(self.connect_to_database)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(180, 320, 101, 16))
        self.lineEdit_7 = QLineEdit(self.connect_to_database)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(300, 310, 251, 31))
        self.stackedWidget_4.addWidget(self.connect_to_database)

        self.gridLayout_3.addWidget(self.stackedWidget_4, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.frame_2 = QFrame(Settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)


        self.retranslateUi(Settings)

        self.stackedWidget_4.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.Set_default_user.setText(QCoreApplication.translate("Settings", u"Set Default User", None))
        self.initialize_devices.setText(QCoreApplication.translate("Settings", u"Initialize Devices", None))
        self.plot_appearance.setText(QCoreApplication.translate("Settings", u"Set Plot Appearance", None))
        self.save_location.setText(QCoreApplication.translate("Settings", u"Set File Locations", None))
        self.connect_to_webserver.setText(QCoreApplication.translate("Settings", u"Connect to Database", None))
        self.label_11.setText(QCoreApplication.translate("Settings", u"Set Default User", None))
        self.label_16.setText(QCoreApplication.translate("Settings", u"Admin Mode:", None))
        self.label_17.setText(QCoreApplication.translate("Settings", u"User Name:", None))
        self.checkBox_7.setText(QCoreApplication.translate("Settings", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("Settings", u"CheckBox", None))
        self.label_18.setText(QCoreApplication.translate("Settings", u"Pro Mode:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Settings", u"Initialize Device", None))
        self.label_13.setText(QCoreApplication.translate("Settings", u"Select Camera Interface:", None))
        self.label_14.setText(QCoreApplication.translate("Settings", u"Select pH Meter:", None))
        self.pushButton_13.setText(QCoreApplication.translate("Settings", u"Initalize Camera", None))
        self.pushButton_14.setText(QCoreApplication.translate("Settings", u"Initialize pH meter", None))
        self.label_19.setText(QCoreApplication.translate("Settings", u"Select ...", None))
        self.pushButton_15.setText(QCoreApplication.translate("Settings", u"Initalize ...", None))
        self.label_20.setText(QCoreApplication.translate("Settings", u"Connect to database", None))
        self.label_21.setText(QCoreApplication.translate("Settings", u"Connect via IP:", None))
        self.label_22.setText(QCoreApplication.translate("Settings", u"Open DataBase File:", None))
        self.label_23.setText(QCoreApplication.translate("Settings", u"Advanced Settings:", None))
        self.pushButton_16.setText(QCoreApplication.translate("Settings", u"Open Filepath", None))
        self.pushButton_17.setText(QCoreApplication.translate("Settings", u"Connect with IP", None))
        self.label_24.setText(QCoreApplication.translate("Settings", u"Username:", None))
        self.label_25.setText(QCoreApplication.translate("Settings", u"Password:", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Settings ", None))
    # retranslateUi

