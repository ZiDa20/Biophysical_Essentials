
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class MeanVoltage(SweepWiseAnalysisTemplate):
    """Calculates the mean voltage of the sliced data"""
    function_name = 'mean_voltage'
    plot_type_options = ["Boxplot", "Violinplot"]

    def __init__(self):
        """Initializes the MeanVoltage Class by calling the SweepWiseAnalysisTemplate __init__ method
        """
        SweepWiseAnalysisTemplate.__init__(self)
        

    @classmethod
    def specific_calculation(cls) -> float:
        """Calculates the mean voltage of the sliced data

        Returns:
            float: mean_value
        """
        cls.cslow_normalization = 0
        mean_val = np.mean(cls.sliced_volt)
        return mean_val

    @classmethod
    def calculate_results(cls) -> list:
        """Calculates the Results by calling the SweepWiseAnalysisTemplate calculate_results method

        Returns:??
            list: returns the calculated results in form of result tables
        """
        return super(MeanVoltage,cls).calculate_results()

    @classmethod
    def visualize_results(cls,custom_plot_widget):
        """_summary_

        Args:
            custom_plot_widget (QWidget): The Widget which holds the data in the stacked widget?? Improve

        Returns:
            pd.DataFrame: pd.DataFrame holding the results of the Analysis in a long format
        """
        return super(MeanVoltage,cls).visualize_results(custom_plot_widget)

    def __str__(self) -> str:
        return "Mean Voltage Class"
    