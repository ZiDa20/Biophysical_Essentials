# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics_function_table.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_StatisticsTable(object):
    def setupUi(self, StatisticsTable):
        if not StatisticsTable.objectName():
            StatisticsTable.setObjectName(u"StatisticsTable")
        StatisticsTable.resize(1152, 711)
        self.gridLayout = QGridLayout(StatisticsTable)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(StatisticsTable)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 500))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statistics_table_widget = QTableWidget(self.groupBox)
        if (self.statistics_table_widget.columnCount() < 5):
            self.statistics_table_widget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.statistics_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.statistics_table_widget.setObjectName(u"statistics_table_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statistics_table_widget.sizePolicy().hasHeightForWidth())
        self.statistics_table_widget.setSizePolicy(sizePolicy1)
        self.statistics_table_widget.horizontalHeader().setVisible(True)
        self.statistics_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.statistics_table_widget.horizontalHeader().setDefaultSectionSize(125)
        self.statistics_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.statistics_table_widget.horizontalHeader().setStretchLastSection(False)
        self.statistics_table_widget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.statistics_table_widget)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 100))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.statistics_result_grid = QGridLayout()
        self.statistics_result_grid.setObjectName(u"statistics_result_grid")

        self.gridLayout_4.addLayout(self.statistics_result_grid, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(StatisticsTable)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StatisticsTable)
    # setupUi

    def retranslateUi(self, StatisticsTable):
        StatisticsTable.setWindowTitle(QCoreApplication.translate("StatisticsTable", u"Form", None))
        self.label.setText(QCoreApplication.translate("StatisticsTable", u"WELCOME TO THE STATISTICS FEATURE", None))
        self.groupBox.setTitle(QCoreApplication.translate("StatisticsTable", u"Analysis Function Selection", None))
        ___qtablewidgetitem = self.statistics_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StatisticsTable", u"Select", None));
        ___qtablewidgetitem1 = self.statistics_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StatisticsTable", u"Analysis Function", None));
        ___qtablewidgetitem2 = self.statistics_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("StatisticsTable", u"Meta Data Selection", None));
        ___qtablewidgetitem3 = self.statistics_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("StatisticsTable", u"Data Distribution", None));
        ___qtablewidgetitem4 = self.statistics_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("StatisticsTable", u"Statistical Model", None));
        self.label_2.setText(QCoreApplication.translate("StatisticsTable", u" We have scanned your analysis functions and meta data selection and entered the data in the table below. \n"
" We have also analyzed the data distribution by running the Shapiro Wilk test and suggest you the test selected in the combo box. \n"
" Select the checkbox for each analysis function that you want to analyze statistically. \n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StatisticsTable", u"Configuration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StatisticsTable", u"Results", None))
    # retranslateUi


from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from scipy import stats
from functools import partial
import pandas as pd
from CustomWidget.Pandas_Table import PandasTable

class StatisticsTablePromoted(QWidget, Ui_StatisticsTable):
    def __init__(self, parent_stacked, analysis_stacked, hierachy_stacked_list, SeriesItems, database_handler, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.tabWidget.widget(1).hide()
        self.statistics_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.statistics_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.parent_stacked = parent_stacked
        self.analysis_stacked = analysis_stacked
        self.hierachy_stacked_list = hierachy_stacked_list
        self.SeriesItems = SeriesItems
        self.database_handler = database_handler
        
        self.autofill_statistics_table_widget()   

    
    def autofill_statistics_table_widget(self):

        series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")
        analysis_functions = self.database_handler.get_analysis_functions_for_specific_series(series_name[0])

        #initiate the table in case there are no rows yet
        existing_row_numbers = self.statistics_table_widget.rowCount()

        if  existing_row_numbers == 0:
            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
            self.statistics_table_widget.setColumnCount(5)
            self.statistics_table_widget.setRowCount(len(analysis_functions))
            self.statistics_table_buttons = [0] * len(analysis_functions)

        self.statistics_add_meta_data_buttons = [0]*len(analysis_functions)

        for i in analysis_functions:

            # prepare a row for each analysis
            analysis_function = i[0]
            print(analysis_function)
            row_to_insert = analysis_functions.index(i) + existing_row_numbers

            # add a checkbox in column 0
            self.select_checkbox = QCheckBox()
            self.statistics_table_widget.setCellWidget(row_to_insert, 0,self.select_checkbox)

            #add the analysis function to column 1
            self.statistics_table_widget.setItem(row_to_insert, 1,
                                                                    QTableWidgetItem(str(analysis_function)))

            # add meta data change button to column2
            self.statistics_add_meta_data_buttons[row_to_insert] =  QPushButton("Change")
            self.statistics_table_widget.setCellWidget(row_to_insert, 2, self.statistics_add_meta_data_buttons[row_to_insert])

            # get the meta data from the plot widget
            # @todo better get them from the database
            self.analysis_stacked.setCurrentIndex(self.parent_stacked)
            self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(1)
            result_plot_widget = self.hierachy_stacked_list[self.parent_stacked].currentWidget()
            self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(3)

            row = analysis_functions.index(i)
            qwidget_item = result_plot_widget.OfflineResultGrid.itemAtPosition(row, 0)
            qwidget_item_1 = result_plot_widget.OfflineResultGrid.itemAtPosition(1, 0)
            qwidget_item_2 = result_plot_widget.OfflineResultGrid.itemAtPosition(2, 0)

            custom_plot_widget = qwidget_item_1.widget()
            df = custom_plot_widget.statistics

            unique_meta_data = list(df["meta_data"].unique())

            if len(unique_meta_data) == len(df["meta_data"].values):
                dialog = QDialog()

                dialog.exec()

            else:
                
                #for meta_data in unique_meta_data:
                self.statistics_table_widget.setItem(row_to_insert,2, QTableWidgetItem('\n'.join(unique_meta_data)))
                                                
                #unique_meta_data.index(meta_data), 2,QTableWidgetItem(str(meta_data)))

                # show distrib�tion
                self.data_dist  = QComboBox()
                self.data_dist.addItems(["Normal Distribution", "Non-Normal Distribution"])
                # "Bernoulli Distribution", "Binomial Distribution", "Poisson Distribution"
                cell_widget = QWidget()
                cell_widget_layout = QGridLayout()
                cell_widget.setLayout(cell_widget_layout)
                cell_widget_layout.addWidget(self.data_dist,0,0)
                self.statistics_table_widget.setCellWidget(row_to_insert, 3, cell_widget)

                # show test
                self.stat_test = QComboBox()
                self.stat_test.addItems(["t-Test", "Wilcoxon Test", "GLM"])
                self.statistics_table_widget.setCellWidget(row_to_insert, 4, self.stat_test)

                shapiro_test = stats.shapiro(df["Result"])
                print(shapiro_test)
                cell_widget_layout.addWidget(QLabel("Shapiro Wilk Test \n p-Value = " + str(round(shapiro_test.pvalue,3))),1,0)
                if shapiro_test.pvalue >= 0.05:
                    # evidence that data comes from normal distribution
                    self.data_dist.setCurrentIndex(0)
                    self.stat_test.setCurrentIndex(0)
                else:
                    # no evidence that data comes from normal distribution
                    self.data_dist.setCurrentIndex(1)
                    self.stat_test.setCurrentIndex(1)

                #self.statistics_add_meta_data_buttons[row_to_insert].clicked.connect(partial(self.select_statistics_meta_data, statistics_table_widget, row_to_insert))
                
                self.statistics_table_widget.show()

        start_statistics = QPushButton("Run Statistic Test")
        self.verticalLayout_2.addWidget(start_statistics)

        start_statistics.clicked.connect(partial(self.calculate_statistics,df))

    def calculate_statistics(self,df):

        for row in range(self.statistics_table_widget.rowCount()):

            # get the test to be performed from the combo box (position 4)
            test_type = self.statistics_table_widget.cellWidget(row,4).currentText()

            #meta_data = statistics_table.cellWidget(row,2).currentText()


            if test_type == "t-Test":

                print("executing t test")

                # get unique meta data groups to compare
                unique_groups  = list(df["meta_data"].unique())

                # get a list of tuples for pairwise comparison
                pairs = self.get_pairs(unique_groups)

                # result data frame to be displayed
                res_df = pd.DataFrame(columns=["Group_1", "Group_2", "p_Value"])
                for p in pairs:
                    group1 = df[df["meta_data"]==p[0]]["Result"]
                    group2 = df[df["meta_data"]==p[1]]["Result"]
                    res =  stats.ttest_ind(group1,group2)
                    tmp = pd.DataFrame({"Group_1":[p[0]], "Group_2":[p[1]], "p_Value":[res.pvalue]})

                    res_df = pd.concat([res_df, tmp])

                print(res_df)
                self.show_statistic_results(res_df)

            else:
                print("not implemented yet")

    def show_statistic_results(self, statistics_df):
        # plot the df as table
        
        statistics_table_view = QTableView()
        model = PandasTable(statistics_df)
        statistics_table_view.setModel(model)
        self.statistics_result_grid.addWidget(statistics_table_view)
        statistics_table_view.show()
        self.tabWidget.widget(1).show()
        self.tabWidget.setCurrentIndex(1)
        # make the seaborn plot



    def get_pairs(self, item_list):
        # Initialize an empty list to store the pairs
        pairs = []
        # Iterate over the items in the list
        for i, item1 in enumerate(item_list):
            # Iterate over the remaining items in the list
            for item2 in item_list[i+1:]:
                # Add the pair to the list
                pairs.append((item1, item2))
        return pairs
