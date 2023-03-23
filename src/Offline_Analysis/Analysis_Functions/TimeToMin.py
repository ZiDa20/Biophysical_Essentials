import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import SweepWiseAnalysisTemplate

class TimeToMin(SweepWiseAnalysisTemplate):
    """ Calculates the Time to the minimum within the selecte cursor bounds

    Args:
        SweepWiseAnalysisTemplate (SweepWiseAnalysisTemplate)
    """
    def __init__(self):
        super().__init__()
        self.plot_type_options = ["No Split", "Split by Meta Data"]
        self.function_name = 'time_to_min'


    def specific_calculation(self):
        self.cslow_normalization = 0
        index = np.where(self.sliced_volt == np.amin(self.sliced_volt))[0]
        if len(index)>1:
            index = index[0]
        # the index is the position in the sliced trace: so when the
        # time is not sliced - but one only needs the relative time between zero and this index
        # and time is a linear interpolation
        min_time = self.time[index]
        if isinstance(min_time, np.ndarray):
            min_time = min_time[0]
        return min_time

    def live_data_calculation(self):
        """
        when live plot: draw a horizontal line from the start of a cursor bound to the minimum
        additionally illustrate this point (x,y value) with a marker
        @return:
        """
        y_min = np.min(self.sliced_volt)
        index = np.where(self.sliced_volt == y_min)[0][0]
        left_bound_pos = np.argwhere(np.array(self.time) > self.lower_bound)[0][0]
        #print(left_bound_pos)
        x_val = self.time[left_bound_pos:left_bound_pos+ index]
        y_val = [y_min for _ in x_val]
        return x_val, y_val
