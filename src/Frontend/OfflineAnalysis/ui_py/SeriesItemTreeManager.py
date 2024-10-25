from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from Frontend.OfflineAnalysis.ui_py.SideBarTreeParentItem import SideBarParentItem, SideBarConfiguratorItem, SideBarAnalysisItem
from Frontend.OfflineAnalysis.CustomWidget.specififc_analysis_tab import SpecificAnalysisTab
from functools import partial
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from Backend.PlotHandler.plot_widget_manager import PlotWidgetManager
from Backend.ExperimentTree.treeview_manager import TreeViewManager
import copy
from Frontend.CustomWidget.Pandas_Table import PandasTable
from Frontend.OfflineAnalysis.CustomWidget.statistics_function_table_handler import StatisticsTablePromoted
from Frontend.OfflineAnalysis.CustomWidget.normalization_dialog_handler import Normalization_Dialog
from  Frontend.OfflineAnalysis.CustomWidget.construction_side_handler import ConstrcutionSideDialog   
from StyleFrontend.animated_ap import LoadingAnimation
import pandas as pd
from PySide6.QtTest import QTest
import picologging
from Frontend.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog
from Backend.tokenmanager import OfflineAnalysisTreeTokens


class SeriesItemTreeWidget():
    """Should create the TreeWidget that holds the Series Items"""
    def __init__(self,
                 offlinetree,
                 plot_buttons,
                 frontend_style,
                 database_handler,
                 offline_manager,
                 show_sweeps_radio,
                 blank_analysis_tree,
                 ribbon_bar):

        super().__init__()
        self.logger= picologging.getLogger(__name__)
        self.offline_tree = offlinetree
        self.SeriesItems = offlinetree.SeriesItems
        self.SeriesItems.setHeaderLabel("Series Selector:")
        self.frontend_style = frontend_style
        self.offline_widget = None
        self.database_handler = database_handler
        self.tab_list = []
        self.parent_count = 0
        self.hierachy_stacked_list = []
        self.series_list = []
        self.analysis_stacked = QStackedWidget()
        self.trial_stacked = QStackedWidget()
        self.tree_widget_index_count = 0
        self.show_sweeps_radio = show_sweeps_radio
        self.navigation_list = []
        self.current_tab_tree_view_manager_dict= {}
        self.current_tab_visualization_dict = {}

        self.blank_analysis_tree_view_manager = blank_analysis_tree
        
        self.parent_stacked = None
        self.home = plot_buttons[0]
        self.zoom = plot_buttons[1]
        self.pan = plot_buttons[2]
        self.single_series_item = None
        self.multi_series_item = None
        self.ribbon_bar = ribbon_bar
        
    def create_top_level_items(self):
        """_summary_: This creates the two top level items for the tree widget
        """
        
        self.single_series_item = SideBarParentItem(self.SeriesItems)
        self.single_series_item.set_text("Single Series Analysis:")
        self.SeriesItems.addTopLevelItem(self.single_series_item)

        # creates a top level item that is used for the multi series analysis
        self.multi_series_item = SideBarParentItem(self.SeriesItems)
        self.multi_series_item.set_text("Multi-Series Analysis:")
        self.SeriesItems.addTopLevelItem(self.multi_series_item)

    def add_widget_to_splitter(self, layout):
        layout.addWidget(self.analysis_stacked)

    def add_analysis_tree_selection(self, index):
        # retrieve the current tab
        if index == 0:
            current_tab = self.tab_list[self.SeriesItems.currentItem().data(7, Qt.UserRole)]
            current_tab.subwindow_calc.show()

    def built_analysis_specific_tree(self, series_names_list, analysis_function, offline_stacked_widget, reload = False):
        """
        Function to built series name (e.g. IV, 5xRheo) specific tree. Each series get's a parent item for 3 childs:
        1) Plot - Result Visualization).
        2) Tables - Numerical Data shown in the result visualization)
        3) Statistics - Statistical Test Performed on the results
        @param series_names_list:
        @return:
        """
        if not reload:
            self.ap = LoadingAnimation("Preparing your data: Please Wait", self.frontend_style)
            self.ap.make_widget()
            self.database_handler.write_analysis_series_types_to_database(series_names_list)

        # make new tree parent elements and realted childs for ech specific series
        
        # get the select analysis function button from the ribbon bar and only connect if once
        b = self.find_widget_by_name(self.ribbon_bar,"select_analysis_fct")
        b.clicked.connect(partial(analysis_function))

        for index, s in enumerate(series_names_list):

            QApplication.processEvents()
            
            index += self.tree_widget_index_count
            # Custom designer widget: contains treeview, plot, analysis function table ...
            new_tab_widget = SpecificAnalysisTab(self.frontend_style)
            new_tab_widget.analysis_functions.groupBox.hide()

            # set the small bpe logo to the upper left corner
            custom_icon = QIcon(r':Frontend/Button/light_mode/offline_analysis/bpe_logo_small.png')
            new_tab_widget.subwindow.setWindowIcon(custom_icon)
            new_tab_widget.PlotWindow.setWindowIcon(custom_icon)
      
            print(s)
            new_tab_widget.series_name = s

            #new_tab_widget.analysis_functions.select_series_analysis_functions.clicked.connect(partial(analysis_function, s))
            
            # show normalization options only in voltage clamp mode to avoid further checks user confusion
            recording_mode = self.database_handler.query_recording_mode(s)
            if recording_mode == "Voltage Clamp":
                new_tab_widget.analysis_functions.normalization_combo_box.currentTextChanged.connect(self.normalization_value_handler)
            else:
                #new_tab_widget.analysis_functions.normalization_group_box.hide()
                new_tab_widget.analysis_functions.normalization_combo_box.hide()

            new_tab_widget.setObjectName(s)
            self.tab_list.append(new_tab_widget)
            self.tab_changed(index, s)

            QApplication.processEvents()

            self.hierachy_stacked = QStackedWidget()
            self.hierachy_stacked.addWidget(QWidget())
            self.analysis_stacked.addWidget(self.hierachy_stacked) # analysis stacked is the original stacked widget
            # fill the treetabwidgetitems
            parent = SideBarParentItem(self.SeriesItems, parent_widget = self.single_series_item)
            parent.setting_data(s, new_tab_widget, self.hierachy_stacked, index, False)
            # set the child items of the widget
            configurator = SideBarConfiguratorItem(parent, "Analysis Configurator")
            configurator.setting_data(new_tab_widget, self.hierachy_stacked, self.parent_count, index)
            
            QApplication.processEvents()
        
            self.series_list.append(s)
            # child stacked notebook per parent node
            self.hierachy_stacked_list.append(self.hierachy_stacked)
            self.plot_widgets = []
            self.parent_count += 1

            QApplication.processEvents()
        
        # connect the treewidgetsitems
        self.SeriesItems.itemClicked.connect(self.offline_analysis_result_tree_item_clicked)
        #set the analysis notebook as index
        offline_stacked_widget.setCurrentIndex(3)
        self.SeriesItems.expandToDepth(2)
        self.tree_widget_index_count = self.tree_widget_index_count + len(series_names_list)

        QApplication.processEvents()
        
        if not reload:
            self.ap.stop_and_close_animation()


    def normalization_value_handler(self):
        """show the normalization values to the user and allow to edit the values
            values will be stored in the current tab and written to db when all other grid values of the current tab
            are written to the db
        """
        # get the experiment name and series identifier from the treeview model
        current_tab = self.tab_list[self.SeriesItems.currentItem().data(7, Qt.UserRole)]
        treeview_manager = self.current_tab_tree_view_manager_dict[str(self.SeriesItems.currentItem().data(7, Qt.UserRole))]
        model_df = treeview_manager.selected_tree_view_data_table
        normalization_dialog = Normalization_Dialog(current_tab, self.database_handler, model_df)
        self.frontend_style.set_pop_up_dialog_style_sheet(normalization_dialog)
        print("showing now")
        normalization_dialog.exec()


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

        self.click_top_level_tree_item()

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
        try:    
            if self.SeriesItems.currentItem().data(5, Qt.UserRole) == 0: # thats the parent which is clicked
                parent_tree_item = self.SeriesItems.currentItem()
                parent_stacked_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
                parent_stacked_widget = self.SeriesItems.currentItem().data(4, Qt.UserRole)

            else: # child is clicked
                parent_tree_item = self.SeriesItems.currentItem().parent()
                parent_stacked_index = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)
                parent_stacked_widget = self.SeriesItems.currentItem().parent().data(4, Qt.UserRole)

            print(parent_tree_item.data(8, Qt.UserRole))
            if parent_tree_item.data(8, Qt.UserRole) is False:
                # add new children within the tree:
                for i in ["Plot", "Tables", "Statistics",]: # "Advanced Analysis"]:
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
        except Exception as e:
            print("catched another error: 2")
            print(e)

    def tab_changed(self, index, series_name):
        """Function tab changed will be called whenever a tab in the notebook of the selected series for analysis is
        changed. Index is the tab number correlating with a global list of tab objects self.tab_list
        @author dz, 20.07.2021, updated 02.12.2022"""

        current_tab = self.tab_list[index]

        # if there was no tab visualization object created for this tab create a new one,
        # else reuse the existing one
        if str(index) not in self.current_tab_visualization_dict.keys():
            current_tab_plot_manager = PlotWidgetManager(current_tab.series_plot, self.database_handler, None, False, self.frontend_style)
            self.current_tab_visualization_dict[str(index)] = current_tab_plot_manager
        else:
            current_tab_plot_manager = self.current_tab_visualization_dict[str(index)]
        
        # if there was no tree view manager object created for this tab create a new one,
        # else reuse the existing one
        if str(index) not in self.current_tab_tree_view_manager_dict.keys():

            current_tab_tree_view_manager = TreeViewManager(self.database_handler,
                                                        current_tab.treebuild,
                                                        self.show_sweeps_radio,
                                                        current_tab,
                                                        frontend = self.frontend_style)
            
            self.current_tab_tree_view_manager_dict[str(index)] = current_tab_tree_view_manager
            self.logger.info("added current_tab_tree_view_manager")
            self.logger.info(self.current_tab_tree_view_manager_dict)
        else:
            self.logger.info("reused existing tab_tree_view_manager")
            current_tab_tree_view_manager = self.current_tab_tree_view_manager_dict[str(index)]

        current_tab.frontend_style = self.frontend_style

        
        # make a deepcopy to be able to slize the copied item without changing its parent
        current_tab_tree_view_manager.selected_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.selected_tree_view_data_table)
        
        current_tab_tree_view_manager.discarded_tree_view_data_table = copy.deepcopy(
            self.blank_analysis_tree_view_manager.discarded_tree_view_data_table)

        # slice out all series names that are not related to the specific chosen one
        # at the moment its setting back every plot! @2toDO:MZ
        
        #current_tab_tree_view_manager.create_series_specific_tree(series_name,current_tab_plot_manager)
        current_tab_tree_view_manager.update_treeviews(current_tab_plot_manager,series_name)

        navigation = NavigationToolbar(current_tab_plot_manager.canvas, None)
        self.home.clicked.connect(navigation.home)
        self.zoom.clicked.connect(navigation.zoom)
        self.pan.clicked.connect(navigation.pan)



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
        # works only    if results are organized row wise
        print("column count =", result_plot_widget.OfflineResultGrid.columnCount())

        if result_plot_widget.OfflineResultGrid.columnCount() == 1:
            print("row count =", result_plot_widget.OfflineResultGrid.rowCount())

        for r in range(1, result_plot_widget.OfflineResultGrid.rowCount()):
            for t in range(0, result_plot_widget.OfflineResultGrid.columnCount()):
                qwidget_item = result_plot_widget.OfflineResultGrid.itemAtPosition(r, t)

                try:
                    custom_plot_widget = qwidget_item.widget()
                except AttributeError as e:
                    print("no Widget found here")
                    continue
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
                    #self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
                    self.model.resize_header(self.table_view)
                    print("setting the model")

                    table_tab_widget.insertTab(1, self.table_view, custom_plot_widget.analysis_name)

        self.hierachy_stacked_list[parent_stacked].insertWidget(2, table_tab_widget)
        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(2)

    def offline_analysis_result_tree_item_clicked(self):
        """
        Whenever an item within the result tree view is clicked, this function is called
        @return:
        @author:DZ
        @todo restructure this and move it maybe into a new class with the related functions ?
        """
        try:
            if self.SeriesItems.currentItem().text(0) == OfflineAnalysisTreeTokens.MULTI_SERIES_TOKEN.value:
                ConstrcutionSideDialog(self.frontend_style)
            elif self.SeriesItems.currentItem().data(1, Qt.UserRole) is not None:
                #self.result_analysis_parent_clicked()
                #  the "parent" (series name) was clicked but we actually need the children Analysis Configurator, Plot, Table or Statistics
                self.SeriesItems.setCurrentItem(self.SeriesItems.currentItem().child(0))
                self.offline_analysis_result_tree_item_clicked()
            else:
                """identifiy the parent"""

                if self.SeriesItems.currentItem().child(0):
                    parent_stacked = self.SeriesItems.currentItem().data(7, Qt.UserRole)
                else:
                    parent_stacked = self.SeriesItems.currentItem().parent().data(7, Qt.UserRole)
                
                child_text = self.SeriesItems.currentItem().text(0) 
                if  child_text == OfflineAnalysisTreeTokens.CONFIGURATOR_TOKEN.value:
                    self.simple_analysis_configuration_clicked(parent_stacked)
                    self.parent_stacked = parent_stacked
                    self.set_ribbon_bar_page(1)

                if child_text == OfflineAnalysisTreeTokens.PLOT_TOKEN.value:
                    self.analysis_stacked.setCurrentIndex(parent_stacked)
                    self.hierachy_stacked_list[parent_stacked].setCurrentIndex(OfflineAnalysisTreeTokens.PLOT_INDEX.value)
                    self.set_ribbon_bar_page(2)

                if child_text == OfflineAnalysisTreeTokens.TABLES_TOKEN.value:
                    self.view_table_clicked(parent_stacked)
                    self.set_ribbon_bar_page(2)

                if child_text == OfflineAnalysisTreeTokens.STATISTICS_TOKEN.value:
                    # get the qtdesigner created table widget
                    statistics_table_widget = StatisticsTablePromoted(parent_stacked, self.analysis_stacked, self.hierachy_stacked_list,self.SeriesItems, self.database_handler,self.frontend_style)
                    # add it to the statistic child in the tree
                    if statistics_table_widget.meta_data_selected:
                        self.hierachy_stacked_list[parent_stacked].insertWidget(3,statistics_table_widget)
                        self.hierachy_stacked_list[parent_stacked].setCurrentIndex(OfflineAnalysisTreeTokens.STATISTICS_INDEX.value)
                        self.set_ribbon_bar_page(2)
                    else:
                        "@todo: open the meta data dialog in"
                        print("open dialog")
                    

        except Exception as e:
            print("catched an error 1")
            print(e)

    def set_ribbon_bar_page(self,page_index):
        self.find_widget_by_name(self.ribbon_bar,"ribbon_series_normalization").setCurrentIndex(page_index)
        self.find_widget_by_name(self.ribbon_bar,"ribbon_analysis").setCurrentIndex(page_index)
        if page_index > 1:
            self.find_widget_by_name(self.ribbon_bar,"ribbon_plot_options").setCurrentIndex(1)
        else:
            self.find_widget_by_name(self.ribbon_bar,"ribbon_plot_options").setCurrentIndex(0)
    
    
    def find_widget_by_name(self, parent:object, name:str):
        """The ribbon bar is given as qframe and requires identification and extraction of the corect item by its name
        Recursion is applied to get the childrens childs

        Args:
            parent (_type_): initially its the self.ribbon_bar 
            name (_type_): name of the object as str

        Returns:
            _type_: QStackedWidget, QPushButton ... anything like this
        """
        if parent.objectName() == name:
            return parent

        for child in parent.findChildren(QWidget):
            if child.objectName() == name:
                return child

        for child in parent.findChildren(QWidget):
            found_widget = self.find_widget_by_name(child, name)
            if found_widget:
                return found_widget

        return None
    
    def click_top_level_item(self):
        """Clicks the first top level item in the tree widget.
        """
        first_item = self.SeriesItems.topLevelItem(0).child(0)
        self.SeriesItems.setCurrentItem(first_item)
        self.SeriesItems.itemClicked.emit(first_item, 0)

        current_tab = self.tab_list[self.SeriesItems.currentItem().data(7, Qt.UserRole)]
        index =  current_tab.treebuild.selected_tree_view.model().index(0, 0, current_tab.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
        current_tab.treebuild.selected_tree_view.setCurrentIndex(index)
        # Get the rect of the index
        rect = current_tab.treebuild.selected_tree_view.visualRect(index)
        QTest.mouseClick(current_tab.treebuild.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())


    def click_top_level_tree_item(self, experiment = False):
        """Should click the toplevel item of the model_view
        """
        pos = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        print(pos)
        current_tab = self.tab_list[pos]
        model = current_tab.treebuild.selected_tree_view.model()


        if experiment: # this is applied whenever we supply a name of the exact experiment
            index = self.findName(model, experiment)
        else:
            model_df = current_tab.treebuild.selected_tree_view.model()._data 
            if "Label" in model_df["type"].unique():
                parent_index =  current_tab.treebuild.selected_tree_view.model().index(0, 0, current_tab.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
                index = current_tab.treebuild.selected_tree_view.model().index(0,2,parent_index)
            else:
                index =  current_tab.treebuild.selected_tree_view.model().index(0, 0, current_tab.treebuild.selected_tree_view.model().index(0,0, QModelIndex()))
 
        # Get the rect of the index
        # current_tab.treebuild.selected_tree_view.setCurrentIndex(index)
        rect = current_tab.treebuild.selected_tree_view.visualRect(index)
        QTest.mouseClick(current_tab.treebuild.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())
      
        col_count = len(self.current_tab_tree_view_manager_dict[str(pos)].selected_tree_view_data_table["type"].unique())
        self.current_tab_tree_view_manager_dict[str(pos)].update_mdi_areas(col_count)


    def findName(self,model, name, parent=QModelIndex()):
        """_summary_: this function should identify the index of a selected name
        in the tree using a recursive approach combined by looping through each element in the tree

        Args:
            model (QTreeViw): QTreeView model
            name (str): Name of the searched string
            parent (QModelIndex, optional): _description_. Defaults to QModelIndex().

        Returns:
            QModelIndex: Location of the searched string
        """
        for row in range(model.rowCount(parent)):
            for column in range(model.columnCount(parent)):
                index = model.index(row, column, parent)
                print(model.data(index, Qt.DisplayRole))
                if model.data(index, Qt.DisplayRole) == name:
                    return index
                result = self.findName(model, name, index)
                if result.isValid():
                    return result
        return QModelIndex()