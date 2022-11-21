# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(655, 872)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(550, 0))
        self.groupBox_4.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.directory_tree_widget = QTabWidget(self.groupBox_4)
        self.directory_tree_widget.setObjectName(u"directory_tree_widget")
        sizePolicy.setHeightForWidth(self.directory_tree_widget.sizePolicy().hasHeightForWidth())
        self.directory_tree_widget.setSizePolicy(sizePolicy)
        self.directory_tree_widget.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:left;\n"
"width: 50;\n"
"height:50\n"
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
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.gridLayout_8 = QGridLayout(self.selected_tree_view)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.experiments_tree_view = QTreeWidget(self.selected_tree_view)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")
        self.experiments_tree_view.setFrameShape(QFrame.NoFrame)
        self.experiments_tree_view.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.experiments_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.selected_tree_view, "")
        self.discarde_tree_view = QWidget()
        self.discarde_tree_view.setObjectName(u"discarde_tree_view")
        self.gridLayout_2 = QGridLayout(self.discarde_tree_view)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.outfiltered_tree_view = QTreeWidget(self.discarde_tree_view)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")

        self.gridLayout_2.addWidget(self.outfiltered_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.discarde_tree_view, "")

        self.gridLayout_5.addWidget(self.directory_tree_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.directory_tree_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Experiment Hierarchie", None))
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Discard", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Group", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Form", u"Selected", None))
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Form", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"Group", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.discarde_tree_view), QCoreApplication.translate("Form", u"Discarded", None))
    # retranslateUi

