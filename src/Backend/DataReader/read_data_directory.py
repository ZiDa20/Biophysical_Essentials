    

from Backend.tokenmanager import InputDataTypes
from Backend.DataReader.heka_reader import Bundle
from Backend.DataReader.new_unbundled_reader import BundleFromUnbundled
from Backend.DataReader.ABFclass import AbfReader
from Backend.DataReader.SegmentENUM import EnumSegmentTypes
from Backend.reusable_general_functions import clean_label
import pandas as pd
import picologging
import debugpy
from copy import deepcopy
import re

class ReadDataDirectory(object):
    """
    ReadDataDirectory Class to compromise all the functions orchestrating multiple file reading

    Args:
        object (_type_): _description_
    """
    def __init__(self,database_handler):
        self.logger = picologging.getLogger(__name__)
        self.database_handler = database_handler
        # this is a mapping dict that maps a potential problem causing experiment 
        #name to a new name that was accepted by the user
        self.experiment_name_mapping = {}
        self.meta_data_assignment_list = None
        self.meta_data_assigned_experiment_names = None

    def qthread_heka_reading(self,data_type,input_files, directory_path, progress_callback):
        """ read the dat files in a separate thread that reads in through the directory
        adds the dat.files run through the heka reader to get the data file and pulse generator files

        args:
           dat_files type: list of strings - the dat files to be read
           directory_path type: string - the path to the directory where the dat files are located
           progress_callback type: function - the function to be called when the progress changes

        returns:
          bundle_list type: list of tuples - the list of bundles that were read
         @author: dz, 20240331
        """
        #debugpy.debug_this_thread()
        bundle_list = [] # list of tuples (bundle_data, bundle_name, pgf_file)
        for i in input_files:
           bundle_list = self.single_dat_file_handling(i,directory_path, data_type,bundle_list)
        return bundle_list,[]
    



    def single_dat_file_handling(self,file_name:str,directory_path:str, data_type:InputDataTypes,bundle_list:list)->list:
        """
        single_dat_file_handling Handles a single dat file, so far, the following types are covered:
        (1) bundle heka with one and more experiments per recording file
        (2) unbundle heka files with one experiment per recording file

        Args:
            file_name (str): _description_
            directory_path (str): _description_
            data_type (InputDataTypes): _description_
            bundle_list (list): _description_

        Returns:
            list: _description_
        """
        if InputDataTypes.HEKA_DATA_FILE_ENDING.value in file_name:
            #self.logger.info("qthread_heka_reading: Generating Bundle for:" + file_name)
            splitted_name = file_name.split(".") # retrieve the name
            file = directory_path + "/" + file_name # the full path to the file
            try:
                match data_type:
                    case InputDataTypes.BUNDLED_HEKA_DATA:
                        print("1")
                        bundle = Bundle(file) # open heka reader
                    case InputDataTypes.UNBUNDLED_HEKA_DATA:
                        print("2")
                        bundle = BundleFromUnbundled(directory_path + "/",splitted_name[0]).generate_bundle()
                    case _: 
                        #self.logger.error("Error in qthread_heka_reading")
                        bundle = None
                print("finished match")
                # check if bundle has more than one experiment: 
                group_records = len(bundle.pul.children)
                if group_records > 1: # and if yes - split them into multiple bundles for later multithreading
                    self.create_multiple_bundles_from_one_dat_file(bundle,file,bundle_list,splitted_name[0])
                else:
                    pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], bundle, []) # retrieve pgf data
                    data_access_array = [0,-1,0,0]
                    bundle_list.append((bundle, splitted_name[0], data_access_array,pgf_tuple_data_frame)) 
                print("finished try")
            except Exception as e:
                self.logger.error(
                f"Error in bundled HEKA file reading: {str(file)} the error occured: {str(e)}")
        return bundle_list
    
    def create_multiple_bundles_from_one_dat_file(self,bundle:Bundle,file:str,bundle_list:list,experiment_name)->list:
        """
       if more than one experiment per recording is detected - this will be splitted into different 
       bundles to allow for multithreading when reading and writing into database

        Args:
            bundle (Bundle): _description_
            file (str): _description_
            bundle_list (list): _description_
            experiment_name (_type_): _description_

        Returns:
            list: _description_
        """
        # 
        pgf_lower_limit = 0 # pgf StimChannels are just numbered from 1 - X for each exectued series
        group_records = len(bundle.pul.children)
        for cell_experiment in range(group_records):
            pul = deepcopy(bundle.pul) # make a deep copy to not override the original bundle
            pul.children = pul.children[cell_experiment:cell_experiment+1] # this will override the children

            series_cnt = len(pul.children[0].children)
            label = clean_label(pul.children[0].Label)# label might contain rexps that need to be replaced to ensure proper functioning

            pgf = deepcopy(bundle.pgf)
            pgf.children = pgf.children[pgf_lower_limit:pgf_lower_limit+ series_cnt] 
            pgf_lower_limit += series_cnt

            # make the fakebundle
            sub_bundle = Bundle(file,[(InputDataTypes.HEKA_PULSE_FILE_ENDING.value, pul),
                (InputDataTypes.HEKA_DATA_FILE_ENDING.value, bundle.data),
                (InputDataTypes.HEKA_STIMULATION_FILE_ENDING.value, pgf)])

            pgf_tuple_data_frame = self.read_series_specific_pgf_trace_into_df([], sub_bundle, []) # retrieve pgf data
            data_access_array = [cell_experiment,-1,0,0]
            bundle_list.append((sub_bundle, experiment_name+"_"+label, data_access_array,pgf_tuple_data_frame))#, InputDataTypes.BUNDLED_HEKA_FILE_ENDING)) 
        
        return bundle_list

    def qthread_abf_bundle_reading(self,abf_files, directory_path, progress_callback):
        try:
            abf_list = [] # list of tuples (bundle_data, bundle_name, pgf_file)
            for i in abf_files:
                abf_file_data = []
                if isinstance(i,list):
                            for abf in i:
                                #print(abf)
                                file_2 = directory_path + "/" + abf
                                abf_file = AbfReader(file_2)
                                data_file = abf_file.get_data_table()
                                meta_data = abf_file.get_metadata_table()
                                pgf_tuple_data_frame = abf_file.get_command_epoch_table()
                                experiment_name = [abf_file.get_experiment_name(), "None", "None", "None", "None", "None", "None", "None"]
                                series_name = abf_file.get_series_name()
                                abf_file_data.append((data_file, meta_data, pgf_tuple_data_frame, series_name, InputDataTypes.ABF_FILE_ENDING))
                if isinstance(i,list):
                    abf_list.append((abf_file_data, experiment_name))
            return [],abf_list
        except Exception as e:
            self.logger.error(f"Error in abf  file reading: {str(i[0])} the error occured: {str(e)}")

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
    
    def write_directory_into_database(self, dat_files, abf_files,  meta_data_assignment_list, progress_callback):
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
        self.meta_data_assignment_list = meta_data_assignment_list
        self.meta_data_assigned_experiment_names =  [i[0] for i in self.meta_data_assignment_list]
        ################################################################################################################
        #Progress Bar setup
        max_value = len(self.meta_data_assigned_experiment_names)
        progress_value = 0

        try:
            increment = 100/max_value
        except Exception as e:
            print("no increment error")
            increment = 100

        self.database_handler.open_connection()     
        ################################################################################################################
        for i in dat_files:
            # loop through the dat files and read them in
            self.logger.info(f"write_directory_into_database: this is the data file i {i}")
            try:
                progress_value = progress_value + increment
                #debugpy.debug_this_thread()
                self.single_file_into_db([], i[0],  i[1], self.database_handler,i[2],i[3])
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
                    self.logger.error(es)
                    self.database_handler.database.close() # we close the database connection and emit an error message


        for i in abf_files:
            #print("running abf file and this i ", i)
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


    def  regexp_check(self,file_name):
        """
        Check if the file name contains disallowed characters: whitespace, dashes, hyphens, and hashtags.
        
        Args:
        file_name (str): The file name to be checked.
        
        Returns:
        bool: True if the file name contains disallowed characters, False otherwise.
        """
        # Regular expression pattern to check for disallowed characters
        pattern = r'[ \-#]'
        
        # Search for disallowed characters in the file name
        
        print(file_name)
        if re.search(pattern, file_name):
            # Replace disallowed characters with underscores
            print("regexp in file name detected")
            new_file_name = re.sub(pattern, '_', file_name)
            print("renamed to:")
            print(new_file_name)
            return  new_file_name
        else:
            # If no match is found, return False
            print("regexp not detected")
            return file_name


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

        experiment_name =  self.regexp_check(experiment_name)

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
                self.logger.error(F"single_file_into_db: meta data assignment failed: {e}")
                self.logger.info("adding " + experiment_name + " without meta data")

                '''experiment_label = 'default, all other parameters are none '''
                meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]


            ''' add meta data as the default data indicated with a -1'''
            database.add_experiment_to_global_meta_data(-1, meta_data)

        if "Series" in node_type:
            # node type will become the new series identifier while current value in self.seriesidentfier is the previous series identifier 
            self.logger.info(F"single_file_into_db: adding series_identifier {node_type} of experiment {experiment_name} to db")
            try:
                # sweeps are appended to the sweep data df as long as no new series name is detected
                # if a new series is detected and sweep_data_df is not empty, swepps that belong to the previous series are written to the database  
                # afterwird the sweep_data_df is reseted to an emtpy df  
                if not self.sweep_data_df.empty:   
                    self.logger.info(f"single_file_into_db: non empty sweep_data_df for series {self.series_identifier} needs to be written to the database")
                    #self.logger.info(self.sweep_data_df)
                    #self.logger.info(self.sweep_meta_data_df)
                    database.add_sweep_df_to_database(experiment_name, self.series_identifier,self.sweep_data_df,self.sweep_meta_data_df)
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
            database.add_single_series_to_database(experiment_name, node_label, node_type)
            self.logger.info(f"single_file_into_db:  added new series with experiment_name {experiment_name}, series_name = {node_label} and identifier {node_type} to db")
            #print(sliced_pgf_tuple_data_frame)
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
            try:
                self.logger.info("single_file_into_db:  sweep detected, will be added to sweep_dfdf")
                self.write_sweep_data_into_df(bundle,data_access_array,metadata)
                data_access_array[2] += 1
            except Exception as e:
                self.logger.error("Error in Sweep Read/Writing detected" + str(e))
        if "NoneType" in node_type:
            self.logger.error(
                "None Type Error in experiment file " + experiment_name + " detected. The file was skipped")
            return


        for i in range(len(node.children)):
            self.single_file_into_db(index + [i], bundle, experiment_name, database, data_access_array , pgf_tuple_data_frame)

        if node_type == "Pulsed" and not self.sweep_data_df.empty:
            # copy from above .. smarter to have it here to avoid additional if condition in all the recursions
            if experiment_name in self.experiment_name_mapping.keys():
                self.logger.info(f"single_file_into_db: replaced the original experiment name {experiment_name} with the new one {self.experiment_name_mapping[experiment_name]}")    
                experiment_name = self.experiment_name_mapping[experiment_name]

            database.add_sweep_df_to_database(experiment_name, self.series_identifier, self.sweep_data_df,
                                              self.sweep_meta_data_df)
            
    def single_abf_file_into_db(self,abf_bundle,database):
        # here should be changed the defalt by experimental label!
        try:
            self.logger.info("single file into db" )
            #self.logger.info("adding to experiments"+abf_bundle[1][0])
            database.add_experiment_to_experiment_table(abf_bundle[1][0])

            pos = self.meta_data_assigned_experiment_names.index(abf_bundle[1][0])
            meta_data = self.meta_data_assignment_list[pos]
            database.add_experiment_to_global_meta_data(-1 ,meta_data)

            self.logger.info("entering the abf file funciton in treeview manager")
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
           self.logger.error("single_abf_file_into_db: error detected")

    def write_sweep_data_into_df(self,bundle,data_access_array,metadata):
        """

        @param bundle: bundle of the .dat file
        @param data_access_array:
        @param metadata: all metadata from series and sweeps, sweeps specific meta data is at pos [sweepnumber]
        @return:
        """
        try:
            data_array = bundle.data[data_access_array]
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
        except Exception as e:
            self.logger.error("Error in function write_sweep_data_into_df" + str(e))