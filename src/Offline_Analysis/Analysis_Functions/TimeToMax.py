import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class TimeToMax(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'time_to_max'
        self.plot_type_options = ["No Split", "Split by Meta Data"]


    @classmethod
    def specific_calculation(self):
        self.cslow_normalization = 0
        index = np.where(self.sliced_volt == np.max(self.sliced_volt))[0]
        if len(index)>1:
            index = index[0]
        # the index is the position in the sliced trace: so when the
        # time is not sliced - but one only needs the relative time between zero and this index
        # and time is a linear interpolation
        max_time = self.time[index]
        print("max_time:")
        print(index)
        print(type(max_time))
        if  isinstance(max_time, np.ndarray):
            print("array")
            max_time = max_time[0]

        print(max_time)

        return max_time

    @classmethod
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
        y_val = []
        for i in x_val:
            y_val.append(y_max)
        return tuple((x_val, y_val))

    @classmethod
    def calculate_results(self):
        return super(TimeToMax,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget, canvas, visualization):
        return super(TimeToMax,self).visualize_results(custom_plot_widget)

    @classmethod
    def live_data(self, lower_bound, upper_bound, experiment_name, series_identifier, database_handler,
                  sweep_name=None):
        return super(TimeToMax, self).live_data(lower_bound, upper_bound, experiment_name, series_identifier,
                                                database_handler, sweep_name)