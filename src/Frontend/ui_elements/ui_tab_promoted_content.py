# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_promoted_content.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_specific_analysis_tab(object):
    def setupUi(self, specific_analysis_tab):
        if not specific_analysis_tab.objectName():
            specific_analysis_tab.setObjectName(u"specific_analysis_tab")
        specific_analysis_tab.resize(926, 543)
        self.verticalLayoutWidget_2 = QWidget(specific_analysis_tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(310, 10, 611, 221))
        self.series_plot = QVBoxLayout(self.verticalLayoutWidget_2)
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget = QWidget(specific_analysis_tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(310, 260, 611, 251))
        self.function_selection_grid = QGridLayout(self.gridLayoutWidget)
        self.function_selection_grid.setObjectName(u"function_selection_grid")
        self.function_selection_grid.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(specific_analysis_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 20, 291, 491))
        self.selected_tab = QWidget()
        self.selected_tab.setObjectName(u"selected_tab")
        self.selected_tree_widget = QTreeWidget(self.selected_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.selected_tree_widget.setHeaderItem(__qtreewidgetitem)
        self.selected_tree_widget.setObjectName(u"selected_tree_widget")
        self.selected_tree_widget.setGeometry(QRect(0, 0, 281, 461))
        self.tabWidget.addTab(self.selected_tab, "")
        self.discarded_tab = QWidget()
        self.discarded_tab.setObjectName(u"discarded_tab")
        self.discarded_tree_widget = QTreeWidget(self.discarded_tab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.discarded_tree_widget.setHeaderItem(__qtreewidgetitem1)
        self.discarded_tree_widget.setObjectName(u"discarded_tree_widget")
        self.discarded_tree_widget.setGeometry(QRect(0, 0, 291, 461))
        self.tabWidget.addTab(self.discarded_tab, "")

        self.retranslateUi(specific_analysis_tab)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(specific_analysis_tab)
    # setupUi

    def retranslateUi(self, specific_analysis_tab):
        specific_analysis_tab.setWindowTitle(QCoreApplication.translate("specific_analysis_tab", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selected_tab), QCoreApplication.translate("specific_analysis_tab", u"Selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discarded_tab), QCoreApplication.translate("specific_analysis_tab", u"Discarded", None))
    # retranslateUi

