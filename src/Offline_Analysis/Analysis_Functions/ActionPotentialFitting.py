from unittest import result
import numpy as np
import pandas as pd
import math

class ActionPotentialFitting(object):

    def __init__(self):

        # really needed ?
        self.function_name = "Action Potential Fitting"
        self.analysis_function_id = None

        self.data = None
        self.voltage = None

        self.database = None  # database
        self.plot_type_options = ["Boxplot"]

        self.lower_bound = None
        self.upper_bound = None
        self.time = None
        self.data = None

        self.sliced_volt = None

        self.database = None
        self.series_name = None

    def show_configuration_options(self):
        print("not implemented")

    @classmethod
    def calculate_results(self):
        """
        iterate through each single sweep of all not discarded series in the database and save the calculated result
        to a new database table.
        :return:
        """

        # @todo get this from the configuration window
        series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)

        # @todo Discuss - is that the case ?
        try:
            if series_specific_recording_mode == "Voltage Clamp":
                cslow_normalization = 1
            else:
                cslow_normalization = 0
        except Exception as e:
            print("Error in Excecute_Single_Series_Analysis")
            print(e)
            cslow_normalization = 0

        data_table_names = []
        # get the names of all data tables to be evaluated
        data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
        # set time to non - will be set by the first data frame
        # should assure that the time and bound setting will be only exeuted once since it is the same all the time
        self.time = None
        self.upper_bounds = None
        self.lower_bounds = None

        for data_table in data_table_names:

            #
            if self.time is None:
                self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)
            # calculate the time
            # set the lower bound
            # set the upper bound

            entire_sweep_table = self.database.get_entire_sweep_table(data_table)

            # added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
            # adding the name would increase readibility of the database ut also add a lot of redundant information

            result_data_frame = pd.DataFrame()

            for column in entire_sweep_table:

                self.data = entire_sweep_table.get(column)

                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

                res = self.specific_calculation()

                # res can be none if there is a beat that had no action potential
                if res is not None:
                    #print("result")
                    #print(res)

                    if cslow_normalization:
                        cslow = self.database.get_cslow_value_for_sweep_table(data_table)
                        res = res / cslow
                        print("normalized")
                        print(res)

                    # get the sweep number
                    sweep_number = column.split("_")
                    sweep_number = int(sweep_number[1])

                    if result_data_frame.empty:
                        result_data_frame = pd.DataFrame.from_dict(res, orient='index', columns = [str(sweep_number)])
            
                    else:
                        col_count = len(result_data_frame.columns)
                        #print(col_count)
                        dataframe = pd.DataFrame.from_dict(res, orient='index', columns = [str(sweep_number)])
                        print(dataframe)
                        result_data_frame = pd.concat([result_data_frame, dataframe],axis=1)
                        print(result_data_frame)

            # write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table
            result_data_frame['Fitting Parameters'] = result_data_frame.index
            #print(result_data_frame)

            new_specific_result_table_name = self.create_new_specific_result_table_name(self.database.analysis_id,
                                                                                        data_table)
            self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                   self.analysis_function_id,
                                                                                   data_table,
                                                                                   new_specific_result_table_name,
                                                                                   result_data_frame)

            # make sure to register all fitting parameters to plotted

            print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')

        self.run_late_register_feature()

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
    def specific_calculation(self):
        print("running action potential fitting")

        fitting_parameters = {}
        # gets a single trace

        manual_threshold = 0.010  # * 1000 # where
        smoothing_window_length = 19

        # will return nan  if no AP peak with the manually specified threshold was detected
        if np.max(self.data) < manual_threshold:
            return None

        np.set_printoptions(suppress=False)
        first_derivative = []

        # self.data = np.multiply(self.data,1000)
        # self.data = np.round(self.data,2)

        for i in range(len(self.time) - 1):
            first_derivative.append(((self.data[i + 1] - self.data[i]) / (self.time[i + 1] - self.time[i])))

        # dx = np.diff(self.time)
        # dy = np.diff(self.data)
        # first_derivative = dy/dx

        first_derivative = np.array(first_derivative)
        # first_derivative = first_derivative.astype(float)
        first_derivative = np.round(first_derivative, 2)

        # if all values are 0 it will return
        if all(v == 0 for v in first_derivative):
            # print(self.table_name)
            # print(self._sweep)
            return None

        smoothed_first_derivative = first_derivative.copy()

        for i in range(len(first_derivative)):

            if i < (len(first_derivative) - smoothing_window_length - 1):

                # print(first_derivative[i])
                # print(first_derivative[i:i+smoothing_window_length])

                smoothed_val = np.mean(first_derivative[i:i + smoothing_window_length])
            else:
                smoothed_val = np.mean(first_derivative[i - smoothing_window_length:i])

            if math.isnan(smoothed_val):
                print("nan error")

            else:
                smoothed_first_derivative[i] = smoothed_val
        # print("no error")

        smoothed_first_derivative = np.round(smoothed_first_derivative, 2)

        """
        f = open('ap_debug.csv', 'a')

        writer = csv.writer(f)
        writer.writerow(self.time)
        writer.writerow(self.data)
        # writer.writerow(dx)
        # writer.writerow(dy)
        writer.writerow(first_derivative)
        writer.writerow(smoothed_first_derivative)

        """
        # returns a tuple of true values and therefore needs to be taken at pos 0
        threshold_pos_origin = np.where(smoothed_first_derivative >= manual_threshold)[0]

        threshold_pos = None

        for pos in threshold_pos_origin:
            if np.all(smoothed_first_derivative[pos:pos + 2 * smoothing_window_length] > manual_threshold) \
                    or (np.max(self.data[pos:pos + 2 * smoothing_window_length]) == np.max(self.data)):
                # np.polyfit(smoothed_first_derivative[pos:pos+2*smoothing_window_length,1)
                threshold_pos = pos
                break

        # if still none means there was no real AP
        if threshold_pos is None:
            return None

        t_threshold = self.time[threshold_pos]
        v_threshold = self.data[threshold_pos]

        time_to_amplitude = self.time[np.argmax(self.data)]

        amplitude_pos = np.argmax(self.data)

        # delta_amplitude = amplitude - v_threshold

        # get the point of hyperpolarisation which is the first extremum (minimum) after the AP peak
        # therefore get the first zero crossing point after zero crossing point of the AP peak from the first derivate.
        # using numpys where returns a tuple. I want to have the first point in this tuple -> [0][0]
        # ahp_pos = np.where(smoothed_first_derivative[amplitude_pos:]>=0)[0] [0] +  amplitude_pos

        ahp_pos = np.argmax(smoothed_first_derivative[amplitude_pos:] >= 0)

        # double the window to make sure to not miss the minimum due to the smoothing before
        try:
            ahp = np.amin(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)])
        except Exception as e:
            print(e)  # happens if ahp_pos is zero

            return None

        t_ahp = self.time[np.argwhere(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)] == ahp)][0][0]
        t_ahp += time_to_amplitude

        # only run analysis if there is an action potential, otherwise return nan
        if np.max(self.data) > manual_threshold:
            fitting_parameters['AP_Amplitude'] = np.max(self.data)
            fitting_parameters['Threshold_Amplitude'] = self.data[threshold_pos]
            fitting_parameters['AHP_Amplitude'] = np.amin(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)])
            fitting_parameters['t_AHP'] = t_ahp
            fitting_parameters['time_to_ahp'] = \
                self.time[np.argwhere(self.data[amplitude_pos:(amplitude_pos + 2 * ahp_pos)] == ahp)][0][0]
            fitting_parameters['delta_ap_threshold'] = abs(np.max(self.data)) - abs(v_threshold)
            fitting_parameters['max_first_derivate'] = np.max(smoothed_first_derivative)
            # fitting_parameters['time_max_first_derivate'] = self.time[np.argwhere(smoothed_first_derivative == np.max(smoothed_first_derivative))]
            fitting_parameters['min_first_derivate'] = np.min(smoothed_first_derivative)

        #print(fitting_parameters)

        return fitting_parameters

    @classmethod
    def run_late_register_feature(self):
        print("not implemented")

    @classmethod
    def visualize_results(self, parent_widget, canvas, visualization_type):

        ' check if this given analysis id is connected with a result, if not, the concerning Action Potential Fitting id needs to be read from the analysis function table'

        q = f"select * from results where analysis_function_id = \'{parent_widget.analysis_function_id}\'"
        #print(self.database.get_data_from_database(self.database.database, q))

        if not self.database.get_data_from_database(self.database.database, q):
            q = """select analysis_function_id from analysis_functions where analysis_id = (?) and function_name = (?)"""
            apf_id = self.database.get_data_from_database(self.database.database, q,
                                                          [parent_widget.analysis_id, "Action Potential Fitting"])[0][0]

            result_table_list = self.get_list_of_result_tables(parent_widget.analysis_id,
                                                               apf_id)

        else:
            # series which have to be visualized
            result_table_list = self.get_list_of_result_tables(parent_widget.analysis_id,
                                                               parent_widget.analysis_function_id)

            # go through each result table, calculate the mean for each row, add to the correct meta_data_specific data frame

        meta_data_groups = []
        meta_data_specific_df = []

        for table in result_table_list:


            self.database.database.execute(f'select * from {table}')
            query_data_df = self.database.database.fetchdf()
            query_data_df.set_index('Fitting Parameters', inplace =True, drop = True)


            q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                f'specific_result_table_name = \'{table}\'))'

            meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

            # override the upper left plot panel which would not show any result data. By setting to AP Amplitude it
            # will always display amplitude and the function itself does not need to be lte registered anymore

            if parent_widget.analysis_name == "Action Potential Fitting":
                parent_widget.analysis_name = "AP_Amplitude"

            # index has the same name as the function. Will not work if the names differ.
            x_data = np.mean(query_data_df.loc[parent_widget.analysis_name].values)

            if meta_data_group in meta_data_groups:
                specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
                specific_df.insert(0, str(table), x_data, True)
                meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df
            else:
                # add a new meta data group
                meta_data_groups.append(meta_data_group)
                meta_data_specific_df.append(pd.DataFrame({str(table): [x_data]}))

        #print(meta_data_specific_df[0])

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
    def run_late_register_feature(self):

        #print("running late register")

        #self.database.write_analysis_function_name_and_cursor_bounds_to_database('AP_Amplitude', self.series_name, 0, 0)
        #self.database.write_analysis_function_name_and_cursor_bounds_to_database('Threshold_Amplitude', self.series_name, 0, 0)
        #self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_AHP', self.series_name, 0, 0)
        #self.database.write_analysis_function_name_and_cursor_bounds_to_database('time_to_ahp', self.series_name, 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('delta_ap_threshold', self.series_name, 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('min_first_derivate', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('max_first_derivate', self.series_name, 0, 0)


    @classmethod
    def specific_visualisation(self, queried_data, function_analysis_id):
        print("specific result visualization")
        return 0

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

