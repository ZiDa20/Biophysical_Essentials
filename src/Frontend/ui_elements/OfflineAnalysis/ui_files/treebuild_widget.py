# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treebuild_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QSizePolicy, QTabWidget,
    QTreeView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 872)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(10000000, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.directory_tree_widget = QTabWidget(self.groupBox_4)
        self.directory_tree_widget.setObjectName(u"directory_tree_widget")
        sizePolicy.setHeightForWidth(self.directory_tree_widget.sizePolicy().hasHeightForWidth())
        self.directory_tree_widget.setSizePolicy(sizePolicy)
        self.directory_tree_widget.setAutoFillBackground(True)
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
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        sizePolicy.setHeightForWidth(self.selected_tab.sizePolicy().hasHeightForWidth())
        self.selected_tab.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.selected_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selected_tree_view = QTreeView(self.selected_tab)
        self.selected_tree_view.setObjectName(u"selected_tree_view")

        self.gridLayout_8.addWidget(self.selected_tree_view, 0, 0, 1, 1)

        self.descriptive_meta_data_label = QLabel(self.selected_tab)
        self.descriptive_meta_data_label.setObjectName(u"descriptive_meta_data_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.descriptive_meta_data_label.sizePolicy().hasHeightForWidth())
        self.descriptive_meta_data_label.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.descriptive_meta_data_label, 2, 0, 1, 1)

        self.line = QFrame(self.selected_tab)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line, 1, 0, 1, 1)

        self.directory_tree_widget.addTab(self.selected_tab, "")
        self.discarded_tab = QWidget()
        self.discarded_tab.setObjectName(u"discarded_tab")
        sizePolicy.setHeightForWidth(self.discarded_tab.sizePolicy().hasHeightForWidth())
        self.discarded_tab.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.discarded_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.discarded_tree_view = QTreeView(self.discarded_tab)
        self.discarded_tree_view.setObjectName(u"discarded_tree_view")

        self.gridLayout_2.addWidget(self.discarded_tree_view, 0, 0, 1, 1)

        self.discarded_meta_data_label = QLabel(self.discarded_tab)
        self.discarded_meta_data_label.setObjectName(u"discarded_meta_data_label")
        sizePolicy1.setHeightForWidth(self.discarded_meta_data_label.sizePolicy().hasHeightForWidth())
        self.discarded_meta_data_label.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.discarded_meta_data_label, 2, 0, 1, 1)

        self.line_2 = QFrame(self.discarded_tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.directory_tree_widget.addTab(self.discarded_tab, "")

        self.gridLayout_5.addWidget(self.directory_tree_widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.directory_tree_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Experiment Hierarchie", None))
        self.descriptive_meta_data_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.selected_tab), QCoreApplication.translate("Form", u"Selected", None))
        self.discarded_meta_data_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.discarded_tab), QCoreApplication.translate("Form", u"Discarded", None))
    # retranslateUi

