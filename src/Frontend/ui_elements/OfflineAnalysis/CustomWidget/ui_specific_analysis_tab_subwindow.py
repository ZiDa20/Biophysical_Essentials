# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specific_analysis_tab_subwindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QLayout, QMdiArea, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from Frontend.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild

class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1282, 955)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpecificAnalysisTab.sizePolicy().hasHeightForWidth())
        SpecificAnalysisTab.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout_2 = QGridLayout(SpecificAnalysisTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.CameraMDI = QMdiArea(SpecificAnalysisTab)
        self.CameraMDI.setObjectName(u"CameraMDI")
        sizePolicy.setHeightForWidth(self.CameraMDI.sizePolicy().hasHeightForWidth())
        self.CameraMDI.setSizePolicy(sizePolicy)
        self.CameraMDI.setMinimumSize(QSize(400, 500))
        self.CameraMDI.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.CameraWindow = QWidget()
        self.CameraWindow.setObjectName(u"CameraWindow")
        sizePolicy.setHeightForWidth(self.CameraWindow.sizePolicy().hasHeightForWidth())
        self.CameraWindow.setSizePolicy(sizePolicy)
        self.CameraWindow.setMinimumSize(QSize(600, 600))
        self.gridLayout_13 = QGridLayout(self.CameraWindow)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget = TreeBuild(self.CameraWindow)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 600))
        self.widget.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)

        self.CameraMDI.addSubWindow(self.CameraWindow)
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        sizePolicy.setHeightForWidth(self.subwindow.sizePolicy().hasHeightForWidth())
        self.subwindow.setSizePolicy(sizePolicy)
        self.subwindow.setMinimumSize(QSize(600, 800))
        self.gridLayout_4 = QGridLayout(self.subwindow)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.subwindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(6, 0, 6, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_5 = QGroupBox(self.page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setFocusPolicy(Qt.NoFocus)
        self.groupBox_5.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 6, 0, 6)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.series_plot = QVBoxLayout()
        self.series_plot.setObjectName(u"series_plot")
        self.series_plot.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.gridLayout.addLayout(self.series_plot, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.analysis_function = QGridLayout()
        self.analysis_function.setObjectName(u"analysis_function")

        self.gridLayout_7.addLayout(self.analysis_function, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.start_analysis_button = QPushButton(self.groupBox_5)
        self.start_analysis_button.setObjectName(u"start_analysis_button")
        self.start_analysis_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.start_analysis_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.select_series_analysis_functions = QPushButton(self.groupBox_5)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.select_series_analysis_functions)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_7.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.dock_button = QPushButton(self.groupBox_5)
        self.dock_button.setObjectName(u"dock_button")
        self.dock_button.setMinimumSize(QSize(30, 30))
        self.dock_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_7.addWidget(self.dock_button, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy4)
        self.gridLayout_10 = QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.calc_animation_layout = QGridLayout()
        self.calc_animation_layout.setObjectName(u"calc_animation_layout")

        self.gridLayout_10.addLayout(self.calc_animation_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.CameraMDI.addSubWindow(self.subwindow)

        self.gridLayout_2.addWidget(self.CameraMDI, 0, 0, 1, 1)


        self.retranslateUi(SpecificAnalysisTab)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.CameraWindow.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Subwindow", None))
        self.subwindow.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Subwindow", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add New Analysis Functions(s)", None))
        self.dock_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"D", None))
    # retranslateUi

