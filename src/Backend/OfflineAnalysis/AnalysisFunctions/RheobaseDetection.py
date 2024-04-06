import numpy as np
import pandas as pd
from natsort import natsorted, ns
from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.SweepWiseAnalysis import SweepWiseAnalysisTemplate
import picologging
class RheobaseDetection(SweepWiseAnalysisTemplate):
    """Analysis Class to detect the minimum current that needs to be injected into a cell to fire action potentials
    :author dz, 13.07.2022
    @todo: revise this class and make it more efficient
    """
    
    def __init__(self):
        super().__init__()
        self.function_name = "Rheobase-Detection"
        self.plot_type_options = ["Rheobase Plot", "Sweep Plot"]
        self.logger = picologging.getLogger(__name__)
        #@todo: we need a way for the user to modify this parameter in the frontend
        self.ap_detection_threshold = 0.01
        self.result_label = "Injected Current"
        self.result_unit = "A"
        # bether not hradcode ?! 
        self.result_unit_prefix = "p"

    def calculate_results(self):  # sourcery skip: low-code-quality
        """
        calculate_results calculates the current that needs to be injected to make the cell fire an action potential
        """
        self.logger.info(f"Running Rheobase Detection for series {self.series_name}")
        self.series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)
        # get the names of all data tables to be evaluated
        data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
        
        # set to None, will be set once and should be equal for all data tables
        self.time = None
        agg_table = pd.DataFrame(columns=["injected_current","rheobase_sweep", "experiment_name","Sweep_table_Name"])

        for table_name in data_table_names:
            result_data_frame = self.find_rheobase(table_name)
            agg_table = pd.concat([agg_table, result_data_frame])
               
        new_specific_result_table_name = self.database.create_new_specific_result_table_name(
                            self.analysis_function_id, "Rheobase_detection")     
        
        # Insert a new column named "label" with value "A" at position 1
        row_number = len(agg_table)
        agg_table.insert(loc=1, column='y_label', value=[self.result_label]*row_number)
        agg_table.insert(loc=2, column='unit_prefix', value=[self.result_unit_prefix]*row_number)
        agg_table.insert(loc=3, column='unit', value=[self.result_unit]*row_number)
       
        
        self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id, 
                                                                                        self.analysis_function_id, 
                                                                                        table_name, 
                                                                                        new_specific_result_table_name, 
                                                                                        agg_table)

    def find_rheobase(self,table_name:str)->pd.DataFrame:
        """
        find_rheobase Returns the current that needs to be injected to evoke the 1st stable action potential


        Args:
            table_name (str): data base table name

        Returns:
            pd.DataFrame: _description_
        """
        #holding_value = None
        experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,table_name)
        
        entire_sweep_table = self.database.get_entire_sweep_table_as_df(table_name)

        key_1 = list(entire_sweep_table.keys())[0]

        if entire_sweep_table[key_1].shape != self.data_shape:
            self.data_shape = entire_sweep_table[key_1].shape
            self.time = self.database.get_time_in_ms_of_by_sweep_table_name(table_name)

        # really if condition needed ? seems to be alsways none ?!
        #if holding_value is None:
            #print(f'requesting holding value for table {table_name}')
            
        increment_value = self.database.get_data_from_recording_specific_pgf_table(table_name, "increment", 1)
        #   holding_value = self.database.get_data_from_recording_specific_pgf_table(table_name, "holding", 0)

        # get the data frame and make sure to sort sweep numbers correctly
        number_of_sweeps = len(entire_sweep_table.columns)
        column_names = list(entire_sweep_table.columns)
        nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
        entire_sweep_table = entire_sweep_table[nat_sorted_columns]

        # analyse by column
        for column in entire_sweep_table:
            sweep_number = column.split("_")
            sweep_number = int(sweep_number[1])
            s0 = self.get_sweep(table_name, entire_sweep_table,sweep_number)

            condition_1 =  np.max(s0) > self.ap_detection_threshold
            condition_2 = sweep_number<=number_of_sweeps-2

            if condition_1 and condition_2:
                # look into the next and next but one sweep to make sure the AP generation is stable, 
                # will be only executed if conditions 1 and 2 have been true
                s1 = self.get_sweep(table_name, entire_sweep_table, sweep_number + 1)
                s2 = self.get_sweep(table_name, entire_sweep_table, sweep_number + 2)

                condition_3 = (np.max(s1) >= self.ap_detection_threshold)
                condition_4 = (np.max(s2) >= self.ap_detection_threshold)

                if condition_3 and condition_4:
                    # get the holding value and the incrementation steps from the pgf data for this series
                    # the HEKA data will be in pA
                    #@todo: what about the abf data ? 
                    injected_current =  (sweep_number - 1) * increment_value * 1000 #* 1000 to convert from nA to pA
                    #rheobase = holding_value*1000 + injected_current

                    #print(f"1st Rheobase detected: {sweep_number}/{number_of_sweeps}")
                    #print(injected_current)
                    #print(increment_value)
                    #print(holding_value)
                    return pd.DataFrame([{"injected_current": injected_current, 
                                          "rheobase_sweep": sweep_number,
                                          "experiment_name": experiment_name, 
                                          "Sweep_table_Name": table_name}])

        
        # per default, none will be returned as 1st Ap param
        #print("no rheobase detected")
        return pd.DataFrame([{  "injected_current": None, 
                                "rheobase_sweep": -1,
                                "experiment_name": experiment_name, 
                                "Sweep_table_Name": table_name}])

                        
    def get_sweep(self,table_name:str,sweep_table:dict,sweep_number_of_interest:int):
        next_sweep = f"sweep_{str(sweep_number_of_interest)}"
        sweep_data = sweep_table.get(next_sweep)
        y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(table_name, next_sweep)
        return np.interp(sweep_data, (sweep_data.min(), sweep_data.max()), (y_min, y_max))


    def specific_calculation(self):
        """this needs to be implemented!!"""
        pass
    
    
    "deprecated ?! DZ, 06.04.2024"
    #def get_max_values_per_sweep_table(self, data_table_names):
    #    # This needs an overhaul!!!
    #    """
    #    Args:
    #        data_table_names (list): list of Rheobase tables per experiment
    #    """
    #    
    #    holding_value = None
    #    agg_table = pd.DataFrame()
    #    for data_table in data_table_names: # got through the data tables
    #        experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
    #        increment = 0
    #        current_list = []
    #        mean_voltage_list = []
    #        series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)
    #        if holding_value is None:
    #            print(f'requesting holding value for table {data_table}')
    #            increment_value = self.database.get_data_from_recording_specific_pgf_table(data_table, "increment", 1)
    #        entire_sweep_table = self.database.get_entire_sweep_table_as_df(data_table)
    #        number_of_sweeps = len(entire_sweep_table.columns)
    #        column_names = list(entire_sweep_table.columns)
    #        nat_sorted_columns = list(natsorted(column_names, key=lambda y: y.lower()))
    #        entire_sweep_table = entire_sweep_table[nat_sorted_columns]

    #        for column in entire_sweep_table:
    #            print(column)
    #            self.data = entire_sweep_table.get(column)
    #            if series_specific_recording_mode != "Voltage Clamp":
    #                y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
    #                self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

    #            mean_voltage_list.append(np.max(self.data))
    #            current_list.append(increment)
    #            increment += increment_value*1000

    #        meaned_rheobase = pd.DataFrame()
    #        meaned_rheobase["current"] = current_list
    #        meaned_rheobase["Result"] = mean_voltage_list
    #        meaned_rheobase["experiment_name"] = experiment_name
    #        agg_table = pd.concat([agg_table, meaned_rheobase])

    #    mean_table_name = self.database.create_new_specific_result_table_name(
    #                    self.analysis_function_id, "Rheobase_detection") + "_max"
        
    #    self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
    #                                                                            self.analysis_function_id,
    #                                                                            data_table, 
    #                                                                            mean_table_name,
    #                                                                            agg_table)