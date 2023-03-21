# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_analysis_functions.ui'
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
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1256, 501)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.analysis_syntax = QLabel(self.groupBox_2)
        self.analysis_syntax.setObjectName(u"analysis_syntax")

        self.gridLayout_2.addWidget(self.analysis_syntax, 1, 1, 1, 1)

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

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_6)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.add_combined = QPushButton(self.groupBox_2)
        self.add_combined.setObjectName(u"add_combined")

        self.gridLayout_2.addWidget(self.add_combined, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.single_interval_grid = QGridLayout()
        self.single_interval_grid.setObjectName(u"single_interval_grid")

        self.gridLayout_5.addLayout(self.single_interval_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.selection_grid = QGridLayout()
        self.selection_grid.setObjectName(u"selection_grid")
        self.remove_last = QPushButton(self.groupBox_3)
        self.remove_last.setObjectName(u"remove_last")

        self.selection_grid.addWidget(self.remove_last, 1, 0, 1, 1)

        self.clear_all = QPushButton(self.groupBox_3)
        self.clear_all.setObjectName(u"clear_all")

        self.selection_grid.addWidget(self.clear_all, 1, 1, 1, 1)

        self.selection_list_widget = QListWidget(self.groupBox_3)
        self.selection_list_widget.setObjectName(u"selection_list_widget")

        self.selection_grid.addWidget(self.selection_list_widget, 0, 0, 1, 2)


        self.gridLayout_6.addLayout(self.selection_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 2, 1, 1)

        self.continue_with_selection = QPushButton(Dialog)
        self.continue_with_selection.setObjectName(u"continue_with_selection")

        self.gridLayout.addWidget(self.continue_with_selection, 3, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Combine Intervals", None))
        self.analysis_syntax.setText("")
        self.sub_analysis.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.div_analysis.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.l_bracket_analysis.setText(QCoreApplication.translate("Dialog", u"(", None))
        self.r_bracket_analysis.setText(QCoreApplication.translate("Dialog", u")", None))
        self.remove_last_analysis.setText(QCoreApplication.translate("Dialog", u"<-", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.add_combined.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Single Interval", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Selection", None))
        self.remove_last.setText(QCoreApplication.translate("Dialog", u"Remove Last", None))
        self.clear_all.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.continue_with_selection.setText(QCoreApplication.translate("Dialog", u"Continue with Selection", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select your Analysis Functions", None))
    # retranslateUi

