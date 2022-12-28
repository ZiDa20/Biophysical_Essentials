import math

import numpy as np
import pandas as pd
import sys
import csv
from scipy.signal import find_peaks

class AnalysisRaw():

    def __init__(self,time = None, data = None):
        """ Object initializing
        add trace with childs """

        # set the time the experiment was runnning
        self.time = time
        self.data = data # set the data associated to the time
        self._trace = None

        # make additional slots for the metadata
        self._lower_bounds = None
        self._upper_bounds = None

        self._sweep = None # sweep in voltage or as current
        self._meta = None # integrate the metadata to the child
        self.sliced_trace = None # both time as well as voltage data
        self.sliced_volt = None # only voltage data
        self._area = None
        self._max = None
        self._mean = None
        self._min = None

        # for extended analysis
        self.holding = None
        self.increment = None

        # for debug purpose:
        self.table_name = None

    