# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_main_widget_layouted.ui'
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
        Offline_Analysis.resize(1063, 721)
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
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        sizePolicy.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.start_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.view_analysis_from_db = QPushButton(self.start_page)
        self.view_analysis_from_db.setObjectName(u"view_analysis_from_db")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_analysis_from_db.sizePolicy().hasHeightForWidth())
        self.view_analysis_from_db.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.view_analysis_from_db, 4, 1, 1, 1)

        self.label_3 = QLabel(self.start_page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_3, 4, 3, 1, 1)

        self.user_feedback_label = QLabel(self.start_page)
        self.user_feedback_label.setObjectName(u"user_feedback_label")
        sizePolicy1.setHeightForWidth(self.user_feedback_label.sizePolicy().hasHeightForWidth())
        self.user_feedback_label.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.user_feedback_label, 1, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_12, 3, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.start_label = QLabel(self.start_page)
        self.start_label.setObjectName(u"start_label")
        sizePolicy1.setHeightForWidth(self.start_label.sizePolicy().hasHeightForWidth())
        self.start_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.start_label.setFont(font)
        self.start_label.setScaledContents(False)

        self.gridLayout_4.addWidget(self.start_label, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 4, 5, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 4, 2, 1, 1)

        self.blank_analysis_button = QPushButton(self.start_page)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        sizePolicy1.setHeightForWidth(self.blank_analysis_button.sizePolicy().hasHeightForWidth())
        self.blank_analysis_button.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.blank_analysis_button, 1, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 3, 5, 1, 1)

        self.label_2 = QLabel(self.start_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_2, 3, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.new_analysis_with_template = QPushButton(self.start_page)
        self.new_analysis_with_template.setObjectName(u"new_analysis_with_template")
        sizePolicy1.setHeightForWidth(self.new_analysis_with_template.sizePolicy().hasHeightForWidth())
        self.new_analysis_with_template.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.new_analysis_with_template, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.gridLayout_5 = QGridLayout(self.blank_analysis)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.select_directory_button = QPushButton(self.blank_analysis)
        self.select_directory_button.setObjectName(u"select_directory_button")

        self.gridLayout_5.addWidget(self.select_directory_button, 1, 0, 1, 1)

        self.selected_directory = QLabel(self.blank_analysis)
        self.selected_directory.setObjectName(u"selected_directory")

        self.gridLayout_5.addWidget(self.selected_directory, 1, 1, 1, 3)

        self.filter_box = QGroupBox(self.blank_analysis)
        self.filter_box.setObjectName(u"filter_box")
        self.verticalLayout_2 = QVBoxLayout(self.filter_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_2 = QTabWidget(self.filter_box)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_10 = QGridLayout(self.tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_10.addWidget(self.pushButton, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)


        self.gridLayout_5.addWidget(self.filter_box, 2, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.blank_analysis)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 3, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_5.addLayout(self.verticalLayout, 3, 3, 2, 1)

        self.pushButton_3 = QPushButton(self.blank_analysis)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.compare_series = QPushButton(self.blank_analysis)
        self.compare_series.setObjectName(u"compare_series")

        self.gridLayout_5.addWidget(self.compare_series, 5, 2, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_4 = QPushButton(self.blank_analysis)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.blank_analysis)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.blank_analysis)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 6, 3, 1, 1)

        self.directory_tree_widget = QTabWidget(self.blank_analysis)
        self.directory_tree_widget.setObjectName(u"directory_tree_widget")
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.gridLayout_7 = QGridLayout(self.selected_tree_view)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.experiments_tree_view = QTreeWidget(self.selected_tree_view)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")

        self.gridLayout_7.addWidget(self.experiments_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.selected_tree_view, "")
        self.discarded_tree_view = QWidget()
        self.discarded_tree_view.setObjectName(u"discarded_tree_view")
        self.gridLayout_8 = QGridLayout(self.discarded_tree_view)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.outfiltered_tree_view = QTreeWidget(self.discarded_tree_view)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Objects");
        self.outfiltered_tree_view.setHeaderItem(__qtreewidgetitem)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")

        self.gridLayout_8.addWidget(self.outfiltered_tree_view, 0, 0, 1, 1)

        self.directory_tree_widget.addTab(self.discarded_tree_view, "")

        self.gridLayout_5.addWidget(self.directory_tree_widget, 3, 0, 4, 2)

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

        self.widget_sepcific_label = QLabel(self.Start_Analysis)
        self.widget_sepcific_label.setObjectName(u"widget_sepcific_label")
        self.widget_sepcific_label.setFont(font)
        self.widget_sepcific_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.widget_sepcific_label, 0, 0, 1, 1)

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
        self.offline_analysis_widgets.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.directory_tree_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.view_analysis_from_db.setText(QCoreApplication.translate("Offline_Analysis", u"View Analysis From Database", None))
        self.label_3.setText(QCoreApplication.translate("Offline_Analysis", u" View Visualizations of preovious analysis. \n"
" It's a read only mode - You can not modify the analysis", None))
        self.user_feedback_label.setText(QCoreApplication.translate("Offline_Analysis", u" Configure a new analysis from the scratch. \n"
" Define filter settings to discard in an automated manner, \n"
" select and discard experiments manually, \n"
" set up analysis function and specify regions of interest. ", None))
        self.start_label.setText(QCoreApplication.translate("Offline_Analysis", u"SELECT ", None))
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"New Blank Analysis", None))
        self.label_2.setText(QCoreApplication.translate("Offline_Analysis", u" Simply apply previous analysis settings to new experiment files.\n"
" Additional changes are possible too", None))
        self.new_analysis_with_template.setText(QCoreApplication.translate("Offline_Analysis", u"New Analysis using previous analysis as template", None))
        self.select_directory_button.setText(QCoreApplication.translate("Offline_Analysis", u"Select Directory", None))
        self.selected_directory.setText(QCoreApplication.translate("Offline_Analysis", u"TextLabel", None))
        self.filter_box.setTitle(QCoreApplication.translate("Offline_Analysis", u"Selected Filter", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"No filter selected", None))
        self.pushButton.setText(QCoreApplication.translate("Offline_Analysis", u"Add Filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("Offline_Analysis", u"Add Filter", None))
        self.pushButton_2.setText(QCoreApplication.translate("Offline_Analysis", u"Hold", None))
        self.pushButton_3.setText(QCoreApplication.translate("Offline_Analysis", u"Clear", None))
        self.compare_series.setText(QCoreApplication.translate("Offline_Analysis", u"Select Series To Be Analyzed", None))
        self.pushButton_4.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Offline_Analysis", u"PushButton", None))
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Offline_Analysis", u"Remove", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Offline_Analysis", u"Objects", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Offline_Analysis", u"Selected", None))
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Offline_Analysis", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        self.directory_tree_widget.setTabText(self.directory_tree_widget.indexOf(self.discarded_tree_view), QCoreApplication.translate("Offline_Analysis", u"Discarded", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.template_tab), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        self.widget_sepcific_label.setText(QCoreApplication.translate("Offline_Analysis", u"CONFIGURE YOUR OFFLINE ANALYSIS", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.Start_Analysis), QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.visualization_tab_widget.setTabText(self.visualization_tab_widget.indexOf(self.template_tab_2), QCoreApplication.translate("Offline_Analysis", u"Tab 1", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.visualization), QCoreApplication.translate("Offline_Analysis", u"Visualization", None))
    # retranslateUi

