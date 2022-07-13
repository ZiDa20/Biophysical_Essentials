import sys

import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView


class PandasTable(QAbstractTableModel):
    """ this table can abstract the pandas table into a pyqt table that might be editable
    --> AbstractModel as input
    ToDO MZ: implement in OnlineAnalysis 
    --> Need to build a table
    """

    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index): # get the number of rows
        """ get the dataframe shape row
        index -> int """
        return self._data.shape[0]

    def columnCount(self, parnet=None): # get the number of columns
        """ get the dataframe shape colum
        """
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole): # get the data
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data.iloc[index.row(), index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.iloc[index.row(), index.column()] = value
            return True
        return False

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable 

