# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_analysis_functins.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1256, 536)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sub_analysis = QPushButton(self.groupBox_2)
        self.sub_analysis.setObjectName(u"sub_analysis")
        self.sub_analysis.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.sub_analysis)

        self.div_analysis = QPushButton(self.groupBox_2)
        self.div_analysis.setObjectName(u"div_analysis")
        self.div_analysis.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.div_analysis)

        self.l_bracket_analysis = QPushButton(self.groupBox_2)
        self.l_bracket_analysis.setObjectName(u"l_bracket_analysis")
        self.l_bracket_analysis.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.l_bracket_analysis)

        self.r_bracket_analysis = QPushButton(self.groupBox_2)
        self.r_bracket_analysis.setObjectName(u"r_bracket_analysis")
        self.r_bracket_analysis.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.r_bracket_analysis)

        self.remove_last_analysis = QPushButton(self.groupBox_2)
        self.remove_last_analysis.setObjectName(u"remove_last_analysis")
        self.remove_last_analysis.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.remove_last_analysis)

        self.clear_analysis_button = QPushButton(self.groupBox_2)
        self.clear_analysis_button.setObjectName(u"clear_analysis_button")
        self.clear_analysis_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.clear_analysis_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.analysis_syntax = QLabel(self.groupBox_2)
        self.analysis_syntax.setObjectName(u"analysis_syntax")

        self.gridLayout_2.addWidget(self.analysis_syntax, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 2, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")

        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.gridLayout.addWidget(self.groupBox_3, 3, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select your Analysis Functions", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Combine Intervals", None))
        self.sub_analysis.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.div_analysis.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.l_bracket_analysis.setText(QCoreApplication.translate("Dialog", u"(", None))
        self.r_bracket_analysis.setText(QCoreApplication.translate("Dialog", u")", None))
        self.remove_last_analysis.setText(QCoreApplication.translate("Dialog", u"<-", None))
        self.clear_analysis_button.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.analysis_syntax.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Single Interval", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Selection", None))
    # retranslateUi

