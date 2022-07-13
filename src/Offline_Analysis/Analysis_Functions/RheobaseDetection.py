import numpy as np
import pandas as pd
from natsort import natsorted, ns

class RheobaseDetection(object):
    """
    Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    """
    def __init__(self):

        # really needed ?
        self.function_name = "Rheobase-Detection"
        self.analysis_function_id = None
        self.series_name = None
        self.database = None
        self.plot_type_options = ["Boxplot"]
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

        # set to None, will be set once and should be equal for all data tables
        holding_value = None
        increment_value = None
        self.time = None

        for data_table in data_table_names:

            #print("processing new data table")

            if self.time is None:
                self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)

            if holding_value is None:
                increment_value = self.database.get_data_from_pgf_table(self.series_name, "increment", 1)
                holding_value = self.database.get_data_from_pgf_table(self.series_name, "holding", 0)

            # get the data frame and make sure to sort sweep numbers correctly
            entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)
            #entire_sweep_table.sort_index(axis=1, inplace = True)

            number_of_sweeps = len(entire_sweep_table.columns)
            column_names = list(entire_sweep_table.columns)
            nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
            entire_sweep_table = entire_sweep_table[nat_sorted_columns]

            # analyse by column
            for column in entire_sweep_table:

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
                            injected_current = holding_value + (sweep_number - 1) * increment_value
                            new_specific_result_table_name = self.create_new_specific_result_table_name(
                                self.database.analysis_id, data_table)

                            result_data_frame = pd.DataFrame({'1st AP': [injected_current]})

                            self.database.update_results_table_with_new_specific_result_table_name(
                                self.database.analysis_id, self.analysis_function_id, data_table,
                                new_specific_result_table_name, result_data_frame)
                            break

                    else:
                        injected_current = holding_value + (sweep_number - 1) * increment_value
                        new_specific_result_table_name = self.create_new_specific_result_table_name(
                            self.database.analysis_id, data_table)

                        result_data_frame = pd.DataFrame({'1st AP': [injected_current]})


                        self.database.update_results_table_with_new_specific_result_table_name(
                        self.database.analysis_id, self.analysis_function_id, data_table, new_specific_result_table_name, result_data_frame)
                        break


    @classmethod
    def visualize_results(self, parent_widget, canvas, visualization_type):

        result_table_list = self.get_list_of_result_tables(parent_widget.analysis_id,
                                                           parent_widget.analysis_function_id)

        # go through each result table, calculate the mean for each row, add to the correct meta_data_specific data frame

        meta_data_groups = []
        meta_data_specific_df = []

        for table in result_table_list:
            self.database.database.execute(f'select * from {table}')
            query_data_df = self.database.database.fetchdf()


            q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                f'specific_result_table_name = \'{table}\'))'

            meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

            x_data = np.mean(query_data_df['1st AP'].values)
            #print(x_data)
            if meta_data_group in meta_data_groups:
                specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
                specific_df.insert(0, str(table), x_data, True)
                meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df
            else:
                # add a new meta data group
                meta_data_groups.append(meta_data_group)
                meta_data_specific_df.append(pd.DataFrame({str(table): [x_data]}))

            # print(meta_data_specific_df[0])

            # make the boxplot
        ax = canvas.figure.subplots()

        boxplot_matrix = []
        for meta_data in meta_data_specific_df:
            boxplot_matrix.append(meta_data.iloc[0].values)

        # no nan handling required since sweeps without an AP are not stored in the dataframe
        filtered_box_plot_data = boxplot_matrix

        #print(filtered_box_plot_data)

        # make custom labels containing the correct meta data group and the number of evaluated cells
        custom_labels = []

        for i in range(0, len(meta_data_groups)):
            custom_labels.append(meta_data_groups[i] + ": " + str(len(filtered_box_plot_data[i])))

        plot = ax.boxplot(filtered_box_plot_data,  # notch=True,  # notch shape
                          vert=True,  # vertical box alignment
                          patch_artist=True)

        # ax.violinplot(filtered_box_plot_data)
        ax.set_xticks(np.arange(1, len(meta_data_groups) + 1), labels=meta_data_groups)
        ax.set_xlim(0.25, len(meta_data_groups) + 0.75)

        default_colors = ['k', 'b', 'r', 'g', 'c']

        for patch, color in zip(plot['boxes'], default_colors[0:len(plot['boxes'])]):
            patch.set_facecolor(color)

        ax.legend(plot['boxes'], custom_labels, loc='upper left')

        parent_widget.export_data_frame = pd.DataFrame(filtered_box_plot_data)
        parent_widget.export_data_frame = parent_widget.export_data_frame.transpose()
        parent_widget.export_data_frame.columns = meta_data_groups

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
