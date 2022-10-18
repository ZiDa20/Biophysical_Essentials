import pandas as pd

import raw_analysis as ra
from online_analysis_manager import *
from data_db import DuckDBDatabaseHandler
from treeview_manager import *
from PySide6.QtCore import *  # type: ignore
from Worker import Worker

import sys
import os
sys.path.append(os.path.dirname(os.getcwd()) + "/src/Offline_Analysis/Analysis_Functions")#/Function_Templates")
from AnalysisFunctionRegistration import *
from itertools import zip_longest
#from src.Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import *

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
        self.bundle_liste = []


    @property
    def directory_path(self):
        return self._directory_path

    @directory_path.setter
    def directory_path(self,val):
        self._directory_path = val

    def execute_single_series_analysis(self,series_name, progress_callback):
        """
        Performs all selected analysis calculations for a specific series name: e.g. all analysis functions
        (min_current, mean_current, max_current) for a series called 'IV'.
        Gets  called from offline_analysis_widget_function start_offline_analysis_of_single_series
        @param series_name: name of the single series (e.g. IV) to be analyzed)
        @author dz, 13.07.2022
        """

        # read analysis functions from database
        analysis_function_tuple = self.database.get_series_specific_analysis_functions(series_name)
        #print(analysis_function_tuple)
        progress_value = 100/len(analysis_function_tuple)
        progress = 0

        for fn in analysis_function_tuple:

            progress += progress_value
            progress_callback.emit((progress, str(fn[0])))
            # get the correct class analysis object
            specific_analysis_class = AnalysisFunctionRegistration().get_registered_analysis_class(fn[0])

            cursor_bounds = self.database.get_cursor_bounds_of_analysis_function(fn[1], series_name)

            # set up the series where the analysis should be applied and the database where the results will be stored
            specific_analysis_class.series_name = series_name
            specific_analysis_class.database = self.database
            specific_analysis_class.lower_bound = cursor_bounds[0][0]
            specific_analysis_class.upper_bound = cursor_bounds[0][1]
            specific_analysis_class.analysis_function_id = fn[1]

            # run the calculation which will be also written to the database
            specific_analysis_class.calculate_results()

        self.database.database.close()
        return True

    def get_database(self):
        """ retrieves the database object from the manager class """
        return self.database

    def read_data_from_experiment_directory(self,tree,discarded_tree,meta_data_option_list, meta_data_assignment_list=None):
        """
        Whenever the user selects a directory, a treeview of this directory will be created and by that,
        the database entries will be generated. Primary key constraints will check whether the data are already in
        the database and avoid copies of already existing data
        @param tree:
        @param discarded_tree:
        @param meta_data_option_list:
        @param meta_data_assignment_list:
        @author dz, 13.07.2022
        """

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
            self.tree_view_manager.meta_data_assignment_list = meta_data_assignment_list

        data_list = self.package_list(self._directory_path)

        # create a threadpool
        self.threadpool = QThreadPool()
        self.threadpool.setExpiryTimeout(1000)
        threads = self.threadpool.globalInstance().maxThreadCount() # get the number of threads

        # start the threadpool running the bundle read in function
        if len(data_list) < threads: # 
            data_list_final = list(self.chunks(data_list, threads/2))
            for i,t in enumerate(data_list_final): 
                # read
                bundle_worker = self.run_bundle_function_in_thread(t)

        else:
            data_list_final = list(self.chunks(data_list, threads-1))
            for i,t in enumerate(data_list_final):
                bundle_worker = self.run_bundle_function_in_thread(t)

        bundle_worker.signals.finished.connect(
            partial(self.run_database_threading, self.bundle_liste, tree, discarded_tree))

        return self.tree_view_manager

        #return bundle_worker # self.tree_view_manager # return the treeview manager object


    def run_bundle_function_in_thread(self,bundle_liste):
        """
        Runs the bundle function in a thread
        @param bundle_liste:
        @param tree:
        @param discarded_tree:
        author MZ, 13.07.2022
        """
        bundle_worker = Worker(self.tree_view_manager.qthread_bundle_reading,bundle_liste,self._directory_path)
        bundle_worker.signals.result.connect(self.show_bundle_result,Qt.DirectConnection)
        self.threadpool.start(bundle_worker)
        return bundle_worker
        

    def run_database_threading(self, bundle_liste, tree, discarded_tree):
        
        self.threadpool.clear()
        self.database.database.close()
        worker = Worker(self.tree_view_manager.write_directory_into_database, self.database, bundle_liste)
        #worker.signals.progress.connect(self.progress_fn)
        #worker.signals.result.connect(self.set_database)
        worker.signals.finished.connect(partial(self.tree_view_manager.update_treeview,tree,discarded_tree)) # when done, update the treeview
         # signal to update progress bar
        self.threadpool.start(worker) # start the thread


    def show_bundle_result(self, result):
        for i in result:
            self.bundle_liste.append(i)

    """
    def set_database(self, result):
        print(result)
    """

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), int(n)):
            yield lst[i:i + int(n)]

    def progress_fn(self,data):
        """ check the progress of the worker thread which contains the readed dat files
        args:
            data(int): progress of the worker thread
            
        """
        self.progressbar.setValue(data[0])
        self.statusbar.showMessage(f"Writing data to database: {data[1]}")

    def write_analysis_series_types_to_database(self,series_type_list):
        """
        write the analysis series types to the database.
        called by offline_analysis_widget -> built_analysis_specific_notebook
        @param series_type_list:
        @author dz, 13.07.2022

        """
        self.database.write_analysis_series_types_to_database(series_type_list,self.analysis_id)

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

    # deprecated ?
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

    def package_list(self, dat_path):
        """
        Makes a list of all .dat files in tje specified directory
        @param dat_path:
        @author dz, 13.07.2022
        """
        if isinstance(dat_path, str):
            self.data_list = os.listdir(dat_path)
            self.data = [i for i in self.data_list if ".dat" in i]
            return self.data
