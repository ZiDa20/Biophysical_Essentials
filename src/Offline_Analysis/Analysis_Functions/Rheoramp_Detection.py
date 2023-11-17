import pandas as pd
from scipy.signal import find_peaks
from natsort import natsorted, ns
import numpy as np
from math import nan, isnan
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
import  seaborn as sns

class RheorampDetection(SweepWiseAnalysisTemplate):
    
    """_summary_

    Returns:
        _type_: _description_
    """
    
    def __init__(self):
        super().__init__()
        self.function_name = "RheoRamp-Detection"
        self.plot_type_options = ["Rheoramp-AUC"]
        
        
    def specific_calculation(self):
        """Implement this!"""
        pass
    
    def calculate_results(self):

            print("running rheoramp calculation")

            series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(
                self.series_name)

            # run a peak detection for each sweep.
            # store x and y position of each sweep in the db
            # get the names of all data tables to be evaluated
            data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
            agg_table = pd.DataFrame()
            # set time to non - will be set by the first data frame
            # should assure that the time and bound setting will be only exeuted once since it is the same all the time
            for data_table in data_table_names:
                experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
                entire_sweep_table = self.database.get_entire_sweep_table(data_table, fetchmode = 1)
                key_1 = list(entire_sweep_table.keys())[0]
                
                if entire_sweep_table[key_1].shape != self.data_shape:
                    self.data_shape = entire_sweep_table[key_1].shape
                    self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)

                #number_of_sweeps = len(entire_sweep_table.columns)
                #column_names = list(entire_sweep_table.columns)
                #nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
                #entire_sweep_table = entire_sweep_table[nat_sorted_columns]

                result_data_frame = pd.DataFrame()

                for column in entire_sweep_table:

                    data = entire_sweep_table.get(column)
                    if series_specific_recording_mode != "Voltage Clamp":
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                        data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
                      
                    # run the peak detection
                    peaks, _ = find_peaks(data, height=0.00, distance=200)

                    peak_y = data[peaks]
                    peak_x = self.time[peaks]

                    sweep_number = column.split("_")
                    sweep_number = int(sweep_number[1])
                    print(peaks)
                    number_peaks = len(peak_x) if peaks is not None else 0
                    tmp_df = pd.DataFrame([[sweep_number, number_peaks]], columns = ["Rheoramp","Number AP"])
                    tmp_df["experiment_name"] = experiment_name
                    tmp_df["Sweep_Table_Name"] = data_table
                    result_data_frame = pd.concat([result_data_frame,tmp_df])
                
                agg_table = pd.concat([agg_table, result_data_frame])

                # write result_data_frame into database

                #print(result_data_frame)

            new_specific_result_table_name = self.database.create_new_specific_result_table_name(self.analysis_function_id,
                                                                                        "Rheoramp_Number")

            print(agg_table)
            self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                    self.analysis_function_id,
                                                                                    data_table,
                                                                                    new_specific_result_table_name,
                                                                                    agg_table)

            print("added %s to database",new_specific_result_table_name)

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