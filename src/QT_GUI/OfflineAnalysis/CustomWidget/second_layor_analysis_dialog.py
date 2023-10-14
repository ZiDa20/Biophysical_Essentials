# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second_layer_analysis_functions.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(753, 588)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.run_second_layer_analysis_function = QPushButton(Dialog)
        self.run_second_layer_analysis_function.setObjectName(u"run_second_layer_analysis_function")

        self.gridLayout.addWidget(self.run_second_layer_analysis_function, 3, 0, 1, 1)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.gridLayout.addWidget(self.cancel, 3, 1, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.first_layer_analysis_functions = QComboBox(self.groupBox_2)
        self.first_layer_analysis_functions.setObjectName(u"first_layer_analysis_functions")

        self.gridLayout_3.addWidget(self.first_layer_analysis_functions, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.second_layer_analysis_functions = QComboBox(self.groupBox)
        self.second_layer_analysis_functions.addItem("")
        self.second_layer_analysis_functions.addItem("")
        self.second_layer_analysis_functions.addItem("")
        self.second_layer_analysis_functions.setObjectName(u"second_layer_analysis_functions")

        self.gridLayout_2.addWidget(self.second_layer_analysis_functions, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.run_second_layer_analysis_function.setText(QCoreApplication.translate("Dialog", u"Run", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Select Previous Analysis", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Results from which first layer analysis should be considered for the second layer analysis function ?", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Select Second Layer Analysis Function", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Which function do you want to execute", None))
        self.second_layer_analysis_functions.setItemText(0, QCoreApplication.translate("Dialog", u"PCA", None))
        self.second_layer_analysis_functions.setItemText(1, QCoreApplication.translate("Dialog", u"IV-Boltzmann Fitting", None))
        self.second_layer_analysis_functions.setItemText(2, QCoreApplication.translate("Dialog", u"Hill-Curve", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome to the second layer analysis function selection", None))
    # retranslateUi

