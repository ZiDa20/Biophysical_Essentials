# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'online_analysis_notebook_ribbon.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

from Frontend.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild
from groupbox_resizing_class import GroupBoxSize

class Ui_Online_Analysis(object):
    def setupUi(self, Online_Analysis):
        if not Online_Analysis.objectName():
            Online_Analysis.setObjectName(u"Online_Analysis")
        Online_Analysis.resize(1390, 956)
        self.gridLayout_5 = QGridLayout(Online_Analysis)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.online_analysis = QTabWidget(Online_Analysis)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.online_analysis_window.sizePolicy().hasHeightForWidth())
        self.online_analysis_window.setSizePolicy(sizePolicy)
        self.online_analysis_window.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_19 = QGridLayout(self.online_analysis_window)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.groupBox_3 = QGroupBox(self.online_analysis_window)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.groupBox_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.plot_page = QWidget()
        self.plot_page.setObjectName(u"plot_page")
        sizePolicy.setHeightForWidth(self.plot_page.sizePolicy().hasHeightForWidth())
        self.plot_page.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.plot_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tree_plot_widget_layout = QVBoxLayout()
        self.tree_plot_widget_layout.setObjectName(u"tree_plot_widget_layout")
        self.widget = QWidget(self.plot_page)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QGridLayout(self.widget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.plot_layout = QGridLayout()
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_17.addLayout(self.plot_layout, 0, 1, 1, 1)


        self.tree_plot_widget_layout.addWidget(self.widget)


        self.gridLayout_9.addLayout(self.tree_plot_widget_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.plot_page)
        self.animation_page = QWidget()
        self.animation_page.setObjectName(u"animation_page")
        sizePolicy.setHeightForWidth(self.animation_page.sizePolicy().hasHeightForWidth())
        self.animation_page.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.animation_page)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.animation_layout = QGridLayout()
        self.animation_layout.setObjectName(u"animation_layout")

        self.gridLayout_16.addLayout(self.animation_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.animation_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.online_treeview = TreeBuild(self.online_analysis_window)
        self.online_treeview.setObjectName(u"online_treeview")
        sizePolicy.setHeightForWidth(self.online_treeview.sizePolicy().hasHeightForWidth())
        self.online_treeview.setSizePolicy(sizePolicy)
        self.online_treeview.setMinimumSize(QSize(0, 0))
        self.online_treeview.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_19.addWidget(self.online_treeview, 0, 0, 1, 1)

        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.gridLayout_20 = QGridLayout(self.labbook_window)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = GroupBoxSize(self.labbook_window)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(400, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(250, 0))
        self.graphicsView.setMaximumSize(QSize(400, 300))

        self.gridLayout_7.addWidget(self.graphicsView, 4, 0, 1, 1)

        self.image_experiment = QGraphicsView(self.groupBox)
        self.image_experiment.setObjectName(u"image_experiment")
        sizePolicy.setHeightForWidth(self.image_experiment.sizePolicy().hasHeightForWidth())
        self.image_experiment.setSizePolicy(sizePolicy)
        self.image_experiment.setMinimumSize(QSize(250, 0))
        self.image_experiment.setMaximumSize(QSize(400, 300))
        self.image_experiment.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_7.addWidget(self.image_experiment, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.label_13, 3, 0, 1, 1)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_4, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.gridLayout_20.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.table_layout = QGridLayout()
        self.table_layout.setObjectName(u"table_layout")

        self.gridLayout_20.addLayout(self.table_layout, 0, 2, 1, 1)

        self.online_analysis.addTab(self.labbook_window, "")
        self.Transfer = QWidget()
        self.Transfer.setObjectName(u"Transfer")
        self.gridLayout = QGridLayout(self.Transfer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.groupBox_5 = QGroupBox(self.Transfer)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.gridLayout_27 = QGridLayout(self.groupBox_5)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.series_treeview = QTableView(self.groupBox_5)
        self.series_treeview.setObjectName(u"series_treeview")

        self.gridLayout_27.addWidget(self.series_treeview, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_5, 1, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.Transfer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableView = QTableView(self.groupBox_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_2, 0, 3, 1, 1)

        self.groupBox_4 = QGroupBox(self.Transfer)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.gridLayout_23 = QGridLayout(self.groupBox_4)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.experiment_treeview = QTableView(self.groupBox_4)
        self.experiment_treeview.setObjectName(u"experiment_treeview")

        self.gridLayout_26.addWidget(self.experiment_treeview, 0, 0, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_26, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_4, 0, 0, 1, 3)

        self.transfer_into_db_button = QPushButton(self.Transfer)
        self.transfer_into_db_button.setObjectName(u"transfer_into_db_button")

        self.gridLayout_29.addWidget(self.transfer_into_db_button, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.Transfer)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy2.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy2)
        self.groupBox_9.setMaximumSize(QSize(600, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView_2 = QGraphicsView(self.groupBox_9)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_6.addWidget(self.graphicsView_2, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_9, 1, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_29, 0, 0, 1, 1)

        self.online_analysis.addTab(self.Transfer, "")

        self.gridLayout_8.addWidget(self.online_analysis, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 2, 0, 1, 1)

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
"}\n"
"\n"
"QPushButton:disabled{\n"
"    opacity: 0.5;\n"
"	background-color:#1c252e; \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.PlotGroup = QGroupBox(self.frame)
        self.PlotGroup.setObjectName(u"PlotGroup")
        self.gridLayout_12 = QGridLayout(self.PlotGroup)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.plot_home = QPushButton(self.PlotGroup)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(6)
        self.plot_home.setFont(font)
        self.plot_home.setStyleSheet(u"")

        self.gridLayout_35.addWidget(self.plot_home, 0, 0, 1, 1)

        self.plot_move = QPushButton(self.PlotGroup)
        self.plot_move.setObjectName(u"plot_move")
        self.plot_move.setMinimumSize(QSize(30, 30))
        self.plot_move.setMaximumSize(QSize(30, 30))
        self.plot_move.setFont(font)
        self.plot_move.setStyleSheet(u"")

        self.gridLayout_35.addWidget(self.plot_move, 0, 2, 1, 1)

        self.plot_zoom = QPushButton(self.PlotGroup)
        self.plot_zoom.setObjectName(u"plot_zoom")
        self.plot_zoom.setMinimumSize(QSize(30, 30))
        self.plot_zoom.setMaximumSize(QSize(30, 30))
        self.plot_zoom.setFont(font)
        self.plot_zoom.setStyleSheet(u"")

        self.gridLayout_35.addWidget(self.plot_zoom, 0, 1, 1, 1)

        self.save_plot_online = QPushButton(self.PlotGroup)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(30, 30))
        self.save_plot_online.setMaximumSize(QSize(30, 30))
        self.save_plot_online.setFont(font)
        self.save_plot_online.setStyleSheet(u"")

        self.gridLayout_35.addWidget(self.save_plot_online, 0, 4, 1, 1)

        self.show_pgf_file = QPushButton(self.PlotGroup)
        self.show_pgf_file.setObjectName(u"show_pgf_file")
        self.show_pgf_file.setMinimumSize(QSize(30, 30))
        self.show_pgf_file.setMaximumSize(QSize(30, 30))
        self.show_pgf_file.setFont(font)
        self.show_pgf_file.setStyleSheet(u"")

        self.gridLayout_35.addWidget(self.show_pgf_file, 0, 5, 1, 1)

        self.line_3 = QFrame(self.PlotGroup)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_35.addWidget(self.line_3, 0, 3, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_35, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.PlotGroup, 0, 5, 2, 1)

        self.LabbookGroup = QGroupBox(self.frame)
        self.LabbookGroup.setObjectName(u"LabbookGroup")
        self.gridLayout_14 = QGridLayout(self.LabbookGroup)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.save_labbook_button = QPushButton(self.LabbookGroup)
        self.save_labbook_button.setObjectName(u"save_labbook_button")
        sizePolicy3.setHeightForWidth(self.save_labbook_button.sizePolicy().hasHeightForWidth())
        self.save_labbook_button.setSizePolicy(sizePolicy3)
        self.save_labbook_button.setMinimumSize(QSize(30, 30))
        self.save_labbook_button.setMaximumSize(QSize(30, 30))
        self.save_labbook_button.setFont(font)
        self.save_labbook_button.setStyleSheet(u"")

        self.gridLayout_36.addWidget(self.save_labbook_button, 0, 1, 1, 1)

        self.add_metadata_button = QPushButton(self.LabbookGroup)
        self.add_metadata_button.setObjectName(u"add_metadata_button")
        sizePolicy3.setHeightForWidth(self.add_metadata_button.sizePolicy().hasHeightForWidth())
        self.add_metadata_button.setSizePolicy(sizePolicy3)
        self.add_metadata_button.setMinimumSize(QSize(30, 30))
        self.add_metadata_button.setMaximumSize(QSize(30, 30))
        self.add_metadata_button.setFont(font)
        self.add_metadata_button.setStyleSheet(u"")

        self.gridLayout_36.addWidget(self.add_metadata_button, 0, 0, 1, 1)

        self.save_image = QPushButton(self.LabbookGroup)
        self.save_image.setObjectName(u"save_image")
        sizePolicy3.setHeightForWidth(self.save_image.sizePolicy().hasHeightForWidth())
        self.save_image.setSizePolicy(sizePolicy3)
        self.save_image.setMinimumSize(QSize(30, 30))
        self.save_image.setMaximumSize(QSize(30, 30))
        self.save_image.setFont(font)
        self.save_image.setStyleSheet(u"")

        self.gridLayout_36.addWidget(self.save_image, 0, 2, 1, 1)

        self.start_video_button = QPushButton(self.LabbookGroup)
        self.start_video_button.setObjectName(u"start_video_button")
        sizePolicy3.setHeightForWidth(self.start_video_button.sizePolicy().hasHeightForWidth())
        self.start_video_button.setSizePolicy(sizePolicy3)
        self.start_video_button.setMinimumSize(QSize(30, 30))
        self.start_video_button.setMaximumSize(QSize(30, 30))
        self.start_video_button.setFont(font)
        self.start_video_button.setStyleSheet(u"")

        self.gridLayout_36.addWidget(self.start_video_button, 0, 3, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_36, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.LabbookGroup, 0, 10, 2, 1)

        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_25 = QGridLayout(self.groupBox_6)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.edit_meta = QPushButton(self.groupBox_6)
        self.edit_meta.setObjectName(u"edit_meta")
        self.edit_meta.setMinimumSize(QSize(30, 30))
        self.edit_meta.setMaximumSize(QSize(30, 30))
        self.edit_meta.setStyleSheet(u"")

        self.gridLayout_37.addWidget(self.edit_meta, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_37.addWidget(self.label_4, 0, 1, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_37, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_6, 0, 3, 2, 1)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 0, 15, 1, 1)

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


        self.gridLayout_3.addWidget(self.SweepLevel, 0, 6, 2, 1)

        self.groupBox_7 = QGroupBox(self.frame)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_28 = QGridLayout(self.groupBox_7)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.go_home = QPushButton(self.groupBox_7)
        self.go_home.setObjectName(u"go_home")
        self.go_home.setMinimumSize(QSize(40, 40))
        self.go_home.setMaximumSize(QSize(40, 40))

        self.gridLayout_22.addWidget(self.go_home, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_22.addWidget(self.label_3, 0, 1, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_22, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_7, 0, 0, 2, 1)

        self.groupBox_8 = QGroupBox(self.frame)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_34 = QGridLayout(self.groupBox_8)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.batch_config = QPushButton(self.groupBox_8)
        self.batch_config.setObjectName(u"batch_config")
        self.batch_config.setMinimumSize(QSize(30, 30))
        self.batch_config.setMaximumSize(QSize(30, 30))

        self.gridLayout_33.addWidget(self.batch_config, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")

        self.gridLayout_33.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_34.addLayout(self.gridLayout_33, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_8, 0, 16, 2, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 11, 1, 1)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 0, 13, 1, 1, Qt.AlignVCenter)

        self.DataGroup = QGroupBox(self.frame)
        self.DataGroup.setObjectName(u"DataGroup")
        self.gridLayout_11 = QGridLayout(self.DataGroup)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(1, 3, 1, 3)
        self.DataOptions = QGridLayout()
        self.DataOptions.setObjectName(u"DataOptions")
        self.button_select_data_file = QPushButton(self.DataGroup)
        self.button_select_data_file.setObjectName(u"button_select_data_file")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_select_data_file.sizePolicy().hasHeightForWidth())
        self.button_select_data_file.setSizePolicy(sizePolicy4)
        self.button_select_data_file.setMinimumSize(QSize(30, 30))
        self.button_select_data_file.setMaximumSize(QSize(30, 30))
        self.button_select_data_file.setFont(font)
        self.button_select_data_file.setStyleSheet(u"")

        self.DataOptions.addWidget(self.button_select_data_file, 0, 0, 1, 1)

        self.renameSeries = QPushButton(self.DataGroup)
        self.renameSeries.setObjectName(u"renameSeries")
        self.renameSeries.setMinimumSize(QSize(30, 30))
        self.renameSeries.setMaximumSize(QSize(30, 30))
        self.renameSeries.setStyleSheet(u"")

        self.DataOptions.addWidget(self.renameSeries, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.DataOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.DataGroup, 0, 2, 2, 1)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy5)
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 0, 7, 1, 1)

        self.TransferGroup = QGroupBox(self.frame)
        self.TransferGroup.setObjectName(u"TransferGroup")
        self.gridLayout_21 = QGridLayout(self.TransferGroup)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(1, 3, 1, 3)
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.transfer_to_offline_analysis = QPushButton(self.TransferGroup)
        self.transfer_to_offline_analysis.setObjectName(u"transfer_to_offline_analysis")
        sizePolicy3.setHeightForWidth(self.transfer_to_offline_analysis.sizePolicy().hasHeightForWidth())
        self.transfer_to_offline_analysis.setSizePolicy(sizePolicy3)
        self.transfer_to_offline_analysis.setMinimumSize(QSize(30, 30))
        self.transfer_to_offline_analysis.setMaximumSize(QSize(30, 30))
        self.transfer_to_offline_analysis.setFont(font)
        self.transfer_to_offline_analysis.setStyleSheet(u"")

        self.gridLayout_15.addWidget(self.transfer_to_offline_analysis, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_5 = QLabel(self.TransferGroup)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_15.addWidget(self.label_5, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.TransferGroup, 0, 12, 2, 1)

        self.line_7 = QFrame(self.frame)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_8 = QFrame(self.frame)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 0, 4, 1, 1)

        self.ClassifierGroup = QGroupBox(self.frame)
        self.ClassifierGroup.setObjectName(u"ClassifierGroup")
        self.gridLayout_13 = QGridLayout(self.ClassifierGroup)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(1, 3, 1, 3)
        self.ClassificationOptions = QGridLayout()
        self.ClassificationOptions.setObjectName(u"ClassificationOptions")
        self.classifier_stream = QPushButton(self.ClassifierGroup)
        self.classifier_stream.setObjectName(u"classifier_stream")
        self.classifier_stream.setMinimumSize(QSize(30, 30))
        self.classifier_stream.setMaximumSize(QSize(30, 30))
        self.classifier_stream.setFont(font)
        self.classifier_stream.setStyleSheet(u"")

        self.ClassificationOptions.addWidget(self.classifier_stream, 0, 0, 1, 1)

        self.label_2 = QLabel(self.ClassifierGroup)
        self.label_2.setObjectName(u"label_2")

        self.ClassificationOptions.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_13.addLayout(self.ClassificationOptions, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.ClassifierGroup, 0, 14, 2, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Online_Analysis)

        self.online_analysis.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Online_Analysis)
    # setupUi

    def retranslateUi(self, Online_Analysis):
        Online_Analysis.setWindowTitle(QCoreApplication.translate("Online_Analysis", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Online_Analysis", u"Data View", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Online_Analysis", u"Online Analysis", None))
        self.groupBox.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbbook Table", None))
        self.label_9.setText(QCoreApplication.translate("Online_Analysis", u"Selected Experiment Image", None))
        self.label_13.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Recording GIF Quality", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Online_Analysis", u"Labbook", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Online_Analysis", u"Series", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbook", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Online_Analysis", u"Experiments", None))
        self.transfer_into_db_button.setText(QCoreApplication.translate("Online_Analysis", u"Transfer into DB", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Online_Analysis", u"Cell Image", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.Transfer), QCoreApplication.translate("Online_Analysis", u"Transfer", None))
        self.PlotGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Plot Options", None))
#if QT_CONFIG(tooltip)
        self.plot_home.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Set the plot back to the original state</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.plot_home.setText("")
#if QT_CONFIG(tooltip)
        self.plot_move.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Pan and move the plot</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.plot_move.setText("")
#if QT_CONFIG(tooltip)
        self.plot_zoom.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Zoom into the plot</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.plot_zoom.setText("")
#if QT_CONFIG(tooltip)
        self.save_plot_online.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Save plot as image (.png)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_plot_online.setText("")
#if QT_CONFIG(tooltip)
        self.show_pgf_file.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Show or hide the PGF information</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.show_pgf_file.setText("")
        self.LabbookGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbook Options", None))
#if QT_CONFIG(tooltip)
        self.save_labbook_button.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>save the labbook as .csv</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_labbook_button.setText("")
#if QT_CONFIG(tooltip)
        self.add_metadata_button.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Add metadata to the labbook</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.add_metadata_button.setText("")
#if QT_CONFIG(tooltip)
        self.save_image.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>save image of cell to .png</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_image.setText("")
#if QT_CONFIG(tooltip)
        self.start_video_button.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>start the gif of the experiment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.start_video_button.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Online_Analysis", u"Edit Metadata", None))
        self.edit_meta.setText("")
        self.label_4.setText(QCoreApplication.translate("Online_Analysis", u"Edit Data", None))
        self.SweepLevel.setTitle(QCoreApplication.translate("Online_Analysis", u"Sweeps", None))
        self.show_sweeps_radio.setText(QCoreApplication.translate("Online_Analysis", u"Sweeps", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Online_Analysis", u"Home", None))
        self.go_home.setText("")
        self.label_3.setText(QCoreApplication.translate("Online_Analysis", u"Go Home", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Online_Analysis", u"Go To", None))
        self.batch_config.setText("")
        self.label.setText(QCoreApplication.translate("Online_Analysis", u"Go To Experimentator", None))
        self.DataGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Data Options", None))
#if QT_CONFIG(tooltip)
        self.button_select_data_file.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Open a .dat or .abf file from Directory</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_select_data_file.setText("")
#if QT_CONFIG(tooltip)
        self.renameSeries.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p><span style=\" font-size:6pt;\">Rename a particular series</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.renameSeries.setText("")
        self.TransferGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Transfer Options", None))
#if QT_CONFIG(tooltip)
        self.transfer_to_offline_analysis.setToolTip(QCoreApplication.translate("Online_Analysis", u"<html><head/><body><p>Start the Transfer into the Offline DataBase</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.transfer_to_offline_analysis.setText("")
        self.label_5.setText(QCoreApplication.translate("Online_Analysis", u"Start Transfer", None))
        self.ClassifierGroup.setTitle(QCoreApplication.translate("Online_Analysis", u"Classifier Options", None))
        self.classifier_stream.setText("")
        self.label_2.setText(QCoreApplication.translate("Online_Analysis", u"ML Classifer", None))
    # retranslateUi

