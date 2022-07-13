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
        Database_Viewer.resize(1305, 822)
        self.gridLayout_2 = QGridLayout(Database_Viewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.data_base_stacked_widget = QStackedWidget(Database_Viewer)
        self.data_base_stacked_widget.setObjectName(u"data_base_stacked_widget")
        self.data_base = QWidget()
        self.data_base.setObjectName(u"data_base")
        self.gridLayout_4 = QGridLayout(self.data_base)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.query_gb = QGroupBox(self.data_base)
        self.query_gb.setObjectName(u"query_gb")
        self.query_gb.setMinimumSize(QSize(500, 0))
        self.query_gb.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_5 = QGridLayout(self.query_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_3 = QGroupBox(self.query_gb)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(500, 0))
        self.gridLayout_12 = QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")

        self.gridLayout_12.addLayout(self.table_layout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.query_line_edit = QLineEdit(self.query_gb)
        self.query_line_edit.setObjectName(u"query_line_edit")
        self.query_line_edit.setMinimumSize(QSize(400, 0))
        self.query_line_edit.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_3.addWidget(self.query_line_edit, 0, Qt.AlignLeft)

        self.query_execute = QPushButton(self.query_gb)
        self.query_execute.setObjectName(u"query_execute")
        self.query_execute.setMinimumSize(QSize(50, 0))
        self.query_execute.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.query_execute, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.query_gb, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.available_tables_gb = QGroupBox(self.data_base)
        self.available_tables_gb.setObjectName(u"available_tables_gb")
        self.available_tables_gb.setMinimumSize(QSize(300, 0))
        self.available_tables_gb.setMaximumSize(QSize(300, 16777215))
        self.gridLayout_7 = QGridLayout(self.available_tables_gb)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea = QScrollArea(self.available_tables_gb)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 640))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.database_table = QListWidget(self.scrollAreaWidgetContents)
        self.database_table.setObjectName(u"database_table")

        self.gridLayout_6.addWidget(self.database_table, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.button_database_series = QGridLayout()
        self.button_database_series.setObjectName(u"button_database_series")

        self.gridLayout_7.addLayout(self.button_database_series, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.available_tables_gb, 0, 0, 2, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.textBrowser = QTextBrowser(self.data_base)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(300, 0))
        self.textBrowser.setMaximumSize(QSize(16777215, 250))

        self.gridLayout_8.addWidget(self.textBrowser, 2, 0, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

        self.data_base_stacked_widget.addWidget(self.data_base)

        self.gridLayout_2.addWidget(self.data_base_stacked_widget, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.frame = QFrame(Database_Viewer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Database_Viewer)

        self.data_base_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Database_Viewer)
    # setupUi

    def retranslateUi(self, Database_Viewer):
        Database_Viewer.setWindowTitle(QCoreApplication.translate("Database_Viewer", u"Form", None))
        self.query_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Query", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Database_Viewer", u"Data", None))
        self.query_execute.setText(QCoreApplication.translate("Database_Viewer", u"Execute", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Available Tables", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Database_Viewer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Here you can browse your database, check the tables and also draw columns if numeric. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Database_Viewer", u"DataBase Viewer", None))
    # retranslateUi

