import math

import numpy as np
import pandas as pd
import sys
import csv




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

    def get_elements(self,recording_mode):
        if recording_mode == "Voltage Clamp":
            return ["max_current","min_current","mean_current","area_current","time-to-maximum","time-to-minimum"]
        else:
            return ["Single_action_potential_analysis", "AP-fitting","Event-Detection","Cluster","Input Resistance"]

    def call_function_by_string_name(self,function_name):
        # it seemed to be easier to call an return vals with if than with dictionary ... maybe not the best way (dz)
        if function_name == "max_current":
            return self.max_current()
        if function_name == "min_current":
            return self.min_current()
        if function_name == "mean_current":
            return self.mean_current()
        if function_name == "area_current":
            return self.get_area()
        if function_name =="time-to-maximum":
            return self.time_to_maximum()
        if function_name == "time-to-minimum":
            return self.time_to_minimum()

        # @TODO add current clamp functions
        if function_name== "Single_action_potential_analysis":
            return self.single_action_potential_analysis()

    @property
    def lower_bounds(self):
        """ get the lower and upper bounds """
        print("The lower bound: ")
        return self._lower_bounds


    @property
    def upper_bounds(self):
        print("The upper bound: ")
        return self._upper_bounds


    @lower_bounds.setter
    def lower_bounds(self, lower_bound):
        """ set the lower and upper bound """
        if type(lower_bound) in [int,float]:
            self._lower_bounds = lower_bound
        else:
            raise TypeError("Wrong Input please specificy floats")


    @upper_bounds.setter
    def upper_bounds(self, upper_bound):
        """ set the lower and upper bound """
        if type(upper_bound) in [int,float]:
            self._upper_bounds = upper_bound
        else:
            raise TypeError("Wrong Input please specificy floats")

    def construct_trace(self):
        """ construct the trace """
        try:
            self.trace = np.vstack((self.time, self.data)).T
        except:
            raise ValueError("Please use the same dimension, only 1-dimensional arrays should be used")


    def slice_trace(self):
        """ slice the trace based on the incoming upper and lower bounds """
        if all([self._lower_bounds, self._upper_bounds]):
            self.sliced_trace = self.trace[((self.trace[:,0] > self._lower_bounds) & (self.trace[:,0] < self._upper_bounds))]
            self.sliced_volt = self.sliced_trace[:,1]
        else:
            raise ValueError("No upper and lower bonds set yet, please sets and use the rectangular function")



    def max_current(self):
        """ determine the max voltage """
        self._max = np.max(self.sliced_volt)
        return self._max

    def mean_current(self):
        self._mean = np.mean(self.sliced_volt)
        return self._mean

    def min_current(self):
        self._min = np.min(self.sliced_volt)
        return self._min

    def time_to_maximum(self):
        index = self.index_calculation(self._max)
        time = self.sliced_trace[:,0][:index]
        self._max_time = self.calculate_time(np.max(time),np.min(time))
        print(self._max_time)

    def time_to_minimum(self):
        index = self.index_calculation(self._min)
        time = self.sliced_trace[:,0][:index]
        self._min_time = self.calculate_time(np.max(time),np.min(time))
        print(self._min_time)

    def time_to_threshold(self, threshold):
        if type(threshold) in [int,float]:
            index = self.index_calculation(threshold, True)
            time = self.sliced_trace[:,0][:index]
            self._threshold_time = self.calculate_time(np.max(time),np.min(time))
            print(self._threshold_time)
        else:
            raise ValueError("Please use a float or integer as a valid voltage threshold")

    def index_calculation(self, value, comp = None):
        if comp:
            index = np.where(self.sliced_volt > value)[0][0]
            return index
        index = np.where(self.sliced_volt == value)[0][0]
        return index

    def calculate_time(self,maximum, minimum):
        time = maximum-minimum
        if time < 0:
                qc = 1
                return rseries, qc
        else:
            raise "Rseries changed to much is flagged for quality check"
            qc = 0
            return rseries, qc

    def get_area(self):
        self.area =  np.trapz(self.sliced_trace[:,0],self.sliced_trace[:,1])
        return abs(self.area)*10000

    def single_action_potential_analysis(self):
        manual_threshold = 0.010 * 1000

        np.set_printoptions(suppress=False)
        first_derivative = []

        self.data = np.multiply(self.data,1000)
        self.data = np.round(self.data,2)

        for i in range(len(self.time)-1):
            first_derivative.append(((self.data[i+1]-self.data[i])/(self.time[i+1]-self.time[i])))
            
        #dx = np.diff(self.time)
        #dy = np.diff(self.data)
        #first_derivative = dy/dx



        first_derivative = np.array(first_derivative)
        #first_derivative = first_derivative.astype(float)
        first_derivative = np.round(first_derivative,2)

        smoothed_first_derivative = first_derivative.copy()
        smoothing_window_length = 19

        for i in range(len(first_derivative)):

            if i < (len(first_derivative)-smoothing_window_length-1):

                #print(first_derivative[i])
                # print(first_derivative[i:i+smoothing_window_length])

                smoothed_val = np.mean(first_derivative[i:i+smoothing_window_length])
            else:
                smoothed_val = np.mean(first_derivative[i- smoothing_window_length:i ])

            if math.isnan(smoothed_val):
                print("nan error") 

            else:
                smoothed_first_derivative[i] = smoothed_val
                print("no error")


        smoothed_first_derivative = np.round(smoothed_first_derivative,2)

        f = open('ap_debug.csv', 'a')

        writer = csv.writer(f)
        writer.writerow(self.time)
        writer.writerow(self.data)
        #writer.writerow(dx)
        #writer.writerow(dy)
        writer.writerow(first_derivative)
        writer.writerow(smoothed_first_derivative)

         # returns a tuple of true values and therefore needs to be taken at pos 0
        threshold_pos = np.where(smoothed_first_derivative>=manual_threshold)[0]

        for pos in threshold_pos:
            if np.all(smoothed_first_derivative[pos:pos+2*smoothing_window_length]>manual_threshold):
                threshold_pos = pos
                break


        t_threshold = self.time[threshold_pos]
        v_threshold = self.data[threshold_pos]

        amplitude = np.max(self.data)
        time_to_amplitude = self.time[np.argmax(self.data) ]
        
        amplitude_pos = np.argmax(self.data)
        
        delta_amplitude = amplitude - v_threshold


        # get the point of hyperpolarisation which is the first extremum (minimum) after the AP peak
        # therefore get the first zero crossing point after zero crossing point of the AP peak from the first derivate.
        # using numpys where returns a tuple. I want to have the first point in this tuple -> [0][0]
        #ahp_pos = np.where(smoothed_first_derivative[amplitude_pos:]>=0)[0] [0] +  amplitude_pos

        ahp_pos = np.argmax(smoothed_first_derivative[amplitude_pos:]>=0)

        # double the window to make sure to not miss the minimum due to the smoothing before
        ahp = np.amin( self.data[amplitude_pos:(amplitude_pos+2*ahp_pos)] )

        t_ahp = self.time[np.argwhere(self.data[amplitude_pos:(amplitude_pos+2*ahp_pos)]==ahp)] [0] + time_to_amplitude

        print("done")
        return amplitude


    @classmethod
    def __sub__(cls, first_trace, second_trace):
        try:
            sub_trace = self.slice_volt - second_trace
        except ValueError:
            raise("Please use input with the same shape")

    @classmethod
    def __add__(cls,first_trace, second_trace):
        try:
            sub_trace = self.slice_volt + second_trace
            return sub_trace

        except:
            raise ValueError("Please use input with the same shape")

    @classmethod
    def __multiply__(cls, first_trace, second_trace):
        try:
            sub_trace = self.slice_volt * second_trace
            return sub_trace

        except ValueError:
            raise("Please use input with the same shape")

