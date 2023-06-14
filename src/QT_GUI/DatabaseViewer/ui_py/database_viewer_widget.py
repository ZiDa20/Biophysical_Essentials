from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.DatabaseViewer.ui_py.data_base_designer_object import Ui_Database_Viewer
import pandas as pd
from CustomWidget.Pandas_Table import PandasTable
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from QT_GUI.DatabaseViewer.ui_py.ui_execute_query import ExecuteDialog
from functools import partial
from QT_GUI.OfflineAnalysis.CustomWidget.ExportOfflineDialog import ExportOfflineDialog
import duckdb


class Database_Viewer(QWidget, Ui_Database_Viewer):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.data_base_stacked_widget.setCurrentIndex(0)
        self.data_base_stacked_widget.setCurrentIndex(0)
        #self.connect_to_database.clicked.connect(self.show_basic_tables)
        self.execute_dialog = ExecuteDialog()
        self.execute_dialog.pushButton.clicked.connect(partial(self.query_data,True))
        self.execute_dialog.pushButton_2.clicked.connect(self.execute_dialog.close)
        self.complex_query.clicked.connect(self.execute_dialog.show)
        self.database_handler = None
        self.query_execute.clicked.connect(self.query_data)
        self.data_base_content = None
        self.plot = None
        self.canvas = None
        self.export_table.clicked.connect(self.export_table_to_csv)
        self.select_columns.clicked.connect(self.export_offline_analysis_id)
        self.database_table.itemClicked.connect(self.pull_table_from_database)
        self.frontend_style = None
        self.SearchTable.clicked.connect(self.search_database_table)
        self.select_table.currentTextChanged.connect(self.retrieve_tables)

    def update_database_handler(self,database_handler, frontend_style):
        self.database_handler = database_handler
        self.frontend_style = frontend_style
        suggestions = [i[0] for i in self.database_handler.database.execute("SHOW TABLES").fetchall()]
        completer = QCompleter(suggestions)
        self.lineEdit.setCompleter(completer)

    def export_table_to_csv(self):
        """
        Table will be exported as csv file
        """
        if self.data_base_content is not None:
            response = QFileDialog.getSaveFileName(self, "Save File", "", "CSV(*.csv)")
            self.pandas_frame.to_csv(response[0])
        else:
            print("No Table to export")

    def show_basic_tables(self,database_handler):
        '''
        Request available tables and plot the content
        :return:
        '''
        #database_handler.database.close()
        #self.database = database_handler.database

        q = """SHOW TABLES"""
        try: 
            tables_names = [i[0] for i in self.database_handler.database.execute(q).fetchall()]
        except duckdb.ConnectionException:
            print("open database since it is closed")
            self.database_handler.open_connection()
            tables_names = [i[0] for i in self.database_handler.database.execute(q).fetchall()]

        self.table_dictionary = {"Result Table": [],
                                 "Raw signal" : [],
                                 "Generator Table":[],
                                 "Meta Table": [],
                                 "Selected Meta":[],
                                 "Experiment": [],
                                 "Analysis Table":[],
                                 "Labbook Table": [],
                                 "Solutions": [],
                                 "Other Tables": []}

        # for each table, create a button in a dropdown list
        # connect the button to a function plotting the table
        for table_name in tables_names:
            if "imon_signal" in table_name:
                self.table_dictionary["Raw signal"].append(table_name)
            elif "imon_meta" in table_name:
                self.table_dictionary["Meta Table"].append(table_name)
            elif "meta_data" in table_name:
                self.table_dictionary["Selected Meta"].append(table_name)
            elif ("experiment" in table_name) or ("global" in table_name):
                self.table_dictionary["Experiment"].append(table_name)
            elif "analysis" in table_name and "result" not in table_name:
                self.table_dictionary["Analysis Table"].append(table_name)
            elif "pgf" in table_name:
                self.table_dictionary["Generator Table"].append(table_name)
            elif "labbook" in table_name:
                self.table_dictionary["Labbook Table"].append(table_name)
            elif "results" in table_name:
                self.table_dictionary["Result Table"].append(table_name)
            elif "solution" in table_name:
                self.table_dictionary["Solutions"].append(table_name)
            else:
                self.table_dictionary["Other Tables"].append(table_name)
                
                

        # create a button for each table
        self.retrieve_tables("Analysis Table", True)
        self.select_table.clear()
        self.select_table.addItems(list(self.table_dictionary.keys()))
        

    def retrieve_tables(self, manual_table = None, manual = None):
        """
        When button clicked then we should retrieve the associated tables to structure the
        Tables better
        Args:
            manual_table type: str Name of the table to be retrieved
            manual type: bool if true then we are in manual mode
        """
        
        if manual_table == "":
            manual_table = "Result Table"
        retrieved_tables = sorted(self.table_dictionary[manual_table])
    
        self.database_table.clear()

        # add each item to the listview
        self.database_table.addItems(retrieved_tables)
        if manual:
            self.pull_table_from_database(None,"offline_analysis")

    @Slot(str)
    def pull_table_from_database(self, event = None,  text_query = None):
        '''
        Pull the table from the database and plot it
        Args:
            event: event that triggered the function
            text_query: if not None then we are in manual mode, else click event sender will be registered
        '''
        table_name = text_query or self.sender().currentItem().text()
        q = f'SELECT * from {table_name}'
        try:
            # returns a dict, keys = column names, values = array = single rows

            table_dict = self.database_handler.database.execute(q).fetchnumpy()
            self.create_table_from_dict(table_dict)
        except Exception as e:
            print(f"failed{str(e)}")


    def create_table_from_dict(self,table_dict):
        '''
        Create a QTABLE Widget from a given input dict
        Args:
            table_dict: dict with keys = column names, values = array = single rows for the table
        '''
        # create the table from dict
        print("called")
        self.pandas_frame = pd.DataFrame(table_dict)

        if self.pandas_frame.shape[0] > 500:
            view_frame = self.pandas_frame.head(100)

        else:
            view_frame = self.pandas_frame

        # create a table widget
        if self.data_base_content:
            for i in reversed(range(self.table_layout.count())):
                self.table_layout.itemAt(i).widget().deleteLater()

        # set the TableView and the Model
        scroll_area = QScrollArea()
        self.data_base_content = QTableView()
        scroll_area.setWidget(self.data_base_content)
        scroll_area.setWidgetResizable(True)
        self.data_base_content.setObjectName("data_base_content")
        self.data_base_content.setMinimumHeight(300)
        self.data_base_content.horizontalHeader().setSectionsClickable(True)

        # create two models one for the table show and a second for the data visualizations
        self.viewing_model = PandasTable(self.pandas_frame)
        self.data_base_content_model = PandasTable(view_frame)
        self.data_base_content.setModel(self.data_base_content_model)
        self.viewing_model.resize_header(self.data_base_content)
        #self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_layout.addWidget(scroll_area)
        self.data_base_content.setGeometry(20, 20, 691, 581)

        # show and retrieve the selected columns
        self.data_base_content.show()
        # at the moment this is slow and instable and therefor is not implemented
        #self.data_base_content.clicked.connect(self.retrieve_column)


    @Slot()
    def query_data(self, multi_line = None):
        '''
        Query the database with the given query
        Args:
            multi_line: if not None than multi-line string will be generated from QDialog else single execution'''
        if multi_line:
            query = self.execute_dialog.textEdit.toPlainText()
        else:
            query = self.query_line_edit.text()
        try:
            result_dict = self.database_handler.database.execute(query).fetchnumpy()
            self.create_table_from_dict(result_dict)
        except Exception as e:
            #@TODO: add a dialog box to show the error if tables are not found
            print("Error: %s", e)


    def retrieve_column(self, index):
        """
        Here we can retrieve the data of the the selected columns

        args:
            index type: QModelIndex Index of the selected row

        returns:None
        """

        index = self.data_base_content.currentIndex().column()
        data = []
        for row in range(self.viewing_model.rowCount(index)):
            it = self.viewing_model.index(row, index).data()
            data.append(it if it is not None else "")
        try:
            float_table = np.asarray([float(x) for x in data])
            self.draw_table(float_table)
        except Exception as e:
            print(f"The Error is: {e}" )


    def draw_table(self, floating_numbers):
        """
        Draws the selected column if it contains numbers
        The data amount is using only every 10th point to reduce
        slowness of the matplotlib plot

        args:
            floating_numbers type(np.array): list of numbers
            """
        if self.plot:
            for i in reversed(range(self.gridLayout_10.count())):
                self.gridLayout_10.itemAt(i).widget().deleteLater()
        # this should show the sliced array
        if self.canvas:
            self.canvas.deleteLater()

        sliced_array = floating_numbers[::10]
        self.raw_database_signal_plot(sliced_array)

        # draw the figure
    def raw_database_signal_plot(self, sliced_array):
        """
        Draws the raw signal of the selected column
        in the DataBase Viewer
        Args:
            sliced_array (_type_): array of data, where only every 10th point
            is used to reduce the overhead
        """
        # creates the Canvase
        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        self.navigation = NavigationToolbar(self.canvas, self)
        #add the buttons for the plot navigation
        self.plot_option_connection()
        #draws the figure
        self.draw_figure()

    def plot_option_connection(self):
        """
        Plot Control Options mapped to the ribbon bar buttons
        """
        self.plot_zoom.clicked.connect(self.navigation.zoom)
        self.plot_home.clicked.connect(self.navigation.home)
        self.plot_move.clicked.connect(self.navigation.pan)
        self.save_plot_online.clicked.connect(self.save_image)

    def draw_figure(self):
        """
        Draws the figure in the canvas
        @ToDO add this to the frontend class
        args:
            fig type: matplotlib.figure.Figure
        returns:
            None"""
        fig = self.canvas.figure
        ax = fig.add_subplot(111)
        fig.tight_layout()
        ax.set_xlabel("Time")
        ax.set_ylabel("Unit [A]|[V]")
        self.gridLayout_10.addWidget(self.canvas)

    def save_image(self):
        """
        Saves the current plot as png file
        """
        if self.canvas:
            response = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png)")
            self.canvas.figure.savefig(response[0])
            response.close()
        else:
            raise AttributeError("No Plot selected here")
            # add here a QDialog that opens with error message

    def search_database_table(self):
        # this needs to be implemented
        text = self.lineEdit.text()
        table = self.database_handler.database.execute(f"Select * from {text}").fetchdf()
        table = table.iloc[:100,]
        self.data_base_content_model.update_data(table)

    def export_offline_analysis_id(self):
        database_export = ExportOfflineDialog(self.database_handler, self.frontend_style)

