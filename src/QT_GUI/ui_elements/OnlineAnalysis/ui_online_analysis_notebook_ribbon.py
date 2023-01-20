# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'online_analysis_notebook_ribbon.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from groupbox_resizing_class import GroupBoxSize
from treebuild_widget import TreeBuild


class Ui_Online_Analysis(object):
    def setupUi(self, Online_Analysis):
        if not Online_Analysis.objectName():
            Online_Analysis.setObjectName(u"Online_Analysis")
        Online_Analysis.resize(1388, 1006)
        self.gridLayout_5 = QGridLayout(Online_Analysis)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(Online_Analysis)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 120))
        self.frame.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.gridLayout_22.addWidget(self.label_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../../Logo/new_logo_final.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_22.addWidget(self.label_3, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_22, 0, 0, 1, 1)

        self.DataGroup = QGroupBox(self.frame)
        self.DataGroup.setObjectName(u"DataGroup")
        self.gridLayout_11 = QGridLayout(self.DataGroup)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.button_select_data_file = QPushButton(self.DataGroup)
        self.button_select_data_file.setObjectName(u"button_select_data_file")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_select_data_file.sizePolicy().hasHeightForWidth())
        self.button_select_data_file.setSizePolicy(sizePolicy)
        self.button_select_data_file.setMinimumSize(QSize(40, 40))
        self.button_select_data_file.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(6)
        self.button_select_data_file.setFont(font1)
        self.button_select_data_file.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/open_file.png);\n"
"")

        self.DataOptions.addWidget(self.button_select_data_file, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.DataOptions.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.DataGroup, 0, 1, 2, 1)

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


        self.gridLayout_3.addWidget(self.groupBox_6, 0, 2, 2, 1)

        self.SweepLevel = QGroupBox(self.frame)
        self.SweepLevel.setObjectName(u"SweepLevel")
        self.gridLayout_31 = QGridLayout(self.SweepLevel)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.show_sweeps_radio = QRadioButton(self.SweepLevel)
        self.show_sweeps_radio.setObjectName(u"show_sweeps_radio")

        self.gridLayout_32.addWidget(self.show_sweeps_radio, 0, 0, 1, 1)


        self.gridLayout_31.addLayout(self.gridLayout_32, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.SweepLevel, 0, 3, 2, 1)

        self.PlotGroup = QGroupBox(self.frame)
        self.PlotGroup.setObjectName(u"PlotGroup")
        self.gridLayout_12 = QGridLayout(self.PlotGroup)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(1, 3, 1, 3)
        self.PlotOptions = QGridLayout()
        self.PlotOptions.setObjectName(u"PlotOptions")
        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(25, 25))
        self.plot_move.setMaximumSize(QSize(25, 25))
        self.plot_move.setFont(font1)
        self.plot_move.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/move.png);")

        self.PlotOptions.addWidget(self.plot_move, 1, 2, 1, 1)

        self.save_plot_online = QPushButton(self.PlotGroup)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(25, 25))
        self.save_plot_online.setMaximumSize(QSize(25, 25))
        self.save_plot_online.setFont(font1)
        self.save_plot_online.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/save_img.png);")

        self.PlotOptions.addWidget(self.save_plot_online, 1, 0, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(25, 25))
        self.plot_zoom.setMaximumSize(QSize(25, 25))
        self.plot_zoom.setFont(font1)
        self.plot_zoom.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/zoom.png);")

        self.PlotOptions.addWidget(self.plot_zoom, 0, 2, 1, 1)

        self.show_pgf_file = QPushButton(self.PlotGroup)
        self.show_pgf_file.setObjectName(u"show_pgf_file")
        self.show_pgf_file.setMinimumSize(QSize(25, 25))
        self.show_pgf_file.setMaximumSize(QSize(25, 25))
        self.show_pgf_file.setFont(font1)
        self.show_pgf_file.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/pgf.png);")

        self.PlotOptions.addWidget(self.show_pgf_file, 0, 0, 1, 1)

        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(25, 25))
        self.plot_home.setMaximumSize(QSize(25, 25))
        self.plot_home.setFont(font1)
        self.plot_home.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/home.png);")

        self.PlotOptions.addWidget(self.plot_home, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.PlotOptions.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.gridLayout_12.addLayout(self.PlotOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.PlotGroup, 0, 4, 2, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 5, 2, 1)

        self.ClassifierGroup = QGroupBox(self.frame)
        self.ClassifierGroup.setObjectName(u"ClassifierGroup")
        self.gridLayout_13 = QGridLayout(self.ClassifierGroup)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(1, 3, 1, 3)
        self.ClassificationOptions = QGridLayout()
        self.ClassificationOptions.setObjectName(u"ClassificationOptions")
        self.classifier_stream = QPushButton(self.ClassifierGroup)
        self.classifier_stream.setObjectName(u"classifier_stream")
        self.classifier_stream.setMinimumSize(QSize(40, 40))
        self.classifier_stream.setMaximumSize(QSize(40, 40))
        self.classifier_stream.setFont(font1)
        self.classifier_stream.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/machine_learning.png);")

        self.ClassificationOptions.addWidget(self.classifier_stream, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.ClassificationOptions.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.ClassificationOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.ClassifierGroup, 0, 6, 2, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 0, 7, 2, 1)

        self.LabbookGroup = QGroupBox(self.frame)
        self.LabbookGroup.setObjectName(u"LabbookGroup")
        self.gridLayout_14 = QGridLayout(self.LabbookGroup)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(1, 3, 1, 3)
        self.LabbookOptions = QGridLayout()
        self.LabbookOptions.setObjectName(u"LabbookOptions")
        self.save_labbook_button = QPushButton(self.LabbookGroup)
        self.save_labbook_button.setObjectName(u"save_labbook_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_labbook_button.sizePolicy().hasHeightForWidth())
        self.save_labbook_button.setSizePolicy(sizePolicy1)
        self.save_labbook_button.setMinimumSize(QSize(25, 25))
        self.save_labbook_button.setMaximumSize(QSize(25, 25))
        self.save_labbook_button.setFont(font1)
        self.save_labbook_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/export_csv.png);")

        self.LabbookOptions.addWidget(self.save_labbook_button, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.LabbookGroup)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/save_gif.png);")

        self.LabbookOptions.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.add_metadata_button = QPushButton(self.LabbookGroup)
        self.add_metadata_button.setObjectName(u"add_metadata_button")
        sizePolicy1.setHeightForWidth(self.add_metadata_button.sizePolicy().hasHeightForWidth())
        self.add_metadata_button.setSizePolicy(sizePolicy1)
        self.add_metadata_button.setMinimumSize(QSize(25, 25))
        self.add_metadata_button.setMaximumSize(QSize(25, 25))
        self.add_metadata_button.setFont(font1)
        self.add_metadata_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/add_meta.png);")

        self.LabbookOptions.addWidget(self.add_metadata_button, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.LabbookOptions.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.LabbookGroup)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/save_img.png);")

        self.LabbookOptions.addWidget(self.pushButton, 2, 0, 1, 1)


        self.gridLayout_14.addLayout(self.LabbookOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.LabbookGroup, 0, 8, 2, 1)

        self.TransferGroup = QGroupBox(self.frame)
        self.TransferGroup.setObjectName(u"TransferGroup")
        self.gridLayout_21 = QGridLayout(self.TransferGroup)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.transfer_to_offline_analysis = QPushButton(self.TransferGroup)
        self.transfer_to_offline_analysis.setObjectName(u"transfer_to_offline_analysis")
        sizePolicy1.setHeightForWidth(self.transfer_to_offline_analysis.sizePolicy().hasHeightForWidth())
        self.transfer_to_offline_analysis.setSizePolicy(sizePolicy1)
        self.transfer_to_offline_analysis.setMinimumSize(QSize(60, 60))
        self.transfer_to_offline_analysis.setMaximumSize(QSize(60, 60))
        self.transfer_to_offline_analysis.setFont(font1)
        self.transfer_to_offline_analysis.setStyleSheet(u"background-image: url(../QT_GUI/Button/OnlineAnalysis/sql.png);\n"
"")

        self.gridLayout_15.addWidget(self.transfer_to_offline_analysis, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_21.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.TransferGroup, 0, 9, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(500, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 10, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.online_analysis = QTabWidget(Online_Analysis)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        self.gridLayout_19 = QGridLayout(self.online_analysis_window)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_2 = GroupBoxSize(self.online_analysis_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(5000, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.online_analysis_tabs = QTabWidget(self.groupBox_2)
        self.online_analysis_tabs.setObjectName(u"online_analysis_tabs")
        self.recorded_series_plot_tab = QWidget()
        self.recorded_series_plot_tab.setObjectName(u"recorded_series_plot_tab")
        self.gridLayoutWidget = QWidget(self.recorded_series_plot_tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1321, 751))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tree_plot_widget_layout = QVBoxLayout()
        self.tree_plot_widget_layout.setObjectName(u"tree_plot_widget_layout")
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.gridLayout_17 = QGridLayout(self.widget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.plot_layout = QGridLayout()
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_17.addLayout(self.plot_layout, 0, 1, 1, 1)


        self.tree_plot_widget_layout.addWidget(self.widget)


        self.gridLayout_2.addLayout(self.tree_plot_widget_layout, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.online_treeview = TreeBuild(self.gridLayoutWidget)
        self.online_treeview.setObjectName(u"online_treeview")
        self.online_treeview.setMinimumSize(QSize(400, 0))
        self.online_treeview.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_18.addWidget(self.online_treeview, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_18, 0, 0, 1, 1)

        self.online_analysis_tabs.addTab(self.recorded_series_plot_tab, "")
        self.live_recording_tab = QWidget()
        self.live_recording_tab.setObjectName(u"live_recording_tab")
        self.gridLayout = QGridLayout(self.live_recording_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_10 = QSpacerItem(5, 300, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_10, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.online_analysis_tabs.addTab(self.live_recording_tab, "")
        self.fast_online_analysis = QWidget()
        self.fast_online_analysis.setObjectName(u"fast_online_analysis")
        self.online_analysis_tabs.addTab(self.fast_online_analysis, "")

        self.gridLayout_8.addWidget(self.online_analysis_tabs, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.gridLayout_20 = QGridLayout(self.labbook_window)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 4, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_10, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = GroupBoxSize(self.labbook_window)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setMinimumSize(QSize(400, 0))

        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(250, 0))
        self.graphicsView.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_9.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.label_13, 0, 1, 1, 1)

        self.image_experiment = QGraphicsView(self.groupBox)
        self.image_experiment.setObjectName(u"image_experiment")
        sizePolicy2.setHeightForWidth(self.image_experiment.sizePolicy().hasHeightForWidth())
        self.image_experiment.setSizePolicy(sizePolicy2)
        self.image_experiment.setMinimumSize(QSize(250, 0))
        self.image_experiment.setMaximumSize(QSize(16777215, 300))
        self.image_experiment.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_9.addWidget(self.image_experiment, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_9, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.gridLayout_20.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.label_12 = QLabel(self.labbook_window)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_12.setFont(font2)

        self.gridLayout_20.addWidget(self.label_12, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")

        self.gridLayout_20.addLayout(self.gridLayout_16, 3, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.treebuild_widget = TreeBuild(self.labbook_window)
        self.treebuild_widget.setObjectName(u"treebuild_widget")

        self.gridLayout_6.addWidget(self.treebuild_widget, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.online_analysis.addTab(self.labbook_window, "")
        self.Transfer = QWidget()
        self.Transfer.setObjectName(u"Transfer")
        self.gridLayoutWidget_5 = QWidget(self.Transfer)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 10, 1361, 831))
        self.gridLayout_29 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.save_to_new_file_button = QPushButton(self.gridLayoutWidget_5)
        self.save_to_new_file_button.setObjectName(u"save_to_new_file_button")

        self.gridLayout_29.addWidget(self.save_to_new_file_button, 2, 1, 1, 1)

        self.append_to_existing_file_button = QPushButton(self.gridLayoutWidget_5)
        self.append_to_existing_file_button.setObjectName(u"append_to_existing_file_button")

        self.gridLayout_29.addWidget(self.append_to_existing_file_button, 2, 2, 1, 1)

        self.transfer_into_db_button = QPushButton(self.gridLayoutWidget_5)
        self.transfer_into_db_button.setObjectName(u"transfer_into_db_button")

        self.gridLayout_29.addWidget(self.transfer_into_db_button, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_23 = QGridLayout(self.groupBox_4)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.experiment_treeview = QTableView(self.groupBox_4)
        self.experiment_treeview.setObjectName(u"experiment_treeview")

        self.gridLayout_26.addWidget(self.experiment_treeview, 0, 0, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_26, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_4, 0, 0, 1, 3)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_27 = QGridLayout(self.groupBox_5)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.series_treeview = QTreeView(self.groupBox_5)
        self.series_treeview.setObjectName(u"series_treeview")

        self.gridLayout_27.addWidget(self.series_treeview, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_5, 1, 0, 1, 3)

        self.online_analysis.addTab(self.Transfer, "")

        self.gridLayout_5.addWidget(self.online_analysis, 1, 0, 1, 1)


        self.retranslateUi(Online_Analysis)

        self.online_analysis.setCurrentIndex(0)
        self.online_analysis_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Online_Analysis)
    # setupUi

    def retranslateUi(self, Online_Analysis):
        Online_Analysis.setWindowTitle(QCoreApplication.translate("Online_Analysis", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Online_Analysis", u"Online Analysis:", None))
        self.label_3.setText("")
        self.DataGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Data Options", None))
        self.button_select_data_file.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Online_Analysis", u"Edit Metadata", None))
        self.merge_series.setText("")
        self.edit_meta.setText("")
        self.show_colum.setText("")
        self.SweepLevel.setTitle(QCoreApplication.translate("Online_Analysis", u"Sweeps", None))
        self.show_sweeps_radio.setText("")
        self.PlotGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Plot Options", None))
        self.plot_move.setText("")
        self.save_plot_online.setText("")
        self.plot_zoom.setText("")
        self.show_pgf_file.setText("")
        self.plot_home.setText("")
        self.ClassifierGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Classifier Options", None))
        self.classifier_stream.setText("")
        self.LabbookGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbook Options", None))
        self.save_labbook_button.setText("")
        self.pushButton_2.setText("")
        self.add_metadata_button.setText("")
        self.pushButton.setText("")
        self.TransferGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Transfer Options", None))
        self.transfer_to_offline_analysis.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Online_Analysis", u"Visualization of the Traces", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Online_Analysis", u"Data View", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.recorded_series_plot_tab), QCoreApplication.translate("Online_Analysis", u"Plot Window", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.live_recording_tab), QCoreApplication.translate("Online_Analysis", u"Live Recording", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.fast_online_analysis), QCoreApplication.translate("Online_Analysis", u"Fast Analysis", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Online_Analysis", u"Online Analysis", None))
        self.groupBox.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbbook Table", None))
        self.label_9.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Image", None))
        self.label_13.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Temporal GIF", None))
        self.label_12.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Report", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Online_Analysis", u"Labbook", None))
        self.save_to_new_file_button.setText(QCoreApplication.translate("Online_Analysis", u"Transfer and Save to New File", None))
        self.append_to_existing_file_button.setText(QCoreApplication.translate("Online_Analysis", u"Transfer and Save To Existing File", None))
        self.transfer_into_db_button.setText(QCoreApplication.translate("Online_Analysis", u"Transfer into DB", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Online_Analysis", u"Experiments", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Online_Analysis", u"Series", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.Transfer), QCoreApplication.translate("Online_Analysis", u"Transfer", None))
    # retranslateUi

