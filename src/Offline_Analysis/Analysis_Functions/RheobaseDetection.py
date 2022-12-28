import numpy as np
import pandas as pd
from natsort import natsorted, ns

class RheobaseDetection(object):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    function_name = "Rheobase-Detection"
    plot_type_options = ["Rheobase Plot", "Sweep Plot"]
    def __init__(self):

        # really needed ?
        self.function_name = "Rheobase-Detection"
        self.analysis_function_id = None
        self.series_name = None
        self.database = None
        self.plot_type_options = ["Rheobase Plot", "Sweep Plot"]
        self.lower_bound = None
        self.upper_bound = None

    @classmethod
    def create_new_specific_result_table_name(cls, analysis_function_id, data_table_name):
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        return "results_analysis_function_" + str(analysis_function_id) + "_" + data_table_name

    @classmethod
    def calculate_results(self):

        #print("Running Rheobase Detection")
        ap_detection_threshold = 0.01
        
        series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)

        # get the names of all data tables to be evaluated
        data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
        self.get_max_values_per_sweep_table(data_table_names)
        # set to None, will be set once and should be equal for all data tables
        self.time = None

        for data_table in data_table_names:
            holding_value = None
            
            #print("processing new data table")
            # here we should select which increment should be used 
            if self.time is None:
                self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)

            if holding_value is None:

                print(f'requesting holding value for table {data_table}')

                increment_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)

                holding_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "holding", 0)

            # get the data frame and make sure to sort sweep numbers correctly
            entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)
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

                    # two options are allowed in here
                    if sweep_number<=number_of_sweeps-2:

                        next_sweep = "sweep_"+str(sweep_number+1)
                        s1 = entire_sweep_table.get(next_sweep)
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, next_sweep)
                        s1 = np.interp(s1, (s1.min(), s1.max()), (y_min, y_max))

                        next_sweep = "sweep_" + str(sweep_number + 2)
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
                            new_specific_result_table_name = self.create_new_specific_result_table_name(
                                self.database.analysis_id, data_table)

                            print("injected current with greater 2 sweeps")
                            print(injected_current)
                            result_data_frame = pd.DataFrame({'1st AP': [injected_current]})

                            self.database.update_results_table_with_new_specific_result_table_name(
                                self.database.analysis_id, self.analysis_function_id, data_table,
                                new_specific_result_table_name, result_data_frame)
                            break

                    else:
                        # holding_value +
                        injected_current = (sweep_number - 1) * increment_value * 1000
                        print("injected current with smaller - 2 sweeps")
                        print(injected_current)
                        new_specific_result_table_name = self.create_new_specific_result_table_name(
                            self.database.analysis_id, data_table)

                        result_data_frame = pd.DataFrame({'1st AP': [injected_current]})


                        self.database.update_results_table_with_new_specific_result_table_name(
                        self.database.analysis_id, self.analysis_function_id, data_table, new_specific_result_table_name, result_data_frame)
                        break

    @classmethod
    def get_max_values_per_sweep_table(self, data_table_names):
        """
        Args:
            data_table_names (list): list of Rheobase tables per experiment
        """
        
        for data_table in data_table_names:
            increment = 0
            current_list = []
            mean_voltage_list = []
            series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)
            holding_value = None

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
            meaned_rheobase["max_voltage"] = mean_voltage_list
            mean_table_name = self.create_new_specific_result_table_name(
                            self.database.analysis_id, data_table) + "_max"
            self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                    self.analysis_function_id,
                                                                                    data_table, 
                                                                                    mean_table_name,
                                                                                    meaned_rheobase)

    @classmethod
    def visualize_results(self, parent_widget):

        result_table_list = self.get_list_of_result_tables(parent_widget.analysis_id,
                                                           parent_widget.analysis_function_id)

        return result_table_list

    @classmethod
    def get_list_of_result_tables(self, analysis_id, analysis_function_id):
        '''
        reading all specific result table names from the database
        '''
        q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
        result_list = self.database.get_data_from_database(self.database.database, q,
                                                           [analysis_id, analysis_function_id])
        #print(analysis_id)
        #print(analysis_function_id)
        #print(q)
        result_list = (list(zip(*result_list))[0])
        return result_list
