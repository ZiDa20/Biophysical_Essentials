import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class RheobaseDetection(SweepWiseAnalysisTemplate):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    
    def __init__(self):
        super().__init__()
        self.function_name = "Rheobase-Detection"
        self.plot_type_options = ["Rheobase Plot", "Sweep Plot"]
   
    def calculate_results(self):  # sourcery skip: low-code-quality

        #print("Running Rheobase Detection")
        ap_detection_threshold = 0.01

        series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)

        # get the names of all data tables to be evaluated
        data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
        self.get_max_values_per_sweep_table(data_table_names)
        # set to None, will be set once and should be equal for all data tables
        self.time = None
        agg_table = pd.DataFrame()
        for data_table in data_table_names:
            holding_value = None
            experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
            #print("processing new data table")
            # here we should select which increment should be used 
            
            entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)

            key_1 = list(entire_sweep_table.keys())[0]
            if entire_sweep_table[key_1].shape != self.data_shape:
                self.data_shape = entire_sweep_table[key_1].shape
                self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)

            if holding_value is None:

                print(f'requesting holding value for table {data_table}')

                increment_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)

                holding_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "holding", 0)

            # get the data frame and make sure to sort sweep numbers correctly
            #entire_sweep_table.sort_index(axis=1, inplace = True)

            number_of_sweeps = len(entire_sweep_table.columns)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            # analyse by column
            for column in entire_sweep_table:
                print(column)
                self.data = entire_sweep_table.get(column)


                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

                sweep_number = column.split("_")
                sweep_number = int(sweep_number[1])



                if np.max(self.data) > ap_detection_threshold:
                    if sweep_number<=number_of_sweeps-2:
                        next_sweep = f"sweep_{str(sweep_number + 1)}"
                        s1 = entire_sweep_table.get(next_sweep)
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, next_sweep)
                        s1 = np.interp(s1, (s1.min(), s1.max()), (y_min, y_max))

                        next_sweep = f"sweep_{str(sweep_number + 2)}"
                        s2 = entire_sweep_table.get(next_sweep)
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, next_sweep)
                        s2 = np.interp(s2, (s2.min(), s2.max()), (y_min, y_max))

                        if (np.max(s1) > ap_detection_threshold) and (np.max(s2) > ap_detection_threshold):
                            # get the holding value and the incrementation steps from the pgf data for this series
                            # sweeps , holding, increment
                            #injected_current = holding_value + (sweep_number - 1) * increment_value
                            print("increment_value")
                            print(increment_value)
                            injected_current =  (sweep_number - 1) * increment_value * 1000
                            

                            print("injected current with greater 2 sweeps")
                            print(injected_current)
                            result_data_frame = pd.DataFrame({'1st AP': [injected_current]})
                            result_data_frame["experiment_name"] = experiment_name
                            agg_table = pd.concat([agg_table, result_data_frame])
                            break

                    else:
                        # holding_value +
                        injected_current = (sweep_number - 1) * increment_value * 1000
                        print("injected current with smaller - 2 sweeps")
                        print(injected_current)
                        new_specific_result_table_name = self.create_new_specific_result_table_name(
                            self.analysis_function_id, data_table)

                        result_data_frame = pd.DataFrame({'1st AP': [injected_current]})
                        result_data_frame["experiment_name"] = experiment_name
                        agg_table = pd.concat([agg_table, result_data_frame])
                        break
               
        new_specific_result_table_name = self.database.create_new_specific_result_table_name(
                            self.analysis_function_id, "Rheobase_detection")     
        
        self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id, 
                                                                                        self.analysis_function_id, 
                                                                                        data_table, 
                                                                                        new_specific_result_table_name, 
                                                                                        agg_table)

    def specific_calculation(self):
        """this needs to be implemented!!"""
        pass
    
    
    def get_max_values_per_sweep_table(self, data_table_names):
        # This needs an overhaul!!!
        """
        Args:
            data_table_names (list): list of Rheobase tables per experiment
        """
        
        holding_value = None
        agg_table = pd.DataFrame()
        for data_table in data_table_names: # got through the data tables
            experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
            increment = 0
            current_list = []
            mean_voltage_list = []
            series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)
            if holding_value is None:
                    print(f'requesting holding value for table {data_table}')
                    increment_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)
            entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)
            number_of_sweeps = len(entire_sweep_table.columns)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            for column in entire_sweep_table:
                    print(column)
                    self.data = entire_sweep_table.get(column)
                    if series_specific_recording_mode != "Voltage Clamp":
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                        self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

                    mean_voltage_list.append(np.max(self.data))
                    current_list.append(increment)
                    increment += increment_value*1000

            meaned_rheobase = pd.DataFrame()
            meaned_rheobase["current"] = current_list
            meaned_rheobase["Result"] = mean_voltage_list
            meaned_rheobase["experiment_name"] = experiment_name
            agg_table = pd.concat([agg_table, meaned_rheobase])

        mean_table_name = self.database.create_new_specific_result_table_name(
                        self.analysis_function_id, "Rheobase_detection") + "_max"
        
        self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                self.analysis_function_id,
                                                                                data_table, 
                                                                                mean_table_name,
                                                                                agg_table)