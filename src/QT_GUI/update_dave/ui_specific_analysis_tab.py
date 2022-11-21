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
        SpecificAnalysisTab.resize(1591, 944)
        self.tabWidget = QTabWidget(SpecificAnalysisTab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 100, 291, 691))
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        self.selected_tree_widget = QTreeWidget(self.selected_tab)
        self.selected_tree_widget.setObjectName(u"selected_tree_widget")
        self.selected_tree_widget.setGeometry(QRect(0, 0, 281, 671))
        self.tabWidget.addTab(self.selected_tab, "")
        self.discarded_tab = QWidget()
        self.discarded_tab.setObjectName(u"discarded_tab")
        self.discarded_tree_widget = QTreeWidget(self.discarded_tab)
        self.discarded_tree_widget.setObjectName(u"discarded_tree_widget")
        self.discarded_tree_widget.setGeometry(QRect(0, 0, 291, 661))
        self.tabWidget.addTab(self.discarded_tab, "")
        self.gridLayoutWidget_3 = QWidget(SpecificAnalysisTab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 800, 239, 41))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.groupBox = QGroupBox(SpecificAnalysisTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(360, 430, 1111, 421))
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 40, 1101, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1099, 369))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(130, 0, 971, 291))
        self.function_selection_grid = QGridLayout(self.gridLayoutWidget)
        self.function_selection_grid.setObjectName(u"function_selection_grid")
        self.function_selection_grid.setContentsMargins(0, 0, 0, 0)
        self.coloumn_3_row_3 = QLabel(self.gridLayoutWidget)
        self.coloumn_3_row_3.setObjectName(u"coloumn_3_row_3")
        self.coloumn_3_row_3.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.coloumn_3_row_3, 5, 3, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.label, 4, 2, 1, 1)

        self.coloumn_1_row_1 = QLabel(self.gridLayoutWidget)
        self.coloumn_1_row_1.setObjectName(u"coloumn_1_row_1")
        self.coloumn_1_row_1.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.coloumn_1_row_1, 5, 0, 1, 1)

        self.coloumn_3_head = QLabel(self.gridLayoutWidget)
        self.coloumn_3_head.setObjectName(u"coloumn_3_head")
        self.coloumn_3_head.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.coloumn_3_head, 4, 3, 1, 1)

        self.coloumn_2_row_2 = QLabel(self.gridLayoutWidget)
        self.coloumn_2_row_2.setObjectName(u"coloumn_2_row_2")
        self.coloumn_2_row_2.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.coloumn_2_row_2, 5, 1, 1, 1)

        self.select_series_analysis_functions = QPushButton(self.gridLayoutWidget)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")

        self.function_selection_grid.addWidget(self.select_series_analysis_functions, 6, 0, 1, 4)

        self.headline = QLabel(self.gridLayoutWidget)
        self.headline.setObjectName(u"headline")
        self.headline.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.headline, 3, 1, 1, 2)

        self.coloumn_2_head = QLabel(self.gridLayoutWidget)
        self.coloumn_2_head.setObjectName(u"coloumn_2_head")
        self.coloumn_2_head.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.coloumn_2_head, 4, 1, 1, 1)

        self.coloumn_1_head = QLabel(self.gridLayoutWidget)
        self.coloumn_1_head.setObjectName(u"coloumn_1_head")
        self.coloumn_1_head.setAlignment(Qt.AlignCenter)
        self.coloumn_1_head.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.function_selection_grid.addWidget(self.coloumn_1_head, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.function_selection_grid.addWidget(self.label_2, 5, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(360, 100, 1101, 311))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(100, 30, 1001, 271))
        self.series_plot = QVBoxLayout(self.verticalLayoutWidget_2)
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 40, 71, 51))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 120, 71, 51))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 200, 71, 51))
        self.filter_box = QGroupBox(SpecificAnalysisTab)
        self.filter_box.setObjectName(u"filter_box")
        self.filter_box.setGeometry(QRect(20, 20, 1441, 41))
        self.tabWidget_2 = QTabWidget(self.filter_box)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(30, 20, 731, 80))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 20, 111, 16))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(270, 20, 171, 23))
        self.tabWidget_2.addTab(self.tab, "")

        self.retranslateUi(SpecificAnalysisTab)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        ___qtreewidgetitem = self.selected_tree_widget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Move", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selected_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Selected", None))
        ___qtreewidgetitem1 = self.discarded_tree_widget.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("SpecificAnalysisTab", u"Move", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("SpecificAnalysisTab", u"Show", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("SpecificAnalysisTab", u"Object", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discarded_tab), QCoreApplication.translate("SpecificAnalysisTab", u"Discarded", None))
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Function Settings", None))
        self.coloumn_3_row_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-style:italic;\">None</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Right Boundary</span></p></body></html>", None))
        self.coloumn_1_row_1.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-style:italic;\">None</span></p></body></html>", None))
        self.coloumn_3_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Specific Analaysis <br/>Intervall</span></p></body></html>", None))
        self.coloumn_2_row_2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-style:italic;\">None</span></p></body></html>", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Select Analaysis Functions", None))
        self.headline.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.coloumn_2_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Left Boundary</span></p></body></html>", None))
        self.coloumn_1_head.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Analysis Function</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"<html><head/><body><p><span style=\" font-style:italic;\">None</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Signal Traces", None))
        self.pushButton_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Center", None))
        self.pushButton.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Hold", None))
        self.pushButton_2.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Clear", None))
        self.filter_box.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Selected Filter", None))
        self.label_3.setText(QCoreApplication.translate("SpecificAnalysisTab", u"No filter selected", None))
        self.pushButton_4.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add Filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("SpecificAnalysisTab", u"Add Filter", None))
    # retranslateUi

