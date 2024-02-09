# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QWidget, QDialog, QProgressDialog)

class Ui_LoadingDialog(QDialog):
    def setupUi(self, LoadingDialog):
        if not LoadingDialog.objectName():
            LoadingDialog.setObjectName(u"LoadingDialog")
        LoadingDialog.resize(400, 300)
        self.gridLayout_2 = QGridLayout(LoadingDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.loading_dialog = QGridLayout()
        self.loading_dialog.setObjectName(u"loading_dialog")

        self.gridLayout_2.addLayout(self.loading_dialog, 0, 0, 1, 1)


        self.retranslateUi(LoadingDialog)

        QMetaObject.connectSlotsByName(LoadingDialog)
    # setupUi

    def retranslateUi(self, LoadingDialog):
        LoadingDialog.setWindowTitle(QCoreApplication.translate("LoadingDialog", u"Dialog", None))
    # retranslateUi

