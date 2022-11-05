# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_base_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)

class Ui_Database_Viewer(object):
    def setupUi(self, Database_Viewer):
        if not Database_Viewer.objectName():
            Database_Viewer.setObjectName(u"Database_Viewer")
        Database_Viewer.resize(1083, 822)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Database_Viewer.sizePolicy().hasHeightForWidth())
        Database_Viewer.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Database_Viewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 268, 579))
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
        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")

        self.gridLayout_12.addLayout(self.table_layout, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.query_line_edit = QLineEdit(self.query_gb)
        self.query_line_edit.setObjectName(u"query_line_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.query_line_edit.sizePolicy().hasHeightForWidth())
        self.query_line_edit.setSizePolicy(sizePolicy2)
        self.query_line_edit.setMinimumSize(QSize(250, 30))
        self.query_line_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.query_line_edit, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.query_execute = QPushButton(self.query_gb)
        self.query_execute.setObjectName(u"query_execute")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.query_execute.sizePolicy().hasHeightForWidth())
        self.query_execute.setSizePolicy(sizePolicy3)
        self.query_execute.setMinimumSize(QSize(100, 0))
        self.query_execute.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_9.addWidget(self.query_execute, 0, 0, 1, 1)

        self.select_columns = QPushButton(self.query_gb)
        self.select_columns.setObjectName(u"select_columns")

        self.gridLayout_9.addWidget(self.select_columns, 0, 1, 1, 1)

        self.export_table = QPushButton(self.query_gb)
        self.export_table.setObjectName(u"export_table")

        self.gridLayout_9.addWidget(self.export_table, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_9, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.gridLayout_5.addLayout(self.gridLayout_10, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.query_gb, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_4.addLayout(self.gridLayout_8, 0, 2, 1, 1)

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
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(Database_Viewer)

        self.data_base_stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Database_Viewer)
    # setupUi

    def retranslateUi(self, Database_Viewer):
        Database_Viewer.setWindowTitle(QCoreApplication.translate("Database_Viewer", u"Form", None))
        self.available_tables_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Database Connection", None))
        self.query_gb.setTitle(QCoreApplication.translate("Database_Viewer", u"Query", None))
        self.groupBox_3.setTitle("")
        self.query_execute.setText(QCoreApplication.translate("Database_Viewer", u"Execute", None))
        self.select_columns.setText(QCoreApplication.translate("Database_Viewer", u"Select Columns", None))
        self.export_table.setText(QCoreApplication.translate("Database_Viewer", u"Export Table", None))
        self.label.setText(QCoreApplication.translate("Database_Viewer", u"DataBase Viewer", None))
    # retranslateUi

