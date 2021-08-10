from PySide6.QtGui import *
from PySide6.QtCore import *
import os
from PySide6.QtWidgets import *
from PySide6 import *
import re
import heka_reader
from functools import partial
class TreeViewManager():
    ''' Main class to handle interactions with treeviews. In general two  usages are defined right now:
    1) read multiple .dat files from a directory and create representative treeview + write all the data into a datbase
    2) read a single .dat file '''

    def __init__(self,database=None):
        self.database = database

            # analysis mode 0 = online analysis
            # analysis mode 1 = offline_analysis
        if self.database is None:
            self.analysis_mode = 0
            print("setting analysis mode 0 (online analysis)")
        else:
            self.analysis_mode = 1
            print("setting analysis mode 1 (offline analysis)")


    def get_series_specific_treeviews(self, selected_tree, discarded_tree, dat_files, directory_path, series_name):
        print("specific analysis view for series ", series_name)
        self.analysis_mode = 1
        self.create_treeview_from_directory(selected_tree,discarded_tree,dat_files,directory_path,0,series_name)

    def create_treeview_from_directory(self, tree, discarded_tree ,dat_files,directory_path,database_mode,series_name=None):
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
            bundle = self.open_bundle_of_file(file)
            # add the experiment name into experiment table
            if database_mode:
                self.database.add_experiment_to_experiment_table(i)
                self.database.create_mapping_between_experiments_and_analysis_id(i)

            tree, discarded_tree = self.create_treeview_from_single_dat_file([], bundle, "", [],tree, discarded_tree, i,self.database,database_mode,series_name)

        return tree, discarded_tree

    def open_bundle_of_file(self,file_name):
        print(file_name)
        return heka_reader.Bundle(file_name)

    def create_treeview_from_single_dat_file(self, index, bundle, parent, node_list, tree, discarded_tree, experiment_name, database,data_base_mode,series_name=None):
        """
        Creates the treeview and also writes series (info + data) and sweep (info + data) into the database
        :param index:
        :param bundle:
        :param parent:
        :param node_list:
        :param tree:
        :param discarded_tree:
        :param experiment_name:
        :param database:
        :param data_base_mode:
        :param series_name:
        :return:
        """

        root = bundle.pul
        node = root

        #select the last node
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

        discard_button = QPushButton()


        pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
        discard_button.setIcon(pixmap)

        metadata = node

        if "Pulsed" in node_type:
            print("skipped")
            parent = ""

        if "Group" in node_type:
            top_level_item_amount= tree.topLevelItemCount()
            if top_level_item_amount == 0:
                parent = QTreeWidgetItem(tree)
            else:
                parent = QTreeWidgetItem(top_level_item_amount)

            if  self.analysis_mode == 0:
                parent.setText(0, node_label)
                parent.setData(3, 0, [0])  # hard coded tue to .dat file structure
            else:
                parent.setText(0, experiment_name)
                parent.setData(3, 0, [experiment_name])

            tree.addTopLevelItem(parent)

            # add discard button in coloumn 2
            print("adding discard button to parent ")
            discard_button = QPushButton()
            discard_button.setStyleSheet("border:none")
            discard_button.setIcon(pixmap)
            discard_button.clicked.connect(partial(self.discard_button_clicked,parent,tree,discarded_tree))
            tree.setItemWidget(parent,2,discard_button)


        if "Series" in node_type:
            if series_name is None or series_name == node_label:
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
                    database.add_single_series_to_database(experiment_name, node_label, node_type)

                if  self.analysis_mode==0:
                    data.append(series_number - 1)
                else:
                    data.append(node_type)

                child.setData(3, 0, data)

                # often the specific series identifier will be needed to ensure unique identification of series
                # whereas the user will the series name instead
                child.setData(4, 0, node_type)

                child.setExpanded(False)
                parent = child

                discard_button = QPushButton()
                discard_button.setIcon(pixmap)
                discard_button.setStyleSheet("border:none")
                discard_button.clicked.connect(partial(self.discard_button_clicked, child, tree, discarded_tree))
                tree.setItemWidget(child, 2, discard_button)

            else:
                print("rejected")

        if "Sweep" in node_type:
            if series_name is None or series_name == parent.text(0):
                child = QTreeWidgetItem(parent)
                child.setText(0, node_type)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setCheckState(1, Qt.Unchecked)
                sweep_number = self.get_number_from_string(node_type)
                data = parent.data(3, 0)

                if self.analysis_mode == 0:
                    data.append(sweep_number - 1)
                    data.append(0)

                    # write the metadata dictionary to the 5 th column to read it when plotting

                else:
                    data.append(sweep_number)
                    series_identifier = self.get_number_from_string(data[1])


                    if data_base_mode:
                        data_array = bundle.data[[0, series_identifier - 1, sweep_number - 1, 0]]
                        series_identifier = parent.data(4, 0)
                        # insert the sweep
                        database.add_single_sweep_tp_database(experiment_name, series_identifier, sweep_number, metadata,
                                                              data_array)

                child.setData(3, 0, data)
                parent = child

        if "Trace" in node_type:
            if self.analysis_mode==0:
                #print("setting following metadata", node)
                #print("to node:", parent.text(0))
                #print("in series", parent.parent.text(0))
                parent.setData(5,0,node.get_fields())

        node_list.append([node_type, node_label, parent])



        for i in range(len(node.children)):
            self.create_treeview_from_single_dat_file(index + [i], bundle, parent, node_list, tree, discarded_tree, experiment_name,
                                                      database, data_base_mode,series_name)

        return tree, discarded_tree

    #def add_series_to_treeview(self,parent,node_label,node_type,data_base_mode,experiment_name,pixmap,tree,discarded_tree):



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


    def reinsert_button_clicked(self, item, experiment_tree, discarded_tree):
        print("reinsert button clicked")
        # changed tree a and b in comparison to discard_button_clicked
        self.tree_button_clicked(item, discarded_tree, experiment_tree,"reinsert")
        print("executed reinsert function")

    def discard_button_clicked(self, item, experiment_tree, discarded_tree):
        print("discard button clicked")
        self.tree_button_clicked(item, experiment_tree, discarded_tree,"discard")
        print("executed discard function")

    def tree_button_clicked(self, item, experiment_tree,discarded_tree,function):
        """function can be -reinsert- or -discard-"""
        if ".dat" in item.text(0):
            # this will be executed for .dat files
            # @todo needs to be eddited for group in online_analysis
            self.move_experiment_from_treeview_a_to_b(item,experiment_tree,discarded_tree,function)
            #database.move_experiment_to_discarded_experiments_table(item.text(0))
        else:
            self.move_series_from_treeview_a_to_b(item,experiment_tree,discarded_tree, function)

            experiment_name = item.parent().text(0)
            series_name = item.text(0)
            series_identifier = item.data(4,0)

            if self.database is not None:
                if function == "reinsert":
                    self.database.reinsert_specific_series(experiment_name,series_name,series_identifier)
                else:
                    self.database.discard_specific_series(experiment_name, series_name, series_identifier)

    def move_experiment_from_treeview_a_to_b(self, item, tree_a, tree_b,function):
        """move .dat and its specific children """
        item_identifier = item.text(0) # top level item
        child_amount = item.childCount()
        index_of_item_to_delete = tree_a.indexOfTopLevelItem(item)
        tli_amount = tree_b.topLevelItemCount()
        print("toplevelamount in destination")
        print(tli_amount)

        # 1) check if there is already a substructure of the experiment in tree b
        for i in range (tli_amount):

            # 1a) if a substructure was found, add the remaining children to tree b too and remove item from tree a
            tli = tree_b.topLevelItem(i)
            if tli.text(0)==item_identifier:

                for c in range(child_amount):
                    child = item.child(0)
                    print(i)
                    print(child.text(0))
                    c_p = child.parent()
                    p_t = c_p.text(0)
                    print(p_t)
                    ind = tree_a.indexOfTopLevelItem(c_p)
                    self.move_series_from_treeview_a_to_b(child, tree_a, tree_b, function)
                    tree_b.setItemWidget(child, 2,
                                         self.create_row_specific_widget(child, tree_a, tree_b,function))

                tree_a.takeTopLevelItem(index_of_item_to_delete)
                return

        tree_a.takeTopLevelItem(index_of_item_to_delete)
        # 2) if the experiment was not found, add the item and it's children
        tree_b.addTopLevelItem(item)
        tree_b.setItemWidget(item, 2,
                             self.create_row_specific_widget(item, tree_a, tree_b,function))

        for c in range(child_amount):
            child = item.child(c)
            tree_b.setItemWidget(child, 2,
                                 self.create_row_specific_widget(child, tree_a, tree_b,function))

    def move_series_from_treeview_a_to_b(self, item, tree_a, tree_b,function):
        """move a series from tree a to tree b, therefore it will be removed from tree a"""
        parent = item.parent()
        parent_index = tree_a.indexOfTopLevelItem(parent)
        parent_text = parent.text(0)
        item_index = parent.indexOfChild(item)
        discarded_tree_top_level_amount = tree_b.topLevelItemCount()

        # 1) remove the series item and its child from tree a
        tree_a.topLevelItem(parent_index).takeChild(item_index)

        # 1a) if there is no series in the experiment remaining, remove the empty top level item also
        child_count = tree_a.topLevelItem(parent_index).childCount()
        if child_count ==0:
            tree_a.takeTopLevelItem(parent_index)

        # 2) check if parent is already existent in tree b
        for i in range(discarded_tree_top_level_amount):
            if parent_text == tree_b.topLevelItem(i).text(0):
                print("parent is already there")
                child_amount =tree_b.topLevelItem(i).childCount()
                # insert to the last position
                tree_b.topLevelItem(i).insertChild(child_amount, item)
                tree_b.setItemWidget(item, 2, self.create_row_specific_widget(item, tree_a, tree_b,function))
                return

        # 3) add a new topLevelItem if no matching parent was found before
        new_parent = QTreeWidgetItem(discarded_tree_top_level_amount)
        new_parent.setText(0,parent_text)
        new_parent.setFlags(new_parent.flags() | Qt.ItemIsUserCheckable)
        new_parent.setCheckState(1, Qt.Unchecked)
        tree_b.addTopLevelItem(new_parent)
        tree_b.setItemWidget(new_parent, 2,
                             self.create_row_specific_widget(item, tree_a, tree_b,function))

        tree_b.topLevelItem(discarded_tree_top_level_amount).insertChild(0, item)
        tree_b.setItemWidget(item, 2, self.create_row_specific_widget(item, tree_a, tree_b,function))

        #return tree_a,tree_b

    def create_row_specific_widget(self,item,experiment_tree,discarded_tree,function):
        """create a new pushbutton object from a given pixmap, connect it to the button clicked function, return the object"""
        button = QPushButton()
        button.setStyleSheet("border:none")
        if function == "reinsert":
            pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\\discard_red_cross_II.png")
            # revert the flipped trees (flipping performed in reinsert button clicked)
            button.clicked.connect(partial(self.discard_button_clicked, item, discarded_tree,experiment_tree))
        else:
            pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\\reinsert.png")
            button.clicked.connect(partial(self.reinsert_button_clicked, item, experiment_tree, discarded_tree))
        button.setIcon(pixmap)
        return button

