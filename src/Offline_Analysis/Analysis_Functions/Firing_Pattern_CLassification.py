import pandas as pd
from scipy.signal import find_peaks
from natsort import natsorted, ns
import numpy as np
from math import nan, isnan
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
import  seaborn as sns

class FiringPatternCLassification(SweepWiseAnalysisTemplate):
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    def __init__(self):
        super().__init__()
        self.function_name = "Firing_Pattern"
        self.plot_type_options = ["Parameter-Heatmap"]
        
        
    def specific_calculation(self):
        # get the action potential firing pattern parameters for these 5 intervals:
        # traces come in here sliced already          
            # for total, 1/4, 2/4, 3/4, 4/4
                # - total number of action potentials
                # - total frequency of action potentials
                # - time to first action potential
                # - mean time diff between actions potential
                # - std time diff
                # 5. max height of action potentials
                # 6. min height of action potentials
                # 7. std deviation of action potential amplitudes

        print("running firing pattern analysis ")
        # @todo: let the user define this threshold (also dependent on the sampling frequency)
        height_threshold = 0.001
        distance_threshold = 200
        number_of_subintervals = 4 # per default total and 4 smaller intervals are examined
        self.res_dict = {}
       
        interval_length = len(self.sliced_volt)//number_of_subintervals
        print(interval_length)
        for interval in range(0,number_of_subintervals+1): 
            # i 0: do the total interval, else do small subinterval
            if interval == 0:
                start = interval_length * interval
                end = len(self.sliced_volt)
                prefix = "total_"
            else:
                start = interval_length * (interval-1)
                end = start + interval_length
                prefix = "int_"+str(interval)+"_"

            interval_signal = self.sliced_volt[start:end]
            interval_time = self.sliced_time[start:end]
            print(np.max(interval_signal))
            peaks, _ = find_peaks(interval_signal, height=height_threshold)#, distance=distance_threshold)
            peak_y = interval_signal[peaks]
            peak_x = interval_time[peaks]

            print(start)
            print(end)
            print("debug")
            # peak count
            n = prefix+"ap_count"
            self.res_dict[n] = len(peak_y)
            # ap frequency
            self.res_dict[prefix+"ap_frequency"] = len(peak_y)/(np.max(interval_time)-np.min(interval_time)) * 1000 # to compensate for the milliseconds 

        print(self.res_dict)
        res_df = pd.DataFrame([self.res_dict])
        return res_df   
    
    def append_to_result_df(self,column:int, data_table:str, res:pd.DataFrame):
        """append the new results for the specific data table and column to the existing result table for all the selected data

        Args:
            column (int): sweep number
            data_table (str): sweep_data table name
            res (pd.DataFrame): data frame with the numerical results for each parameter (==column)

        Returns:
            pd.DataFrame: concatted results of the so far analysed data
        """
        print("Firing Pattern Analysis Results")
        sweep_number = column.split("_")
        sweep_number = int(sweep_number[1])
        #"", "",, , "Duration", "Result", "Increment","experiment_name"]
        res["Analysis_ID"] = self.database.analysis_id
        res["Function_Analysis_ID"] = self.analysis_function_id
        res["Sweep_Table_Name"] = data_table
        res[ "Sweep_Number"] = sweep_number
        res[self.unit_name] = self.unit_name
        res["experiment_name"] = self.experiment_name

        merged_all_results = pd.concat([self.merged_all_results,res],ignore_index=True)
        return merged_all_results
