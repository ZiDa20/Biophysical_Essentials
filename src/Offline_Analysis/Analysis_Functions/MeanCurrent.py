
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanCurrent(SweepWiseAnalysisTemplate):
    function_name = 'mean_current'
    plot_type_options = ["No Split", "Split by Meta Data"]

    def __init__(self):
        SweepWiseAnalysisTemplate.__init__(self)
        
    @classmethod
    def specific_calculation(self):
        self.cslow_normalization = 1
        max_val = np.mean(self.sliced_volt)
        return max_val

    @classmethod
    def live_data_calculation(self):
        """
        when live plot: draw a horizontal line where the mean value is from the beginning to the end of the cursor bound
        interval
        @return:
        """
        self.cslow_normalization = 1
        mean_val = np.mean(self.sliced_volt)

        print(self.lower_bound)
        print(self.upper_bound)
        left_bound_pos  = np.argwhere(np.array(self.time)>self.lower_bound)[0][0]
        right_bound_pos  = np.argwhere(np.array(self.time)>self.upper_bound)[0][0]
        print(left_bound_pos)
        print(right_bound_pos)
        x_val = self.time[left_bound_pos:right_bound_pos]
        y_val = []
        for i in x_val:
            y_val.append(mean_val)
        return tuple((x_val, y_val))

   
    @classmethod
    def live_data(self, lower_bound, upper_bound, experiment_name, series_identifier, database_handler,
                  sweep_name=None):
        return super(MeanCurrent, self).live_data(lower_bound, upper_bound, experiment_name, series_identifier,
                                                 database_handler, sweep_name)