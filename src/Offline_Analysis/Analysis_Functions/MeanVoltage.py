
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanVoltage(SweepWiseAnalysisTemplate):
    """Calculates the mean voltage of the sliced data"""
    
    def __init__(self):
        super().__init__()
        self.function_name = 'mean_voltage'
        self.plot_type_options = ["Boxplot", "Violinplot"]

    def specific_calculation(self) -> float:
        """Calculates the mean voltage of the sliced data

        Returns:
            float: mean_value
        """
        self.cslow_normalization = 0
        mean_val = np.mean(self.sliced_volt)
        return mean_val

   
    