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
        result_plot_visualizer.resize(558, 415)
        self.gridLayout = QGridLayout(result_plot_visualizer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.specific_plot_box = QGroupBox(result_plot_visualizer)
        self.specific_plot_box.setObjectName(u"specific_plot_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specific_plot_box.sizePolicy().hasHeightForWidth())
        self.specific_plot_box.setSizePolicy(sizePolicy)
        self.specific_plot_box.setMaximumSize(QSize(16777215, 400))
        self.gridLayout_2 = QGridLayout(self.specific_plot_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.plot_layout = QVBoxLayout()
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_2.addLayout(self.plot_layout, 2, 1, 5, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.Control_button = QGroupBox(self.specific_plot_box)
        self.Control_button.setObjectName(u"Control_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Control_button.sizePolicy().hasHeightForWidth())
        self.Control_button.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.Control_button)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_type = QLabel(self.Control_button)
        self.plot_type.setObjectName(u"plot_type")

        self.verticalLayout.addWidget(self.plot_type)

        self.plot_type_combo_box = QComboBox(self.Control_button)
        self.plot_type_combo_box.setObjectName(u"plot_type_combo_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plot_type_combo_box.sizePolicy().hasHeightForWidth())
        self.plot_type_combo_box.setSizePolicy(sizePolicy2)
        self.plot_type_combo_box.setMinimumSize(QSize(150, 0))
        self.plot_type_combo_box.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.plot_type_combo_box)

        self.split_data_label = QLabel(self.Control_button)
        self.split_data_label.setObjectName(u"split_data_label")

        self.verticalLayout.addWidget(self.split_data_label)

        self.split_data_combo_box = QComboBox(self.Control_button)
        self.split_data_combo_box.setObjectName(u"split_data_combo_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.split_data_combo_box.sizePolicy().hasHeightForWidth())
        self.split_data_combo_box.setSizePolicy(sizePolicy3)
        self.split_data_combo_box.setMinimumSize(QSize(150, 0))
        self.split_data_combo_box.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.split_data_combo_box)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.Control_button)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.export_data_button = QPushButton(self.Control_button)
        self.export_data_button.setObjectName(u"export_data_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.export_data_button.sizePolicy().hasHeightForWidth())
        self.export_data_button.setSizePolicy(sizePolicy4)
        self.export_data_button.setMinimumSize(QSize(150, 50))
        self.export_data_button.setMaximumSize(QSize(25, 16777215))
        self.export_data_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/Logo/export_plot.png);\n"
"background-color: rgba(255,255,255,0);\n"
"background-repeat:None;\n"
"border: 1px #fff5cc;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.export_data_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_5)

        self.save_plot_button = QPushButton(self.Control_button)
        self.save_plot_button.setObjectName(u"save_plot_button")
        sizePolicy4.setHeightForWidth(self.save_plot_button.sizePolicy().hasHeightForWidth())
        self.save_plot_button.setSizePolicy(sizePolicy4)
        self.save_plot_button.setMinimumSize(QSize(150, 50))
        self.save_plot_button.setStyleSheet(u"background-image: url(../QT_GUI/Button/Logo/data_button.png);\n"
"background-color: rgba(255,255,255,0);\n"
"background-repeat:None;\n"
"border: 1px #fff5cc;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.save_plot_button)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Control_button, 2, 5, 4, 1)


        self.gridLayout.addWidget(self.specific_plot_box, 0, 1, 1, 1)


        self.retranslateUi(result_plot_visualizer)

        QMetaObject.connectSlotsByName(result_plot_visualizer)
    # setupUi

    def retranslateUi(self, result_plot_visualizer):
        result_plot_visualizer.setWindowTitle(QCoreApplication.translate("result_plot_visualizer", u"Form", None))
        self.specific_plot_box.setTitle(QCoreApplication.translate("result_plot_visualizer", u"GroupBox", None))
        self.Control_button.setTitle(QCoreApplication.translate("result_plot_visualizer", u"Controls", None))
        self.plot_type.setText(QCoreApplication.translate("result_plot_visualizer", u"Plot Type:", None))
        self.split_data_label.setText(QCoreApplication.translate("result_plot_visualizer", u"Split Data:", None))
        self.label.setText(QCoreApplication.translate("result_plot_visualizer", u"Save Data:", None))
        self.export_data_button.setText(QCoreApplication.translate("result_plot_visualizer", u"     Save Data", None))
        self.save_plot_button.setText(QCoreApplication.translate("result_plot_visualizer", u"    Save Plot", None))
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

