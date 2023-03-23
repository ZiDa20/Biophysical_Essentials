import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MaxCurrent(SweepWiseAnalysisTemplate):
    """Calculates the max amplitude within the selecte Cursorbounds

    Args:
        SweepWiseAnalysisTemplate:
    """
    def __init__(self):
        super().__init__()
        self.plot_type_options = ["No Split", "Split by Meta Data"]
        self.function_name = 'max_current'

    def specific_calculation(self):
        self.cslow_normalization = 1
        return np.max(self.sliced_volt)

    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        self.cslow_normalization = 1
        max_val = np.max(self.sliced_volt)
        pos = np.where(self.sliced_volt == max_val)
        x_val = self.time[pos][0] + self.lower_bound
        return tuple((x_val, max_val))
