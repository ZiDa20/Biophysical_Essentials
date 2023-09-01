import duckdb
import pandas as pd
import sys

class ExportOfflineAnalysis:
    # This class should handle the export of a specific offline analysis ID for viewing purposes!
    def __init__(self, database_handler, offline_analysis_id, path) -> None:
        self.database_handler = database_handler
        self.offline_analysis_id = offline_analysis_id
        self.path = path
        self.transfer_list = (
            "experiment_analysis_mapping",
            "series_analysis_mapping",
            "normalization_values",
            "experiments",
            "experiment_series",
            "analysis_series",
            "results",
            "global_meta_data",
            "selected_meta_data",
            "sweep_meta_data",
            "solution"
        )
        self.export_database = None

    def create_new_database(self):
        """_summary_: Creates a new database that self.database_handler.databasetains only information about a specific experiment!
        """
        self.path += f"/offline_analysis_id_{self.offline_analysis_id}.db"
        try:
            if sys.platform != "darwin": # check
                path = self.path.replace("/","\\")
            else:
                path = self.path.replace("\\","/")
            self.export_database = duckdb.connect(path)
            print("Succesfully generated a new database that should handle the export")
        except Exception as e:
            print(f"This did not work out accordingly: {e}")


    def add_tables_to_database(self):

        # get the analysis_series_name from the duckdb database using a certain analysis_id code
        # this should be a export offline analysis id function that can be shared and used with others using the viewer portion!
        # tables from experiment section
        experiment_analysis_mapping = self.database_handler.database.execute(f"SELECT * FROM experiment_analysis_mapping WHERE analysis_id = {self.offline_analysis_id}").fetchdf() # experiment_analysis_mapping_table
        experiments = self.database_handler.database.execute(f"SELECT * FROM experiments WHERE experiment_name IN {tuple(experiment_analysis_mapping['experiment_name'].values)}").fetch_df() # experiment_table
        experiment_series = self.database_handler.database.execute(f"SELECT * FROM experiment_series WHERE experiment_name IN {tuple(experiment_analysis_mapping['experiment_name'].values)}").fetch_df()

        # Analysis Tables
        offline_analysis = self.database_handler.database.execute(f"SELECT * FROM offline_analysis WHERE analysis_id = {self.offline_analysis_id}").fetchdf()
        analysis_series =  self.database_handler.database.execute(f"SELECT * FROM analysis_series WHERE analysis_id = {self.offline_analysis_id}").fetchdf()
        series_analysis_mapping =  self.database_handler.database.execute(f"SELECT * FROM series_analysis_mapping WHERE analysis_id = {self.offline_analysis_id}").fetchdf()
        normalization_values = self.database_handler.database.execute(f"SELECT * FROM normalization_values WHERE offline_analysis_id = {self.offline_analysis_id}").fetchdf()
        solution = self.database_handler.database.execute("SELECT * FROM solution").fetchdf()
        analysis_functions =  self.database_handler.database.execute(f"SELECT * FROM analysis_functions WHERE analysis_id = {self.offline_analysis_id}").fetchdf()
        max_index = max(analysis_functions["analysis_function_id"].tolist())

        self.create_table_offline_analysis(max_index)
        # result table names
        results =  self.database_handler.database.execute(f"SELECT * FROM results WHERE analysis_id = {self.offline_analysis_id}").fetchdf()

        #here we retrieve the selected metadata tables from the analysis
        global_meta_data =  self.database_handler.database.execute(f"SELECT * FROM global_meta_data WHERE experiment_name IN {tuple(experiment_analysis_mapping['experiment_name'].values)}").fetchdf()
        selected_meta_data =  self.database_handler.database.execute(f"SELECT * FROM selected_meta_data WHERE offline_analysis_id = {self.offline_analysis_id}").fetchdf()
        sweep_meta_data =  self.database_handler.database.execute(f"SELECT * FROM sweep_meta_data WHERE experiment_name IN {tuple(experiment_analysis_mapping['experiment_name'].values)}").fetchdf()

        for data in self.transfer_list:
            self.export_database.execute(f"CREATE TABLE {data} AS SELECT * FROM {data}")

        self.export_database.executemany("INSERT INTO offline_analysis (analysis_id, date_time, user_name) VALUES (?, ?, ?)", offline_analysis.iloc[:,:-1].values)
        print(analysis_functions.values.shape)
        self.export_database.executemany("INSERT INTO analysis_functions VALUES (?, ?, ?, ?,?,?,?)", analysis_functions.values)

        self.add_pgf_meta_raw_tables_batch(experiment_series, results)
        self.export_database.close()

    def add_pgf_meta_raw_tables_batch(self, experiment_series, results):
        """_summary_

        Args:
            experiment_series (pd.DataFrame): Holds the experiment series data that also contains information about the pgf table, the meta data table and the raw data
            results (pd.DataFrame): this holds information about the final analyzed dataframes
        """
        table_names = ["sweep_table_name", "meta_data_table_name", "pgf_data_table_name"]
        for name in table_names:
            for table in experiment_series[name]:
                    df_data = self.database_handler.database.execute(f"Select * from {table}").fetchdf()
                    self.export_database.execute(f"CREATE TABLE {table} AS SELECT * FROM df_data")

        for result in results["specific_result_table_name"]:
            df_data = self.database_handler.database.execute(f"Select * from {result}").fetchdf()
            self.export_database.execute(f"CREATE TABLE {result} AS SELECT * FROM df_data")


    def create_table_offline_analysis(self, max_length):

        self.export_database.execute(f"CREATE SEQUENCE unique_offline_analysis_sequence START {self.offline_analysis_id + 1};")
        self.export_database.execute(f"CREATE SEQUENCE analysis_function_sequence START {max_length + 1};")

        sql_create_offline_analysis_table = """ CREATE TABLE offline_analysis(
                                                analysis_id integer PRIMARY KEY DEFAULT(nextval ('unique_offline_analysis_sequence')),
                                                date_time TIMESTAMP,
                                                user_name TEXT,
                                                selected_meta_data text); """

        sql_create_analysis_function_table = """ CREATE TABLE analysis_functions(
                                                analysis_function_id integer PRIMARY KEY DEFAULT(NEXTVAL('analysis_function_sequence')),
                                                function_name text,
                                                lower_bound float,
                                                upper_bound float,
                                                analysis_series_name text,
                                                analysis_id integer,
                                                pgf_segment integer,
                                                );"""

        self.export_database.execute(sql_create_offline_analysis_table)
        self.export_database.execute(sql_create_analysis_function_table)


