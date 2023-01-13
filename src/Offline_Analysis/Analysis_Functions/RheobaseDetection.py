import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class RheobaseDetection(SweepWiseAnalysisTemplate):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    function_name = "Rheobase-Detection"
    plot_type_options = ["Rheobase Plot", "Sweep Plot"]
    analysis_function_id = None
    
    def __init__(cls):

        # really needed ?
        cls.series_name = None
        cls.database = None
        cls.plot_type_options = ["Rheobase Plot", "Sweep Plot"]
        cls.lower_bound = None
        cls.upper_bound = None

    @classmethod
    def calculate_results(cls):

        #print("Running Rheobase Detection")
        ap_detection_threshold = 0.01
        
        series_specific_recording_mode = cls.database.get_recording_mode_from_analysis_series_table(cls.series_name)

        # get the names of all data tables to be evaluated
        data_table_names = cls.database.get_sweep_table_names_for_offline_analysis(cls.series_name)
        cls.get_max_values_per_sweep_table(data_table_names)
        # set to None, will be set once and should be equal for all data tables
        cls.time = None

        for data_table in data_table_names:
            holding_value = None
            
            #print("processing new data table")
            # here we should select which increment should be used 
            if cls.time is None:
                cls.time = cls.database.get_time_in_ms_of_by_sweep_table_name(data_table)

            if holding_value is None:

                print(f'requesting holding value for table {data_table}')

                increment_value = cls.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)

                holding_value = cls.database.get_data_from_recording_specific_pgf_table(data_table, "holding", 0)

            # get the data frame and make sure to sort sweep numbers correctly
            entire_sweep_table = cls.database.get_entire_sweep_table_as_df(data_table)
            #entire_sweep_table.sort_index(axis=1, inplace = True)

            number_of_sweeps = len(entire_sweep_table.columns)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            # analyse by column
            for column in entire_sweep_table:
                print(column)
                cls.data = entire_sweep_table.get(column)
            

                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    cls.data = np.interp(cls.data, (cls.data.min(), cls.data.max()), (y_min, y_max))

                sweep_number = column.split("_")
                sweep_number = int(sweep_number[1])

        

                if np.max(cls.data) > ap_detection_threshold:

                    # two options are allowed in here
                    if sweep_number<=number_of_sweeps-2:

                        next_sweep = "sweep_"+str(sweep_number+1)
                        s1 = entire_sweep_table.get(next_sweep)
                        y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, next_sweep)
                        s1 = np.interp(s1, (s1.min(), s1.max()), (y_min, y_max))

                        next_sweep = "sweep_" + str(sweep_number + 2)
                        s2 = entire_sweep_table.get(next_sweep)
                        y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, next_sweep)
                        s2 = np.interp(s2, (s2.min(), s2.max()), (y_min, y_max))

                        if (np.max(s1) > ap_detection_threshold) and (np.max(s2) > ap_detection_threshold):
                            # get the holding value and the incrementation steps from the pgf data for this series
                            # sweeps , holding, increment
                            #injected_current = holding_value + (sweep_number - 1) * increment_value
                            print("increment_value")
                            print(increment_value)
                            injected_current =  (sweep_number - 1) * increment_value * 1000
                            new_specific_result_table_name = cls.create_new_specific_result_table_name(
                                cls.analysis_function_id, data_table)

                            print("injected current with greater 2 sweeps")
                            print(injected_current)
                            result_data_frame = pd.DataFrame({'1st AP': [injected_current]})

                            cls.database.update_results_table_with_new_specific_result_table_name(
                                cls.database.analysis_id, cls.analysis_function_id, data_table,
                                new_specific_result_table_name, result_data_frame)
                            break

                    else:
                        # holding_value +
                        injected_current = (sweep_number - 1) * increment_value * 1000
                        print("injected current with smaller - 2 sweeps")
                        print(injected_current)
                        new_specific_result_table_name = cls.create_new_specific_result_table_name(
                            cls.analysis_function_id, data_table)

                        result_data_frame = pd.DataFrame({'1st AP': [injected_current]})


                        cls.database.update_results_table_with_new_specific_result_table_name(cls.database.analysis_id, 
                                                                                               cls.analysis_function_id, 
                                                                                               data_table, 
                                                                                               new_specific_result_table_name, 
                                                                                               result_data_frame)
                        break

    @classmethod
    def get_max_values_per_sweep_table(cls, data_table_names):
        # This needs an overhaul!!!
        """
        Args:
            data_table_names (list): list of Rheobase tables per experiment
        """
        
        for data_table in data_table_names: # got through the data tables
            increment = 0
            current_list = []
            mean_voltage_list = []
            series_specific_recording_mode = cls.database.get_recording_mode_from_analysis_series_table(cls.series_name)
            holding_value = None

            if holding_value is None:
                    print(f'requesting holding value for table {data_table}')
                    increment_value = cls.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)
            entire_sweep_table = cls.database.get_entire_sweep_table_as_df(data_table)
            number_of_sweeps = len(entire_sweep_table.columns)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            for column in entire_sweep_table:
                    print(column)
                    cls.data = entire_sweep_table.get(column)
                    if series_specific_recording_mode != "Voltage Clamp":
                        y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                        cls.data = np.interp(cls.data, (cls.data.min(), cls.data.max()), (y_min, y_max))
                    
                    mean_voltage_list.append(np.max(cls.data))
                    current_list.append(increment)
                    increment += increment_value*1000
            
            meaned_rheobase = pd.DataFrame()
            meaned_rheobase["current"] = current_list
            meaned_rheobase["max_voltage"] = mean_voltage_list
            
            
            mean_table_name = cls.create_new_specific_result_table_name(
                            cls.analysis_function_id, data_table) + "_max"
            cls.database.update_results_table_with_new_specific_result_table_name(cls.database.analysis_id,
                                                                                    cls.analysis_function_id,
                                                                                    data_table, 
                                                                                    mean_table_name,
                                                                                    meaned_rheobase)