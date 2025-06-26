import os
import json
import struct
import pandas as pd
import numpy as np
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from datetime import datetime
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp


class NanionReader(object):

    def __init__(self, file_list:list[str], database:DuckDBDatabaseHandler):
        super().__init__()
        self.database_handler = database    
        self.file_list = file_list # list of json files which were selected by the user 

    def get_experiment_names(self):
        
        detected_rows, detected_cols = -1, -1
        data_table_list = []

        for item in self.file_list:
            if not item.get('selected'):
                continue

            specific_name = item['specific_name']
            full_path = os.path.join(item['path'], item['filename'])
            print(f"Processing file: {specific_name}")

            try:
                with open(full_path, 'r') as file:
                    recording_data = json.load(file)

                # Update column and row info if not yet initialized
                if detected_rows == -1 and detected_cols == -1:
                    detected_cols, detected_rows = self.get_col_row_info(recording_data)
    	        
                    self._initialize_experiments(self.database_handler, detected_cols, detected_rows)
        
                # Verify column and row consistency
                current_cols, current_rows = self.get_col_row_info(recording_data)
                if (current_cols, current_rows) != (detected_cols, detected_rows):
                    raise ValueError("Inconsistent column/row dimensions detected.")

                # Process each well
                for col in range(current_cols):  # actual ColsMeasured
                    for row in range(current_rows):  # actual WP_nRows
                        experiment_name = self._generate_experiment_name(col, row)
                        meta_data = [experiment_name, f"{datetime.now().strftime('%Y%m%d')}_NANION", 
                                     "None", 
                                     "None", 
                                     "None", 
                                     "None", 
                                     "None", 
                                     "None"]
                        data_table_list.append(meta_data)

            except Exception as e:
                print(f"Error processing {full_path}: {e}") 
        meta_data_df = pd.DataFrame(data_table_list, columns=["Experiment_name", "Experiment_label", "Species", "Genotype", "Sex", "Celltype","Condition",
                        "Individuum_id"])
        return meta_data_df

    def read_and_write_data_to_database(self,meta_data_popup:Assign_Meta_Data_PopUp,frontend_loading_animation):

        frontend_loading_animation.make_widget()
        meta_data_group_assignment_list = meta_data_popup.content_model._data.values.tolist()
        for n in meta_data_group_assignment_list:
            print("adding meta data to existing experiment ", n)
            self.database_handler.add_meta_data_group_to_existing_experiment(n)
        meta_data_popup.close()
        self.read_info_from_json()
        frontend_loading_animation.stop_and_close_animation()

    def read_info_from_json(self):
        """
        Reads and processes selected JSON files, extracting relevant information and storing it in the database.
        
        Args:
            file_list (list): A list of dictionaries containing file metadata (e.g., path, filename, specific_name).
            database (DuckDBDatabaseHandler): The database handler instance for storing processed data.

        Raises:
            ValueError: If column and row dimensions are inconsistent across files.
        """
        detected_rows, detected_cols = -1, -1

        for item in self.file_list:
            if not item.get('selected'):
                continue

            specific_name = item['specific_name']
            full_path = os.path.join(item['path'], item['filename'])
            print(f"Processing file: {specific_name}")

            try:
                with open(full_path, 'r') as file:
                    recording_data = json.load(file)

                # Update column and row info if not yet initialized
                if detected_rows == -1 and detected_cols == -1:
                    detected_cols, detected_rows = self.get_col_row_info(recording_data)

                    #self._initialize_experiments(self.database, detected_cols, detected_rows)

                # Verify column and row consistency
                current_cols, current_rows = self.get_col_row_info(recording_data)
                if (current_cols, current_rows) != (detected_cols, detected_rows):
                    raise ValueError("Inconsistent column/row dimensions detected.")

                # Extract and display relevant information
                self._display_recording_info(recording_data, specific_name)

                # Process each well
                for col in range(current_cols):  # actual ColsMeasured
                    for row in range(current_rows):  # actual WP_nRows
                        sweep_df, sweep_meta_data_df, stim_table = self.read_data_from_json(recording_data, full_path, col, row,specific_name)
                        experiment_name = self._generate_experiment_name(col, row)
                        self._store_data(self.database_handler, experiment_name, specific_name, sweep_df, sweep_meta_data_df, stim_table)

            except Exception as e:
                print(f"Error processing {full_path}: {e}")

    def _initialize_experiments(self, database:DuckDBDatabaseHandler, cols, rows):
        """
        Initializes experiments in the database for each well, identified by column and row.
        
        Args:
            database (DuckDBDatabaseHandler): The database handler instance.
            cols (int): Number of columns detected in the JSON data.
            rows (int): Number of rows detected in the JSON data.
        """
        for col in range(cols):
            for row in range(rows):
                well_id = f"{chr(row + 65)}{col + 1}"
                experiment_name = f"{datetime.now().strftime('%Y%m%d')}_{well_id}"
                database.add_experiment_to_experiment_table(experiment_name)
                meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]
                database.add_experiment_to_global_meta_data(-1, meta_data)

    def _display_recording_info(self, recording_data, specific_name):
        """
        Displays relevant recording information from the JSON data.
        
        Args:
            recording_data (dict): The JSON data loaded from the file.
            specific_name (str): The specific name associated with the file being processed.
        
        Raises:
            KeyError: If expected keys are missing in the JSON data.
        """
        try:
            trace_header = recording_data["TraceHeader"]
            dataset_id = recording_data["DatasetIdentifier"]
            print(f"File Name: {dataset_id['DataName']}")
            print(f"ChipLayout Columns: {trace_header['Chiplayout']['WP_nCols']}")
            print(f"ChipLayout Rows: {trace_header['Chiplayout']['WP_nRows']}")
            print(f"Measurement Layout Columns Measured: {trace_header['MeasurementLayout']['ColsMeasured']}")
            print(f"Trace Files: {trace_header['FileInformation']['FileList']}")
            print(f"Content of {specific_name}:")
        except KeyError as e:
            print(f"Missing expected key in recording data: {e}")

    def _store_data(self, database: DuckDBDatabaseHandler, experiment_name, specific_name, sweep_df, sweep_meta_data_df, stim_table):
        """
        Stores extracted sweep and stimulus data into the database.
        
        Args:
            database (DuckDBDatabaseHandler): The database handler instance.
            experiment_name (str): The unique name of the experiment.
            specific_name (str): The specific name associated with the file being processed.
            sweep_df (DataFrame): The data frame containing sweep data.
            stim_table (DataFrame): The data frame containing stimulus table data.
        """
        #@todo: make sure this is never empty - otherwise db entry will fail ! 
        #@todo: make sure, the specific name is unique: eg. IV1 and IV2
        series_identifier = specific_name

        database.add_single_series_to_database(experiment_name, specific_name, series_identifier)
        
        database.add_sweep_df_to_database(experiment_name, series_identifier, sweep_df, sweep_meta_data_df)

        database.create_series_specific_pgf_table(
            stim_table, f"pgf_table_{experiment_name}_{specific_name}", experiment_name, specific_name
        )

    def _generate_experiment_name(self, col, row):
        """
        Generates a unique experiment name based on column and row indices.
        
        Args:
            col (int): The column index.
            row (int): The row index.
        
        Returns:
            str: A unique experiment name in the format YYYYMMDD_ColumnRow.
        """
        well_id = f"{chr(row + 65)}{col + 1}"
        return f"{datetime.now().strftime('%Y%m%d')}_{well_id}"

    def get_col_row_info(self,recording_data):
        nCols =         recording_data["TraceHeader"]["MeasurementLayout"]["nCols"]         # Number of Columns measured
        #WP_nRows =      recording_data["TraceHeader"]["Chiplayout"]["WP_nRows"] 
        nRows = recording_data["CellTable"]["NofCellRows"]            # Chip Information: Number of Rows
        return nCols, nRows
    
    def read_data_from_json(self, recording_data,json_file,well_id_column,well_id_row,specific_name):

        print("reading data from json") 
        time_scaling = recording_data["TraceHeader"].get("TimeScalingIV")
        if time_scaling is None:
            print(f"Warning: 'TimeScalingIV' missing in {json_file}, trying 'TimeScaling' instead.")
            time_scaling = recording_data["TraceHeader"].get("TimeScaling")

        if time_scaling is None:
            print(f"Error: Neither 'TimeScalingIV' nor 'TimeScaling' found in {json_file}. Skipping.")
            return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
        
        I2DScale = time_scaling.get("I2DScale")
        TR_Time = time_scaling.get("TR_Time")

        # Read out all necessary information from JSON file
        DataName =      recording_data["DatasetIdentifier"]["DataName"]
        WP_nCols =      recording_data["TraceHeader"]["Chiplayout"]["WP_nCols"]             # Chip Information: Number of Columns
        WP_nRows =      recording_data["TraceHeader"]["Chiplayout"]["WP_nRows"]             # Chip Information: Number of Rows
        nCols =         recording_data["TraceHeader"]["MeasurementLayout"]["nCols"]         # Number of Columns measured

        ColsMeasured =  recording_data["TraceHeader"]["MeasurementLayout"]["ColsMeasured"]  # Array of Columns measured
        NofSweeps =     recording_data["TraceHeader"]["MeasurementLayout"]["NofSweeps"]     # Number of Sweeps measured
        NofSamples =    recording_data["TraceHeader"]["MeasurementLayout"]["NofSamples"]    # Number of Samplepoints per Sweep
        LeakData =      recording_data["TraceHeader"]["MeasurementLayout"]["Leakdata"]      # Leak Data recorded
        SweepsPerFile = recording_data["TraceHeader"]["FileInformation"]["SweepsPerFile"]   # Number of Samplepoints per Sweep
        TracefileList = recording_data["TraceHeader"]["FileInformation"]["FileList"]        # List of Tracefiles
        voltage_protocol = recording_data["ExperimentConditions"]["VoltageProtocol"]
        #I2DScale =      recording_data["TraceHeader"]["TimeScalingIV"]["I2DScale"]          # Array of I2D Scale Factors for each Well
        #TR_Time =       recording_data["TraceHeader"]["TimeScalingIV"]["TR_Time"]           # Trace Time
        
        recordingMode = "3"
        y_unit = "A"
        x_start = 0
        x_interval = TR_Time[1]-TR_Time[0] # 

        sweep_df = pd.DataFrame(np.zeros((NofSamples, NofSweeps)))
        meta_data_df = pd.DataFrame(np.zeros((5, NofSweeps+1)))
        

        pgf_df = self.convert_voltage_protocol_into_pgf_df(voltage_protocol, specific_name,specific_name, NofSweeps)

        for sweep in range(NofSweeps): #range(0,1): #
            print(f"processing sweep {sweep}")             
            #ColsMeasured,NofSweeps,NofSamples,LeakData,SweepsPerFile,TracefileList)

            # Check for IV Measurements and build the Time and Stimulus Array correctly
            IsIV = True if recording_data.get("TraceHeader", {}).get("TimeScalingIV") is not None else False
            if IsIV:
                Stimulus =      recording_data["TraceHeader"]["TimeScalingIV"]["Stimulus"][sweep]   # Stimulus (per Sweep Different)
            else:
                Stimulus =      recording_data["TraceHeader"]["TimeScaling"]["Stimulus"]            # Stimulus

            # Calculate index of the file that contains the target Sweep and first column index that was measured
            target_file_index = (sweep+1) // SweepsPerFile                                      # Index of the Tracefile to be read
            start_column_index = next((i for i, x in enumerate(ColsMeasured) if x != -1), None) # Index of first column measured

            # Calculate the Bytesize for one Well and Sweep
            DataperWell = NofSamples * LeakData * 2     # Bytesize for one Well (Faktore of 2 bytes 1 Values == 2 Bytes)

            # Calculate the Byte Offset and with this the Position within the Tracefile where starting to Read
            ColumnOffset = DataperWell * WP_nRows       # Byte Offset for whole columns
            SweepOffset = ColumnOffset * nCols          # Byte Offset for one Sweep
            ReadOffset = ((sweep) % SweepsPerFile) * SweepOffset + (well_id_column-start_column_index) * ColumnOffset  + well_id_row * DataperWell  # Target Read Position

            # Select and Read Trace from .dat file
            trace_dir = os.path.dirname(json_file)
            #print(f"dirname {trace_dir}:\n")
            tracefile = os.path.join(trace_dir, TracefileList[target_file_index])

            # Normalize the reconstructed path to the correct format for the OS
            tracefile = os.path.normpath(tracefile)


            #print(f"tracefile {tracefile}:\n")
            with open (tracefile, 'rb') as file:
                file.seek(ReadOffset)                   # Set the Read Offset
                binary_trace = file.read(DataperWell)   # Read all Traceinformation

            # Transform and Split Trace from ByteArray: 2 Bytes make 1 I16. Transform into Double Values with I2D Scale
            full_trace_raw = struct.unpack('<' + 'h' * (len(binary_trace) // 2), binary_trace)          # 2 Bytes make 1 int

            if len(full_trace_raw)>NofSamples:
                I2DScale_Well = I2DScale[(well_id_column-start_column_index) * WP_nRows + well_id_row]
                full_trace = [x*I2DScale_Well for x in full_trace_raw]
                Trace_nonleak = full_trace[0:NofSamples]                    
                Trace_leak = full_trace [NofSamples+1:2*NofSamples] if LeakData == 2 else []
                print(f"successfully processed sweep {sweep}")
            else:
                print("Here was a problem with this particular sweep")
                Trace_nonleak = [0]*NofSamples
            try:
                sweep_df.iloc[:, sweep] = Trace_nonleak
                meta_data_df.iloc[:, sweep] = [recordingMode, y_unit,x_start,x_interval,NofSamples] 

            except Exception as e:
                print("error in concat")
                print(e)

        # make sure the header has the appropriate names - important for downstream processing
        sweep_df.columns = [f"sweep_{i}" for i in range(1, len(sweep_df.columns) + 1)]
        meta_data_df.columns = [f"sweep_{i}" for i in range(1, len(meta_data_df.columns) + 1)]

        meta_data_df.insert(0, "Parameter", ["RecordingMode", "YUnit","XStart","XInterval","DataPoints"])  # Add the parameter column
        meta_data_df = meta_data_df.set_index("Parameter")
        print("returning")
        return sweep_df,meta_data_df,pgf_df
    
    def convert_voltage_protocol_into_pgf_df(self,voltage_protocol,series_name,series_identifier, nof_sweeps):
      
        data_list = []
        for segment in voltage_protocol:
            print(segment)
        
            series_name = series_name
            start_time = 0
            start_segment=0
            segment_class = "CONSTANT"
            sweep_number = nof_sweeps
            node_type ="StimChannel"
            holding_potential=segment['VoltageStart']/1000# # e.g. -0.08 for -80 mV
            duration = segment['Duration ms']/1000# 0.05s == 50 ms
            increment = 0 # e.g. 0.05 for 50 ms
            voltage=segment['VoltageStart']/1000 - segment['VoltageEnd']/1000
            selectd_channel = 0
            series_identifier = series_name
            children_amount = 0
            sine_cycle = None
            sine_amplitude= None
            
            data_list.append(    [series_name,
                                str(start_time),
                                str(start_segment),
                                segment_class,
                                str(sweep_number),
                                node_type,
                                str(holding_potential),
                                str(duration),
                                str(increment),
                                str(voltage),
                                str(selectd_channel),
                                str(series_identifier),
                                str(children_amount),
                                str(sine_cycle),
                                str(sine_amplitude)
                                ])

        #  pgf_df = pd.DataFrame(np.zeros(len(voltage_protocol,15)))    
        return pd.DataFrame(data_list,columns = ["series_name","start_time","start_segment","segment_class",
                                                 "sweep_number","node_type", "holding_potential", "duration", 
                                                 "increment", "voltage", "selected_channel", "series_id", "children_amount",
                                                 "sine_amplitude","sine_cycle"])
    



    def nanion_into_db(self,database):
        experiment_name = "well_id"

        database.add_experiment_to_experiment_table(experiment_name)
        




# Output that can be used for any further analysis
            #   Trace_nonleak:  Trace data without leak correction
            #   Trace_leak:     Leak-Corrected Trace (empty if not recorded)
            #   TR_Time:        Array of Time Values for each Trace (=X-Axis)
            #   Stimulus:       Voltage or Current Stimulus Values (Depending on the Mode)

            # Generate Output
            #print("Experiment Recording: {}".format(DataName))
            #print("Number of Sweeps: {}".format(NofSweeps))
            #print("Well ID: {}".format(chr(well_id_row+65)+ str(well_id_column+1)))
            #print("IV Data: {}".format("Yes" if IsIV else "No"))
            #print("Leak Data recorded: {}".format("Yes" if LeakData==2 else "No"))
            #print("Sample Count: {}".format(NofSamples))

            # Visualize Data in a Plot
            #fig, ax1 = plt.subplots(layout="constrained")
            #ax1.plot(TR_Time, Trace_nonleak, label="Trace")
            #ax2 = ax1.twinx()
            #ax2.plot(TR_Time, Stimulus, color='red', linewidth = 0.5, label="Stimulus")
            # Formatting Plot
            #ax1.set_xlabel("Time in s")
            #ax1.set_ylabel("Trace / (A)")
            #ax2.set_ylabel("Stimulus / (V)")
            #ax1.set_title("Well {} Sweep {} of {}".format((chr(well_id_row+65)+ str(well_id_column+1)), sweep, DataName))
            #formatter = ticker.EngFormatter()
            #ax1.yaxis.set_major_formatter(formatter)
            #ax2.yaxis.set_major_formatter(formatter)
            #Display Plot
            #plt.show()
            
   

        
        
