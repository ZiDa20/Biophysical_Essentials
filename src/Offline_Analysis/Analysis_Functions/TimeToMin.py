import numpy as np
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class TimeToMin(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'time_to_min'
        self.plot_type_options = ["No Split", "Split by Meta Data"]


    @classmethod
    def specific_calculation(self):
        self.cslow_normalization = 0
        index = np.where(self.sliced_volt == np.amin(self.sliced_volt))[0]



        if len(index)>1:
            index = index[0]

        # the index is the position in the sliced trace: so when the
        # time is not sliced - but one only needs the relative time between zero and this index
        # and time is a linear interpolation
        min_time = self.time[index]
        print("min_time:")
        print(index)
        print(type(min_time))
        if  isinstance(min_time, np.ndarray):
            print("array")
            min_time = min_time[0]

        print(min_time)

        return min_time

    @classmethod
    def calculate_results(self):
        return super(TimeToMin,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(TimeToMin,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)