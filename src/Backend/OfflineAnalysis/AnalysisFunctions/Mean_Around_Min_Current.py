
from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.SweepWiseAnalysis import *

class MeanAroundMinCurrent(SweepWiseAnalysisTemplate):
    
    def __init__(self):
        super().__init__()
        self.function_name = 'mean_aorund_min'
        self.plot_type_options = ["No Split", "Split by Meta Data"]
        
    def specific_calculation(self):
            """Finds the minimum voltage in the sliced signal and calculates the mean voltage 
            in a ±50 ms window around it.
            """
            self.cslow_normalization = 1  # Not clear why this is needed, but keeping it

            # Identify the index of the minimum voltage value in the sliced signal
            min_index = np.argmin(self.sliced_volt)

            # Get the time at this minimum voltage
            min_time = self.sliced_time[min_index]

            # Define threshold time window (±50 ms)
            lower_thresh = min_time - 50
            upper_thresh = min_time + 50

            # Find indices within the threshold time range
            mask = (self.sliced_time >= lower_thresh) & (self.sliced_time <= upper_thresh)

            # Compute the mean voltage within this window
            mean_voltage = np.mean(self.sliced_volt[mask])

            return mean_voltage  # Return the calculated mean voltage

        
    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        #self.cslow_normalization = 1
        # Identify the index of the minimum voltage value in the sliced signal
        #min_index = np.argmin(self.sliced_volt)
        #x_val = self.sliced_time[self.sliced_volt] +self.lower_bound

        #return tuple((x_val, self.sliced_volt[min_index]))
 
        self.cslow_normalization = 1
        min_val = np.min(self.sliced_volt)
        pos = np.where(self.sliced_volt == min_val)
        x_val = self.time[pos][0] +self.lower_bound
        return tuple((x_val, min_val))
 