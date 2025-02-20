from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.ExponentialFittingTemplate import ExponentialFittingTemplate
import numpy as np

class MonoExponentialFitting(ExponentialFittingTemplate):
    """
    Mono-exponential fitting class. This class handles the curve fitting for mono-exponential functions,
    which involve a single exponential decay term. It also includes methods for calculating fit quality metrics
    specific to mono-exponential fitting.
    """
    
    def __init__(self):
        """
        Initializes the MonoExponentialFitting class with custom function name and plot options.
        """
        super().__init__()
        self.function_name = 'mono_exponential_fitting'
        self.plot_type_options = ["ExponentialFitting-Heatmap"]
        self.not_normalize = True

    def monoexponential(self, x, a1, t1, c):
        """
        Mono-exponential function.
        Describes a process with a single exponential decay.

        Args:
            x (array): Independent variable (e.g., time).
            a1 (float): Amplitude of the exponential component.
            t1 (float): Time constant of the exponential component.
            c (float): Offset constant.

        Returns:
            array: Computed mono-exponential values.
        """
        return a1 * np.exp(-x / t1) + c

    def specific_calculation(self):
        """
        Performs mono-exponential fitting on the sliced data and calculates fit quality metrics.

        This method uses the `monoexponential` function to fit the data and compute metrics like 
        Residual Sum of Squares (RSS), R², RMSE, and Chi-Square. The results are returned in a dictionary.

        Returns:
            dict: A dictionary containing the fitting parameters (A1, t1, C) and quality metrics.
        """
        print("Performing mono-exponential fitting")

        # Use the data for fitting from class instance
        x_data = self.sliced_time 
        y_data = self.sliced_volt

        # Initial guess for mono-exponential parameters
        initial_params = [-0.3, 100, 0]
        
        # Call the method to perform fitting and calculate fit quality metrics
        popt, y_fit_mon, rss, r_squared, rmse, chi_square = self.specific_calculation_helper(x_data, y_data, self.monoexponential, initial_params)
        
        # Output fit results
        print("Mono-Exponential Fit Parameters:", popt)
        print("Mono-Exponential Fit Quality:")
        print(f"RSS: {rss}")
        print(f"R²: {r_squared}")
        print(f"RMSE: {rmse}")
        print(f"Chi-Square: {chi_square}")

        # Return results
        return {
            "A1": popt[0],
            "t1": popt[1],
            "C": popt[2],
            "RSS": rss,
            "R²": r_squared,
            "RMSE": rmse,
            "Chi-Square": chi_square
        }

    def live_data_calculation(self):
        """
        Performs live data calculation for mono-exponential fitting.

        This method is used to calculate the mono-exponential fit in real-time for the given data.

        Returns:
            tuple: A tuple containing:
                - x_data (array): Independent variable (e.g., time).
                - y_fit_mon (array): Fitted values from the mono-exponential function.
        """
        x_data = self.sliced_time 
        y_data = self.sliced_volt
        
        # Initial guess for mono-exponential parameters
        initial_params = [-0.3, 100, 0]
        
        popt, y_fit_mon, _, _, _, _ = self.specific_calculation_helper(x_data, y_data, self.monoexponential, initial_params)
        
        return x_data, y_fit_mon