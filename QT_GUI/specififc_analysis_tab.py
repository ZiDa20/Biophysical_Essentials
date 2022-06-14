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
        SpecificAnalysisTab.resize(1183, 854)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout = QGridLayout(SpecificAnalysisTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_40 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_40, 5, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_24, 10, 0, 1, 1)

        self.select_series_analysis_functions = QPushButton(SpecificAnalysisTab)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.select_series_analysis_functions, 7, 11, 1, 1)

        self.verticalSpacer_37 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_37, 15, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_33, 0, 18, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_35, 16, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_27, 0, 2, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_28, 0, 6, 1, 1)

        self.groupBox = QGroupBox(SpecificAnalysisTab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMaximumSize(QSize(16777215, 500))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.analysis_table_widget = QTableWidget(self.groupBox)
        if (self.analysis_table_widget.columnCount() < 5):
            self.analysis_table_widget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.analysis_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.analysis_table_widget.setObjectName(u"analysis_table_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.analysis_table_widget.sizePolicy().hasHeightForWidth())
        self.analysis_table_widget.setSizePolicy(sizePolicy2)
        self.analysis_table_widget.horizontalHeader().setVisible(True)
        self.analysis_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.analysis_table_widget.horizontalHeader().setDefaultSectionSize(125)
        self.analysis_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.analysis_table_widget.horizontalHeader().setStretchLastSection(False)
        self.analysis_table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.analysis_table_widget)


        self.gridLayout.addWidget(self.groupBox, 1, 11, 6, 8)

        self.horizontalSpacer_18 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_18, 0, 15, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 9, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_41, 2, 0, 1, 1)

        self.verticalSpacer_39 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_39, 6, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_20, 0, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_21, 0, 12, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_22, 1, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_33, 11, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_30, 0, 11, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_34, 0, 5, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_19, 0, 13, 1, 1)

        self.go_back_tp_page_2 = QPushButton(SpecificAnalysisTab)
        self.go_back_tp_page_2.setObjectName(u"go_back_tp_page_2")

        self.gridLayout.addWidget(self.go_back_tp_page_2, 18, 4, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_23, 7, 0, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_28, 13, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_24, 0, 1, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_30, 8, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_32, 9, 0, 1, 1)

        self.groupBox_4 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.groupBox_4.setMinimumSize(QSize(300, 450))
        self.groupBox_4.setMaximumSize(QSize(600, 16777215))
        self.tabWidget = QTabWidget(self.groupBox_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 26, 411, 631))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setMinimumSize(QSize(0, 350))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"border:0")
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        self.gridLayout_8 = QGridLayout(self.selected_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selected_tree_widget = QTreeWidget(self.selected_tab)
        self.selected_tree_widget.setObjectName(u"selected_tree_widget")
        sizePolicy4.setHeightForWidth(self.selected_tree_widget.sizePolicy().hasHeightForWidth())
        self.selected_tree_widget.setSizePolicy(sizePolicy4)

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

        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 14, 9)

        self.verticalSpacer_38 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_38, 4, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_26, 0, 14, 1, 1)

        self.start_analysis_button = QPushButton(SpecificAnalysisTab)
        self.start_analysis_button.setObjectName(u"start_analysis_button")
        self.start_analysis_button.setEnabled(False)

        self.gridLayout.addWidget(self.start_analysis_button, 7, 16, 1, 3)

        self.horizontalSpacer_29 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_29, 0, 7, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_22, 0, 17, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_32, 0, 16, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_36, 17, 0, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_34, 14, 0, 1, 1)

        self.groupBox_5 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setFocusPolicy(Qt.NoFocus)
        self.groupBox_5.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.series_plot = QVBoxLayout()
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_7.addLayout(self.series_plot, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 8, 11, 11, 8)

        self.verticalSpacer_26 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_26, 18, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_25, 0, 4, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_29, 0, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 42, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_25, 12, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 8, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 10, 1, 1)

        self.groupBox_3 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 40, 111, 41))
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 40, 261, 42))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 3, 9)


        self.retranslateUi(SpecificAnalysisTab)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add New Analysis Functions(s)", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Function Selection", None))
        ___qtablewidgetitem = self.analysis_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Functions", None));
        ___qtablewidgetitem1 = self.analysis_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Left Boundary", None));
        ___qtablewidgetitem2 = self.analysis_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Right Boundary", None));
        ___qtablewidgetitem3 = self.analysis_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Configuration", None));
        self.go_back_tp_page_2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Go Back", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Experiment Hierarchie", None))
        ___qtreewidgetitem = self.selected_tree_widget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("SpecificAnalysisTab", u"Discard", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Group", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Sel", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selected_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None))
        ___qtreewidgetitem1 = self.discarded_tree_widget.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("SpecificAnalysisTab", u"Reinsert", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Group", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Sel", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discarded_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Discarded", None))
        self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Filter Selection", None))
        self.pushButton_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add Filter", None))
        self.label_7.setText(QCoreApplication.translate("SpecificAnalysisTab", u"No Filter Selected", None))
    # retranslateUi

class SpecificAnalysisTab(QWidget, Ui_SpecificAnalysisTab):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)