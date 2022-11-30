from PySide6.QtCore import *  # type: ignore
from tree_item_class import TreeItem
import numpy as np


class TreeModel(QAbstractItemModel):
    def __init__(self, data_df, discarded = None, parent=None):
        super(TreeModel, self).__init__(parent)

        # data frame with columns comes in
        # column names will always hold item_name, parent, type, level, identifier

        # artificially, remove, hidden1 and hidden2 will be added
        header = ["experiment", "series", "remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]

        # This can change in size according to unique types within input dataframe
        self.item_dict = {}
        for i in range(0,len(header)):
            self.item_dict.update({header[i]:i})

        print(self.item_dict)

        self.column_count = len(header)
        self.parent_dict = None
        self.discarded = discarded
        self.rootItem = TreeItem(header)
        self.setupModelData(data_df, self.rootItem)


    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

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
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def setupModelData(self, data_df, parent):
        # [item_name, parent, type, level, identifier]
        parents = [parent]
        parent_dict = {"root":parents[-1]}
        print("incoming df ")
        print(data_df)
        for i in np.unique(data_df["level"]):
            print("level = ", i)

            # list of lists: dataframe row wise
            items_to_add = data_df[data_df["level"]==i].values.tolist()

            for item in items_to_add:
                # create a list representing the row that will be written into the tree
                print(item)
                list_for_one_item = [""] * self.column_count

                list_for_one_item[i]=item[0]

                if self.discarded:
                    list_for_one_item[self.item_dict["remove"]] = "<-"
                else:
                    list_for_one_item[self.item_dict["remove"]] = "x"

                list_for_one_item[self.item_dict["hidden2_type"]]= item[2]

                list_for_one_item[self.item_dict["hidden3_parent"]]=item[1]

                if item[2]=="Series":
                    list_for_one_item[self.item_dict["hidden1_identifier"]] = item[4]

                if item[2]=="Experiment":
                    #print("experiment")
                    #print(item[0])
                    root = parent_dict.get("root")
                    new_parent = TreeItem(list_for_one_item, root)
                    parent_dict.update({str(item[0]): new_parent})
                    root.appendChild(new_parent)
                else:
                    print("series")
                    print(parent_dict.get(str(item[1])))
                    parent = parent_dict.get(str(item[1]))
                    new_parent = TreeItem(list_for_one_item, parent)
                    parent_dict.update({str(item[0]): new_parent})
                    parent.appendChild(new_parent)

        self.parent_dict = parent_dict
