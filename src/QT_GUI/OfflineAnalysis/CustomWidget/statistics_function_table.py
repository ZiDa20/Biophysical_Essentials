# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_function_table.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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

class Ui_StatisticsTable(object):
    def setupUi(self, StatisticsTable):
        if not StatisticsTable.objectName():
            StatisticsTable.setObjectName(u"StatisticsTable")
        StatisticsTable.resize(779, 356)
        self.gridLayout = QGridLayout(StatisticsTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(StatisticsTable)
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
        self.statistics_table_widget = QTableWidget(self.groupBox)
        if (self.statistics_table_widget.columnCount() < 5):
            self.statistics_table_widget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.statistics_table_widget.setObjectName(u"statistics_table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statistics_table_widget.sizePolicy().hasHeightForWidth())
        self.statistics_table_widget.setSizePolicy(sizePolicy1)
        self.statistics_table_widget.horizontalHeader().setVisible(True)
        self.statistics_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.statistics_table_widget.horizontalHeader().setDefaultSectionSize(125)
        self.statistics_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.statistics_table_widget.horizontalHeader().setStretchLastSection(False)
        self.statistics_table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.statistics_table_widget)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(StatisticsTable)

        QMetaObject.connectSlotsByName(StatisticsTable)
    # setupUi

    def retranslateUi(self, StatisticsTable):
        StatisticsTable.setWindowTitle(QCoreApplication.translate("StatisticsTable", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatisticsTable", u"Analysis Function Selection", None))
        ___qtablewidgetitem = self.statistics_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StatisticsTable", u"Select", None));
        ___qtablewidgetitem1 = self.statistics_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StatisticsTable", u"Analysis Function", None));
        ___qtablewidgetitem2 = self.statistics_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StatisticsTable", u"Meta Data Selection", None));
        ___qtablewidgetitem3 = self.statistics_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StatisticsTable", u"Data Distribution", None));
        ___qtablewidgetitem4 = self.statistics_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StatisticsTable", u"Statistical Model", None));
    # retranslateUi

class StatisticsTablePromoted(QWidget, Ui_StatisticsTable):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)