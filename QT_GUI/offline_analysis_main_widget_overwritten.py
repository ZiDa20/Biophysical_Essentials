# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_main_widget.ui'
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
        Offline_Analysis.resize(1286, 943)
        self.Offline_Analysis_Notebook = QTabWidget(Offline_Analysis)
        self.Offline_Analysis_Notebook.setObjectName(u"Offline_Analysis_Notebook")
        self.Offline_Analysis_Notebook.setGeometry(QRect(0, 0, 1281, 881))
        self.Offline_Analysis_Notebook.setTabShape(QTabWidget.Rounded)
        self.Start_Analysis = QWidget()
        self.Start_Analysis.setObjectName(u"Start_Analysis")
        self.offline_analysis_widgets = QStackedWidget(self.Start_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setGeometry(QRect(0, 0, 1271, 851))
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.new_analysis_with_template = QPushButton(self.start_page)
        self.new_analysis_with_template.setObjectName(u"new_analysis_with_template")
        self.new_analysis_with_template.setGeometry(QRect(300, 330, 181, 61))
        self.view_analysis_from_db = QPushButton(self.start_page)
        self.view_analysis_from_db.setObjectName(u"view_analysis_from_db")
        self.view_analysis_from_db.setGeometry(QRect(300, 400, 181, 61))
        self.start_label = QLabel(self.start_page)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setGeometry(QRect(440, 170, 251, 41))
        font = QFont()
        font.setPointSize(20)
        self.start_label.setFont(font)
        self.blank_analysis_button = QPushButton(self.start_page)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setGeometry(QRect(300, 260, 181, 61))
        self.user_feedback_label = QLabel(self.start_page)
        self.user_feedback_label.setObjectName(u"user_feedback_label")
        self.user_feedback_label.setGeometry(QRect(560, 260, 321, 201))
        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.compare_series = QPushButton(self.blank_analysis)
        self.compare_series.setObjectName(u"compare_series")
        self.compare_series.setGeometry(QRect(430, 750, 771, 41))
        self.widget_sepcific_label = QLabel(self.blank_analysis)
        self.widget_sepcific_label.setObjectName(u"widget_sepcific_label")
        self.widget_sepcific_label.setGeometry(QRect(490, 50, 361, 41))
        self.widget_sepcific_label.setFont(font)
        self.select_directory_button = QPushButton(self.blank_analysis)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setGeometry(QRect(90, 110, 121, 31))
        self.selected_directory = QLabel(self.blank_analysis)
        self.selected_directory.setObjectName(u"selected_directory")
        self.selected_directory.setGeometry(QRect(240, 110, 581, 21))
        self.verticalLayoutWidget = QWidget(self.blank_analysis)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(570, 250, 631, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget = QWidget(self.blank_analysis)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 160, 1111, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.blank_analysis)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(90, 220, 301, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.experiments_tree_view = QTreeWidget(self.tab)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")
        self.experiments_tree_view.setGeometry(QRect(0, 0, 301, 551))
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.outfiltered_tree_view = QTreeWidget(self.tab_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Objects");
        self.outfiltered_tree_view.setHeaderItem(__qtreewidgetitem)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")
        self.outfiltered_tree_view.setGeometry(QRect(0, 0, 301, 541))
        self.tabWidget_3.addTab(self.tab_2, "")
        self.pushButton_2 = QPushButton(self.blank_analysis)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 250, 75, 51))
        self.pushButton_3 = QPushButton(self.blank_analysis)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(420, 330, 75, 51))
        self.gridLayoutWidget_2 = QWidget(self.blank_analysis)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(440, 810, 239, 41))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.analysis_specific_notebook = QWidget()
        self.analysis_specific_notebook.setObjectName(u"analysis_specific_notebook")
        self.tabWidget = QTabWidget(self.analysis_specific_notebook)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1271, 851))
        self.template_tab = SpecificAnalysisTab()
        self.template_tab.setObjectName(u"template_tab")
        self.tabWidget.addTab(self.template_tab, "")
        self.offline_analysis_widgets.addWidget(self.analysis_specific_notebook)
        self.Offline_Analysis_Notebook.addTab(self.Start_Analysis, "")
        self.visualization = QWidget()
        self.visualization.setObjectName(u"visualization")
        self.Offline_Analysis_Notebook.addTab(self.visualization, "")

        self.retranslateUi(Offline_Analysis)

        self.Offline_Analysis_Notebook.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.new_analysis_with_template.setText(QCoreApplication.translate("Offline_Analysis", u"New Analysis using \n"
" previous analysis as template", None))
        self.view_analysis_from_db.setText(QCoreApplication.translate("Offline_Analysis", u"View Analysis From Database", None))
        self.start_label.setText(QCoreApplication.translate("Offline_Analysis", u"Select your Analysis", None))
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"New Blank Analysis", None))
        self.user_feedback_label.setText(QCoreApplication.translate("Offline_Analysis", u"Further Information about your selected analysis", None))
        self.compare_series.setText(QCoreApplication.translate("Offline_Analysis", u"Select Series To Be Analyzed", None))
        self.widget_sepcific_label.setText(QCoreApplication.translate("Offline_Analysis", u"Configure your Analysis", None))
        self.select_directory_button.setText(QCoreApplication.translate("Offline_Analysis", u"Select Directory", None))
        self.selected_directory.setText(QCoreApplication.translate("Offline_Analysis", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Offline_Analysis", u"Add New Filter", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"No filter selected", None))
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Offline_Analysis", u"Remove", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Offline_Analysis", u"Objects", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Offline_Analysis", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("Offline_Analysis", u"Tab 2", None))
        self.pushButton_2.setText(QCoreApplication.translate("Offline_Analysis", u"Hold", None))
        self.pushButton_3.setText(QCoreApplication.translate("Offline_Analysis", u"Clear", None))
        self.pushButton_4.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.template_tab), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.Start_Analysis), QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.visualization), QCoreApplication.translate("Offline_Analysis", u"Visualization", None))
    # retranslateUi
