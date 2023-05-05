from PySide6.QtCore import QAbstractTableModel, Qt, Signal, QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from Offline_Analysis.error_dialog_class import CustomErrorDialog


class PandasTable(QAbstractTableModel):
    """ this table can abstract the pandas table into a pyqt table that might be editable
    --> AbstractModel as input
    ToDO MZ: implement in OnlineAnalysis 
    --> Need to build a table
    """
    data_changed = Signal()
    def __init__(self, data, index_uneditable = None): #sliced_data = None, 
        super().__init__()
        
        self._data = data
        self._full_data = None
        self.unchanged_data = data
        self.index_uneditable: list = index_uneditable

    
    @property    
    def full_data(self):
        return self._full_data
    
    @full_data.setter    
    def full_data(self, dataframe):
        self._full_data = dataframe
        
    def rowCount(self, parent=QModelIndex()): # get the number of rows
        """ get the dataframe shape row
        index -> int """
        return self._data.shape[0]

    def columnCount(self, parent=QModelIndex()): # get the number of columns
        """ get the dataframe shape colum
        """
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole): # get the data
        if index.isValid() and role in [Qt.DisplayRole, Qt.EditRole]:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def setData(self, index, value, role):
        
        if  self.index_uneditable is not None and index.column() not in self.index_uneditable:
        
            try:
                test_val = float(value)
                self._data.iloc[index.row(), index.column()] = value
                return True
            except Exception as e:
                # somehow we have to bring the frontend style here to use the error dialog. dz
                # CustomErrorDialog("Your input is of wrong data type. Please check your input")
                return False

        else:        
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
        
        if  self.index_uneditable is not None and index.column() in self.index_uneditable:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled 
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable 
    
    def resize_header(self,parent):
        try:
            column_count = self.columnCount()
            for i in range(column_count):
                size_hint = parent.horizontalHeader().sectionSizeHint(i)
                size_hint = size_hint + 20
                parent.horizontalHeader().resizeSection(i, size_hint)
        except IndexError as e:
            pass

    def slice_experiment_data(self, text):
        data = self.unchanged_data
        data = data[data["experiment_name"].str.contains(text)]
        self._data = data
        top_left = self.index(0, 0)
        bottom_right = self.index(1, 2)
        self.dataChanged.emit(top_left, bottom_right)
       
    def slice_series_data(self, text):
        data = self.unchanged_data
        print(text)
        data = data[data["series_name"].str.contains(text) | data["series_identifier"].str.contains(text)]
        print(data)
        self._data = data
        top_left = self.index(0, 0)
        bottom_right = self.index(1, 2)
        self.dataChanged.emit(top_left, bottom_right)

    def update_data(self, data):
        self._data = data
        top_left = self.index(0, 0)
        bottom_right = self.index(data.shape[0] - 1, data.shape[1] - 1)
        self.dataChanged.emit(top_left, bottom_right)
