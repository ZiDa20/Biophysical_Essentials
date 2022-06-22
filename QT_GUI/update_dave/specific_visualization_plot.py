# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specific_visualization_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from groupbox_resizing_class import *

class Ui_result_plot_visualizer(object):
    def setupUi(self, result_plot_visualizer):
        if not result_plot_visualizer.objectName():
            result_plot_visualizer.setObjectName(u"result_plot_visualizer")
        result_plot_visualizer.resize(683, 489)
        self.specific_plot_box = GroupBoxSize(result_plot_visualizer)
        self.specific_plot_box.setObjectName(u"specific_plot_box")
        self.specific_plot_box.setGeometry(QRect(10, 10, 651, 421))
        self.gridLayout_2 = QGridLayout(self.specific_plot_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 7, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 9, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 6, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 8, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 8, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 0, 10, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 7, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 9, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 10, 0, 1, 1)

        self.plot_type = QLabel(self.specific_plot_box)
        self.plot_type.setObjectName(u"plot_type")

        self.gridLayout_2.addWidget(self.plot_type, 1, 8, 1, 1)

        self.plot_layout = QVBoxLayout()
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_2.addLayout(self.plot_layout, 1, 1, 10, 7)

        self.split_data_label = QLabel(self.specific_plot_box)
        self.split_data_label.setObjectName(u"split_data_label")

        self.gridLayout_2.addWidget(self.split_data_label, 4, 8, 1, 1)

        self.plot_type_combo_box = QComboBox(self.specific_plot_box)
        self.plot_type_combo_box.setObjectName(u"plot_type_combo_box")

        self.gridLayout_2.addWidget(self.plot_type_combo_box, 2, 8, 1, 2)

        self.split_data_combo_box = QComboBox(self.specific_plot_box)
        self.split_data_combo_box.setObjectName(u"split_data_combo_box")

        self.gridLayout_2.addWidget(self.split_data_combo_box, 5, 8, 1, 2)

        self.save_plot_button = QPushButton(self.specific_plot_box)
        self.save_plot_button.setObjectName(u"save_plot_button")

        self.gridLayout_2.addWidget(self.save_plot_button, 7, 8, 1, 2)

        self.export_data_button = QPushButton(self.specific_plot_box)
        self.export_data_button.setObjectName(u"export_data_button")

        self.gridLayout_2.addWidget(self.export_data_button, 9, 8, 1, 2)


        self.retranslateUi(result_plot_visualizer)

        QMetaObject.connectSlotsByName(result_plot_visualizer)
    # setupUi

    def retranslateUi(self, result_plot_visualizer):
        result_plot_visualizer.setWindowTitle(QCoreApplication.translate("result_plot_visualizer", u"Form", None))
        self.specific_plot_box.setTitle(QCoreApplication.translate("result_plot_visualizer", u"GroupBox", None))
        self.plot_type.setText(QCoreApplication.translate("result_plot_visualizer", u"Plot Type", None))
        self.split_data_label.setText(QCoreApplication.translate("result_plot_visualizer", u"Split Data", None))
        self.save_plot_button.setText(QCoreApplication.translate("result_plot_visualizer", u"Save Plot", None))
        self.export_data_button.setText(QCoreApplication.translate("result_plot_visualizer", u"Export Data", None))
    # retranslateUi



class ResultPlotVisualizer(QWidget, Ui_result_plot_visualizer):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


        ## manually added
        self.analysis_id = None
        self.analysis_function_id = None
        self.analysis_name = None
        # object where plot data will be stored to be exported easily
        self.export_data_frame = None

