# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_function_table.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AnalysisFunction(object):
    def setupUi(self, AnalysisFunction):
        if not AnalysisFunction.objectName():
            AnalysisFunction.setObjectName(u"AnalysisFunction")
        AnalysisFunction.resize(1274, 496)
        self.gridLayout_3 = QGridLayout(AnalysisFunction)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(AnalysisFunction)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.AnalysisPage = QWidget()
        self.AnalysisPage.setObjectName(u"AnalysisPage")
        self.gridLayout = QGridLayout(self.AnalysisPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.AnalysisPage)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 500))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.analysis_table_widget = QTableWidget(self.groupBox)
        if (self.analysis_table_widget.columnCount() < 5):
            self.analysis_table_widget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.analysis_table_widget.setObjectName(u"analysis_table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.analysis_table_widget.sizePolicy().hasHeightForWidth())
        self.analysis_table_widget.setSizePolicy(sizePolicy1)
        self.analysis_table_widget.horizontalHeader().setVisible(True)
        self.analysis_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.analysis_table_widget.horizontalHeader().setDefaultSectionSize(125)
        self.analysis_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.analysis_table_widget.horizontalHeader().setStretchLastSection(False)
        self.analysis_table_widget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.analysis_table_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.AnalysisPage)
        self.FilterFunction = QWidget()
        self.FilterFunction.setObjectName(u"FilterFunction")
        self.gridLayout_4 = QGridLayout(self.FilterFunction)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.FilterFunction)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.FilterFunction)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.retranslateUi(AnalysisFunction)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AnalysisFunction)
    # setupUi

    def retranslateUi(self, AnalysisFunction):
        AnalysisFunction.setWindowTitle(QCoreApplication.translate("AnalysisFunction", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AnalysisFunction", u"Analysis Function", None))
        ___qtablewidgetitem = self.analysis_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AnalysisFunction", u"Analysis Functions", None));
        ___qtablewidgetitem1 = self.analysis_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AnalysisFunction", u"Left Boundary", None));
        ___qtablewidgetitem2 = self.analysis_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AnalysisFunction", u"Right Boundary", None));
        ___qtablewidgetitem3 = self.analysis_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AnalysisFunction", u"Configuration", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("AnalysisFunction", u"Filter Function", None))
    # retranslateUi




class AnalysisFunctionTable(QWidget, Ui_AnalysisFunction):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)