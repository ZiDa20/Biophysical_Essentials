# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_main_widget_layouted_trial.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from specific_analysis_tab import SpecificAnalysisTab


class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(956, 986)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Offline_Analysis.sizePolicy().hasHeightForWidth())
        Offline_Analysis.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Offline_Analysis)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Offline_Analysis_Notebook = QTabWidget(Offline_Analysis)
        self.Offline_Analysis_Notebook.setObjectName(u"Offline_Analysis_Notebook")
        self.Offline_Analysis_Notebook.setTabShape(QTabWidget.Rounded)
        self.Start_Analysis = QWidget()
        self.Start_Analysis.setObjectName(u"Start_Analysis")
        sizePolicy.setHeightForWidth(self.Start_Analysis.sizePolicy().hasHeightForWidth())
        self.Start_Analysis.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.Start_Analysis)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.offline_analysis_widgets = QStackedWidget(self.Start_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        sizePolicy.setHeightForWidth(self.offline_analysis_widgets.sizePolicy().hasHeightForWidth())
        self.offline_analysis_widgets.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.offline_analysis_widgets.setFont(font)
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        sizePolicy.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.start_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_10, 9, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 0, 17, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 6, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 0, 12, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 0, 11, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 10, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_21, 20, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 0, 5, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 8, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_18, 17, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 16, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 0, 13, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 0, 10, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 11, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_20, 19, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 0, 14, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 7, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_19, 18, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_14, 13, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 0, 16, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 15, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 0, 9, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 12, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 0, 15, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 8, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_15, 14, 0, 1, 1)

        self.groupBox = QGroupBox(self.start_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(509, 350))
        self.groupBox.setFont(font)
        self.blank_analysis_button = QPushButton(self.groupBox)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setGeometry(QRect(40, 60, 161, 41))
        self.blank_analysis_button.setFont(font)
        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(40, 170, 161, 71))
        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(40, 280, 161, 41))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 60, 241, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 170, 251, 41))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 280, 231, 41))

        self.gridLayout_4.addWidget(self.groupBox, 7, 5, 9, 10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.start_page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_2)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 4, 5, 1, 10)

        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.gridLayout_2 = QGridLayout(self.blank_analysis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_32 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_32, 1, 14, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_34, 15, 0, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_29, 1, 0, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_28, 14, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_22, 1, 15, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_37, 16, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_21, 1, 10, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_18, 1, 13, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_26, 19, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_26, 1, 12, 1, 1)

        self.groupBox_3 = QGroupBox(self.blank_analysis)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 30, 111, 41))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 30, 601, 42))

        self.gridLayout_2.addWidget(self.groupBox_3, 7, 1, 2, 16)

        self.verticalSpacer_32 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_32, 10, 0, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_38, 5, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_25, 1, 4, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_19, 1, 11, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_24, 1, 1, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_41, 4, 0, 1, 1)

        self.headline_layout = QVBoxLayout()
        self.headline_layout.setObjectName(u"headline_layout")
        self.label = QLabel(self.blank_analysis)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.headline_layout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.headline_layout, 3, 5, 1, 11)

        self.verticalSpacer_40 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_40, 6, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_20, 1, 3, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_27, 20, 0, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_29, 1, 7, 1, 1)

        self.groupBox_2 = QGroupBox(self.blank_analysis)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.select_directory_button = QPushButton(self.groupBox_2)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setGeometry(QRect(10, 30, 111, 41))
        self.selected_directory = QLabel(self.groupBox_2)
        self.selected_directory.setObjectName(u"selected_directory")
        self.selected_directory.setGeometry(QRect(160, 30, 601, 42))

        self.gridLayout_2.addWidget(self.groupBox_2, 4, 1, 2, 16)

        self.horizontalSpacer_31 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_31, 1, 17, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_23, 8, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_24, 11, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_27, 1, 2, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_22, 3, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_30, 9, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_25, 13, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_34, 1, 5, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_35, 17, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_33, 12, 0, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_39, 7, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_23, 1, 8, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 39, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_36, 18, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_30, 1, 9, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_28, 1, 6, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_33, 1, 16, 1, 1)

        self.groupBox_4 = QGroupBox(self.blank_analysis)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(300, 0))
        self.groupBox_4.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.directory_tree_widget = QTabWidget(self.groupBox_4)
        self.directory_tree_widget.setObjectName(u"directory_tree_widget")
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.gridLayout_8 = QGridLayout(self.selected_tree_view)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.experiments_tree_view = QTreeWidget(self.selected_tree_view)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")

        self.gridLayout_8.addWidget(self.experiments_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.selected_tree_view, "")
        self.discarde_tree_view = QWidget()
        self.discarde_tree_view.setObjectName(u"discarde_tree_view")
        self.outfiltered_tree_view = QTreeWidget(self.discarde_tree_view)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")
        self.outfiltered_tree_view.setGeometry(QRect(0, 0, 341, 421))
        self.directory_tree_widget.addTab(self.discarde_tree_view, "")

        self.gridLayout_5.addWidget(self.directory_tree_widget, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 10, 1, 10, 7)

        self.groupBox_5 = QGroupBox(self.blank_analysis)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 10, 9, 9, 8)

        self.compare_series = QPushButton(self.blank_analysis)
        self.compare_series.setObjectName(u"compare_series")

        self.gridLayout_2.addWidget(self.compare_series, 19, 11, 1, 4)

        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.analysis_specific_notebook = QWidget()
        self.analysis_specific_notebook.setObjectName(u"analysis_specific_notebook")
        self.gridLayout_6 = QGridLayout(self.analysis_specific_notebook)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.analysis_specific_notebook)
        self.tabWidget.setObjectName(u"tabWidget")
        self.template_tab = SpecificAnalysisTab()
        self.template_tab.setObjectName(u"template_tab")
        self.tabWidget.addTab(self.template_tab, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.analysis_specific_notebook)

        self.gridLayout_3.addWidget(self.offline_analysis_widgets, 1, 0, 1, 1)

        self.Offline_Analysis_Notebook.addTab(self.Start_Analysis, "")
        self.visualization = QWidget()
        self.visualization.setObjectName(u"visualization")
        self.visualization_tab_widget = QTabWidget(self.visualization)
        self.visualization_tab_widget.setObjectName(u"visualization_tab_widget")
        self.visualization_tab_widget.setGeometry(QRect(0, 0, 1641, 961))
        self.template_tab_2 = SpecificAnalysisTab()
        self.template_tab_2.setObjectName(u"template_tab_2")
        self.visualization_tab_widget.addTab(self.template_tab_2, "")
        self.Offline_Analysis_Notebook.addTab(self.visualization, "")

        self.gridLayout.addWidget(self.Offline_Analysis_Notebook, 0, 0, 1, 1)


        self.retranslateUi(Offline_Analysis)

        self.Offline_Analysis_Notebook.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(1)
        self.directory_tree_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Offline_Analysis", u"Offline Analysis Options", None))
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"Blank Analysis", None))
        self.pushButton_8.setText(QCoreApplication.translate("Offline_Analysis", u"Analysis from \n"
" previous Analysis", None))
        self.pushButton_9.setText(QCoreApplication.translate("Offline_Analysis", u"Open Analysis Results", None))
        self.label_3.setText(QCoreApplication.translate("Offline_Analysis", u"Start a new analysis from the scratch !", None))
        self.label_4.setText(QCoreApplication.translate("Offline_Analysis", u"Use an existing analysis from the database \n"
"and modify paramters for a new analysis !", None))
        self.label_5.setText(QCoreApplication.translate("Offline_Analysis", u"Opens the visualization of results of \n"
"already succesfully performed analysis", None))
        self.label_2.setText(QCoreApplication.translate("Offline_Analysis", u"SELECT A SPECIFIC OFFLINE ANALYSIS", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Offline_Analysis", u"Filter Selection", None))
        self.pushButton_3.setText(QCoreApplication.translate("Offline_Analysis", u"Add Filter", None))
        self.label_7.setText(QCoreApplication.translate("Offline_Analysis", u"No Filter Selected", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"Blank Offline Analysis", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Offline_Analysis", u"Experiment Location", None))
        self.select_directory_button.setText(QCoreApplication.translate("Offline_Analysis", u"Select Directory", None))
        self.selected_directory.setText(QCoreApplication.translate("Offline_Analysis", u"No Path Selected", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Offline_Analysis", u"Experiment Hierarchie", None))
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Offline_Analysis", u"Discard", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Offline_Analysis", u"Sel", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Offline_Analysis", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Offline_Analysis", u"Selected", None))
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Offline_Analysis", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Offline_Analysis", u"Selected", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Offline_Analysis", u"Object", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.discarde_tree_view), QCoreApplication.translate("Offline_Analysis", u"Discarded", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data View", None))
        self.compare_series.setText(QCoreApplication.translate("Offline_Analysis", u"SELECT SERIES TO BE ANALYZED", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.template_tab), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.Start_Analysis), QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.visualization_tab_widget.setTabText(self.visualization_tab_widget.indexOf(self.template_tab_2), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.visualization), QCoreApplication.translate("Offline_Analysis", u"Visualization", None))
    # retranslateUi

