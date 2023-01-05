# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specific_analysis_tab_12052022.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from treebuild_widget import TreeBuild


class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1227, 854)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout_5 = QGridLayout(SpecificAnalysisTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.start_analysis_button = QPushButton(SpecificAnalysisTab)
        self.start_analysis_button.setObjectName(u"start_analysis_button")
        self.start_analysis_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.start_analysis_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.select_series_analysis_functions = QPushButton(SpecificAnalysisTab)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.select_series_analysis_functions)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.groupBox_5 = QGroupBox(SpecificAnalysisTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.groupBox_5.setFocusPolicy(Qt.NoFocus)
        self.groupBox_5.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.series_plot = QVBoxLayout()
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout_7.addLayout(self.series_plot, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = TreeBuild(SpecificAnalysisTab)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(100, 0))

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 5, 1)

        self.analysis_function = QGridLayout()
        self.analysis_function.setObjectName(u"analysis_function")

        self.gridLayout_5.addLayout(self.analysis_function, 1, 1, 1, 1)


        self.retranslateUi(SpecificAnalysisTab)

        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add New Analysis Functions(s)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
    # retranslateUi

