import numpy as np
import pandas as pd
import math
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
#from numba import jit

class ActionPotentialFitting(SweepWiseAnalysisTemplate):
    
    
    def __init__(self):
        super().__init__()
        self.plot_type_options = ["Action_Potential_Fitting", "Mean_Action_Potential_Fitting", "PCA-Plot", "Single_AP_Parameter"]
        self.function_name = "Action_Potential_Fitting"
    
    def show_configuration_options(self):
        print("not implemented")

    def live_data(self, lower_bound, upper_bound, experiment_name, series_identifier, database_handler,
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
            parameter_list = self.live_data_single_trace(database_handler,data,data_table_name,sweep_name,time,
                                                         parameter_list)
        else:
            for column in entire_sweep_table:
                print("column is ", column )
                data = entire_sweep_table.get(column)
                parameter_list = self.live_data_single_trace(database_handler,data,data_table_name,column,time,
                                                             parameter_list)

        return parameter_list


    def live_data_single_trace(self,database_handler,data,data_table_name,column,time, parameter_list):
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
        #parameter_list.append((t_max_amplitude, max_amplitude/1e9))
        parameter_list.append((t_max_amplitude, max_amplitude/1e3))


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
        agg_table = pd.DataFrame()
        for data_table in data_table_names:
            experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
            # add logger
            entire_sweep_table = self.database.get_entire_sweep_table(data_table)
            experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
            key_1 = list(entire_sweep_table.keys())[0]
            if entire_sweep_table[key_1].shape != self.data_shape:
                self.data_shape = entire_sweep_table[key_1].shape
                self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)
            # calculate the time
            # set the lower bound
            # set the upper bound
            # added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
            # adding the name would increase readibility of the database ut also add a lot of redundant information

            result_data_frame = pd.DataFrame()

            # we should vectorize this
            for column in entire_sweep_table:

                self.data = entire_sweep_table.get(column)

                if series_specific_recording_mode != "Voltage Clamp":
                    y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
                    self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

                res = self.specific_calculation(experiment_name)
                print(res)
                # res can be none if there is a beat that had no action potential
                if res is not None:
                    #print("result")
                    #print(res)

                    # should be in the outer loop not in the inner
                    if cslow_normalization:
                        cslow = self.database.get_cslow_value_for_sweep_table(data_table)
                        res = res / cslow
                        # add logger
                    # get the sweep number
                    sweep_number = column.split("_")
                    sweep_number = int(sweep_number[1])
                    
                    
                    dataframe = pd.DataFrame.from_dict(res, orient='index', columns = [str(sweep_number)]).T
                    #print(dataframe)
                    result_data_frame = pd.concat([result_data_frame, dataframe])
                    
                        #print(result_data_frame)

            # write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table
            #result_data_frame["experiment_name"] = experiment_name
            agg_table = pd.concat([agg_table, result_data_frame])
            #print(result_data_frame)
        print("here is the aggregated table")
        print(agg_table)
        new_specific_result_table_name = self.database.create_new_specific_result_table_name(self.analysis_function_id,
                                                                                    "AP_Fitting")
        self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
                                                                                self.analysis_function_id,
                                                                                data_table,
                                                                                new_specific_result_table_name,
                                                                                agg_table)

        # make sure to register all fitting parameters to plotted

        print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')

        self.run_late_register_feature()

        
    def specific_calculation(self,experiment_name, manual_threshold = 10, smoothing_window_length = 19):
        print("running action potential fitting")

        fitting_parameters = {}
        manual_threshold = manual_threshold  # in mV/ms
        smoothing_window_length = smoothing_window_length  # in ms
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
            fitting_parameters["experiment_name"] = experiment_name
            #fitting_parameters["meta_data"] = experiment_name

            return fitting_parameters

        else:
            return None

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

 
    def run_late_register_feature(self):
        print("not implemented")

    @staticmethod
    def visualize_results(parent_widget, database):

        #check if this given analysis id is connected with a result, if not, the concerning
        # Action Potential Fitting id needs to be read from the analysis function table'

        q = f"select * from results where analysis_function_id = \'{parent_widget.analysis_function_id}\'"

        if not database.get_data_from_database(database.database, q):
            q = """select analysis_function_id from analysis_functions where analysis_id = (?) and function_name = (?)"""
            
            apf_id = database.get_data_from_database(database.database, q,
                                                          [parent_widget.analysis_id, "Action_Potential_Fitting"])[0][0]

            result_table_list = ActionPotentialFitting.get_list_of_result_tables(parent_widget.analysis_id,
                                                               apf_id, database)

        else:
            # series which have to be visualized
            result_table_list = ActionPotentialFitting.get_list_of_result_tables(parent_widget.analysis_id,
                                                               parent_widget.analysis_function_id, database)


        # go through each result table, calculate the mean for each row, add to the correct meta_data_specific data frame

        return result_table_list

    def specific_visualisation(self, queried_data, function_analysis_id):
        print("specific result visualization")
        return 0


