import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class InputResistance(SweepWiseAnalysisTemplate):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    
    plot_type_options = ["Linear Regression", "Aggregated"]
    function_name = "Input Resistance"
    database = None
    
    @classmethod
    def specific_calculation(cls):
        cls.cslow_normalization = 0
        return np.min(cls.sliced_volt)
    
    @classmethod
    def live_data_calculation(cls):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        cls.cslow_normalization = 1
        min_val = np.min(cls.sliced_volt)
        pos = np.where(cls.sliced_volt == min_val)
        x_val = cls.time[pos][0] +cls.lower_bound
        return tuple((x_val, min_val))
 


        
        
