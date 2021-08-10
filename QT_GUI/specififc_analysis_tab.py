# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specific_analysis_tab.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1439, 854)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout = QGridLayout(SpecificAnalysisTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_27 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_27, 0, 2, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_21, 0, 10, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_26, 0, 12, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_33, 0, 16, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_34, 0, 5, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_29, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(300, 450))
        self.groupBox_4.setMaximumSize(QSize(400, 16777215))
        self.tabWidget = QTabWidget(self.groupBox_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 26, 341, 431))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(0, 350))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"border:0")
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        self.gridLayout_8 = QGridLayout(self.selected_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selected_tree_widget = QTreeWidget(self.selected_tab)
        self.selected_tree_widget.setObjectName(u"selected_tree_widget")
        sizePolicy1.setHeightForWidth(self.selected_tree_widget.sizePolicy().hasHeightForWidth())
        self.selected_tree_widget.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.selected_tree_widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.selected_tab, "")
        self.discarded_tab = QWidget()
        self.discarded_tab.setObjectName(u"discarded_tab")
        self.gridLayout_2 = QGridLayout(self.discarded_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.discarded_tree_widget = QTreeWidget(self.discarded_tab)
        self.discarded_tree_widget.setObjectName(u"discarded_tree_widget")

        self.gridLayout_2.addWidget(self.discarded_tree_widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.discarded_tab, "")

        self.gridLayout.addWidget(self.groupBox_4, 3, 1, 9, 7)

        self.horizontalSpacer_22 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_22, 0, 15, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_20, 0, 3, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_19, 0, 11, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_28, 12, 0, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_41, 2, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_23, 6, 0, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_35, 15, 0, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_34, 13, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_26, 17, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_32, 8, 0, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_36, 16, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_30, 0, 9, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_38, 3, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 0, 13, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_33, 10, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_25, 0, 4, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_37, 14, 0, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_39, 5, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_24, 9, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_32, 0, 14, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_30, 7, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_23, 0, 8, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_22, 1, 0, 1, 1)

        self.groupBox = QGroupBox(SpecificAnalysisTab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMaximumSize(QSize(16777215, 500))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.function_selection_grid = QGridLayout()
        self.function_selection_grid.setObjectName(u"function_selection_grid")
        self.function_selection_grid.setSizeConstraint(QLayout.SetMinimumSize)
        self.column_1_head = QLabel(self.groupBox)
        self.column_1_head.setObjectName(u"column_1_head")
        self.column_1_head.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.column_1_head, 0, 1, 1, 1)

        self.column_3_row_3 = QLabel(self.groupBox)
        self.column_3_row_3.setObjectName(u"column_3_row_3")
        self.column_3_row_3.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setItalic(True)
        self.column_3_row_3.setFont(font1)

        self.function_selection_grid.addWidget(self.column_3_row_3, 1, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setFont(font1)

        self.function_selection_grid.addWidget(self.label_11, 1, 4, 1, 1)

        self.column_2_head = QLabel(self.groupBox)
        self.column_2_head.setObjectName(u"column_2_head")
        self.column_2_head.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.column_2_head, 0, 2, 1, 1)

        self.column_2_row_2 = QLabel(self.groupBox)
        self.column_2_row_2.setObjectName(u"column_2_row_2")
        self.column_2_row_2.setMaximumSize(QSize(16777215, 50))
        self.column_2_row_2.setFont(font1)

        self.function_selection_grid.addWidget(self.column_2_row_2, 1, 2, 1, 1)

        self.select_series_analysis_functions = QPushButton(self.groupBox)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        self.select_series_analysis_functions.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.select_series_analysis_functions, 1, 0, 1, 1)

        self.column_4_head = QLabel(self.groupBox)
        self.column_4_head.setObjectName(u"column_4_head")
        self.column_4_head.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.column_4_head, 0, 4, 1, 1)

        self.column_3_head = QLabel(self.groupBox)
        self.column_3_head.setObjectName(u"column_3_head")
        self.column_3_head.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.column_3_head, 0, 3, 1, 1)

        self.column_0_head = QLabel(self.groupBox)
        self.column_0_head.setObjectName(u"column_0_head")
        self.column_0_head.setMaximumSize(QSize(16777215, 50))

        self.function_selection_grid.addWidget(self.column_0_head, 0, 0, 1, 1)

        self.column_1_row_1 = QLabel(self.groupBox)
        self.column_1_row_1.setObjectName(u"column_1_row_1")
        self.column_1_row_1.setMaximumSize(QSize(16777215, 50))
        self.column_1_row_1.setFont(font1)

        self.function_selection_grid.addWidget(self.column_1_row_1, 1, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.function_selection_grid)

        self.gridLayout.addWidget(self.groupBox, 12, 1, 6, 16)

        self.horizontalSpacer_29 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_29, 0, 7, 1, 1)

        self.groupBox_5 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setFocusPolicy(Qt.NoFocus)
        self.groupBox_5.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.series_plot = QVBoxLayout()
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_7.addLayout(self.series_plot, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_5, 3, 8, 9, 9)

        self.verticalSpacer_25 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_25, 11, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_28, 0, 6, 1, 1)

        self.verticalSpacer_40 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_40, 4, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_24, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 20, 111, 41))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 20, 601, 42))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 2, 16)

        self.retranslateUi(SpecificAnalysisTab)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(SpecificAnalysisTab)

    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Experiment Hierarchie", None))
        ___qtreewidgetitem = self.selected_tree_widget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Discard", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selected_tab),
                                  QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None))
        ___qtreewidgetitem1 = self.discarded_tree_widget.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discarded_tab),
                                  QCoreApplication.translate("SpecificAnalysisTab", u"Discarded", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Function Selection", None))
        self.column_1_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Left Common Cursor", None))
        self.column_3_row_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"None", None))
        self.label_11.setText(QCoreApplication.translate("SpecificAnalysisTab", u"None", None))
        self.column_2_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Right Common Cursor", None))
        self.column_2_row_2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"None", None))
        self.select_series_analysis_functions.setText(
            QCoreApplication.translate("SpecificAnalysisTab", u"Add Function", None))
        self.column_4_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Right Sepcific Cursor", None))
        self.column_3_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Left Sepcific Cursor", None))
        self.column_0_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Function", None))
        self.column_1_row_1.setText(QCoreApplication.translate("SpecificAnalysisTab", u"None", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Filter Selection", None))
        self.pushButton_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add Filter", None))
        self.label_7.setText(QCoreApplication.translate("SpecificAnalysisTab", u"No Filter Selected", None))
    # retranslateUi


class SpecificAnalysisTab(QWidget, Ui_SpecificAnalysisTab):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)