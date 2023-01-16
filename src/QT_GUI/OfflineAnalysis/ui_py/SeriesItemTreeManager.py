from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.ui_py.SideBarTreeParentItem import SideBarParentItem, SideBarConfiguratorItem, SideBarAnalysisItem
from QT_GUI.OfflineAnalysis.CustomWidget.specififc_analysis_tab import SpecificAnalysisTab
from functools import partial
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from plot_widget_manager import PlotWidgetManager
from treeview_manager import TreeViewManager
import copy
from Pandas_Table import PandasTable
from QT_GUI.OfflineAnalysis.CustomWidget.statistics_function_table import StatisticsTablePromoted
from scipy import stats
import pandas as pd

class SeriesItemTreeWidget():
    """Should create the TreeWidget that holds the Series Items"""
    def __init__(self, offlinetree):
        super().__init__()
        self.offline_tree = offlinetree
        self.SeriesItems = offlinetree.SeriesItems
        self.offline_widget = None
        self.database_handler = None
        self.tab_list = []
        self.parent_count = 0
        self.hierachy_stacked_list = []
        self.series_list = []
        self.analysis_stacked = QStackedWidget()
        self.tree_widget_index_count = 0
        self.show_sweeps_radio = None
        self.offline_manager = None
        self.navigation_list = []
        self.current_tab_visualization = []
        self.blank_analysis_tree_view_manager = None
        self.parent_stacked = None
        self.splitter = None

    def add_widget_to_splitter(self):
        self.splitter.addWidget(self.analysis_stacked)


    def built_analysis_specific_tree(self, series_names_list, analysis_function, offline_stacked_widget, selected_meta_data_list):
        """
        Function to built series name (e.g. IV, 5xRheo) specific tree. Each series get's a parent item for 3 childs:
        1) Plot - Result Visualization).
        2) Tables - Numerical Data shown in the result visualization)
        3) Statistics - Statistical Test Performed on the results
        @param series_names_list:
        @return:
        """
        # add selection to database

        self.database_handler.write_analysis_series_types_to_database(series_names_list)

        # make new tree parent elements and realted childs for ech specific series
        for index, s in enumerate(series_names_list):
            index += self.tree_widget_index_count

            # Custom designer widget: contains treeview, plot, analysis function table ...
            new_tab_widget = SpecificAnalysisTab()
            new_tab_widget.select_series_analysis_functions.clicked.connect(partial(analysis_function, s))
            new_tab_widget.setObjectName(s)

            self.tab_list.append(new_tab_widget)
            self.tab_changed(index, s,selected_meta_data_list)
            self.hierachy_stacked = QStackedWidget()
            self.hierachy_stacked.addWidget(QWidget())
            self.analysis_stacked.addWidget(self.hierachy_stacked)
            # fill the treetabwidgetitems
            parent = SideBarParentItem(self.SeriesItems)
            parent.setting_data(s, new_tab_widget, self.hierachy_stacked, index, False)
            # set the child items of the widget
            configurator = SideBarConfiguratorItem(parent, "Analysis Configurator")
            configurator.setting_data(new_tab_widget, self.hierachy_stacked, self.parent_count, index)
            self.series_list.append(s)
            # child stacked notebook per parent node
            self.hierachy_stacked_list.append(self.hierachy_stacked)
            self.plot_widgets = []
            self.parent_count += 1


        # connect the treewidgetsitems
        self.SeriesItems.itemClicked.connect(self.offline_analysis_result_tree_item_clicked)      
        #set the analysis notebook as index
        offline_stacked_widget.setCurrentIndex(3)
        self.SeriesItems.expandToDepth(2)
        self.tree_widget_index_count = index +1

    def simple_analysis_configuration_clicked(self,parent_stacked:int):
        """
        load its parent configuration widget and display it
        @param parent_stacked:
        @return:
        """
        stacked_widget = self.SeriesItems.currentItem().parent().data(4, Qt.UserRole)
        config_widget = self.SeriesItems.currentItem().parent().child(0).data(2, Qt.UserRole)

        # insert the windget
        stacked_widget.insertWidget(0, config_widget)
        stacked_widget.setCurrentIndex(0)

        self.analysis_stacked.setCurrentIndex(parent_stacked)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(0)

    def add_new_analysis_tree_children(self):
        """
        MZ: Refactored--> should no check if the children are already there
        add tree items to the analysis
            - plot for the result grpahics
            - table for the data from the result plots
            - statistics ..
            - advanced
        @param offline_tab:
        @return:
        """
        if self.SeriesItems.currentItem().data(5, Qt.UserRole) == 0: # thats the parent which is clicked
            parent_tree_item = self.SeriesItems.currentItem()
            parent_stacked_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            parent_stacked_widget = self.SeriesItems.currentItem().data(4, Qt.UserRole)

        else: # child is clicked
            parent_tree_item = self.SeriesItems.currentItem().parent()
            parent_stacked_index = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)
            parent_stacked_widget = self.SeriesItems.currentItem().parent().data(4, Qt.UserRole)

        if parent_tree_item.data(8, Qt.UserRole) is False:
            # add new children within the tree:
            for i in ["Plot", "Tables", "Statistics", "Advanced Analysis"]:
                new_child = SideBarAnalysisItem(i, parent_tree_item)
                parent_stacked_widget.addWidget(QWidget())
                if i in ["Plot", "Tables"]:
                    new_child.setting_data(self.hierachy_stacked)
                
            # overwrite the old stacked widget with the new extended stacked widget
            self.hierachy_stacked_list[parent_stacked_index] = parent_stacked_widget
            if self.SeriesItems.currentItem().data(5, Qt.UserRole) == 0:
                self.SeriesItems.currentItem().setData(8, Qt.UserRole, True)
            else:
                self.SeriesItems.currentItem().parent().setData(8, Qt.UserRole, True)


    def tab_changed(self, index, series_name, selected_meta_data_list):
        """Function tab changed will be called whenever a tab in the notebook of the selected series for analysis is
        changed. Index is the tab number correlating with a global list of tab objects self.tab_list
        @author dz, 20.07.2021, updated 02.12.2022"""

        current_tab = self.tab_list[index]
        series_name = series_name

        current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.database_handler, None, False)
        #self.navigation = NavigationToolbar(current_tab_plot_manager.canvas, None)
        #self.navigation_list.append(self.navigation)
        self.current_tab_visualization.append(current_tab_plot_manager)
        
        current_tab_tree_view_manager = TreeViewManager(self.database_handler, current_tab.widget)
        current_tab_tree_view_manager.show_sweeps_radio = self.show_sweeps_radio

        current_tab_tree_view_manager.selected_meta_data_list = selected_meta_data_list
        # make a deepcopy to be able to slize the copied item without changing its parent
        current_tab_tree_view_manager.selected_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.selected_tree_view_data_table)
        current_tab_tree_view_manager.discarded_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.discarded_tree_view_data_table)

        # slice out all series names that are not related to the specific chosen one
        current_tab_tree_view_manager.create_series_specific_tree(series_name,current_tab_plot_manager)

    """
    def offline_analysis_result_tree_item_clicked(self):
        \"""
        Whenever an item within the result tree view is clicked, this function is called
        @return:
        @author:DZ
        @todo restructure this and move it maybe into a new class with the related functions ?
        \"""
        print("this is the function to connect")
        if self.SeriesItems.currentItem().data(1, Qt.UserRole) is not None:
            #self.result_analysis_parent_clicked()
            self.SeriesItems.setCurrentItem(self.SeriesItems.currentItem().child(0))
            self.offline_analysis_result_tree_item_clicked()
        else:
            \"""identifiy the parent\"""
            if self.SeriesItems.currentItem().child(0):
                parent_stacked = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            else:
                parent_stacked = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)

            if self.SeriesItems.currentItem().text(0) == "Analysis Configurator":
                self.simple_analysis_configuration_clicked(parent_stacked)
                self.parent_stacked = parent_stacked

            if self.SeriesItems.currentItem().text(0) == "Plot":
                self.analysis_stacked.setCurrentIndex(parent_stacked)
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

            if self.SeriesItems.currentItem().text(0) == "Tables":
                self.view_table_clicked(parent_stacked)

            if self.SeriesItems.currentItem().text(0) == "Statistics":

                # uic the designer object
                # create in the py file an additional class named StatisticalTableWidget
                statistics_table_widget = StatisticsTablePromoted()

                self.hierachy_stacked_list[parent_stacked].insertWidget(3,statistics_table_widget)
                #statistics_table_widget.statistics_table_widget.setColumnCount(6)
                #statistics_table_widget.statistics_table_widget.setRowCount(2)
                #statistics_table_widget.statistics_table_widget.show()
                statistics_table_widget.statistics_table_widget.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                statistics_table_widget.statistics_table_widget.verticalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(3)

                series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")
                analysis_functions = self.database_handler.get_analysis_functions_for_specific_series(series_name[0])


                # -------------------
                existing_row_numbers = statistics_table_widget.statistics_table_widget.rowCount()


                if existing_row_numbers == 0:

                    # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
                    statistics_table_widget.statistics_table_widget.setColumnCount(6)
                    statistics_table_widget.statistics_table_widget.setRowCount(
                        len(analysis_functions))
                    self.statistics_table_buttons = [0] * len(analysis_functions)
                #else:
                #    current_tab.analysis_table_widget.analysis_table_widget.setRowCount(
                #        existing_row_numbers + len(self.selected_analysis_functions))
                #    self.table_buttons = self.table_buttons + [0] * len(self.selected_analysis_functions)

                self.statistics_add_meta_data_buttons = [0]*len(analysis_functions)

                for i in analysis_functions:
                    # prepare a row for each analysis
                    analysis_function = i[0]
                    print(analysis_function)
                    row_to_insert = analysis_functions.index(i) + existing_row_numbers

                    self.statistics_add_meta_data_buttons[row_to_insert] =  QPushButton("Choose")
                    self.select_checkbox = QCheckBox()
                    self.data_dist  = QComboBox()
                    self.data_dist.addItems(["Normal Distribution", "Bernoulli Distribution", "Binomial Distribution", "Poisson Distribution" ])
                    self.data_dist.setCurrentIndex(0)
                    self.stat_test = QComboBox()
                    self.stat_test.addItems(["t-Test", "Wilcoxon Test", "GLM"])
                    self.stat_test.setCurrentIndex(0)
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 0,self.select_checkbox)
                    statistics_table_widget.statistics_table_widget.setItem(row_to_insert, 1,
                                                                            QTableWidgetItem(str(analysis_function)))
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 2, self.statistics_add_meta_data_buttons[row_to_insert])

                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 3, self.data_dist)
                    statistics_table_widget.statistics_table_widget.setCellWidget(row_to_insert, 4, self.stat_test)

                    self.statistics_add_meta_data_buttons[row_to_insert].clicked.connect(partial(self.select_statistics_meta_data, statistics_table_widget, row_to_insert))

                    #current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_to_insert, 5,
                    #                                                                      self.live_result)

                    #self.statistics_table_buttons[row_to_insert].clicked.connect(
                    #    partial(self.open_statistics_meta_data_selection,row_to_insert))
                    #self.live_result.clicked.connect(
                    #    partial(self.show_live_results_changed, row_to_insert, current_tab, self.live_result))
                    statistics_table_widget.statistics_table_widget.show()

                
                start_statistics = QPushButton("Run Statistic Test")
                statistics_table_widget.verticalLayout_2.addWidget(start_statistics)

                start_statistics.clicked.connect(partial(self.calculate_statistics,statistics_table_widget.statistics_table_widget))

    """

    def view_table_clicked(self, parent_stacked:int):
        """
        specific function to display result tables that are stored within the related plot widget
        @param parent_stacked: position of the stacked widget
        @return:
        """
        self.analysis_stacked.setCurrentIndex(parent_stacked)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

        result_plot_widget = self.hierachy_stacked_list[parent_stacked].currentWidget()

        """create a table view within a tab widget: each tab will become one plot/one specific analysis """

        table_tab_widget = QTabWidget()
        table_tab_widget = QTabWidget()

        # works only    if results are organized row wise
        print("column count =", result_plot_widget.OfflineResultGrid.columnCount())
        if result_plot_widget.OfflineResultGrid.columnCount() == 1:
            print("row count =", result_plot_widget.OfflineResultGrid.rowCount())

            for r in range(1, result_plot_widget.OfflineResultGrid.rowCount()):

                qwidget_item = result_plot_widget.OfflineResultGrid.itemAtPosition(r, 0)
                custom_plot_widget = qwidget_item.widget()
                data = custom_plot_widget.export_data_frame
                # print(data)
                if data.empty:
                    print("Data to be displayed in the table are None. Fill the table first !")
                else:
                    print("creating the table")
                    self.model = PandasTable(data)
                    # Creating a QTableView
                    self.table_view = QTableView()
                    self.table_view.setModel(self.model)
                    print("setting the model")
                    horizontal_header = self.table_view.horizontalHeader()
                    horizontal_header.setSectionResizeMode(
                        QHeaderView.ResizeToContents
                    )
                    table_tab_widget.insertTab(1, self.table_view, custom_plot_widget.analysis_name)
        else:
            print("More than one column of analysis results is not implemented yet")

        self.hierachy_stacked_list[parent_stacked].insertWidget(2, table_tab_widget)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(2)


    def offline_analysis_result_tree_item_clicked(self):
        """
        Whenever an item within the result tree view is clicked, this function is called
        @return:
        @author:DZ
        @todo restructure this and move it maybe into a new class with the related functions ?
        """

        if self.SeriesItems.currentItem().data(1, Qt.UserRole) is not None:
            #self.result_analysis_parent_clicked()
            self.SeriesItems.setCurrentItem(self.SeriesItems.currentItem().child(0))
            self.offline_analysis_result_tree_item_clicked()
        else:
            """identifiy the parent"""
            if self.SeriesItems.currentItem().child(0):
                parent_stacked = self.SeriesItems.currentItem().data(7, Qt.UserRole)
            else:
                parent_stacked = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)

            if self.SeriesItems.currentItem().text(0) == "Analysis Configurator":
                self.simple_analysis_configuration_clicked(parent_stacked)
                self.parent_stacked = parent_stacked

            if self.SeriesItems.currentItem().text(0) == "Plot":
                self.analysis_stacked.setCurrentIndex(parent_stacked)
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)

            if self.SeriesItems.currentItem().text(0) == "Tables":
                self.view_table_clicked(parent_stacked)

            if self.SeriesItems.currentItem().text(0) == "Statistics":
                
                # get the qtdesigner created table widget
                statistics_table_widget = StatisticsTablePromoted()

                # add it to the statistic child in the tree
                self.hierachy_stacked_list[parent_stacked].insertWidget(3,statistics_table_widget)
                #statistics_table_widget.statistics_table_widget.setColumnCount(6)
                #statistics_table_widget.statistics_table_widget.setRowCount(2)
                #statistics_table_widget.statistics_table_widget.show()
                statistics_table_widget.statistics_table_widget.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                statistics_table_widget.statistics_table_widget.verticalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)

                # switch to the statistic tab
                self.hierachy_stacked_list[parent_stacked].setCurrentIndex(3)

                # fill the table widget according to created plots 
                self.autofill_statistics_table_widget(statistics_table_widget.statistics_table_widget,parent_stacked,statistics_table_widget)
            
            if  self.SeriesItems.currentItem().text(0) ==  "t-Test":
                print("t-test clicked")
    
    def autofill_statistics_table_widget(self,statistics_table_widget,parent_stacked,parentW):

        series_name = self.SeriesItems.currentItem().parent().text(0).split(" ")
        analysis_functions = self.database_handler.get_analysis_functions_for_specific_series(series_name[0])

        #initiate the table in case there are no rows yet
        existing_row_numbers = statistics_table_widget.rowCount()

        if  existing_row_numbers == 0:
            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
            statistics_table_widget.setColumnCount(5)
            statistics_table_widget.setRowCount(len(analysis_functions))
            self.statistics_table_buttons = [0] * len(analysis_functions)
        
        self.statistics_add_meta_data_buttons = [0]*len(analysis_functions)

        for i in analysis_functions:

            # prepare a row for each analysis
            analysis_function = i[0]
            print(analysis_function)
            row_to_insert = analysis_functions.index(i) + existing_row_numbers

            # add a checkbox in column 0
            self.select_checkbox = QCheckBox()
            statistics_table_widget.setCellWidget(row_to_insert, 0,self.select_checkbox)

            #add the analysis function to column 1
            statistics_table_widget.setItem(row_to_insert, 1,
                                                                    QTableWidgetItem(str(analysis_function)))

            # add meta data change button to column2
            self.statistics_add_meta_data_buttons[row_to_insert] =  QPushButton("Change")
            statistics_table_widget.setCellWidget(row_to_insert, 2, self.statistics_add_meta_data_buttons[row_to_insert])

            # get the meta data from the plot widget
            # @todo better get them from the database
            self.analysis_stacked.setCurrentIndex(parent_stacked)
            self.hierachy_stacked_list[parent_stacked].setCurrentIndex(1)
            result_plot_widget = self.hierachy_stacked_list[parent_stacked].currentWidget()
            self.hierachy_stacked_list[parent_stacked].setCurrentIndex(3)
            
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
                for meta_data in unique_meta_data:
                    statistics_table_widget.setItem(row_to_insert + unique_meta_data.index(meta_data), 2,
                                                                        QTableWidgetItem(str(meta_data)))
                        
                # show distrib�tion
                self.data_dist  = QComboBox()
                self.data_dist.addItems(["Normal Distribution", "Non-Normal Distribution"])
                # "Bernoulli Distribution", "Binomial Distribution", "Poisson Distribution"
                cell_widget = QWidget()
                cell_widget_layout = QGridLayout()
                cell_widget.setLayout(cell_widget_layout)
                cell_widget_layout.addWidget(self.data_dist,0,0)
                statistics_table_widget.setCellWidget(row_to_insert, 3, cell_widget)

                # show test
                self.stat_test = QComboBox()
                self.stat_test.addItems(["t-Test", "Wilcoxon Test", "GLM"])
                statistics_table_widget.setCellWidget(row_to_insert, 4, self.stat_test)

                shapiro_test = stats.shapiro(df["values"])
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

                statistics_table_widget.show()

        start_statistics = QPushButton("Run Statistic Test")
        parentW.verticalLayout_2.addWidget(start_statistics)

        start_statistics.clicked.connect(partial(self.calculate_statistics,statistics_table_widget,parent_stacked,df ))

    def calculate_statistics(self,statistics_table,parent_stacked,df):

        for row in range(0,statistics_table.rowCount()):

            # get the test to be performed from the combo box (position 4)
            test_type = statistics_table.cellWidget(row,4).currentText()

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
                    group1 = df[df["meta_data"]==p[0]]["values"]
                    group2 = df[df["meta_data"]==p[1]]["values"]
                    res =  stats.ttest_ind(group1,group2)
                    tmp = pd.DataFrame({"Group_1":[p[0]], "Group_2":[p[1]], "p_Value":[res.pvalue]})
                   
                    res_df = pd.concat([res_df, tmp])
                
                print(res_df)

            else:
                print("not implemented yet")

        # add to the new "t-test child" if it does not exist yet
        t_test_child = QTreeWidgetItem(self.SeriesItems.currentItem())
        t_test_child.setText(0, "t-Test")
        
    
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
            