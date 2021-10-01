# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_meta_data_options_pop_up.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(778, 676)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.select_from_database_button = QPushButton(Dialog)
        self.select_from_database_button.setObjectName(u"select_from_database_button")

        self.gridLayout.addWidget(self.select_from_database_button, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.assign_now_button = QPushButton(Dialog)
        self.assign_now_button.setObjectName(u"assign_now_button")

        self.gridLayout.addWidget(self.assign_now_button, 3, 1, 1, 1)

        self.load_template_button = QPushButton(Dialog)
        self.load_template_button.setObjectName(u"load_template_button")

        self.gridLayout.addWidget(self.load_template_button, 2, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.assign_one_group_to_all = QPushButton(Dialog)
        self.assign_one_group_to_all.setObjectName(u"assign_one_group_to_all")
        self.assign_one_group_to_all.setEnabled(True)

        self.gridLayout.addWidget(self.assign_one_group_to_all, 3, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.select_from_database_button.setText(QCoreApplication.translate("Dialog", u"Select From Database", None))
        self.assign_now_button.setText(QCoreApplication.translate("Dialog", u"Assign Now", None))
        self.load_template_button.setText(QCoreApplication.translate("Dialog", u"Load From Template", None))
        self.assign_one_group_to_all.setText(QCoreApplication.translate("Dialog", u"Assign Later", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select an option to assign metadata groups to thte experiments !", None))
    # retranslateUi

