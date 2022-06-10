import numpy as np
from numpy.core.arrayprint import DatetimeFormat 
from scipy.signal import savgol_filter
from scipy.signal import chirp, find_peaks, peak_widths

class CurrentClamp():
    """Class to perform action potential detection by means of peak detection and 
    further Action potential fitting to get onset, max mV, duration, half-width and rising time"""

    def __init__(self):
        """ redo the init function --> should be filled with parameters for fitting """ 
        self.window = 101
      
    
        self.threshold = 0 # select the threshold for peak detection
        self.prominence = 0.1
        self.lower = None
        self.upper = None

    def set_window_length(self, window):
        self.window = window
        print(self.window)

    def set_prominence(self, prominence):
        self.prominence = prominence

    def set_mv_threshold(self, threshold):
        self.threshold = threshold

    def get_window_length(self):
        return self.window
    
    def get_prominence(self):
        return self.prominence

    def get_mv_threshold(self):
        return self.threshold


    def get_time_derivative(self,time):
        """ get the time derivative for the slope calculation """
        deriv_time = np.diff(time)
        return deriv_time

    def get_derivatives_data(self, data_trace):
        """get the first filtered derivative
        input -> data_trace only data series"""
        self.data_trace = data_trace
        first_derivative = savgol_filter(data_trace, 
                                              window_length = self.window, 
                                              polyorder = 2, 
                                              deriv = 1
                                              )
        second_derivative = savgol_filter(first_derivative, 
                                        window_length = self.window, 
                                        polyorder = 2, 
                                        deriv = 1 )

        third_derivative = np.diff(second_derivative)

        return first_derivative, second_derivative, third_derivative


    def get_peak_second_derivative(self, second_diff):
        """ get the peak of the second derivative;
        input -> second_diff
        """
        second_peak = np.max(second_diff)
        index_peak = np.where(second_diff == second_peak)
        second_peak = self.data_trace[index_peak[0][0]]
        return index_peak[0][0], second_peak

    
    def get_peak_first_derivative(self, first_diff):
        """ get the peak of the first derivative;
        input -> first derivativ
        """
        first_peak = np.max(first_diff)
        index_peak = np.where(first_diff == first_peak)
        first_peak = self.data_trace[index_peak[0][0]]
        return index_peak[0][0], first_peak

    def get_max_value_data(self, data):
        """ get the max value of the peak of the peak of the peak 
        of the normal data stream
        """
        max = np.max(data)
        index_max = np.where(data == max)
        return index_max[0][0], max

    def get_sliced_third_min(self, third_deriv):
        max_third = np.max(third_deriv)
        third_sliced_min = np.min(third_deriv[np.where(third_deriv == max_third)[0][0]: ])
        third_sliced_index = np.where(third_deriv == third_sliced_min)
        third_min = self.data_trace[third_sliced_index[0][0]]
        return third_sliced_index[0][0], third_min

    def get_half_width(self, data):
        peaks, _ = find_peaks(data, prominence = self.prominence, height=self.threshold)

        if len(peaks) > 0:
            results_half = peak_widths(data, peaks, rel_height=0.5)
            result_eight = peak_widths(data, peaks, rel_height=0.2)
            return results_half, result_eight, len(peaks), peaks
        else:
            return(None, None, 0, None)

    def get_slope(self, first_deriv, deriv_time, start_series, end_series):
        """ Calculate the slope of the signal using the dv/dt method
        input: 
        first_deriv --> first derivative,
        deriv_time -> derivative of the time,
        start and end series to slice ROI,
        """

        first_slope = first_deriv[start_series:end_series]
        time_slope = deriv_time[start_series:end_series]
        slope = first_slope/time_slope
        return np.mean(slope)

        


        




    
   

        
        
    
        
        
        