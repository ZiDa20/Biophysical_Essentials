
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanVoltage(SweepWiseAnalysisTemplate):
    """Calculates the mean voltage of the sliced data"""
    function_name = 'mean_voltage'
    plot_type_options = ["Boxplot", "Violinplot"]

    @classmethod
    def specific_calculation(cls) -> float:
        """Calculates the mean voltage of the sliced data

        Returns:
            float: mean_value
        """
        cls.cslow_normalization = 0
        mean_val = np.mean(cls.sliced_volt)
        return mean_val

    def __str__(self) -> str:
        return "Mean Voltage Class"
    