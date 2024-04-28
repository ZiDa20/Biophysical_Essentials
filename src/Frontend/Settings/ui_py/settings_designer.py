# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_new_layout_240428.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1146, 689)
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.page_headline = QLabel(Form)
        self.page_headline.setObjectName(u"page_headline")
        font = QFont()
        font.setPointSize(19)
        self.page_headline.setFont(font)
        self.page_headline.setLayoutDirection(Qt.LeftToRight)
        self.page_headline.setAlignment(Qt.AlignCenter)
        self.page_headline.setMargin(5)

        self.gridLayout.addWidget(self.page_headline, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.database_settings_details = QWidget()
        self.database_settings_details.setObjectName(u"database_settings_details")
        self.gridLayout_3 = QGridLayout(self.database_settings_details)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.database_settings_details)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 800))
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.current_database_label = QLabel(self.groupBox_5)
        self.current_database_label.setObjectName(u"current_database_label")
        self.current_database_label.setMinimumSize(QSize(0, 0))
        self.current_database_label.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_7.addWidget(self.current_database_label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.restore_db_defaults_button = QPushButton(self.widget)
        self.restore_db_defaults_button.setObjectName(u"restore_db_defaults_button")

        self.gridLayout_4.addWidget(self.restore_db_defaults_button, 9, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.db_path_lineEdit = QLineEdit(self.groupBox_3)
        self.db_path_lineEdit.setObjectName(u"db_path_lineEdit")

        self.gridLayout_5.addWidget(self.db_path_lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.select_db_path_button = QPushButton(self.groupBox_3)
        self.select_db_path_button.setObjectName(u"select_db_path_button")

        self.gridLayout_5.addWidget(self.select_db_path_button, 0, 2, 1, 1)

        self.db_name_line_edit = QLineEdit(self.groupBox_3)
        self.db_name_line_edit.setObjectName(u"db_name_line_edit")

        self.gridLayout_5.addWidget(self.db_name_line_edit, 1, 1, 1, 1)

        self.create_database_button = QPushButton(self.groupBox_3)
        self.create_database_button.setObjectName(u"create_database_button")

        self.gridLayout_5.addWidget(self.create_database_button, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.search_existing_db_button = QPushButton(self.groupBox_4)
        self.search_existing_db_button.setObjectName(u"search_existing_db_button")

        self.gridLayout_6.addWidget(self.search_existing_db_button, 0, 2, 1, 1)

        self.existing_db_lineEdit = QLineEdit(self.groupBox_4)
        self.existing_db_lineEdit.setObjectName(u"existing_db_lineEdit")

        self.gridLayout_6.addWidget(self.existing_db_lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.connect_to_existing_db_button = QPushButton(self.groupBox_4)
        self.connect_to_existing_db_button.setObjectName(u"connect_to_existing_db_button")

        self.gridLayout_6.addWidget(self.connect_to_existing_db_button, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 8, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.database_settings_details)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.databas_category_button = QPushButton(self.groupBox)
        self.databas_category_button.setObjectName(u"databas_category_button")

        self.verticalLayout.addWidget(self.databas_category_button)

        self.back_to_home = QPushButton(self.groupBox)
        self.back_to_home.setObjectName(u"back_to_home")

        self.verticalLayout.addWidget(self.back_to_home)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.page_headline.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Details", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Current Database Connection", None))
        self.current_database_label.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Status: Successfully Connected", None))
        self.label_6.setText("")
        self.restore_db_defaults_button.setText(QCoreApplication.translate("Form", u"Restore Default Settings", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Create a new database", None))
        self.label.setText(QCoreApplication.translate("Form", u"Path", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name", None))
        self.select_db_path_button.setText(QCoreApplication.translate("Form", u"Select Path", None))
        self.create_database_button.setText(QCoreApplication.translate("Form", u"Create New Database", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Connect to existing database", None))
        self.search_existing_db_button.setText(QCoreApplication.translate("Form", u"Select DB", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Database", None))
        self.connect_to_existing_db_button.setText(QCoreApplication.translate("Form", u"Connect to existing DB", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Select the path and the name of the database object. ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Category", None))
        self.databas_category_button.setText(QCoreApplication.translate("Form", u"Database Settings", None))
        self.back_to_home.setText(QCoreApplication.translate("Form", u"Back to Home", None))
    # retranslateUi

