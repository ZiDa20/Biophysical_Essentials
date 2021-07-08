from PySide6.QtGui import *
from PySide6.QtCore import *
import os
from PySide6.QtWidgets import *
from PySide6 import *
import re
import heka_reader
class TreeViewManager():
    ''' Main class to handle interactions with treeviews. In general two  usages are defined right now:
    1) read multiple .dat files from a directory and create representative treeview + write all the data into a datbase
    2) read a single .dat file '''

    def create_treeview_from_directory(self, tree, database,dat_files,directory_path):
        '''
        creates a treeview from multiple .dat files in a directory,
        :param tree: QTreeWidget
        :param database: Sqlite database object - must not be empty
        :param dat_files: string list of names of .dat files
        :param directory_path: string of the .dat-file directory path
        :return: a data filled QTreeWidget
        '''
        for i in dat_files:
            file = directory_path + "/" + i
            bundle = heka_reader.Bundle(file)
            # add the experiment name into experiment table
            database.add_experiment_to_experiment_table(i)
            tree = self.create_treeview_from_single_dat_file([], bundle, "", [],tree, i,database,1)

        return tree

    def create_treeview_from_single_dat_file(self, index, bundle, parent, node_list, tree, experiment_name, database,data_base_mode):
        '''

        :param index:
        :param bundle:
        :param parent:
        :param node_list:
        :param tree:
        :param experiment_name:
        :param database:
        :param data_base_mode: write into the database if this mode is enabled (1) otherwise only create treeview(0)

        :return:
        '''
        ''' creates the treeview and also writes series (info + data) and sweep (info + data) into the database'''

        root = bundle.pul
        node = root

        '''select the last node '''
        for i in index:
            node = node[i]
        node_type = node.__class__.__name__
        if node_type.endswith('Record'):
            node_type = node_type[:-6]
        try:
            node_type += str(getattr(node, node_type + 'Count'))
        except AttributeError:
            pass
        try:
            node_label = node.Label
        except AttributeError:
            node_label = ''
        metadata = []
        try:
            metadata.append(node)
        except Exception as e:
            metadata.append(node)

        discard_button = QPushButton()
        pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
        discard_button.setIcon(pixmap)

        if "Pulsed" in node_type:
            print("skipped")
            parent = ""
        if "Group" in node_type:
            parent = QTreeWidgetItem(tree)
            if data_base_mode:
                parent.setText(0, experiment_name)
                tree.addTopLevelItem(parent)
                parent.setData(3, 0, [experiment_name])
            else:
                parent.setText(0, node_label)
                parent.setData(3, 0, [0])  # hard coded tue to .dat file structure

            # add discard button in coloumn 2
            tree.setItemWidget(parent,2,discard_button)
            discard_button.clicked.connect(self.discard_button_clicked)
            #discard_button.setProperty("identifier","experimentName_seriesIdentifier")


        if "Series" in node_type:
            for s in node_list:
                if "Group" in s[0]:
                    parent = s[2]
                    break
            child = QTreeWidgetItem(parent)
            child.setText(0, node_label)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setCheckState(1, Qt.Unchecked)
            series_number = self.get_number_from_string(node_type)
            data = parent.data(3, 0)
            if data_base_mode:
                data.append(node_type)
                database.add_single_series_to_database(experiment_name,node_label,node_type)
            else:
                data.append(series_number - 1)
            child.setData(3, 0, data)
            child.setData(4,0,node_type)
            child.setExpanded(True)
            parent = child
            tree.setItemWidget(child,2,discard_button)


        if "Sweep" in node_type:
            child = QTreeWidgetItem(parent)
            child.setText(0, node_type)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setCheckState(1, Qt.Unchecked)
            sweep_number = self.get_number_from_string(node_type)
            data = parent.data(3, 0)

            if data_base_mode:
                s_p = self.get_number_from_string(data[1])
                data_array = bundle.data[[0,s_p-1,sweep_number-1,0]]
                series_identifier = parent.data(4,0)
                database.add_single_sweep_tp_database(experiment_name,series_identifier, sweep_number, metadata, data_array)
                data.append(sweep_number)
            else:
                data.append(sweep_number - 1)
                data.append(0)

            child.setData(3, 0, data)

        node_list.append([node_type, node_label, parent])



        for i in range(len(node.children)):
            self.create_treeview_from_single_dat_file(index + [i], bundle, parent, node_list, tree, experiment_name,
                                                      database,data_base_mode)

        return tree

    def get_number_from_string(self,string):
        '''split something like Series1 into Series,1'''
        splitted_string = re.match(r"([a-z]+)([0-9]+)",string,re.I)
        res = splitted_string.groups()
        return int(res[1])

    def uncheck_entire_tree(self,tree):
        top_level_items = tree.topLevelItemCount()
        for i in range(0,top_level_items):
            parent_item = tree.topLevelItem(i)
            self.uncheck_parents_childs(parent_item)
            parent_item.setCheckState(1, Qt.Unchecked)


    def uncheck_parents_childs(self,parent):
        child_count = parent.childCount()
        for c in range(0,child_count):
            parent.child(c).setCheckState(1, Qt.Unchecked)

            if parent.child(c).childCount()>0:
                self.uncheck_parents_childs(parent.child(c))


    @Slot()
    def discard_button_clicked(self):
        print("a discard button was clicked")

