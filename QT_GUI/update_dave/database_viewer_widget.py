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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 820)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.data_base_stacked_widget = QStackedWidget(Form)
        self.data_base_stacked_widget.setObjectName(u"data_base_stacked_widget")
        self.no_database = QWidget()
        self.no_database.setObjectName(u"no_database")
        self.gridLayout = QGridLayout(self.no_database)
        self.gridLayout.setObjectName(u"gridLayout")
        self.instruction_label = QLabel(self.no_database)
        self.instruction_label.setObjectName(u"instruction_label")

        self.gridLayout.addWidget(self.instruction_label, 0, 0, 1, 1)

        self.connect_to_database = QPushButton(self.no_database)
        self.connect_to_database.setObjectName(u"connect_to_database")

        self.gridLayout.addWidget(self.connect_to_database, 1, 0, 1, 1)

        self.data_base_stacked_widget.addWidget(self.no_database)
        self.data_base = QWidget()
        self.data_base.setObjectName(u"data_base")
        self.gridLayout_4 = QGridLayout(self.data_base)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.query_gb = QGroupBox(self.data_base)
        self.query_gb.setObjectName(u"query_gb")
        self.query_gb.setMinimumSize(QSize(500, 0))
        self.query_gb.setMaximumSize(QSize(500, 16777215))
        self.gridLayout_5 = QGridLayout(self.query_gb)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_3 = QGroupBox(self.query_gb)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(500, 0))

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

        self.horizontalLayout_3.addWidget(self.query_execute)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.query_gb, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 749))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.available_tables_gb, 0, 0, 2, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.textBrowser = QTextBrowser(self.data_base)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(300, 0))
        self.textBrowser.setMaximumSize(QSize(300, 250))

        self.gridLayout_8.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 2, 1, 1)

        self.data_base_stacked_widget.addWidget(self.data_base)

        self.gridLayout_2.addWidget(self.data_base_stacked_widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.data_base_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.instruction_label.setText(QCoreApplication.translate("Form", u"No database connected - please select a database to connect", None))
        self.connect_to_database.setText(QCoreApplication.translate("Form", u"Select Database", None))
        self.query_gb.setTitle(QCoreApplication.translate("Form", u"Query", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Data", None))
        self.query_execute.setText(QCoreApplication.translate("Form", u"Execute", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Form", u"Available Tables", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Here you can browse your database, check the tables and also draw columns if numeric. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
    # retranslateUi

