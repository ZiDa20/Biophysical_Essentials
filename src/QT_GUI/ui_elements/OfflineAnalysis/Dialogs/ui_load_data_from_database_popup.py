# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_data_from_database_popup.ui'
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
        Dialog.resize(991, 786)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 941, 721))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.load_data = QPushButton(self.gridLayoutWidget)
        self.load_data.setObjectName(u"load_data")

        self.gridLayout.addWidget(self.load_data, 2, 0, 1, 4)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.groupBox_3 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.meta_data_list = QListWidget(self.groupBox_3)
        self.meta_data_list.setObjectName(u"meta_data_list")

        self.gridLayout_4.addWidget(self.meta_data_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 3, 1, 1)

        self.selected_labels = QGroupBox(self.gridLayoutWidget)
        self.selected_labels.setObjectName(u"selected_labels")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selected_labels.sizePolicy().hasHeightForWidth())
        self.selected_labels.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.selected_labels, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.available_labels = QGroupBox(self.gridLayoutWidget)
        self.available_labels.setObjectName(u"available_labels")
        sizePolicy.setHeightForWidth(self.available_labels.sizePolicy().hasHeightForWidth())
        self.available_labels.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.available_labels)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.available_labels_list = QListWidget(self.available_labels)
        self.available_labels_list.setObjectName(u"available_labels_list")
        self.available_labels_list.setDragEnabled(True)
        self.available_labels_list.setDragDropMode(QAbstractItemView.DragDrop)

        self.gridLayout_2.addWidget(self.available_labels_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.available_labels, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.load_data.setText(QCoreApplication.translate("Dialog", u"Load Selection", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Drag and Drop available Experiment Labels(s) label selection to load recordings from the database", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Meta Data Selection", None))
        self.selected_labels.setTitle(QCoreApplication.translate("Dialog", u"Label Selection", None))
        self.available_labels.setTitle(QCoreApplication.translate("Dialog", u"Available Label", None))
    # retranslateUi

