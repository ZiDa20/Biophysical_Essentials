import pyabf
import numpy as np
import pandas as pd
from loggers.abf_logger import abf_logger

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
        self.epochs_dataframe = None
        self.logger = abf_logger
        self.metadata_table = None
        self.data_table = None
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
                print("abf loaded")
            except Exception as e:
                print(f"this is the error: {e}")


        if self.abf:
            self.data_table, self.metadata_table = self.get_data_from_sweep()
            self.build_command_epoch_table()
            self.make_membrane_test()


    def load_abf(self):
        """ Load the data from the Path and insert into abf object"""

        self.abf = pyabf.ABF(self.abf_path)

    def get_data_from_sweep(self):
        """
        Extract the data sweeps as table and save it into pd.DataFrame
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
        columns_list = []

        # loop through each individual swee and extracts the raw data
        # as well as metadata
        for columns, sweep in enumerate(self.abf.sweepList, start=1):
            self.abf.setSweep(sweep)
            sweep_meta_data = self.extract_metadata_parameters(self.abf)
            data = self.abf.sweepY
            time = self.abf.sweepX
            data_sweep[sweep] = data
            meta_data_sweep[sweep] = sweep_meta_data
            columns_list.append(f"sweep_{str(columns)}")
        # construction of the pd.DataFrame that can be inserted into the DuckDB databse
        data_sweep.index = time
        data_sweep.columns = columns_list
        data_sweep = data_sweep/1e12
        meta_data_sweep.columns = ["Parameter"] + columns_list
        meta_data_sweep = meta_data_sweep.set_index("Parameter")
        return data_sweep, meta_data_sweep

    def extract_metadata_parameters(self, abf_file):
        """_summary_

        Args:
            abf_file (_type_): _description_

        Returns:
            _type_: _description_
        """
        metadata_list = [
            abf_file.dacUnits[0],
            abf_file.dataRate,
            abf_file.dataPointCount,
            abf_file.dataLengthSec,
            abf_file.sweepCount,
            abf_file.sweepLabelY,
            abf_file.sweepLabelX,
            abf_file.sweepUnitsY,
            abf_file.sweepUnitsX,
            abf_file.adcNames[0],
            abf_file.adcUnits[0],
            1,
            abf_file.adcUnits[0][1],
            0,
            abf_file.dataSecPerPoint,
            abf_file.sweepPointCount,
            np.min(abf_file.sweepY),
        ]

        metadata_list.append(np.max(abf_file.sweepY))

        metadata_list.append("3" if abf_file.adcUnits[0] == "pA" else "0")

        return metadata_list

    def build_command_epoch_table(self):
        """Retrieves the PGF Table equivalent to the Dat Files
        """
        columns_list = ["series_name",
                    "sweep_number",
                    "node_type",
                    "holding_potential",
                    "duration",
                    "increment",
                    "voltage",

        ]

        # retrieves the first and the last sweep
        first, last = self.get_first_and_last_sweep()
        epochs_list = [
            [
                self.abf.protocol
                for _ in range(len(self.abf._epochPerDacSection.fEpochInitLevel))
            ],
            [
                self.abf.sweepCount
                for _ in range(len(self.abf._epochPerDacSection.fEpochInitLevel))
            ],
            self.abf._epochPerDacSection.nEpochType,
            [i / 1000 for i in self.abf._epochPerDacSection.fEpochInitLevel],
            [i / 10000 for i in self.abf._epochPerDacSection.lEpochInitDuration],
            [i / 1000 for i in self.abf._epochPerDacSection.fEpochLevelInc],
            [i / 1000 for i in self.abf._epochPerDacSection.fEpochInitLevel],
        ]
        #epochs_list.append(self.abf._epochPerDacSection.nEpochType)
        self.epochs_dataframe = pd.DataFrame(epochs_list, index = columns_list)
        self.epochs_dataframe.insert(loc = 0,
                                    column="col1",
                                    value = first)
        self.epochs_dataframe.insert(loc = len(self.epochs_dataframe.columns),
                                    column="col2",
                                    value = last)
        self.epochs_dataframe

        self.epochs_dataframe = self.epochs_dataframe.transpose()
        print(self.abf.channelList)
        self.epochs_dataframe["selected_channel"] = str(self.abf.channelList[0] + 1)


    def get_first_and_last_sweep(self):
        """Get The first and the last sweep from the dac eopchstable since
        these are usually not inserted in the pyABF class

        Returns:
            tuple: first_command and last_command section for the pgf file
        """
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
        """Getter for the sweep raw data table

        Returns:
            pd.DataFrame: table containing the raw data per swee
        """
        return self.data_table

    def get_metadata_table(self):
        """Gets the Metadata table from the amplifier

        Returns:
            pd.DataFrame: Table holding the Metadata
        """
        return self.metadata_table

    def get_command_epoch_table(self):
        """PGF File Getter from ABF File

        Returns:
            pd.DataFrame: Table holding the command epoch waves
        """
        return self.epochs_dataframe

    def get_memtest(self):
        """Can be used to run a membrane test retrieving the capacitance

        Returns:
            list: membrane test results
        """
        if self.abf_property_dictionary:
            return self.abf_property_dictionary["memtest"]

    def get_experiment_name(self):
        """Get The Current Experiment Name using the path IDD

        Returns:
            _type_: _description_
        """
        if self.abf_path_id:
            return self.abf_path_id

    def get_series_name(self):
        """Get the Current Series Name

        Returns:
            _type_: _description_
        """
        return self.abf.protocol

