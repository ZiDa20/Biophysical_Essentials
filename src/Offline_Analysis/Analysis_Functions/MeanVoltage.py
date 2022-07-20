
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanVoltage(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'mean_voltage'
        self.plot_type_options = ["Boxplot"]

    @classmethod
    def specific_calculation(self):
        max_val = np.mean(self.sliced_volt)
        return max_val

    @classmethod
    def calculate_results(self):
        return super(MeanVoltage,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(MeanVoltage,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)