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
        self.function_name = 'MonoExponentialFitting'
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
        if self.sliced_time is None or self.sliced_volt is None:
            return None

        if len(self.sliced_time) == 0 or len(self.sliced_volt) == 0:
            return None

        x_data = self.sliced_time - self.sliced_time[0]
        y_data = self.sliced_volt

        # Remove NaNs
        mask = ~np.isnan(x_data) & ~np.isnan(y_data)
        x_data = x_data[mask]
        y_data = y_data[mask]

        if len(x_data) < 5:
            return None

        # Initial guess for mono-exponential parameters
        initial_params = [-0.3, 100, 0]
        
        # Call the method to perform fitting and calculate fit quality metrics
        result = self.specific_calculation_helper(
            x_data, y_data, self.monoexponential, initial_params
        )

        if result is None or result[0] is None:
            print("Fitting failed safely")
            return None

        popt, y_fit, rss, r_squared, rmse, chi_square = result
        
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

        x_data = self.sliced_time
        y_data = self.sliced_volt

        if x_data is None or y_data is None:
            return None, None

        if len(x_data) == 0 or len(y_data) == 0:
            return None, None

        # Normalize (important)
        x_data = x_data - x_data[0]

        initial_params = [-0.3, 100, 0]

        result = self.specific_calculation_helper(
        x_data, y_data, self.monoexponential, initial_params
        )

        if result is None or result[0] is None:
            return None, None

        popt, y_fit_mon, _, _, _, _ = result

        return x_data, y_fit_mon

    # 24_03_2026 def live_data_calculation(self):
    #     """
    #     Performs live data calculation for mono-exponential fitting.

    #     This method is used to calculate the mono-exponential fit in real-time for the given data.

    #     Returns:
    #         tuple: A tuple containing:
    #             - x_data (array): Independent variable (e.g., time).
    #             - y_fit_mon (array): Fitted values from the mono-exponential function.
    #     """
    #     x_data = self.sliced_time 
    #     y_data = self.sliced_volt
        
    #     # Initial guess for mono-exponential parameters
    #     initial_params = [-0.3, 100, 0]
        
    #     popt, y_fit_mon, _, _, _, _ = self.specific_calculation_helper(x_data, y_data, self.monoexponential, initial_params)
        
    #     return x_data, y_fit_mon