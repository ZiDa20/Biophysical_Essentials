
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MinCurrent(SweepWiseAnalysisTemplate):
    
    def __init__(self):
        super().__init__()
        self.function_name = 'min_current'
        self.plot_type_options = ["No Split", "Split by Meta Data"]
        
    def specific_calculation(self):
        self.cslow_normalization = 1
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
 