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
    def calculate_results(self):
        return super(TimeToMax,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(TimeToMax,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)