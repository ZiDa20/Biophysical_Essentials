
from src.Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MaxCurrent(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'max_current'

    @classmethod
    def specific_calculation(self):

        max_val = np.max(self.sliced_volt)
        return max_val

    @classmethod
    def calculate_results(self):
        return super(MaxCurrent,self).calculate_results()

    @classmethod
    def visualize_results(self):
        return super(MaxCurrent,self).visualize_results()