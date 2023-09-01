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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QScrollArea, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

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

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1108, 549))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
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
        if (self.statistics_table_widget.columnCount() < 7):
            self.statistics_table_widget.setColumnCount(7)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.statistics_table_widget.setObjectName(u"statistics_table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statistics_table_widget.sizePolicy().hasHeightForWidth())
        self.statistics_table_widget.setSizePolicy(sizePolicy1)
        self.statistics_table_widget.horizontalHeader().setVisible(True)
        self.statistics_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.statistics_table_widget.horizontalHeader().setDefaultSectionSize(30)
        self.statistics_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.statistics_table_widget.horizontalHeader().setStretchLastSection(False)
        self.statistics_table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.statistics_table_widget)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.statistics_result_grid = QVBoxLayout()
        self.statistics_result_grid.setObjectName(u"statistics_result_grid")

        self.gridLayout_3.addLayout(self.statistics_result_grid, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.tab_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(StatisticsTable)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StatisticsTable)
    # setupUi

    def retranslateUi(self, StatisticsTable):
        StatisticsTable.setWindowTitle(QCoreApplication.translate("StatisticsTable", u"Form", None))
        self.label.setText(QCoreApplication.translate("StatisticsTable", u"WELCOME TO THE STATISTICS FEATURE", None))
        self.label_2.setText(QCoreApplication.translate("StatisticsTable", u" We have scanned your analysis functions and meta data selection and entered the data in the table below. \n"
" We have also analyzed the data distribution by running the Shapiro Wilk test and suggest you the test selected in the combo box. \n"
" Select the checkbox for each analysis function that you want to analyze statistically. \n"
"", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatisticsTable", u"Analysis Function Selection", None))
        ___qtablewidgetitem = self.statistics_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StatisticsTable", u"Select", None));
        ___qtablewidgetitem1 = self.statistics_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StatisticsTable", u"Analysis Function", None));
        ___qtablewidgetitem2 = self.statistics_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StatisticsTable", u"Meta Data Selection", None));
        ___qtablewidgetitem3 = self.statistics_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StatisticsTable", u"Data Dependency", None));
        ___qtablewidgetitem4 = self.statistics_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StatisticsTable", u"Data Distribution", None));
        ___qtablewidgetitem5 = self.statistics_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("StatisticsTable", u"Variance", None));
        ___qtablewidgetitem6 = self.statistics_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("StatisticsTable", u"Statistical Model", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StatisticsTable", u"Basic Tests", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StatisticsTable", u"Results", None))
        self.label_4.setText(QCoreApplication.translate("StatisticsTable", u"Select the model type first", None))
        self.label_3.setText(QCoreApplication.translate("StatisticsTable", u"Welcome to the modelling feature. Here you can select more complex models to evaluate your recording results", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("StatisticsTable", u"Generalized Linear Mixed Model (GLM)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("StatisticsTable", u"Generalized Mixed Efects Model", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("StatisticsTable", u"Modelling", None))
    # retranslateUi

