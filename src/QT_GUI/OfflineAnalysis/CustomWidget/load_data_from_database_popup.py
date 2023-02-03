# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_data_from_database_popup.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1181, 786)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.available_labels = QGroupBox(Dialog)
        self.available_labels.setObjectName(u"available_labels")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.available_labels.sizePolicy().hasHeightForWidth())
        self.available_labels.setSizePolicy(sizePolicy)
        self.available_labels.setMaximumSize(QSize(400, 16777215))
        self.available_labels.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.available_labels)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_grid = QGridLayout()
        self.label_grid.setObjectName(u"label_grid")

        self.gridLayout_2.addLayout(self.label_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.available_labels, 2, 0, 1, 1)

        self.load_data = QPushButton(Dialog)
        self.load_data.setObjectName(u"load_data")
        sizePolicy.setHeightForWidth(self.load_data.sizePolicy().hasHeightForWidth())
        self.load_data.setSizePolicy(sizePolicy)
        self.load_data.setMaximumSize(QSize(400, 40))

        self.gridLayout.addWidget(self.load_data, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.diagram_grid = QGridLayout()
        self.diagram_grid.setObjectName(u"diagram_grid")

        self.gridLayout_4.addLayout(self.diagram_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 2, 2, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Descriptive Statistics and Experiment Selection", None))
        self.available_labels.setTitle(QCoreApplication.translate("Dialog", u"Available Label", None))
        self.load_data.setText(QCoreApplication.translate("Dialog", u"Load Selection", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Descriptive Statistics", None))
    # retranslateUi

