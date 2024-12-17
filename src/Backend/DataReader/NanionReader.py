import os
import json
import struct
import pandas as pd
import numpy as np
from database.DatabaseHandler.data_db import DuckDBDatabaseHandler
from datetime import datetime

class NanionReader(object):

    def __init__(self, file_list:list[str], database:DuckDBDatabaseHandler):
        super().__init__()
        self.database_handler = database
        self.read_info_from_json(file_list,database)

    def read_info_from_json(self, file_list,database:DuckDBDatabaseHandler):
        detected_number_of_rows = -1
        detected_number_of_columns = -1
        
        for item in file_list:
            if item['selected']:
                specific_name = item['specific_name']
                full_path = os.path.join(item['path'], item['filename'])
                print(f"Specific name: {specific_name}")
                
                
                # Load the JSON file content
                try:
                    with open(full_path, 'r') as file:

                        # Read the whole JSON file into the recording-data dictionary
                        #with open(json_file.replace("\\", "/"), 'r') as file:
                        recording_data = json.load(file)

                        #print(recording_data["TraceHeader"]["MeasurementLayout"])

                        # experiment writing must be executed only once
                        if (detected_number_of_columns < 0) & (detected_number_of_rows < 0):   
                            #update the number of columns and rows
                            detected_number_of_columns, detected_number_of_rows = self.get_col_row_info(recording_data)
                            #write all the wells as experiments into the database
                            for well_id_column in range(detected_number_of_columns):#ColsMeasured:
                                for well_id_row in range(detected_number_of_rows): #WP_nRows:
                                    id = chr(well_id_row+65)+ str(well_id_column+1)
                                  

                                    # Get today's date in YYYYMMDD format
                                    todays_date = datetime.now().strftime("%Y%m%d")
                                    experiment_name = todays_date + "_" + id
                                    #print(f"Well ID: {id}")
                                    database.add_experiment_to_experiment_table(experiment_name)
                                    #experiment_label = 'default, all other parameters are none
                                    meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]
                                    #add meta data as the default data indicated with a -1
                                    #database.add_experiment_to_global_meta_data(-1, meta_data)

                                
                        # read and write the series information
                        if (detected_number_of_columns, detected_number_of_rows) != self.get_col_row_info(recording_data):
                            raise Exception("Unequal number of columns and rows detected. Can not proceed.")
                        else: 
                            
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

                            # Print all the relevant information
                            print(f'File Name: {DataName}')
                            print(f'ChipLayout: Columns: {WP_nCols}')
                            print(f'ChipLayout: Rows: {WP_nRows}')
                            print(f'Number of Columns Measured: {nCols}')
                            print(f'Array of Columns Measured: {ColsMeasured}')
                            print(f'Number of Sweeps Measured: {NofSweeps}')
                            print(f'Number of Samplepoints per Sweep: {NofSamples}')
                            print(f'Leak Data Recorded: {LeakData}')
                            print(f'Sweeps Per File: {SweepsPerFile}')
                            print(f'List of Tracefiles: {TracefileList}')        
                            print(f"Content of {specific_name}:\n")


                            for well_id_column in [0]:#ColsMeasured:

                                for well_id_row in range(0,1): #WP_nRows:   

                                    sweep_df, stim_table = self.read_data_from_json(recording_data,full_path,well_id_column,well_id_row)
                                    # adding the series to the database
                                    #series_name = {node_label} and identifier {node_type}
                                    database.add_single_series_to_database(experiment_name, specific_name, "Series")
                                    meta_data = [experiment_name, "default", "None", "None", "None", "None", "None", "None"]
                                    database.add_sweep_df_to_database(experiment_name, self.series_identifier,sweep_df,meta_data)

                                    database.create_series_specific_pgf_table(stim_table,#sliced_pgf_tuple_data_frame,
                                                            "pgf_table_" + experiment_name + "_" + specific_name,
                                                            experiment_name, specific_name)
                
                                    database.add_sweep_df_to_database(experiment_name, self.series_identifier, self.sweep_data_df,
                                                    self.sweep_meta_data_df)


                except Exception as e:
                    print(f"Failed to read {full_path}: {e}")

    def get_col_row_info(self,recording_data):
        nCols =         recording_data["TraceHeader"]["MeasurementLayout"]["nCols"]         # Number of Columns measured
        #WP_nRows =      recording_data["TraceHeader"]["Chiplayout"]["WP_nRows"] 
        nRows = recording_data["CellTable"]["NofCellRows"]            # Chip Information: Number of Rows
        return nCols, nRows
    
    def read_data_from_json(self, recording_data,json_file,well_id_column,well_id_row):
                
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
        
        sweep_df = pd.DataFrame(np.zeros((NofSamples, NofSweeps)))

        for sweep in range(NofSweeps): #range(0,1): #

            #ColsMeasured,NofSweeps,NofSamples,LeakData,SweepsPerFile,TracefileList)

            # Check for IV Measurements and build the Time and Stimulus Array correctly
            IsIV = True if recording_data.get("TraceHeader", {}).get("TimeScalingIV") is not None else False
            if IsIV:
                I2DScale =      recording_data["TraceHeader"]["TimeScalingIV"]["I2DScale"]          # Array of I2D Scale Factors for each Well
                TR_Time =       recording_data["TraceHeader"]["TimeScalingIV"]["TR_Time"]           # Trace Time
                Stimulus =      recording_data["TraceHeader"]["TimeScalingIV"]["Stimulus"][sweep]   # Stimulus (per Sweep Different)
            else:
                I2DScale =      recording_data["TraceHeader"]["TimeScaling"]["I2DScale"]            # Array of I2D Scale Factors for each Well
                TR_Time =       recording_data["TraceHeader"]["TimeScaling"]["TR_Time"]             # Trace Time
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
            print(f"dirname {trace_dir}:\n")
            tracefile = os.path.join(trace_dir, TracefileList[target_file_index])
            print(f"tracefile {tracefile}:\n")
            with open (tracefile, 'rb') as file:
                file.seek(ReadOffset)                   # Set the Read Offset
                binary_trace = file.read(DataperWell)   # Read all Traceinformation

            # Transform and Split Trace from ByteArray: 2 Bytes make 1 I16. Transform into Double Values with I2D Scale
            full_trace_raw = struct.unpack('<' + 'h' * (len(binary_trace) // 2), binary_trace)          # 2 Bytes make 1 int
            I2DScale_Well = I2DScale[(well_id_column-start_column_index) * WP_nRows + well_id_row]
            full_trace = [x*I2DScale_Well for x in full_trace_raw]
            Trace_nonleak = full_trace[0:NofSamples]                    
            Trace_leak = full_trace [NofSamples+1:2*NofSamples] if LeakData == 2 else []

            # Output that can be used for any further analysis
            #   Trace_nonleak:  Trace data without leak correction
            #   Trace_leak:     Leak-Corrected Trace (empty if not recorded)
            #   TR_Time:        Array of Time Values for each Trace (=X-Axis)
            #   Stimulus:       Voltage or Current Stimulus Values (Depending on the Mode)

            # Generate Output
            print("Experiment Recording: {}".format(DataName))
            print("Number of Sweeps: {}".format(NofSweeps))
            print("Well ID: {}".format(chr(well_id_row+65)+ str(well_id_column+1)))
            print("IV Data: {}".format("Yes" if IsIV else "No"))
            print("Leak Data recorded: {}".format("Yes" if LeakData==2 else "No"))
            print("Sample Count: {}".format(NofSamples))

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
            sweep_df.iloc[:, sweep] = Trace_nonleak
        return sweep_df
    def nanion_into_db(self,database):
        experiment_name = "well_id"

        database.add_experiment_to_experiment_table(experiment_name)
        


    	
   

        
        
