
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MaxCurrent(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'max_current'
        self.plot_type_options = ["No Split", "Split by Meta Data"]


    @classmethod
    def specific_calculation(self):
        self.cslow_normalization = 1
        max_val = np.max(self.sliced_volt)
        return max_val

    @classmethod
    def calculate_results(self):
        return super(MaxCurrent,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(MaxCurrent,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)