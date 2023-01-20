import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MaxCurrent(SweepWiseAnalysisTemplate):
    
    plot_type_options = ["No Split", "Split by Meta Data"]
    function_name = 'max_current'
    database = None

    @classmethod
    def specific_calculation(cls):
        cls.cslow_normalization = 1
        max_val = np.max(cls.sliced_volt)
        return max_val

    @classmethod
    def live_data_calculation(cls):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        cls.cslow_normalization = 1
        max_val = np.max(cls.sliced_volt)
        pos = np.where(cls.sliced_volt == max_val)
        x_val = cls.time[pos][0] + cls.lower_bound
        return tuple((x_val, max_val))
