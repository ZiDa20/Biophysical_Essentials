import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class InputResistance(SweepWiseAnalysisTemplate):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    
    def __init__(self):
        super().__init__()
        self.plot_type_options = ["Linear Regression", "Aggregated"]
        self.function_name = "InputResistance"
        self.database = None
    
    def specific_calculation(self):
        return np.min(self.sliced_volt)
    
    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        self.cslow_normalization = 1
        min_val = np.min(self.sliced_volt)
        pos = np.where(self.sliced_volt == min_val)
        x_val = self.time[pos][0] +self.lower_bound
        return tuple((x_val, min_val))
 


        
        
