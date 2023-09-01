import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class CapacitanceMeasurements(SweepWiseAnalysisTemplate):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """

    def __init__(self):
        super().__init__()
        self.plot_type_options = ["Capacitance Plot"]
        self.function_name = "CapacitanceMeasurements"
        self.database = None
        self.PREWINDOW = 400 # this should be the window before the pgf segment
        self.POSTWINDOW = 400 # this should be the window after the pgf segment
        self.LAGWINDOW = 50 # this should be the window after the pgf segment
        self.duration_list = None
        self.pgf_segment = None
        self.not_normalize = True

    def specific_calculation(self):
        """
        This function is called by the parent class and contains the main calculation
        Returns:
            _type_: _description_
        """
        upper_bound, lower_bound = self.get_pgf_segments_upper_lower()
        times = self.get_time_per_segment(upper_bound, lower_bound)
        upper_mean = np.mean(self.sliced_volt[times[2]:times[3]])
        lower_mean = np.mean(self.sliced_volt[times[0]:times[1]])
        return upper_mean-lower_mean

    def get_time_per_segment(self, upper_bound: float, lower_bound: float):
        """
        This function is called by the parent class and contains the main calculation
        Returns:
            _type_: _description_
        """
        # time lower - 200 - time lower
        # time upper + 50 : time upper + 50 + 400
        # this should be an editor in the graphical interface
        # we should make the widget more configurable through the analysis function

        try:
            time_lower = 0
            time_lower_end = np.argmax(self.time >= self.PREWINDOW)
            time_upper = np.argmax(self.time >= upper_bound + self.LAGWINDOW)
            time_upper_end = np.argmax(self.time >= upper_bound + self.LAGWINDOW + self.POSTWINDOW)
            return time_lower, time_lower_end, time_upper, time_upper_end
        except Exception as e:
            print(f"this is the error of the capacitance: {e}")

    def get_pgf_segments_upper_lower(self):
        """ This calculates the duration of the pulse stimulated"""
        self.duration_list = [float(i) for i in self.duration_list]
        pgf_segments_lower = np.sum(self.duration_list[:self.pgf_segment - 1]) * 1000
        pgf_segments_upper = np.sum(self.duration_list[:self.pgf_segment]) * 1000
        return pgf_segments_upper, pgf_segments_lower

    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        self.cslow_normalization = 1
        min_val = np.min(self.sliced_volt)
        pos = np.where(self.sliced_volt == min_val)
        x_val = self.time[pos][0] +self.lower_bound
        return tuple((x_val, min_val))
