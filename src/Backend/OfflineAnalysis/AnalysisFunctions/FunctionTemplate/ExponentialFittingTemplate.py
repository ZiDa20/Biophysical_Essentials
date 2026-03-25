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

    # --- DYNAMIC BOUNDS ---
    n_params = len(initial_params)

    lower_bounds = [-np.inf] * n_params
    upper_bounds = [np.inf] * n_params

    # Optional: enforce tau > 0 (only if you want)
    for i in range(n_params):
        if i % 2 == 1:  # assumes t1, t2 are at index 1, 3
            lower_bounds[i] = 1e-6
            upper_bounds[i] = 5000

    try:
        popt, _ = curve_fit(
            fit_function,
            x_data,
            y_data,
            p0=initial_params,
            bounds=(lower_bounds, upper_bounds),
            maxfev=20000
        )

        y_fit = fit_function(x_data, *popt)

    except Exception as e:
        print("Fitting failed:", e)
        return None, None, None, None, None, None

    # --- FIT QUALITY METRICS ---
    rss = np.sum((y_data - y_fit) ** 2)

    ss_total = np.sum((y_data - np.mean(y_data)) ** 2)
    r_squared = 1 - (rss / ss_total) if ss_total != 0 else None

    rmse = np.sqrt(np.mean((y_data - y_fit) ** 2))

    y_fit_safe = np.where(y_fit == 0, 1e-12, y_fit)
    chi_square = np.sum(((y_data - y_fit) ** 2) / y_fit_safe)

    return popt, y_fit, rss, r_squared, rmse, chi_square

    # 24_03_2026: def specific_calculation_helper(self, x_data, y_data, fit_function, initial_params):
    #     """
    #     Performs curve fitting and computes fit quality metrics for the given data.

    #     Args:
    #         x_data (array-like): Independent variable (e.g., time).
    #         y_data (array-like): Dependent variable (e.g., voltage).
    #         fit_function (function): The fitting function to be used (e.g., `monoexponential` or `biexponential`).
    #         initial_params (list): Initial guess for the fitting parameters.

    #     Returns:
    #         tuple: A tuple containing:
    #             - popt (array): Optimal parameters for the fitting function.
    #             - y_fit (array): Fitted values from the fit function.
    #             - rss (float): Residual Sum of Squares.
    #             - r_squared (float): Coefficient of determination (R²).
    #             - rmse (float): Root Mean Square Error.
    #             - chi_square (float): Chi-Square statistic.
    #     """
    #     try:
    #         popt, _ = curve_fit(
    #             fit_function,
    #             x_data,
    #             y_data,
    #             p0=initial_params,
    #             bounds=(
    #                 [-np.inf, 1e-6, -np.inf],   # tau > 0
    #                 [np.inf, 5000, np.inf]      # tau upper bound
    #             ),
    #             maxfev=20000
    #         )
        
    #         y_fit = fit_function(x_data, *popt)
    #     except Exception as e:
    #         print("Fitting failed:", e)
    #         return None, None, None, None, None, None
    #     # Compute fit quality metrics
    #     rss = np.sum((y_data - y_fit) ** 2)  # Residual Sum of Squares
    #     ss_total = np.sum((y_data - np.mean(y_data)) ** 2)  # Total sum of squares
    #     r_squared = 1 - (rss / ss_total)  # R²
    #     rmse = np.sqrt(np.mean((y_data - y_fit) ** 2))  # RMSE
    #     # 24_03_2026 : chi_square = np.sum(((y_data - y_fit) ** 2) / y_fit)  # Chi-Square
    #     y_fit_safe = np.where(y_fit == 0, 1e-12, y_fit)
    #     chi_square = np.sum(((y_data - y_fit) ** 2) / y_fit_safe)
    #     return popt, y_fit, rss, r_squared, rmse, chi_square