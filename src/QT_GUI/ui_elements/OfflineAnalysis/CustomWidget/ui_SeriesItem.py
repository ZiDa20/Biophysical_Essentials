# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SeriesItem.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_OfflineTree(object):
    def setupUi(self, OfflineTree):
        if not OfflineTree.objectName():
            OfflineTree.setObjectName(u"OfflineTree")
        OfflineTree.resize(291, 623)
        self.gridLayout = QGridLayout(OfflineTree)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TreeLayout1 = QGridLayout()
        self.TreeLayout1.setObjectName(u"TreeLayout1")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(OfflineTree)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label = QLabel(OfflineTree)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.TreeLayout1.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.SeriesItems = QTreeWidget(OfflineTree)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.SeriesItems.setHeaderItem(__qtreewidgetitem)
        self.SeriesItems.setObjectName(u"SeriesItems")

        self.TreeLayout1.addWidget(self.SeriesItems, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.TreeLayout1, 0, 0, 1, 1)


        self.retranslateUi(OfflineTree)

        QMetaObject.connectSlotsByName(OfflineTree)
    # setupUi

    def retranslateUi(self, OfflineTree):
        OfflineTree.setWindowTitle(QCoreApplication.translate("OfflineTree", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("OfflineTree", u"Discard Series", None))
        self.label.setText(QCoreApplication.translate("OfflineTree", u"Analysis Tree:", None))
    # retranslateUi

