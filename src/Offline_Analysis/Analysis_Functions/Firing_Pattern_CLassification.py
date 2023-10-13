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
        self.function_name = "RheoRamp-Detection"
        self.plot_type_options = ["Rheoramp-AUC"]
        
        
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
        height_threshold = 0
        distance_threshold = 200
        number_of_subintervals = 4 # per default total and 4 smaller intervals are examined
        self.res_dict = {}
        import debugpy
        debugpy.breakpoint()

       
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

            peaks, _ = find_peaks(interval_signal, height=height_threshold, distance=distance_threshold)
            peak_y = interval_signal[peaks]
            peak_x = interval_time[peaks]
            
            print(start)
            print(end)
            print("debug")
            # peak count
            self.res_dict[prefix+"ap_count"] = len(peak_y)
            # ap frequency
            self.res_dict[prefix+"ap_frequency"] = len(peak_y)/(np.max(interval_time)-np.min(interval_time)) * 1000 # to compensate for the milliseconds 

        print(self.res_dict)


    def merge_lists_to_list_of_tuples(self,list1, list2):
        """_summary_

        Args:
            list1 (_type_): _description_
            list2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        return [(list1[i], list2[i]) for i in range(len(list1))]
     
   
    def get_list_of_result_tables(self, analysis_id, analysis_function_id):
        '''
        reading all specific result table names from the database
        '''
        q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
        result_list = self.database.get_data_from_database(self.database.database, q,
                                                           [analysis_id, analysis_function_id])
        # print(analysis_id)
        # print(analysis_function_id)
        # print(q)
        result_list = (list(zip(*result_list))[0])
        return result_list
