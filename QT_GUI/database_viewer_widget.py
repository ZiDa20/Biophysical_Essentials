from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import duckdb
import os
from database_viewer_designer_object import Ui_Database_Viewer
from src.data_db import DuckDBDatabaseHandler


class Database_Viewer(QWidget, Ui_Database_Viewer):
    '''class to handle all frontend functions and user inputs in module offline analysis '''

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        #self.data_base_stacked_widget.setCurrentIndex(0)
        self.data_base_stacked_widget.setCurrentIndex(0)

        self.connect_to_database.clicked.connect(self.show_basic_tables)

        self.database_handler = None
        self.query_execute.clicked.connect(self.query_data)

    def update_database_handler(self,database_handler):
        self.database_handler = database_handler

    @Slot()
    def open_database(self):
        #@todo: find a way to anyhow access the already opened database object from offline analysis
        """open a dropdown menu and connect to a database selected by the user"""
        cew = os.getcwd()
        self.db_file_name = "duck_db_analysis_database.db"
        try:
            self.database = duckdb.connect(cew + "/" + self.db_file_name, read_only=True)
            self.instruction_label.setText(f'You are connected to database {self.db_file_name}')
            self.data_base_stacked_widget.setCurrentIndex(1)
            self.show_basic_tables()
        except:
            print("failed")

    def show_basic_tables(self):
        '''
        Request available tables and plot the content
        :return:
        '''
        self.data_base_stacked_widget.setCurrentIndex(1)
        self.database = self.database_handler.database

        q = """SELECT * FROM information_schema.tables"""
        tables_names = self.database.execute(q).fetchall()
        tables = []
        # for each table, create a button in a dropdown list
        # connect the button to a function plotting the table
        button_list = []
        for l in range (len(tables_names)):
            sub_list = tables_names[l]
            table_name = sub_list[2]
            tables.append(table_name)
            button_list.append(QPushButton(self.available_tables_gb))
            button_list[l].setText(table_name)
            button_list[l].setGeometry(QRect(10, 30+l*41, 150, 41))
            button_list[l].setObjectName('%s' % table_name)
            button_list[l].clicked.connect(self.pull_table_from_database)
            button_list[l].show()
        print(tables)
        print("finished")

    @Slot(str)
    def pull_table_from_database(self):
        '''

        :param table_name:
        :return:
        '''
        table_name = self.sender().text()
        q = f'SELECT * from {table_name}'

        try:
            # returns a dict, keys = column names, values = array = single rows
            table_dict = self.database.execute(q).fetchnumpy()
            self.create_table_from_dict(table_dict)
        except:
            print("failed")


    def create_table_from_dict(self,table_dict):
        '''
        Create a QTABLE Widget from a given input dict
        :param table_dict: dict with table names as keys and row values as values
        :return:
        '''
        column_names = list(table_dict.keys())
        row_values = list(table_dict.values())

        data_base_content = QTableWidget(self.groupBox_3)
        data_base_content.setGeometry(20, 20, 691, 581)
        data_base_content.setColumnCount(len(column_names))
        row_count = len(row_values[0])
        data_base_content.setRowCount(len(row_values[0]))

        for column in range(len(column_names)):
            data_base_content.setHorizontalHeaderItem(column, QTableWidgetItem(column_names[column]))
            data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            data_base_content.resizeColumnToContents(column)

        for column in range(len(column_names)):
            for row in range(len(row_values[0])):
                value = row_values[column][row]
                data_base_content.setItem(row,column,QTableWidgetItem(str(value)))

        data_base_content.show()



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
