# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListViewTables.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QWidget)

class Ui_ListViewTables(object):
    def setupUi(self, ListViewTables):
        if not ListViewTables.objectName():
            ListViewTables.setObjectName(u"ListViewTables")
        ListViewTables.resize(576, 694)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListViewTables.sizePolicy().hasHeightForWidth())
        ListViewTables.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ListViewTables)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.available_tables_gb = QGroupBox(ListViewTables)
        self.available_tables_gb.setObjectName(u"available_tables_gb")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.available_tables_gb.sizePolicy().hasHeightForWidth())
        self.available_tables_gb.setSizePolicy(sizePolicy1)
        self.available_tables_gb.setMinimumSize(QSize(0, 0))
        self.available_tables_gb.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.available_tables_gb.setFont(font)
        self.gridLayout_7 = QGridLayout(self.available_tables_gb)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.lineEdit = QLineEdit(self.available_tables_gb)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_21.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.SearchTable = QPushButton(self.available_tables_gb)
        self.SearchTable.setObjectName(u"SearchTable")
        self.SearchTable.setMinimumSize(QSize(30, 30))
        self.SearchTable.setMaximumSize(QSize(30, 30))

        self.gridLayout_21.addWidget(self.SearchTable, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_21, 2, 0, 1, 1)

        self.line_2 = QFrame(self.available_tables_gb)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 0, 0, 1, 1)

        self.label_2 = QLabel(self.available_tables_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)

        self.line = QFrame(self.available_tables_gb)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line, 3, 0, 1, 1)

        self.scrollArea = QScrollArea(self.available_tables_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 558, 488))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.database_table = QListWidget(self.scrollAreaWidgetContents)
        self.database_table.setObjectName(u"database_table")

        self.gridLayout_6.addWidget(self.database_table, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 8, 0, 1, 1)

        self.label = QLabel(self.available_tables_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 4, 0, 1, 1)

        self.select_table = QComboBox(self.available_tables_gb)
        self.select_table.setObjectName(u"select_table")

        self.gridLayout_7.addWidget(self.select_table, 6, 0, 1, 1)

        self.line_3 = QFrame(self.available_tables_gb)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_3, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.available_tables_gb, 0, 0, 1, 1)


        self.retranslateUi(ListViewTables)

        QMetaObject.connectSlotsByName(ListViewTables)
    # setupUi

    def retranslateUi(self, ListViewTables):
        ListViewTables.setWindowTitle(QCoreApplication.translate("ListViewTables", u"Form", None))
#if QT_CONFIG(accessibility)
        self.available_tables_gb.setAccessibleName(QCoreApplication.translate("ListViewTables", u"new_color", None))
#endif // QT_CONFIG(accessibility)
        self.available_tables_gb.setTitle(QCoreApplication.translate("ListViewTables", u"Select Database Table", None))
        self.SearchTable.setText("")
#if QT_CONFIG(accessibility)
        self.line_2.setAccessibleName(QCoreApplication.translate("ListViewTables", u"divider", None))
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("ListViewTables", u"Search for Table", None))
#if QT_CONFIG(accessibility)
        self.line.setAccessibleName(QCoreApplication.translate("ListViewTables", u"divider", None))
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("ListViewTables", u"Select Table of Interest:", None))
#if QT_CONFIG(accessibility)
        self.select_table.setAccessibleName(QCoreApplication.translate("ListViewTables", u"qcombo", None))
#endif // QT_CONFIG(accessibility)
    # retranslateUi

