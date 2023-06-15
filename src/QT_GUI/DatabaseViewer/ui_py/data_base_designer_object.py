# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_base_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Database_Viewer(object):
    def setupUi(self, Database_Viewer):
        if not Database_Viewer.objectName():
            Database_Viewer.setObjectName(u"Database_Viewer")
        Database_Viewer.resize(1313, 968)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Database_Viewer.sizePolicy().hasHeightForWidth())
        Database_Viewer.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Database_Viewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(-1)
        self.gridLayout_2.setContentsMargins(1, 6, 1, 3)
        self.widget = QWidget(Database_Viewer)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 120))
        self.widget.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_19 = QGridLayout(self.groupBox_4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(2, 2, 2, 2)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.HomeButton = QPushButton(self.groupBox_4)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setMaximumSize(QSize(40, 40))

        self.gridLayout.addWidget(self.HomeButton, 0, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.gridLayout_18 = QGridLayout(self.groupBox_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setHorizontalSpacing(-1)
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setContentsMargins(2, 6, 2, 6)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(-1)
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)

        self.gridLayout_11.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignRight)

        self.export_table = QPushButton(self.groupBox_5)
        self.export_table.setObjectName(u"export_table")
        self.export_table.setMinimumSize(QSize(30, 30))
        self.export_table.setMaximumSize(QSize(30, 30))
        self.export_table.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.export_table, 0, 5, 1, 1, Qt.AlignLeft)

        self.select_columns = QPushButton(self.groupBox_5)
        self.select_columns.setObjectName(u"select_columns")
        self.select_columns.setMinimumSize(QSize(30, 30))
        self.select_columns.setMaximumSize(QSize(30, 30))
        self.select_columns.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.select_columns, 0, 3, 1, 1, Qt.AlignLeft)

        self.ImportDB = QPushButton(self.groupBox_5)
        self.ImportDB.setObjectName(u"ImportDB")
        self.ImportDB.setMinimumSize(QSize(30, 30))
        self.ImportDB.setMaximumSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.ImportDB, 0, 1, 1, 1, Qt.AlignLeft)

        self.ParquetExport = QPushButton(self.groupBox_5)
        self.ParquetExport.setObjectName(u"ParquetExport")
        self.ParquetExport.setMinimumSize(QSize(30, 30))
        self.ParquetExport.setMaximumSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.ParquetExport, 0, 7, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_11.addWidget(self.label_7, 0, 4, 1, 1, Qt.AlignRight)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignRight)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_11.addWidget(self.label_8, 0, 6, 1, 1, Qt.AlignRight)


        self.gridLayout_18.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.widget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_14 = QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(2, 6, 2, 6)
        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_14.addWidget(self.label_4, 0, 0, 1, 1)

        self.query_line_edit = QLineEdit(self.groupBox_6)
        self.query_line_edit.setObjectName(u"query_line_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.query_line_edit.sizePolicy().hasHeightForWidth())
        self.query_line_edit.setSizePolicy(sizePolicy2)
        self.query_line_edit.setMinimumSize(QSize(0, 0))
        self.query_line_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_14.addWidget(self.query_line_edit, 0, 1, 1, 1)

        self.query_execute = QPushButton(self.groupBox_6)
        self.query_execute.setObjectName(u"query_execute")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.query_execute.sizePolicy().hasHeightForWidth())
        self.query_execute.setSizePolicy(sizePolicy3)
        self.query_execute.setMinimumSize(QSize(30, 30))
        self.query_execute.setMaximumSize(QSize(30, 30))
        self.query_execute.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.query_execute, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_17 = QGridLayout(self.groupBox_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_17.addWidget(self.label_5, 0, 0, 1, 1)

        self.complex_query = QPushButton(self.groupBox_2)
        self.complex_query.setObjectName(u"complex_query")
        self.complex_query.setMinimumSize(QSize(30, 30))
        self.complex_query.setMaximumSize(QSize(30, 30))
        self.complex_query.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.complex_query, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(2, 6, 2, 6)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.SQL = QPushButton(self.groupBox)
        self.SQL.setObjectName(u"SQL")
        self.SQL.setMinimumSize(QSize(30, 30))
        self.SQL.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.SQL, 0, 1, 1, 1)

        self.AWS = QPushButton(self.groupBox)
        self.AWS.setObjectName(u"AWS")
        self.AWS.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.AWS, 0, 3, 1, 1)

        self.NWB = QPushButton(self.groupBox)
        self.NWB.setObjectName(u"NWB")
        self.NWB.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.NWB, 0, 5, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_9.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_9.addWidget(self.label_11, 0, 4, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(12, -1, 12, -1)

        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.retranslateUi(Database_Viewer)

        QMetaObject.connectSlotsByName(Database_Viewer)
    # setupUi

    def retranslateUi(self, Database_Viewer):
        Database_Viewer.setWindowTitle(QCoreApplication.translate("Database_Viewer", u"Form", None))
#if QT_CONFIG(accessibility)
        self.groupBox_4.setAccessibleName(QCoreApplication.translate("Database_Viewer", u"ribbon_bar", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_4.setTitle(QCoreApplication.translate("Database_Viewer", u"Home", None))
        self.HomeButton.setText("")
#if QT_CONFIG(accessibility)
        self.groupBox_5.setAccessibleName(QCoreApplication.translate("Database_Viewer", u"ribbon_bar", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_5.setTitle(QCoreApplication.translate("Database_Viewer", u"Import/Export", None))
        self.label_3.setText(QCoreApplication.translate("Database_Viewer", u"Export Analysis", None))
        self.export_table.setText("")
        self.select_columns.setText("")
        self.ImportDB.setText("")
        self.ParquetExport.setText("")
        self.label_7.setText(QCoreApplication.translate("Database_Viewer", u"Export CSV", None))
        self.label_6.setText(QCoreApplication.translate("Database_Viewer", u"Import Database", None))
        self.label_8.setText(QCoreApplication.translate("Database_Viewer", u"Export Parquet", None))
#if QT_CONFIG(accessibility)
        self.groupBox_6.setAccessibleName(QCoreApplication.translate("Database_Viewer", u"ribbon_bar", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_6.setTitle(QCoreApplication.translate("Database_Viewer", u"Query Database", None))
        self.label_4.setText(QCoreApplication.translate("Database_Viewer", u"Query Table:", None))
        self.query_execute.setText("")
#if QT_CONFIG(accessibility)
        self.groupBox_2.setAccessibleName(QCoreApplication.translate("Database_Viewer", u"ribbon_bar", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("Database_Viewer", u"Complex Query", None))
        self.label_5.setText(QCoreApplication.translate("Database_Viewer", u"Open Comlex Query:", None))
        self.complex_query.setText("")
#if QT_CONFIG(accessibility)
        self.groupBox.setAccessibleName(QCoreApplication.translate("Database_Viewer", u"ribbon_bar", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle(QCoreApplication.translate("Database_Viewer", u"Share Database Online", None))
        self.label_9.setText(QCoreApplication.translate("Database_Viewer", u"Export Database", None))
        self.SQL.setText("")
        self.AWS.setText("")
        self.NWB.setText(QCoreApplication.translate("Database_Viewer", u"NWB", None))
        self.label_10.setText(QCoreApplication.translate("Database_Viewer", u"BPE Online", None))
        self.label_11.setText(QCoreApplication.translate("Database_Viewer", u"NWB Export", None))
    # retranslateUi

