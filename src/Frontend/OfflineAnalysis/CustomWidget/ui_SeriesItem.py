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

class Ui_OfflineTree(QWidget):
    def setupUi(self, OfflineTree):
        if not OfflineTree.objectName():
            OfflineTree.setObjectName(u"OfflineTree")
        OfflineTree.resize(291, 623)
        self.gridLayout = QGridLayout(OfflineTree)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.TreeLayout1 = QGridLayout()
        self.TreeLayout1.setObjectName(u"TreeLayout1")
        self.SeriesItems = QTreeWidget(OfflineTree)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.SeriesItems.setHeaderItem(__qtreewidgetitem)
        self.SeriesItems.setObjectName(u"SeriesItems")
        self.SeriesItems.setFrameShape(QFrame.NoFrame)
        self.SeriesItems.setFrameShadow(QFrame.Plain)
        self.SeriesItems.setLineWidth(0)

        self.TreeLayout1.addWidget(self.SeriesItems, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.TreeLayout1, 0, 0, 1, 1)


        self.retranslateUi(OfflineTree)

        QMetaObject.connectSlotsByName(OfflineTree)
    # setupUi

    def retranslateUi(self, OfflineTree):
        OfflineTree.setWindowTitle(QCoreApplication.translate("OfflineTree", u"Form", None))
    # retranslateUi
class OfflineTree(Ui_OfflineTree):
    def __init__(self,parent = None):
        self.parent = parent
        QWidget.__init__(self,parent)
        self.setupUi(self)