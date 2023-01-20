import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class TimeToMax(SweepWiseAnalysisTemplate):

    plot_type_options = ["No Split", "Split by Meta Data"]
    function_name = 'time_to_max'
   
    @classmethod
    def specific_calculation(cls):
        cls.cslow_normalization = 0
        index = np.where(cls.sliced_volt == np.max(cls.sliced_volt))[0]
        if len(index)>1:
            index = index[0]
        # the index is the position in the sliced trace: so when the
        # time is not sliced - but one only needs the relative time between zero and this index
        # and time is a linear interpolation
        max_time = cls.time[index]
        print("max_time:")
        print(index)
        print(type(max_time))
        if  isinstance(max_time, np.ndarray):
            max_time = max_time[0]

        print(max_time)

        return max_time

    @classmethod
    def live_data_calculation(cls):
        """
        when live plot: draw a horizontal line from the start of a cursor bound to the minimum
        additionally illustrate this point (x,y value) with a marker
        @return:
        """
        y_max = np.max(cls.sliced_volt)
        index = np.where(cls.sliced_volt == y_max)[0][0]
        left_bound_pos = np.argwhere(np.array(cls.time) > cls.lower_bound)[0][0]
        #print(left_bound_pos)
        x_val = cls.time[left_bound_pos:left_bound_pos+ index]
        y_val = []
        for i in x_val:
            y_val.append(y_max)
        return tuple((x_val, y_val))
