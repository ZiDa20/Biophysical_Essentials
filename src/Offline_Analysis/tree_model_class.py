from PySide6.QtCore import *  # type: ignore
from Offline_Analysis.tree_item_class import TreeItem
import numpy as np

class TreeModel(QAbstractItemModel):
    # a class to create a model to be displayed in a treeview widget
    # model will be a pandas data frame

    def __init__(self, data_df, discarded = None, parent=None):



        super(TreeModel, self).__init__(parent)

        # data frame with columns comes in
        # column names will always hold item_name, parent, type, level, identifier

        self.header = []
        #if not data_df.empty:
        print("data_df", data_df)
        if data_df.empty:
            return None
        display_columns = data_df["type"].unique().tolist()
        print(display_columns)
        """
        if "Experiment" in display_columns:
            self.header.append("experiment")
        if "Series" in display_columns:
            self.header.append("series")
        if "Sweep" in display_columns:
            self.header.append("sweep")
        """

        #self.header = self.header + ["remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]
        self.header = display_columns + ["remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]

        # This can change in size according to unique types within input dataframe
        self.item_dict = {}
        for i in range(0,len(self.header)):
            self.item_dict.update({self.header[i]:i})

        print("item dictionary =", self.item_dict)

        self.column_count = len(self.header)
        self.parent_dict = None
        self.discarded = discarded
        self.rootItem = TreeItem(self.header)
        root_parent = [self.rootItem][-1]
        self.parent_dict = {"root":root_parent}
        self.setupModelData(data_df, self.rootItem)
        self._data = data_df


    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            try:
                return self.rootItem.columnCount()
            except AttributeError:
                return 0

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return item.data(index.column())

    def get_data_row(self,index, role):
        if not index.isValid():
            return None

        if role != Qt.DisplayRole:
            return None

        item = index.internalPointer()

        return (item.itemData[index.column()], item.itemData)

    def get_parent_data(self,index):
        if not index.isValid():
            return None

        item = index.internalPointer()
        parentItem = item.parent()
        return parentItem.itemData

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)
        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            try:
                parentItem = self.rootItem
            except AttributeError:
                return 0
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, data_df, parent):
        # [item_name, parent, type, level, identifier]

        print("incoming df ")
        print(data_df)

        # go through each level of the data frame 
        for i in np.unique(data_df["level"]):
            print("level = ", i)

            # list of lists: dataframe row wise
            items_to_add = data_df[data_df["level"]==i].values.tolist()

            for item in items_to_add:
                # create a list of lists.
                # each list is representing a row that will be added to the tree
                
                list_for_one_item = [""] * self.column_count
                type = item[2]
                list_for_one_item[self.item_dict[type]]=item[0]

                if self.discarded: # should not be shown on sweep and meta data level
                    list_for_one_item[self.item_dict["remove"]] = "<-"
                else:
                    list_for_one_item[self.item_dict["remove"]] = "x"

                list_for_one_item[self.item_dict["hidden2_type"]]= item[2]

                list_for_one_item[self.item_dict["hidden3_parent"]]=item[1]

                if item[2]=="Series":
                    list_for_one_item[self.item_dict["hidden1_identifier"]] = item[4]

                parent = self.parent_dict.get(str(item[1]))
                new_parent = TreeItem(list_for_one_item, parent)
                self.parent_dict.update({str(item[4]): new_parent})
                #print("appending parent", str(item[4]))

                """
                if item[2]=="Series" or item[2]=="Sweep":
                    parent_name = str(item[1]) + "_" + str(item[4])
                    self.parent_dict.update({parent_name: new_parent})
                    print("appending parent: ", parent_name)
                else:
                """
                try:
                    parent.appendChild(new_parent)
                except Exception as e:
                    print(e)