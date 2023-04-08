
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanCurrent(SweepWiseAnalysisTemplate):
    """MeanCurrent of the selected series per sweep in the selected cursor boundaries

    Args:
        SweepWiseAnalysisTemplate (object): _description_

    """
    
    def __init__(self):
        super().__init__()
        self.function_name = 'mean_current'
        self.plot_type_options = ["No Split", "Split by Meta Data"]

    def specific_calculation(self):
        """mean calculation specifically

        Returns:
            float: The mean value for the selected trace within the boundaries
        """
        self.cslow_normalization = 1
        return np.mean(self.sliced_volt)

    def live_data_calculation(self):
        """
        when live plot: draw a horizontal line where the mean value is from the beginning to the end of the cursor bound
        interval
        @return:
        """
        self.cslow_normalization = 1
        mean_val = np.mean(self.sliced_volt)

        left_bound_pos  = np.argwhere(np.array(self.time)>self.lower_bound)[0][0]
        right_bound_pos  = np.argwhere(np.array(self.time)>self.upper_bound)[0][0]
        x_val = self.time[left_bound_pos:right_bound_pos]
        y_val = [mean_val for _ in x_val]
        return x_val, y_val
