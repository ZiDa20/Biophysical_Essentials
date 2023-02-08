# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analysis_function_table.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AnalysisFunction(object):
    def setupUi(self, AnalysisFunction):
        if not AnalysisFunction.objectName():
            AnalysisFunction.setObjectName(u"AnalysisFunction")
        AnalysisFunction.resize(779, 356)
        self.gridLayout = QGridLayout(AnalysisFunction)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(AnalysisFunction)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 500))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.analysis_table_widget = QTableWidget(self.groupBox)
        if (self.analysis_table_widget.rowCount() < 7):
            self.analysis_table_widget.setRowCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.analysis_table_widget.setVerticalHeaderItem(6, __qtablewidgetitem6)
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

        self.verticalLayout_2.addWidget(self.analysis_table_widget)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(AnalysisFunction)

        QMetaObject.connectSlotsByName(AnalysisFunction)
    # setupUi

    def retranslateUi(self, AnalysisFunction):
        AnalysisFunction.setWindowTitle(QCoreApplication.translate("AnalysisFunction", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("AnalysisFunction", u"Analysis Function Selection", None))
        ___qtablewidgetitem = self.analysis_table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AnalysisFunction", u"Color", None));
        ___qtablewidgetitem1 = self.analysis_table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AnalysisFunction", u"Type", None));
        ___qtablewidgetitem2 = self.analysis_table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AnalysisFunction", u"Function", None));
        ___qtablewidgetitem3 = self.analysis_table_widget.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AnalysisFunction", u"Left Cursor", None));
        ___qtablewidgetitem4 = self.analysis_table_widget.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AnalysisFunction", u"Right Cursor", None));
        ___qtablewidgetitem5 = self.analysis_table_widget.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AnalysisFunction", u"PGF Seg", None));
        ___qtablewidgetitem6 = self.analysis_table_widget.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AnalysisFunction", u"Live", None));
    # retranslateUi

