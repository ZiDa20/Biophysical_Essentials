# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offline_analysis_designer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from QT_GUI.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild
from QT_GUI.OfflineAnalysis.CustomWidget.ui_SeriesItem import OfflineTree


class Ui_Offline_Analysis(object):
    def setupUi(self, Offline_Analysis):
        if not Offline_Analysis.objectName():
            Offline_Analysis.setObjectName(u"Offline_Analysis")
        Offline_Analysis.resize(1274, 710)
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


        self.gridLayout_13.addLayout(self.gridLayout_22, 0, 0, 2, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_2, 0, 3, 2, 1)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_6, 0, 9, 2, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line, 0, 11, 2, 1)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_4, 0, 13, 2, 1)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_5, 0, 1, 2, 1)

        self.groupBox_8 = QGroupBox(self.frame)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_33 = QGridLayout(self.groupBox_8)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.clear = QPushButton(self.groupBox_8)
        self.clear.setObjectName(u"clear")
        self.clear.setMinimumSize(QSize(30, 30))
        self.clear.setMaximumSize(QSize(30, 30))
        self.clear.setStyleSheet(u"QPushButton {background-image: url(../QT_GUI/Button/OnlineAnalysis/broom.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

        self.gridLayout_34.addWidget(self.clear, 0, 0, 1, 1)

        self.show_colum_2 = QPushButton(self.groupBox_8)
        self.show_colum_2.setObjectName(u"show_colum_2")
        self.show_colum_2.setMinimumSize(QSize(30, 30))
        self.show_colum_2.setMaximumSize(QSize(30, 30))
        self.show_colum_2.setStyleSheet(u"QPushButton {background-image: url(../QT_GUI/Button/OnlineAnalysis/add_column.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

        self.gridLayout_34.addWidget(self.show_colum_2, 0, 1, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_34, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_8, 0, 6, 2, 1)

        self.SweepLevel = QGroupBox(self.frame)
        self.SweepLevel.setObjectName(u"SweepLevel")
        self.gridLayout_31 = QGridLayout(self.SweepLevel)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.show_sweeps_radio = QRadioButton(self.SweepLevel)
        self.show_sweeps_radio.setObjectName(u"show_sweeps_radio")

        self.gridLayout_32.addWidget(self.show_sweeps_radio, 0, 0, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_32, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.SweepLevel, 0, 8, 2, 1)

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


        self.gridLayout_13.addWidget(self.FilterOptions, 0, 14, 2, 1)

        self.SeriesSelection = QGroupBox(self.frame)
        self.SeriesSelection.setObjectName(u"SeriesSelection")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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


        self.gridLayout_13.addWidget(self.SeriesSelection, 0, 15, 2, 1)

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


        self.gridLayout_13.addWidget(self.StartAnalysis, 0, 16, 2, 1)

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
        self.edit_meta.setStyleSheet(u"QPushButton {background-image: url(../QT_GUI/Button/OnlineAnalysis/edit_metadata.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

        self.gridLayout_24.addWidget(self.edit_meta, 0, 0, 1, 1)

        self.edit_series_meta_data = QPushButton(self.groupBox_6)
        self.edit_series_meta_data.setObjectName(u"edit_series_meta_data")
        self.edit_series_meta_data.setMinimumSize(QSize(30, 30))
        self.edit_series_meta_data.setMaximumSize(QSize(30, 30))
        self.edit_series_meta_data.setStyleSheet(u"QPushButton {background-image: url(../QT_GUI/Button/OnlineAnalysis/burst.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

        self.gridLayout_24.addWidget(self.edit_series_meta_data, 0, 1, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_24, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_6, 0, 4, 2, 1)

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
        self.load_from_database.setStyleSheet(u"QPushButton {background-image: url(../QT_GUI/Button/OnlineAnalysis/load_database.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

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
        self.select_directory_button.setStyleSheet(u"QPushButton{background-image: url(../QT_GUI/Button/OnlineAnalysis/open.png);}\n"
"QToolTip { color: #ffffff; background-color: #000000; border: 0px; }")

        self.DataOptions.addWidget(self.select_directory_button, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.DataOptions.addItem(self.horizontalSpacer_19, 0, 1, 1, 1)


        self.gridLayout_15.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.DataGroup, 0, 2, 2, 1)

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


        self.gridLayout_13.addWidget(self.groupBox_7, 0, 12, 2, 1)

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


        self.gridLayout_13.addWidget(self.PlotGroup, 0, 10, 2, 1)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_3, 0, 7, 2, 1)

        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_7, 0, 5, 2, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)

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
        self.gridLayout_39 = QGridLayout(self.start_page)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.open_analysis_results_button = QPushButton(self.start_page)
        self.open_analysis_results_button.setObjectName(u"open_analysis_results_button")

        self.gridLayout_4.addWidget(self.open_analysis_results_button, 2, 5, 1, 2)

        self.blank_analysis_button = QPushButton(self.start_page)
        self.blank_analysis_button.setObjectName(u"blank_analysis_button")
        self.blank_analysis_button.setFont(font)

        self.gridLayout_4.addWidget(self.blank_analysis_button, 2, 0, 1, 2)

        self.label_3 = QLabel(self.start_page)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 5, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")

        self.gridLayout_4.addLayout(self.gridLayout_38, 1, 6, 1, 1)

        self.label = QLabel(self.start_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")

        self.gridLayout_4.addLayout(self.gridLayout_29, 1, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 5, 1, 1)


        self.gridLayout_39.addLayout(self.gridLayout_4, 0, 0, 1, 1)

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
        self.groupBox_5 = QGroupBox(self.blank_analysis)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
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


        self.gridLayout_2.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.offline_analysis_widgets.addWidget(self.blank_analysis)
        self.analysis_specific_notebook = QWidget()
        self.analysis_specific_notebook.setObjectName(u"analysis_specific_notebook")
        self.gridLayout_6 = QGridLayout(self.analysis_specific_notebook)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.SeriesItems_2 = OfflineTree(self.analysis_specific_notebook)
        self.SeriesItems_2.setObjectName(u"SeriesItems_2")
        sizePolicy2.setHeightForWidth(self.SeriesItems_2.sizePolicy().hasHeightForWidth())
        self.SeriesItems_2.setSizePolicy(sizePolicy2)
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

        self.offline_analysis_widgets.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Offline_Analysis)
    # setupUi

    def retranslateUi(self, Offline_Analysis):
        Offline_Analysis.setWindowTitle(QCoreApplication.translate("Offline_Analysis", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Offline_Analysis", u"Offline Analysis", None))
        self.go_back_button.setText("")
        self.fo_forward_button.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("Offline_Analysis", u"Treeview Metadata", None))
#if QT_CONFIG(tooltip)
        self.clear.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Clean the Treeview", None))
#endif // QT_CONFIG(tooltip)
        self.clear.setText("")
#if QT_CONFIG(tooltip)
        self.show_colum_2.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Select meta data and sort data in the treeview", None))
#endif // QT_CONFIG(tooltip)
        self.show_colum_2.setText("")
        self.SweepLevel.setTitle(QCoreApplication.translate("Offline_Analysis", u"Sweeps", None))
#if QT_CONFIG(tooltip)
        self.show_sweeps_radio.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Show Single Sweeps for each series", None))
#endif // QT_CONFIG(tooltip)
        self.show_sweeps_radio.setText("")
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
        self.groupBox_6.setTitle(QCoreApplication.translate("Offline_Analysis", u"Assign Metadata", None))
        self.merge_series.setText("")
#if QT_CONFIG(tooltip)
        self.edit_meta.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Modify Experiment Meta Data", None))
#endif // QT_CONFIG(tooltip)
        self.edit_meta.setText("")
#if QT_CONFIG(tooltip)
        self.edit_series_meta_data.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Modify Series Meta Data", None))
#endif // QT_CONFIG(tooltip)
        self.edit_series_meta_data.setText("")
        self.DataGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data Options", None))
#if QT_CONFIG(tooltip)
        self.load_from_database.setToolTip(QCoreApplication.translate("Offline_Analysis", u"Load data from the database", None))
#endif // QT_CONFIG(tooltip)
        self.load_from_database.setText("")
        self.load_meta_data.setText("")
        self.select_directory_button.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("Offline_Analysis", u"Upload", None))
        self.postgresql_upload.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Offline_Analysis", u"Plot Options", None))
        self.save_plot_online.setText("")
        self.plot_zoom.setText("")
        self.plot_move.setText("")
        self.plot_home.setText("")
        self.open_analysis_results_button.setText(QCoreApplication.translate("Offline_Analysis", u"View Results", None))
#if QT_CONFIG(tooltip)
        self.blank_analysis_button.setToolTip(QCoreApplication.translate("Offline_Analysis", u"<html><head/><body><p>Start a new analysis from scratch</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blank_analysis_button.setText(QCoreApplication.translate("Offline_Analysis", u"Start Blank Analysis", None))
        self.label_3.setText(QCoreApplication.translate("Offline_Analysis", u"Open Existing Analysis", None))
        self.label.setText(QCoreApplication.translate("Offline_Analysis", u"New Blank Analysis", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Offline_Analysis", u"Data View", None))
    # retranslateUi

