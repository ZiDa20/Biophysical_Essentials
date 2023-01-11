import pandas as pd
from scipy.signal import find_peaks
from natsort import natsorted, ns
import numpy as np
from math import nan, isnan



class PeakFinding(object):
    
    """_summary_

    Returns:
        _type_: _description_
    """
    function_name = "Peak-Detection"
    plot_type_options = ["Time-AP-Relationship","AP-Overlay"]
    database = None  # database
    analysis_function_id = None
    series_name = None
    AP_WINDOW = 50

    @classmethod
    def calculate_results(cls):
    
        print("running rheoramp calculation")
        
        series_specific_recording_mode = cls.database.get_recording_mode_from_analysis_series_table(
            cls.series_name)

        # run a peak detection for each sweep.
        # store x and y position of each sweep in the db

        # get the names of all data tables to be evaluated
        data_table_names = cls.database.get_sweep_table_names_for_offline_analysis(cls.series_name)
            # set time to non - will be set by the first data frame
        # should assure that the time and bound setting will be only exeuted once since it is the same all the time
        time = None
        for data_table in data_table_names:

            if time is None:
                    time = cls.database.get_time_in_ms_of_by_sweep_table_name(data_table)

            entire_sweep_table = cls.database.get_entire_sweep_table_as_df(data_table)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            for column in entire_sweep_table:
                
                data = entire_sweep_table.get(column)

                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    data = np.interp(data, (data.min(), data.max()), (y_min, y_max))

                # run the peak detection
                peaks, _ = find_peaks(data, height=0.00, distance=200)
                               
                if len(peaks) > 0:
                    print(peaks)
                    ap_window = cls.extract_ap_potentials(data, time, peaks, column)
                else:
                     ap_window = None

            # write result_data_frame into database

            if ap_window:
                result_data_frame = pd.DataFrame(ap_window, columns = ["AP_Window", "AP_Time", "Sweep", "Peak"])

                new_specific_result_table_name = cls.create_new_specific_result_table_name(cls.analysis_function_id,
                                                                                            data_table, True)

                cls.database.update_results_table_with_new_specific_result_table_name(cls.database.analysis_id,
                                                                                        cls.analysis_function_id,
                                                                                        data_table,
                                                                                        new_specific_result_table_name,
                                                                                        result_data_frame)

                print("added %s to database",new_specific_result_table_name )


    @classmethod
    def extract_ap_potentials(cls, data: np.array, time: np.array, peaks:np.array, column:str):
        """´Function to extract the action potentials using the detected peaks


        Args:
            data (np.array): holding the signal data
            time (np.array): holding the time data
            peaks (np.array): holding the detected peaks

        Returns:
            _type_: _description_

        """
        ap_window = {"AP_Window": [], "AP_Time":[], "Sweep": [], "Peak": []}
        peak_count = 1

        for peak in list(peaks):
            ap_window["AP_Window"].extend(data[peak - cls.AP_WINDOW:peak + cls.AP_WINDOW])
            ap_window["AP_Time"].extend(time[peak - cls.AP_WINDOW:peak + cls.AP_WINDOW])
            ap_window["Sweep"].extend([column] *data[peak - cls.AP_WINDOW:peak + cls.AP_WINDOW].shape[0] )
            ap_window["Peak"].extend([peak_count]*data[peak - cls.AP_WINDOW:peak + cls.AP_WINDOW].shape[0])
            peak_count += 1

        
        #print(pd.DataFrame(ap_window, columns = ["AP_Window", "AP_Time"]))
        return ap_window
            
    @classmethod
    def merge_lists_to_list_of_tuples(self,list1, list2):
        """_summary_

        Args:
            list1 (_type_): _description_
            list2 (_type_): _description_

        Returns:
            _type_: _description_
        """
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
        return merged_list

    @classmethod
    def create_new_specific_result_table_name(cls, analysis_function_id, data_table_name, ap_window = None):
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        if ap_window:
            return "results_analysis_function_" + str(analysis_function_id) + "_" + data_table_name + "_" +"apwindow"
        else:
            return None

    @classmethod
    def visualize_results(cls, parent_widget):

        print("rheoramp visualization")

        result_table_list = cls.get_list_of_result_tables(parent_widget.analysis_id,
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
        # print(analysis_id)
        # print(analysis_function_id)
        # print(q)
        result_list = (list(zip(*result_list))[0])
        return result_list


    