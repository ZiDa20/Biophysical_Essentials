from Offline_Analysis.Analysis_Functions.Function_Templates.SeriesWiseAnalysis import *
import numpy as np
import math

class ActionPotentialFitting(SeriesWiseAnalysisTemplate):

    def __init__(self):
        SeriesWiseAnalysisTemplate.__init__(self)
        self.function_name = 'Action Potential Fitting'


    @classmethod
    def specific_calculation(self):

        print("running action potential fitting")

        fitting_parameters = {}
        # gets a single trace

        manual_threshold = 0.010  # * 1000 # where
        smoothing_window_length = 19

        # will return nan  if no AP peak with the manually specified threshold was detected
        if np.max(self.data) < manual_threshold:
            return None

        np.set_printoptions(suppress=False)
        first_derivative = []

        # self.data = np.multiply(self.data,1000)
        # self.data = np.round(self.data,2)

        for i in range(len(self.time) - 1):
            first_derivative.append(((self.data[i + 1] - self.data[i]) / (self.time[i + 1] - self.time[i])))

        # dx = np.diff(self.time)
        # dy = np.diff(self.data)
        # first_derivative = dy/dx

        first_derivative = np.array(first_derivative)
        # first_derivative = first_derivative.astype(float)
        first_derivative = np.round(first_derivative, 2)

        # if all values are 0 it will return
        if all(v == 0 for v in first_derivative):
            print(self.table_name)
            print(self._sweep)
            return None

        smoothed_first_derivative = first_derivative.copy()

        for i in range(len(first_derivative)):

            if i < (len(first_derivative) - smoothing_window_length - 1):

                # print(first_derivative[i])
                # print(first_derivative[i:i+smoothing_window_length])

                smoothed_val = np.mean(first_derivative[i:i + smoothing_window_length])
            else:
                smoothed_val = np.mean(first_derivative[i - smoothing_window_length:i])

            if math.isnan(smoothed_val):
                print("nan error")

            else:
                smoothed_first_derivative[i] = smoothed_val
                # print("no error")

        smoothed_first_derivative = np.round(smoothed_first_derivative, 2)

        """
        f = open('ap_debug.csv', 'a')

        writer = csv.writer(f)
        writer.writerow(self.time)
        writer.writerow(self.data)
        # writer.writerow(dx)
        # writer.writerow(dy)
        writer.writerow(first_derivative)
        writer.writerow(smoothed_first_derivative)
        
        """
        # returns a tuple of true values and therefore needs to be taken at pos 0
        threshold_pos_origin = np.where(smoothed_first_derivative >= manual_threshold)[0]

        threshold_pos = None

        for pos in threshold_pos_origin:
            if np.all(smoothed_first_derivative[pos:pos + 2 * smoothing_window_length] > manual_threshold) \
                    or (np.max(self.data[pos:pos + 2 * smoothing_window_length]) == np.max(self.data)):
                # np.polyfit(smoothed_first_derivative[pos:pos+2*smoothing_window_length,1)
                threshold_pos = pos
                break

        # if still none means there was no real AP
        if threshold_pos is None:
            print(self.table_name)
            print(self._sweep)
            return None

        t_threshold = self.time[threshold_pos]
        v_threshold = self.data[threshold_pos]

        time_to_amplitude = self.time[np.argmax(self.data)]

        amplitude_pos = np.argmax(self.data)

        # delta_amplitude = amplitude - v_threshold

        # get the point of hyperpolarisation which is the first extremum (minimum) after the AP peak
        # therefore get the first zero crossing point after zero crossing point of the AP peak from the first derivate.
        # using numpys where returns a tuple. I want to have the first point in this tuple -> [0][0]
        # ahp_pos = np.where(smoothed_first_derivative[amplitude_pos:]>=0)[0] [0] +  amplitude_pos

        ahp_pos = np.argmax(smoothed_first_derivative[amplitude_pos:] >= 0)

        # double the window to make sure to not miss the minimum due to the smoothing before
        try:
            ahp = np.amin(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)])
        except Exception as e:
            print(e)  # happens if ahp_pos is zero
            print(self.table_name)
            print(self._sweep)
            return None

        t_ahp = self.time[np.argwhere(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)] == ahp)][0][0]
        t_ahp += time_to_amplitude

        # only run analysis if there is an action potential, otherwise return nan
        if np.max(self.data) > manual_threshold:
            fitting_parameters['AP_Amplitude'] = np.max(self.data)
            fitting_parameters['Threshold_Amplitude'] = self.data[threshold_pos]
            fitting_parameters['AHP_Amplitude'] = np.amin(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)])
            fitting_parameters['t_AHP'] = t_ahp
            fitting_parameters['time_to_ahp'] = self.time[np.argwhere(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)] == ahp)][0][0]
            fitting_parameters['delta_ap_threshold'] = abs(np.max(self.data)) - abs(v_threshold)
            fitting_parameters['max_first_derivate'] = np.max(smoothed_first_derivative)
            fitting_parameters['time_max_first_derivate'] = self.time[np.argwhere(smoothed_first_derivative == np.max(smoothed_first_derivative))]
            fitting_parameters['min_first_derivate'] = np.min(smoothed_first_derivative)

        return self.fitting_parameters

    @classmethod
    def calculate_results(self):
        return super(ActionPotentialFitting,self).calculate_results()

    @classmethod
    def visualize_results(self,custom_plot_widget,analysis_id,analysis_function_id):
        return super(ActionPotentialFitting,self).visualize_results(custom_plot_widget,analysis_id,analysis_function_id)


