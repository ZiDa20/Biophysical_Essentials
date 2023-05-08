# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'normalization_value_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(979, 616)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_grid_layout = QGridLayout()
        self.table_grid_layout.setObjectName(u"table_grid_layout")

        self.gridLayout_3.addLayout(self.table_grid_layout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 3, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 6, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.normalization_method = QComboBox(Dialog)
        self.normalization_method.setObjectName(u"normalization_method")

        self.gridLayout_2.addWidget(self.normalization_method, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Sorry, this is not implemented yet. If you have a specific use case to be implemented, please contact us and we are happy to provide a solution", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"From the Combo Box below, select the normalization method. If further input is required, the wizard will giude you through that process. ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Confirm And Continue", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select Normalization Method", None))
    # retranslateUi

