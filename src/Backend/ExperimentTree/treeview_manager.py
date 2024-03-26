#TreeView Manager class to handle actions for given tree view objects.
import itertools
from functools import partial
import numpy as np
import pandas as pd
import debugpy
from PySide6.QtCore import QObject, Signal, QThreadPool, Qt, QModelIndex, QSize
from PySide6.QtWidgets import QFileDialog
from PySide6.QtTest import QTest
from Backend.cancel_button_delegate import CancelButtonDelegate
from Backend.PlotHandler.plot_widget_manager import PlotWidgetManager
from Backend.DataReader.ABFclass import AbfReader
from Backend.DataReader.heka_reader import Bundle
from Backend.ExperimentTree.tree_model_class import TreeModel
import picologging
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
from Backend.DataReader.SegmentENUM import EnumSegmentTypes
from PySide6.QtWidgets import QApplication
from database.DatabaseHandler.SeriesTableWriter import SeriesTableWriter

#debugpy.breakpoint()
class TreeViewManager:
    """
    Manager class to handle actions for given tree view objects.
    Tree views are parts of the offline as well as the online analysis
    __author__: dz
    """

    def __init__(self,database=None, treebuild_widget =None, show_sweep_radio = None, specific_analysis_tab = None, frontend = None):

        # it's the database handler
        if database:
            self.database_handler = database
            self.offline_analysis_id = self.database_handler.analysis_id
        else:
            print("debug here")
        # the promoted tree widget containing a tab widget with selected and discarded tree view
        self.tree_build_widget = treebuild_widget
        self.selected_tree_view_data_table = pd.DataFrame()
        self.discarded_tree_view_data_table = pd.DataFrame()
        # qradio button which can be checked or not
        self.show_sweeps_radio = show_sweep_radio

        # list of meta data group names represented as strings
        self.selected_meta_data_list = None

        # frontend style can be set to show all popups in the correct theme and color
        self.frontend_style = frontend

        # specific analysis tab needed for the resize actions of the mdi area
        self.specific_analysis_tab = specific_analysis_tab

        self.threadpool = QThreadPool()

        self._node_list_STATE = []
        self._discardet_nodes_STATE = []
        self._pgf_info_STATE = []

        self.meta_data_group_column = None

        self.stimulation_count = 0
        self.channel_count = 0
        self.stim_channel_count = 0

        self._data_view_STATE = 0

        self.logger = picologging.getLogger(__name__)
        self.meta_data_assignment_list = None
        self.configure_default_signals()

        # this is a mapping dict that maps a potential problem causing experiment name to a new name that was accepted by the user
        self.experiment_name_mapping = {}
        # introduce logger

    """ ############################## Chapter A Create treeview functions ######################################### """

    def configure_default_signals(self):
        """Configure the Default Signals which are used for Thread Safe communication"""
        self.data_read_finished = DataReadFinishedSignal()
        self.tree_build_finished = DataReadFinishedSignal()
        self.experiment_tree_finished = DataReadFinishedSignal()

    def qthread_heka_bundle_reading(self,dat_files, directory_path, progress_callback):
        bundle_list = [] # list of tuples (bundle_data, bundle_name, pgf_file)
        for i in dat_files:
           if ".dat" in i:
                    print(i)
                    file = directory_path + "/" + i # the full path to the file
                    bundle = self.open_bundle_of_file(file) # open heka reader
                    pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], bundle, []) # retrieve pgf data
                    splitted_name = i.split(".") # retrieve the name
                    bundle_list.append((bundle, splitted_name[0], pgf_tuple_data_frame, ".dat"))
        return bundle_list

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

    def write_directory_into_database(self, dat_files, abf_files, progress_callback):
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
        max_value = len(self.meta_data_assigned_experiment_names)
    
    
        progress_value = 0
        increment = 100/max_value
        self.database_handler.open_connection()     
        ################################################################################################################
        for i in dat_files:
            # loop through the dat files and read them in
            print("this is the data file i ", i)
            try:
                progress_value = progress_value + increment
                print("running dat file and this i ", i)
                self.single_file_into_db([], i[0],  i[1], self.database_handler, [0, -1, 0, 0], i[2])
                progress_callback.emit((round(progress_value,2),i))
            except Exception as e:
                print(
                    f"The DAT file could not be written to the database: {str(i[0])} the error occured: {str(e)}"
                )
                self.logger.error(
                    f"The DAT file could not be written to the database: {str(i[0])} the error occured: {str(e)}"
                )
                try:
                     progress_callback.emit((round(progress_value,2),i))
                except Exception as es:
                    print(es)
                    self.database_handler.database.close() # we close the database connection and emit an error message


        for i in abf_files:
            print("running abf file and this i ", i)
            try:
                progress_value = progress_value + increment
                self.single_abf_file_into_db(i, self.database_handler)
                progress_callback.emit((round(progress_value,2),i))
            except Exception as e:
                print(e)
                self.logger.error(
                    f"The ABF file could not be written to the database: {str(i[0])} the error occured: {str(e)}"
                )
                self.database_handler.database.close() # we close the database connection and emit an error message

        # trial to see if the database opens correctly
        self.database_handler.database.close()
        return "database closed"

    def map_data_to_analysis_id(self, parent_name_table:list):
        """
        link the selected data to an unique offline analysis id: from this point, all db searches, discardings and reinsertions are based on the mapping tables
        """

        # list of experiment names
        for experiment in parent_name_table:
            self.database_handler.create_mapping_between_experiments_and_analysis_id(experiment)

        # series mapping is based on the previously generated epxeriment mapping table
        self.database_handler.create_mapping_between_series_and_analysis_id()

    def show_discarded_flag_dialog_trees(self,selected_tree_view,discarded_tree_view):
        """_summary_: creates the treeviews for the dialog to load discarded flagged items from previous analysis

        Args:
            selected_tree_view (_type_): _description_
            discarded_tree_view (_type_): _description_
        """


        selected_data = self.create_data_frame_for_tree_model(False, False, None) # no sweeps, no specific series
        discarded_data = self.create_data_frame_for_tree_model(True, False, None) # no sweeps, no specific series
        
        if discarded_data.empty:
            discarded_data = pd.DataFrame(columns = selected_data.columns)
            discarded_data.loc[0] = ["Empty", "root", "Experiment","0","Empty"]
        
        selected_model = TreeModel(selected_data)
        discarded_model = TreeModel(discarded_data, "discarded")
        
        selected_tree_view.setModel(selected_model)
        discarded_tree_view.setModel(discarded_model)
        
        #selected_tree_view.expandAll()
        #discarded_tree_view.expandAll()

        for m,v in zip([selected_model, discarded_model],[selected_tree_view,discarded_tree_view]):
            for i in range(len(m.header)):
                    if m.header[i] == "Series" or m.header[i] =="Experiment":
                        v.setColumnHidden(i, False)
                    else:
                        v.setColumnHidden(i, True)


    def update_treeviews(self, plot_widget_manager: PlotWidgetManager, series_name = None):
        """
        do all the frontend handling for treeviews that are managed by the given tree_view_manager
        @param tree_view_manager: treeview manager class object
        @return:
        @toDO split!!!!
        """

        # create two global tables that can be reused for further visualizations and store it within the related tree view manager
        # the selected and discarded data will be selected from the global table
        selected_table_view_table = self.create_data_frame_for_tree_model(False, self.show_sweeps_radio.isChecked(),series_name)
        discarded_table_view_table = self.create_data_frame_for_tree_model(True, self.show_sweeps_radio.isChecked(),series_name)

        # set the label below selected and discarded treeview
        for table,label_object in zip([selected_table_view_table, discarded_table_view_table],[self.tree_build_widget.descriptive_meta_data_label, self.tree_build_widget.discarded_meta_data_label]):
            unique_types = table["type"].unique()
            counts = [len(table[table["type"] == type]) for type in unique_types]
            labels = [f"{type}: {cnt}" for type, cnt in zip(unique_types, counts)]
            label = ", ".join(labels)
            label_object.setText(label)

        print("new table \n ", selected_table_view_table)

        # create the models for the selected and discarded tree

        self.selected_model = TreeModel(selected_table_view_table)
        self.discarded_model = TreeModel(discarded_table_view_table, "discarded")

        # check both column counts: if one of the trees is empty, make sure to adopt the size to the non empty one
        col_count_selected = len(selected_table_view_table["type"].unique())
        col_count_discarded = len(discarded_table_view_table["type"].unique())

        if col_count_discarded>col_count_selected:
            col_count= col_count_discarded
        else:
            col_count = col_count_selected

        # workaround .. works around okish -- forces the tree to change its with
        if self.specific_analysis_tab:
            self.update_mdi_areas(col_count)
        else:
            self.tree_build_widget.selected_tree_view.setMinimumWidth(350 + (col_count-2)*100)
            #self.tree_build_widget.selected_tree_view.setMaximumWidth(350 + (col_count-2)*100)
        
        # make the delete button
        delegate_delete = CancelButtonDelegate(self.tree_build_widget.selected_tree_view,
                                               True,
                                               col_count_selected,
                                               self.frontend_style.default_mode) 
        
        self.tree_build_widget.selected_tree_view.setItemDelegate(delegate_delete)
        self.tree_build_widget.selected_tree_view.setModel(self.selected_model)
        self.tree_build_widget.selected_tree_view.expandAll()

        
        delegate_reinsert = CancelButtonDelegate(self.tree_build_widget.discarded_tree_view,
                                                 False,
                                                 col_count_discarded,
                                                 self.frontend_style.default_mode)
        
        self.tree_build_widget.discarded_tree_view.setItemDelegate(delegate_reinsert)
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
            partial(self.handle_tree_view_click, self.selected_model, plot_widget_manager,series_name))
        
        self.tree_build_widget.discarded_tree_view.clicked.connect(
            partial(self.handle_tree_view_click, self.discarded_model, plot_widget_manager,series_name))

        self.selected_tree_view_data_table = selected_table_view_table
        self.discarded_tree_view_data_table = discarded_table_view_table

    def update_mdi_areas(self,col_count):
        self.specific_analysis_tab.subwindow.setMaximumSize(QSize(350 + (col_count-2)*100, 16777215))
        self.specific_analysis_tab.subwindow.resize(QSize(350 + (col_count-2)*100,  self.specific_analysis_tab.subwindow.height()))
        self.specific_analysis_tab.show_and_tile()

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
        """
        creates the series df needed for treeview visualization
        """
        
        if series_name:
            q = """select t2.renamed_series_name, t1.experiment_name, t1.series_identifier, t1.sweep_table_name
                    from experiment_series as t1
                        inner join (
                            select * from series_analysis_mapping 
                            where analysis_id = (?) and analysis_discarded = (?) )
                        as t2
                        on t1.experiment_name = t2.experiment_name and t1.series_identifier = t2.series_identifier
                        where t2.renamed_series_name = (?)"""

            series_table = self.database_handler.database.execute(q, (self.offline_analysis_id, discarded_state,series_name)).fetchdf()

        else:
             q = """select t2.renamed_series_name, t1.experiment_name, t1.series_identifier, t1.sweep_table_name
                    from experiment_series as t1
                        inner join (
                            select * from series_analysis_mapping 
                            where analysis_id = (?) and analysis_discarded = (?) )
                        as t2
                        on t1.experiment_name = t2.experiment_name and t1.series_identifier = t2.series_identifier"""
            
             series_table = self.database_handler.database.execute(q, (self.offline_analysis_id, discarded_state)).fetchdf()

        series_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        series_df["item_name"] = series_table["renamed_series_name"].values.tolist()
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

    def handle_tree_view_click(self, model, plot_widget_manager: PlotWidgetManager, series_name, index):
        """
        Handler function to handle treeview clicks in online and offline analysis mode.
        """
        data_pos = model.item_dict

        # ["experiment", "series", "remove", "hidden1_identifier", "hidden2_type", "hidden3_parent"]
        tree_item_list = model.get_data_row(index, Qt.DisplayRole)
        #print("click", tree_item_list)
        #print(data_pos)
        #print(tree_item_list)
        print("tree clicked")
        tree_item_list = list(tree_item_list)

        p  = tree_item_list[1][data_pos["hidden3_parent"]].split("::")
        tree_item_list[1][data_pos["hidden3_parent"]] = p[len(p)-1]

        i = tree_item_list[1][data_pos["hidden1_identifier"]].split("::")
        tree_item_list[1][data_pos["hidden1_identifier"]] = i[len(i)-1]

        # remove: move an experiment or series from selected to discarded tree and mark it in the database as discarded
        if tree_item_list[0] == "x":
            self.move_tree_view_item(tree_item_list, series_name, data_pos, plot_widget_manager, "True")
       
        # reinsert: move and experiment or series from selected to discarded tree and mark it in the database as discarded
        if tree_item_list[0] == "<-":
            self.move_tree_view_item(tree_item_list, series_name, data_pos, plot_widget_manager, "False")
    

        if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
            print("series clicked")
            #print(tree_item_list)
            plot_widget_manager.table_view_series_clicked_load_from_database(tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]])


            plot_widget_manager.check_live_analysis_plot(tree_item_list[1][data_pos["hidden3_parent"]],
                                                              tree_item_list[1][data_pos["hidden1_identifier"]])


        if tree_item_list[1][data_pos["hidden2_type"]] == "Sweep":
            print("sweep clicked")
            #print(tree_item_list)

            parent_data = model.get_parent_data(index)
            #print(parent_data)
            #print(parent_data[data_pos["hidden3_parent"]])
            #print(parent_data[data_pos["hidden1_identifier"]])
            #print(data_pos)
            #print(tree_item_list[1][data_pos["Sweep"]])
            plot_widget_manager.table_view_sweep_clicked_load_from_database(parent_data[data_pos["hidden3_parent"]],
                                                                            parent_data[data_pos["hidden1_identifier"]],
                                                                            tree_item_list[1][data_pos["Sweep"]])

            plot_widget_manager.check_live_analysis_plot(parent_data[data_pos["hidden3_parent"]],
                                tree_item_list[1][data_pos["hidden3_parent"]],
                                tree_item_list[1][data_pos["Sweep"]])



    def move_tree_view_item(self, tree_item_list, series_name, data_pos, plot_widget_manager:PlotWidgetManager, discarded_state:str):
        """
        Move a single series or an entire experiment:
             Remove     item(s) from selected to discarded treeview and set discarded_state	= True
             Reinsert   item(s) from discarded to selected treeview and set discarded = False        

        discarded_state ="True"/"False"
        """
        #print("x clicked")
        #print(series_name)

        if tree_item_list[1][data_pos["hidden2_type"]] == "Series":
            # set the related series to discarded
            query = f'update series_analysis_mapping set analysis_discarded = {discarded_state} where '\
                    f'analysis_id = {self.offline_analysis_id} '\
                    f'and experiment_name = \'{tree_item_list[1][data_pos["hidden3_parent"]]}\' ' \
                    f'and series_identifier = \'{tree_item_list[1][data_pos["hidden1_identifier"]]}\''
            #print(discard_query)
            self.database_handler.database.execute(query)

            self.update_treeviews(plot_widget_manager,series_name)

        if tree_item_list[1][data_pos["hidden2_type"]] == "Experiment":
            # set all series of the related series to discarded
            self.database_handler.database.execute(f'update series_analysis_mapping set analysis_discarded = {discarded_state} where '\
                                                    f'analysis_id = {self.offline_analysis_id} '\
                                                    f'and experiment_name = \'{tree_item_list[1][data_pos["Experiment"]]}\' ')
            
            self.update_treeviews(plot_widget_manager,series_name)

   
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
        q = f'select distinct experiment_name from series_analysis_mapping where analysis_discarded = {discarded_state} '

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

    def create_treeview_with_meta_data_parents(self, meta_data_table,series_name = None):

        """
        make labels according to the entries in the meta data table
        meta_data_table = pandas data frame with columns [table, column, values]
        """
        # Create an empty DataFrame with the necessary columns
        df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])

        # Define constants for table names
        GLOBAL_META_DATA_TABLE = "global_meta_data"
        EXPERIMENT_SERIES_TABLE = "series_analysis_mapping"
        SWEEP_META_DATA_TABLE = "sweep_meta_data"
        
        # lets assume pure frames first: 
        if meta_data_table["table_name"].unique().tolist() == [GLOBAL_META_DATA_TABLE, EXPERIMENT_SERIES_TABLE]:
            global_meta_data_query = f'select * from global_meta_data '\
                                        f'where experiment_name in '\
                                        f'(select experiment_name from experiment_analysis_mapping '\
                                        f'where analysis_id = {self.offline_analysis_id})'
            
            global_meta_data = self.database_handler.database.execute(global_meta_data_query).fetchdf()
            global_meta_data_condition_column = meta_data_table[meta_data_table["table_name"] == GLOBAL_META_DATA_TABLE]["condition_column"]
            global_meta_data["agg"] = global_meta_data[global_meta_data_condition_column].agg('::'.join, axis=1)
        

            series_meta_data_query = f'select * from series_analysis_mapping where analysis_id = {self.offline_analysis_id} and series_name == \'{series_name}\''
            series_meta_data = self.database_handler.database.execute(series_meta_data_query).fetchdf()
            
            merged_meta_data_df = pd.DataFrame(columns=["experiment_name", "agg"])
            
            # go through each experiment and check the series meta data
            for experiment, aggregate in zip(global_meta_data["experiment_name"].values.tolist(), global_meta_data["agg"].values.tolist()):
                tmp = series_meta_data[series_meta_data["experiment_name"] == experiment]
                experiment_series_meta_data = tmp["series_meta_data"].unique().tolist()
                for i in experiment_series_meta_data:
                    merged_meta_data_df = merged_meta_data_df.append({"experiment_name": experiment, "agg": aggregate + "::" + i}, ignore_index=True)
            
            global_meta_data = merged_meta_data_df

        else:

            if meta_data_table["table_name"].unique().tolist() == [GLOBAL_META_DATA_TABLE]:
                global_meta_data_query = f'select * from global_meta_data '\
                                        f'where experiment_name in '\
                                        f'(select experiment_name from experiment_analysis_mapping '\
                                        f'where analysis_id = {self.offline_analysis_id})'
            
            elif meta_data_table["table_name"].unique().tolist() == [EXPERIMENT_SERIES_TABLE]:
                # this will be always series specific !! 
                global_meta_data_query = f'select * from series_analysis_mapping where analysis_id = {self.offline_analysis_id} and series_name == \'{series_name}\''\
        


            global_meta_data = self.database_handler.database.execute(global_meta_data_query).fetchdf()
            
            global_meta_data["agg"] = global_meta_data[meta_data_table["condition_column"]].agg('::'.join, axis=1)
        
        global_meta_data["root"] = "root"
        global_meta_data["agg_experiment_names"] =global_meta_data[["root", "agg","experiment_name"]].agg('::'.join, axis=1)
            
        # go through all created meta data label combinations, e.g. [KO::Male, KO::Female, WT::Male, W::Female] and get the related experiment name
        for c in global_meta_data["agg"].unique():
            
            # add the label as parent
            new_item_df = pd.DataFrame( {"item_name": [c], "parent": "root", "type": "Label", "level": 0, "identifier": ["root::" + c]})
            df = pd.concat([df, new_item_df])


            identifier_list =  global_meta_data.loc[global_meta_data["agg"]==c,"agg_experiment_names"]
            experiment_names = global_meta_data.loc[global_meta_data["agg"]==c,"experiment_name"].values

            new_item_df = pd.DataFrame( {"item_name": experiment_names, "parent": ["root::" + c]*len(experiment_names),
            "type": ["Experiment"]*len(experiment_names), "level": [1]*len(experiment_names), "identifier": identifier_list})

            df = pd.concat([df, new_item_df])


        return df

    def add_experiments_series_sweeps_to_meta_data_label(self, meta_data_table, discarded_state, series_name = None):

        """
        creating the df for a treeview which is splitted by given meta data and holds sweeps too
        meta_data_table: Pandas DataFrame with columns: table_name, condition_column, conditions (list)
        """

        # get a dataframe with hierarchical strcutured meta data items and exoeriments
        # thsi dataframe will have 2 levels: meta data label a parent and the experiment names
        df = self.create_treeview_with_meta_data_parents(meta_data_table,series_name)
        series_level = df["level"].max() + 1

        experiments_only = df[df["type"]=="Experiment"]

        experiment_name = experiments_only["item_name"].values
        experiment_id =  experiments_only["identifier"].values
        #experiment_label = df[df["item_name"]].values

        # append series to the experiments
        for name,id  in zip(experiment_name,experiment_id) : # index

            #print("experiment = ", name)
            series_meta_data = None

            # if there was a selection of series meta data -- 
            if "series_analysis_mapping" in meta_data_table["table_name"].values.tolist():  
            #    # split at ::
                label = id.split("::")
                #'root::male::before::220315_01' -> before would be the series meta data
                series_meta_data = label[len(label)-2]

            df, series_table = self.add_series_to_treeview(df, name, id , discarded_state, series_name, series_level, series_meta_data)
           
            #print(series_table["experiment_name"].unique)
            
            # create sweeps
            if self.show_sweeps_radio.isChecked():
                dfs= self.add_sweeps_to_treeview(series_table) #, series_level, experiment_row["identifier"])
                if dfs:
                    dfs.append(df)
                    df = pd.concat(dfs)
        return df.sort_values(by=["level"])
     
    def add_series_to_treeview(self, df, experiment_name,experiment_id, discarded_state, series_name, series_level, series_meta_data=None):
        """
        function to query series for a givn experiment and to create unqiue identifiers which is required for the treeeview representation
        """

        # get all series linked with this experiment
        query = f'SELECT t1.*, t2.sweep_table_name FROM series_analysis_mapping as t1 JOIN experiment_series as t2 ON t1.experiment_name = t2.experiment_name AND t1.series_identifier = t2.series_identifier where t1.experiment_name = \'{experiment_name}\' and t1.analysis_discarded = {discarded_state} and t1.analysis_id = {self.offline_analysis_id}'

        if series_meta_data:
            query = query + f' and t1.series_meta_data = \'{series_meta_data}\' '

        # if specified, get only specific series names
        if series_name is not None:
            query = query + f' and t1.renamed_series_name = \'{series_name}\''

        # get the series table from db
        series_table = self.database_handler.database.execute(query).fetchdf()

        # if no series were found for this experiment, it will be removed from the treeview
        if series_table.empty:
            df = df[df.item_name != experiment_name]
            return df, series_table

        # if series were found they need be appended to the df
        series_df = pd.DataFrame(columns=["item_name", "parent", "type", "level", "identifier"])
        series_names = series_table["renamed_series_name"].values.tolist()
        series_df["item_name"] = series_names
        series_df["parent"] = [experiment_id]*len(series_names)
        series_df["type"] = ["Series"]*len(series_names)
        series_df["level"] = [series_level]*len(series_names)
        series_ids = [
            experiment_id + "::" + s for s in series_table["series_identifier"]
        ]
        series_df["identifier"] = series_ids
        series_table["identifier"] = series_ids

        df = pd.concat([df, series_df])

        return df, series_table


    def add_sweeps_to_treeview(self, series_table): #, series_level, identifier):

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

        print("adding sweeps")
        # Prepare a list to store the generated DataFrames
        dfs = []
        try:
            table_names = series_table["sweep_table_name"].values
            parent_names = series_table["identifier"].values
        except Exception as e:
            print(e)
            return []
        
        for s,sweep_parent in zip(table_names,parent_names):

            # Fetch the sweep table data in bulk
            sweep_table = self.database_handler.database.execute(f'select * from {s}').fetchdf()

            # Get column names and generate identifiers
            item_names = sweep_table.columns
            sweep_ids = [sweep_parent + "::" + c_name for c_name in item_names]

            # Create a sweep DataFrame using vectorized operations
            sweep_df = pd.DataFrame({
                "item_name": item_names,
                "parent": np.repeat(sweep_parent, len(item_names)),
                "type": np.repeat("Sweep", len(item_names)),
                "level": np.repeat(3, len(item_names)),
                "identifier": sweep_ids
            })

            # Append the sweep DataFrame to the list
            dfs.append(sweep_df)

        # Concatenate all the DataFrames in the list
        return  dfs


    def single_file_into_db(self,index, bundle, experiment_name, database,  data_access_array , pgf_tuple_data_frame=None):
        """Main Functions to write a single (.dat ?) file into the database. Called during multithreading ! 
        If the filename (==experimentname) was identified as corrupted, the mapped new name is used instead
        This function is executed recursively

        Args:
            index (_type_): _description_
            bundle (_type_): _description_
            experiment_name (_type_): _description_
            database (_type_): _description_
            data_access_array (_type_): _description_
            pgf_tuple_data_frame (_type_, optional): _description_. Defaults to None.
        """
  
        if database is None:
            database = self.database_handler

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

        self.logger.info(f"single_file_into_db: current node = {node_type}")

        metadata = node

        if "Pulsed" in node_type:
            parent = ""
            
        if "Amplifier" in node_type:
            print("yes")

        if "Group" in node_type:

            self.logger.info("single_file_into_db: " +  "experiment_name=" + experiment_name)
            self.sweep_data_df = pd.DataFrame()
            self.sweep_meta_data_df = pd.DataFrame()
            self.series_identifier = None

            if experiment_name in self.experiment_name_mapping.keys():
                self.logger.info(f"single_file_into_db: replaced the original experiment name {experiment_name} with the new one {self.experiment_name_mapping[experiment_name]}")    
                experiment_name = self.experiment_name_mapping[experiment_name]

            self.logger.info(F"single_file_into_db: adding experiment {experiment_name} to db")
            database.add_experiment_to_experiment_table(experiment_name)
            try:
                pos = self.meta_data_assigned_experiment_names.index(experiment_name)
                meta_data = self.meta_data_assignment_list[pos]
            except Exception as e:
                self.logger.error(F"single_file_into_db: meta data assignment failed: " + {e})
                self.logger.info("adding " + experiment_name + " without meta data")

                '''experiment_label = 'default, all other parameters are none '''
                meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]


            ''' add meta data as the default data indicated with a -1'''
            database.add_experiment_to_global_meta_data(-1, meta_data)

        if "Series" in node_type:
            # node type will become the new series identifier while current value in self.seriesidentfier is the previous series identifier 
            self.logger.info(F"single_file_into_db: adding series_identifier {node_type} of experiment {experiment_name} to db")
            
            series_table_writer = SeriesTableWriter(database.database, experiment_name, self.series_identifier)
            try:
                # sweeps are appended to the sweep data df as long as no new series name is detected
                # if a new series is detected and sweep_data_df is not empty, swepps that belong to the previous series are written to the database  
                # afterwird the sweep_data_df is reseted to an emtpy df  
                if not self.sweep_data_df.empty:   
                    self.logger.info(f"single_file_into_db: non empty sweep_data_df for series {self.series_identifier} needs to be written to the database")
                    
                    series_table_writer.add_sweep_df_to_database(self.sweep_data_df,self.sweep_meta_data_df)
                    self.sweep_data_df = pd.DataFrame()
                    self.sweep_meta_data_df = pd.DataFrame()
                    self.logger.info("single_file_into_db:  sweep_data_df reseted to empty df")
                else:
                    self.logger.info("single_file_into_db:  sweep_data_df was already, all good")

            except Exception as e:
                self.logger.error(F"single_file_into_db: error in series writing: " + {e})
                self.sweep_data_df = pd.DataFrame()
                self.sweep_meta_data_df = pd.DataFrame()

            sliced_pgf_tuple_data_frame = pgf_tuple_data_frame[pgf_tuple_data_frame.series_id == node_type]

            # adding the series to the database
            series_table_writer.add_single_series_to_database(node_label, node_type)
            
            self.logger.info(f"single_file_into_db:  added new series with experiment_name {experiment_name}, series_name = {node_label} and identifier {node_type} to db")

            #print(sliced_pgf_tuple_data_frame)
            series_table_writer.create_series_specific_pgf_table(sliced_pgf_tuple_data_frame,
                                                                 node_type
                                                )


            # update the series counter
            data_access_array[1]+=1
            # reset the sweep counter
            data_access_array[2] = 0
            # update series_identifier
            self.series_identifier = node_type

        if "Sweep" in node_type :
            self.logger.info("single_file_into_db:  sweep detected, will be added to sweep_dfdf")
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
            print("finishs with non empty dataframe")
            # copy from above .. smarter to have it here to avoid additional if condition in all the recursions
            if experiment_name in self.experiment_name_mapping.keys():
                self.logger.info(f"single_file_into_db: replaced the original experiment name {experiment_name} with the new one {self.experiment_name_mapping[experiment_name]}")    
                experiment_name = self.experiment_name_mapping[experiment_name]

            database.add_sweep_df_to_database(experiment_name, 
                                              self.series_identifier, 
                                              self.sweep_data_df,
                                              self.sweep_meta_data_df)

    def single_abf_file_into_db(self,abf_bundle,database):
        # here should be changed the defalt by experimental label!
        
        try:
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
        except Exception as e:
            print("error detected")

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
      
        child_node = metadata[0]
        child_node_ordered_dict = dict(child_node.get_fields())

        meta_data_df = pd.DataFrame.from_dict(
            data=child_node_ordered_dict,
            orient='index',
            columns=[f'sweep_{str(data_access_array[2] + 1)}'],
        )

        self.sweep_meta_data_df = pd.concat([self.sweep_meta_data_df, meta_data_df], axis=1)
        self.logger.info(f'added new sweep_{str(data_access_array[2] + 1)} to self.sweep_data_df')

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

    def click_top_level(self) -> None:
        """Clicks automatically the top-level item of the selected tree view after tree was ubild to show the plot"""
        index = self.tree_build_widget.selected_tree_view.model().index(0, 0, self.tree_build_widget.selected_tree_view.model().index(0,0, QModelIndex()))
        self.tree_build_widget.selected_tree_view.setCurrentIndex(index)
        rect = self.tree_build_widget.selected_tree_view.visualRect(index)
        QTest.mouseClick(self.tree_build_widget.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())

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
                                               sweep_number =None, 
                                               stim_channel = None,
                                               start_time = None,
                                               start_segment = None,
                                               series_number = None,
                                               children_amount = None,
                                               sine_amplitude = None,
                                               sine_cycle = None,
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
            stim_channel = node.DacChannel
            children_amount = node.children
            sine_amplitude = node.Sine_Amplitude
            sine_cycle = node.Sine_Cycle

        elif node_type == "Stimulation":
            series_name = node.EntryName
            sweep_number = node.NumberSweeps
            start_time = node.DataStartTime
            start_segment = node.DataStartSegment
            
        if node_type == "StimChannel":
            duration = node.Duration
            increment = node.DeltaVIncrement
            voltage = node.Voltage
            series_number = f"Series{str(series_count)}"
            segment_class = EnumSegmentTypes(node.Class.decode("ascii")).name
            if segment_class != "SINE":
                sine_amplitude = "None"
                sine_cycle = "None"
                

            data_list.append([series_name,
                              str(start_time),
                              str(start_segment),
                              segment_class,
                              str(sweep_number),
                              node_type,
                              str(holding_potential),
                              str(duration),
                              str(increment),
                              str(voltage),
                              str(stim_channel),
                              str(series_number),
                              str(len(children_amount)),
                              str(sine_cycle),
                              str(sine_amplitude)
                              ]
                              )
            series_count = series_count
            start_time = "None"
            start_segment = "None"

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
                                                            start_time,
                                                            start_segment,
                                                            series_number,
                                                            children_amount,
                                                            sine_amplitude,
                                                            sine_cycle
                                                            )
        except Exception as e:
            print(f"Error in PGF-file generation: {e}")


        return pd.DataFrame(data_list,columns = ["series_name","start_time","start_segment","segment_class",
                                                 "sweep_number","node_type", "holding_potential", "duration", 
                                                 "increment", "voltage", "selected_channel", "series_id", "children_amount",
                                                 "sine_amplitude","sine_cycle"])

    def write_experiment_to_csv(self,plot_widget_manager):
        """write the entire experiment of the currently selected and displayed series into a csv file
        """
        # let the user select the location where to store the csv file
        file, experiment_name, series_identifier = self.select_csv_location(True)
        # for the experiment - get all series identifiers
        series_identifier = self.database_handler.database.execute(f'SELECT series_identifier FROM experiment_series where experiment_name == \'{experiment_name}\' ').fetchdf()

        series_identifier = series_identifier["series_identifier"].values.tolist()
        if file[0]!="":

            for s_i in series_identifier:
                QApplication.processEvents()
                self.get_series_data_and_write_to_csv(plot_widget_manager,file,experiment_name,s_i)
                self.logger.info(f"write_experiment_to_csv: added series {s_i} to csv file")
    

    def write_series_to_csv(self,plot_widget_manager):
        """write the currently selected and displayed series into a csv file
        therefore, a dialog will be opened that allows the user to select the location
        """
        # let the user select the location where to store the csv file
        file, experiment_name, series_identifier = self.select_csv_location(False)
        # get the data for all sweeps for the selected series from the db and store it in the csv
        if file[0]!="":
            self.get_series_data_and_write_to_csv(plot_widget_manager,file,experiment_name,series_identifier)
        

    def get_series_data_and_write_to_csv(self, plot_widget_manager: PlotWidgetManager, file, experiment_name:str, series_identifier:str):
        """queries the data table from the database and writes it to a given csv file

        Args:
            plot_widget_manager (_type_): the plot widget manager to use fir the time extraction 
            file (_type_): the csv file to write to 
            experiment_name (_type_): the name of the experiment
            series_identifier (_type_): the name of the series that is currently being displayed
        """
        series_data = self.database_handler.get_sweep_table_for_specific_series(experiment_name, series_identifier)
       
        # get the meta data to correctly display y values of traces
        meta_data_df = self.database_handler.get_meta_data_table_of_specific_series(experiment_name, series_identifier)
        series_data["time"] = plot_widget_manager.get_time_from_meta_data(meta_data_df)
        
        series_data.index.name = series_identifier

        series_data.to_csv(file[0], index = True, mode='a')  

        print(series_data.head())
    
    def select_csv_location(self,experiment:bool):
        """open a qfiledialog and let the user choose its file location and file name too but suggest already the correct name

        Args:
            experiment (bool): True if an entire experiment will be written or false if only a single series will be written

        Returns:
            _type_: the file to write to, the experiment name and the series identifier of the currently selected and displayed series
        """
        #file_name = QFileDialog.getSaveFileName(self,'SaveFile')[0]
        index = self.tree_build_widget.selected_tree_view.currentIndex()
        tree_item_list = self.tree_build_widget.selected_tree_view.model().get_data_row(index, Qt.DisplayRole)

        if tree_item_list is None:
            self.logger.error("Please click the series you want to save first: No series in the treeview was clicked")
            CustomErrorDialog("Please click the series you want to save first", self.frontend_style)
            return "","",""
        
        if experiment:
            file_name = tree_item_list[1][5]+ "_data.csv"
        else:
            file_name = tree_item_list[1][5]+ "_"+ tree_item_list[1][1] + "_" + tree_item_list[1][3] + "_data.csv"


        file = QFileDialog().getSaveFileName(None, "Save File", file_name, ".csv")        


        x1 = tree_item_list[1][5] # experiment name
        x2 = tree_item_list[1][1] # series name
        x3 = tree_item_list[1][3] # series identifier
        return file,x1,x3
    
    def clear_tree(self):
        self.tree_build_widget.selected_tree_view.setModel(TreeModel(pd.DataFrame()))
        #self.tree_build_widget.selected_tree_view.reset()



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