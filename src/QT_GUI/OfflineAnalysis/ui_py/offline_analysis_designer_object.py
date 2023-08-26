# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_designer.ui'
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
    QGroupBox, QLayout, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QWidget)

from QT_GUI.OfflineAnalysis.CustomWidget.ui_SeriesItem import OfflineTree
from QT_GUI.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild

class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(1428, 708)
        self.gridLayout_8 = QGridLayout(Offline_Analysis)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
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
        self.gridLayout_13.setHorizontalSpacing(5)
        self.gridLayout_13.setContentsMargins(2, 2, 2, 2)
        self.groupBox_8 = QGroupBox(self.frame)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.gridLayout_33 = QGridLayout(self.groupBox_8)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.clear = QPushButton(self.groupBox_8)
        self.clear.setObjectName(u"clear")
        self.clear.setMinimumSize(QSize(30, 30))
        self.clear.setMaximumSize(QSize(30, 30))
        self.clear.setStyleSheet(u"")

        self.gridLayout_34.addWidget(self.clear, 0, 0, 1, 1)

        self.show_sweeps_radio = QRadioButton(self.groupBox_8)
        self.show_sweeps_radio.setObjectName(u"show_sweeps_radio")

        self.gridLayout_34.addWidget(self.show_sweeps_radio, 0, 5, 1, 1)

        self.add_meta_data_to_treeview = QPushButton(self.groupBox_8)
        self.add_meta_data_to_treeview.setObjectName(u"add_meta_data_to_treeview")
        self.add_meta_data_to_treeview.setMinimumSize(QSize(30, 30))
        self.add_meta_data_to_treeview.setMaximumSize(QSize(30, 30))
        self.add_meta_data_to_treeview.setStyleSheet(u"")

        self.gridLayout_34.addWidget(self.add_meta_data_to_treeview, 0, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox_8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_34.addWidget(self.line_3, 0, 4, 1, 1)

        self.series_to_csv = QPushButton(self.groupBox_8)
        self.series_to_csv.setObjectName(u"series_to_csv")
        self.series_to_csv.setMinimumSize(QSize(30, 30))
        self.series_to_csv.setMaximumSize(QSize(30, 30))

        self.gridLayout_34.addWidget(self.series_to_csv, 0, 2, 1, 1)

        self.experiment_to_csv = QPushButton(self.groupBox_8)
        self.experiment_to_csv.setObjectName(u"experiment_to_csv")
        self.experiment_to_csv.setMinimumSize(QSize(30, 30))
        self.experiment_to_csv.setMaximumSize(QSize(30, 30))

        self.gridLayout_34.addWidget(self.experiment_to_csv, 0, 3, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_34, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_8, 0, 5, 2, 1)

        self.FilterOptions = QGroupBox(self.frame)
        self.FilterOptions.setObjectName(u"FilterOptions")
        sizePolicy.setHeightForWidth(self.FilterOptions.sizePolicy().hasHeightForWidth())
        self.FilterOptions.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QGridLayout(self.FilterOptions)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.delete_selected = QPushButton(self.FilterOptions)
        self.delete_selected.setObjectName(u"delete_selected")
        self.delete_selected.setMinimumSize(QSize(30, 30))
        self.delete_selected.setMaximumSize(QSize(30, 30))
        self.delete_selected.setStyleSheet(u"")

        self.gridLayout_23.addWidget(self.delete_selected, 0, 1, 1, 1)

        self.add_filter_button = QPushButton(self.FilterOptions)
        self.add_filter_button.setObjectName(u"add_filter_button")
        self.add_filter_button.setMinimumSize(QSize(30, 30))
        self.add_filter_button.setMaximumSize(QSize(30, 30))
        self.add_filter_button.setStyleSheet(u"")

        self.gridLayout_23.addWidget(self.add_filter_button, 0, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_23, 3, 0, 1, 1)


        self.gridLayout_13.addWidget(self.FilterOptions, 0, 4, 2, 1)

        self.DataGroup = QGroupBox(self.frame)
        self.DataGroup.setObjectName(u"DataGroup")
        sizePolicy.setHeightForWidth(self.DataGroup.sizePolicy().hasHeightForWidth())
        self.DataGroup.setSizePolicy(sizePolicy)
        self.gridLayout_15 = QGridLayout(self.DataGroup)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.load_from_database = QPushButton(self.DataGroup)
        self.load_from_database.setObjectName(u"load_from_database")
        self.load_from_database.setMinimumSize(QSize(30, 30))
        self.load_from_database.setMaximumSize(QSize(30, 30))
        self.load_from_database.setStyleSheet(u"")

        self.DataOptions.addWidget(self.load_from_database, 0, 1, 1, 1)

        self.append = QPushButton(self.DataGroup)
        self.append.setObjectName(u"append")
        self.append.setMinimumSize(QSize(30, 30))
        self.append.setMaximumSize(QSize(30, 30))
        self.append.setStyleSheet(u"")

        self.DataOptions.addWidget(self.append, 0, 2, 1, 1)

        self.change_series_name = QPushButton(self.DataGroup)
        self.change_series_name.setObjectName(u"change_series_name")
        self.change_series_name.setMinimumSize(QSize(30, 30))
        self.change_series_name.setMaximumSize(QSize(30, 30))

        self.DataOptions.addWidget(self.change_series_name, 0, 3, 1, 1)

        self.select_directory_button = QPushButton(self.DataGroup)
        self.select_directory_button.setObjectName(u"select_directory_button")
        self.select_directory_button.setMinimumSize(QSize(30, 30))
        self.select_directory_button.setMaximumSize(QSize(30, 30))
#if QT_CONFIG(tooltip)
        self.select_directory_button.setToolTip(u"Load data from directory into database")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.select_directory_button.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.select_directory_button.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.select_directory_button.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.select_directory_button.setAutoFillBackground(False)
        self.select_directory_button.setStyleSheet(u"")

        self.DataOptions.addWidget(self.select_directory_button, 0, 0, 1, 1)

        self.load_selected_discarded = QPushButton(self.DataGroup)
        self.load_selected_discarded.setObjectName(u"load_selected_discarded")
        self.load_selected_discarded.setMinimumSize(QSize(30, 30))
        self.load_selected_discarded.setMaximumSize(QSize(30, 30))

        self.DataOptions.addWidget(self.load_selected_discarded, 0, 4, 1, 1)


        self.gridLayout_15.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.DataGroup, 0, 1, 2, 1)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_25 = QGridLayout(self.groupBox_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.edit_meta = QPushButton(self.groupBox_6)
        self.edit_meta.setObjectName(u"edit_meta")
        self.edit_meta.setMinimumSize(QSize(30, 30))
        self.edit_meta.setMaximumSize(QSize(30, 30))
        self.edit_meta.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.edit_meta, 0, 0, 1, 1)

        self.edit_series_meta_data = QPushButton(self.groupBox_6)
        self.edit_series_meta_data.setObjectName(u"edit_series_meta_data")
        self.edit_series_meta_data.setMinimumSize(QSize(30, 30))
        self.edit_series_meta_data.setMaximumSize(QSize(30, 30))
        self.edit_series_meta_data.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.edit_series_meta_data, 0, 1, 1, 1)

        self.merge_series = QPushButton(self.groupBox_6)
        self.merge_series.setObjectName(u"merge_series")
        self.merge_series.setMinimumSize(QSize(30, 30))
        self.merge_series.setMaximumSize(QSize(30, 30))
        self.merge_series.setStyleSheet(u"")

        self.gridLayout_24.addWidget(self.merge_series, 0, 2, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_24, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_6, 0, 3, 2, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_21 = QGridLayout(self.groupBox_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.go_back_button = QPushButton(self.groupBox_2)
        self.go_back_button.setObjectName(u"go_back_button")
        self.go_back_button.setMinimumSize(QSize(40, 40))
        self.go_back_button.setMaximumSize(QSize(50, 503))
        self.go_back_button.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.go_back_button, 0, 2, 1, 1)

        self.fo_forward_button = QPushButton(self.groupBox_2)
        self.fo_forward_button.setObjectName(u"fo_forward_button")
        self.fo_forward_button.setMinimumSize(QSize(40, 40))
        self.fo_forward_button.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.fo_forward_button, 0, 3, 1, 1)

        self.go_home = QPushButton(self.groupBox_2)
        self.go_home.setObjectName(u"go_home")
        self.go_home.setMinimumSize(QSize(40, 40))

        self.gridLayout_11.addWidget(self.go_home, 0, 0, 1, 1)

        self.line_8 = QFrame(self.groupBox_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_8, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_2, 0, 0, 2, 1)

        self.PlotGroup = QGroupBox(self.frame)
        self.PlotGroup.setObjectName(u"PlotGroup")
        sizePolicy.setHeightForWidth(self.PlotGroup.sizePolicy().hasHeightForWidth())
        self.PlotGroup.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.PlotGroup)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(1, 3, 1, 3)
        self.PlotOptions = QGridLayout()
        self.PlotOptions.setObjectName(u"PlotOptions")
        self.line_6 = QFrame(self.PlotGroup)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.PlotOptions.addWidget(self.line_6, 0, 5, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(30, 30))
        self.plot_zoom.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(6)
        self.plot_zoom.setFont(font)
        self.plot_zoom.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_zoom, 0, 1, 1, 1)

        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))
        self.plot_home.setFont(font)
        self.plot_home.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_home, 0, 0, 1, 1)

        self.plot_meta = QPushButton(self.PlotGroup)
        self.plot_meta.setObjectName(u"plot_meta")
        self.plot_meta.setMinimumSize(QSize(30, 30))
        self.plot_meta.setMaximumSize(QSize(30, 30))

        self.PlotOptions.addWidget(self.plot_meta, 0, 6, 1, 1)

        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(30, 30))
        self.plot_move.setMaximumSize(QSize(30, 30))
        self.plot_move.setFont(font)
        self.plot_move.setStyleSheet(u"")

        self.PlotOptions.addWidget(self.plot_move, 0, 2, 1, 1)

        self.turn_off_grid = QPushButton(self.PlotGroup)
        self.turn_off_grid.setObjectName(u"turn_off_grid")
        self.turn_off_grid.setMinimumSize(QSize(30, 30))
        self.turn_off_grid.setMaximumSize(QSize(30, 30))

        self.PlotOptions.addWidget(self.turn_off_grid, 0, 3, 1, 1)

        self.show_pgf_trace = QPushButton(self.PlotGroup)
        self.show_pgf_trace.setObjectName(u"show_pgf_trace")
        self.show_pgf_trace.setMinimumSize(QSize(30, 30))
        self.show_pgf_trace.setMaximumSize(QSize(30, 30))

        self.PlotOptions.addWidget(self.show_pgf_trace, 0, 4, 1, 1)


        self.gridLayout_16.addLayout(self.PlotOptions, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.PlotGroup, 0, 6, 2, 1)

        self.ribbon_series_normalization = QStackedWidget(self.frame)
        self.ribbon_series_normalization.setObjectName(u"ribbon_series_normalization")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_19 = QGridLayout(self.page)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(0)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.SeriesSelection = QGroupBox(self.page)
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
        self.compare_series.setStyleSheet(u"")

        self.gridLayout_26.addWidget(self.compare_series, 0, 0, 1, 1)

        self.selected_series_combo = QComboBox(self.SeriesSelection)
        self.selected_series_combo.setObjectName(u"selected_series_combo")
        self.selected_series_combo.setMinimumSize(QSize(50, 0))
        self.selected_series_combo.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_26.addWidget(self.selected_series_combo, 0, 1, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_26, 1, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_10, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.SeriesSelection, 0, 0, 1, 1)

        self.ribbon_series_normalization.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_29 = QGridLayout(self.page_2)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_30 = QGridLayout(self.groupBox_3)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.select_analysis_fct = QPushButton(self.groupBox_3)
        self.select_analysis_fct.setObjectName(u"select_analysis_fct")
        self.select_analysis_fct.setMinimumSize(QSize(30, 30))
        self.select_analysis_fct.setMaximumSize(QSize(30, 30))

        self.gridLayout_30.addWidget(self.select_analysis_fct, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.ribbon_series_normalization.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_35 = QGridLayout(self.page_3)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.page_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_36 = QGridLayout(self.groupBox_7)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.configure_report_button = QPushButton(self.groupBox_7)
        self.configure_report_button.setObjectName(u"configure_report_button")
        self.configure_report_button.setMinimumSize(QSize(30, 30))
        self.configure_report_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_36.addWidget(self.configure_report_button, 0, 0, 1, 1)


        self.gridLayout_35.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.ribbon_series_normalization.addWidget(self.page_3)

        self.gridLayout_13.addWidget(self.ribbon_series_normalization, 0, 8, 1, 1)

        self.ribbon_analysis = QStackedWidget(self.frame)
        self.ribbon_analysis.setObjectName(u"ribbon_analysis")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_27 = QGridLayout(self.page_4)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.StartAnalysis = QGroupBox(self.page_4)
        self.StartAnalysis.setObjectName(u"StartAnalysis")
        sizePolicy.setHeightForWidth(self.StartAnalysis.sizePolicy().hasHeightForWidth())
        self.StartAnalysis.setSizePolicy(sizePolicy)
        self.gridLayout_20 = QGridLayout(self.StartAnalysis)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.start_analysis = QPushButton(self.StartAnalysis)
        self.start_analysis.setObjectName(u"start_analysis")
        self.start_analysis.setMinimumSize(QSize(50, 50))
        self.start_analysis.setMaximumSize(QSize(50, 50))
        self.start_analysis.setStyleSheet(u"")

        self.gridLayout_20.addWidget(self.start_analysis, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.StartAnalysis, 0, 0, 1, 1)

        self.ribbon_analysis.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_28 = QGridLayout(self.page_5)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.page_5)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.run_analysis_functions = QPushButton(self.groupBox)
        self.run_analysis_functions.setObjectName(u"run_analysis_functions")
        self.run_analysis_functions.setMinimumSize(QSize(50, 50))
        self.run_analysis_functions.setMaximumSize(QSize(50, 50))
        self.run_analysis_functions.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.run_analysis_functions, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox, 0, 0, 1, 1)

        self.ribbon_analysis.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_31 = QGridLayout(self.page_6)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.page_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_32 = QGridLayout(self.groupBox_4)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.create_report_button = QPushButton(self.groupBox_4)
        self.create_report_button.setObjectName(u"create_report_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.create_report_button.sizePolicy().hasHeightForWidth())
        self.create_report_button.setSizePolicy(sizePolicy2)
        self.create_report_button.setMinimumSize(QSize(30, 30))
        self.create_report_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_32.addWidget(self.create_report_button, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.ribbon_analysis.addWidget(self.page_6)

        self.gridLayout_13.addWidget(self.ribbon_analysis, 0, 9, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)

        self.offline_analysis_widgets = QStackedWidget(Offline_Analysis)
        self.offline_analysis_widgets.setObjectName(u"offline_analysis_widgets")
        self.offline_analysis_widgets.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.offline_analysis_widgets.sizePolicy().hasHeightForWidth())
        self.offline_analysis_widgets.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(10)
        self.offline_analysis_widgets.setFont(font1)
        self.blank_analysis = QWidget()
        self.blank_analysis.setObjectName(u"blank_analysis")
        self.gridLayout_2 = QGridLayout(self.blank_analysis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 5, 0, 5)
        self.widget_2 = QWidget(self.blank_analysis)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.treebuild = TreeBuild(self.blank_analysis)
        self.treebuild.setObjectName(u"treebuild")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.treebuild.sizePolicy().hasHeightForWidth())
        self.treebuild.setSizePolicy(sizePolicy4)
        self.treebuild.setMinimumSize(QSize(0, 0))
        self.treebuild.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_14.addWidget(self.treebuild, 0, 0, 1, 2)


        self.gridLayout_9.addLayout(self.gridLayout_14, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.blank_analysis)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy5)
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.groupBox_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setStyleSheet(u"border-radius: 5px;")
        self.plot_page = QWidget()
        self.plot_page.setObjectName(u"plot_page")
        sizePolicy4.setHeightForWidth(self.plot_page.sizePolicy().hasHeightForWidth())
        self.plot_page.setSizePolicy(sizePolicy4)
        self.plot_page.setStyleSheet(u"border-radius: 5px;")
        self.gridLayout_3 = QGridLayout(self.plot_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.plot_page)
        self.widget.setObjectName(u"widget")
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setStyleSheet(u"border-radius: 5px;")
        self.gridLayout_12 = QGridLayout(self.widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(5, 0, 5, 0)
        self.canvas_grid_layout = QGridLayout()
        self.canvas_grid_layout.setObjectName(u"canvas_grid_layout")

        self.gridLayout_12.addLayout(self.canvas_grid_layout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.plot_page)
        self.animation_page = QWidget()
        self.animation_page.setObjectName(u"animation_page")
        sizePolicy4.setHeightForWidth(self.animation_page.sizePolicy().hasHeightForWidth())
        self.animation_page.setSizePolicy(sizePolicy4)
        self.gridLayout_22 = QGridLayout(self.animation_page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.animation_layout = QGridLayout()
        self.animation_layout.setObjectName(u"animation_layout")

        self.gridLayout_22.addLayout(self.animation_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.animation_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.analysis_specific_notebook = QWidget()
        self.analysis_specific_notebook.setObjectName(u"analysis_specific_notebook")
        self.gridLayout_6 = QGridLayout(self.analysis_specific_notebook)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(1)
        self.gridLayout_6.setContentsMargins(0, 5, 0, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.SeriesItems_2 = OfflineTree(self.analysis_specific_notebook)
        self.SeriesItems_2.setObjectName(u"SeriesItems_2")
        sizePolicy4.setHeightForWidth(self.SeriesItems_2.sizePolicy().hasHeightForWidth())
        self.SeriesItems_2.setSizePolicy(sizePolicy4)
        self.SeriesItems_2.setMaximumSize(QSize(250, 16777215))

        self.gridLayout_5.addWidget(self.SeriesItems_2, 0, 0, 1, 1)

        self.WidgetAnalysis = QGridLayout()
        self.WidgetAnalysis.setObjectName(u"WidgetAnalysis")

        self.gridLayout_5.addLayout(self.WidgetAnalysis, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.analysis_specific_notebook)

        self.gridLayout_8.addWidget(self.offline_analysis_widgets, 1, 0, 1, 1)


        self.retranslateUi(Offline_Analysis)

        self.ribbon_series_normalization.setCurrentIndex(0)
        self.ribbon_analysis.setCurrentIndex(0)
        self.offline_analysis_widgets.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Offline_Analysis", u"Treeview Options", None))
#if QT_CONFIG(tooltip)
        self.clear.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Clean the Treeview", None))
#endif // QT_CONFIG(tooltip)
        self.clear.setText("")
#if QT_CONFIG(tooltip)
        self.show_sweeps_radio.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Show Single Sweeps for each series", None))
#endif // QT_CONFIG(tooltip)
        self.show_sweeps_radio.setText(QCoreApplication.translate("Offline_Analysis", u"Sweeps", None))
#if QT_CONFIG(tooltip)
        self.add_meta_data_to_treeview.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Select meta data and sort data in the treeview", None))
#endif // QT_CONFIG(tooltip)
        self.add_meta_data_to_treeview.setText("")
#if QT_CONFIG(tooltip)
        self.series_to_csv.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Download raw data from currently selected series</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.series_to_csv.setText("")
#if QT_CONFIG(tooltip)
        self.experiment_to_csv.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Download raw data from currently selected experiment from Treeview</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.experiment_to_csv.setText("")
        self.FilterOptions.setTitle(QCoreApplication.translate("Offline_Analysis", u"Filter Options", None))
#if QT_CONFIG(tooltip)
        self.delete_selected.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Delete the selected experiments</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_selected.setText("")
#if QT_CONFIG(tooltip)
        self.add_filter_button.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Add Filters </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_filter_button.setText("")
        self.DataGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data Options", None))
#if QT_CONFIG(tooltip)
        self.load_from_database.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Load data from the database", None))
#endif // QT_CONFIG(tooltip)
        self.load_from_database.setText("")
#if QT_CONFIG(tooltip)
        self.append.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Series can be merged and aggregations performed creating a new series</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.append.setText("")
#if QT_CONFIG(tooltip)
        self.change_series_name.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Rename Series</span></p><p>Change the name of a series</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.change_series_name.setText("")
        self.select_directory_button.setText("")
#if QT_CONFIG(tooltip)
        self.load_selected_discarded.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Load Discarded Flags </span></p><p>Apply already performed selection of discarded and selected data from a previous analysis</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.load_selected_discarded.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Offline_Analysis", u"Edit Metadata", None))
#if QT_CONFIG(tooltip)
        self.edit_meta.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Modify Experiment Meta Data", None))
#endif // QT_CONFIG(tooltip)
        self.edit_meta.setText("")
#if QT_CONFIG(tooltip)
        self.edit_series_meta_data.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Modify Series Meta Data", None))
#endif // QT_CONFIG(tooltip)
        self.edit_series_meta_data.setText("")
        self.merge_series.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Offline_Analysis", u"Page Control", None))
        self.go_back_button.setText("")
        self.fo_forward_button.setText("")
        self.go_home.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Plot Options", None))
        self.plot_zoom.setText("")
        self.plot_home.setText("")
        self.plot_meta.setText("")
        self.plot_move.setText("")
        self.turn_off_grid.setText("")
        self.show_pgf_trace.setText("")
        self.SeriesSelection.setTitle(QCoreApplication.translate("Offline_Analysis", u"Select Series", None))
#if QT_CONFIG(tooltip)
        self.compare_series.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Specifiy which Series should be analyzed</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.compare_series.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Offline_Analysis", u"Select Analysis", None))
        self.select_analysis_fct.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("Offline_Analysis", u"Configure Report", None))
        self.configure_report_button.setText("")
        self.StartAnalysis.setTitle(QCoreApplication.translate("Offline_Analysis", u"Set Up Analysis", None))
        self.start_analysis.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Offline_Analysis", u"Run Analysis", None))
        self.run_analysis_functions.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Offline_Analysis", u"Create Report", None))
        self.create_report_button.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data View", None))
    # retranslateUi

