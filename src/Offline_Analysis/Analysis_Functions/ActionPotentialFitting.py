from unittest import result
import numpy as np
import pandas as pd
import math
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
#from numba import jit

class ActionPotentialFitting(SweepWiseAnalysisTemplate):
    
    plot_type_options = ["Action_Potential_Fitting", "Mean_Action_Potential_Fitting", "PCA-Plot", "Single_AP_Parameter"]
    function_name = "Action_Potential_Fitting"
    data_shape = None
    database = None
    time = None
    
    
    def show_configuration_options(self):
        print("not implemented")

    @classmethod
    def live_data(cls, lower_bound, upper_bound, experiment_name, series_identifier, database_handler,
                  sweep_name=None):
        """
        Will plot 3 points: threshold, max und hyperpolarization, draw bandwith
        @param lower_bound:
        @param upper_bound:
        @param experiment_name:
        @param series_identifier:
        @param database_handler:
        @param sweep_name:
        @return:
        """

        print("live plot of ap fitting")
        data_table_name = database_handler.get_sweep_table_name(experiment_name, series_identifier)
        time = database_handler.get_time_in_ms_of_by_sweep_table_name(data_table_name)
        entire_sweep_table = database_handler.get_entire_sweep_table(data_table_name)

        parameter_list = []

        if sweep_name is not None:
            data = entire_sweep_table.get(sweep_name)
            parameter_list = cls.live_data_single_trace(database_handler,data,data_table_name,sweep_name,time,
                                                         parameter_list)
        else:
            for column in entire_sweep_table:
                print("column is ", column )
                data = entire_sweep_table.get(column)
                parameter_list = cls.live_data_single_trace(database_handler,data,data_table_name,column,time,
                                                             parameter_list)

        return parameter_list


    @classmethod
    def live_data_single_trace(cls,database_handler,data,data_table_name,column,time, parameter_list):
        y_min, y_max = database_handler.get_ymin_from_metadata_by_sweep_table_name(data_table_name, column)
        data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
        manual_threshold = 10  # in mV/ms
        smoothing_window_length = 19
        data = data  * 1000# cast to mV
        dx = np.diff(time)
        dy = np.diff(data)
        first_derivative = dy / dx
        first_derivative = np.array(first_derivative)

        if all(v == 0 for v in first_derivative):
            print("returning None")
            return parameter_list

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
            return parameter_list

        t_threshold = time[threshold_pos]
        v_threshold = data[threshold_pos]
        parameter_list.append((t_threshold,v_threshold/1e9))
        ####### calc max amplitude ####
        max_amplitude = np.max(data)
        max_amplitude_pos = np.argmax(data >= max_amplitude)
        t_max_amplitude = time[max_amplitude_pos]
        print(max_amplitude)
        parameter_list.append((t_max_amplitude, max_amplitude/1e9))

        ###### calc afterhyperpolarization #####

        dev_1_min = np.min(smoothed_first_derivative)
        pos_dev_1_min = np.where(smoothed_first_derivative == dev_1_min)[0][0]
        hyperpol_pos = np.where(smoothed_first_derivative[pos_dev_1_min:len(smoothed_first_derivative)] >= 0)[0][0]
        hyperpol_pos = hyperpol_pos + pos_dev_1_min

        parameter_list.append((time[hyperpol_pos],data[hyperpol_pos]/1e9))

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
            half_width_amplitude = v_threshold + ((max_amplitude - v_threshold) / 2)
            left_hw_pos = np.argmax(data >= half_width_amplitude)
            right_hw_pos = np.argmax(data[max_amplitude_pos:15000] <= half_width_amplitude) + max_amplitude_pos

            time_1st_half_width = time[left_hw_pos]
            time_2nd_half_width = time[right_hw_pos]

            half_width = time_2nd_half_width - time_1st_half_width
            print(half_width)
        except Exception as e:
            print(f"Error in half width calculation {e}")
            half_width = np.NAN
            return None

        x = time[left_hw_pos:right_hw_pos]
        y = []
        for t in x:
            y.append(half_width_amplitude/1e9)
        parameter_list.append((x,y))
        return parameter_list


    @classmethod
    def calculate_results(cls):
        """
        iterate through each single sweep of all not discarded series in the database and save the calculated result
        to a new database table.
        :return:
        """

        # @todo get this from the configuration window
        series_specific_recording_mode = cls.database.get_recording_mode_from_analysis_series_table(cls.series_name)

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
        data_table_names = cls.database.get_sweep_table_names_for_offline_analysis(cls.series_name)
        # set time to non - will be set by the first data frame
        # should assure that the time and bound setting will be only exeuted once since it is the same all the time
        cls.time = None
        cls.upper_bounds = None
        cls.lower_bounds = None

        for data_table in data_table_names:

            print("reading_table")
            print(data_table)
            #
            entire_sweep_table = cls.database.get_entire_sweep_table(data_table)

            key_1 = list(entire_sweep_table.keys())[0]
            if entire_sweep_table[key_1].shape != cls.data_shape:
                cls.data_shape = entire_sweep_table[key_1].shape
                cls.time = cls.database.get_time_in_ms_of_by_sweep_table_name(data_table)
            # calculate the time
            # set the lower bound
            # set the upper bound
            # added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
            # adding the name would increase readibility of the database ut also add a lot of redundant information

            result_data_frame = pd.DataFrame()

            # we should vectorize this
            for column in entire_sweep_table:

                cls.data = entire_sweep_table.get(column)

                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    cls.data = np.interp(cls.data, (cls.data.min(), cls.data.max()), (y_min, y_max))

                res = cls.specific_calculation()

                # res can be none if there is a beat that had no action potential
                if res is not None:
                    #print("result")
                    #print(res)

                    if cslow_normalization:
                        cslow = cls.database.get_cslow_value_for_sweep_table(data_table)
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

            new_specific_result_table_name = cls.create_new_specific_result_table_name(cls.analysis_function_id,
                                                                                        data_table)
            cls.database.update_results_table_with_new_specific_result_table_name(cls.database.analysis_id,
                                                                                   cls.analysis_function_id,
                                                                                   data_table,
                                                                                   new_specific_result_table_name,
                                                                                   result_data_frame)

            # make sure to register all fitting parameters to plotted

            print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')

        cls.run_late_register_feature()

    @classmethod
    def create_new_specific_result_table_name(cls, analysis_function_id, data_table_name):
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        return f"results_analysis_function_{str(analysis_function_id)}_{data_table_name}"
        
    @classmethod
    def specific_calculation(cls, manual_threshold = 10, smoothing_window_length = 19):
        print("running action potential fitting")

        fitting_parameters = {}
        manual_threshold = manual_threshold  # in mV/ms
        smoothing_window_length = smoothing_window_length  # in ms
        data = np.array(cls.data)*1000 # cast to mV
        time = cls.time
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
        smoothed_first_derivative = ActionPotentialFitting.smooth_action_potential(first_derivative, smoothing_window_length)
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

        v_mem = np.mean(data[:left_bound - 1])
        print(v_mem)

        ####### calc max amplitude ####

        max_amplitude = np.max(data)
        max_amplitude_pos = np.argmax(data >= max_amplitude)
        t_max_amplitude = time[max_amplitude_pos]

        ###### calc afterhyperpolarization #####
        dev_1_min = np.min(smoothed_first_derivative)
        pos_dev_1_min = np.where(smoothed_first_derivative == dev_1_min)[0][0]
        hyperpol_pos = np.where(smoothed_first_derivative[pos_dev_1_min:len(smoothed_first_derivative)] >= 0)[0][0]
        hyperpol_pos = hyperpol_pos + pos_dev_1_min


        ahp = data[hyperpol_pos]
        ahp_pos = hyperpol_pos
        t_ahp = time[hyperpol_pos]

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
            half_width_amplitude = v_threshold + ((max_amplitude - v_threshold) / 2)
            left_hw_pos = np.argmax(data >= half_width_amplitude)
            right_hw_pos = np.argmax(data[max_amplitude_pos:15000] <= half_width_amplitude)+ max_amplitude_pos

            time_1st_half_width = time[left_hw_pos]
            time_2nd_half_width = time[right_hw_pos]

            half_width = time_2nd_half_width - time_1st_half_width
            print(half_width)
        except Exception as e:
            print(f"Error in half width calculation the error: {e}")
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

    @staticmethod
    def smooth_action_potential(first_derivative, smoothing_window_length):
        """_summary_

        Args:
            first_derivative (_type_): _description_
            smoothing_window_length (_type_): _description_

        Returns:
            _type_: _description_
        """
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
        return smoothed_first_derivative

 
    @classmethod
    def run_late_register_feature(cls):
        print("not implemented")

    @classmethod
    def visualize_results(cls, parent_widget):

        #check if this given analysis id is connected with a result, if not, the concerning
        # Action Potential Fitting id needs to be read from the analysis function table'

        q = f"select * from results where analysis_function_id = \'{parent_widget.analysis_function_id}\'"

        if not cls.database.get_data_from_database(cls.database.database, q):
            q = """select analysis_function_id from analysis_functions where analysis_id = (?) and function_name = (?)"""
            apf_id = cls.database.get_data_from_database(cls.database.database, q,
                                                          [parent_widget.analysis_id, "Action_Potential_Fitting"])[0][0]

            result_table_list = cls.get_list_of_result_tables(parent_widget.analysis_id,
                                                               apf_id)

        else:
            # series which have to be visualized
            result_table_list = cls.get_list_of_result_tables(parent_widget.analysis_id,
                                                               parent_widget.analysis_function_id)


        # go through each result table, calculate the mean for each row, add to the correct meta_data_specific data frame

        return result_table_list


    @classmethod
    def run_late_register_feature(cls):
        """
        late register to make plots for each of these parameters
        @return:
        """
        print("yoho")
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
        """
    @classmethod
    def specific_visualisation(cls, queried_data, function_analysis_id):
        print("specific result visualization")
        return 0

    @classmethod
    def get_list_of_result_tables(cls, analysis_id, analysis_function_id):
        '''
        reading all specific result table names from the database
        '''


        q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
        result_list = cls.database.get_data_from_database(cls.database.database, q,
                                                           [analysis_id, analysis_function_id])
        #print(analysis_id)
        #print(analysis_function_id)
        #print(q)
        result_list = (list(zip(*result_list))[0])
        return result_list

