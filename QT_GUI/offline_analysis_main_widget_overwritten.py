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


class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(961, 651)
        self.Offline_Analysis_Notebook = QTabWidget(Offline_Analysis)
        self.Offline_Analysis_Notebook.setObjectName(u"Offline_Analysis_Notebook")
        self.Offline_Analysis_Notebook.setGeometry(QRect(0, 0, 931, 621))
        self.Offline_Analysis_Notebook.setTabShape(QTabWidget.Rounded)
        self.Start_Analysis = QWidget()
        self.Start_Analysis.setObjectName(u"Start_Analysis")
        self.offline_analysis_widgets = QStackedWidget(self.Start_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setGeometry(QRect(0, 0, 931, 590))
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.new_analysis_with_template = QPushButton(self.start_page)
        self.new_analysis_with_template.setObjectName(u"new_analysis_with_template")
        self.new_analysis_with_template.setGeometry(QRect(180, 260, 181, 61))
        self.view_analysis_from_db = QPushButton(self.start_page)
        self.view_analysis_from_db.setObjectName(u"view_analysis_from_db")
        self.view_analysis_from_db.setGeometry(QRect(180, 330, 181, 61))
        self.start_label = QLabel(self.start_page)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setGeometry(QRect(320, 100, 251, 41))
        font = QFont()
        font.setPointSize(20)
        self.start_label.setFont(font)
        self.blank_analysis_button = QPushButton(self.start_page)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setGeometry(QRect(180, 190, 181, 61))
        self.user_feedback_label = QLabel(self.start_page)
        self.user_feedback_label.setObjectName(u"user_feedback_label")
        self.user_feedback_label.setGeometry(QRect(440, 190, 321, 201))
        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.compare_series = QPushButton(self.blank_analysis)
        self.compare_series.setObjectName(u"compare_series")
        self.compare_series.setGeometry(QRect(70, 530, 811, 41))
        self.widget_sepcific_label = QLabel(self.blank_analysis)
        self.widget_sepcific_label.setObjectName(u"widget_sepcific_label")
        self.widget_sepcific_label.setGeometry(QRect(310, 40, 361, 41))
        self.widget_sepcific_label.setFont(font)
        self.select_directory_button = QPushButton(self.blank_analysis)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setGeometry(QRect(70, 90, 93, 28))
        self.selected_directory = QLabel(self.blank_analysis)
        self.selected_directory.setObjectName(u"selected_directory")
        self.selected_directory.setGeometry(QRect(180, 90, 131, 21))
        self.experiments_tree_view = QTreeWidget(self.blank_analysis)
        self.experiments_tree_view.setObjectName(u"experiments_tree_view")
        self.experiments_tree_view.setGeometry(QRect(70, 130, 271, 261))
        self.outfiltered_tree_view = QTreeWidget(self.blank_analysis)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Objects");
        self.outfiltered_tree_view.setHeaderItem(__qtreewidgetitem)
        self.outfiltered_tree_view.setObjectName(u"outfiltered_tree_view")
        self.outfiltered_tree_view.setGeometry(QRect(70, 400, 271, 111))
        self.verticalLayoutWidget = QWidget(self.blank_analysis)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(390, 130, 471, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.Offline_Analysis_Notebook.addTab(self.Start_Analysis, "")
        self.visualization = QWidget()
        self.visualization.setObjectName(u"visualization")
        self.Offline_Analysis_Notebook.addTab(self.visualization, "")

        self.retranslateUi(Offline_Analysis)

        self.Offline_Analysis_Notebook.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(1)


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
        ___qtreewidgetitem = self.experiments_tree_view.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Offline_Analysis", u"Remove", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Offline_Analysis", u"Objects", None));
        ___qtreewidgetitem1 = self.outfiltered_tree_view.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Offline_Analysis", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Offline_Analysis", u"Show", None));
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.Start_Analysis), QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.Offline_Analysis_Notebook.setTabText(self.Offline_Analysis_Notebook.indexOf(self.visualization), QCoreApplication.translate("Offline_Analysis", u"Visualization", None))
    # retranslateUi

