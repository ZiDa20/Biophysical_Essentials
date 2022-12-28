
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MinCurrent(SweepWiseAnalysisTemplate):
    
    function_name = 'min_current'
    plot_type_options = ["No Split", "Split by Meta Data"]
    def __init__(self):
        super(SweepWiseAnalysisTemplate, self).__init__()
        
    @classmethod
    def specific_calculation(cls):
        cls.cslow_normalization = 1
        max_val = np.min(cls.sliced_volt)
        return max_val

    @classmethod
    def live_data_calculation(cls):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        cls.cslow_normalization = 1
        min_val = np.min(cls.sliced_volt)
        pos = np.where(cls.sliced_volt == min_val)
        x_val = cls.time[pos][0] +cls.lower_bound
        return tuple((x_val, min_val))

    @classmethod
    def calculate_results(cls):
        return super(MinCurrent,cls).calculate_results()

    @classmethod
    def visualize_results(cls,custom_plot_widget):
        return super(MinCurrent,cls).visualize_results(custom_plot_widget)

    @classmethod
    def live_data(cls, lower_bound, upper_bound, experiment_name, series_identifier, database_handler, sweep_name=None):
        """"""    
        return super(MinCurrent, cls).live_data(lower_bound, upper_bound, experiment_name, series_identifier,
                                                 database_handler, sweep_name)

    def __str__(self) -> str:
        return "Min Current Class"