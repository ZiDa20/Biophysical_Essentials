from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import duckdb
import os

from matplotlib.pyplot import table
from data_base_designer_object import Ui_Database_Viewer
from data_db import DuckDBDatabaseHandler
import pyqtgraph as pg
import pandas as pd
from Pandas_Table import PandasTable


class Database_Viewer(QWidget, Ui_Database_Viewer):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.data_base_stacked_widget.setCurrentIndex(0)
        self.data_base_stacked_widget.setCurrentIndex(0)

        #self.connect_to_database.clicked.connect(self.show_basic_tables)

        self.database_handler = None
        self.query_execute.clicked.connect(self.query_data)
        self.data_base_content = None
        self.plot = None
        
        

    def update_database_handler(self,database_handler):
        self.database_handler = database_handler

    @Slot()
    def open_database(self):
        #@todo: find a way to anyhow access the already opened database object from offline analysis
        """open a dropdown menu and connect to a database selected by the user"""
        cew = os.path.dirname(os.getcwd())
        self.db_file_name = "duck_db_analysis_database.db"
        try:
            self.database = duckdb.connect(cew + '/src/' + self.db_file_name, read_only=True)
            #self.instruction_label.setText(f'You are connected to database {self.db_file_name}')
            #self.data_base_stacked_widget.setCurrentIndex(1)
            self.show_basic_tables(True)
        except Exception as e:
            print(e)
            print("failed")

    def show_basic_tables(self,database_handler):
        '''
        Request available tables and plot the content
        :return:
        '''
        database_handler.database.close()
        database_handler.open_connection()
        self.database = database_handler.database

        q = """SELECT * FROM information_schema.tables"""
        tables_names = self.database.execute(q).fetchall()

        self.table_dictionary = {"imon_signal" : [], "pgf_tables":[], "imon_meta": [], "experiment": [], "analysis_table":[]}
        
        # for each table, create a button in a dropdown list
        # connect the button to a function plotting the table
        button_list = []
        for l in range (len(tables_names)):
            sub_list = tables_names[l]
            table_name = sub_list[2]

            if "imon_signal" in table_name:
                self.table_dictionary["imon_signal"].append(table_name)
            if "imon_meta" in table_name:
                self.table_dictionary["imon_meta"].append(table_name)
            if "experiment" in table_name:
                self.table_dictionary["experiment"].append(table_name)
            if "analysis" in table_name:
                self.table_dictionary["analysis_table"].append(table_name)
            if "pgf" in table_name:
                self.table_dictionary["pgf_tables"].append(table_name)

        # clean the list first to remove unwanted overlap after multiple calls
        for i in reversed(range(self.button_database_series.count())):
            self.button_database_series.itemAt(i).widget().deleteLater()

        # create a button for each table
        for key, value in self.table_dictionary.items():
            button = QPushButton(key)
            self.button_database_series.addWidget(button)
            button.clicked.connect(self.retrieve_tables)


    def retrieve_tables(self):
        """ When button clicked then we should retrieve the associated tables to structure the 
        Tables better"""
        text = self.sender().text()
        retrieved_tables = sorted(self.table_dictionary.get(text))
        self.database_table.clear()
        for tables in retrieved_tables:
            self.database_table.addItem(tables)
        
        self.database_table.itemClicked.connect(self.pull_table_from_database)
        #print("finished")

    @Slot(str)
    def pull_table_from_database(self):
        '''

        :param table_name:
        :return:
        '''
        table_name = self.sender().currentItem().text()
        q = f'SELECT * from {table_name}'

        try:
            # returns a dict, keys = column names, values = array = single rows
            table_dict = self.database.execute(q).fetchnumpy()
            self.create_table_from_dict(table_dict)
        except Exception as e:
            print("failed" + str(e))


    def create_table_from_dict(self,table_dict):
        '''
        Create a QTABLE Widget from a given input dict
        :param table_dict: dict with table names as keys and row values as values
        :return:
        '''
   
        # create the table from dict
        pandas_frame = pd.DataFrame(table_dict)
        if self.data_base_content:
            for i in reversed(range(self.table_layout.count())):
                self.table_layout.itemAt(i).widget().deleteLater()

        # set the TableView and the Model
        self.data_base_content = QTableView()
        self.data_base_content.horizontalHeader().setSectionsClickable(True)
        self.data_base_content_model = PandasTable(pandas_frame)
        self.data_base_content.setModel(self.data_base_content_model)
        self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # stretch it
        self.table_layout.addWidget(self.data_base_content)
        self.data_base_content.setGeometry(20, 20, 691, 581)

        # show and retrieve the selected columns
        self.data_base_content.show()
        self.data_base_content.clicked.connect(self.retrieve_column)
        

    @Slot()
    def query_data(self):
        '''handle input in the query field'''

        query = self.query_line_edit.text()
        try:
            result_dict = self.database.execute(query).fetchnumpy()
            #@todo handle situation when this is no dict...  e.g. a single result ?
            self.create_table_from_dict(result_dict)
        except Exception as e:
            #@todo open console and feed back the catched exception
            print("Error: %s", e)

    
    def retrieve_column(self, index):
        """ Here we can retrieve the data of the the selected columns
        
        args:
            index type: QModelIndex Index of the selected row
            
        returns:
            None"""

        index = self.data_base_content.currentIndex().column()
        data = []

        for row in range(self.data_base_content.model().rowCount(index)):
            it = self.data_base_content.model().index(row, index).data()
            data.append(it if it is not None else "")
        try:
            float_table = [float(x) for x in data]
            self.draw_table(float_table)
        except Exception as e:
            print(f"The Error is: {e}" )


    def draw_table(self, table):
        """
        Draws the selected column if it contains numbers
        
        args:
            table type(dataframe): list of numbers
            """
        if self.plot:
            self.gridLayout_10.removeWidget(self.plot)
            self.plot.setParent(None)
        self.plot = pg.plot(table)
        self.gridLayout_10.addWidget(self.plot)
