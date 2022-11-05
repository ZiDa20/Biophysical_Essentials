# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'online_analysis_notebook.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu
from groupbox_resizing_class import GroupBoxSize

class Ui_Online_Analysis(object):
    def setupUi(self, Online_Analysis):
        if not Online_Analysis.objectName():
            Online_Analysis.setObjectName(u"Online_Analysis")
        Online_Analysis.resize(1434, 900)
        self.gridLayout_5 = QGridLayout(Online_Analysis)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(Online_Analysis)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.online_analysis = QTabWidget(Online_Analysis)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        self.gridLayout_19 = QGridLayout(self.online_analysis_window)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.show_pgf_file = QPushButton(self.online_analysis_window)
        self.show_pgf_file.setObjectName(u"show_pgf_file")
        self.show_pgf_file.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.show_pgf_file, 0, 1, 1, 1)

        self.classifier_stream = QPushButton(self.online_analysis_window)
        self.classifier_stream.setObjectName(u"classifier_stream")
        self.classifier_stream.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.classifier_stream, 0, 3, 1, 1)

        self.button_select_data_file = QPushButton(self.online_analysis_window)
        self.button_select_data_file.setObjectName(u"button_select_data_file")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_select_data_file.sizePolicy().hasHeightForWidth())
        self.button_select_data_file.setSizePolicy(sizePolicy)
        self.button_select_data_file.setMinimumSize(QSize(150, 0))

        self.gridLayout_11.addWidget(self.button_select_data_file, 0, 0, 1, 1)

        self.transfer_to_offline_analysis = QPushButton(self.online_analysis_window)
        self.transfer_to_offline_analysis.setObjectName(u"transfer_to_offline_analysis")
        sizePolicy.setHeightForWidth(self.transfer_to_offline_analysis.sizePolicy().hasHeightForWidth())
        self.transfer_to_offline_analysis.setSizePolicy(sizePolicy)
        self.transfer_to_offline_analysis.setMinimumSize(QSize(50, 30))
        self.transfer_to_offline_analysis.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.transfer_to_offline_analysis, 0, 4, 1, 1)

        self.save_plot_online = QPushButton(self.online_analysis_window)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.save_plot_online, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_11, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.online_analysis_window)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(300, 0))
        self.groupBox_4.setMaximumSize(QSize(448, 16777215))
        self.gridLayout_18 = QGridLayout(self.groupBox_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_18.setContentsMargins(0, -1, -1, -1)
        self.tree_layouting_change = QGridLayout()
        self.tree_layouting_change.setObjectName(u"tree_layouting_change")
        self.tree_tab_widget = QTabWidget(self.groupBox_4)
        self.tree_tab_widget.setObjectName(u"tree_tab_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tree_tab_widget.sizePolicy().hasHeightForWidth())
        self.tree_tab_widget.setSizePolicy(sizePolicy2)
        self.tree_tab_widget.setMinimumSize(QSize(300, 600))
        self.tree_tab_widget.setStyleSheet(u"")
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.verticalLayout_2 = QVBoxLayout(self.selected_tree_view)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.selected_tree_view)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.tree_tab_widget.addTab(self.selected_tree_view, "")
        self.discarded_tree_view = QWidget()
        self.discarded_tree_view.setObjectName(u"discarded_tree_view")
        self.gridLayout_4 = QGridLayout(self.discarded_tree_view)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.treeWidget_2 = QTreeWidget(self.discarded_tree_view)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        sizePolicy1.setHeightForWidth(self.treeWidget_2.sizePolicy().hasHeightForWidth())
        self.treeWidget_2.setSizePolicy(sizePolicy1)
        self.treeWidget_2.setMinimumSize(QSize(300, 0))
        self.treeWidget_2.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.treeWidget_2, 0, 0, 1, 1)

        self.tree_tab_widget.addTab(self.discarded_tree_view, "")

        self.tree_layouting_change.addWidget(self.tree_tab_widget, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.tree_layouting_change, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_2 = GroupBoxSize(self.online_analysis_window)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(1500, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.online_analysis_tabs = QTabWidget(self.groupBox_2)
        self.online_analysis_tabs.setObjectName(u"online_analysis_tabs")
        self.recorded_series_plot_tab = QWidget()
        self.recorded_series_plot_tab.setObjectName(u"recorded_series_plot_tab")
        self.gridLayout_2 = QGridLayout(self.recorded_series_plot_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolbar_layout = QGridLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_widget = QWidget(self.recorded_series_plot_tab)
        self.toolbar_widget.setObjectName(u"toolbar_widget")
        self.toolbar_widget.setMinimumSize(QSize(50, 0))
        self.toolbar_widget.setMaximumSize(QSize(50, 16777215))

        self.toolbar_layout.addWidget(self.toolbar_widget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.toolbar_layout, 0, 2, 3, 1)

        self.tree_plot_widget_layout = QVBoxLayout()
        self.tree_plot_widget_layout.setObjectName(u"tree_plot_widget_layout")
        self.succesfull_import = QCustomSlideMenu(self.recorded_series_plot_tab)
        self.succesfull_import.setObjectName(u"succesfull_import")

        self.tree_plot_widget_layout.addWidget(self.succesfull_import)

        self.label = QLabel(self.recorded_series_plot_tab)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.tree_plot_widget_layout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.tree_plot_widget_layout, 0, 1, 3, 1)

        self.online_analysis_tabs.addTab(self.recorded_series_plot_tab, "")
        self.live_recording_tab = QWidget()
        self.live_recording_tab.setObjectName(u"live_recording_tab")
        self.gridLayout = QGridLayout(self.live_recording_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(5, 300, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_10, 1, 0, 1, 1)

        self.online_analysis_tabs.addTab(self.live_recording_tab, "")
        self.fast_online_analysis = QWidget()
        self.fast_online_analysis.setObjectName(u"fast_online_analysis")
        self.online_analysis_tabs.addTab(self.fast_online_analysis, "")

        self.gridLayout_8.addWidget(self.online_analysis_tabs, 0, 1, 2, 1)


        self.gridLayout_19.addWidget(self.groupBox_2, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(5, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.gridLayout_20 = QGridLayout(self.labbook_window)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.groupBox_5 = QGroupBox(self.labbook_window)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setMinimumSize(QSize(300, 0))
        self.groupBox_5.setMaximumSize(QSize(448, 16777215))
        self.gridLayout_17 = QGridLayout(self.groupBox_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_17.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.save_labbook_button = QPushButton(self.labbook_window)
        self.save_labbook_button.setObjectName(u"save_labbook_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.save_labbook_button.sizePolicy().hasHeightForWidth())
        self.save_labbook_button.setSizePolicy(sizePolicy3)
        self.save_labbook_button.setMinimumSize(QSize(150, 0))

        self.gridLayout_10.addWidget(self.save_labbook_button, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.labbook_window)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.labbook_window)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.pushButton_2, 0, 3, 1, 1)

        self.add_metadata_button = QPushButton(self.labbook_window)
        self.add_metadata_button.setObjectName(u"add_metadata_button")
        sizePolicy3.setHeightForWidth(self.add_metadata_button.sizePolicy().hasHeightForWidth())
        self.add_metadata_button.setSizePolicy(sizePolicy3)
        self.add_metadata_button.setMinimumSize(QSize(150, 0))

        self.gridLayout_10.addWidget(self.add_metadata_button, 0, 0, 1, 1)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy5.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy5)

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

        self.online_analysis.addTab(self.labbook_window, "")

        self.gridLayout_5.addWidget(self.online_analysis, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.retranslateUi(Online_Analysis)

        self.online_analysis.setCurrentIndex(0)
        self.tree_tab_widget.setCurrentIndex(0)
        self.online_analysis_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Online_Analysis)
    # setupUi

    def retranslateUi(self, Online_Analysis):
        Online_Analysis.setWindowTitle(QCoreApplication.translate("Online_Analysis", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Online_Analysis", u"Online Analysis ", None))
        self.show_pgf_file.setText(QCoreApplication.translate("Online_Analysis", u"Show PGF File", None))
        self.classifier_stream.setText(QCoreApplication.translate("Online_Analysis", u"Classifier Stream", None))
        self.button_select_data_file.setText(QCoreApplication.translate("Online_Analysis", u"Open .Dat File", None))
        self.transfer_to_offline_analysis.setText(QCoreApplication.translate("Online_Analysis", u"Transfer to offline Analysis", None))
        self.save_plot_online.setText(QCoreApplication.translate("Online_Analysis", u"Save Plot", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Online_Analysis", u"Experiment Hierachy", None))
#if QT_CONFIG(accessibility)
        self.tree_tab_widget.setAccessibleName(QCoreApplication.translate("Online_Analysis", u"tab_widgets", None))
#endif // QT_CONFIG(accessibility)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Online_Analysis", u"Remove", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Online_Analysis", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Online_Analysis", u"Object", None));
        self.tree_tab_widget.setTabText(self.tree_tab_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Online_Analysis", u"Selected", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Online_Analysis", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Online_Analysis", u"Show", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Online_Analysis", u"Object", None));
        self.tree_tab_widget.setTabText(self.tree_tab_widget.indexOf(self.discarded_tree_view), QCoreApplication.translate("Online_Analysis", u"Discarded", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Online_Analysis", u"Visualization of the Traces", None))
        self.label.setText(QCoreApplication.translate("Online_Analysis", u"Load a File to Plot Data", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.recorded_series_plot_tab), QCoreApplication.translate("Online_Analysis", u"Plot Window", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.live_recording_tab), QCoreApplication.translate("Online_Analysis", u"Live Recording", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.fast_online_analysis), QCoreApplication.translate("Online_Analysis", u"Fast Analysis", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Online_Analysis", u"Online Analysis", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Online_Analysis", u"TreeView Experiment", None))
        self.save_labbook_button.setText(QCoreApplication.translate("Online_Analysis", u"Save Labbook", None))
        self.pushButton.setText(QCoreApplication.translate("Online_Analysis", u"Save Image", None))
        self.pushButton_2.setText(QCoreApplication.translate("Online_Analysis", u"Save Gif", None))
        self.add_metadata_button.setText(QCoreApplication.translate("Online_Analysis", u"Add Metadata to Labbook", None))
        self.groupBox.setTitle(QCoreApplication.translate("Online_Analysis", u"Labbbook Table", None))
        self.label_9.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Image", None))
        self.label_13.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Temporal GIF", None))
        self.label_12.setText(QCoreApplication.translate("Online_Analysis", u"Experiment Report", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Online_Analysis", u"Labbook", None))
    # retranslateUi
