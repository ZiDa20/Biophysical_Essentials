# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_offline_result.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_OfflineTabWidget(object):
    def setupUi(self, OfflineTabWidget):
        if not OfflineTabWidget.objectName():
            OfflineTabWidget.setObjectName(u"OfflineTabWidget")
        OfflineTabWidget.resize(1159, 814)
        self.gridLayout = QGridLayout(OfflineTabWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.OfflineTabGrid = QGridLayout()
        self.OfflineTabGrid.setObjectName(u"OfflineTabGrid")
        self.OfflineScroll = QScrollArea(OfflineTabWidget)
        self.OfflineScroll.setObjectName(u"OfflineScroll")
        self.OfflineScroll.setWidgetResizable(True)
        self.OfflineResultWidget = QWidget()
        self.OfflineResultWidget.setObjectName(u"OfflineResultWidget")
        self.OfflineResultWidget.setGeometry(QRect(0, 0, 1137, 792))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OfflineResultWidget.sizePolicy().hasHeightForWidth())
        self.OfflineResultWidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.OfflineResultWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.OfflineResultGrid = QGridLayout()
        self.OfflineResultGrid.setObjectName(u"OfflineResultGrid")

        self.gridLayout_2.addLayout(self.OfflineResultGrid, 0, 1, 1, 1)

        self.OfflineScroll.setWidget(self.OfflineResultWidget)

        self.OfflineTabGrid.addWidget(self.OfflineScroll, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.OfflineTabGrid, 0, 0, 1, 1)


        self.retranslateUi(OfflineTabWidget)

        QMetaObject.connectSlotsByName(OfflineTabWidget)
    # setupUi

    def retranslateUi(self, OfflineTabWidget):
        OfflineTabWidget.setWindowTitle(QCoreApplication.translate("OfflineTabWidget", u"Form", None))
    # retranslateUi



class OfflineResultTab(QWidget, Ui_OfflineTabWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)