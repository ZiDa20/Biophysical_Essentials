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
from PySide6.QtWidgets import (QAbstractScrollArea, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLayout, QMdiArea, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget, QMdiSubWindow, QDockWidget, QMainWindow, QStatusBar, QSizeGrip)

from QT_GUI.OfflineAnalysis.CustomWidget.analysis_table_widget import Analysis_Function_Table

from QT_GUI.OfflineAnalysis.ui_py.treebuild_widget  import TreeBuild


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
                #self.CameraMDI.setSizePolicy(sizePolicy)
                self.CameraMDI.setMinimumSize(QSize(100, 500))
                self.CameraMDI.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

                self.trial_main = QMainWindow()
                #self.trial_main.setStatusBar(self.statusBar)
                self.PlotWindow = QMdiSubWindow()
                self.PlotWindow.setWidget(self.trial_main)
                self.statusBar = QStatusBar()
                
                self.PlotWindow.setObjectName(u"PlotWindow")
                self.PlotWindow.setMinimumSize(QSize(16777215,16777215))
                #sizePolicy.setHeightForWidth(self.PlotWindow.sizePolicy().hasHeightForWidth())
                self.PlotWindow.setMaximumSize(QSize(16777215, 16777215))
                #self.PlotWindow.setSizePolicy(sizePolicy)
                self.PlotWindow.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.gridLayout_13 = QGridLayout()
                self.gridLayout_13.setObjectName(u"gridLayout_13")
                
                self.treebuild= TreeBuild(self.PlotWindow)
                self.treebuild.setObjectName(u"widget")
                self.treebuild.setMinimumSize(QSize(300, 300))
                #self.widget.groupBox_4.setMaximumSize(QSize(16777215, 16777215))
                #self.widget.setMaximumSize(QSize(16777215, 16777215))
                #self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                #self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)
                self.subwindow = QMdiSubWindow()
                self.dock_widget = QDockWidget("Dock Widget", self)
                self.plot_widget = QWidget()
                self.subwindow.setObjectName(u"subwindow")
                self.grid = QSizeGrip(self.subwindow)
                #sizePolicy.setHeightForWidth(self.subwindow.sizePolicy().hasHeightForWidth())
                #self.subwindow.setSizePolicy(sizePolicy)
                #self.subwindow.setMinimumSize(QSize(600, 800))
                self.gridLayout_4 = QGridLayout()
                self.gridLayout_4.setObjectName(u"gridLayout_4")
                self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
                self.stackedWidget = QStackedWidget()
                self.stackedWidget.setObjectName(u"stackedSub")
                self.stackedWidget.setAccessibleName("substack")
                self.subwindow_layout = QVBoxLayout(self.treebuild.groupBox_4)
                self.subwindow_layout.addWidget(self.grid, alignment=Qt.AlignBottom | Qt.AlignLeft)
                self.subwindow.setMinimumSize(QSize(0, 0))
                self.subwindow.setMaximumSize(QSize(350, 16777215))
                self.subwindow.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                #self.stackedWidget.setMinimumSize(QSize(400,700))
                #sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
                #self.stackedWidget.setSizePolicy(sizePolicy)
                self.stackedWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                
                self.page = QWidget()
                self.page.setObjectName(u"page")
                sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
                self.analysis_function = QGridLayout()
                self.analysis_function.setObjectName(u"analysis_function")

                self.gridLayout_7.addLayout(self.analysis_function, 1, 0, 1, 1)

                self.horizontalLayout = QHBoxLayout()
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout.addItem(self.horizontalSpacer)

                self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                self.horizontalLayout.addItem(self.horizontalSpacer_3)

                self.dock_button = QPushButton("Dock me",self.groupBox_5)
                self.horizontalLayout.addWidget(self.dock_button)
        

                self.tile_button = QPushButton("tile me",self.groupBox_5)
                self.horizontalLayout.addWidget(self.tile_button)

                self.gridLayout_7.addLayout(self.horizontalLayout, 2, 0, 1, 1)

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
                sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
                self.dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
                self.dock_widget.setWidget(self.stackedWidget)
                self.stackedWidget.addWidget(self.page_2)


                self.analysis_functions = Analysis_Function_Table(SpecificAnalysisTab)
                self.analysis_functions.setObjectName(u"analysis_functions")
                


                #self.analysi_grid.addLayout(self.select_series_analysis_functions)
                #self.analysi_grid.addLayout(self.analysis_button_grid, 0, 1, 1, 1)
                #self.analysis_stacked_widget = QStackedWidget(self.groupBox)
                #self.analysis_stacked_widget.setObjectName(u"analysis_stacked_widget")
                #self.analysis_stacked_widget.setEnabled(True)
                #self.page_3 = QWidget()
                #self.page_3.setObjectName(u"page_3")
                #self.analysis_stacked_widget.addWidget(self.page_3)
                #self.page_4 = QWidget()
                #self.page_4.setObjectName(u"page_4")
                #self.analysis_stacked_widget.addWidget(self.page_4)
                #self.analysi_grid.addWidget(self.analysis_stacked_widget, 0, 0, 1, 1)
                
                #self.gridLayout_9.addLayout(self.analysi_grid, 0, 0, 1, 1)

                self.trial_main.addDockWidget(Qt.TopDockWidgetArea,self.dock_widget)
                self.CameraMDI.addSubWindow(self.PlotWindow)
                self.subwindow.setWidget(self.treebuild)
                self.CameraMDI.addSubWindow(self.subwindow)

                

                #self.subwindow_calc.setWidget(self.groupBox)
                #self.CameraMDI.addSubWindow(self.subwindow_calc)
                self.gridLayout_2.addWidget(self.analysis_functions,0,1)

                #self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)

                
                self.gridLayout_2.addWidget(self.CameraMDI, 0, 0, 1, 1)
                self.stackedWidget.setCurrentIndex(0)
                

                self.retranslateUi(SpecificAnalysisTab)
                QMetaObject.connectSlotsByName(SpecificAnalysisTab)
        # setupUi

        def retranslateUi(self, SpecificAnalysisTab):
                SpecificAnalysisTab.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Form", None))
                self.PlotWindow.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Plot", None))
                self.subwindow.setWindowTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Analysis Tree", None))
                self.groupBox_5.setTitle(QCoreApplication.translate("SpecificAnalysisTab", u"Data View", None))
                #self.start_analysis_button.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Start Analysis", None))
                #self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Add New Analysis Functions(s)", None))
                #self.select_series_analysis_functions.setText(QCoreApplication.translate("SpecificAnalysisTab", u"Functions", None))
        # retranslateUi




class SpecificAnalysisTab(QWidget, Ui_SpecificAnalysisTab):
    def __init__(self,frontend, parent=None):
        QWidget.__init__(self,  parent)
        self.setupUi(self)
        #add this to promote 
        self.frontend_style = frontend
        #self.analysis_table_widget = AnalysisFunctionTable()
        self.data_table = []
        self.treebuild.groupBox_4.setStyleSheet("border-radius: 0px;")
        #self.subwindow_calc.hide()
        
        # this needs to be added to the stylesheets
        self.CameraMDI.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.CameraMDI.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.CameraMDI.tileSubWindows()
        self.title_bar_widget = self.dock_widget.titleBarWidget()
        self.dock_widget.setTitleBarWidget(QWidget(self.dock_widget))
        self.PlotWindow.setWindowFlags(self.PlotWindow.windowFlags() | Qt.WindowMinMaxButtonsHint)
        self.dock_button.clicked.connect(self.undock_me)
        self.dock_widget.topLevelChanged.connect(self.remove_title_bar_dock)
        self.tile_button.clicked.connect(self.show_and_tile)
        self.floating: bool = False
        self.frontend_style.set_pop_up_dialog_style_sheet(self)

        # Set the minimum height of each cell to 50 pixels
        # Set the vertical size policy of the widgets to Minimum
        #for i in range(1,self.analysis_button_grid.rowCount()):
        #    for j in range(self.analysis_button_grid.columnCount()):
        #        widget = self.analysis_button_grid.itemAtPosition(i, j).widget()
        #        widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)


        self.normalization_values = None
        #self.show_and_tile()

    def show_and_tile(self):
        """ Should draw subwindows next to each other"""
        
        # Get the size and position of the subwindow
        subwindow_rect = self.subwindow.frameGeometry()
        subwindow_pos = subwindow_rect.topRight()

        # Adjust the position of the plot window
        plotwindow_pos = self.PlotWindow.pos()
        plotwindow_pos.setX(subwindow_pos.x() + 10)  # Adjust the X position as needed

        # Resize the plot window
        self.PlotWindow.resize(self.CameraMDI.width()-self.subwindow.width(), self.CameraMDI.height())

        # Move the plot window next to the subwindow
        self.PlotWindow.move(plotwindow_pos)

        print("Tiling subwindows")
    def undock_me(self):
        """_summary_: This is a handler to dock and undock
        """
        if self.floating is not True:
            self.floating = True
            self.dock_widget.setFloating(self.floating)
            self.dock_widget.setTitleBarWidget(self.title_bar_widget)
            self.PlotWindow.showMinimized()
                    
        else:
            self.floating = False
            self.dock_widget.setFloating(self.floating)
            self.dock_widget.setTitleBarWidget(QWidget(self.dock_widget))
        
    def remove_title_bar_dock(self):
        """_summary_: Should remove the title bar whenver the toplevelchanged signal is initiated
        """
        self.dock_widget.setTitleBarWidget(QWidget(self.dock_widget))
        self.floating = False
            
        
