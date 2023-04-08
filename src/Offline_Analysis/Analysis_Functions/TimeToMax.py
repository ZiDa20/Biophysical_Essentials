import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class TimeToMax(SweepWiseAnalysisTemplate):


    def __init__(self):
        self.plot_type_options = ["No Split", "Split by Meta Data"]
        self.function_name = 'time_to_max'
   
    
    def specific_calculation(self):
        """_summary_: Specific calculation for the TimeToMax
        Should calculate the time it takes from the the cursorbound to the maximum value

        Returns:
            float: max_time
        """
        self.cslow_normalization = 0
        index = np.where(self.sliced_volt == np.max(self.sliced_volt))[0]
        if len(index)>1:
            index = index[0]
        # the index is the position in the sliced trace: so when the
        # time is not sliced - but one only needs the relative time between zero and this index
        # and time is a linear interpolation
        # we should add logging of values here
        max_time = self.time[index]
        if isinstance(max_time, np.ndarray):
            max_time = max_time[0]
        return max_time

    
    def live_data_calculation(self):
        """
        when live plot: draw a horizontal line from the start of a cursor bound to the minimum
        additionally illustrate this point (x,y value) with a marker
        @return:
        """
        y_max = np.max(self.sliced_volt)
        index = np.where(self.sliced_volt == y_max)[0][0]
        left_bound_pos = np.argwhere(np.array(self.time) > self.lower_bound)[0][0]
        #print(left_bound_pos)
        x_val = self.time[left_bound_pos:left_bound_pos+ index]
        y_val = [y_max for _ in x_val]
        return x_val, y_val
