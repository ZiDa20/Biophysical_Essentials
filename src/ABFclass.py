import pyabf
import numpy as np
import pandas as pd
import logging

#####################################################################################
#ABFReader class which should Read an ABF file and return a dictionary containing the data
#####################################################################################
import pyabf
import numpy as np
import pandas as pd
import logging

#####################################################################################
#ABFReader class which should Read an ABF file and return a dictionary containing the data
#####################################################################################

class AbfReader():
    """ Class to load ABF files from path, path string should be inserted to open 
    the abf file with pyabf
    """
    
    def __init__(self, abf_path:str):
        """ abf_path: str -> should be file to open """
        self.abf_path: str = abf_path
        self.initialize_logger()


        try:
            self.abf_path_id: list = self.abf_path.split("/")[-1].split("_")[:2]
            self.abf_path_id: str = "_".join(self.abf_path_id)

        except Exception as e:
            self.abt_path_id = None
            self.logger("ABF File is not correctly formated")
    

        self.abf = None
        self.abf_property_dictionary: dict = None

        
        if self.abf_path:
            try:
                self.load_abf()
            except Exception as e:
                print(f"this is the error: {e}")
        

        if self.abf:
            self.data_table, self.metadata_table = self.get_data_from_sweep()
            self.build_command_epoch_table()
            self.make_membrane_test()

    def initialize_logger(self):
        """ initalized the logger module and write the loger file to abf_file_loaging.log"""
        self.logger = logging.getLogger()
        file_handler = logging.FileHandler('../Logs/abf_file_loaging.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        #self.logger.setLevel(logging.error)


    def load_abf(self):
        """ Load the data from the Path and insert into abf object"""
        try:
            self.abf = pyabf.ABF(self.abf_path)
        except:
            self.logger.error("ABF file could not be loaded, Check path or File for potential corruption")
        
        
    def get_data_from_sweep(self):
        """ Extract the data sweeps as table and save it into pd.DataFrame
        """
        data_sweep = pd.DataFrame()
        meta_data_sweep = pd.DataFrame()
        metadata_index = ["dacUnits", 
                          "dataRate",
                          "dataPointCount",
                          "dataLengthSec",
                          "sweepNumber",
                          "sweepLabelY",
                          "sweepLabelX",
                          "sweepUnitsY",
                          "sweepUnitsX",
                          "adcNames",
                          "adcUnits",
                          "CSlow",
                          "YUnit",
                          "XStart",
                          "XInterval",
                          "DataPoints",
                          "Ymin",
                          "Ymax", 
                          "RecordingMode"]
        
        meta_data_sweep["Parameters"] = metadata_index

        columns = 1
        columns_list = []

        for sweep in self.abf.sweepList:
            self.abf.setSweep(sweep)
            sweep_meta_data = self.extract_metadata_parameters(self.abf)
            data = self.abf.sweepY
            time = self.abf.sweepX
            data_sweep[sweep] = data
            meta_data_sweep[sweep] = sweep_meta_data
            columns_list.append("sweep_" + str(columns))
            columns += 1
        data_sweep.index = time
        data_sweep.columns = columns_list
        print(data_sweep)
        data_sweep = data_sweep/1e12
        print(data_sweep)
        meta_data_sweep.columns = ["Parameter"] + columns_list
        meta_data_sweep = meta_data_sweep.set_index("Parameter")
    
        return data_sweep, meta_data_sweep


    def extract_metadata_parameters(self, abf_file):

        """ Extract the metadata from the abf file and return it as a list"""
        metadata_list = []
        
        metadata_list.append(abf_file.dacUnits[0])
        metadata_list.append(abf_file.dataRate)
        metadata_list.append(abf_file.dataPointCount)
        metadata_list.append(abf_file.dataLengthSec)
        metadata_list.append(abf_file.sweepCount)
        metadata_list.append(abf_file.sweepLabelY)
        metadata_list.append(abf_file.sweepLabelX)
        metadata_list.append(abf_file.sweepUnitsY)
        metadata_list.append(abf_file.sweepUnitsX)
        metadata_list.append(abf_file.adcNames[0])
        metadata_list.append(abf_file.adcUnits[0])
        metadata_list.append(1)
        metadata_list.append(abf_file.adcUnits[0][1])
        metadata_list.append(0)
        metadata_list.append(abf_file.dataSecPerPoint) # data rate
        metadata_list.append(abf_file.sweepPointCount) #
        metadata_list.append(np.min(abf_file.sweepY))
        metadata_list.append(np.max(abf_file.sweepY))

        metadata_list.append("3" if abf_file.adcUnits[0] == "pA" else "0")

        return metadata_list
            
    def build_command_epoch_table(self):

        """ retrieve the command epoch table for the analysis
        Epochs Table ramp is indicated as 2, step protocol as 1"""
        epochs_list = [] # epoch lists
        columns_list = ["series_name",
                    "sweep_number",
                    "node_type",
                    "holding_potential",
                    "duration",
                    "increment",
                    "voltage"
                    
        ]
       

        first, last = self.get_first_and_last_sweep()


        
        # append the list with the levels and fill the dataframe
        epochs_list.append([self.abf.protocol for i in range(len(self.abf._epochPerDacSection.fEpochInitLevel))])
        epochs_list.append([self.abf.sweepCount for i in range(len(self.abf._epochPerDacSection.fEpochInitLevel))])
        epochs_list.append(self.abf._epochPerDacSection.nEpochType)
        epochs_list.append([i/1000 for i in self.abf._epochPerDacSection.fEpochInitLevel])
        epochs_list.append([i/10000 for i in self.abf._epochPerDacSection.lEpochInitDuration])
        epochs_list.append([i/1000 for i in self.abf._epochPerDacSection.fEpochLevelInc])
        epochs_list.append([i/1000 for i in self.abf._epochPerDacSection.fEpochInitLevel])
        



        #epochs_list.append(self.abf._epochPerDacSection.nEpochType)
        self.epochs_dataframe = pd.DataFrame(epochs_list, index = columns_list)  
      
        
       
        self.epochs_dataframe.insert(loc = 0,
                                    column="col1",
                                    value = first 
                        )
        self.epochs_dataframe.insert(loc = len(self.epochs_dataframe.columns),
                                    column="col2",
                                    value = last 
                        )
      
        self.epochs_dataframe = self.epochs_dataframe.transpose()
        
            

    def get_first_and_last_sweep(self):
        """ Get the first and last sweep of the abf file"""

        series = self.abf.protocol
        sweep_number = self.abf.sweepCount
        first_potential = self.abf.sweepEpochs.levels[0]
        last_potential = self.abf.sweepEpochs.levels[-1]
        first_time = (self.abf.sweepEpochs.p2s[0] - self.abf.sweepEpochs.p1s[0])/10000
        last_time = (self.abf.sweepEpochs.p2s[-1] - self.abf.sweepEpochs.p1s[-1])/10000
    
        first_command = [series, sweep_number,0,first_potential, first_time, 0, first_potential]
        last_command = [series, sweep_number, 0, last_potential, last_time, 0, last_potential]
        return first_command, last_command




    def make_membrane_test(self):
        """ Dysfunctional for most recording, should record the membrane properties
        But not working for most of the recordings"""
        try:
            memtest = pyabf.tools.memtest.Memtest(self.abf)
            self.abf_property_dictionary["memtest"].append(memtest.CmStep.values)
        except Exception as e:
            self.logger.error("currently not working for the data")

    def get_data_table(self):
        """ Returns the data table as pd.DataFrame"""
        return self.data_table

    def get_metadata_table(self):
        """ Returns the metadata table as pd.DataFrame"""
        return self.metadata_table

    def get_command_epoch_table(self):
        """ Returns the command epoch table as pd.DataFrame"""
        return self.epochs_dataframe

    def get_memtest(self):
        """ Returns the memtest table as list"""
        if self.abf_property_dictionary:
            return self.abf_property_dictionary["memtest"]

    def get_experiment_name(self):
        if self.abf_path_id:
            return self.abf_path_id

    def get_series_name(self):
        return self.abf.protocol
        
        