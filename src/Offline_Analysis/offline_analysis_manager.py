import os
from typing import TYPE_CHECKING, Optional
from PySide6.QtCore import *  # type: ignore
from Threading.Worker import Worker
from Offline_Analysis.Analysis_Functions.AnalysisFunctionRegistration import AnalysisFunctionRegistration
from database.data_db import DuckDBDatabaseHandler
from Backend.treeview_manager import TreeViewManager

if TYPE_CHECKING:
    import logging
    
    

class OfflineManager():
    '''manager class to perform all backend functions of module offline analysis '''

    def __init__(self):
        """ constructor of the Offline Analysis Manager Class
        """
        self.meta_path: Optional[str] = None
        self.dat_files: Optional[list] = None

        self._directory_path: Optional[str] = None
        # nodelist for the treeview
        self.directory_content_list: list = [['','','']]
        #list of filterelements and their parameters
        self.filter_list: list = []
        # list of series specific analysis functions and their coursor bounds
        self.series_specific_analysis_list: list = []
        # database object to setted by the main function
        self.database: Optional[DuckDBDatabaseHandler] = None
        self.analysis_id: Optional[int] = None

        self.tree_view_manager: Optional[TreeViewManager] = None
        self.bundle_liste: list = []
        self.abf_bundle_list: list = []
        self.dat_list: Optional[list] = None
        self.bundle_worker: Optional[Worker] = None
        self.dummy_meta_data_list: Optional[list] = None
        self.options_list_dummy: Optional[list] = None

    @property
    def directory_path(self):
        """_summary_: Getter from the Analysis Directory Path

        Returns:
            str: Directory Path
        """
        return self._directory_path

    @directory_path.setter
    def directory_path(self,val: str) -> None:
        """_summary_: Setter for the Analysis Directory Path

        Args:
            val (str): String of the Directory Path
        """
        self._directory_path = val

    def set_status_and_progress_bar(self,status, progress):
        self.statusbar = status
        self.progressbar = progress
        self.statusbar.setText("The Process is beeing set up ... ")

    def execute_single_series_analysis(self,series_name: str, progress_callback) -> bool:
        """
        Performs all selected analysis calculations for a specific series name: e.g.
        all analysis functions(min_current, mean_current, max_current) for a series called 'IV'.
        Gets  called from offline_analysis_widget_function start_offline_analysis_of_single_series
        @param series_name: name of the single series (e.g. IV) to be analyzed)
        @author dz/mz, 13.07.2022
        """

        # read analysis functions from database
        analysis_function_tuple = self.database.get_series_specific_analysis_functions(series_name)
        #print(analysis_function_tuple)
        print("analysis function tuple ", analysis_function_tuple)

        progress_value = 100/len(analysis_function_tuple)
        progress = 0

        for fn in analysis_function_tuple:
            progress += progress_value
            progress_callback.emit((progress, str(fn[0])))
            # get the correct class analysis object
            specific_analysis_class = AnalysisFunctionRegistration().get_registered_analysis_class(fn[0])()
            cursor_bounds = self.database.get_cursor_bounds_of_analysis_function(fn[1], series_name)

            # set up the series where the analysis should be applied and the database where the results will be stored
            # set the cursor bound ->
            specific_analysis_class.lower_bound = cursor_bounds[0][0]
            specific_analysis_class.upper_bound = cursor_bounds[0][1]
            specific_analysis_class.database = self.database
            specific_analysis_class.series_name = series_name
            specific_analysis_class.analysis_function_id = fn[1]

            # run the calculation which will be also written to the database
            specific_analysis_class.calculate_results()

        self.database.database.close()
        return True

    def get_database(self) -> DuckDBDatabaseHandler:
        """ retrieves the database object from the manager class """
        return self.database

    def read_data_from_experiment_directory(self,tree_view_manager, 
                                            meta_data_assignment_list: Optional[list[str]]=None):
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
        self.tree_view_manager = tree_view_manager

        # meta_data_option_list can be an empty list: in this case, the treeeview manager will provide default elements
        # if not empty, this list contains all options in the dropdown menu of each combo box
        # when reading a template, "none" might not be assigned - therefore it might be necessary to add this option first

        self.tree_view_manager.meta_data_option_list = []
        self.tree_view_manager.meta_data_assignment_list = meta_data_assignment_list

        data_list = self.package_list(self._directory_path)
        # create a threadpool
        self.threadpool = QThreadPool()
        self.threadpool.setExpiryTimeout(1000)
        threads = self.threadpool.globalInstance().maxThreadCount() # get the number of threads

        # start the threadpool running the bundle read in function
        if len(data_list) < threads: #
            data_list_final = list(self.chunks(data_list, len(data_list)))
            print(f"this is the data_list final: {data_list_final} ")
            for i,t in enumerate(data_list_final):
                # read
                self.run_bundle_function_in_thread(t)

        else:
            data_list_final = list(self.chunks(data_list, threads))
            for i,t in enumerate(data_list_final):
                self.run_bundle_function_in_thread(t)

        print("finished analysis using the database manager")
        self.bundle_worker.signals.finished.connect(self.run_database_threading)

        return self.tree_view_manager

    def run_bundle_function_in_thread(self,bundle_liste: list) -> None:
        """
        Runs the bundle function in a thread
        @param bundle_liste:
        @param tree:
        @param discarded_tree:
        author MZ, 13.07.2022
        """
        self.bundle_worker = Worker(self.tree_view_manager.qthread_bundle_reading,bundle_liste,self._directory_path)
        self.bundle_worker.signals.result.connect(self.bundle_to_instance_list, Qt.DirectConnection)
        self.threadpool.start(self.bundle_worker)

    def run_database_threading(self) -> None:
        """_summary_

        Args:
            bundle_liste (list): Collection of Bundle Files /dat files
            abf_list (list): list of packages ABF files based on date and experimental number
        """
        self.threadpool.clear()
        self.database.database.close()
        print("here we go into thte run database threading")
        self.worker = Worker(self.tree_view_manager.write_directory_into_database, self.bundle_liste, self.abf_bundle_list)
        self.worker.signals.progress.connect(self.progress_fn)
        #worker.signals.result.connect(self.set_database)
        self.worker.signals.finished.connect(self.tree_view_manager.update_treeview) # when done, update the treeview
        # signal to update progress bar
        self.threadpool.start(self.worker) # start the thread

    def bundle_to_instance_list(self, result: list):
        """Should append the created bundled list for abf and dat files
        to the instance list which can be accessed

        Args:
            result (event, callback): The bundled results from the indivdiual Qthreads
        """
        bundle_result, abf_result = result
        for i in bundle_result:
            self.bundle_liste.append(i)
        for i in abf_result:
            self.abf_bundle_list.append(i)

    def chunks(self, lst: list, n: int):
        """Should create a chunked list used for the Qthreads

        Args:
            lst (list): The list that should be chunked
            n (int): Pieces that should the list be chunked to

        Yields:
            generator: The chunked list of list as a generator
        """
        for i in range(0, len(lst), int(n)):
            yield lst[i:i + int(n)]

    def progress_fn(self,data) -> None:
        """Checks the progress in the Thread and shows off
        percentage in the ProgressBar

        Args:
            data (callback, tuple[float, str]): Tuple of current Experiment Name and Progress
        """
        self.progressbar.setValue(data[0])
        #self.statusbar.showMessage(f"Writing data to database: {data[1]}")
        self.statusbar.setText(f"Writing data to database: {data[1][1]}")


    def write_analysis_series_types_to_database(self,series_type_list: list) -> None:
        """
        write the analysis series types to the database.
        called by offline_analysis_widget -> built_analysis_specific_notebook
        @param series_type_list:
        @author dz, 13.07.2022

        """
        self.database.write_analysis_series_types_to_database(series_type_list,self.analysis_id)

    def write_analysis_function_to_database(self,function_selection: str,series_name: str) -> None:
        """ write the analysis function to the database

        args:
            function_selection type(string): name of the function
            series_name type(string): name of the series
        """
        self.database.write_analysis_function_to_database(function_selection,series_name)

    def write_coursor_bounds_to_database(self,left_coursor: float, right_coursor: float, series_name: str) -> None:
        """ write the cursor bounds to the database

        args:
            left_coursor type(float): left bound of the cursor
            right_coursor type(float): right bound of the cursor
            series_name type(string): name of the series

        """
        self.database.write_coursor_bounds_to_database(left_coursor, right_coursor, series_name)

    def read_trace_data_and_write_to_database(self,series_name: str) -> None:
        """ read the trace data from the directory and write it to the database

        args:
            series_name type(string): name of the series
        """
        self.database.read_trace_data_and_write_to_database(series_name,self.dat_files)

    # deprecated ?
    def calculate_single_series_results_and_write_to_database(self,series_name: str) -> None:
        """ calculate the single series results and write them to the database

        args:
            series_name type(string): name of the series
        """
        self.database.calculate_single_series_results_and_write_to_database(series_name)

    def read_series_type_specific_analysis_functions_from_database(self,series_name: str) -> list:
        '''function that will return a list of strings with analysis function names

        args:
            series_name type(string): name of the series
        returns:
            analysis_function_list type(list): list of strings with analysis function names

        '''
        return self.database.read_series_type_specific_analysis_functions_from_database(series_name)

    def package_list(self, dat_path: str) -> list:
        """_summary_: This packages the list of dat files and abf files into a list of list

        Args:
            dat_path (str): The path to the dat and abf files

        Returns:
            list: Holding the dat and abf files
        """
        abf_file_bundle = {} # list to bundle abf files
        if isinstance(dat_path, str):
            data_list = os.listdir(dat_path)
            dat_list = [i for i in data_list if ".dat" in i]
            experiment_names = [i.split(".")[0] for i in dat_list]
            abf_list = [i for i in data_list if ".abf" in i]
            # get the list of list for abf files
            for i in abf_list:
                if "abf" in i:
                    experiment_name = i.split("_")[:2]
                    experiment_name = "_".join(experiment_name)
                    experiment_names.append(experiment_name)

                    if experiment_name not in abf_file_bundle.keys():
                        abf_file_bundle[experiment_name] = []
                    abf_file_bundle[experiment_name].append(i)

        return list(abf_file_bundle.values()) + dat_list



