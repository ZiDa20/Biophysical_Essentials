# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_base_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

class Ui_Database_Viewer(object):
    def setupUi(self, Database_Viewer):
        if not Database_Viewer.objectName():
            Database_Viewer.setObjectName(u"Database_Viewer")
        Database_Viewer.resize(1234, 822)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Database_Viewer.sizePolicy().hasHeightForWidth())
        Database_Viewer.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Database_Viewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 12, 1, 3)
        self.data_base_stacked_widget = QStackedWidget(Database_Viewer)
        self.data_base_stacked_widget.setObjectName(u"data_base_stacked_widget")
        self.data_base = QWidget()
        self.data_base.setObjectName(u"data_base")
        self.gridLayout_4 = QGridLayout(self.data_base)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.available_tables_gb = QGroupBox(self.data_base)
        self.available_tables_gb.setObjectName(u"available_tables_gb")
        self.available_tables_gb.setMinimumSize(QSize(300, 0))
        self.available_tables_gb.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.available_tables_gb.setFont(font)
        self.gridLayout_7 = QGridLayout(self.available_tables_gb)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea = QScrollArea(self.available_tables_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 543))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.database_table = QListWidget(self.scrollAreaWidgetContents)
        self.database_table.setObjectName(u"database_table")

        self.gridLayout_6.addWidget(self.database_table, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.label = QLabel(self.available_tables_gb)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)

        self.select_table = QComboBox(self.available_tables_gb)
        self.select_table.setObjectName(u"select_table")

        self.gridLayout_7.addWidget(self.select_table, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.available_tables_gb, 0, 2, 1, 1)

        self.query_gb = QGroupBox(self.data_base)
        self.query_gb.setObjectName(u"query_gb")
        sizePolicy.setHeightForWidth(self.query_gb.sizePolicy().hasHeightForWidth())
        self.query_gb.setSizePolicy(sizePolicy)
        self.query_gb.setMinimumSize(QSize(500, 0))
        self.query_gb.setMaximumSize(QSize(16777215, 16777215))
        self.query_gb.setFont(font)
        self.query_gb.setStyleSheet(u"QPushButton{\n"
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
        self.gridLayout_5 = QGridLayout(self.query_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 0, -1)
        self.groupBox_3 = QGroupBox(self.query_gb)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(450, 0))
        self.gridLayout_12 = QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")

        self.gridLayout_12.addLayout(self.table_layout, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_5.addLayout(self.gridLayout_10, 2, 0, 1, 1)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.lineEdit = QLineEdit(self.query_gb)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_20.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_2 = QLabel(self.query_gb)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_20.addWidget(self.label_2, 0, 0, 1, 1)

        self.SearchTable = QPushButton(self.query_gb)
        self.SearchTable.setObjectName(u"SearchTable")
        self.SearchTable.setMinimumSize(QSize(30, 30))
        self.SearchTable.setMaximumSize(QSize(30, 30))

        self.gridLayout_20.addWidget(self.SearchTable, 0, 2, 1, 1)

        self.query_execute = QPushButton(self.query_gb)
        self.query_execute.setObjectName(u"query_execute")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.query_execute.sizePolicy().hasHeightForWidth())
        self.query_execute.setSizePolicy(sizePolicy2)
        self.query_execute.setMinimumSize(QSize(30, 30))
        self.query_execute.setMaximumSize(QSize(30, 30))
        self.query_execute.setStyleSheet(u"")

        self.gridLayout_20.addWidget(self.query_execute, 1, 2, 1, 1)

        self.query_line_edit = QLineEdit(self.query_gb)
        self.query_line_edit.setObjectName(u"query_line_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.query_line_edit.sizePolicy().hasHeightForWidth())
        self.query_line_edit.setSizePolicy(sizePolicy3)
        self.query_line_edit.setMinimumSize(QSize(0, 0))
        self.query_line_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_20.addWidget(self.query_line_edit, 1, 1, 1, 1, Qt.AlignVCenter)

        self.label_4 = QLabel(self.query_gb)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_20.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_20, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.query_gb, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 2, 1, 1)

        self.data_base_stacked_widget.addWidget(self.data_base)

        self.gridLayout_2.addWidget(self.data_base_stacked_widget, 1, 0, 1, 1)

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
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.DataGroup = QGroupBox(self.widget)
        self.DataGroup.setObjectName(u"DataGroup")
        self.gridLayout_13 = QGridLayout(self.DataGroup)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.open_db = QPushButton(self.DataGroup)
        self.open_db.setObjectName(u"open_db")
        self.open_db.setMinimumSize(QSize(30, 30))
        self.open_db.setMaximumSize(QSize(30, 30))
        self.open_db.setStyleSheet(u"")

        self.DataOptions.addWidget(self.open_db, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.DataGroup)

        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_18 = QGridLayout(self.groupBox_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.export_table = QPushButton(self.groupBox_5)
        self.export_table.setObjectName(u"export_table")
        self.export_table.setMinimumSize(QSize(30, 30))
        self.export_table.setMaximumSize(QSize(30, 30))
        self.export_table.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.export_table, 0, 2, 1, 1)

        self.select_columns = QPushButton(self.groupBox_5)
        self.select_columns.setObjectName(u"select_columns")
        self.select_columns.setMinimumSize(QSize(30, 30))
        self.select_columns.setMaximumSize(QSize(30, 30))
        self.select_columns.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.select_columns, 0, 1, 1, 1)

        self.ImportDB = QPushButton(self.groupBox_5)
        self.ImportDB.setObjectName(u"ImportDB")
        self.ImportDB.setMinimumSize(QSize(30, 30))
        self.ImportDB.setMaximumSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.ImportDB, 0, 0, 1, 1)

        self.ParquetExport = QPushButton(self.groupBox_5)
        self.ParquetExport.setObjectName(u"ParquetExport")
        self.ParquetExport.setMinimumSize(QSize(30, 30))
        self.ParquetExport.setMaximumSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.ParquetExport, 0, 3, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_17 = QGridLayout(self.groupBox_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_17.addWidget(self.label_5, 0, 0, 1, 1)

        self.complex_query = QPushButton(self.groupBox_2)
        self.complex_query.setObjectName(u"complex_query")
        self.complex_query.setMinimumSize(QSize(30, 30))
        self.complex_query.setMaximumSize(QSize(30, 30))
        self.complex_query.setStyleSheet(u"")

        self.gridLayout_17.addWidget(self.complex_query, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.PlotGroup = QGroupBox(self.widget)
        self.PlotGroup.setObjectName(u"PlotGroup")
        self.gridLayout_14 = QGridLayout(self.PlotGroup)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(1, 3, 1, 3)
        self.PlotOptions = QGridLayout()
        self.PlotOptions.setObjectName(u"PlotOptions")
        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(6)
        self.plot_home.setFont(font1)
        self.plot_home.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_home, 0, 0, 1, 1)

        self.save_plot_online = QPushButton(self.PlotGroup)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(30, 30))
        self.save_plot_online.setMaximumSize(QSize(30, 30))
        self.save_plot_online.setFont(font1)
        self.save_plot_online.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.save_plot_online, 0, 3, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(30, 30))
        self.plot_zoom.setMaximumSize(QSize(30, 30))
        self.plot_zoom.setFont(font1)
        self.plot_zoom.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_zoom, 0, 1, 1, 1)

        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(30, 30))
        self.plot_move.setMaximumSize(QSize(30, 30))
        self.plot_move.setFont(font1)
        self.plot_move.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_move, 0, 2, 1, 1)


        self.gridLayout_14.addLayout(self.PlotOptions, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.PlotGroup)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.SQL = QPushButton(self.groupBox)
        self.SQL.setObjectName(u"SQL")
        self.SQL.setMinimumSize(QSize(30, 30))
        self.SQL.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.SQL, 0, 0, 1, 1)

        self.AWS = QPushButton(self.groupBox)
        self.AWS.setObjectName(u"AWS")
        self.AWS.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.AWS, 0, 1, 1, 1)

        self.NWB = QPushButton(self.groupBox)
        self.NWB.setObjectName(u"NWB")
        self.NWB.setMaximumSize(QSize(30, 30))

        self.gridLayout_9.addWidget(self.NWB, 0, 2, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_9, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Database_Viewer)

        self.data_base_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Database_Viewer)
    # setupUi

    def retranslateUi(self, Database_Viewer):
        Database_Viewer.setWindowTitle(QCoreApplication.translate("Database_Viewer", u"Form", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Database Connection", None))
        self.label.setText(QCoreApplication.translate("Database_Viewer", u"Select Table of Interest:", None))
        self.query_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Database Viewer", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Database_Viewer", u"Search for Table", None))
        self.SearchTable.setText("")
        self.query_execute.setText("")
        self.label_4.setText(QCoreApplication.translate("Database_Viewer", u"Query Table", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Database_Viewer", u"Home", None))
        self.HomeButton.setText("")
        self.DataGroup.setTitle(QCoreApplication.translate("Database_Viewer", u"Data Options", None))
        self.open_db.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Database_Viewer", u"Import/Export", None))
        self.export_table.setText("")
        self.select_columns.setText("")
        self.ImportDB.setText("")
        self.ParquetExport.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Database_Viewer", u"Table Selection", None))
        self.label_5.setText(QCoreApplication.translate("Database_Viewer", u"Open Comlex Query:", None))
        self.complex_query.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Database_Viewer", u"Plot Options", None))
        self.plot_home.setText("")
        self.save_plot_online.setText("")
        self.plot_zoom.setText("")
        self.plot_move.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Database_Viewer", u"Share Database Online", None))
        self.SQL.setText("")
        self.AWS.setText("")
        self.NWB.setText(QCoreApplication.translate("Database_Viewer", u"NWB", None))
    # retranslateUi

