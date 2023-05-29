import duckdb
import os
from pathlib import Path
import datetime


class DuckDBInitializer:
    def __init__(self, logger, data_file: str, in_memory: bool, database_path: str):
        """_summary_
        """
        self.db_file_name = data_file
        self.logger = logger
        self.in_memory = in_memory
        self.database_path: str = database_path
        self.path = str(Path(f'{self.database_path}{self.db_file_name}'))
        self.dir_list = os.listdir(self.database_path)
        self._return_value: bool = False
        self.database = None

    @property
    def return_value(self):
        return self._return_value

    @return_value.setter
    def return_value(self, value: bool):
        if isinstance(value, bool):
            self._return_value = value
        else:
            raise TypeError(f"self._return_value should be of type Bool and not of type {type(value)}")


    def init_database(self):
        # creates a new analysis database and writes the tables or connects to an existing database

        if self.db_file_name in self.dir_list:
            self.connect_database()
        else:
            self.connect_database()
            self.create_database_tables()

        # inserts new analysis id with default username admin
        # TODO implement roles admin, user, etc. ..
        self.analysis_id = self.insert_new_analysis("admin")
        return self.database, self.analysis_id

    def connect_database(self):
        '''Creates a new database or connects to an already existing database. Returns True if a new database has been created,
        returns false if an existing database was connected '''

        self.logger.info("A new database will created. Created and Connected to new database: %s",
                            self.db_file_name)
        print("A new database will created. Created and Connected to new database: %s",
                            self.db_file_name)

        try:
            # self.database = duckdb.connect(database=':memory:', read_only=False)
            if self.in_memory:
                self.database = duckdb.connect(database=':memory:')
                self.logger.info("connection successfull to online_in_memory_database")
            else:
                self.database = duckdb.connect(self.path, read_only=False)
                self.logger.info("connection successfull to offline_database")

        except Exception as e:
            self.logger.error("An error occured during database initialization. Error Message: %s", e)

    def create_database_tables(self):
        '''function to create the tables needed for the default database'''

        # create a unique sequence analoque to auto increment function
        create_unique_offline_analysis_sequence = """CREATE SEQUENCE unique_offline_analysis_sequence;"""
        create_solution_sequence = """CREATE SEQUENCE solution_sequence;"""
        self.database.execute(create_unique_offline_analysis_sequence)
        self.database.execute(create_solution_sequence)

        # create all database tables assuming they do not exist'''

        sql_create_experiment_mapping_table = """  create table experiment_analysis_mapping(
                                        experiment_name text,
                                        analysis_id integer,
                                        UNIQUE (experiment_name, analysis_id)
                                        ); """

        sql_create_series_mapping_table = """  create table series_analysis_mapping(
                                        analysis_id integer,
                                        experiment_name text,
                                        series_identifier text,
                                        series_name text,
                                        renamed_series_name text,
                                        analysis_discarded text,
                                        primary key (analysis_id, experiment_name, series_identifier)
                                        ); """

        sql_create_global_meta_data_table = """CREATE TABLE global_meta_data(
                                        analysis_id integer,
                                        experiment_name text,
                                        experiment_label text,
                                        species text,
                                        genotype text,
                                        sex text,
                                        celltype text,
                                        condition text,
                                        individuum_id text,
                                        primary key (analysis_id, experiment_name)
                                        );"""

        sql_create_offline_analysis_table = """ CREATE TABLE offline_analysis(
                                                analysis_id integer PRIMARY KEY DEFAULT(nextval ('unique_offline_analysis_sequence')),
                                                date_time TIMESTAMP,
                                                user_name TEXT,
                                                selected_meta_data text); """

        sql_create_experiments_table = """CREATE TABLE experiments(
                                               experiment_name text PRIMARY KEY,
                                               labbook_table_name text,
                                               image_directory text
                                           );"""

        sql_create_experiment_series_table = """ CREATE TABLE experiment_series(
                                              experiment_name text,
                                              series_name text,
                                              series_identifier text,
                                              discarded boolean,
                                              primary key (experiment_name,series_identifier),
                                              sweep_table_name text,
                                              meta_data_table_name text,
                                              pgf_data_table_name text,
                                              series_meta_data text
                                              ); """

        sql_create_series_table = """CREATE TABLE analysis_series(
                                                   analysis_series_name text,
                                                   time text,
                                                   recording_mode text,
                                                   analysis_id integer,
                                                   primary key (analysis_series_name, analysis_id)
                                               ); """

        sql_create_filter_table = """ CREATE TABLE filters(
                                        filter_criteria_name text primary key,
                                        lower_threshold float,
                                        upper_threshold float,
                                        analysis_id integer
                                    ); """

        sql_create_analysis_function_table = """ CREATE TABLE analysis_functions(
                                            analysis_function_id integer PRIMARY KEY DEFAULT(NEXTVAL('unique_offline_analysis_sequence')),
                                            function_name text,
                                            lower_bound float,
                                            upper_bound float,
                                            analysis_series_name text,
                                            analysis_id integer,
                                            pgf_segment integer
                                            );"""

        sql_create_results_table = """ CREATE TABLE results(
                                            analysis_id integer,
                                            analysis_function_id integer,
                                            sweep_table_name text,
                                            specific_result_table_name text
                                            ); """

        sql_create_sweep_meta_data_table ="""CREATE TABLE sweep_meta_data(
                                                sweep_name text,
                                                series_identifier text,
                                                experiment_name text,
                                                meta_data text,
                                                primary key (sweep_name,series_identifier, experiment_name)
                                                ); """

        sql_create_selected_meta_data_table = """CREATE TABLE selected_meta_data(
                                                table_name text,
                                                condition_column text,
                                                conditions text,
                                                analysis_function_id integer,
                                                offline_analysis_id integer
                                                );"""

        sql_solutions_table = """CREATE TABLE solution(
                                                solution_id integer PRIMARY KEY DEFAULT(nextval ('solution_sequence')),
                                                solutions text
                                                );"""

        try:
            self.database.execute(sql_create_offline_analysis_table)
            self.database.execute(sql_create_filter_table)
            self.database.execute(sql_create_series_table)
            self.database.execute(sql_create_experiments_table)
            self.database.execute(sql_create_sweep_meta_data_table)
            self.database.execute(sql_create_analysis_function_table)
            self.database.execute(sql_create_results_table)
            self.database.execute(sql_create_experiment_series_table)
            self.database.execute(sql_create_experiment_mapping_table)
            self.database.execute(sql_create_series_mapping_table)
            self.database.execute(sql_create_global_meta_data_table)
            self.database.execute(sql_create_selected_meta_data_table)
            self.database.execute(sql_solutions_table)
            self.logger.info("create_table created all tables successfully")
        except Exception as e:
            self.logger.info("create_tables function failed with error %s", e)


    def insert_new_analysis(self, user_name):
        ''' Insert a new analysis id into the table offline_analysis. ID's are unique by sequence and will not be
        defined manually. Instead, username (role) and date and time of the creation of this new analysis will be
        stored in the database'''

        time_stamp = datetime.datetime.now()
        q = f"insert into offline_analysis (date_time, user_name) values ('{time_stamp}','{user_name}')"
        self.database = self.database.execute(q)
        self.logger.info("Started new Analysis for user %s at time %s", user_name, time_stamp)

        q = """select analysis_id from offline_analysis where date_time = (?) AND user_name = (?) """
        self.analysis_id = self.database.execute(q, (time_stamp, user_name)).fetchall()[0][0]
        self.logger.info("Analysis id for this analysis will be: %s", self.analysis_id)
        return self.analysis_id

    def open_connection(self, read_only = False):
        """ Opens a connection to the database"""
        print("trials to open connection")
        try:
            self.database = duckdb.connect(self.path, read_only=read_only)
            self.logger.debug("opened connection to database %s", self.db_file_name)
            print("succeeded")
            return self.database

        except Exception as e:
            self.logger.error("failed to open connection to database %s with error %s", self.db_file_name, e)
            print("failed")