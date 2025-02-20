from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.ExponentialFittingTemplate import ExponentialFittingTemplate
import numpy as np


class BiExponentialFitting(ExponentialFittingTemplate):
    """
    Bi-exponential fitting class. This class handles the curve fitting for bi-exponential functions,
    which involve two exponential decay terms. It also includes methods for calculating fit quality metrics
    specific to bi-exponential fitting.
    """
    
    def __init__(self):
        """
        Initializes the BiExponentialFitting class with custom function name and plot options.
        """
        super().__init__()
        self.function_name = 'bi_exponential_fitting'
        self.plot_type_options = ["ExponentialFitting-Heatmap"]
        self.not_normalize = True
    
    def biexponential(self, x, a1, t1, a2, t2, c):
        """
        Bi-exponential function.
        Describes a process with two exponential decays.

        Args:
            x (array): Independent variable (e.g., time).
            a1 (float): Amplitude of the first exponential component.
            t1 (float): Time constant of the first exponential component.
            a2 (float): Amplitude of the second exponential component.
            t2 (float): Time constant of the second exponential component.
            c (float): Offset constant.

        Returns:
            array: Computed bi-exponential values.
        """
        return a1 * np.exp(-x / t1) + a2 * np.exp(-x / t2) + c

    def specific_calculation(self):
        """
        Performs bi-exponential fitting on the sliced data and calculates fit quality metrics.

        This method uses the `biexponential` function to fit the data and compute metrics like 
        Residual Sum of Squares (RSS), R², RMSE, and Chi-Square. The results are returned in a dictionary.

        Returns:
            dict: A dictionary containing the fitting parameters (A1, t1, A2, t2, C) and quality metrics.
        """
        print("Performing bi-exponential fitting")

        # Use the data for fitting from class instance
        x_data = self.sliced_time 
        y_data = self.sliced_volt

        # Initial guess for bi-exponential parameters
        initial_params = [-0.3, 1000, -0.05, 100, 0]
        
        # Call the method to perform fitting and calculate fit quality metrics
        popt, y_fit_bi, rss, r_squared, rmse, chi_square = self.specific_calculation_helper(x_data, y_data, self.biexponential, initial_params)
        
        # Output fit results
        print("Bi-Exponential Fit Parameters:", popt)
        print("Bi-Exponential Fit Quality:")
        print(f"RSS: {rss}")
        print(f"R²: {r_squared}")
        print(f"RMSE: {rmse}")
        print(f"Chi-Square: {chi_square}")

        # Return results
        return {
            "A1": popt[0],
            "t1": popt[1],
            "A2": popt[2],
            "t2": popt[3],
            "C": popt[4],
            "RSS": rss,
            "R²": r_squared,
            "RMSE": rmse,
            "Chi-Square": chi_square
        }

    def live_data_calculation(self):
        """
        Performs live data calculation for bi-exponential fitting.

        This method is used to calculate the bi-exponential fit in real-time for the given data.

        Returns:
            tuple: A tuple containing:
                - x_data (array): Independent variable (e.g., time).
                - y_fit_bi (array): Fitted values from the bi-exponential function.
        """
        x_data = self.sliced_time 
        y_data = self.sliced_volt
        
        # Initial guess for bi-exponential parameters
        initial_params = [-0.3, 1000, -0.05, 100, 0]
        
        popt, y_fit_bi, _, _, _, _ = self.specific_calculation_helper(x_data, y_data, self.biexponential, initial_params)
        
        return x_data, y_fit_bi


