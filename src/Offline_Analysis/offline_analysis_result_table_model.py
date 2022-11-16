from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor
import numpy as np
class OfflineAnalysisResultTableModel(QAbstractTableModel):

    # data come as dataframe

    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.input_data_frame = data
        self.input_data_dict = data.to_dict()
        self.column_count = len(data.columns)
        self.row_count = len(data.index)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.input_data_frame.columns[section]
        else:
            return f"{section}"

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        #print(row)
        #print(column)
        #print("return val = ",np.array(self.input_data_frame)[row][0])
        if role == Qt.DisplayRole:
            return str(np.array(self.input_data_frame)[row][column])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.black)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None