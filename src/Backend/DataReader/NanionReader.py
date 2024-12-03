import os
import json
class NanionReader(object):

    def __init__(self, file_list):
        super().__init__()
        self.read_data_from_json(file_list)

    def read_data_from_json(self, file_list):

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

                        print(recording_data["TraceHeader"]["MeasurementLayout"])

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
                except Exception as e:
                    print(f"Failed to read {full_path}: {e}")
