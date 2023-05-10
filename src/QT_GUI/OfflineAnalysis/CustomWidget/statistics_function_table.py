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
    QLabel, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StatisticsTable(object):
    def setupUi(self, StatisticsTable):
        if not StatisticsTable.objectName():
            StatisticsTable.setObjectName(u"StatisticsTable")
        StatisticsTable.resize(1152, 711)
        self.gridLayout = QGridLayout(StatisticsTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(StatisticsTable)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab)
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


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(StatisticsTable)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StatisticsTable)
    # setupUi

    def retranslateUi(self, StatisticsTable):
        StatisticsTable.setWindowTitle(QCoreApplication.translate("StatisticsTable", u"Form", None))
        self.label.setText(QCoreApplication.translate("StatisticsTable", u"WELCOME TO THE STATISTICS FEATURE", None))
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
        self.label_2.setText(QCoreApplication.translate("StatisticsTable", u" We have scanned your analysis functions and meta data selection and entered the data in the table below. \n"
" We have also analyzed the data distribution by running the Shapiro Wilk test and suggest you the test selected in the combo box. \n"
" Select the checkbox for each analysis function that you want to analyze statistically. \n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StatisticsTable", u"Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StatisticsTable", u"Tab 2", None))
    # retranslateUi

class StatisticsTablePromoted(QWidget, Ui_StatisticsTable):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)