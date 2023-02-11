from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget, QTabWidget)

from QT_GUI.OfflineAnalysis.CustomWidget.analysis_function_table_designer import AnalysisFunctionTable
from QT_GUI.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild

class Ui_SpecificAnalysisTab(object):
    def setupUi(self, SpecificAnalysisTab):
        if not SpecificAnalysisTab.objectName():
            SpecificAnalysisTab.setObjectName(u"SpecificAnalysisTab")
        SpecificAnalysisTab.resize(1262, 920)
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

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 3, 5, 1)

        self.tabWidget = QTabWidget(SpecificAnalysisTab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(900, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = TreeBuild(self.tab)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(100, 0))
        self.widget.setMaximumSize(QSize(600, 16777215))

        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.analysis_function = QGridLayout()
        self.analysis_function.setObjectName(u"analysis_function")

        self.gridLayout_4.addLayout(self.analysis_function, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.start_analysis_button = QPushButton(self.tab_2)
        self.start_analysis_button.setObjectName(u"start_analysis_button")
        self.start_analysis_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.start_analysis_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.select_series_analysis_functions = QPushButton(self.tab_2)
        self.select_series_analysis_functions.setObjectName(u"select_series_analysis_functions")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.select_series_analysis_functions.sizePolicy().hasHeightForWidth())
        self.select_series_analysis_functions.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.select_series_analysis_functions)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 2, 1, 1)


        self.retranslateUi(SpecificAnalysisTab)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SpecificAnalysisTab)
    # setupUi

    def retranslateUi(self, SpecificAnalysisTab):
        SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SpecificAnalysisTab", u"Experiments", None))
        self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
        self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add New Analysis Functions(s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SpecificAnalysisTab", u"Analysis", None))
    # retranslateUi


class SpecificAnalysisTab(QWidget, Ui_SpecificAnalysisTab):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        #add this to promote 
        self.analysis_table_widget = AnalysisFunctionTable()