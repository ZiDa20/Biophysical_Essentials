import numpy as np
import pandas as pd
from natsort import natsorted, ns

class InputResistance(object):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    def __init__(self):

        # really needed ?
        self.function_name = "Input Resistance"
        self.analysis_function_id = None
        self.series_name = None
        self.database = None
        self.plot_type_options = ["Rheobase Plot", "Sweep Plot"]
        self.lower_bound = None
        self.upper_bound = None

    @classmethod
    def create_new_specific_result_table_name(cls, analysis_function_id, data_table_name):
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        return "results_analysis_function_" + str(analysis_function_id) + "_" + data_table_name

    @classmethod
    def calculate_results(self):
        print("hello")
