from dataclasses import dataclass
from time import time
import numpy as numpy
import pandas as pd 
import os 
import sys
from numba import jit


##################################################
# Current Clamp Analysis without AP fitting      #
##################################################


class CurentClamp():

    def __init__(self, data, time):
        """ Initialize the current clamp data"""
        self.data = data
        self.time = time
        pass


    def calculate_resting_membrane(bounds_dictionary):

        """ Calculate the major means
        params:
        bounds_dictionary <- type(dict) -> Describes the input bounds """

        for i in input_bounds: # go trough al bounds and create the sliced arrays
            slice_data_1 <- self.data[in:out].np.mean() # calculate the means of this arrray


        return data # return the data should be input for plotting --> long dataframe format ToDo@MZ


    def input_resistance(bounds_dictionary):

        """Calculate the input resistance from the input data
        paramas:
        bounds_dictionary <- type(dict) -> Describes the input bounds"""



    def hyperpolarization_sacks(bounds_dictionary):

        """get type classification of putative hcn channel expression 
        params:
        bounds_dictionary <- type(dict) -> Describes the input bounds"""

