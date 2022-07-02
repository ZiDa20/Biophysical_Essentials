from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import re
import heka_reader
from functools import partial
import csv
import sys
import os
import logging

import time
sys.path.append(os.getcwd()[:-3] + "QT_GUI")
from add_new_meta_data_group_pop_up_handler import Add_New_Meta_Data_Group_Pop_Up_Handler
from Worker import Worker
from data_db import *
import pandas as pd


class TreeViewManager():
    """ Main class to handle interactions with treeviews. In general two  usages are defined right now:
    1) read multiple .dat files from a directory and create representative treeview + write all the data into a datbase
    2) read a single .dat file without writing to the database.

    Each time a NEW tree view will be needed, a new instance of this class will be generated representing a new treeview
    object. Objects might be changed in a later request.
    ---

    This class is splitted into the following subsections:
    A) Create treeview functions
    B) Functions to interact with created treeviews
    C) Helper Functions

    __author__: dz
    """

    def __init__(self,database=None):

        self.database = database

        # column 1 shows checkbox to select an item and provide information about selected items
        self.checkbox_column = 1

        # column 2 displays meta data group information
        self.meta_data_group_column = 2

        # column 3 in the treeview shows red cross or blue reinsert arrow
        self.discard_column = 3

        # list of meta data group names represented as strings
        self.meta_data_option_list=["+ Add", "None"]

        # frontend style can be set to show all popups in the correct theme and color
        self.frontend_style = None

        self.analysis_mode = 0

        # analysis mode 0 = online analysis with a single .dat file, analysis mode 1 = offline_analysis with multiple files
        if self.database is None:
            print("setting analysis mode 0 (online analysis)")
        else:
            self.analysis_mode = 1
            print("setting analysis mode 1 (offline analysis)")

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self._node_list_STATE = []
        self._discardet_nodes_STATE = []
        self._pgf_info_STATE = []

        self.stimulation_count = 0
        self.channel_count = 0
        self.stim_channel_count = 0

        self._data_view_STATE = 0

        # introduce logger
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/tree_view_manager.log')
        print(file_handler)
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info('Treeview Manager Initialized')

    """ ############################## Chapter A Create treeview functions ######################################### """

    def get_series_specific_treeviews(self, selected_tree, discarded_tree, dat_files, directory_path, series_name):
        '''
        Function to fill selected and discarded tree view with tree representations of experiments containing only one
        specific series.

        :param selected_tree: treeview object to be filled with the selected objects
        :param discarded_tree: treeview object to be filled with the discarded objects
        :param dat_files: list of file names
        :param directory_path: path to the dat_files directory as string object
        :param series_name:  name of the user selected series that will be the only one in the new treeview in each
        experiment
        :return: None
        '''

        print("specific analysis view for series ", series_name)

        # analysis mode 1 = offline analysis
        self.analysis_mode = 1

        # no database interaction needed when treeview will be created - therefore database mode == 0
        self.create_treeview_from_directory(selected_tree,discarded_tree,dat_files,directory_path,0,series_name)

    def insert_parent_into_treeview_from_database(self,selected_tree,discarded_tree, parent,experiment_name):
        # insert the created parent
        selected_tree.addTopLevelItem(parent)

        # add discard button in the globaly specified discard column
        discard_button = QPushButton()
        pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
        discard_button.setIcon(pixmap)

        discard_button.clicked.connect(partial(self.discard_button_clicked, parent, selected_tree, discarded_tree))
        selected_tree.setItemWidget(parent, self.discard_column, discard_button)

        # add combo box for meta data group selection
        selected_tree = self.add_meta_data_combo_box_and_assign(experiment_name, selected_tree, parent)
        # add correct meta data group
        # tree = self.add__meta_data_combo_box_and_assign_correctly(tree, parent)


    def create_treeview_from_database(self,selected_tree,discarded_tree,experiment_label,specific_series_name=None):
        """ read through the database and fill the trees of selected and discarded items"""

        # discarded = False = means read all selected items
        self.fill_treeview_from_database(selected_tree,discarded_tree, experiment_label,False, specific_series_name)
        self.fill_treeview_from_database(discarded_tree,selected_tree, experiment_label, True, specific_series_name)

    def fill_treeview_from_database(self,tree,discarded_tree,experiment_label,discarded_state, specific_series_name):

        # get the experiments linked with this analysis number
        not_discard_experiments_stored_in_db = self.database.get_experiment_names_by_experiment_label(experiment_label)

        # @todo not implemented yet - also add !
        discard_experiments_stored_in_db = []

        # add the common tree root
        parent = ""

        # for each experiment built a single tree and append to the main
        for experiment in not_discard_experiments_stored_in_db:

            # the experiment name will be mapped with the new analysis
            # @todo if already existing it will not be inserted again will happen since create_treeview_from_database will be called multiple times
            self.database.create_mapping_between_experiments_and_analysis_id(experiment)

            # add experiment as top level item, read meta data group too
            # create a new toplevelitem according to the toplevelcount
            top_level_item_amount = tree.topLevelItemCount()

            if top_level_item_amount == 0:
                parent = QTreeWidgetItem(tree)
            else:
                parent = QTreeWidgetItem(top_level_item_amount)

            parent.setText(0, experiment)

            # list of tuples: [('Block Pulse', 'Series1'), ... ]
            series_identifier_tuple = self.database.get_series_names_of_specific_experiment(experiment,discarded_state)

            if series_identifier_tuple is None:
                #@todo error handling
                print("error")

            if specific_series_name is not None:
                # figure out whether the experiment contains no, one ore multiple series by this series name
                series_identifier_list = []

                for tuple in series_identifier_tuple:
                    if tuple[0]==specific_series_name:
                        series_identifier_list.append(tuple[1])


                if len(series_identifier_list)>0:
                    # the parent will only added if there are valid series inside
                    self.insert_parent_into_treeview_from_database(tree, discarded_tree, parent, experiment)

                    for series_identifier in series_identifier_list:
                        child = QTreeWidgetItem(parent)
                        child.setText(0, specific_series_name)
                        child.setData(3, 0, (experiment, series_identifier))

                        discard_button = QPushButton()
                        pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
                        discard_button.setIcon(pixmap)

                        discard_button.clicked.connect(
                            partial(self.discard_button_clicked, child, tree, discarded_tree))

                        tree.setItemWidget(child, self.discard_column, discard_button)

                        sweep_table_data_frame = self.database.get_sweep_table_for_specific_series(experiment,
                                                                                                   series_identifier)
                        column_names = sweep_table_data_frame.columns.values.tolist()

                        for sweep_number in range(0, len(sweep_table_data_frame.columns)):
                            sweep_child = QTreeWidgetItem(child)
                            sweep_child.setText(0, column_names[sweep_number])


            else:
                #insert the experiment as parent
                self.insert_parent_into_treeview_from_database(tree,discarded_tree,parent,experiment)

                # add all series of an existing experiment to the parent item
                for tuple in series_identifier_tuple:

                    series_name = tuple[0]
                    series_identifier = tuple[1]

                    child = QTreeWidgetItem(parent)
                    child.setText(0, series_name)
                    child.setData(3,0,(experiment, series_identifier))

                    #child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                    #child.setCheckState(self.checkbox_column, Qt.Unchecked)

                    discard_button = QPushButton()
                    pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
                    discard_button.setIcon(pixmap)

                    discard_button.clicked.connect(
                        partial(self.discard_button_clicked, child, tree, discarded_tree))

                    # insert the button
                    tree.setItemWidget(child, self.discard_column, discard_button)

                    # get the data as a dataframe, tuple[1] holds the exact identifier
                    sweep_table_data_frame = self.database.get_sweep_table_for_specific_series(experiment,series_identifier)
                    column_names = sweep_table_data_frame.columns.values.tolist()

                    for sweep_number in range(0,len(sweep_table_data_frame.columns)):
                        sweep_child = QTreeWidgetItem(child)
                        sweep_child.setText(0,column_names[sweep_number] )

        #return selected_tree, discarded_tree

    def write_directory_into_database(self, dat_files, directory_path, selected_tree,discarded_tree):
        # write the .dat files into the database
        for i in dat_files:
            file = directory_path + "/" + i
            bundle = self.open_bundle_of_file(file)
            splitted_name = i.split(".")
            pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], bundle, [], None, None, None)
            """
            self.database.database.close()

            worker = Worker(self.single_file_into_db, index=[], bundle=bundle, experiment_name=splitted_name[0], database=None, data_access_array=[0,-1,0,0],
                                     series_identifier="", pgf_tuple_data_frame=pgf_tuple_data_frame)

            worker.signals.result.connect(self.print_output)
            worker.signals.finished.connect(partial(self.update_treeview,selected_tree,discarded_tree))
            worker.signals.progress.connect(self.progress_fn)

            self.threadpool.start(worker)
            """

            self.single_file_into_db([], bundle,  splitted_name[0], self.database, [0, -1, 0, 0],"", pgf_tuple_data_frame)


        self.update_treeview(selected_tree,discarded_tree)

    def print_output(self):
        print('output')

    def progress_fn(self):
        print('progress')

    def update_treeview(self,selected_tree,discarded_tree):
        selected_tree.clear()
        self.create_treeview_from_database(selected_tree, discarded_tree, "", None)

    #progress_callback
    def single_file_into_db(self,index, bundle, experiment_name, database, data_access_array , series_identifier, pgf_tuple_data_frame=None):

            if database is None:
                database = DuckDBDatabaseHandler.init_database()
                self.database = database

            self.logger.info("started treeview generation")
            #print("started treeview generation")
            root = bundle.pul
            node = root

            # select the last node
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

            self.logger.info("processed" + node_type)

            metadata = node

            if "Pulsed" in node_type:
                print("skipped")
                parent = ""

            if "Group" in node_type:
                self.database.add_experiment_to_experiment_table(experiment_name)

            if "Series" in node_type:
                sliced_pgf_tuple_data_frame = pgf_tuple_data_frame[pgf_tuple_data_frame.series_name == node_label]
                database.add_single_series_to_database(experiment_name, node_label, node_type)
                database.create_series_specific_pgf_table(sliced_pgf_tuple_data_frame,
                                                          "pgf_table_" + experiment_name + "_" + node_type,
                                                          experiment_name, node_type)
                # update the series counter
                data_access_array[1]+=1
                # reset the sweep counter
                data_access_array[2] = 0
                # update series_identifier
                series_identifier = node_type

            if "Sweep" in node_type :
                data_array = bundle.data[data_access_array]
                database.add_single_sweep_to_database(experiment_name, series_identifier, data_access_array[2]+1, metadata,
                                                          data_array)
                data_access_array[2] += 1

            if "NoneType" in node_type:
                self.logger.info(
                    "None Type Error in experiment file " + experiment_name + " detected. The file was skipped")
                return

            for i in range(len(node.children)):
                # progress_callback
                self.single_file_into_db(index + [i], bundle, experiment_name, database, data_access_array ,
                                    series_identifier, pgf_tuple_data_frame)


    def create_treeview_from_directory(self, tree, discarded_tree ,dat_files,directory_path,database_mode,series_name=None,tree_level=None):
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

            self.logger.info("processing file " + file)

            # open the file
            bundle = self.open_bundle_of_file(file)

            # add the experiment name into experiment table and create the mapping between this experiment id and the current offline analysis id
            # the mapping table is there to map an experiment (by it's id) to a new analysis id instead of creating a copy of all data in the xperiment

            splitted_name = i.split(".")

            if database_mode:

                insertion_state = self.database.add_experiment_to_experiment_table(splitted_name[0])
                self.database.create_mapping_between_experiments_and_analysis_id(splitted_name[0])

                # no database interaction when the file is already in the database to safe time
                # @todo ask the user whether this is ok or not - give a manual option
                if insertion_state == 0:
                    database_mode = insertion_state
                    print("turned off database mode ")

            pgf_tuple_data_frame= self.read_series_specific_pgf_trace_into_df([],bundle,[],None,None,None)

            tree, discarded_tree = self.create_treeview_from_single_dat_file([], bundle, "", [],tree, discarded_tree, splitted_name[0]
                                                                             ,self.database,database_mode,pgf_tuple_data_frame,series_name,tree_level)





            print(pgf_tuple_data_frame)

            print("created tree for file" + i)



            # turn on database mode for the next file
            database_mode = 1
            print("turned on database mode ")


        return tree, discarded_tree

    def create_treeview_from_single_dat_file(self, index, bundle, parent, node_list, tree, discarded_tree,
                                             experiment_name, database,data_base_mode,pgf_tuple_data_frame=None, series_name=None, tree_level= None):
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

        # tree level controls the depth of the tree, 1= group, 2 = series, 3 = sweep, 4 = trace
        if tree_level is None:
            tree_level = 4

        root = bundle.pul
        node = root

        # select the last node
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

        self.logger.info("processed" + node_type)

        # create the discard button to move an item from one tree to another
        discard_button = QPushButton()
        pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\discard_red_cross_II.png")
        discard_button.setIcon(pixmap)

        
        metadata = node
        #print(node_type)
        #print(metadata)



        if "Pulsed" in node_type:
            print("skipped")
            parent = ""

        if "Group" in node_type and tree_level>0:
            parent,tree = self.add_group_to_treeview(tree, discarded_tree, node_label, experiment_name, pixmap)

        if "Series" in node_type and tree_level>1:

            sliced_pgf_tuple_data_frame = None

            if pgf_tuple_data_frame is not None:
                sliced_pgf_tuple_data_frame = pgf_tuple_data_frame[pgf_tuple_data_frame.series_name == node_label]

            parent,tree = self.add_series_to_treeview(tree, discarded_tree, parent, series_name, node_label, node_list,
                                                      node_type, experiment_name, data_base_mode, database, pixmap,
                                                      sliced_pgf_tuple_data_frame)



        if "Sweep" in node_type and tree_level>2:
            parent = self.add_sweep_to_treeview(series_name, parent, node_type, data_base_mode, bundle, database,
                                                experiment_name, metadata)

        if "Trace" in node_type and tree_level>3:
            if self.analysis_mode==0:

                # trace meta data information will be added to the sweep level
                parent.setData(5,0,node.get_fields())

        if "NoneType" in node_type:
            self.logger.info("None Type Error in experiment file " + experiment_name + " detected. The file was skipped")
            return tree, discarded_tree

        node_list.append([node_type, node_label, parent])


        for i in range(len(node.children)):
            self.create_treeview_from_single_dat_file(index + [i], bundle, parent, node_list, tree, discarded_tree, experiment_name,
                                                      database, data_base_mode,pgf_tuple_data_frame,series_name,tree_level)

        self.final_tree = tree
        return tree, discarded_tree

    def add_group_to_treeview(self,tree,discarded_tree, node_label,experiment_name,pixmap):
        '''
        Adds a new group item (experiment) to the treeview.
        :param tree: tree where to add the new group
        :param discarded_tree:
        :param node_label:
        :param experiment_name: string name of the experiment
        :param pixmap: style pixmap for the concerning button
        :return:
        '''

        # create a new toplevelitem according to the toplevelcount
        top_level_item_amount = tree.topLevelItemCount()
        if top_level_item_amount == 0:
            parent = QTreeWidgetItem(tree)
        else:
            parent = QTreeWidgetItem(top_level_item_amount)

        # analysis mode decodes whether data will be written(1) to database or not(0)
        if self.analysis_mode == 0:
            parent.setText(0, node_label)
            parent.setData(3, 0, [0])  # hard coded tue to .dat file structure
        else:
            parent.setText(0, experiment_name)
            parent.setData(3, 0, [experiment_name])

        # insert the created parent
        tree.addTopLevelItem(parent)

        # add discard button in coloumn 2
        # print("adding discard button to parent ")
        discard_button = QPushButton()
        discard_button.setStyleSheet("border:none")
        discard_button.setIcon(pixmap)
        discard_button.clicked.connect(partial(self.discard_button_clicked, parent, tree, discarded_tree))

        tree.setItemWidget(parent, self.discard_column, discard_button)

        # add combo box for meta data group selection
        tree = self.add_new_meta_data_combo_box(tree,parent)

        return parent,tree

    def add_series_to_treeview(self,tree,discarded_tree,parent,series_name,node_label,node_list,node_type,
                               experiment_name,data_base_mode,database,pixmap,pgf_tuple_data_frame=None):
        '''
        Function to add a new series-node to the tree.
        :param tree: treeview of the selected objects
        :param discarded_tree: treeview of the discarded objects
        :param parent: parent node object
        :param series_name:
        :param node_label:
        :param node_list:
        :param node_type:
        :param experiment_name:
        :param data_base_mode:
        :param database:
        :param pixmap:
        :return:
        '''

        if series_name is None or series_name == node_label:
            for s in node_list:
                if "Group" in s[0]:
                    parent = s[2]
                    break

            child = QTreeWidgetItem(parent)
            child.setText(0, node_label)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setCheckState(self.checkbox_column, Qt.Unchecked)
            series_number = self.get_number_from_string(node_type)
            data = parent.data(3, 0)

            if data_base_mode:
                database.add_single_series_to_database(experiment_name, node_label, node_type)

                database.create_series_specific_pgf_table(pgf_tuple_data_frame,
                                                          "pgf_table_"+experiment_name+"_" + node_type,
                                                          experiment_name, node_type)

            if self.analysis_mode == 0:
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
            discard_button.setStyleSheet("border:none")
            discard_button.setFixedSize(QSize(40, 30))
            discard_button.setIcon(pixmap)
            discard_button.setStyleSheet("border:none")
            discard_button.clicked.connect(partial(self.discard_button_clicked, child, tree, discarded_tree))

            tree.setItemWidget(child, self.discard_column, discard_button)

            # add combo box for meta data group selection
            tree = self.add_new_meta_data_combo_box(tree, parent)

            return parent,tree

        else:
            print("rejected")
            # returns the input tree and parent
            return parent, tree

    def add_sweep_to_treeview(self, series_name,parent,node_type,data_base_mode,bundle,database,experiment_id,metadata):
     '''
     Adds the data array and related meta data to the database.
     :param series_name: name (vartype text) of the recorded series (e.g. IV)
     :param parent: parent widget item -> in this case a series item
     :param node_type:
     :param data_base_mode:
     :param bundle:
     :param database:
     :param experiment_id:
     :param metadata:
     :return:
     '''

     if series_name is None or series_name == parent.text(0):
        child = QTreeWidgetItem(parent)
        child.setText(0, node_type)
        child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
        child.setCheckState(self.checkbox_column, Qt.Unchecked)
        sweep_number = self.get_number_from_string(node_type)
        data = parent.data(3, 0)


        if self.analysis_mode == 0:
            data.append(sweep_number - 1)
            data.append(0)
        else:
            data.append(sweep_number)
            series_identifier = self.get_number_from_string(data[1])

            if data_base_mode:
                data_array = bundle.data[[0, series_identifier - 1, sweep_number - 1, 0]]
                series_identifier = parent.data(4, 0)
                # insert the sweep
                database.add_single_sweep_to_database(experiment_id, series_identifier, sweep_number, metadata,
                                                          data_array)

        child.setData(3, 0, data)
        parent = child
        return parent

    def add_new_meta_data_combo_box(self,tree,parent):
        self.experimental_combo_box = QComboBox()
        self.experimental_combo_box = self.insert_meta_data_items_into_combo_box(self.experimental_combo_box)
        self.experimental_combo_box.setCurrentText("None")
        tree.setItemWidget(parent, self.meta_data_group_column, self.experimental_combo_box)

        self.experimental_combo_box.currentTextChanged.connect(self.add_new_meta_data_group)



        return tree

    def add_meta_data_combo_box_and_assign(self,experiment_name,tree,widget,series_identifier=None):
        """

        :return:
        :author dz, 28.06.2022
        """
        self.experimental_combo_box = QComboBox()

        #per default
        meta_data_group_name = 'None'


        if series_identifier is None:
            meta_data_group_name = self.database.get_meta_data_group_of_specific_experiment(experiment_name)

            if meta_data_group_name not in self.meta_data_option_list:
                self.meta_data_option_list.append(meta_data_group_name)
        else:
            print("not implement yet")

        self.experimental_combo_box = self.insert_meta_data_items_into_combo_box(self.experimental_combo_box)
        self.experimental_combo_box.setCurrentText(meta_data_group_name)
        tree.setItemWidget(widget, self.meta_data_group_column, self.experimental_combo_box)

        #self.experimental_combo_box.currentTextChanged.connect(self.add_new_meta_data_group)

        return tree

    """######################### Chapter B Functions to interact with created treeviews ############################"""

    def assign_meta_data_groups_from_list(self,tree,meta_data_group_assignment_list):
        ''' Goes through the final tree and will try the assign the assignments from the tuple list
        todo:  error handling for incomplete lists '''

        # extract all names (tuple position 0) and texts into a seperate list
        name_list = list(map(lambda x: x[0], meta_data_group_assignment_list))
        text_list = list(map(lambda x: x[1], meta_data_group_assignment_list))

        for ind in range(0,tree.topLevelItemCount()):
            top_level_item =  tree.topLevelItem(ind)
            top_level_combo_box = tree.itemWidget(top_level_item, self.meta_data_group_column)

            try:
                pos = name_list.index(top_level_item.text(0))
                print(text_list[pos])
                top_level_combo_box.setCurrentText(text_list[pos])
                #self.final_tree.setItemWidget(top_level_item,self.meta_data_group_column,top_level_combo_box)

            except Exception as e:
                top_level_combo_box.setCurrentText("None")
                print("Error in updating meta data group assignment")
                print(e)

    def get_meta_data_group_assignments(self):
        '''
        Iterates through each experiment and series and finally returns a list of assigned meta data group names
        :return:
        '''

        meta_data_group_assignments = []

        for index in range (self.final_tree.topLevelItemCount()):
            top_level_item=self.final_tree.topLevelItem(index)
            top_level_combo_box = self.final_tree.itemWidget(top_level_item,self.meta_data_group_column)
            meta_data_group_assignments.append((top_level_item.text(0),top_level_combo_box.currentText()))


        return meta_data_group_assignments




    def add_new_meta_data_group(self,new_text):
        '''
        Will display a new popup window if the + Add function was selected by user input. Popup asks the user to enter a
        new meta data group name.
        :param new_text: text of the newly selected combo box item
        :return: None
        __edited__ = dz, 290921
        __tested__ = FALSE
        '''

        # + add item will be always at the beginning of the list (== position 0)
        if new_text == self.meta_data_option_list[0]:
            self.enter_meta_data_pop_up = Add_New_Meta_Data_Group_Pop_Up_Handler()

            try:
                self.frontend_style.set_pop_up_dialog_style_sheet(self.enter_meta_data_pop_up)
            except Exception as e:
                print(e)
                print("Error in TreeViewManager/Add_new_meta_data: There was no style object defined for this treeview")

            # cancel button will just close the popup window
            self.enter_meta_data_pop_up.cancel_button.clicked.connect(partial(self.cancel_button_clicked,self.enter_meta_data_pop_up))

            self.enter_meta_data_pop_up.add_button.clicked.connect(self.add_meta_data_button_clicked)

            self.enter_meta_data_pop_up.exec()

    def add_meta_data_button_clicked(self):
        '''
        Returns the user input for the new meta_data_group_name.
        Throws an error to the user if the input is empty.
        :return: None
        __edited__ = dz, 290921
        __tested__ = FALSE
        '''

        new_name = self.enter_meta_data_pop_up.meta_data_name_input.text()

        if new_name:
           self.meta_data_option_list.append(new_name)
           self.enter_meta_data_pop_up.close()

           # extend all combo boxes in the tree by the newly generated item
           self.assign_meta_data_group_identifiers_to_top_level_items(self.final_tree)

           # set the current combo box to the new meta data group
        else:
            # throw an error, colored in red
            self.enter_meta_data_pop_up.error_label.setStyleSheet("color: red;")
            self.enter_meta_data_pop_up.error_label.setText("The meta data name must not be empty! Please enter a name.")

    def assign_meta_data_group_identifiers_to_top_level_items(self,input_tree):
        '''Function to go through the tree in the dialog and assign meta data group items to each top level item '''

        top_level_items_amount = input_tree.topLevelItemCount()

        for n in range(top_level_items_amount):
                tmp_item = input_tree.topLevelItem(n)
                combo_box = input_tree.itemWidget(tmp_item,self.meta_data_group_column)
                combo_box = self.insert_meta_data_items_into_combo_box(combo_box)
                input_tree.setItemWidget(tmp_item,self.meta_data_group_column,combo_box)

    def update_experiment_meta_data_in_database(self, input_tree):
        """
        Goes through the experiment names and writes them into the database.
        Called before tab widget for series specific analysis will be created -> after click on series specific analysis
        :param input_tree: tree which information will be written to the database
        :return:
        """
        self.logger.info('writing meta data from treeview into data base')

        top_level_items_amount = input_tree.topLevelItemCount()

        for n in range(top_level_items_amount):
            experiment_name  = input_tree.topLevelItem(n).text(0)
            meta_data_group = input_tree.itemWidget(input_tree.topLevelItem(n),self.meta_data_group_column).currentText()

            self.database.add_meta_data_group_to_existing_experiment(experiment_name,meta_data_group)


    def cancel_button_clicked(self,dialog):
        '''
        Function to close a given dialog
        :param dialog: dialog to be closed
        :return: None
        __edited__ = dz, 290921
        __tested__ = FALSE
        '''
        print("closing dialog now")
        dialog.close()

    def insert_meta_data_items_into_combo_box(self,combo_box):
        '''
         According to the entries in the global meta data option list, combo box items will be displayed to be selected
          by the user. If nothing is selected None will be inserted.
         :param combo_box: combo box which items will be modified
         :return: None
         __edited__ = dz, 290921
         __tested__ = FALSE
         '''

        # read the current item to be set again at the end
        current_item_text = combo_box.currentText()

        combo_box.clear()
        # reverse the list to always have the newly added group at the top
        reverse_list = list(reversed(self.meta_data_option_list))
        combo_box.addItems(reverse_list)

        # the tree row that displays  +add will be replaced by the new inserted group
        if current_item_text == self.meta_data_option_list[0]:
            combo_box.setCurrentText(reverse_list[0])
        else:
            combo_box.setCurrentText(current_item_text)
            # write change to the database

        return combo_box


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

        if item.parent():
            print(item.text(0))
            self.move_series_from_treeview_a_to_b(item, experiment_tree, discarded_tree, function)

            # assuming that a series button was clicked
            experiment_name = item.data(3,0)[0]
            series_identifier = item.data(3, 0)[1]

            #@todo if the entire experiment gets removed label each series as discarded

            #if self.database is not None:
            if function == "reinsert":
                    self.database.reinsert_specific_series(experiment_name,series_identifier)
            else:
                    self.database.discard_specific_series(experiment_name,series_identifier)
        else:
            # @todo needs to be eddited for group in online_analysis
            self.move_experiment_from_treeview_a_to_b(item,experiment_tree,discarded_tree,function)



            #database.move_experiment_to_discarded_experiments_table(item.text(0))


    def move_experiment_from_treeview_a_to_b(self, item, tree_a, tree_b,function):
        """move the item and its specific children """
        item_identifier = item.text(0) # top level item
        child_amount = item.childCount()
        index_of_item_to_delete = tree_a.indexOfTopLevelItem(item)
        tli_amount = tree_b.topLevelItemCount() # number of top level items
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
                    tree_b.setItemWidget(child, self.discard_column,
                                         self.create_row_specific_widget(child, tree_a, tree_b,function))

                tree_a.takeTopLevelItem(index_of_item_to_delete)
                return

        # 2) if the experiment was not found, the items parent, the item and it's children
        tree_a.takeTopLevelItem(index_of_item_to_delete)

        tree_b.addTopLevelItem(item)
        tree_b.setItemWidget(item, self.discard_column,
                             self.create_row_specific_widget(item, tree_a, tree_b,function))
        self.add_new_meta_data_combo_box(tree_b, item)

        for c in range(child_amount):
            child = item.child(c)
            child.setData = item.child(c).data(3,0)
            tree_b.setItemWidget(child, self.discard_column,
                                 self.create_row_specific_widget(child, tree_a, tree_b,function))
            self.add_new_meta_data_combo_box(tree_b, child)


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
                tree_b.setItemWidget(item,self.discard_column, self.create_row_specific_widget(item, tree_a, tree_b,function))

                self.add_new_meta_data_combo_box(tree_b,item)
                return

        # 3) add a new topLevelItem if no matching parent was found before
        new_parent = QTreeWidgetItem(discarded_tree_top_level_amount)
        new_parent.setText(0,parent_text)
        new_parent.setFlags(new_parent.flags() | Qt.ItemIsUserCheckable)
        new_parent.setCheckState(1, Qt.Unchecked)
        tree_b.addTopLevelItem(new_parent)
        tree_b.setItemWidget(new_parent, self.discard_column,
                             self.create_row_specific_widget(item, tree_a, tree_b,function))

        tree_b.topLevelItem(discarded_tree_top_level_amount).insertChild(0, item)
        tree_b.setItemWidget(item, self.discard_column, self.create_row_specific_widget(item, tree_a, tree_b,function))
        self.add_new_meta_data_combo_box(tree_b, new_parent)

        #return tree_a,tree_b

    def create_row_specific_widget(self,item,experiment_tree,discarded_tree,function):
        """create a new pushbutton object from a given pixmap, connect it to the button clicked function, return the object"""
        button = QPushButton()
        button.setStyleSheet("border:none")
        button.setFixedSize(QSize(40, 30))
        if function == "reinsert":
            pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\\discard_red_cross_II.png")
            # revert the flipped trees (flipping performed in reinsert button clicked)
            button.clicked.connect(partial(self.discard_button_clicked, item, discarded_tree,experiment_tree))
        else:
            pixmap = QPixmap(os.getcwd()[:-3] + "\Gui_Icons\\reinsert.png")
            button.clicked.connect(partial(self.reinsert_button_clicked, item, experiment_tree, discarded_tree))
        button.setIcon(pixmap)
       

        return button

    """####################################### Chapter C Helper Functions ########################################  """

    def open_bundle_of_file(self,file_name):
        print(file_name)
        return heka_reader.Bundle(file_name)

    def get_number_from_string(self,string):
        '''split something like Series1 into Series,1'''
        splitted_string = re.match(r"([a-z]+)([0-9]+)",string,re.I)
        res = splitted_string.groups()
        return int(res[1])


    def write_tuple_list_to_csv_file(self):

        dir_path = QFileDialog.getSaveFileName()

        # open the file in the write mode
        if not ".csv" in dir_path[0]:
            f = open(str(dir_path[0])+".csv", 'w')
        else:
            f = open(str(dir_path[0]), 'w')

        # create the csv writer
        writer = csv.writer(f)

        tuple_list = self.get_meta_data_group_assignments()

        # write single rows, elements seperated by comma, line break by whitespace
        for tuple in tuple_list:
            writer.writerow([tuple[0],tuple[1]])

        # close the file
        f.close()


    def read_series_specific_pgf_trace_into_df(self, index, bundle, data_list, holding_potential = None, series_name = None, sweep_number =None):

        # open the pulse generator part of the bundle
        root = bundle.pgf
        node = root
        for i in index:
            node = node[i]

        # node type e.g. stimulation, chanel or stimchannel
        node_type = node.__class__.__name__
        #print("Node type:")
        #print(node_type)

        if node_type.endswith('PGF'):
            node_type = node_type[:-3]


        if node_type.endswith('PGF'):
            node_type = node_type[:-3]

        if node_type == "Stimulation":
            series_name = node.EntryName
            sweep_number = node.NumberSweeps
        if node_type == "Channel":
            # Holding
            holding_potential = node.Holding

        if node_type == "StimChannel":
            duration = node.Duration
            increment = node.DeltaVIncrement
            voltage = node.Voltage

            data_list.append([series_name,str(sweep_number),node_type,str(holding_potential),str(duration),str(increment),str(voltage)])

        try:
            for i in range(len(node.children)):
                self.read_series_specific_pgf_trace_into_df(index+[i], bundle,data_list, holding_potential, series_name,sweep_number)
        except Exception as e:
            print(e)

        return pd.DataFrame(data_list,columns = ["series_name", "sweep_number","node_type", "holding_potential", "duration", "increment", "voltage"])

    ## outdated .. can be removed .. replaced by read_series_specific_pgf_trace_into_df 09.06.2022 .. dz
    def read_series_specific_pgf_trace(self,index, bundle, pgf_tuple_list,sampling_freq=None, sweep_number = None, vholding=None):
        '''
        Function to generate series specific pgf trace. The result will be always a list of lists to handle  step protocols
        and non-step protocols equally.
        :param index:
        :param bundle:
        :param pgf_tuple_list: list of tuples, tuples contain series name and a matrix of at least one signal,
        in case of step protocols with multiple signals represented as a list of lists
        :return:
        '''

        # open the pulse generator part of the bundle
        root = bundle.pgf
        node = root
        for i in index:
            node = node[i]

        # node type e.g. stimulation, chanel or stimchannel
        node_type = node.__class__.__name__
        #print("Node type:")
        #print(node_type)

        if node_type.endswith('PGF'):
            node_type = node_type[:-3]


        sampling_frequency = sampling_freq
        holding_potential = vholding
        number_of_sweeps = sweep_number
        if node_type == "Stimulation":
            sampling_frequency = 1/node.SampleInterval
            number_of_sweeps = node.NumberSweeps
            pgf_tuple_list.append((node.EntryName,[[]]))

        if node_type == "Channel":
            # Holding
            holding_potential=node.Holding

        if node_type == "StimChannel":
            duration = node.Duration
            increment = node.DeltaVIncrement
            voltage = node.Voltage
            # get the data trace list  and the series name from the last tuple

            series_name = pgf_tuple_list[len(pgf_tuple_list)-1][0]
            final_pulse_trace = pgf_tuple_list[len(pgf_tuple_list)-1][1]

            # case 1 no step protocol, only one signal in the list
            if increment == 0 and len(final_pulse_trace) <= 1:
                final_pulse_trace[0]=self.append_samples(duration,sampling_frequency,voltage,holding_potential,
                                                         final_pulse_trace[0])

            # case 2 no step protocol, multiple signals in the list because section before was step protocol
            if increment == 0 and len(final_pulse_trace) > 1:
               for sub_signal in final_pulse_trace:
                final_pulse_trace[final_pulse_trace.index(sub_signal)]=self.append_samples(duration,sampling_frequency,
                                                                                           voltage,holding_potential,sub_signal)

            # case 3 step protocol, only one signal in the list
            if increment != 0 and len(final_pulse_trace) <= 1:
                pre_signal = final_pulse_trace[0]
                final_pulse_trace = []
                iteration_stop = vholding+number_of_sweeps*increment
                for incrementation_step in range(sweep_number):
                        new_signal = pre_signal
                        voltage = voltage+incrementation_step*increment
                        new_signal= self.append_samples(duration,sampling_frequency,voltage,holding_potential,new_signal)
                        final_pulse_trace.append(new_signal)

            #case 4
            if increment == 1 and len(final_pulse_trace) >= 1:
                print("Error in PGF evaluation: two step protocols following each other isn't implemented yet")

            # write back
            pgf_tuple_list[len(pgf_tuple_list)-1]=(series_name,final_pulse_trace)


        for i in range(len(node.children)):
                # print("entered children " + str(i))
                self.read_series_specific_pgf_trace(index + [i], bundle, pgf_tuple_list, sampling_frequency, number_of_sweeps, holding_potential)

        return pgf_tuple_list


    def append_samples(self,duration,sampling_frequency,voltage,holding_potential,sub_signal):
        '''
        Helper Function that will append new data to a given sub signal. Data amount is calculated from duration and sampling frequency.
        if voltage input == 0 the holding value will be inserted as sample value instead
        :param duration:
        :param sampling_frequency:
        :param voltage:
        :param holding_potential:
        :param sub_signal:
        :return:
        '''
        # generate a number of sampling points and add them to the step trace, at the end, step trace is added to the entire signal
        for sample in range(0, int(duration * sampling_frequency)):
            if voltage != 0:
                sub_signal.append(voltage)
            else:
                sub_signal.append(holding_potential)
        return sub_signal