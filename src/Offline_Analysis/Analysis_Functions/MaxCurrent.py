
from src.Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MaxCurrent(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'max_current'

    @classmethod
    def specific_calculation_II(self):
        print ("calculating max")
        #trace_max = np.max(sliced_trace)
        #return trace_max

    @classmethod
    def calculate_results(self):
        return super(MaxCurrent,self).calculate_results()

    @classmethod
    def visualize_results(self):
        return super(MaxCurrent,self).visualize_results()