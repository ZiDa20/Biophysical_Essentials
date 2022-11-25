# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_statistics_metadata.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class StatisticsMetaData_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 616)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sex_list = QListWidget(self.groupBox)
        self.sex_list.setObjectName(u"sex_list")

        self.gridLayout_3.addWidget(self.sex_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.condition_list = QListWidget(self.groupBox_2)
        self.condition_list.setObjectName(u"condition_list")

        self.gridLayout_4.addWidget(self.condition_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.individuum_list = QListWidget(self.groupBox_3)
        self.individuum_list.setObjectName(u"individuum_list")

        self.gridLayout_5.addWidget(self.individuum_list, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vs_button = QPushButton(self.groupBox_4)
        self.vs_button.setObjectName(u"vs_button")

        self.gridLayout_2.addWidget(self.vs_button, 0, 2, 1, 1)

        self.select_button = QPushButton(self.groupBox_4)
        self.select_button.setObjectName(u"select_button")

        self.gridLayout_2.addWidget(self.select_button, 1, 2, 1, 1)

        self.built_label_list = QListWidget(self.groupBox_4)
        self.built_label_list.setObjectName(u"built_label_list")

        self.gridLayout_2.addWidget(self.built_label_list, 0, 0, 2, 1)

        self.selected_comparisson_list = QListWidget(self.groupBox_4)
        self.selected_comparisson_list.setObjectName(u"selected_comparisson_list")

        self.gridLayout_2.addWidget(self.selected_comparisson_list, 0, 3, 2, 1)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Sex", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Condition", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Individuum_Id", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Stacked Selection ", None))
        self.vs_button.setText(QCoreApplication.translate("Dialog", u"vs", None))
        self.select_button.setText(QCoreApplication.translate("Dialog", u"select", None))
    # retranslateUi

