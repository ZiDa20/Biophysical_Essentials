# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trial_specific_analysis_tab_05022023.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLayout,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

from Frontend.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild

class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1137, 920)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpecificAnalysisTab.sizePolicy().hasHeightForWidth())
        SpecificAnalysisTab.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        SpecificAnalysisTab.setFont(font)
        self.gridLayout_5 = QGridLayout(SpecificAnalysisTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 4, -1, 4)
        self.stackedWidget = QStackedWidget(SpecificAnalysisTab)
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
        self.groupBox_5.setMaximumSize(QSize(5000, 16777215))
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


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy3)
        self.gridLayout_10 = QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.calc_animation_layout = QGridLayout()
        self.calc_animation_layout.setObjectName(u"calc_animation_layout")

        self.gridLayout_10.addLayout(self.calc_animation_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 6, 5, 1)

        self.groupBox = QGroupBox(SpecificAnalysisTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.analysi_grid = QGridLayout()
        self.analysi_grid.setObjectName(u"analysi_grid")
        self.analysis_button_grid = QGridLayout()
        self.analysis_button_grid.setObjectName(u"analysis_button_grid")
        self.select_series_analysis_functions = QPushButton(self.groupBox)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy4)
        self.select_series_analysis_functions.setMinimumSize(QSize(150, 150))
        self.select_series_analysis_functions.setMaximumSize(QSize(150, 150))

        self.analysis_button_grid.addWidget(self.select_series_analysis_functions, 0, 0, 1, 1)


        self.analysi_grid.addLayout(self.analysis_button_grid, 0, 1, 1, 1)

        self.analysis_stacked_widget = QStackedWidget(self.groupBox)
        self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
        self.analysis_stacked_widget.setEnabled(True)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.analysis_stacked_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.analysis_stacked_widget.addWidget(self.page_4)

        self.analysi_grid.addWidget(self.analysis_stacked_widget, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.analysi_grid, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 7, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = TreeBuild(SpecificAnalysisTab)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 4, 1, 1)


        self.retranslateUi(SpecificAnalysisTab)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
#if QT_CONFIG(accessibility)
        SpecificAnalysisTab.setAccessibleName(QCoreApplication.translate("SpecificAnalysisTab", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        SpecificAnalysisTab.setAccessibleDescription(QCoreApplication.translate("SpecificAnalysisTab", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis", None))
#if QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setAccessibleName(QCoreApplication.translate("SpecificAnalysisTab", u"analysis_grid_bt", None))
#endif // QT_CONFIG(accessibility)
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"+", None))
    # retranslateUi

