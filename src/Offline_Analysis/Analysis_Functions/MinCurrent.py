
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MinCurrent(SweepWiseAnalysisTemplate):

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        self.function_name = 'min_current'
        self.plot_type_options = ["No Split", "Split by Meta Data"]


    @classmethod
    def specific_calculation(self):
        self.cslow_normalization = 1
        max_val = np.min(self.sliced_volt)
        return max_val

    @classmethod
    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        self.cslow_normalization = 1
        min_val = np.min(self.sliced_volt)
        pos = np.where(self.sliced_volt == min_val)
        x_val = self.time[pos][0] +self.lower_bound
        return tuple((x_val, min_val))

    @classmethod
    def calculate_results(self):
        return super(MinCurrent,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(MinCurrent,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)

    @classmethod
    def live_data(self, lower_bound, upper_bound, experiment_name, series_identifier, database_handler,
                  sweep_name=None):
        return super(MinCurrent, self).live_data(lower_bound, upper_bound, experiment_name, series_identifier,
                                                 database_handler, sweep_name)