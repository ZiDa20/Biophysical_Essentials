# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_pop_up.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_FilterSettings(object):
    def setupUi(self, FilterSettings):
        if not FilterSettings.objectName():
            FilterSettings.setObjectName(u"FilterSettings")
        FilterSettings.resize(857, 864)
        self.gridLayout = QGridLayout(FilterSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.groupBox_2 = QGroupBox(FilterSettings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.conditional_filter_combo_box = QComboBox(self.groupBox_2)
        self.conditional_filter_combo_box.setObjectName(u"conditional_filter_combo_box")

        self.gridLayout_3.addWidget(self.conditional_filter_combo_box, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 6, 1, 3, 4)

        self.label = QLabel(FilterSettings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 9, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(165, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.groupBox = QGroupBox(FilterSettings)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.meta_data_combo_box = QComboBox(self.groupBox)
        self.meta_data_combo_box.setObjectName(u"meta_data_combo_box")

        self.gridLayout_2.addWidget(self.meta_data_combo_box, 0, 0, 1, 1)

        self.upper_value_line_edit = QLineEdit(self.groupBox)
        self.upper_value_line_edit.setObjectName(u"upper_value_line_edit")

        self.gridLayout_2.addWidget(self.upper_value_line_edit, 2, 3, 1, 1)

        self.horizontalSlider = QSlider(self.groupBox)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 3)

        self.add_filter_button = QPushButton(self.groupBox)
        self.add_filter_button.setObjectName(u"add_filter_button")

        self.gridLayout_2.addWidget(self.add_filter_button, 2, 4, 1, 1)

        self.lower_value_line_edit = QLineEdit(self.groupBox)
        self.lower_value_line_edit.setObjectName(u"lower_value_line_edit")

        self.gridLayout_2.addWidget(self.lower_value_line_edit, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 1, 3, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(FilterSettings)

        QMetaObject.connectSlotsByName(FilterSettings)
    # setupUi

    def retranslateUi(self, FilterSettings):
        FilterSettings.setWindowTitle(QCoreApplication.translate("FilterSettings", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FilterSettings", u"Conditional Filter", None))
        self.pushButton_2.setText(QCoreApplication.translate("FilterSettings", u"Add", None))
        self.label.setText(QCoreApplication.translate("FilterSettings", u"Select filter and other conditional options !", None))
        self.groupBox.setTitle(QCoreApplication.translate("FilterSettings", u"Add Meta Data Filter", None))
        self.add_filter_button.setText(QCoreApplication.translate("FilterSettings", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("FilterSettings", u"Lower Value:", None))
        self.label_3.setText(QCoreApplication.translate("FilterSettings", u"Upper Value:", None))
    # retranslateUi

