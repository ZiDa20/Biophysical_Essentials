import sys
import os
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import heka_reader
from functools import partial
import csv

import logging
from QT_GUI.OfflineAnalysis.CustomWidget.add_new_meta_data_group_pop_up_handler import Add_New_Meta_Data_Group_Pop_Up_Handler
from time import sleep
from database.data_db import *
import pandas as pd
from ABFclass import AbfReader
from plot_widget_manager import PlotWidgetManager
from Offline_Analysis.tree_model_class import TreeModel


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

    def __init__(self,database=None, treebuild_widget =None):

        # it's the database handler
        self.database_handler = database

        # the promoted tree widget containing a tab widget with selected and discarded tree view
        self.tree_build_widget = treebuild_widget
        self.selected_tree_view_data_table = pd.DataFrame()
        self.discarded_tree_view_data_table = pd.DataFrame()

        # qradio button which can be checked or not
        self.show_sweeps_radio = None

        # list of meta data group names represented as strings
        self.selected_meta_data_list = None

        # frontend style can be set to show all popups in the correct theme and color
        self.frontend_style = None

        self.analysis_mode = 0
        self.series_count = 0

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
                    pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], bundle, [], None, None, None) # retrieve pgf data
                    self.series_count = 0
                    splitted_name = i.split(".") # retrieve the name
                    bundle_list.append((bundle, splitted_name[0], pgf_tuple_data_frame, ".dat")) 

                if isinstance(i,list): # check if single_dat file or ABF file packagge
                    for abf in i:
                        file_2 = directory_path + "/" + abf
                        abf_file = AbfReader(file_2)
                        data_file = abf_file.get_data_table()
                        meta_data = abf_file.get_metadata_table()
                        pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                        experiment_name = [abf_file.get_experiment_name(), "default", "None", "None", "None", "None", "None"]
                        series_name = abf_file.get_series_name()
                        abf_file_data.append((data_file, meta_data, pgf_tuple_data_frame, series_name, ".abf"))
                    
            except Exception as e:
                # @todo error handling
                print("Bundle file could not be read: " + str(i[0]) + " the error occured: " + str(e))
                self.logger.error("Bundle file could not be read: " + str(i[0]) + " the error occured: " + str(e))

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
                self.logger.error("The DAT file could not be written to the database: " + str(i[0]) + " the error occured: " + str(e))
                database.database.close() # we close the database connection and emit an error message
        

        for i in abf_files:
            print("running abf file and this i ")
            try:
                #increment = 100/max_value
                #progress_value = progress_value + increment
                self.single_abf_file_into_db(i, database)
                #progress_callback.emit((progress_value,i))
            except Exception as e:
                print(e)
                self.logger.error("The ABF file could not be written to the database: " + str(i[0]) + " the error occured: " + str(e))
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

        self.selected_model = TreeModel(selected_table_view_table)
        self.tree_build_widget.selected_tree_view.setModel(self.selected_model)

        if self.selected_model.header:
            for i in range(0, len(self.selected_model.header)):
                if i < len(self.selected_model.header) - 3:
                    self.tree_build_widget.selected_tree_view.setColumnHidden(i, False)
                else:
                    self.tree_build_widget.selected_tree_view.setColumnHidden(i, True)

        self.discarded_model = TreeModel(discarded_table_view_table, "discarded")
        self.tree_build_widget.discarded_tree_view.setModel(self.discarded_model)

        for i in range(0, len(self.discarded_model.header)):
            if i < len(self.discarded_model.header) - 3:
                self.tree_build_widget.discarded_tree_view.setColumnHidden(i, False)
            else:
                self.tree_build_widget.discarded_tree_view.setColumnHidden(i, True)

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

    def create_data_frame_for_tree_model(self, discarded_state: bool, show_sweeps: bool, series_name = None):
        """
        @param discarded_state: True or False, indicating whether discarded (True) or non discard elements should be loaded
        @return: df, filled filled with experiment and series data
        """

        df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])

        # print("loading experiment_labels", self.selected_meta_data_list)
        q = (
            f'select distinct experiment_name from experiment_series where discarded = {discarded_state} intersect (select experiment_name from global_meta_data where experiment_label = \'{self.selected_meta_data_list[0]}\')')
        parent_name_table = self.database_handler.database.execute(q).fetchdf()

        df["item_name"] = parent_name_table["experiment_name"].values.tolist()
        df["parent"] = "root"
        df["type"] = "Experiment"
        df["level"] = 0
        df["identifier"] = parent_name_table["experiment_name"].values.tolist()

        if series_name:
            q = (f'select * from experiment_series where discarded = {discarded_state}  and series_name = \'{series_name }\' and experiment_name in (select experiment_name from global_meta_data where experiment_label = \'{self.selected_meta_data_list[0]}\')')
        else:
            q = (f'select * from experiment_series where discarded = {discarded_state}  and experiment_name in (select experiment_name from global_meta_data where experiment_label = \'{self.selected_meta_data_list[0]}\')')
        series_table = self.database_handler.database.execute(q).fetchdf()
        series_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        series_df["item_name"] = series_table["series_name"].values.tolist()
        series_df["parent"] = series_table["experiment_name"].values.tolist()
        series_df["type"] = "Series"
        series_df["level"] = 1
        series_df["identifier"] = series_table["series_identifier"].values.tolist()

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

                parent = experiment_name[0] + "_" + identifier[0]

                sweep_df["parent"] = [parent] * len(sweep_table.columns)
                sweep_df["type"] = ["Sweep"] * len(sweep_table.columns)
                sweep_df["level"] = [2] * len(sweep_table.columns)
                sweep_df["identifier"] = sweep_table.columns

                print(sweep_df)
                all_sweeps_df = pd.concat([all_sweeps_df, sweep_df])

            return pd.concat([df, series_df, all_sweeps_df])
        else:
            print("result = ",  pd.concat([df, series_df]))
            return pd.concat([df, series_df])

    def create_series_specific_tree(self, series_name, plot_widget_manager : PlotWidgetManager):
        self.selected_tree_view_data_table = self.create_data_frame_for_tree_model( False, self.show_sweeps_radio.isChecked(), series_name)
        self.discarded_tree_view_data_table = self.create_data_frame_for_tree_model( True, self.show_sweeps_radio.isChecked(), series_name)

        selected_model = TreeModel(self.selected_tree_view_data_table)
        discarded_model = TreeModel(self.discarded_tree_view_data_table, "discarded")

        self.tree_build_widget.selected_tree_view.setModel(selected_model)
        self.tree_build_widget.discarded_tree_view.setModel(discarded_model)

        self.tree_build_widget.selected_tree_view.setColumnHidden(3, True)
        self.tree_build_widget.selected_tree_view.setColumnHidden(4, True)
        self.tree_build_widget.selected_tree_view.setColumnHidden(5, True)

        self.tree_build_widget.discarded_tree_view.setColumnHidden(3, True)
        self.tree_build_widget.discarded_tree_view.setColumnHidden(4, True)
        self.tree_build_widget.discarded_tree_view.setColumnHidden(5, True)

       
        try:
            self.tree_build_widget.selected_tree_view.clicked.disconnect()
            self.tree_build_widget.discarded_tree_view.clicked.disconnect()
        except Exception as e:
            print(e)

        self.tree_build_widget.selected_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, selected_model, plot_widget_manager, series_name))
        self.tree_build_widget.discarded_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, discarded_model, plot_widget_manager, series_name))

    def handle_tree_view_click(self, model, plot_widget_manager: PlotWidgetManager, series_name, index):

        data_pos = model.item_dict

        # ["experiment", "series", "remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]
        tree_item_list = model.get_data_row(index, Qt.DisplayRole)
        print("click", tree_item_list)
        print(data_pos)
        if tree_item_list[0] == "x":
            print("x clicked")
            print(series_name)
            if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
                # set the related series to discarded
                self.database_handler.database.execute(f'update experiment_series set discarded = True where '
                                                       f'experiment_name = \'{tree_item_list[1][data_pos["hidden3_parent"]]}\' '
                                                       f'and series_identifier = \'{tree_item_list[1][data_pos["hidden1_identifier"]]}\'')

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
            plot_widget_manager.table_view_series_clicked_load_from_database(tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]])

            plot_widget_manager.check_live_analysis_plot(tree_item_list[1][data_pos["Series"]],tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]],"series" )


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
            self.logger.error("Not able to open the database properly " + str(e))

    #progress_callback
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

            self.logger.info("processed" + node_type)

            metadata = node

            if "Pulsed" in node_type:
                parent = ""

            if "Group" in node_type:
                self.sweep_data_df = pd.DataFrame()
                self.sweep_meta_data_df = pd.DataFrame()
                self.series_identifier = None

                self.logger.info("adding experiment")
                self.logger.info(experiment_name)
                database.add_experiment_to_experiment_table(experiment_name)

                group_name = None
                try:
                    #print("adding experiment", experiment_name)
                    #print(self.meta_data_assignment_list)
                    #print(self.meta_data_assigned_experiment_names)
                    pos = self.meta_data_assigned_experiment_names.index(experiment_name)
                    meta_data = self.meta_data_assignment_list[pos]
                except Exception as e:
                    print(f"Fehler: {e}")
                    print("adding ", experiment_name, " without meta data")
                    '''experiment_label = 'default, all other parameters are none '''
                    meta_data = [experiment_name, "default", "None", "None", "None", "None", "None"]


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
        database.add_experiment_to_experiment_table(abf_bundle[1][0])
        database.add_experiment_to_global_meta_data(-1 ,abf_bundle[1])
        series_count = 1
        print("we try to enter the abf file funciton in treeview manager")
        for sweep in abf_bundle[0]:
            database.add_single_series_to_database(abf_bundle[1][0], sweep[3], "Series" + str(series_count))
            database.add_sweep_df_to_database(abf_bundle[1][0], "Series" + str(series_count), sweep[0], sweep[1], False)

            pgf_table_name = "pgf_table_" + abf_bundle[1][0] + "_" + "Series" + str(series_count)
            database.create_series_specific_pgf_table(sweep[2].set_index("series_name").reset_index(), pgf_table_name, abf_bundle[1][0], "Series" + str(series_count))
            series_count += 1


    def write_sweep_data_into_df(self,bundle,data_access_array,metadata):
        """

        @param bundle: bund le of the .dat file
        @param data_access_array:
        @param metadata: all metadata from series and sweeps, sweeps specific meta data is at pos [sweepnumber]
        @return:
        """
        data_array = bundle.data[data_access_array]

        # new for the test
        data_array_df = pd.DataFrame({'sweep_' + str(data_access_array[2] + 1): data_array})
        self.sweep_data_df = pd.concat([self.sweep_data_df, data_array_df], axis=1)
        self.logger.info(self.sweep_data_df.columns.tolist())


        child_node = metadata[0]
        child_node_ordered_dict = dict(child_node.get_fields())

        meta_data_df = pd.DataFrame.from_dict(data=child_node_ordered_dict, orient='index',
                                              columns=['sweep_' + str(data_access_array[2] + 1)])

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

    """
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

    """
    """
    def uncheck_entire_tree(self,tree):
        top_level_items = tree.topLevelItemCount()
        for i in range(0,top_level_items):
            parent_item = tree.topLevelItem(i)
            self.uncheck_parents_childs(parent_item)
            parent_item.setCheckState(1, Qt.Unchecked)

    """
    """
    def uncheck_parents_childs(self,parent):
        child_count = parent.childCount()
        for c in range(0,child_count):
            parent.child(c).setCheckState(1, Qt.Unchecked)

            if parent.child(c).childCount()>0:
                self.uncheck_parents_childs(parent.child(c))

    """



    """####################################### Chapter C Helper Functions ########################################  """

    def open_bundle_of_file(self,file_name):
        return heka_reader.Bundle(file_name)

    def get_number_from_string(self,string):
        '''split something like Series1 into Series,1'''
        splitted_string = re.match(r"([a-z]+)([0-9]+)",string,re.I)
        res = splitted_string.groups()
        return int(res[1])

    # ToDo put this into dictionary instead of parameters for dynamic programming
    def read_series_specific_pgf_trace_into_df(self, index, bundle, data_list, 
                                               holding_potential = None, 
                                               series_name = None, 
                                               sweep_number =None, stim_channel = None, 
                                               series_number = None,
                                               children_amount = None,
                                               count = 0):

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
            self.series_count += 1
            
        if node_type == "Channel":
            # Holding
            holding_potential = node.Holding
            stim_channel = node.LinkedChannel
            children_amount = node.children
            
        if node_type == "StimChannel":
            duration = node.Duration
            increment = node.DeltaVIncrement
            voltage = node.Voltage
            series_number = "Series" + str(self.series_count)

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

        try:
            for i in range(len(node.children)):
                self.read_series_specific_pgf_trace_into_df(index+[i], 
                                                            bundle,
                                                            data_list, 
                                                            holding_potential, 
                                                            series_name,
                                                            sweep_number, 
                                                            stim_channel, 
                                                            series_number,
                                                            children_amount,
                                                            count = count)
        except Exception as e:
            print(f"Error in PGF-file generation: {e}")


        return pd.DataFrame(data_list,columns = ["series_name", "sweep_number","node_type", "holding_potential", "duration", "increment", "voltage", "selected_channel", "series_id", "children_amount"])

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

# from QCore
class DataReadFinishedSignal(QObject):
    # signal to be emitted after the data were written to the database successfully
    finished_signal = Signal()