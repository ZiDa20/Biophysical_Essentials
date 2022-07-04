from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import logging
import pandas as pd
from Pandas_Table import *
import pyqtgraph as pg

from online_analysis_designer_object import Ui_Online_Analysis
from online_analysis_manager import OnlineAnalysisManager
from treeview_manager import TreeViewManager
from plot_widget_manager import PlotWidgetManager
from dvg_pyqtgraph_threadsafe import PlotCurve

class Online_Analysis(QWidget, Ui_Online_Analysis):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.setupUi(self)

        self.online_manager = OnlineAnalysisManager()

        self.online_analysis.setCurrentIndex(0)
        self.button_select_data_file.clicked.connect(self.open_single_dat_file)
        self.online_analysis.currentChanged.connect(self.online_analysis_tab_changed)

        # add some empty widgets for a better appearance
        #self.tree_default_empty_widget = QGroupBox()
        #self.tree_layout_online.addWidget(self.tree_default_empty_widget)
        #self.tree_layout_online.setSpacing(0)

        # logger settings
        self.logger=logging.getLogger() # introduce the logger
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/online_analysis.log')
    

        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.debug('Online Analysis Widget Debugger')

        #self.pyqt_graph = pg.PlotWidget(height = 100) # insert a plot widget
        #self.pyqt_graph.setBackground("#232629")
        #self.gridLayout_12.addWidget(self.pyqt_graph)
        #self.online_analysis_tabs.setStyleSheet("background-color: #232629;")
        self.drawing()


    @Slot()
    def online_analysis_tab_changed(self):
        """handler if the tab is changed, tab 0: online analysis, tab 1: labbook"""
        if self.online_analysis.currentIndex()==0:
            self.tree_layouting_change.addWidget(self.tree_tab_widget)
        else:
            self.verticalLayout.addWidget(self.tree_tab_widget)

    def open_single_dat_file(self, file_name = None):
        """open a single .dat file and create a tree view from this, the first series of this treeview will
        also be plotted in an additionally created plot widget"""

        # open selection and retake users file selection
        print(file_name)
        if file_name is False:
            file_name = QFileDialog.getOpenFileName(self, 'OpenFile',"","*.dat")[0]

        #self.label_selected_directory.setText(file_name) can be added for the label but was removed nnow MZ

        # save the path in the manager class
        self.online_manager._dat_file_name = file_name

        # create treeview of this .dat file
        bundle = TreeViewManager().open_bundle_of_file(file_name)

        # make sure to write into an empty tree (otherwise it will only be appended)
        self.treeWidget.clear()
        self.treeWidget_2.clear()

        # for a better appearance an initial default widget will be shown to the user
        # this default widget needs to be removed first
        try:
            self.tree_layouting_change.removeWidget(self.tree_default_empty_widget)
            self.tree_default_empty_widget.deleteLater()
        except:
            print("no default widget found")

        # create two treeviews and write into self.treewidget and self.treewidget_2
        TreeViewManager().create_treeview_from_single_dat_file([], bundle, "", [],self.treeWidget, self.treeWidget_2,"SingleExperiment",[],0,None)
        self.get_columns_data_to_table()
        self.tree_layouting_change.addWidget(self.tree_tab_widget)
        self.tree_tab_widget.setMaximumSize(QSize(330, 700))
       

        #self.verticalLayout_5.addWidget(self.tree_tab_widget)


        # initially show online analysis
        self.tree_tab_widget.setCurrentIndex(0)
        #self.tree_tab_widget.setStyleSheet("background-color: #232629;")

        # initially show all series of an experiment
        self.treeWidget.expandToDepth(0)

        # print first series into a plot widget
        self.online_analysis_plot_manager = PlotWidgetManager(self.tree_plot_widget_layout, self.online_manager,
                                                             self.treeWidget, 0)

        self.treeWidget.itemClicked.connect(self.online_analysis_plot_manager.tree_view_click_handler)
        self.treeWidget_2.itemClicked.connect(self.online_analysis_plot_manager.tree_view_click_handler)


        self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
        self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0).child(0).setCheckState(1,Qt.Checked))

        self.online_analysis_plot_manager.tree_view_click_handler(self.treeWidget.topLevelItem(0).child(0))

        self.get_columns_data_to_table()


        
    def get_columns_data_to_table(self):
        #toDO add the documentation here
        count = self.treeWidget.topLevelItemCount()
        list_rows = []
        final_pandas = pd.DataFrame()
        for i in range(count):
            top_item = self.treeWidget.topLevelItem(i)  # toplevel item
            child_amount = top_item.childCount()
            trial = top_item.child(i).child(0).data(5,0)
            print(trial)

            for t in range(child_amount):
                list_rows.append(top_item.child(t).text(0))
                grand_child = top_item.child(t).child(0)
                data = grand_child.data(5,0)
                df = pd.DataFrame(data, index = [0])
                final_pandas = final_pandas.append(df)


        final_pandas.index = pd.Series(list_rows)
        print(final_pandas.columns)
        final_pandas = final_pandas[["Label","RsValue","CSlow"]]
        final_pandas["comments"] = final_pandas.shape[0] * [""]
        
        self.draw_table(final_pandas)

    def draw_table(self, data):
        """ draws the table of the .dat metadata as indicated by the .pul Bundle file """
        try:
            self.table_model = PandasTable(data)
            print(self.table_model)
            #self.tableWidget.setStyleSheet("background-color:#232629; ")
            self.tableWidget.setModel(self.table_model)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            print(e)


    def draw_live_plot(self,data_x = None):
        """ this is necessary to draw the plot which is plotted to the self.configuration window
        this will further projected to the online-anaysis """
        print(data_x)
        #print(data_x[0], print(data_x[1]))
        #self.drawing()
        self.pyqt_graph.plot(data_x[0], data_x[1])
        #self.pyqt_graph.setData(data_x[0], data_x[1])
        print("try to give an updated view of the data")
        
        print("no error occured here but also not drawn")
        

    def drawing(self):
        """ redraws the graph into online analysis """
        self.pyqt_graph = pg.PlotWidget(height = 100) # insert a plot widget
        self.pyqt_graph.setBackground("#232629")
        self.verticalLayout_6.addWidget(self.pyqt_graph)
        print("initialized")
       


