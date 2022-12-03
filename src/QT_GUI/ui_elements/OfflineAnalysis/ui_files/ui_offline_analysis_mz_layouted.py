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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QTreeView, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from treebuild_widget import TreeBuild

class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(1144, 806)
        self.gridLayout_21 = QGridLayout(Offline_Analysis)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame = QFrame(Offline_Analysis)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)

        self.gridLayout_22.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.go_back_button = QPushButton(self.frame)
        self.go_back_button.setObjectName(u"go_back_button")
        self.go_back_button.setMinimumSize(QSize(40, 40))
        self.go_back_button.setMaximumSize(QSize(50, 503))
        self.go_back_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/back.png);")

        self.gridLayout_30.addWidget(self.go_back_button, 0, 0, 1, 1)

        self.fo_forward_button = QPushButton(self.frame)
        self.fo_forward_button.setObjectName(u"fo_forward_button")
        self.fo_forward_button.setMinimumSize(QSize(40, 40))
        self.fo_forward_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/forward.png);")

        self.gridLayout_30.addWidget(self.fo_forward_button, 0, 1, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_30, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_22)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.AnalysisOptions = QGroupBox(self.frame)
        self.AnalysisOptions.setObjectName(u"AnalysisOptions")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnalysisOptions.sizePolicy().hasHeightForWidth())
        self.AnalysisOptions.setSizePolicy(sizePolicy)
        self.AnalysisOptions.setMinimumSize(QSize(200, 0))
        self.AnalysisOptions.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_8 = QGridLayout(self.AnalysisOptions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_8 = QPushButton(self.AnalysisOptions)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_5.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.blank_analysis_button = QPushButton(self.AnalysisOptions)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setFont(font)

        self.gridLayout_5.addWidget(self.blank_analysis_button, 0, 0, 1, 1)

        self.open_analysis_results_button = QPushButton(self.AnalysisOptions)
        self.open_analysis_results_button.setObjectName(u"open_analysis_results_button")

        self.gridLayout_5.addWidget(self.open_analysis_results_button, 2, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.AnalysisOptions)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.DataGroup = QGroupBox(self.frame)
        self.DataGroup.setObjectName(u"DataGroup")
        self.gridLayout_15 = QGridLayout(self.DataGroup)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.load_from_database = QPushButton(self.DataGroup)
        self.load_from_database.setObjectName(u"load_from_database")
        self.load_from_database.setMinimumSize(QSize(30, 30))
        self.load_from_database.setMaximumSize(QSize(30, 30))
        self.load_from_database.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/load_database.png);")

        self.DataOptions.addWidget(self.load_from_database, 0, 2, 1, 1)

        self.load_meta_data = QPushButton(self.DataGroup)
        self.load_meta_data.setObjectName(u"load_meta_data")
        self.load_meta_data.setMinimumSize(QSize(30, 30))
        self.load_meta_data.setMaximumSize(QSize(30, 30))
        self.load_meta_data.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/add_meta.png);")

        self.DataOptions.addWidget(self.load_meta_data, 2, 0, 1, 1)

        self.select_directory_button = QPushButton(self.DataGroup)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setMinimumSize(QSize(30, 30))
        self.select_directory_button.setMaximumSize(QSize(30, 30))
        self.select_directory_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/open.png);")

        self.DataOptions.addWidget(self.select_directory_button, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.DataOptions.addItem(self.horizontalSpacer_19, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.DataGroup)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_25 = QGridLayout(self.groupBox_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.merge_series = QPushButton(self.groupBox_6)
        self.merge_series.setObjectName(u"merge_series")
        self.merge_series.setMinimumSize(QSize(30, 30))
        self.merge_series.setMaximumSize(QSize(30, 30))
        self.merge_series.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/merge.png);")

        self.gridLayout_24.addWidget(self.merge_series, 1, 0, 1, 1)

        self.edit_meta = QPushButton(self.groupBox_6)
        self.edit_meta.setObjectName(u"edit_meta")
        self.edit_meta.setMinimumSize(QSize(30, 30))
        self.edit_meta.setMaximumSize(QSize(30, 30))
        self.edit_meta.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/edit_metadata.png);")

        self.gridLayout_24.addWidget(self.edit_meta, 0, 0, 1, 1)

        self.show_colum = QPushButton(self.groupBox_6)
        self.show_colum.setObjectName(u"show_colum")
        self.show_colum.setMinimumSize(QSize(30, 30))
        self.show_colum.setMaximumSize(QSize(30, 30))
        self.show_colum.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/add_column.png);")

        self.gridLayout_24.addWidget(self.show_colum, 0, 1, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_24, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)

        self.PlotGroup = QGroupBox(self.frame)
        self.PlotGroup.setObjectName(u"PlotGroup")
        self.gridLayout_16 = QGridLayout(self.PlotGroup)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(1, 3, 1, 3)
        self.PlotOptions = QGridLayout()
        self.PlotOptions.setObjectName(u"PlotOptions")
        self.save_plot_online = QPushButton(self.PlotGroup)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(30, 30))
        self.save_plot_online.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(6)
        self.save_plot_online.setFont(font1)
        self.save_plot_online.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/save_img.png);")

        self.PlotOptions.addWidget(self.save_plot_online, 1, 0, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(30, 30))
        self.plot_zoom.setMaximumSize(QSize(30, 30))
        self.plot_zoom.setFont(font1)
        self.plot_zoom.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/zoom.png);")

        self.PlotOptions.addWidget(self.plot_zoom, 0, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.PlotOptions.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)

        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(30, 30))
        self.plot_move.setMaximumSize(QSize(30, 30))
        self.plot_move.setFont(font1)
        self.plot_move.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/move.png);")

        self.PlotOptions.addWidget(self.plot_move, 1, 2, 1, 1)

        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))
        self.plot_home.setFont(font1)
        self.plot_home.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/home.png);")

        self.PlotOptions.addWidget(self.plot_home, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.PlotOptions, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.PlotGroup)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.groupBox_7 = QGroupBox(self.frame)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(60, 30))
        self.gridLayout_28 = QGridLayout(self.groupBox_7)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.postgresql_upload = QPushButton(self.groupBox_7)
        self.postgresql_upload.setObjectName(u"postgresql_upload")
        self.postgresql_upload.setMinimumSize(QSize(50, 50))
        self.postgresql_upload.setMaximumSize(QSize(50, 50))
        self.postgresql_upload.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/sql.png);")

        self.gridLayout_27.addWidget(self.postgresql_upload, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.FilterOptions = QGroupBox(self.frame)
        self.FilterOptions.setObjectName(u"FilterOptions")
        self.gridLayout_17 = QGridLayout(self.FilterOptions)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.add_filter_button = QPushButton(self.FilterOptions)
        self.add_filter_button.setObjectName(u"add_filter_button")
        self.add_filter_button.setMinimumSize(QSize(30, 30))
        self.add_filter_button.setMaximumSize(QSize(30, 30))
        self.add_filter_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/filter_db.png);")

        self.gridLayout_23.addWidget(self.add_filter_button, 0, 0, 1, 1)

        self.sort_by = QPushButton(self.FilterOptions)
        self.sort_by.setObjectName(u"sort_by")
        self.sort_by.setMinimumSize(QSize(30, 30))
        self.sort_by.setMaximumSize(QSize(30, 30))
        self.sort_by.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/sort_by.png);")

        self.gridLayout_23.addWidget(self.sort_by, 0, 1, 1, 1)

        self.delete_selected = QPushButton(self.FilterOptions)
        self.delete_selected.setObjectName(u"delete_selected")
        self.delete_selected.setMinimumSize(QSize(30, 30))
        self.delete_selected.setMaximumSize(QSize(30, 30))
        self.delete_selected.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/delete.png);")

        self.gridLayout_23.addWidget(self.delete_selected, 1, 1, 1, 1)

        self.select = QPushButton(self.FilterOptions)
        self.select.setObjectName(u"select")
        self.select.setMinimumSize(QSize(30, 30))
        self.select.setMaximumSize(QSize(30, 30))
        self.select.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/select.png);")

        self.gridLayout_23.addWidget(self.select, 1, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_23, 3, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.FilterOptions)

        self.SeriesSelection = QGroupBox(self.frame)
        self.SeriesSelection.setObjectName(u"SeriesSelection")
        sizePolicy.setHeightForWidth(self.SeriesSelection.sizePolicy().hasHeightForWidth())
        self.SeriesSelection.setSizePolicy(sizePolicy)
        self.SeriesSelection.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_18 = QGridLayout(self.SeriesSelection)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(3, 1, 3, 1)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.compare_series = QPushButton(self.SeriesSelection)
        self.compare_series.setObjectName(u"compare_series")
        self.compare_series.setMinimumSize(QSize(40, 40))
        self.compare_series.setMaximumSize(QSize(40, 40))
        self.compare_series.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/select_big.png);")

        self.gridLayout_26.addWidget(self.compare_series, 0, 0, 1, 1)

        self.selected_series_combo = QComboBox(self.SeriesSelection)
        self.selected_series_combo.setObjectName(u"selected_series_combo")
        self.selected_series_combo.setMinimumSize(QSize(100, 0))
        self.selected_series_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_26.addWidget(self.selected_series_combo, 0, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_26, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_10, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.SeriesSelection)

        self.StartAnalysis = QGroupBox(self.frame)
        self.StartAnalysis.setObjectName(u"StartAnalysis")
        self.gridLayout_20 = QGridLayout(self.StartAnalysis)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(3, 1, 3, 1)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.start_analysis = QPushButton(self.StartAnalysis)
        self.start_analysis.setObjectName(u"start_analysis")
        self.start_analysis.setMinimumSize(QSize(50, 50))
        self.start_analysis.setMaximumSize(QSize(50, 50))
        self.start_analysis.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/start_analysis.png);")

        self.gridLayout_19.addWidget(self.start_analysis, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.StartAnalysis)


        self.gridLayout_13.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame, 0, 0, 1, 1)

        self.offline_analysis_widgets = QStackedWidget(Offline_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.offline_analysis_widgets.sizePolicy().hasHeightForWidth())
        self.offline_analysis_widgets.setSizePolicy(sizePolicy1)
        self.offline_analysis_widgets.setFont(font)
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.start_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.start_page)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setPointSize(14)
        self.groupBox.setFont(font2)
        self.gridLayout_29 = QGridLayout(self.groupBox)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.treeView = QTreeView(self.groupBox)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_29.addWidget(self.treeView, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_29.addWidget(self.textEdit, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_29.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 2)

        self.offline_analysis_widgets.addWidget(self.start_page)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.gridLayout_2 = QGridLayout(self.blank_analysis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.blank_analysis)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.treebuild = TreeBuild(self.blank_analysis)
        self.treebuild.setObjectName(u"treebuild")
        sizePolicy1.setHeightForWidth(self.treebuild.sizePolicy().hasHeightForWidth())
        self.treebuild.setSizePolicy(sizePolicy1)
        self.treebuild.setMinimumSize(QSize(400, 0))
        self.treebuild.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_14.addWidget(self.treebuild, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_14, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.blank_analysis)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.toolbar_layout = QGridLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")

        self.gridLayout_7.addLayout(self.toolbar_layout, 2, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.groupBox_5)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.canvas_grid_layout = QGridLayout()
        self.canvas_grid_layout.setObjectName(u"canvas_grid_layout")

        self.gridLayout_12.addLayout(self.canvas_grid_layout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout_7.addLayout(self.verticalLayout, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 0, 1, 1)

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
        sizePolicy2.setHeightForWidth(self.PlotItem.sizePolicy().hasHeightForWidth())
        self.PlotItem.setSizePolicy(sizePolicy2)
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

        self.gridLayout_21.addWidget(self.offline_analysis_widgets, 1, 0, 1, 1)


        self.retranslateUi(Offline_Analysis)

        self.offline_analysis_widgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Offline_Analysis", u"Offline Analysis", None))
        self.go_back_button.setText("")
        self.fo_forward_button.setText("")
        self.AnalysisOptions.setTitle(QCoreApplication.translate("Offline_Analysis", u"Analysis Options:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Open an exisiting analysis from the database and change parameters</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText(QCoreApplication.translate("Offline_Analysis", u"Open Analysis", None))
#if QT_CONFIG(tooltip)
        self.blank_analysis_button.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Start a new analysis from scratch</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"Blank Analysis", None))
        self.open_analysis_results_button.setText(QCoreApplication.translate("Offline_Analysis", u"Result Viewer", None))
        self.DataGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data Options", None))
        self.load_from_database.setText("")
        self.load_meta_data.setText("")
        self.select_directory_button.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Offline_Analysis", u"Edit Metadata", None))
        self.merge_series.setText("")
        self.edit_meta.setText("")
        self.show_colum.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Plot Options", None))
        self.save_plot_online.setText("")
        self.plot_zoom.setText("")
        self.plot_move.setText("")
        self.plot_home.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("Offline_Analysis", u"Upload", None))
        self.postgresql_upload.setText("")
        self.FilterOptions.setTitle(QCoreApplication.translate("Offline_Analysis", u"Filter Options", None))
#if QT_CONFIG(tooltip)
        self.add_filter_button.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Add Filters </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_filter_button.setText("")
#if QT_CONFIG(tooltip)
        self.sort_by.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Sort by Metadata Categories</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sort_by.setText("")
#if QT_CONFIG(tooltip)
        self.delete_selected.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Delete the selected experiments</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_selected.setText("")
#if QT_CONFIG(tooltip)
        self.select.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Multi-select several experiments in the tree</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.select.setText("")
        self.SeriesSelection.setTitle(QCoreApplication.translate("Offline_Analysis", u"Select Series", None))
#if QT_CONFIG(tooltip)
        self.compare_series.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Specifiy which Series should be analyzed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.compare_series.setText("")
        self.StartAnalysis.setTitle(QCoreApplication.translate("Offline_Analysis", u"Start Analysis", None))
        self.start_analysis.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Offline_Analysis", u"How To", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"Documentation", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data View", None))
        self.series_selection.setText(QCoreApplication.translate("Offline_Analysis", u"Collapse Tree", None))
        self.new_analysis.setText(QCoreApplication.translate("Offline_Analysis", u"New Analysis", None))
    # retranslateUi

