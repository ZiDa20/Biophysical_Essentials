# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TreeItemOffline.ui'
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
        Form.resize(1584, 895)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SeriesItems = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.SeriesItems.setHeaderItem(__qtreewidgetitem)
        self.SeriesItems.setObjectName(u"SeriesItems")
        self.SeriesItems.setMinimumSize(QSize(0, 0))
        self.SeriesItems.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.SeriesItems, 0, 0, 1, 1)

        self.PlotItem = QWidget(Form)
        self.PlotItem.setObjectName(u"PlotItem")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotItem.sizePolicy().hasHeightForWidth())
        self.PlotItem.setSizePolicy(sizePolicy)
        self.PlotItem.setMinimumSize(QSize(700, 500))

        self.gridLayout_2.addWidget(self.PlotItem, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BackButtonGrid = QHBoxLayout()
        self.BackButtonGrid.setObjectName(u"BackButtonGrid")
        self.series_selection = QPushButton(Form)
        self.series_selection.setObjectName(u"series_selection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.series_selection.sizePolicy().hasHeightForWidth())
        self.series_selection.setSizePolicy(sizePolicy1)
        self.series_selection.setMinimumSize(QSize(100, 0))

        self.BackButtonGrid.addWidget(self.series_selection)

        self.new_analysis = QPushButton(Form)
        self.new_analysis.setObjectName(u"new_analysis")
        sizePolicy1.setHeightForWidth(self.new_analysis.sizePolicy().hasHeightForWidth())
        self.new_analysis.setSizePolicy(sizePolicy1)
        self.new_analysis.setMinimumSize(QSize(100, 0))

        self.BackButtonGrid.addWidget(self.new_analysis)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonGrid.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.BackButtonGrid, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.series_selection.setText(QCoreApplication.translate("Form", u"Series Selection", None))
        self.new_analysis.setText(QCoreApplication.translate("Form", u"New Analysis", None))
    # retranslateUi

