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
from QT_GUI.OfflineAnalysis.CustomWidget.analysis_function_table_designer import AnalysisFunctionTable

class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1131, 621)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout = QGridLayout(SpecificAnalysisTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.SpecialGrid = QGridLayout()
        self.SpecialGrid.setObjectName(u"SpecialGrid")
        self.groupBox_4 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(400, 450))
        self.groupBox_4.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.groupBox_4)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(200, 350))
        self.tabWidget.setMaximumSize(QSize(600, 16777215))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"border:0")
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.selected_tab.sizePolicy().hasHeightForWidth())
        self.selected_tab.setSizePolicy(sizePolicy1)
        self.selected_tab.setMinimumSize(QSize(300, 0))
        self.selected_tab.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_8 = QGridLayout(self.selected_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selected_tree_widget = QTreeWidget(self.selected_tab)
        font1 = QFont()
        font1.setPointSize(7)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(2, font1);
        __qtreewidgetitem.setFont(1, font1);
        __qtreewidgetitem.setFont(0, font1);
        self.selected_tree_widget.setHeaderItem(__qtreewidgetitem)
        self.selected_tree_widget.setObjectName(u"selected_tree_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selected_tree_widget.sizePolicy().hasHeightForWidth())
        self.selected_tree_widget.setSizePolicy(sizePolicy2)
        self.selected_tree_widget.setMinimumSize(QSize(6, 0))
        self.selected_tree_widget.setMaximumSize(QSize(600, 16777215))
        self.selected_tree_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.selected_tree_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.selected_tree_widget.setAnimated(True)
        self.selected_tree_widget.header().setMinimumSectionSize(50)
        self.selected_tree_widget.header().setHighlightSections(True)

        self.gridLayout_8.addWidget(self.selected_tree_widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.selected_tab, "")
        self.discarded_tab = QWidget()
        self.discarded_tab.setObjectName(u"discarded_tab")
        sizePolicy1.setHeightForWidth(self.discarded_tab.sizePolicy().hasHeightForWidth())
        self.discarded_tab.setSizePolicy(sizePolicy1)
        self.discarded_tab.setMinimumSize(QSize(600, 0))
        self.gridLayout_2 = QGridLayout(self.discarded_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.discarded_tree_widget = QTreeWidget(self.discarded_tab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setFont(3, font1);
        __qtreewidgetitem1.setFont(2, font1);
        __qtreewidgetitem1.setFont(1, font1);
        __qtreewidgetitem1.setFont(0, font1);
        self.discarded_tree_widget.setHeaderItem(__qtreewidgetitem1)
        self.discarded_tree_widget.setObjectName(u"discarded_tree_widget")
        sizePolicy.setHeightForWidth(self.discarded_tree_widget.sizePolicy().hasHeightForWidth())
        self.discarded_tree_widget.setSizePolicy(sizePolicy)
        self.discarded_tree_widget.setMinimumSize(QSize(300, 0))
        self.discarded_tree_widget.setMaximumSize(QSize(600, 16777215))
        self.discarded_tree_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.discarded_tree_widget.setAnimated(True)

        self.gridLayout_2.addWidget(self.discarded_tree_widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.discarded_tab, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.SpecialGrid.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_5 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.groupBox_5.setMinimumSize(QSize(300, 0))
        self.groupBox_5.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_5.setFocusPolicy(Qt.NoFocus)
        self.groupBox_5.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.series_analysis = QVBoxLayout()
        self.series_analysis.setObjectName(u"series_analysis")
        self.series_analysis.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget = QWidget(self.groupBox_5)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.gridLayout_11 = QGridLayout(self.widget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.series_plot = QGridLayout()
        self.series_plot.setObjectName(u"series_plot")

        self.gridLayout_11.addLayout(self.series_plot, 0, 0, 1, 1)


        self.series_analysis.addWidget(self.widget)


        self.gridLayout_7.addLayout(self.series_analysis, 1, 0, 1, 1)

        self.analysis_function = QGridLayout()
        self.analysis_function.setObjectName(u"analysis_function")

        self.gridLayout_7.addLayout(self.analysis_function, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.start_analysis_button = QPushButton(self.groupBox_5)
        self.start_analysis_button.setObjectName(u"start_analysis_button")
        self.start_analysis_button.setEnabled(False)
        self.start_analysis_button.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.start_analysis_button, 0, 4, 1, 1)

        self.select_series_analysis_functions = QPushButton(self.groupBox_5)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy5)
        self.select_series_analysis_functions.setMinimumSize(QSize(0, 30))
        self.select_series_analysis_functions.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.select_series_analysis_functions, 0, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy6)
        self.pushButton_3.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.spacer, 0, 0, 1, 1)

        self.turn_on_peak_detection = QRadioButton(self.groupBox_5)
        self.turn_on_peak_detection.setObjectName(u"turn_on_peak_detection")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.turn_on_peak_detection.sizePolicy().hasHeightForWidth())
        self.turn_on_peak_detection.setSizePolicy(sizePolicy7)
        self.turn_on_peak_detection.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.turn_on_peak_detection, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.SpecialGrid.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.SpecialGrid, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(SpecificAnalysisTab)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Experiment Hierarchie", None))
        ___qtreewidgetitem = self.selected_tree_widget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Discard", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Group", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selected_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None))
        ___qtreewidgetitem1 = self.discarded_tree_widget.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("SpecificAnalysisTab", u"Reinsert", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Group", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Sel", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discarded_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Discarded", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Choose Analysis Functions", None))
        self.pushButton_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Filter Data", None))
        self.turn_on_peak_detection.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Turn On Peak Detection", None))
    # retranslateUi




class SpecificAnalysisTab(QWidget, Ui_SpecificAnalysisTab):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        #add this to promote 
        self.analysis_table_widget = AnalysisFunctionTable()