# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_base_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


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
        self.gridLayout_2.setContentsMargins(1, 0, 1, 3)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 627))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.database_table = QListWidget(self.scrollAreaWidgetContents)
        self.database_table.setObjectName(u"database_table")

        self.gridLayout_6.addWidget(self.database_table, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.available_tables_gb, 0, 2, 1, 1)

        self.query_gb = QGroupBox(self.data_base)
        self.query_gb.setObjectName(u"query_gb")
        sizePolicy.setHeightForWidth(self.query_gb.sizePolicy().hasHeightForWidth())
        self.query_gb.setSizePolicy(sizePolicy)
        self.query_gb.setMinimumSize(QSize(500, 0))
        self.query_gb.setMaximumSize(QSize(16777215, 16777215))
        self.query_gb.setFont(font)
        self.gridLayout_5 = QGridLayout(self.query_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_5.addLayout(self.gridLayout_10, 2, 0, 1, 1)

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


        self.gridLayout_3.addWidget(self.query_gb, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 2, 1, 1)

        self.data_base_stacked_widget.addWidget(self.data_base)

        self.gridLayout_2.addWidget(self.data_base_stacked_widget, 1, 0, 1, 1)

        self.frame = QFrame(Database_Viewer)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"QPushButton{\n"
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.gridLayout_22.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../../Logo/new_logo_final.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_3, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_22)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.DataGroup = QGroupBox(self.frame)
        self.DataGroup.setObjectName(u"DataGroup")
        self.gridLayout_13 = QGridLayout(self.DataGroup)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.export_table = QPushButton(self.DataGroup)
        self.export_table.setObjectName(u"export_table")
        self.export_table.setMinimumSize(QSize(30, 30))
        self.export_table.setMaximumSize(QSize(30, 30))
        self.export_table.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/export_csv.png);")

        self.DataOptions.addWidget(self.export_table, 0, 2, 1, 1)

        self.select_columns = QPushButton(self.DataGroup)
        self.select_columns.setObjectName(u"select_columns")
        self.select_columns.setMinimumSize(QSize(30, 30))
        self.select_columns.setMaximumSize(QSize(30, 30))
        self.select_columns.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/col.png);")

        self.DataOptions.addWidget(self.select_columns, 2, 0, 1, 1)

        self.open_db = QPushButton(self.DataGroup)
        self.open_db.setObjectName(u"open_db")
        self.open_db.setMinimumSize(QSize(30, 30))
        self.open_db.setMaximumSize(QSize(30, 30))
        self.open_db.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/open.png);")

        self.DataOptions.addWidget(self.open_db, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.DataOptions.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)


        self.gridLayout_13.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.DataGroup)

        self.PlotGroup = QGroupBox(self.frame)
        self.PlotGroup.setObjectName(u"PlotGroup")
        self.gridLayout_14 = QGridLayout(self.PlotGroup)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(1, 3, 1, 3)
        self.PlotOptions = QGridLayout()
        self.PlotOptions.setObjectName(u"PlotOptions")
        self.save_plot_online = QPushButton(self.PlotGroup)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(30, 30))
        self.save_plot_online.setMaximumSize(QSize(30, 30))
        font2 = QFont()
        font2.setPointSize(6)
        self.save_plot_online.setFont(font2)
        self.save_plot_online.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/save_img.png);")

        self.PlotOptions.addWidget(self.save_plot_online, 1, 0, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(30, 30))
        self.plot_zoom.setMaximumSize(QSize(30, 30))
        self.plot_zoom.setFont(font2)
        self.plot_zoom.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/zoom.png);")

        self.PlotOptions.addWidget(self.plot_zoom, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.PlotOptions.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(30, 30))
        self.plot_move.setMaximumSize(QSize(30, 30))
        self.plot_move.setFont(font2)
        self.plot_move.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/move.png);")

        self.PlotOptions.addWidget(self.plot_move, 1, 2, 1, 1)

        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))
        self.plot_home.setFont(font2)
        self.plot_home.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/home.png);")

        self.PlotOptions.addWidget(self.plot_home, 0, 0, 1, 1)


        self.gridLayout_14.addLayout(self.PlotOptions, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.PlotGroup)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_17 = QGridLayout(self.groupBox_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.select_table = QComboBox(self.groupBox_2)
        self.select_table.setObjectName(u"select_table")

        self.gridLayout_17.addWidget(self.select_table, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_17.addWidget(self.label, 0, 0, 1, 1, Qt.AlignBottom)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.complex_query = QPushButton(self.groupBox)
        self.complex_query.setObjectName(u"complex_query")
        self.complex_query.setMinimumSize(QSize(30, 30))
        self.complex_query.setMaximumSize(QSize(30, 30))
        self.complex_query.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/open_edit.png);")

        self.gridLayout_9.addWidget(self.complex_query, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.query_execute = QPushButton(self.groupBox)
        self.query_execute.setObjectName(u"query_execute")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.query_execute.sizePolicy().hasHeightForWidth())
        self.query_execute.setSizePolicy(sizePolicy2)
        self.query_execute.setMinimumSize(QSize(30, 30))
        self.query_execute.setMaximumSize(QSize(30, 30))
        self.query_execute.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/execute.png);")

        self.gridLayout_9.addWidget(self.query_execute, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.query_line_edit = QLineEdit(self.groupBox)
        self.query_line_edit.setObjectName(u"query_line_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.query_line_edit.sizePolicy().hasHeightForWidth())
        self.query_line_edit.setSizePolicy(sizePolicy3)
        self.query_line_edit.setMinimumSize(QSize(250, 30))
        self.query_line_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_18.addWidget(self.query_line_edit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_18.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_18, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalSpacer_5 = QSpacerItem(700, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Database_Viewer)

        self.data_base_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Database_Viewer)
    # setupUi

    def retranslateUi(self, Database_Viewer):
        Database_Viewer.setWindowTitle(QCoreApplication.translate("Database_Viewer", u"Form", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Database Connection", None))
        self.query_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Query", None))
        self.groupBox_3.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Database_Viewer", u"DataBase Viewer:", None))
        self.label_3.setText("")
        self.DataGroup.setTitle(QCoreApplication.translate("Database_Viewer", u"Data Options", None))
        self.export_table.setText("")
        self.select_columns.setText("")
        self.open_db.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Database_Viewer", u"Plot Options", None))
        self.save_plot_online.setText("")
        self.plot_zoom.setText("")
        self.plot_move.setText("")
        self.plot_home.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Database_Viewer", u"Table Selection", None))
        self.label.setText(QCoreApplication.translate("Database_Viewer", u"Select Table of Interest:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Database_Viewer", u"Query", None))
        self.complex_query.setText("")
        self.label_5.setText(QCoreApplication.translate("Database_Viewer", u"Complex Query:", None))
        self.query_execute.setText("")
        self.label_6.setText(QCoreApplication.translate("Database_Viewer", u"Execute", None))
        self.label_4.setText(QCoreApplication.translate("Database_Viewer", u"Small Query:", None))
    # retranslateUi

