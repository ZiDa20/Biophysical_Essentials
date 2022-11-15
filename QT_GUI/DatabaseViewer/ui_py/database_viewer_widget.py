from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import duckdb
import os
from data_base_designer_object import Ui_Database_Viewer
import pandas as pd
from Pandas_Table import PandasTable
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


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

        self.canvas = None
        self.export_table.clicked.connect(self.export_table_to_csv)
        
        

    def update_database_handler(self,database_handler):
        self.database_handler = database_handler

    def export_table_to_csv(self):
        """Table will be exported as csv file"""
        if self.data_base_content is not None:
            response = QFileDialog.getSaveFileName(self, "Save File", "", "CSV(*.csv)")
            print(response)
            self.pandas_frame.to_csv(response[0])
        else:
            print("No Table to export")

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
            

    def show_basic_tables(self,database_handler):
        '''
        Request available tables and plot the content
        :return:
        '''
        database_handler.database.close()
        database_handler.open_connection()
        self.database = database_handler.database

        q = """SHOW TABLES"""
        tables_names = self.database.execute(q).fetchall() 

        self.table_dictionary = {"Result Table": [],"Raw signal" : [], "Generator Tables":[], "Meta Table": [], "Experiment": [], "Analysis Table":[]}
        
        # for each table, create a button in a dropdown list
        # connect the button to a function plotting the table
        button_list = []
        for l in range (len(tables_names)):
            table_name = tables_names[l][0]

            if "imon_signal" in table_name:
                self.table_dictionary["Raw signal"].append(table_name)
            if "imon_meta" in table_name:
                self.table_dictionary["Meta Table"].append(table_name)
            if "experiment" in table_name:
                self.table_dictionary["Experiment"].append(table_name)
            if "analysis" in table_name and "result" not in table_name:
                self.table_dictionary["Analysis Table"].append(table_name)
            if "pgf" in table_name:
                self.table_dictionary["Generator Tables"].append(table_name)
            if "results" in table_name:
                self.table_dictionary["Result Table"].append(table_name)


        # create a button for each table

        self.retrieve_tables("Experiment")
        self.select_table.clear()
        for key, value in self.table_dictionary.items():
            self.select_table.addItem(key)
        self.select_table.currentTextChanged.connect(self.retrieve_tables)


    def retrieve_tables(self, value):
        """ When button clicked then we should retrieve the associated tables to structure the 
        Tables better"""
        text = value
        print(value)
        retrieved_tables = sorted(self.table_dictionary.get(text))
        self.database_table.clear()
        for tables in retrieved_tables:
            self.database_table.addItem(tables)
        
        self.database_table.itemClicked.connect(self.pull_table_from_database)

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
        self.data_base_content = QTableView()
        self.data_base_content.setObjectName("data_base_content")
        self.data_base_content.setMinimumHeight(300)
        self.data_base_content.horizontalHeader().setSectionsClickable(True)


        # create two models one for the table show and a second for the data visualizations
        self.viewing_model = PandasTable(self.pandas_frame)
        self.data_base_content_model = PandasTable(view_frame)
        self.data_base_content.setModel(self.data_base_content_model)
        #self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.data_base_content.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
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
        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        fig = self.canvas.figure
        ax = fig.add_subplot(111)
        fig.patch.set_facecolor('#04071a')
        fig.tight_layout()
        ax.set_xlabel("Time")
        ax.set_ylabel("Unit [A]|[V]")
        ax.patch.set_facecolor('#04071a')
        ax.plot(sliced_array, color = "white")
        ax.spines['bottom'].set_color('white') 
        ax.spines['left'].set_color('white')
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')
        self.gridLayout_10.addWidget(self.canvas)

