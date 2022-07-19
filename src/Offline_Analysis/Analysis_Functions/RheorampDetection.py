import pandas as pd
from scipy.signal import find_peaks
from natsort import natsorted, ns
import numpy as np
from math import nan, isnan

import  seaborn as sns

class RheorampDetection(object):

    def __init__(self):

        self.function_name = "RheoRamp-Detection"
        self.series_name = None
        self.analysis_function_id = None
        self.database = None  # database
        self.plot_type_options = ["Boxplot"]

    @classmethod
    def calculate_results(self):

            print("running rheoramp calculation")

            series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(
                self.series_name)

            # run a peak detection for each sweep.
            # store x and y position of each sweep in the db

            # get the names of all data tables to be evaluated
            data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)

            # set time to non - will be set by the first data frame
            # should assure that the time and bound setting will be only exeuted once since it is the same all the time
            time = None


            for data_table in data_table_names:

                if time is None:
                     time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)

                entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)

                number_of_sweeps = len(entire_sweep_table.columns)
                column_names = list(entire_sweep_table.columns)
                nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
                entire_sweep_table = entire_sweep_table[nat_sorted_columns]

                result_data_frame = pd.DataFrame()

                for column in entire_sweep_table:

                    data = entire_sweep_table.get(column)

                    if series_specific_recording_mode != "Voltage Clamp":
                        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                        data = np.interp(data, (data.min(), data.max()), (y_min, y_max))

                    # run the peak detection
                    peaks, _ = find_peaks(data, height=0.00, distance=200)

                    peak_y = data[peaks]
                    peak_x = time[peaks]

                    sweep_number = column.split("_")
                    sweep_number = int(sweep_number[1])

                    tmp_df = pd.DataFrame({str(sweep_number):self.merge_lists_to_list_of_tuples(peak_x,peak_y)})

                    result_data_frame = pd.concat([result_data_frame,tmp_df],axis = 1)

                # write result_data_frame into database

                #print(result_data_frame)

                new_specific_result_table_name = self.create_new_specific_result_table_name(self.analysis_function_id,
                                                                                            data_table)

                self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                       self.analysis_function_id,
                                                                                       data_table,
                                                                                       new_specific_result_table_name,
                                                                                       result_data_frame)

                print("added %s to database",new_specific_result_table_name )

    @classmethod
    def merge_lists_to_list_of_tuples(self,list1, list2):
            merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
            return merged_list

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
    def visualize_results(self, parent_widget, canvas, visualization_type):

        print("rheoramp visualization")

        result_table_list = self.get_list_of_result_tables(parent_widget.analysis_id,
                                                          parent_widget.analysis_function_id)

        meta_data_groups = []
        result_df = pd.DataFrame()

        for table in result_table_list:

            self.database.database.execute(f'select * from {table}')

            query_data_df = self.database.database.fetchdf()

            #print(table)
            #print(query_data_df)


            # in this case, each sweep column holds a list of tuples

            q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                f'specific_result_table_name = \'{table}\'))'

            meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

            for column in query_data_df:

                result_list = []

                data = query_data_df.get(column)
                data = data.dropna(how='all')
                data = data.values.tolist()
                #print(data)
                float_list = []
                for d in data:
                    float_list.append(tuple(float(s) for s in d.strip("()").split(",")))

                #print(float_list)

                x_data = 0

                try: # could fail if there are no tuples e.g. when no AP was detecteed only nans
                    x_coordinates, y_coordinates = map(list, zip(*float_list))

                    #print(x_coordinates)

                    x_data = len(x_coordinates) # number of tuples

                except Exception as e:
                    print("Error")
                    print(e)

                tmp_df = pd.DataFrame([["sweep"+column,x_data,meta_data_group]], columns=["sweep_number","count", "meta_data_name"])

                result_df = pd.concat([result_df, tmp_df])

            print(result_df)

        ax = canvas.figure.subplots()

        # create a grouped boxplot

        print(result_df)

        sns.boxplot(data = result_df, x='sweep_number', y='count', hue = 'meta_data_name', ax = ax )

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
