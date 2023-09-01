# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabaseTable.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_DatabaseTable(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(524, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.query_gb = QGroupBox(Form)
        self.query_gb.setObjectName(u"query_gb")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query_gb.sizePolicy().hasHeightForWidth())
        self.query_gb.setSizePolicy(sizePolicy)
        self.query_gb.setMinimumSize(QSize(500, 0))
        self.query_gb.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(15)
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
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
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


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.query_gb)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_10.addWidget(self.pushButton, 0, 2, 1, 1)

        self.label_12 = QLabel(self.query_gb)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_10.addWidget(self.label_12, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_10, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.query_gb, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(accessibility)
        self.query_gb.setAccessibleName(QCoreApplication.translate("Form", u"new_color", None))
#endif // QT_CONFIG(accessibility)
        self.query_gb.setTitle(QCoreApplication.translate("Form", u"Database Viewer", None))
        self.groupBox_3.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Snow More", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Snow the next 100", None))
    # retranslateUi

