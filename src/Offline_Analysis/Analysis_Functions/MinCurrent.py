
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MinCurrent(SweepWiseAnalysisTemplate):
    
    function_name = 'min_current'
    plot_type_options = ["No Split", "Split by Meta Data"]
        
    @classmethod
    def specific_calculation(cls):
        cls.cslow_normalization = 1
        max_val = np.min(cls.sliced_volt)
        return max_val

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
 