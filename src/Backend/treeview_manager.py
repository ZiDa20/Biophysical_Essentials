import sys
import os

import numpy as np
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from DataReader.heka_reader import Bundle
from functools import partial
import csv

import logging
from QT_GUI.OfflineAnalysis.CustomWidget.add_new_meta_data_group_pop_up_handler import Add_New_Meta_Data_Group_Pop_Up_Handler
from QT_GUI.OfflineAnalysis.CustomWidget.SaveDialog import SaveDialog
from time import sleep
from database.data_db import *
import pandas as pd
from DataReader.ABFclass import AbfReader
from Backend.plot_widget_manager import PlotWidgetManager
from Offline_Analysis.tree_model_class import TreeModel
import itertools


class TreeViewManager:
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

    def __init__(self,database=None, treebuild_widget =None, show_sweep_radio = None):

        # it's the database handler
        self.database_handler = database

        # the promoted tree widget containing a tab widget with selected and discarded tree view
        self.tree_build_widget = treebuild_widget
        self.selected_tree_view_data_table = pd.DataFrame()
        self.discarded_tree_view_data_table = pd.DataFrame()

        # qradio button which can be checked or not
        self.show_sweeps_radio = show_sweep_radio

        # list of meta data group names represented as strings
        self.selected_meta_data_list = None

        # frontend style can be set to show all popups in the correct theme and color
        self.frontend_style = None

        self.analysis_mode = 0
        # analysis mode 0 = online analysis with a single .dat file, analysis mode 1 = offline_analysis with multiple files
        if self.database_handler is None:
            print("setting analysis mode 0 (online analysis)")
        else:
            self.analysis_mode = 1
            print("setting analysis mode 1 (offline analysis)")

        self.threadpool = QThreadPool()
    
        self._node_list_STATE = []
        self._discardet_nodes_STATE = []
        self._pgf_info_STATE = []

        self.stimulation_count = 0
        self.channel_count = 0
        self.stim_channel_count = 0

        self._data_view_STATE = 0

        self.configure_logger()
        self.configure_default_signals()

        # introduce logger


    """ ############################## Chapter A Create treeview functions ######################################### """

    def configure_logger(self):
        """
        Configure the Logger for the Treeview Manager"""
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler('../Logs/tree_view_manager.log')
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.info('Treeview Manager Initialized')

    def configure_default_signals(self):
        """Configure the Default Signals which are used for Thread Safe communication"""
        self.data_read_finished = DataReadFinishedSignal()
        self.tree_build_finished = DataReadFinishedSignal()
        self.experiment_tree_finished = DataReadFinishedSignal()

    def qthread_bundle_reading(self,dat_files, directory_path, progress_callback):
        """ read the dat files in a separate thread that reads in through the directory 
        adds the dat.files run through the heka reader to get the data file and pulse generator files
        
        args:
           dat_files type: list of strings - the dat files to be read
           directory_path type: string - the path to the directory where the dat files are located
           progress_callback type: function - the function to be called when the progress changes
           
        returns:
          bundle_list type: list of tuples - the list of bundles that were read 
          
        """
        bundle_list = [] # list of tuples (bundle_data, bundle_name, pgf_file)
        abf_list = []
        for i in dat_files:
            abf_file_data = []
            try:
                if ".dat" in i:
                    print(i)
                    file = directory_path + "/" + i # the full path to the file
                    bundle = self.open_bundle_of_file(file) # open heka reader
                    pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], bundle, []) # retrieve pgf data
                    splitted_name = i.split(".") # retrieve the name
                    bundle_list.append((bundle, splitted_name[0], pgf_tuple_data_frame, ".dat")) 

                if isinstance(i,list):
                    for abf in i:
                        print(abf)
                        file_2 = directory_path + "/" + abf
                        abf_file = AbfReader(file_2)
                        data_file = abf_file.get_data_table()
                        meta_data = abf_file.get_metadata_table()
                        pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                        experiment_name = [abf_file.get_experiment_name(), "None", "None", "None", "None", "None", "None", "None"]
                        series_name = abf_file.get_series_name()
                        abf_file_data.append((data_file, meta_data, pgf_tuple_data_frame, series_name, ".abf"))

            except Exception as e:
                # @todo error handling
                print(
                    f"Bundle file could not be read: {str(i[0])} the error occured: {str(e)}"
                )
                self.logger.error(
                    f"Bundle file could not be read: {str(i[0])} the error occured: {str(e)}"
                )

            if isinstance(i,list):
                abf_list.append((abf_file_data, experiment_name))
        print(bundle_list)
        return bundle_list, abf_list

    def write_directory_into_database(self,database, dat_files, abf_files, progress_callback):
        """ writes the bundle files as well as the pgf files and meta data files into the
        database in a separate Threads. This is done to avoid blocking the GUI.
        Tedious task with long running time, since only one connection can be opened at a time

        args:
           database type: database object - the database to write the data into
           dat_files type: list of tuples - the bundle tuple files to be read
           progress_callback type: function - the function to be called when the progress changes

        returns:
            database type: database object - the database to write the data into
        """
        self.meta_data_assigned_experiment_names =  [i[0] for i in self.meta_data_assignment_list]
        ################################################################################################################
        #Progress Bar setup
        max_value = len(dat_files)
        progress_value = 0
        database.open_connection()
        ################################################################################################################
        for i in dat_files:
            # loop through the dat files and read them in
            try:
                increment = 100/max_value
                progress_value = progress_value + increment
                self.single_file_into_db([], i[0],  i[1], database, [0, -1, 0, 0], i[2])
                progress_callback.emit((progress_value,i))
            except Exception as e:
                self.logger.error(
                    f"The DAT file could not be written to the database: {str(i[0])} the error occured: {str(e)}"
                )
                progress_callback.emit((progress_value,i))
                database.database.close() # we close the database connection and emit an error message


        for i in abf_files:
            print("running abf file and this i ", i)
            try:
                #increment = 100/max_value
                #progress_value = progress_value + increment
                self.single_abf_file_into_db(i, database)
                #progress_callback.emit((progress_value,i))

            except Exception as e:
                print(e)
                self.logger.error(
                    f"The ABF file could not be written to the database: {str(i[0])} the error occured: {str(e)}"
                )
                database.database.close() # we close the database connection and emit an error message

        # trial to see if the database opens correctly
        self.database_handler.database.close()
        return "database closed"

    def update_treeviews(self, plot_widget_manager: PlotWidgetManager):
        """
        do all the frontend handling for treeviews that are managed by the given tree_view_manager
        @param tree_view_manager: treeview manager class object
        @return:
        """

        # create two global tables that can be reused for further visualizations and store it within the related tree view manager
        selected_table_view_table = self.create_data_frame_for_tree_model(False, self.show_sweeps_radio.isChecked())
        discarded_table_view_table = self.create_data_frame_for_tree_model(True, self.show_sweeps_radio.isChecked())

        label = None
        for type in selected_table_view_table["type"].unique():
            cnt = len(selected_table_view_table[selected_table_view_table["type"] == type])
            if label:
                label = label + ", " + type + " : " + str(cnt)
            else:
                label = type + " : " + str(cnt)

        self.tree_build_widget.descriptive_meta_data_label.setText(label)

        print("new table \n ", selected_table_view_table)

        # since analysis id is primary key this will only add date when its performed first
        for row in selected_table_view_table[selected_table_view_table["type"] == "Experiment"].values.tolist():
            self.database_handler.create_mapping_between_experiments_and_analysis_id(row[0])

        # create the models for the selected and discarded tree
        self.selected_model = TreeModel(selected_table_view_table)
        self.discarded_model = TreeModel(discarded_table_view_table, "discarded")
        
        # assign the models to the visible treeview objects 
        self.tree_build_widget.selected_tree_view.setModel(self.selected_model)  
        self.tree_build_widget.selected_tree_view.expandAll()      
        self.tree_build_widget.discarded_tree_view.setModel(self.discarded_model)
        self.tree_build_widget.discarded_tree_view.expandAll()   
        # display the correct columns according to the selected metadata and sweeps
        self.set_visible_columns_treeview(self.selected_model,self.tree_build_widget.selected_tree_view)
        self.set_visible_columns_treeview(self.discarded_model,self.tree_build_widget.discarded_tree_view)

        try:
            self.tree_build_widget.selected_tree_view.clicked.disconnect()
            self.tree_build_widget.discarded_tree_view.clicked.disconnect()

        except Exception as e :
            print(e)

        self.tree_build_widget.selected_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, self.selected_model, plot_widget_manager,None))
        self.tree_build_widget.discarded_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, self.discarded_model, plot_widget_manager,None))

        self.selected_tree_view_data_table = selected_table_view_table
        self.discarded_tree_view_data_table = discarded_table_view_table

    def set_visible_columns_treeview(self,model,treeview):
        """
        the last 3 columns of the treeview should not be displayed but the remaining columns should
        """
        if model.header:
            for i in range(len(model.header)):
                if i < len(model.header) - 3:
                    treeview.setColumnHidden(i, False)
                else:
                    treeview.setColumnHidden(i, True)

    def create_data_frame_for_tree_model(self, discarded_state: bool, show_sweeps: bool, series_name = None):
        """
        @param discarded_state: True or False, indicating whether discarded (True) or non discard elements should be loaded
        @return: df, filled with experiment and series data
        """

        # create a dataframe of parents (assigned to meta data groups if selected)
        q = f'select table_name, condition_column, conditions from selected_meta_data where offline_analysis_id={self.database_handler.analysis_id} AND analysis_function_id = -1'
        table_name = self.database_handler.database.execute(q).fetchdf() # gets the table

        if not table_name.empty:
            return self.add_experiments_series_sweeps_to_meta_data_label(table_name, discarded_state, series_name)
        experiment_df =  self.create_parents_without_meta_data_parents(discarded_state)
        series_table,  series_df = self.create_series_without_meta_data(series_name, discarded_state, experiment_df)

        experiment_df = experiment_df[experiment_df["item_name"].isin(series_df["parent"].tolist())]
        if show_sweeps:
            all_sweeps_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
            for sweep_table_name in series_table["sweep_table_name"].values.tolist():
                sweep_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
                sweep_table = self.database_handler.database.execute(f'select * from {sweep_table_name}').fetchdf()
                sweep_df["item_name"] = sweep_table.columns

                identifier = series_table[series_table["sweep_table_name"] == sweep_table_name][
                    "series_identifier"].values.tolist()
                experiment_name = series_table[series_table["sweep_table_name"] == sweep_table_name][
                    "experiment_name"].values.tolist()

                parent = experiment_name[0] + "::" + identifier[0]
                print("sweep parent = ", parent)
                sweep_df["parent"] = [parent] * len(sweep_table.columns)
                sweep_df["type"] = ["Sweep"] * len(sweep_table.columns)
                sweep_df["level"] = [experiment_df["level"].max()+2] * len(sweep_table.columns)
                sweep_ids = [parent+"::"+c_name for c_name in sweep_table.columns]
                sweep_df["identifier"] = sweep_ids

                print(sweep_df)
                all_sweeps_df = pd.concat([all_sweeps_df, sweep_df])

            return pd.concat([experiment_df, series_df, all_sweeps_df])

        return pd.concat([experiment_df, series_df])

    def create_series_without_meta_data(self,series_name,discarded_state,experiment_df):
        if series_name:
            q = (f'select * from experiment_series where discarded = {discarded_state}  and series_name = \'{series_name }\' and experiment_name in (select experiment_name from global_meta_data where experiment_label = \'{self.selected_meta_data_list[0]}\')')
        else:
            q = (f'select * from experiment_series where discarded = {discarded_state}  and experiment_name in (select experiment_name from global_meta_data where experiment_label = \'{self.selected_meta_data_list[0]}\')')
        series_table = self.database_handler.database.execute(q).fetchdf()

        series_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        series_df["item_name"] = series_table["series_name"].values.tolist()
        series_df["parent"] = series_table["experiment_name"].values.tolist()
        series_df["type"] = "Series"
        series_df["level"] = experiment_df["level"].max()+1
        identifier_list = [
            experiment + "::" + identifier
            for experiment, identifier in zip(
                series_table["experiment_name"].values.tolist(),
                series_table["series_identifier"].values.tolist(),
            )
        ]
        series_df["identifier"] = identifier_list
        return series_table,  series_df

    def create_series_specific_tree(self, series_name, plot_widget_manager : PlotWidgetManager):
        """
         create a treeview containing only series of the specific series identified by series name
        """
        self.selected_tree_view_data_table = self.create_data_frame_for_tree_model( False, self.show_sweeps_radio.isChecked(), series_name)
        self.discarded_tree_view_data_table = self.create_data_frame_for_tree_model( True, self.show_sweeps_radio.isChecked(), series_name)

        selected_model = TreeModel(self.selected_tree_view_data_table)
        print("selected finished succesful")
        discarded_model = TreeModel(self.discarded_tree_view_data_table, "discarded")

        self.tree_build_widget.selected_tree_view.setModel(selected_model)
        self.tree_build_widget.selected_tree_view.expandAll()   
        self.tree_build_widget.discarded_tree_view.setModel(discarded_model)
        self.tree_build_widget.discarded_tree_view.expandAll()   

        # display the correct columns according to the selected metadata and sweeps
        self.set_visible_columns_treeview(selected_model, self.tree_build_widget.selected_tree_view)
        self.set_visible_columns_treeview(discarded_model,self.tree_build_widget.discarded_tree_view)

       
        try:
            self.tree_build_widget.selected_tree_view.clicked.disconnect()
            self.tree_build_widget.discarded_tree_view.clicked.disconnect()
        except Exception as e:
            print(e)

        self.tree_build_widget.selected_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, selected_model, plot_widget_manager, series_name))
        self.tree_build_widget.discarded_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, discarded_model, plot_widget_manager, series_name))

    def click_qtreeview_cell(self,treeview, index):
        "click on a specific cell"
        model = treeview.model()
        #item = model.data(index, Qt.DisplayRole)
        treeview.setCurrentIndex(index)
        treeview.clicked.emit(index)
        treeview.doubleClicked.emit(index)

    def handle_tree_view_click(self, model, plot_widget_manager: PlotWidgetManager, series_name, index):

        data_pos = model.item_dict

        # ["experiment", "series", "remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]
        tree_item_list = model.get_data_row(index, Qt.DisplayRole)
        print("click", tree_item_list)
        print(data_pos)
        print(tree_item_list)
        tree_item_list = list(tree_item_list)

        p  = tree_item_list[1][data_pos["hidden3_parent"]].split("::")
        tree_item_list[1][data_pos["hidden3_parent"]] = p[len(p)-1]

        i = tree_item_list[1][data_pos["hidden1_identifier"]].split("::")
        tree_item_list[1][data_pos["hidden1_identifier"]] = i[len(i)-1]

        if tree_item_list[0] == "x":
            print("x clicked")
            print(series_name)
            if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
                # set the related series to discarded
                discard_query = f'update experiment_series set discarded = True where ' \
                                f'experiment_name = \'{tree_item_list[1][data_pos["hidden3_parent"]]}\' ' \
                                f'and series_identifier = \'{tree_item_list[1][data_pos["hidden1_identifier"]]}\''
                print(discard_query)
                self.database_handler.database.execute(discard_query)

                self.update_treeviews_after_discard_reinsert(series_name,plot_widget_manager)

            if tree_item_list[1][data_pos["hidden2_type"]] == "Experiment":
                # set all series of the related series to discarded
                self.database_handler.database.execute(f'update experiment_series set discarded = True where '
                                                       f'experiment_name = \'{tree_item_list[1][data_pos["Experiment"]]}\' ')
                print("discarding an experiment")
                print(series_name)
                self.update_treeviews_after_discard_reinsert(series_name,plot_widget_manager)

        if tree_item_list[0] == "<-":
            print("<- clicked")
            if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
                # set the related series to discarded
                self.database_handler.database.execute(f'update experiment_series set discarded = False where '
                                                       f'experiment_name = \'{tree_item_list[1][data_pos["hidden3_parent"]]}\' '
                                                       f'and series_identifier = \'{tree_item_list[1][data_pos["hidden1_identifier"]]}\'')

                self.update_treeviews_after_discard_reinsert(series_name, plot_widget_manager)

            if tree_item_list[1][data_pos["hidden2_type"]] == "Experiment":
                # set all series of the related series to discarded
                self.database_handler.database.execute(f'update experiment_series set discarded = False where '
                                                           f'experiment_name = \'{tree_item_list[1][data_pos["Experiment"]]}\' ')

                self.update_treeviews_after_discard_reinsert(series_name,plot_widget_manager)

        if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
            print("series clicked")
            print(tree_item_list)
            plot_widget_manager.table_view_series_clicked_load_from_database(tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]])

            
            plot_widget_manager.check_live_analysis_plot(tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]])
        

        if tree_item_list[1][data_pos["hidden2_type"]] == "Sweep":
            print("sweep clicked")
            print(tree_item_list)

            parent_data = model.get_parent_data(index)
            print(parent_data)
            print(parent_data[data_pos["hidden3_parent"]])
            print(parent_data[data_pos["hidden1_identifier"]])
            print(data_pos)
            print(tree_item_list[1][data_pos["Sweep"]])
            plot_widget_manager.table_view_sweep_clicked_load_from_database(parent_data[data_pos["hidden3_parent"]],
                                                                            parent_data[data_pos["hidden1_identifier"]],
                                                                            tree_item_list[1][data_pos["Sweep"]])

            plot_widget_manager.check_live_analysis_plot(parent_data[data_pos["hidden3_parent"]],
                                tree_item_list[1][data_pos["hidden3_parent"]],
                                tree_item_list[1][data_pos["Sweep"]])


    def update_treeviews_after_discard_reinsert(self,series_name:str, plot_widget_manager:PlotWidgetManager):
        """

        @param series_name:
        @param plot_widget_manager:
        @return:
        """
        if series_name:
            # load the updated table
            self.create_series_specific_tree(series_name, plot_widget_manager)
        else:
            self.update_treeviews(plot_widget_manager)
        return

    def update_treeview(self):
        """ updates the treeview with the selected and discarded experiments following
        database writing
        toDO: put this also in a thread to avoid sluggish tree loading when lots of data are loaded

        args:
           selected_tree type: QTreeWidget - the treeview to be updated with the selected experiments
           discarded_tree type: QTreeWidget - the tree that is updated with the discarded experiments

        returns:
           None"""
        self.database_handler.open_connection()
        self.logger.info("Database writing thread successfully finished")  #
        # self.database.open_connection() # open the connection to the database in main thread
        
        try:
            df = self.database_handler.database.execute(
                "SELECT * FROM experiments").fetchall()  # get all the experiments as sanity
            if df:
                print("emitting signal for frontend to be ready for data read")
                self.data_read_finished.finished_signal.emit()
                # self.create_treeview_from_database(selected_tree, discarded_tree, "", None)
        except Exception as e:
            self.logger.error(f"Not able to open the database properly {str(e)}")

    def check_for_selected_meta_data(self):
        """
        check the database for anyone selected meta data to be displayed within the treeview
        """
        q = f'select selected_meta_data from offline_analysis where analysis_id = {self.database_handler.analysis_id}'
        table_name = self.database_handler.database.execute(q).fetchdf().values.tolist()
        table_name = table_name[0][0]
        print("found selected meta data", table_name)
        return table_name if table_name != np.nan else None

    def create_parents_without_meta_data_parents(self,discarded_state: bool):
        """
        create experiments as parents without any meta data
        @param discarded_state: true or false: decodes experiment discarded state.
        @return df: pandas data frame with columns [item_name, parent, type, level, identifier]
        """
        q = (f'select distinct experiment_name from experiment_series where '
             f'discarded = {discarded_state} intersect (select experiment_name from global_meta_data where '
             f'experiment_label = \'{self.selected_meta_data_list[0]}\')')

        df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        parent_name_table = self.database_handler.database.execute(q).fetchdf()

        df["item_name"] = parent_name_table["experiment_name"].values.tolist()
        df["parent"] = "root"
        df["type"] = "Experiment"
        df["level"] = 0
        df["identifier"] = parent_name_table["experiment_name"].values.tolist()
        return df       

    def create_meta_data_combinations(self,meta_data_values: list):
        """
        creates combinations of meta data values, function using recursion
        @param meta_data_values: list of meta data values
        @return df: pandas data frame with columns [item_name, parent, type, level, identifier]
        """
        # Base case: if the input lists are empty, return a list with an empty string
        # will happen due to recursion
        if not meta_data_values:
            return ['']

        # Recursive case: if the input lists are not empty, create a list of strings by
        # combining the first item in each list with the strings created from the remaining lists
        subset = [i.strip('][').split(', ') for i in meta_data_values]
        r = len(subset)
        combinations = list(itertools.product(*subset))
        combinations = ["::".join(i) for i in combinations]

        return combinations

    def create_treeview_with_meta_data_parents(self, meta_data_table):

        """
        make labels according to the entries in the meta data table
        meta_data_table = pandas data frame with columns [table, column, values]

        """
        
        # list of lists of meta data tuples per column and table
        meta_data_values = list(set(meta_data_table["conditions"].values))
        combinations = self.create_meta_data_combinations(meta_data_values)

        # Create an empty DataFrame with the necessary columns
        df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])

        # Define constants for table names
        GLOBAL_META_DATA_TABLE = "global_meta_data"
        EXPERIMENT_SERIES_TABLE = "experiment_series"
        SWEEP_META_DATA_TABLE = "sweep_meta_data"

        # go through all created meta data label combinations, e.g. [KO::Male, KO::Female, WT::Male, W::Female] and get the related experiment name
        for c in combinations:
        

            # Create query strings for each table, always reset them 
            #experiment_series_query = f' select distinct experiment_name from {EXPERIMENT_SERIES_TABLE} where discarded = {discarded_state}'
            global_meta_data_query = f'select experiment_name from {GLOBAL_META_DATA_TABLE} where experiment_label = \'{self.selected_meta_data_list[0]}\''
            #sweep_meta_data_query = f'select experiment_name from {SWEEP_META_DATA_TABLE} where '

            # add the label as parent
            new_item_df = pd.DataFrame( {"item_name": [c], "parent": "root", "type": "Label", "level": 0, "identifier": ["root::" + c]})
            df = pd.concat([df, new_item_df])

            # add meta data related experiments as childs
            meta_data_selections = c.split("::")

            for row,index,table in zip(meta_data_table["condition_column"], meta_data_selections, meta_data_table["table_name"]):

                if table ==  GLOBAL_META_DATA_TABLE:
                    # multiple columns are available for global meta data. 
                    # therefore table can appear in multiple rows and therefore I have to append
                    global_meta_data_query =  global_meta_data_query + f'and {row} = \'{index}\''
                if table ==  EXPERIMENT_SERIES_TABLE:
                    # only one column is available
                    # can only appear once
                    experiment_series_query = f'select distinct experiment_name from {EXPERIMENT_SERIES_TABLE} where {row} = \'{index}\''

            # check combination of tables
            if list(meta_data_table["table_name"].unique()) == [GLOBAL_META_DATA_TABLE]:
                experiment_names = self.database_handler.database.execute(global_meta_data_query).fetchdf() 
            else:
                experiment_series_query = experiment_series_query + f' intersect ({global_meta_data_query})'
                experiment_names = self.database_handler.database.execute(experiment_series_query).fetchdf() 


            # empty dataframe might be returned when the meta data combinations does not exist
            if not experiment_names.empty:
                experiment_names = experiment_names.values.tolist()
                experiment_names = [tup[0] for tup in experiment_names]

                identifier_list = ["root::" + c + "::" + e for e in experiment_names]
                new_item_df = pd.DataFrame( {"item_name": experiment_names, "parent": ["root::" + c]*len(experiment_names), 
                "type": ["Experiment"]*len(experiment_names), "level": [1]*len(experiment_names), "identifier": identifier_list})

                df = pd.concat([df, new_item_df])


        return df

    def add_experiments_series_sweeps_to_meta_data_label(self, meta_data_table, discarded_state, series_name = None):

    

        # get a dataframe with hierarchical strcutured meta data items and exoeriments
        df = self.create_treeview_with_meta_data_parents(meta_data_table)
        series_level = df["level"].max() + 1

        # append series to the experiments
        for index,experiment_row in df[df["type"]=="Experiment"].iterrows():
            
            series_meta_data = None
            
            if "experiment_series" in meta_data_table["table_name"].values.tolist():

                # get the parent
                label = df[df.identifier == experiment_row["parent"]]["item_name"].values[0]
                # split at ::
                label = label.split("::")
                series_meta_data = label[meta_data_table["table_name"].values.tolist().index("experiment_series")]
          
    
            df, series_table = self.add_series_to_treeview(df, experiment_row, discarded_state, series_name, series_level, series_meta_data)

            # create sweeps 
            if self.show_sweeps_radio.isChecked():
                df = self.add_sweeps_to_treeview(df, series_table, series_level, experiment_row["identifier"])

        return df

    def add_series_to_treeview(self, df, experiment_row, discarded_state, series_name, series_level, series_meta_data=None):
    

        experiment_name = experiment_row["item_name"]
        experiment_id = experiment_row["identifier"]

        if experiment_name == "220318_03":
            print("found")

        # get all series linked with this experiment
        query = f'select * from experiment_series where experiment_name = \'{experiment_name}\' and discarded = {discarded_state}'

        if series_meta_data:
            query = query + f' and series_meta_data = \'{series_meta_data}\' '

        # if specified, get only specific series names
        if series_name is not None:
            query = query + f' and series_name = \'{series_name}\''

        # get the series table from db
        series_table = self.database_handler.database.execute(query).fetchdf()

        # if no series were found for this experiment, it will be removed from the treeview
        if series_table.empty:
            df = df[df.item_name != experiment_name]
            return df, series_table

        # if series were found they need be appended to the df
        series_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        series_names = series_table["series_name"].values.tolist()
        series_df["item_name"] = series_names
        series_df["parent"] = [experiment_id]*len(series_names)
        series_df["type"] = ["Series"]*len(series_names)
        series_df["level"] = [series_level]*len(series_names)
        series_ids = [
            experiment_id + "::" + s for s in series_table["series_identifier"]
        ]
        series_df["identifier"] = series_ids
        df = pd.concat([df, series_df])

        return df, series_table


    def add_sweeps_to_treeview(self, treeview_df, series_table, series_level, identifier):

        """
        Add sweeps to a treeview DataFrame.

        Args:
            treeview_df (pandas.DataFrame): The DataFrame containing treeview data.
            series_table (pandas.DataFrame): A DataFrame containing information about the sweeps.
            series_level (int): The level at which the sweeps should be added to the treeview.
            identifier (str): The identifier of the parent of the sweeps.

        Returns:
            pandas.DataFrame: The modified treeview DataFrame with sweeps added.
        """

        #if series_table.empty:
        #    return treeview_df
                
        
        for index, row in series_table.iterrows():
            sweep_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])

            sweep_parent = identifier + "::"  + row["series_identifier"]
            sweep_table = self.database_handler.database.execute(f'select * from {row["sweep_table_name"]}').fetchdf()

            sweep_df["item_name"] = sweep_table.columns
            sweep_df["parent"] = [sweep_parent] * len(sweep_table.columns)
            sweep_df["type"] = ["Sweep"] * len(sweep_table.columns)
            sweep_df["level"] = [series_level + 1] * len(sweep_table.columns)
            sweep_ids = [sweep_parent + "::" + c_name for c_name in sweep_table.columns]
            sweep_df["identifier"] = sweep_ids

            treeview_df = pd.concat([treeview_df, sweep_df])

        return treeview_df

    def single_file_into_db(self,index, bundle, experiment_name, database,  data_access_array , pgf_tuple_data_frame=None):

        if database is None:
            database = self.database_handler

        self.logger.info("started treeview generation")
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

        self.logger.info(f"processed{node_type}")

        metadata = node

        if "Pulsed" in node_type:
            parent = ""

        if "Group" in node_type:

            self.sweep_data_df = pd.DataFrame()
            self.sweep_meta_data_df = pd.DataFrame()
            self.series_identifier = None

            self.logger.info("adding experiment")
            print("adding experiment")
            print(experiment_name)
            self.logger.info(experiment_name)
            database.add_experiment_to_experiment_table(experiment_name)

            group_name = None
            try:
                print("adding experiment", experiment_name)
                print(self.meta_data_assignment_list)
                print(self.meta_data_assigned_experiment_names)
                pos = self.meta_data_assigned_experiment_names.index(experiment_name)
                meta_data = self.meta_data_assignment_list[pos]
            except Exception as e:
                print(f"Fehler: {e}")
                print("adding ", experiment_name, " without meta data")
                '''experiment_label = 'default, all other parameters are none '''
                meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]


            ''' add meta data as the default data indicated with a -1'''
            print(meta_data)
            database.add_experiment_to_global_meta_data(-1, meta_data)

        if "Series" in node_type:
            #print(node_type) # node type is None for Series
            self.logger.info(self.series_identifier)
            # make empty new df
            try:
                if not self.sweep_data_df.empty:
                    self.logger.info("Non empty dataframe needs to be written to the database")
                    self.logger.info(self.sweep_data_df)
                    self.logger.info(self.sweep_meta_data_df)
                    database.add_sweep_df_to_database(experiment_name, self.series_identifier,self.sweep_data_df,self.sweep_meta_data_df)
                    self.sweep_data_df = pd.DataFrame()
                    self.sweep_meta_data_df = pd.DataFrame()
                else:
                    self.logger.info("data frame is empty as planned")
            except Exception as e:
                self.sweep_data_df = pd.DataFrame()
                self.sweep_meta_data_df = pd.DataFrame()

            sliced_pgf_tuple_data_frame = pgf_tuple_data_frame[pgf_tuple_data_frame.series_id == node_type]


            database.add_single_series_to_database(experiment_name, node_label, node_type)

            print(sliced_pgf_tuple_data_frame)
            database.create_series_specific_pgf_table(sliced_pgf_tuple_data_frame,
                                                      "pgf_table_" + experiment_name + "_" + node_type,
                                                      experiment_name, node_type)


            # update the series counter
            data_access_array[1]+=1
            # reset the sweep counter
            data_access_array[2] = 0
            # update series_identifier
            self.series_identifier = node_type


        if "Sweep" in node_type :
            self.logger.info(self.series_identifier)
            self.logger.info(node_type)
            self.write_sweep_data_into_df(bundle,data_access_array,metadata)

            #database.add_single_sweep_to_database(experiment_name, series_identifier, data_access_array[2]+1, metadata,
            #                                          data_array)
            data_access_array[2] += 1

        if "NoneType" in node_type:
            self.logger.error(
                "None Type Error in experiment file " + experiment_name + " detected. The file was skipped")
            return


        for i in range(len(node.children)):
            #    progress_callback
            self.single_file_into_db(index + [i], bundle, experiment_name, database, data_access_array , pgf_tuple_data_frame)

        if node_type == "Pulsed" and not self.sweep_data_df.empty:
            print("finiahws with non empty dataframe")
            database.add_sweep_df_to_database(experiment_name, self.series_identifier, self.sweep_data_df,
                                              self.sweep_meta_data_df)

    def single_abf_file_into_db(self,abf_bundle,database):
        # here should be changed the defalt by experimental label!
        print("single file into db" )
        print("adding to experiments", abf_bundle[1][0])
        database.add_experiment_to_experiment_table(abf_bundle[1][0])

        pos = self.meta_data_assigned_experiment_names.index(abf_bundle[1][0])
        meta_data = self.meta_data_assignment_list[pos]
        database.add_experiment_to_global_meta_data(-1 ,meta_data)

        print("we try to enter the abf file funciton in treeview manager")
        for series_count, sweep in enumerate(abf_bundle[0], start=1):
            database.add_single_series_to_database(
                abf_bundle[1][0], sweep[3], f"Series{str(series_count)}"
            )
            database.add_sweep_df_to_database(
                abf_bundle[1][0],
                f"Series{str(series_count)}",
                sweep[0],
                sweep[1],
                False,
            )

            pgf_table_name = "pgf_table_" + abf_bundle[1][0] + "_" + "Series" + str(series_count)
            database.create_series_specific_pgf_table(
                sweep[2].set_index("series_name").reset_index(),
                pgf_table_name,
                abf_bundle[1][0],
                f"Series{str(series_count)}",
            )

    def write_sweep_data_into_df(self,bundle,data_access_array,metadata):
        """

        @param bundle: bund le of the .dat file
        @param data_access_array:
        @param metadata: all metadata from series and sweeps, sweeps specific meta data is at pos [sweepnumber]
        @return:
        """
        data_array = bundle.data[data_access_array]

        # new for the test
        data_array_df = pd.DataFrame(
            {f'sweep_{str(data_access_array[2] + 1)}': data_array}
        )
        self.sweep_data_df = pd.concat([self.sweep_data_df, data_array_df], axis=1)
        self.logger.info(self.sweep_data_df.columns.tolist())


        child_node = metadata[0]
        child_node_ordered_dict = dict(child_node.get_fields())

        meta_data_df = pd.DataFrame.from_dict(
            data=child_node_ordered_dict,
            orient='index',
            columns=[f'sweep_{str(data_access_array[2] + 1)}'],
        )

        self.sweep_meta_data_df = pd.concat([self.sweep_meta_data_df, meta_data_df], axis=1)

    def cancel_button_clicked(self,dialog):
        '''
        Function to close a given dialog
        :param dialog: dialog to be closed
        :return: None
        __edited__ = dz, 290921
        __tested__ = FALSE
        '''
        dialog.close()

    """######################### Chapter B Functions to interact with created treeviews ############################"""

    def assign_meta_data_groups_from_list(self, tree, meta_data_group_assignment_list):
        ''' Goes through the final tree and will try the assign the assignments from the tuple list
        todo:  error handling for incomplete lists '''

        # extract all names (tuple position 0) and texts into a seperate list
        name_list = list(map(lambda x: x[0], meta_data_group_assignment_list))
        text_list = list(map(lambda x: x[1], meta_data_group_assignment_list))

        for ind in range(tree.topLevelItemCount()):
            top_level_item = tree.topLevelItem(ind)
            top_level_combo_box = tree.itemWidget(top_level_item, self.meta_data_group_column)

            try:
                pos = name_list.index(top_level_item.text(0))
                top_level_combo_box.setCurrentText(text_list[pos])
            except Exception as e:
                top_level_combo_box.setCurrentText("None")
                self.logger.error("Could not assign meta data group for " + top_level_item.text(0))

    def reinsert_button_clicked(self, item, experiment_tree, discarded_tree,specific_series=None):
        """ Function to reinsert a given item into the experiment tree via button clicked"""
        print("reinsert button clicked")
        self.tree_button_clicked(item, discarded_tree, experiment_tree,"reinsert",specific_series)

    def discard_button_clicked(self, item, experiment_tree, discarded_tree, specific_series=None):
        """ Function to discard a given item into the discarded tree via button clicked"""
        print("discard button clicked")
        self.tree_button_clicked(item, experiment_tree, discarded_tree,"discard",specific_series)

    def tree_button_clicked(self, item, experiment_tree,discarded_tree,function,specific_series):
        """function can be -reinsert- or -discard-"""

        print("tree button clicked")
        if item.parent():
            self.move_series_from_treeview_a_to_b(item, experiment_tree, discarded_tree, function,specific_series)

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
            self.move_experiment_from_treeview_a_to_b(item,experiment_tree,discarded_tree,function,specific_series)
            if function == "reinsert":
                self.database.database.execute(
                    f'update experiment_series set discarded = \'False\' where experiment_name = \'{item.text(0)}\';')
            else:
                self.database.database.execute(
                    f'update experiment_series set discarded = \'True\' where experiment_name = \'{item.text(0)}\';')

    def insert_meta_data_items_into_combo_box(self, combo_box):
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
    """####################################### Chapter C Helper Functions ########################################  """

    def open_bundle_of_file(self,file_name):
        return Bundle(file_name)

    def get_number_from_string(self,string):
        '''split something like Series1 into Series,1'''
        splitted_string = re.match(r"([a-z]+)([0-9]+)",string,re.I)
        res = splitted_string.groups()
        return int(res[1])

    # ToDo put this into dictionary instead of parameters for dynamic programming
    def read_series_specific_pgf_trace_into_df(self, index, bundle, data_list, series_count = 0,
                                               holding_potential = None, 
                                               series_name = None, 
                                               sweep_number =None, stim_channel = None, 
                                               series_number = None,
                                               children_amount = None,
                                               ):

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

        if node_type == "Channel":
            # Holding
            holding_potential = node.Holding
            stim_channel = node.LinkedChannel
            children_amount = node.children

        elif node_type == "Stimulation":
            series_name = node.EntryName
            sweep_number = node.NumberSweeps

        if node_type == "StimChannel":
            duration = node.Duration
            increment = node.DeltaVIncrement
            voltage = node.Voltage
            series_number = f"Series{str(series_count)}"

            data_list.append([series_name,
                              str(sweep_number),
                              node_type,
                              str(holding_potential),
                              str(duration),
                              str(increment),
                              str(voltage), 
                              str(stim_channel), 
                              str(series_number),
                              str(len(children_amount))])
            series_count = series_count

        try:
            for i in range(len(node.children)):
                if node_type == "Pgf":
                    print(i)
                    series_count = i + 1
                self.read_series_specific_pgf_trace_into_df(index+[i], 
                                                            bundle,
                                                            data_list, 
                                                            series_count,
                                                            holding_potential, 
                                                            series_name,
                                                            sweep_number, 
                                                            stim_channel, 
                                                            series_number,
                                                            children_amount,
                                                            )
        except Exception as e:
            print(f"Error in PGF-file generation: {e}")


        return pd.DataFrame(data_list,columns = ["series_name", "sweep_number","node_type", "holding_potential", "duration", "increment", "voltage", "selected_channel", "series_id", "children_amount"])


    def write_series_to_csv(self, frontend_style):
        """_summary_
        """
        #file_name = QFileDialog.getSaveFileName(self,'SaveFile')[0]
        index = self.tree_build_widget.selected_tree_view.currentIndex()
        tree_item_list = self.tree_build_widget.selected_tree_view.model().get_data_row(index, Qt.DisplayRole)
        file_name = tree_item_list[1][5]+ "_"+ tree_item_list[1][1] + "_" + tree_item_list[1][3] + "_data.csv"
        dlg = SaveDialog(f"Do you want to save the file: {file_name}", frontend_style)
        dlg.setWindowTitle("Save File")
        dlg.exec_()
        if tree_item_list[1][4] == "Series":
            q = f'select sweep_table_name from experiment_series where experiment_name = \'{tree_item_list[1][5]}\' and series_identifier = \'{tree_item_list[1][3]}\''
            table_name = self.database_handler.database.execute(q).fetchdf()
            table_name = table_name["sweep_table_name"].values[0]
            df = self.database_handler.database.execute(f'select * from {table_name}').fetchdf()
            df.to_csv(file_name)
        print("hello from the other side")


    """
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
    """

    """
    def make_table_specific_parents(self,sliced,q):
        \"""
        make treeview dataframe containing meta data label and experiment items
        they are table specific e.g. global_meta_data or experiment_series
        \"""

        df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier", "sql_req"])

        #
        combination_list = sliced["values"].values.tolist()
        for meta_data_values in combination_list:
            column = sliced["column"].values.tolist()[combination_list.index(meta_data_values)]
            if df.empty:
                for val in meta_data_values:
                    new_q = q + f' {column} = \'{val}\''
                    new_item_df = pd.DataFrame(
                        {"item_name": [val], "parent": "root", "type": "Label",  # [meta_data],
                         "level": [combination_list.index(meta_data_values)],
                         "identifier": ["root::" + val],
                         "sql_req":new_q})
                    df = pd.concat([df,new_item_df])
            else:
                for val in meta_data_values:
                    parents = df[df["level"]==combination_list.index(meta_data_values)-1]["identifier"].values.tolist()
                    sql = df[df["level"]==combination_list.index(meta_data_values)-1]["sql_req"].values.tolist()
                    for parent in parents:
                      new_query = sql[parents.index(parent)] + f' and {column} = \'{val}\''
                      print(val)
                      print(parent)
                      print(new_query)
                      new_item_df = pd.DataFrame(
                        {"item_name": [val], "parent": [parent], "type": "Label",  # [meta_data],
                         "level": [combination_list.index(meta_data_values)],
                         "identifier": [parent + "::" + val],
                         "sql_req":new_query})
                      df = pd.concat([df, new_item_df])


        id_list = df[df["level"]==df["level"].max()]["identifier"].values.tolist()
        sql_list = df[df["level"]==df["level"].max()]["sql_req"].values.tolist()
        df_with_sql = df
        df = df.drop(columns=['sql_req'])
        for id in id_list:
            print("id = ", id)
            print("sql: ", sql_list[id_list.index(id)])
            #if list(np.unique(meta_data_table["table"]))==['global_meta_data','experiment_series']
            parent_name_table = self.database_handler.database.execute(sql_list[id_list.index(id)] + ')').fetchdf()
            if not parent_name_table.empty:
                tmp_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
                tmp_df["item_name"] = parent_name_table["experiment_name"].values.tolist()
                tmp_df["parent"] = id
                tmp_df["type"] = "Experiment"
                tmp_df["level"] = df["level"].max() + 1
                exp_id = []
                for exp in parent_name_table["experiment_name"].values.tolist():
                    exp_id.append(id + "::" + exp)
                tmp_df["identifier"] = exp_id
                df = pd.concat([df, tmp_df])

        print("finished")
        print(df)
        for index, row in df_with_sql.iterrows():
            print(row["sql_req"])

        return df
    """

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
        for _ in range(int(duration * sampling_frequency)):
            if voltage != 0:
                sub_signal.append(voltage)
            else:
                sub_signal.append(holding_potential)
        return sub_signal

# from QCore
class DataReadFinishedSignal(QObject):
    # signal to be emitted after the data were written to the database successfully
    finished_signal = Signal()