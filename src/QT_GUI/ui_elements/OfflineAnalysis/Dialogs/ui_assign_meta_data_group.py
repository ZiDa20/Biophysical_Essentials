# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_meta_data_group.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_assign_meta_data_group(object):
    def setupUi(self, assign_meta_data_group):
        if not assign_meta_data_group.objectName():
            assign_meta_data_group.setObjectName(u"assign_meta_data_group")
        assign_meta_data_group.resize(928, 525)
        self.gridLayout = QGridLayout(assign_meta_data_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.close_and_continue_button = QPushButton(assign_meta_data_group)
        self.close_and_continue_button.setObjectName(u"close_and_continue_button")

        self.gridLayout.addWidget(self.close_and_continue_button, 5, 3, 1, 1)

        self.save_to_template_button = QPushButton(assign_meta_data_group)
        self.save_to_template_button.setObjectName(u"save_to_template_button")

        self.gridLayout.addWidget(self.save_to_template_button, 5, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.meta_data_template_layout = QGridLayout()
        self.meta_data_template_layout.setObjectName(u"meta_data_template_layout")

        self.gridLayout.addLayout(self.meta_data_template_layout, 2, 1, 3, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.label = QLabel(assign_meta_data_group)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 4)


        self.retranslateUi(assign_meta_data_group)

        QMetaObject.connectSlotsByName(assign_meta_data_group)
    # setupUi

    def retranslateUi(self, assign_meta_data_group):
        assign_meta_data_group.setWindowTitle(QCoreApplication.translate("assign_meta_data_group", u"Form", None))
        self.close_and_continue_button.setText(QCoreApplication.translate("assign_meta_data_group", u"Close and Continue", None))
        self.save_to_template_button.setText(QCoreApplication.translate("assign_meta_data_group", u"Save to Template", None))
        self.label.setText(QCoreApplication.translate("assign_meta_data_group", u"Assign meta data annotation to each experiment !", None))
    # retranslateUi
