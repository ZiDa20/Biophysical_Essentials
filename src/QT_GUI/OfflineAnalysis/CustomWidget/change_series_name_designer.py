# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_series_name.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.series_names_combobox = QComboBox(self.groupBox)
        self.series_names_combobox.setObjectName(u"series_names_combobox")

        self.gridLayout_3.addWidget(self.series_names_combobox, 0, 0, 1, 1)

        self.new_name_field = QLineEdit(self.groupBox)
        self.new_name_field.setObjectName(u"new_name_field")

        self.gridLayout_3.addWidget(self.new_name_field, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.only_for_analysis = QCheckBox(self.groupBox_2)
        self.only_for_analysis.setObjectName(u"only_for_analysis")

        self.gridLayout.addWidget(self.only_for_analysis, 0, 0, 1, 1)

        self.permanent = QCheckBox(self.groupBox_2)
        self.permanent.setObjectName(u"permanent")

        self.gridLayout.addWidget(self.permanent, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.apply = QPushButton(Dialog)
        self.apply.setObjectName(u"apply")

        self.gridLayout_2.addWidget(self.apply, 3, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Select Changes", None))
        self.new_name_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"New Series Name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Save Changes", None))
        self.only_for_analysis.setText(QCoreApplication.translate("Dialog", u"Only For This Analysis", None))
        self.permanent.setText(QCoreApplication.translate("Dialog", u"Permanent", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Rename Series", None))
        self.apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
    # retranslateUi

