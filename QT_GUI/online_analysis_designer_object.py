# -*- coding: utf-8 -*-

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Online_Analysis(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1751, 961)
        self.online_analysis = QTabWidget(Form)
        self.online_analysis.setObjectName(u"online_analysis")
        self.online_analysis.setGeometry(QRect(-10, 10, 1751, 961))
        self.online_analysis_window = QWidget()
        self.online_analysis_window.setObjectName(u"online_analysis_window")
        self.button_select_data_file = QPushButton(self.online_analysis_window)
        self.button_select_data_file.setObjectName(u"button_select_data_file")
        self.button_select_data_file.setGeometry(QRect(50, 110, 181, 31))
        self.button_switch_to_labbook = QPushButton(self.online_analysis_window)
        self.button_switch_to_labbook.setObjectName(u"button_switch_to_labbook")
        self.button_switch_to_labbook.setGeometry(QRect(50, 830, 181, 31))
        self.tree_tab_widget = QTabWidget(self.online_analysis_window)
        self.tree_tab_widget.setObjectName(u"tree_tab_widget")
        self.tree_tab_widget.setGeometry(QRect(50, 160, 411, 651))
        self.selected_tree_view = QWidget()
        self.selected_tree_view.setObjectName(u"selected_tree_view")
        self.treeWidget = QTreeWidget(self.selected_tree_view)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 0, 411, 631))
        self.tree_tab_widget.addTab(self.selected_tree_view, "")
        self.discarded_tree_view = QWidget()
        self.discarded_tree_view.setObjectName(u"discarded_tree_view")
        self.treeWidget_2 = QTreeWidget(self.discarded_tree_view)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setGeometry(QRect(0, 0, 441, 631))
        self.tree_tab_widget.addTab(self.discarded_tree_view, "")
        self.label_selected_directory = QLabel(self.online_analysis_window)
        self.label_selected_directory.setObjectName(u"label_selected_directory")
        self.label_selected_directory.setGeometry(QRect(270, 110, 481, 31))
        self.button_save_dat_file = QPushButton(self.online_analysis_window)
        self.button_save_dat_file.setObjectName(u"button_save_dat_file")
        self.button_save_dat_file.setGeometry(QRect(250, 830, 181, 31))
        self.button_save_to_offline_analysis = QPushButton(self.online_analysis_window)
        self.button_save_to_offline_analysis.setObjectName(u"button_save_to_offline_analysis")
        self.button_save_to_offline_analysis.setGeometry(QRect(450, 830, 181, 31))
        self.headline_label = QLabel(self.online_analysis_window)
        self.headline_label.setObjectName(u"headline_label")
        self.headline_label.setGeometry(QRect(620, 50, 191, 41))
        font = QFont()
        font.setPointSize(20)
        self.headline_label.setFont(font)
        self.verticalLayoutWidget_4 = QWidget(self.online_analysis_window)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(50, 160, 411, 651))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.online_analysis_tabs = QTabWidget(self.online_analysis_window)
        self.online_analysis_tabs.setObjectName(u"online_analysis_tabs")
        self.online_analysis_tabs.setGeometry(QRect(490, 160, 951, 651))
        self.recorded_series_plot_tab = QWidget()
        self.recorded_series_plot_tab.setObjectName(u"recorded_series_plot_tab")
        self.button_re_center = QPushButton(self.recorded_series_plot_tab)
        self.button_re_center.setObjectName(u"button_re_center")
        self.button_re_center.setGeometry(QRect(40, 20, 71, 51))
        self.button_hold_plot = QPushButton(self.recorded_series_plot_tab)
        self.button_hold_plot.setObjectName(u"button_hold_plot")
        self.button_hold_plot.setGeometry(QRect(40, 80, 71, 51))
        self.button_clear_plot_widget = QPushButton(self.recorded_series_plot_tab)
        self.button_clear_plot_widget.setObjectName(u"button_clear_plot_widget")
        self.button_clear_plot_widget.setGeometry(QRect(40, 140, 71, 51))
        self.verticalLayoutWidget_5 = QWidget(self.recorded_series_plot_tab)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(130, 20, 791, 411))
        self.tree_plot_widget_layout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.tree_plot_widget_layout.setObjectName(u"tree_plot_widget_layout")
        self.tree_plot_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget = QWidget(self.recorded_series_plot_tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(130, 460, 791, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.online_analysis_tabs.addTab(self.recorded_series_plot_tab, "")
        self.fast_online_analysis = QWidget()
        self.fast_online_analysis.setObjectName(u"fast_online_analysis")
        self.online_analysis_tabs.addTab(self.fast_online_analysis, "")
        self.live_recording_tab = QWidget()
        self.live_recording_tab.setObjectName(u"live_recording_tab")
        self.online_analysis_tabs.addTab(self.live_recording_tab, "")
        self.online_analysis.addTab(self.online_analysis_window, "")
        self.labbook_window = QWidget()
        self.labbook_window.setObjectName(u"labbook_window")
        self.verticalLayoutWidget_2 = QWidget(self.labbook_window)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1100, 20, 311, 681))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.image_experiment = QGraphicsView(self.verticalLayoutWidget_2)
        self.image_experiment.setObjectName(u"image_experiment")

        self.verticalLayout_2.addWidget(self.image_experiment)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_9)

        self.add_metadata_button = QPushButton(self.verticalLayoutWidget_2)
        self.add_metadata_button.setObjectName(u"add_metadata_button")

        self.verticalLayout_2.addWidget(self.add_metadata_button)

        self.save_labbook_button = QPushButton(self.verticalLayoutWidget_2)
        self.save_labbook_button.setObjectName(u"save_labbook_button")

        self.verticalLayout_2.addWidget(self.save_labbook_button)

        self.verticalLayoutWidget_3 = QWidget(self.labbook_window)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(460, 20, 631, 681))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.verticalLayoutWidget = QWidget(self.labbook_window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 411, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.online_analysis.addTab(self.labbook_window, "")

        self.retranslateUi(Form)

        self.online_analysis.setCurrentIndex(0)
        self.tree_tab_widget.setCurrentIndex(1)
        self.online_analysis_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_select_data_file.setText(QCoreApplication.translate("Form", u"Select a .Dat File:", None))
        self.button_switch_to_labbook.setText(QCoreApplication.translate("Form", u"Switch to Labbook", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"Remove", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Show", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.tree_tab_widget.setTabText(self.tree_tab_widget.indexOf(self.selected_tree_view), QCoreApplication.translate("Form", u"Selected", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("Form", u"Reinsert", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Form", u"Show", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Object", None));
        self.tree_tab_widget.setTabText(self.tree_tab_widget.indexOf(self.discarded_tree_view), QCoreApplication.translate("Form", u"Discarded", None))
        self.label_selected_directory.setText(QCoreApplication.translate("Form", u"No .dat file selected", None))
        self.button_save_dat_file.setText(QCoreApplication.translate("Form", u"Save Modified .dat File", None))
        self.button_save_to_offline_analysis.setText(QCoreApplication.translate("Form", u"Add Experiment To Offline Analysis", None))
        self.headline_label.setText(QCoreApplication.translate("Form", u"Online Analysis", None))
        self.button_re_center.setText(QCoreApplication.translate("Form", u"Re-Center", None))
        self.button_hold_plot.setText(QCoreApplication.translate("Form", u"Hold", None))
        self.button_clear_plot_widget.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.recorded_series_plot_tab), QCoreApplication.translate("Form", u"Plot Window", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.fast_online_analysis), QCoreApplication.translate("Form", u"Fast Analysis", None))
        self.online_analysis_tabs.setTabText(self.online_analysis_tabs.indexOf(self.live_recording_tab), QCoreApplication.translate("Form", u"Live Recording", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.online_analysis_window), QCoreApplication.translate("Form", u"Online Analysis", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Image of the Experiment", None))
        self.add_metadata_button.setText(QCoreApplication.translate("Form", u"Add Metadata to Labbook", None))
        self.save_labbook_button.setText(QCoreApplication.translate("Form", u"Save Labbook", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Labbook of Experiment", None))
        self.online_analysis.setTabText(self.online_analysis.indexOf(self.labbook_window), QCoreApplication.translate("Form", u"Labbook", None))
    # retranslateUi


