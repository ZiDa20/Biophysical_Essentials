# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_mz_layouted.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from treebuild_widget import TreeBuild

class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(1678, 966)
        self.gridLayout_13 = QGridLayout(Offline_Analysis)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.offline_analysis_widgets = QStackedWidget(Offline_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offline_analysis_widgets.sizePolicy().hasHeightForWidth())
        self.offline_analysis_widgets.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.offline_analysis_widgets.setFont(font)
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy1)
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
        self.open_analysis_results_button = QPushButton(self.groupBox)
        self.open_analysis_results_button.setObjectName(u"open_analysis_results_button")
        self.open_analysis_results_button.setGeometry(QRect(40, 280, 161, 41))
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
        self.widget_2 = QWidget(self.blank_analysis)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_2.addWidget(self.widget_2, 1, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.treebuild = TreeBuild(self.blank_analysis)
        self.treebuild.setObjectName(u"treebuild")
        sizePolicy.setHeightForWidth(self.treebuild.sizePolicy().hasHeightForWidth())
        self.treebuild.setSizePolicy(sizePolicy)
        self.treebuild.setMinimumSize(QSize(400, 0))
        self.treebuild.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_14.addWidget(self.treebuild, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.blank_analysis)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.toolbar_layout = QGridLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_widget = QWidget(self.groupBox_5)
        self.toolbar_widget.setObjectName(u"toolbar_widget")
        self.toolbar_widget.setMinimumSize(QSize(50, 0))
        self.toolbar_widget.setMaximumSize(QSize(50, 16777215))

        self.toolbar_layout.addWidget(self.toolbar_widget, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.toolbar_layout, 2, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.groupBox_5)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.canvas_grid_layout = QGridLayout()
        self.canvas_grid_layout.setObjectName(u"canvas_grid_layout")

        self.gridLayout_12.addLayout(self.canvas_grid_layout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout_7.addLayout(self.verticalLayout, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.blank_analysis)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.add_filter_button = QPushButton(self.groupBox_3)
        self.add_filter_button.setObjectName(u"add_filter_button")

        self.gridLayout_8.addWidget(self.add_filter_button, 0, 7, 1, 1)

        self.compare_series = QPushButton(self.groupBox_3)
        self.compare_series.setObjectName(u"compare_series")

        self.gridLayout_8.addWidget(self.compare_series, 0, 9, 1, 1)

        self.load_meta_data = QPushButton(self.groupBox_3)
        self.load_meta_data.setObjectName(u"load_meta_data")

        self.gridLayout_8.addWidget(self.load_meta_data, 0, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_18, 0, 5, 1, 1)

        self.load_from_database = QPushButton(self.groupBox_3)
        self.load_from_database.setObjectName(u"load_from_database")
        self.load_from_database.setMinimumSize(QSize(100, 0))

        self.gridLayout_8.addWidget(self.load_from_database, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 6, 1, 1)

        self.go_back_button = QPushButton(self.groupBox_3)
        self.go_back_button.setObjectName(u"go_back_button")

        self.gridLayout_8.addWidget(self.go_back_button, 0, 4, 1, 1)

        self.select_directory_button = QPushButton(self.groupBox_3)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setMinimumSize(QSize(100, 0))

        self.gridLayout_8.addWidget(self.select_directory_button, 0, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_8)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.analysis_specific_notebook = QWidget()
        self.analysis_specific_notebook.setObjectName(u"analysis_specific_notebook")
        self.gridLayout_6 = QGridLayout(self.analysis_specific_notebook)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.BackButtonGrid = QHBoxLayout()
        self.BackButtonGrid.setObjectName(u"BackButtonGrid")
        self.series_selection = QPushButton(self.analysis_specific_notebook)
        self.series_selection.setObjectName(u"series_selection")

        self.BackButtonGrid.addWidget(self.series_selection)

        self.new_analysis = QPushButton(self.analysis_specific_notebook)
        self.new_analysis.setObjectName(u"new_analysis")

        self.BackButtonGrid.addWidget(self.new_analysis)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.BackButtonGrid.addItem(self.horizontalSpacer_36)


        self.gridLayout_3.addLayout(self.BackButtonGrid, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.SeriesItems = QTreeWidget(self.analysis_specific_notebook)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.SeriesItems.setHeaderItem(__qtreewidgetitem)
        self.SeriesItems.setObjectName(u"SeriesItems")
        self.SeriesItems.setMinimumSize(QSize(300, 0))
        self.SeriesItems.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.SeriesItems, 0, 0, 1, 1)

        self.PlotItem = QWidget(self.analysis_specific_notebook)
        self.PlotItem.setObjectName(u"PlotItem")
        sizePolicy1.setHeightForWidth(self.PlotItem.sizePolicy().hasHeightForWidth())
        self.PlotItem.setSizePolicy(sizePolicy1)
        self.PlotItem.setMinimumSize(QSize(800, 0))
        self.gridLayout_11 = QGridLayout(self.PlotItem)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.WidgetAnalysis = QGridLayout()
        self.WidgetAnalysis.setObjectName(u"WidgetAnalysis")

        self.gridLayout_11.addLayout(self.WidgetAnalysis, 1, 0, 1, 1)

        self.toolbar_layout_2 = QGridLayout()
        self.toolbar_layout_2.setObjectName(u"toolbar_layout_2")
        self.toolbar_widget_2 = QWidget(self.PlotItem)
        self.toolbar_widget_2.setObjectName(u"toolbar_widget_2")
        self.toolbar_widget_2.setMinimumSize(QSize(50, 0))
        self.toolbar_widget_2.setMaximumSize(QSize(50, 16777215))

        self.toolbar_layout_2.addWidget(self.toolbar_widget_2, 0, 0, 1, 1)


        self.gridLayout_11.addLayout(self.toolbar_layout_2, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.PlotItem, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.analysis_specific_notebook)

        self.gridLayout_13.addWidget(self.offline_analysis_widgets, 2, 0, 1, 1)


        self.retranslateUi(Offline_Analysis)

        self.offline_analysis_widgets.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Offline_Analysis", u"Offline Analysis Options", None))
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"Blank Analysis", None))
        self.pushButton_8.setText(QCoreApplication.translate("Offline_Analysis", u"Analysis from \n"
" previous Analysis", None))
        self.open_analysis_results_button.setText(QCoreApplication.translate("Offline_Analysis", u"Open Analysis Results", None))
        self.label_3.setText(QCoreApplication.translate("Offline_Analysis", u"Start a new analysis from the scratch !", None))
        self.label_4.setText(QCoreApplication.translate("Offline_Analysis", u"Use an existing analysis from the database \n"
"and modify paramters for a new analysis !", None))
        self.label_5.setText(QCoreApplication.translate("Offline_Analysis", u"Opens the visualization of results of \n"
"already succesfully performed analysis", None))
        self.label_2.setText(QCoreApplication.translate("Offline_Analysis", u"SELECT A SPECIFIC OFFLINE ANALYSIS", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data View", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Offline_Analysis", u"Analysis ToolBar", None))
        self.add_filter_button.setText(QCoreApplication.translate("Offline_Analysis", u"Add Filter", None))
        self.compare_series.setText(QCoreApplication.translate("Offline_Analysis", u"SELECT SERIES TO BE ANALYZED", None))
        self.load_meta_data.setText(QCoreApplication.translate("Offline_Analysis", u"Load MetaData", None))
        self.load_from_database.setText(QCoreApplication.translate("Offline_Analysis", u"Load Database", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"Analysis Options:", None))
        self.go_back_button.setText(QCoreApplication.translate("Offline_Analysis", u"Go Back", None))
        self.select_directory_button.setText(QCoreApplication.translate("Offline_Analysis", u"Load Directory", None))
        self.label_6.setText(QCoreApplication.translate("Offline_Analysis", u"Load Data Options: ", None))
        self.series_selection.setText(QCoreApplication.translate("Offline_Analysis", u"Series Selection", None))
        self.new_analysis.setText(QCoreApplication.translate("Offline_Analysis", u"New Analysis", None))
    # retranslateUi

