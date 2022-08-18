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

            print("reading_table")
            print(data_table)
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
                        #print(dataframe)
                        result_data_frame = pd.concat([result_data_frame, dataframe],axis=1)
                        #print(result_data_frame)

            print(result_data_frame)
            # write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table
            result_data_frame['Fitting Parameters'] = result_data_frame.index
            #print(result_data_frame)

            new_specific_result_table_name = self.create_new_specific_result_table_name(self.analysis_function_id,
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
        manual_threshold = 10  # in mV/ms
        smoothing_window_length = 19
        data = np.array(self.data)*1000 # cast to mV
        time = self.time
        dx = np.diff(time)
        dy = np.diff(data)
        first_derivative = dy / dx
        first_derivative = np.array(first_derivative)

        # if all values are 0 it will return
        # whats the usecase ?
        if all(v == 0 for v in first_derivative):
            print("returning None")
            return None

        # very noisy .. therfore use a smoothing filter
        smoothed_first_derivative = first_derivative.copy()

        for i in range(len(first_derivative)):
            if i < (len(first_derivative) - smoothing_window_length - 1):
                smoothed_val = np.mean(first_derivative[i:i + smoothing_window_length])
            else:
                smoothed_val = np.mean(first_derivative[i - smoothing_window_length:i])

            if math.isnan(smoothed_val):
                print("nan error")

            else:
                smoothed_first_derivative[i] = smoothed_val

        smoothed_first_derivative = np.round(smoothed_first_derivative, 2)

        ######## calc threshold #######

        # returns a tuple of true values and therefore needs to be taken at pos 0
        threshold_pos_origin = np.where(smoothed_first_derivative >= manual_threshold)[0]
        max_1st_derivate_pos = np.argwhere(smoothed_first_derivative == np.max(smoothed_first_derivative))[0][0]

        print("max 1st derivate")
        print(max_1st_derivate_pos)
        threshold_pos = None

        for pos in threshold_pos_origin:
            if np.all(smoothed_first_derivative[pos:max_1st_derivate_pos] > manual_threshold):
                # np.polyfit(smoothed_first_derivative[pos:pos+2*smoothing_window_length,1)
                threshold_pos = pos
                break

        print("Threshold")
        print(threshold_pos)

        # if still none means there was no real AP
        if threshold_pos is None:
            print("No Action Potential detected in this sweep")
            return None



        t_threshold = time[threshold_pos]
        v_threshold = data[threshold_pos]

        left_bound = np.argmax(time >= 25)
        print(left_bound)

        v_mem = np.mean(data[0:left_bound - 1])
        print(v_mem)

        ####### calc max amplitude ####

        max_amplitude = np.max(data)
        max_amplitude_pos = np.argmax(data >= max_amplitude)
        t_max_amplitude = time[max_amplitude_pos]

        ###### calc afterhyperpolarization #####

        ahp = np.min(data[max_amplitude_pos:15000])
        ahp_pos = np.argmax(data[max_amplitude_pos:15000] <= ahp) + max_amplitude_pos
        t_ahp = time[ahp_pos]

        ######## first derivate to get repolarization speed ########

        max_1st_derivative_amplitude = np.max(smoothed_first_derivative)
        print(max_1st_derivative_amplitude)
        pos_max_1st_derivative_amplitude = np.argmax(smoothed_first_derivative >= max_1st_derivative_amplitude)
        t_max_1st_derivative_amplitude = time[pos_max_1st_derivative_amplitude]
        data_max_1st = data[pos_max_1st_derivative_amplitude]

        print("max repolarization speed")
        print(max_1st_derivative_amplitude / t_max_1st_derivative_amplitude)

        min_1st_derivative_amplitude = np.min(smoothed_first_derivative)
        pos_min_1st_derivative_amplitude = np.argmax(smoothed_first_derivative <= min_1st_derivative_amplitude)
        t_min_1st_derivative_amplitude = time[pos_min_1st_derivative_amplitude]
        data_min_1st = data[pos_min_1st_derivative_amplitude]

        ##### calc half width #########

        try:
            half_width_amplitude = (max_amplitude - v_threshold) / 2
            left_hw_pos = np.argmax(data >= half_width_amplitude)
            right_hw_pos = np.argmax(data[max_amplitude_pos:15000] <= half_width_amplitude)+ max_amplitude_pos

            time_1st_half_width = time[left_hw_pos]
            time_2nd_half_width = time[right_hw_pos]

            half_width = time_2nd_half_width - time_1st_half_width
            print(half_width)
        except:
            print("Error in half width calculation")
            half_width = np.NAN
            return None

        # only run analysis if there is an action potential, otherwise return nan
        if np.max(data) > manual_threshold:
            fitting_parameters['Vmem [mV]'] = v_mem
            fitting_parameters['Threshold_Amplitude [mV]'] = v_threshold
            fitting_parameters['t_Threshold [ms]'] = t_threshold
            fitting_parameters['delta_t_threshold [ms]'] = t_threshold - 25
            fitting_parameters['passive_repolarization [mV]'] = abs(v_mem) - abs(v_threshold)
            fitting_parameters['AP_Amplitude [mV]'] = max_amplitude
            fitting_parameters['t_AP_Amplitude [ms]'] = t_max_amplitude
            fitting_parameters['delta_ap_threshold [mV]'] = max_amplitude - v_threshold
            fitting_parameters['delta_t_ap_threshold [ms]'] = t_max_amplitude - t_threshold
            fitting_parameters['AHP_Amplitude [mV]'] = ahp
            fitting_parameters['t_AHP [ms]'] = t_ahp
            fitting_parameters['t_threshold_ahp [ms]'] = t_ahp - t_threshold
            fitting_parameters['max_first_derivate [mV/ms]'] = max_1st_derivative_amplitude
            fitting_parameters['t_max_1st_derivative [ms]'] = t_max_1st_derivative_amplitude
            fitting_parameters['min_first_derivate [mV/ms]'] = min_1st_derivative_amplitude
            fitting_parameters['t_min_1st_derivative [ms]'] = t_min_1st_derivative_amplitude
            fitting_parameters['dt t_min-t_max [ms]'] = t_min_1st_derivative_amplitude - t_max_1st_derivative_amplitude
            fitting_parameters['AP_with [ms]'] = half_width

        return fitting_parameters

    @classmethod
    def run_late_register_feature(self):
        print("not implemented")

    @classmethod
    def visualize_results(self, parent_widget, canvas, visualization_type):

        #check if this given analysis id is connected with a result, if not, the concerning
        # Action Potential Fitting id needs to be read from the analysis function table'

        q = f"select * from results where analysis_function_id = \'{parent_widget.analysis_function_id}\'"

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

        print("Plotting")
        print(parent_widget.analysis_name)
        print("total number of Action Potential Result Tables")
        print(len(result_table_list))

        meta_data_groups = []
        meta_data_specific_df = []

        # make the boxplot
        ax = canvas.figure.subplots()

        for table in result_table_list:

            self.database.database.execute(f'select * from {table}')
            query_data_df = self.database.database.fetchdf()
            query_data_df.set_index('Fitting Parameters', inplace =True, drop = True)

            q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                f'specific_result_table_name = \'{table}\'))'

            meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]
            print(meta_data_group)

            # override the upper left plot panel which would not show any result data. By setting to AP Amplitude it
            # will always display amplitude and the function itself does not need to be lte registered anymore

            if parent_widget.analysis_name == "Action Potential Fitting":
                parent_widget.analysis_name = "AP_Amplitude [mV]"

            # index has the same name as the function. Will not work if the names differ.
            try:
                x_data = np.nanmean(query_data_df.loc[parent_widget.analysis_name].values)
                print(x_data)
                print(query_data_df.loc[parent_widget.analysis_name].values)

                if meta_data_group in meta_data_groups:
                    specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
                    specific_df.insert(0, str(table), x_data, True)
                    meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df
                else:
                    # add a new meta data group
                    meta_data_groups.append(meta_data_group)
                    meta_data_specific_df.append(pd.DataFrame({str(table): [x_data]}))

            except Exception as e:
                print("Error occured when calculating numpy mean")
                print(e)
                print(table)
                print(query_data_df)
                #break

        print("meta data specific df")
        print(meta_data_specific_df)

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

        default_colors = ['k', 'b', 'g', 'c','r']

        for patch, color in zip(plot['boxes'], default_colors[0:len(plot['boxes'])]):
            patch.set_facecolor(color)

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        # Put a legend below current axis
        ax.legend(plot['boxes'], custom_labels, loc='center left', bbox_to_anchor=(1, 0.5)) #fancybox=True, shadow=True, ncol=5

        print("filtered boxplot data")
        print(filtered_box_plot_data)
        print(len(filtered_box_plot_data))

        for i in range(1,len(filtered_box_plot_data)+1):
            y = filtered_box_plot_data[i-1]
            # Add some random "jitter" to the x-axis
            x = np.random.normal(i, 0.04, size=len(y))
            ax.plot(x, y, 'r.', alpha=0.8, picker=True)

        def ap_scatter_picker(event):
            ind = event.ind
            print('onpick3 scatter:', ind, x[ind], y[ind])

        canvas.mpl_connect('pick_event', ap_scatter_picker)


        parent_widget.export_data_frame = pd.DataFrame(filtered_box_plot_data)
        parent_widget.export_data_frame = parent_widget.export_data_frame.transpose()
        parent_widget.export_data_frame.columns = meta_data_groups



    @classmethod
    def run_late_register_feature(self):
        """
        late register to make plots for each of these parameters
        @return:
        """
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('Vmem [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('Threshold_Amplitude [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_Threshold [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('delta_t_threshold [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('passive_repolarization [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('AP_Amplitude [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_AP_Amplitude [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('delta_ap_threshold [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('delta_t_ap_threshold [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('AHP_Amplitude [mV]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_AHP [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_threshold_ahp [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('max_first_derivate [mV/ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_max_1st_derivative [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('min_first_derivate [mV/ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('t_min_1st_derivative [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('dt t_min-t_max [ms]', self.series_name,
                                                                                 0, 0)
        self.database.write_analysis_function_name_and_cursor_bounds_to_database('AP_with [ms]', self.series_name,
                                                                                 0, 0)

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

