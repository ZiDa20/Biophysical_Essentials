# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'button_toolbar_online.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(441, 684)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 150, 201, 121))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(-1, 30, 201, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 280, 201, 201))
        self.button_function_1 = QWidget(self.groupBox_3)
        self.button_function_1.setObjectName(u"button_function_1")
        self.button_function_1.setGeometry(QRect(10, 40, 181, 31))
        self.button_function_2 = QWidget(self.groupBox_3)
        self.button_function_2.setObjectName(u"button_function_2")
        self.button_function_2.setGeometry(QRect(10, 80, 181, 31))
        self.button_function_3 = QWidget(self.groupBox_3)
        self.button_function_3.setObjectName(u"button_function_3")
        self.button_function_3.setGeometry(QRect(9, 120, 181, 31))
        self.button_function_4 = QWidget(self.groupBox_3)
        self.button_function_4.setObjectName(u"button_function_4")
        self.button_function_4.setGeometry(QRect(9, 160, 181, 31))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 30, 201, 111))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 201, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Image Options:", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Cursor Bounds", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"Panning", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"Zooming", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Moving", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Image Options:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Display Options:", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Display PGF File", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Split Data and PGF Pulse", None))
    # retranslateUi

