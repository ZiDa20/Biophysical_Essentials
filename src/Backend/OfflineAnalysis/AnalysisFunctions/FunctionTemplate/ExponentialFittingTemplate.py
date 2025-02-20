from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.SweepWiseAnalysis import *
from scipy.optimize import curve_fit
import numpy as np

class ExponentialFittingTemplate(SweepWiseAnalysisTemplate):
    """
    Template class for exponential fitting. This class contains common methods used 
    for both mono-exponential and bi-exponential fitting, including curve fitting and 
    calculation of fit quality metrics.
    """


    def specific_calculation_helper(self, x_data, y_data, fit_function, initial_params):
        """
        Performs curve fitting and computes fit quality metrics for the given data.

        Args:
            x_data (array-like): Independent variable (e.g., time).
            y_data (array-like): Dependent variable (e.g., voltage).
            fit_function (function): The fitting function to be used (e.g., `monoexponential` or `biexponential`).
            initial_params (list): Initial guess for the fitting parameters.

        Returns:
            tuple: A tuple containing:
                - popt (array): Optimal parameters for the fitting function.
                - y_fit (array): Fitted values from the fit function.
                - rss (float): Residual Sum of Squares.
                - r_squared (float): Coefficient of determination (R²).
                - rmse (float): Root Mean Square Error.
                - chi_square (float): Chi-Square statistic.
        """
        popt, _ = curve_fit(fit_function, x_data, y_data, p0=initial_params, maxfev=5000)
        y_fit = fit_function(x_data, *popt)
        
        # Compute fit quality metrics
        rss = np.sum((y_data - y_fit) ** 2)  # Residual Sum of Squares
        ss_total = np.sum((y_data - np.mean(y_data)) ** 2)  # Total sum of squares
        r_squared = 1 - (rss / ss_total)  # R²
        rmse = np.sqrt(np.mean((y_data - y_fit) ** 2))  # RMSE
        chi_square = np.sum(((y_data - y_fit) ** 2) / y_fit)  # Chi-Square

        return popt, y_fit, rss, r_squared, rmse, chi_square