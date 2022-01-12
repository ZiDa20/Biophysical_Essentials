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
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1162, 926)
        self.data_base_stacked_widget = QStackedWidget(Form)
        self.data_base_stacked_widget.setObjectName(u"data_base_stacked_widget")
        self.data_base_stacked_widget.setGeometry(QRect(80, 90, 1021, 731))
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
        self.available_tables_gb = QGroupBox(self.data_base)
        self.available_tables_gb.setObjectName(u"available_tables_gb")
        self.available_tables_gb.setGeometry(QRect(20, 10, 171, 721))
        self.query_gb = QGroupBox(self.data_base)
        self.query_gb.setObjectName(u"query_gb")
        self.query_gb.setGeometry(QRect(210, 10, 731, 91))
        self.query_line_edit = QLineEdit(self.query_gb)
        self.query_line_edit.setObjectName(u"query_line_edit")
        self.query_line_edit.setGeometry(QRect(20, 29, 571, 41))
        self.query_execute = QPushButton(self.query_gb)
        self.query_execute.setObjectName(u"query_execute")
        self.query_execute.setGeometry(QRect(614, 32, 91, 41))
        self.groupBox_3 = QGroupBox(self.data_base)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(210, 110, 731, 621))
        self.data_base_stacked_widget.addWidget(self.data_base)

        self.retranslateUi(Form)

        self.data_base_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.instruction_label.setText(QCoreApplication.translate("Form", u"No database connected - please select a database to connect", None))
        self.connect_to_database.setText(QCoreApplication.translate("Form", u"Select Database", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Form", u"Availabl Tables", None))
        self.query_gb.setTitle(QCoreApplication.translate("Form", u"Query", None))
        self.query_execute.setText(QCoreApplication.translate("Form", u"Execute", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Data", None))
    # retranslateUi

