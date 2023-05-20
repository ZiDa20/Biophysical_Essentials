from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from scipy import stats
from functools import partial
import pandas as pd
from CustomWidget.Pandas_Table import PandasTable
from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import Ui_StatisticsTable
from Offline_Analysis.error_dialog_class import CustomErrorDialog

import itertools

class StatisticsTablePromoted(QWidget, Ui_StatisticsTable):
    def __init__(self, parent_stacked, analysis_stacked, hierachy_stacked_list, SeriesItems, database_handler, frontend_style, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.tabWidget.widget(1).hide()
        self.statistics_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.statistics_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.frontend_style = frontend_style
        self.parent_stacked = parent_stacked
        self.analysis_stacked = analysis_stacked
        self.hierachy_stacked_list = hierachy_stacked_list
        self.SeriesItems = SeriesItems
        self.database_handler = database_handler
        self.check_meta_data_selected()
        self.autofill_statistics_table_widget()   

    
    def check_meta_data_selected(self):
        """
        statistics  can be only applied between meta data groups and therefore the user must select meta data groups before.
        other wise each cell is displayed solely and statistics wont work
        """

        # get the meta data from the plot widget
        # @todo better get them from the database
        self.analysis_stacked.setCurrentIndex(self.parent_stacked)
        self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(1)
        result_plot_widget = self.hierachy_stacked_list[self.parent_stacked].currentWidget()
        self.hierachy_stacked_list[self.parent_stacked].setCurrentIndex(3)

        # get the table widget that holds the dataframe -- can this be removed then ?? 
        qwidget_item_1 = result_plot_widget.OfflineResultGrid.itemAtPosition(1, 0)
        custom_plot_widget = qwidget_item_1.widget()
        df = custom_plot_widget.statistics

        # Compare the two columns for equality
        are_equal = df["experiment_name"] == df["meta_data"]

        if are_equal.all():
            d = CustomErrorDialog("You have not set any meta data. Go back to the plots, select your meta data and come back to statistics", self.frontend_style)
            d.exec_()
        else:
            return


    def autofill_statistics_table_widget(self):
        """
        based on the analysis function data are scanned and prepared for the statistical analysis
        """
        
        
        self.series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")[0]
        analysis_functions = self.database_handler.get_analysis_functions_for_specific_series(self.series_name)

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

            # get the table widget that holds the dataframe -- can this be removed then ?? 
            qwidget_item_1 = result_plot_widget.OfflineResultGrid.itemAtPosition(1, 0)
            custom_plot_widget = qwidget_item_1.widget()
            df = custom_plot_widget.statistics

            unique_meta_data = list(df["meta_data"].unique())



            # @todo whats this if needed for ??? dz 17.05.2023
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
                self.stat_test.addItems(["Independent t-test","Welchs t-test", "Paired t-test", "Wilcoxon Signed-Rank test", "Kruskal Wallis test", "Brunner-Munzel test"])
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
                    self.stat_test.setCurrentIndex(3)

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

            # get unique meta data groups to compare
            unique_groups  = list(df["meta_data"].unique())

            # get a list of tuples for pairwise comparison
            pairs = self.get_pairs(unique_groups)
            
            # test if the table has column "voltage" - this means voltage steps and requieres to make pairs per voltage step (e.g. KO_80mV vs CTRL_80mV)
            # test if the table has column "????"

            if "Voltage" in df.columns:
                voltage_steps = list(df["Voltage"].unique())

                # result data frame to be displayed
                res_df = pd.DataFrame(columns=["Voltage", "Group_1", "Group_2", "p_Value"])
                for v in voltage_steps:
                
                    for p in pairs:
                        group1 = df[(df["meta_data"]==p[0]) & (df["Voltage"]==v)]["Result"]
                        group2 = df[(df["meta_data"]==p[1]) & (df["Voltage"]==v)]["Result"]

                        if len(group2)>=len(group1):
                            group2 = group2[0:len(group1)]
                        else:
                            group1 = group1[0:len(group2)]

                        if test_type == "t-Test":
                            res =  stats.ttest_ind(group1,group2)
                        else:
                            res = stats.wilcoxon(group1,group2)
                        tmp = pd.DataFrame({"Voltage":v, "Group_1":[p[0]], "Group_2":[p[1]], "p_Value":[res.pvalue]})

                        res_df = pd.concat([res_df, tmp])

                        # print each voltage step seperately
                    
                statistics_table_view = QTableView()
                model = PandasTable(res_df)
                statistics_table_view.setModel(model)
                self.statistics_result_grid.addWidget(statistics_table_view)
                statistics_table_view.show()

                self.tabWidget.widget(1).show()
                self.tabWidget.setCurrentIndex(1)

            elif "Step" in df.columns:
                print("not implemented yet")

            else: # simple boxplots for each meta data group to be compared
                
                res_df = pd.DataFrame(columns=["Group_1", "Group_2", "p_Value"]) # result data frame to be displayed
                for p in pairs:
                    group1 = df[df["meta_data"]==p[0]]["Result"]
                    group2 = df[df["meta_data"]==p[1]]["Result"]
                    if test_type == "t-Test":
                        res =  stats.ttest_ind(group1,group2)
                    else:
                        print("not implemented yet")
                    tmp = pd.DataFrame({"Group_1":[p[0]], "Group_2":[p[1]], "p_Value":[res.pvalue]})
                    res_df = pd.concat([res_df, tmp])

                self.show_statistic_results(df, res_df, pairs)
                self.tabWidget.widget(1).show()
                self.tabWidget.setCurrentIndex(1)

    def show_statistic_results(self, df, statistics_df, pairs):
        # plot the df as table
        import seaborn as sns
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_qtagg import FigureCanvas
        from matplotlib.figure import Figure
        from statannotations.Annotator import Annotator

        statistics_table_view = QTableView()
        model = PandasTable(statistics_df)
        statistics_table_view.setModel(model)
        self.statistics_result_grid.addWidget(statistics_table_view)
        statistics_table_view.show()

        
        # Create a FigureCanvasQTAgg from the Figure object returned by Seaborn
        
        fig = plt.Figure()
        ax = fig.add_subplot(111)
        sns.boxplot(data=df,x ="meta_data" ,y = "Result", ax=ax)
        annotator = Annotator(ax, pairs, data=df, x ="meta_data" ,y = "Result")
        # t-test_ind, t-test_welch, t-test_paired, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, Levene, Wilcoxon, Kruskal, Brunner-Munzel.
        annotator.configure(test='t-test_ind', text_format='star', loc='inside') #Mann-Whitney
        annotator.apply_and_annotate()
        canvas = FigureCanvas(fig)
        self.statistics_result_grid.addWidget(canvas)
        canvas.draw_idle()
        
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
