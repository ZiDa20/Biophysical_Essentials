# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_meta_data_group.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_assign_meta_data_group(object):
    def setupUi(self, assign_meta_data_group):
        if not assign_meta_data_group.objectName():
            assign_meta_data_group.setObjectName(u"assign_meta_data_group")
        assign_meta_data_group.resize(1550, 525)
        self.gridLayout = QGridLayout(assign_meta_data_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.meta_data_template_layout = QGridLayout()
        self.meta_data_template_layout.setObjectName(u"meta_data_template_layout")

        self.gridLayout.addLayout(self.meta_data_template_layout, 2, 0, 1, 4)

        self.groupBox = QGroupBox(assign_meta_data_group)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)

        self.load_template = QPushButton(assign_meta_data_group)
        self.load_template.setObjectName(u"load_template")

        self.gridLayout.addWidget(self.load_template, 4, 0, 1, 1)

        self.label = QLabel(assign_meta_data_group)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.save_to_template_button = QPushButton(assign_meta_data_group)
        self.save_to_template_button.setObjectName(u"save_to_template_button")

        self.gridLayout.addWidget(self.save_to_template_button, 4, 3, 1, 1)

        self.pushButton_3 = QPushButton(assign_meta_data_group)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 2)

        self.continue_loading = QPushButton(assign_meta_data_group)
        self.continue_loading.setObjectName(u"continue_loading")

        self.gridLayout.addWidget(self.continue_loading, 4, 1, 1, 2)


        self.retranslateUi(assign_meta_data_group)

        QMetaObject.connectSlotsByName(assign_meta_data_group)
    # setupUi

    def retranslateUi(self, assign_meta_data_group):
        assign_meta_data_group.setWindowTitle(QCoreApplication.translate("assign_meta_data_group", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("assign_meta_data_group", u"Multiple Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("assign_meta_data_group", u"Set For All", None))
        self.label_2.setText(QCoreApplication.translate("assign_meta_data_group", u"Select the column from the dropdown menu to change a value for all experiments. ", None))
        self.load_template.setText(QCoreApplication.translate("assign_meta_data_group", u"Load Template", None))
        self.label.setText(QCoreApplication.translate("assign_meta_data_group", u"Assign meta data annotation to each experiment !", None))
        self.save_to_template_button.setText(QCoreApplication.translate("assign_meta_data_group", u"Save to Template and Conitnue", None))
        self.pushButton_3.setText(QCoreApplication.translate("assign_meta_data_group", u"Reset All Meta Data", None))
        self.continue_loading.setText(QCoreApplication.translate("assign_meta_data_group", u"Select Meta Data As Shown and Continue", None))
    # retranslateUi

