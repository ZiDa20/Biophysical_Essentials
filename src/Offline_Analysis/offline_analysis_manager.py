import pandas as pd

import raw_analysis as ra
from online_analysis_manager import *
from data_db import DuckDBDatabaseHandler
from treeview_manager import *
from PySide6.QtCore import *  # type: ignore
from Worker import Worker

import sys

from src.Offline_Analysis.Analysis_Functions.MaxCurrent import *


class OfflineManager():
    '''manager class to perform all backend functions of module offline analysis '''

    def __init__(self, progress, statusbar):

        """ constructor of the manager class
        
        args:
            progress(QProgressBar): progress bar of the main window
            statusbar(QStatusBar): status bar of the main window
        """
        self.meta_path = None
        self.dat_files = None
        self.statusbar = statusbar
        self.progressbar = progress

        self._directory_path = None

        # nodelist for the treeview
        self.directory_content_list = [['','','']]

        #list of filterelements and their parameters
        self.filter_list = []

        # list of series specific analysis functions and their coursor bounds
        self.series_specific_analysis_list=[]

        # database object to setted by the main function
        self.database = None
        self.analysis_id = None

        self.tree_view_manager = None


    @property
    def directory_path(self):
        return self._directory_path

    @directory_path.setter
    def directory_path(self,val):
        self._directory_path = val

    def get_registered_analysis_class(self,analysis_function_name):
        mapping = {
            "max_current":MaxCurrent
        }
        return mapping.get(analysis_function_name,lambda: MaxCurrent)

    def execute_single_series_analysis_II(self,series_name):
        """
        Performs all selected analysis calculations for a specific series name: e.g. all analysis functions
        (min_current, mean_current, max_current) for a series called 'IV'
        :param series_name:
        :return:
        """

        # read analysis functions from database
        analysis_function_tuple = self.database.get_series_specific_analysis_functions(series_name)
        print(analysis_function_tuple)

        for fn in analysis_function_tuple:

            # get the correct class analysis object
            specific_analysis_class = self.get_registered_analysis_class(fn[0])

            cursor_bounds = self.database.get_cursor_bounds_of_analysis_function(fn[1], series_name)

            # set up the series where the analysis should be applied and the database where the results will be stored
            specific_analysis_class.series_name = series_name
            specific_analysis_class.database = self.database
            specific_analysis_class.lower_bound = cursor_bounds[0][0]
            specific_analysis_class.upper_bound = cursor_bounds[0][1]
            specific_analysis_class.analysis_function_id = fn[1]

            # run the calculation which will be also written to the database
            specific_analysis_class.calculate_results()

            #read the data from the database and create the specific result visualization
                # therefore add
            specific_analysis_class().visualize_results()

        return False #True

    def execute_single_series_analysis(self,series_name):
        """
        Analysis function for single series types (e.g. Block Pulse, IV, ....) in offline analysis mode .
        Therefore, sweep data traces will be load from the database, an analysis object will be created to calculate results and results will be written
        into the database.
        :param series_name:
        :return:
        :author: dz, 30.06.2022

        """

        #@todo give normalization as argument to the function
        series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(series_name)
        try:
            if series_specific_recording_mode == "Voltage Clamp":
                cslow_normalization = 1
            else:
                cslow_normalization = 0
        except Exception as e:
            print("Error in Excecute_Single_Series_Analysis")
            print(e)
            cslow_normalization = 0

        # get series specific time from database


        # get name of sweep tables
        sweep_table_names = self.database.get_sweep_table_names_for_offline_analysis(series_name)

        # holding value - voltage or current from e.g. 'IV', ...
        # @todo this only needed for specific analysis of rheobase
        increment = self.database.get_data_from_pgf_table(series_name, "increment", 1)
        holding = self.database.get_data_from_pgf_table(series_name, "holding", 0)

        print(sweep_table_names)

        # read analysis functions from database
        analysis_functions = self.database.get_series_specific_analysis_funtions(series_name)


        # calculate result for each single sweep data trace and write the result into the database
        for table_name in sweep_table_names:

            # dict
            entire_sweep_table = self.database.get_entire_sweep_table(table_name)
            time = self.database.get_time_in_ms_of_by_sweep_table_name(table_name)

            #if table_name == 'imon_signal_220315_02_Series2':
                #pd.DataFrame(entire_sweep_table).to_csv("debug_signal.csv")


            # error handling
            if entire_sweep_table is None:
                print(series_name)
                print("Error found in table " + table_name)


            for column in entire_sweep_table:

                data = entire_sweep_table.get(column)

                # @todo better way ? dict hast no order - thats why index doesn't work here
                # eg. sweep_1
                sweep_number = column.split("_")

                # if current clamp data .. data need to be rescaled first
                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(table_name,column)
                    data = np.interp(data, (data.min(), data.max()), (y_min, y_max))

                raw_analysis_class_object = ra.AnalysisRaw(time, data)
                raw_analysis_class_object._sweep = int(sweep_number[1])
                raw_analysis_class_object.increment = increment
                raw_analysis_class_object.holding = holding
                raw_analysis_class_object.table_name = table_name
                for a in analysis_functions:
                    # list of cursor bound tuples
                    cursor_bounds = self.database.get_cursor_bounds_of_analysis_function(a,series_name)

                    for c in cursor_bounds:
                        # negative bound values decode invalid/not selected bounds
                        if c[0] > 0.0  and c[1] > 0.0:

                            raw_analysis_class_object._lower_bounds = c[0]
                            raw_analysis_class_object._upper_bounds = c[1]

                            raw_analysis_class_object.construct_trace()
                            raw_analysis_class_object.slice_trace()

                            # @todo: how can this be done bether ?? more generic???
                            if analysis_functions == "Rheobase_Detection":
                                # get the holding value from the database and incrementation steps from database pgf table
                                self.database.get_pgf_holding_value(series_name)

                            res = raw_analysis_class_object.call_function_by_string_name(a)

                            if cslow_normalization:
                                cslow = self.database.get_cslow_value_for_sweep_table(table_name)

                                print(res)
                                print(cslow)
                                res = res/cslow
                                print("normalized")
                                print(res)

                            sweep_number = str(column).split('_')[1]
                            try:
                                self.database.write_result_to_database(c[2],table_name,sweep_number,res)
                            except Exception as e:
                                print(e)

        print("analysis finished")
        return True


    def get_database(self):
        """ retrieves the database object from the manager class """
        return self.database

    def read_data_from_experiment_directory(self,tree,discarded_tree,meta_data_option_list):
        ''' Whenever the user selects a directory, a treeview of this directory will be created and by that,
        the database entries will be generated. Primary key constraints will check whether the data are already in
        the database and avoid copies of already existing data 
        
        args:
            tree type(QTreeWidget): treeview of the directory
        returns:
            tree_view_manager type(TreeViewManager): treeview manager object
        '''

        # initialize a new database or connect to an existing one saved in global self.database variable
        # self.init_database() # better check fo connection at this point

        # create a new tree view manager class object and connect it to the database
        self.tree_view_manager = TreeViewManager(self.database)

        # meta_data_option_list can be an empty list: in this case, the treeeview manager will provide default elements
        # if not empty, this list contains all options in the dropdown menu of each combo box
        # when reading a template, "none" might not be assigned - therefore it might be necessary to add this option first
        if meta_data_option_list:
            try:
                meta_data_option_list.index("None")
            except:
                meta_data_option_list = ["None"] + meta_data_option_list

            self.tree_view_manager.meta_data_option_list = meta_data_option_list

        data_list = self.package_list(self._directory_path)

        # create the treeview with the 2 treeviews "tree" and "discarded tree" in 2 different tabs, 1 = database mode
        #self.tree_view_manager.create_treeview_from_directory(tree,discarded_tree, data_list, self._directory_path,1)
        # add this to the upper function 

        self.database.database.close()

        # added worker to the analysis
        self.threadpool = QThreadPool()
        self.threadpool.globalInstance().setMaxThreadCount(6)
        worker = Worker(self.tree_view_manager.write_directory_into_database, self.database, data_list, self._directory_path)

        #worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(partial(self.tree_view_manager.update_treeview,tree,discarded_tree)) # when done, update the treeview
        worker.signals.progress.connect(self.progress_fn) # signal to update progress bar
        self.threadpool.start(worker) # start the thread

        return self.tree_view_manager # return the treeview manager object


    def progress_fn(self,data):
        """ check the progress of the worker thread which contains the readed dat files
        args:
            data(int): progress of the worker thread
            
        """
        self.progressbar.setValue(data[0])
        self.statusbar.showMessage(f"Writing data to database: {data[1]}")



    def write_analysis_series_types_to_database(self,series_type_list):
        """ write the analysis series types to the database
        
        args:
            series_type_list type(list): list of series types """
        self.database.write_analysis_series_types_to_database(series_type_list,self.analysis_id)

    def write_recording_mode_to_analysis_series_table(self,recording_mode,series_name):
        """ write the recording mode to the database 
        
        args:
            recording_mode type(str): recording mode
            series_name type(str): series name 
        """
        self.database.write_recording_mode_to_analysis_series_table(recording_mode,series_name,self.analysis_id)

    def write_ms_spaced_time_array_to_analysis_series_table(self,time,series_name):
        """ write the millisecond spaced time array to the database 
        
        args:
            time type(np.array): millisecond spaced time array
            series_name type(str): series name
        """
        time_array = np.array(time)
        self.database.write_ms_spaced_time_array_to_analysis_series_table(time_array,series_name, self.analysis_id)

    def write_series_type_specific_experiment_and_sweep_information(self,data_list,series_name):
        '''fill database from series type specific treeview list, no duplicated insertation
        
        args:
            data_list type(list): list of tuples with the following structure:
            series_name type(string): name of the series
            '''
        self.database.fill_database_from_treeview_list(data_list,series_name)

    def write_analysis_function_to_database(self,function_selection,series_name):
        """ write the analysis function to the database 
        
        args:
            function_selection type(string): name of the function
            series_name type(string): name of the series
        """
        self.database.write_analysis_function_to_database(function_selection,series_name)

    def write_coursor_bounds_to_database(self,left_coursor, right_coursor, series_name):
        """ write the cursor bounds to the database 
        
        args:
            left_coursor type(float): left bound of the cursor
            right_coursor type(float): right bound of the cursor
            series_name type(string): name of the series
            
        """
        self.database.write_coursor_bounds_to_database(left_coursor, right_coursor, series_name)

    def read_trace_data_and_write_to_database(self,series_name):
        """ read the trace data from the directory and write it to the database 
        
        args:
            series_name type(string): name of the series
        """
        self.database.read_trace_data_and_write_to_database(series_name,self.dat_files)

    def calculate_single_series_results_and_write_to_database(self,series_name):
        """ calculate the single series results and write them to the database
        
        args:
            series_name type(string): name of the series
        """
        self.database.calculate_single_series_results_and_write_to_database(series_name)

    def read_series_type_specific_analysis_functions_from_database(self,series_name):
        '''function that will return a list of strings with analysis function names
        
        args:
            series_name type(string): name of the series
        returns:
            analysis_function_list type(list): list of strings with analysis function names
            
        '''
        return self.database.read_series_type_specific_analysis_functions_from_database(series_name)

    def ask_file(self, frame):
        """ ask the user to select a file 
        
        args:
            frame type(QWidget): the frame where the file dialog will be shown
        returns:
            metadata_files type(list): list of metadata files
        
        """
        frame.option_add("*foreground","black")
        metadata_files = filedialog.askopenfilename(master=frame)
        return metadata_files#
    
    def ask_directory(self, frame, treeview):
        """ ask the user to select a directory
        
        args:
            frame type(QWidget): the frame where the file dialog will be shown
            treeview type(QTreeView): the treeview that will be updated
        returns:
            directory_path type(string): the path to the directory
            dat_files type(list): list of dat files in the directory
            data_list type(list): list of tuples with the following structure:
            tree type(QTreeView): the treeview that will be updated
        """
        frame.option_add("*foreground","black")
        directory_path = filedialog.askdirectory(master=frame, initialdir=os.getcwd())
        data_list = self.package_list(directory_path)

        # DZ: to be able to reload, the list needs to be reset
        if len(self.directory_content_list)>1:
            self.directory_content_list = [['', '', '']]

        for i in data_list:
            tmp_list = []
            file = directory_path+"/"+i
            bundle = heka_reader.Bundle(file)
            tmp_list = OnlineAnalysisManager().update_data_structure([],bundle,treeview, tmp_list) # maybe it's good to end the list at series level


            for z in range(len(tmp_list)):

                if("Group" in tmp_list[z][0]):
                    tmp_list[z][0]="Group"+i
                    tmp_list[z][1]=i


                if "Pulsed" not in tmp_list[z][0]:
                    self.directory_content_list.append(tmp_list[z])

        tree = OnlineAnalysisManager().built_tree_from_list(treeview,self.directory_content_list,0)
        self.dat_files = directory_path
        return data_list, self.dat_files, tree

    def get_parent_pos(self,start_index,list):
        """ get the parent position of the current index
        
        args:
            start_index type(int): the current index
            list type(list): the list that the index is in
        returns:
            parent_pos type(int): the parent position of the current index
        """
        for d in range(start_index,-1,-1):
            print(list[d][0])
            if "Group" in list[d][0]:
                return d


    def get_series_specific_treeview(self,treeview,series_name):
        """ get the series specific treeview
        
        args:
            treeview type(QTreeView): the treeview that will be updated
            series_name type(string): the name of the series
        returns:
            treeview type(QTreeView): the treeview that will be updated
        """
        series_specific_treeview_list = [["","",""]]
        prvs_parent_pos = -1
        for d in self.directory_content_list:
            if d[1]==series_name:
                start_index = self.directory_content_list.index(d)

                # append parent
                parent_pos = self.get_parent_pos(start_index,self.directory_content_list)
                if parent_pos != prvs_parent_pos:
                    series_specific_treeview_list.append(self.directory_content_list[parent_pos])
                    prvs_parent_pos = parent_pos

                # append the childs
                series_elements = self.get_number_of_series_elements(start_index+1, self.directory_content_list) - start_index
                for z in range(0,series_elements+1):
                    lst_ps= start_index+z
                    series_specific_treeview_list.append(self.directory_content_list[lst_ps])

        try:
            return series_specific_treeview_list, OnlineAnalysisManager().built_tree_from_list(treeview,series_specific_treeview_list,0)
        except Exception as e:
            print(e.args)



    def get_available_series_names(self,file_content_list = None):
        """ get the available series names, by looping through all possible series names
        
        args:
            file_content_list type(list): the list of all the files in the directory
        return:
            series_names type(list): the list of all the series names
            
        """

        if not file_content_list:
            file_content_list=self.directory_content_list

        list_of_series = []
        for i in file_content_list:
            if "Series" in i[0]:
                print(i[0])
                print(i[1])
                if not i[1] in list_of_series:
                    list_of_series.append(i[1])

        print(list_of_series)
        return list_of_series




    def get_multiple_series_data(self,list_of_series,file_content_list=None):
        '''  A function to extract data traces of defined series (defined in list_of_series) .dat files (represented as file_content_list) in a selected directory.
         @input list_of_series: a list of one or more series names string representated
         @return data_list: list of triples [file_name, series_name, sweep, [data_array]]
         @author dz
         @TODO : How to deal with duplicates (e.g. multiple series blockpuls) '''

        if not file_content_list:
            file_content_list = self.directory_content_list

        data_list = [] #to be filled in this function and eventually returned

        for i in list_of_series: # loop through the selected series names (strings)

            for d in file_content_list: # loop through the list of nodes (groups,series,sweeps,...)
                ''' - loop through the list, stop whenever the searched series identifier was found'''
                if d[1]==i: # string comparisson
                   series_position = file_content_list.index(d)
                   # @TODO check for the last element (-1 return)
                   next_series_position = self.get_number_of_series_elements(series_position+1,file_content_list)

                   # get the group the series belongs to (in directory view this is the filename)
                   # go backward from the current series position and choose the first group that will be found
                   for z in range(series_position,-1,-1):

                       if "Group" in file_content_list[z][0]:

                         group_name =  file_content_list[z][1]
                         group_position = z

                         next_group_position = self.get_next_group_position(group_position+1,file_content_list)

                         # check the number of series in the intersection of this group ( one group = one specific .dat file)
                         if next_group_position > 0:
                            series_in_file = OnlineAnalysisManager().get_list_of_series_names(
                                file_content_list[group_position:next_group_position])
                            series_identifiers_in_file = OnlineAnalysisManager().get_list_of_series_identifiers(file_content_list[group_position:next_group_position])
                         else:
                             series_in_file = OnlineAnalysisManager().get_list_of_series_names(
                                 file_content_list[group_position:len(file_content_list)])
                             series_identifiers_in_file = OnlineAnalysisManager().get_list_of_series_identifiers(
                                 file_content_list[group_position:len(file_content_list)])

                         file = [self.dat_files + "/" + group_name]
                         appearance = series_in_file.count(i)
                         if appearance > 1:
                             series_indices = [s for s, x in enumerate(series_in_file) if x == i]
                             for s in series_indices:
                                 series_ident = series_identifiers_in_file[s]
                                 found_series = []
                                 found_series = [s for s, x in enumerate(data_list) if (x[0] == group_name and x[1]==i and x[2]==series_ident)]
                                 if not found_series:
                                     series_pos = s
                                     break
                         else:
                            series_pos = series_in_file.index(i)

                         # open the file and read the data
                         bundle = heka_reader.Bundle(file[0])

                         if next_series_position<0:
                             next_series_position = len(file_content_list)
                         end_val = (next_series_position-series_position-1)//3   # division with 3 because of strcuture: Sweep, Imon, Ileak, Sweep, ...


                         for sweep in range(0,end_val+1):
                             source_array = [0, series_pos, sweep, 0]  # - 1 needed here since Series 1 is at position 0
                             try:
                                data_list.append([group_name,i,series_identifiers_in_file[series_pos],bundle.data[source_array]])
                             except:
                                debug = 1


                         data_length = len(data_list[len(data_list)-1][3])
                         time = np.linspace(0, data_length - 1, data_length)
                         data_list.append([group_name,series_identifiers_in_file[series_pos],"Time",time])
                         break


        return data_list

    # @TODO use instead get_series_amount_of_list_elements(self,list,series_list_index):
    def get_number_of_series_elements(self,start_index,list):
        ''' helper function to return the number of list elements of a series
        @input:     start_index:    integer value where to start to iterate
                    list:           the list with the node series elements
        @return     if a successor series was found, the last index before successor will be returned otherwise -1,
                    right now you have subtract start index and found index manually
        '''
        for i in range(start_index,len(list)):
            if "Series" in list[i][0]:
                return i-1

        return -1

    def check_for_multiple_series_in_a_file(self,node_list,series_list):
        ''' From given series names list all files will be scanned for multiple appearences of one of the series specified in the series list.
            @input  node_list: list of triples
                    series_list: list of series names (strings) the user has selected
            @return True if a series was found multiple times, False if not'''

        for a in series_list:
            for b in node_list:
                if "Group" in b[0]:
                    tmp_group_pos = node_list.index(b)
                    next_group_pos = self.get_next_group_position(tmp_group_pos+1,node_list)
                    if next_group_pos >0:
                        sub_list = node_list[tmp_group_pos:next_group_pos]
                        series_names = OnlineAnalysisManager.get_list_of_series_names(sub_list)
                    else:
                        series_names = OnlineAnalysisManager.get_list_of_series_names(
                            node_list[tmp_group_pos:len(node_list)])
                    cnt = 0
                    for s in series_names:
                        if s == a:
                            cnt = cnt+1

                    if cnt > 1:
                        return True

        return False


    def get_next_group_position(self,start_index,list):
        ''' helper function to return the index of the next group in a given list
        @input:     start_index:    integer value where to start to iterate
                    list:           the list with the series, group and sweep elements
        @return     if a successor group was found, the last index before successor will be returned otherwise -1
        '''
        for i in range(start_index,len(list)):
            if "Group" in list[i][0]:
                return i

        return -1

    def package_list(self, dat_path):
        if  isinstance(dat_path, str):
            self.data_list = os.listdir(dat_path)
            self.data = [i for i in self.data_list if ".dat" in i]
            return self.data
