import sqlite3
from Offline_Analysis.error_dialog_class import CustomErrorDialog
import duckdb
import os
import datetime
import re
import sys
import DataReader.heka_reader
import numpy as np
import io
import logging
import datetime
#from global_meta_data_table import GlobalMetaDataTable
import re
from pathlib import Path



class DuckDBDatabaseHandler():
    ''' A class to handle all data in a duck db databaPse.
     @date: 23.06.2021, @author dz'''

    def __init__(self, frontend_style):
        #
        self.database = None
        self.database_path = None
        self.analysis_id = None

        # set up the classes for the main tables
        #self.global_meta_data_table = GlobalMetaDataTable(self.database,self.analysis_id)

        # logger settings
        self.logger = logging.getLogger()
        self.frontend_style = frontend_style
        file_handler = logging.FileHandler('../Logs/database_manager.log')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.ERROR)
        self.logger.info('Database Manager Initialized')
        self.duck_db_database = "DUCK_DB"
        self.sq_lite_database = "SQ_Lite"

        # change manually for now .. maybe to be implemented in settings tabs
        self.database_architecture = self.duck_db_database  # you can select between 'DUCK_DB' or 'SQ_LITE
        self.init_database()

    # Database functions
    def init_database(self):
        # creates a new analysis database and writes the tables or connects to an existing database
        if self.create_analysis_database():
            self.create_database_tables()
        
        # inserts new analysis id with default username admin
        # TODO implement roles admin, user, etc. ..
        self.analysis_id = self.insert_new_analysis("admin")

    """---------------------------------------------------"""
    """ General database functions                        """
    """---------------------------------------------------"""

    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)


    def create_analysis_database(self):
        '''Creates a new database or connects to an already existing database. Returns True if a new database has been created,
        returns false if an existing database was connected '''

        if self.database_architecture == self.duck_db_database:
            self.db_file_name = "duck_db_analysis_database.db"
        else:
            self.db_file_name = "analysis_database.db"
            # Converts np.array to TEXT when inserting
            sqlite3.register_adapter(np.ndarray, self.adapt_array)

            # Converts TEXT to np.array when selecting
            sqlite3.register_converter("array", self.convert_array)


        cew = os.path.dirname(os.getcwd())

        dir_list = os.listdir(f"{cew}/src/database/")

        return_val = 0
        if self.db_file_name in dir_list:
            self.logger.info("Established connection to existing database: %s ", self.db_file_name)
            print("Established connection to existing database: ", self.db_file_name)
        else:
            self.logger.info("A new database will created. Created and Connected to new database: %s",
                             self.db_file_name)
            print("A new database will created. Created and Connected to new database: %s",
                             self.db_file_name)
            return_val = 1

        try:
            if self.database_architecture == self.duck_db_database:
                # self.database = duckdb.connect(database=':memory:', read_only=False)
                path = f'{cew}/src/database/{self.db_file_name}'
                if sys.platform != "darwin":
                    path = path.replace("/","\\")
                else:
                    path = path.replace("\\","/")
                self.database = duckdb.connect(path, read_only=False)
                self.logger.info("connection successful")
            else:
                self.database = sqlite3.connect(cew + "\\src\\" + self.db_file_name, detect_types=sqlite3.PARSE_DECLTYPES)
        except Exception as e:
            self.logger.error("An error occured during database initialization. Error Message: %s", e)

        return return_val != 0

    def create_database_tables(self):
        '''function to create the tables needed for the default database'''

        # create a unique sequence analoque to auto increment function
        create_unique_offline_analysis_sequence = """CREATE SEQUENCE unique_offline_analysis_sequence;"""
        self.database = self.execute_sql_command(self.database, create_unique_offline_analysis_sequence)

        # create all database tables assuming they do not exist'''

        sql_create_mapping_table = """  create table experiment_analysis_mapping(
                                        experiment_name text,
                                        analysis_id integer,
                                        UNIQUE (experiment_name, analysis_id) 
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
                                            analysis_id integer
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

        try:
            self.database = self.execute_sql_command(self.database, sql_create_offline_analysis_table)
            self.database = self.execute_sql_command(self.database, sql_create_filter_table)
            self.database = self.execute_sql_command(self.database, sql_create_series_table)
            self.database = self.execute_sql_command(self.database, sql_create_experiments_table)
            self.database = self.execute_sql_command(self.database, sql_create_sweep_meta_data_table)
            self.database = self.execute_sql_command(self.database, sql_create_analysis_function_table)
            self.database = self.execute_sql_command(self.database, sql_create_results_table)
            self.database = self.execute_sql_command(self.database, sql_create_experiment_series_table)
            self.database = self.execute_sql_command(self.database, sql_create_mapping_table)
            self.database = self.execute_sql_command(self.database, sql_create_global_meta_data_table)
            self.database = self.execute_sql_command(self.database, sql_create_selected_meta_data_table)

            self.logger.info("create_table created all tables successfully")
        except Exception as e:
            self.logger.info("create_tables function failed with error %s", e)

    # @todo refactor to write to database
    def execute_sql_command(self, database, sql_command, values=None):
        try:
            if values:
                database.execute(sql_command, values)
                # self.logger.info("Execute SQL Command: %s with values %s", sql_command,values)
            else:
                database.execute(sql_command)
                # self.logger.info("Execute SQL Command: %s without values", sql_command)
            database.commit()
            return database
        except Exception as e:
            print(e)
            self.logger.error("Error in Execute SQL Command: %s", e)
            raise Exception(e)
            
    def get_data_from_database(self, database, sql_command, values=None, fetch_mode=None):
        try:
            if values:
                database.execute(sql_command, values)
            else:
                database.execute(sql_command)
            if fetch_mode is None:
                return database.fetchall()
            if fetch_mode == 1:
                return database.fetchnumpy()
            if fetch_mode == 2:
                return database.fetchdf()
        except Exception as e:
            print(e)


    def open_connection(self, read_only = False):
        """ Opens a connection to the database"""
        print("trials to open connection")
        try:
            cew = os.path.dirname(os.getcwd())
            path = self.database_path or str(Path(f'{cew}/src/database/{self.db_file_name}'))
            self.database = duckdb.connect(path, read_only=read_only)
            self.logger.debug("opened connection to database %s", self.db_file_name)
            print("succeeded")

        except Exception as e:
            self.database.close()
            self.open_connection()
            self.logger.error("failed to open connection to database %s with error %s", self.db_file_name, e)
            print("failed")

    """--------------------------------------------------------------"""
    """ Functions to interact with table experiment_analysis_mapping """
    """--------------------------------------------------------------"""

    def create_mapping_between_experiments_and_analysis_id(self, experiment_id):
        q = f'insert into experiment_analysis_mapping values (?,?)'
        try:
            self.database = self.execute_sql_command(self.database, q, (experiment_id, self.analysis_id))
            self.logger.info("Mapped experiment %s to analysis %i", experiment_id, self.analysis_id)
        except Exception as e:
            self.logger.info("Mapping between experiment %s and analysis %i FAILED", experiment_id, self.analysis_id)

    """---------------------------------------------------"""
    """ Functions to interact with table offline_analysis """
    """---------------------------------------------------"""

    def insert_new_analysis(self, user_name):
        ''' Insert a new analysis id into the table offline_analysis. ID's are unique by sequence and will not be
        defined manually. Instead, username (role) and date and time of the creation of this new analysis will be
        stored in the database'''

        time_stamp = datetime.datetime.now()
        q = f"insert into offline_analysis (date_time, user_name) values ('{time_stamp}','{user_name}')"
        self.database = self.execute_sql_command(self.database, q)
        self.logger.info("Started new Analysis for user %s at time %s", user_name, time_stamp)

        q = """select analysis_id from offline_analysis where date_time = (?) AND user_name = (?) """
        self.analysis_id = self.get_data_from_database(self.database, q, (time_stamp, user_name))[0][0]
        self.logger.info("Analysis id for this analysis will be: %s", self.analysis_id)
        return self.analysis_id

    """---------------------------------------------------"""
    """    Functions to interact with table filters       """
    """---------------------------------------------------"""

    def write_filter_into_database(self, filter_name, lower_threshold, upper_threshold):
        q = """ insert into filters values (?,?,?,?)"""
        self.database = self.execute_sql_command(self.database, q,
                                                 (filter_name, lower_threshold, upper_threshold, self.analysis_id))

    """---------------------------------------------------"""
    """    Functions to interact with table analysis_series     """
    """---------------------------------------------------"""

    def write_analysis_series_types_to_database(self, name_list):
        '''Takes the user selected series types (e.g. block pulse, iv, ...) and places them in the referring database
        table "series"
        @date: 23.06.2021, @author: dz '''

        for n in name_list:
            # query the recording mode
            recording_mode = self.query_recording_mode(n)

            q = """insert into analysis_series (analysis_series_name, recording_mode, analysis_id) values (?,?,?) """

            try:
                self.database = self.execute_sql_command(self.database, q, (n, recording_mode, self.analysis_id))
                self.logger.info(f'inserting new analysis_series with id  {self.analysis_id}')
            except Exception as e:
                self.logger.info(f'ERROR while inserting new analysis_series with id  {self.analysis_id}')

        self.logger.info("inserted all series")

    def query_recording_mode(self, series_name):
        """
        Get the recording mode from the meta data table of a (by-name-) specified series
        :param series_name:
        :return: str Voltage Clamp or Current Clamp
        """
        print(str(series_name))
        print(self.analysis_id)

        if isinstance(series_name,tuple):
            series_name = series_name[0]

        print(str(series_name))

        q = """select experiment_name from experiment_series where series_name=(?) intersect
        (select experiment_name from experiment_analysis_mapping where analysis_id = (?))"""
        experiment_names_list = self.get_data_from_database(self.database, q, (series_name, self.analysis_id))

        print(experiment_names_list)

        q = """ select meta_data_table_name from experiment_series where experiment_name = (?) and series_name = (?)"""
        self.logger.info(f'select meta_data_table_name from experiment_series where experiment_name = \"{experiment_names_list[0][0]}\" and series_name = \"{series_name}\" ')
        name = self.get_data_from_database(self.database, q, (experiment_names_list[0][0], series_name))[0][0]

        q = f'SELECT Parameter, sweep_1 FROM {name}'
        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        x = str(meta_data_dict.get('RecordingMode'))
        print("recording mode: for this shit!!!!!!!!!!!!!!!!! " + x)
        if int(x) == 3:
            return "Voltage Clamp"
        else:
            return "Current Clamp"

    # deprecated dz 22.02.2022
    def write_ms_spaced_time_array_to_analysis_series_table(self, time_np_array, analysis_series_name, analysis_id):
        """

        :param time_np_array: time in milliseconds already converted into numpy array
        :return:
        """
        q = 'update analysis_series set time = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.execute_sql_command(self.database, q, (time_np_array, analysis_series_name, analysis_id))

    def write_recording_mode_to_analysis_series_table(self, recording_mode, analysis_series_name, analysis_id):
        q = 'update analysis_series set recording_mode = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.execute_sql_command(self.database, q, (recording_mode, analysis_series_name, analysis_id))

    def get_recording_mode_from_analysis_series_table(self, analysis_series_name):
        """
        returns the recording mode as string Voltage Clamp or Current Clamp
        :param analysis_series_name:
        :param analysis_id:
        :return:
        """
        q = """select recording_mode from analysis_series where analysis_series_name = (?) AND analysis_id = (?)"""
        return self.get_data_from_database(self.database, q, (analysis_series_name, self.analysis_id))[0][0]

    def get_time_in_ms_of_by_sweep_table_name(self,sweep_table_name):
        """

        :param sweep_table_name:
        :return:
        :author: dz, 29.06.2022
        """
        q = f'select meta_data_table_name from experiment_series where sweep_table_name = \'{sweep_table_name}\' '
        meta_data_table_name = self.get_data_from_database(self.database, q)[0][0]

        # calculated time again as in plot widget manager
        q = f'SELECT Parameter, sweep_1 FROM {meta_data_table_name}'

        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        x_start = float(meta_data_dict.get('XStart'))
        x_interval = float(meta_data_dict.get('XInterval'))
        number_of_datapoints = int(meta_data_dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    # used dz 29.06.2022#
    def get_time_in_ms_of_analyzed_series(self, experiment_name, series_identifier):

        # get the related meta data table name from the first experiment in the list
        q = """select meta_data_table_name from experiment_series where experiment_name = (?) AND series_name = (?)"""
        res = self.get_data_from_database(self.database, q, (experiment_name, series_identifier))[0][0]

        # calculated time again as in plot widget manager
        q = f'SELECT Parameter, sweep_1 FROM {res}'

        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        x_start = float(meta_data_dict.get('XStart'))
        x_interval = float(meta_data_dict.get('XInterval'))
        number_of_datapoints = int(meta_data_dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def get_ymin_from_metadata_by_sweep_table_name(self,table_name,sweep):
        """

        :param table_name:
        :param sweep: e.g. sweep_1 (str)
        :return:
        :author dz, 21.06.2022
        """
        q = f'select meta_data_table_name from experiment_series where sweep_table_name = \'{table_name}\''
        r = self.get_data_from_database(self.database, q)[0][0]

        q = f'SELECT Parameter, {sweep} FROM {r}'

        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        y_min = float(meta_data_dict.get('Ymin'))
        y_max = float(meta_data_dict.get('Ymax'))

        return y_min,y_max

    def get_sweep_table_names_for_offline_analysis(self, series_name, meta = None):
        '''
        returns table names for all with this analysis linked experiments containing a given series name
        :param series_name:  name of the series (e.g. Block Pulse, .. )
        :return: a list of sweep table names
        '''
        # returns a list of tuples
        if meta:
            experiment_names = self.get_experiments_by_series_name_and_analysis_id_with_meta(series_name, meta)
        else:
            experiment_names = self.get_experiments_by_series_name_and_analysis_id(series_name)
        sweep_table_names = []

        for experiment_tuple in experiment_names:
            # get the related meta data table name from the first experiment in the list
            if meta:
                q = f'select sweep_table_name from experiment_series where experiment_name = (?) AND series_name = (?) AND discarded = (?) AND series_meta_data = (?)'
                try:
                    r = self.get_data_from_database(self.database, q, (experiment_tuple[0], series_name, False, meta))[0][0]
                    sweep_table_names.append(r)
                except Exception as e:
                    self.logger.error(f"Error in get_sweep_table_names_for_offline_analysis: {e}")
            else:
                q = f'select sweep_table_name from experiment_series where experiment_name = (?) AND series_name = (?) AND discarded = (?)'
                try:
                    r = self.get_data_from_database(self.database, q, (experiment_tuple[0], series_name, False))[0][0]
                    sweep_table_names.append(r)
                except Exception as e:
                    self.logger.error(f"Error in get_sweep_table_names_for_offline_analysis: {e}")

        return sweep_table_names

    def get_experiments_by_series_name_and_analysis_id(self, series_name):
        '''
        Find experiments of the current analysis containing the series specified by the series name.
        :param series_name: name of the series (e.g. Block Pulse, .. )
        :return: list of tuples of experimentnames (e.g. [(experiment_1,),(experiment_2,)]
        '''
        q = """select experiment_name from experiment_analysis_mapping where analysis_id = (?) intersect (select experiment_name from experiment_series where series_name = (?))"""
        res = self.get_data_from_database(self.database, q, (self.analysis_id, series_name))
        # res = self.get_data_from_database(self.database, q, (self.analysis_id))
        return res
    
    def get_experiments_by_series_name_and_analysis_id_with_meta(self, series_name, meta_data):
        '''
        Find experiments of the current analysis containing the series specified by the series name.
        :param series_name: name of the series (e.g. Block Pulse, .. )
        :param meta_data associated 
        :return: list of tuples of experimentnames (e.g. [(experiment_1,),(experiment_2,)]
        '''
        q = """select experiment_name from experiment_analysis_mapping where analysis_id = (?) intersect (select experiment_name from experiment_series where series_name = (?) AND series_meta_data = (?))"""
        res = self.get_data_from_database(self.database, q, (self.analysis_id, series_name, meta_data))
        # res = self.get_data_from_database(self.database, q, (self.analysis_id))
        return res

    def get_sweep_table_name(self, experiment_name, series_identifier):
        '''
        returns the sweep table name for a given experiment and series name
        :param experiment_name:
        :param series_name:
        :return:
        '''
        q = f'select sweep_table_name from experiment_series where experiment_name = \'{experiment_name}\' AND series_identifier = \'{series_identifier}\''
        print("hello", q)
        res = self.database.execute(q).fetchdf()

        return res["sweep_table_name"].tolist()[0]

    def get_entire_sweep_table(self, table_name):
        '''
        Fetches all sweeps in a sweep table.
        :param table_name:
        :return: the table as dict {column: numpy_array(data ... )]}
        '''
        try:
            return self.database.execute(f'select * from {table_name}').fetchnumpy()
        except Exception as e:
            print(table_name)
            return None

    def get_entire_sweep_table_as_df(self, table_name):
        '''
        Fetches all sweeps in a sweep table.
        :param table_name:
        :return: the table as dict {column: numpy_array(data ... )]}
        '''
        try:
            return self.database.execute(f'select * from {table_name}').fetchdf()
        except Exception as e:
            print(table_name)
            return None
    """---------------------------------------------------"""
    """    Functions to interact with table global_meta_data    """
    """---------------------------------------------------"""

    def add_experiment_to_global_meta_data(self, id, meta_data):
        q = f'insert into global_meta_data (analysis_id,experiment_name, experiment_label, species, genotype, sex, celltype, condition, individuum_id) values ' \
            f'({id},\'{meta_data[0]}\',\'{meta_data[1]}\',\'{meta_data[2]}\',\'{meta_data[3]}\',\'{meta_data[4]}\',\'{meta_data[5]}\',\'{meta_data[6]}\' ,\'{meta_data[7]}\')'
        try:
            self.database = self.execute_sql_command(self.database, q)
            self.logger.info(meta_data[0], "added succesfully to global_meta_data")
            return 1
        except Exception as e:
            if "Constraint Error" in str(e):
                self.logger.info(
                    "Experiment with name %s was already in global meta data")
            else:
                print("adding experiment to global meta data failed")

    def get_available_experiment_label(self):
        """
        return all available label in the database
        @return: a tuple list
        """
        q = f'select distinct experiment_label from global_meta_data'
        res = self.get_data_from_database(self.database, q)
        return res

    def get_meta_data_group_of_specific_experiment(self, experiment_name):
        """
        :param experiment_name:
        :return:
        :author dz, 28.06.2022
        """
        q = f'select condition from global_meta_data where experiment_name = \'{experiment_name}\''
        return self.get_data_from_database(self.database, q)[0][0]

    def add_meta_data_group_to_existing_experiment(self, meta_data_list: list):
        """
        Insert meta data group into an exsiting experiment
        :param meta_data_list: [0]: experiment_name, [1]: experiment_label, [2] = species, [3] = ...
        :return:
        """
        print(meta_data_list)
        q = f'update global_meta_data set experiment_label = \'{meta_data_list[1]}\',' \
            f'species = \'{meta_data_list[2]}\', genotype = \'{meta_data_list[3]}\', sex = \'{meta_data_list[4]}\', celltype = \'{meta_data_list[5]}\', condition = \'{meta_data_list[6]}\',individuum_id = \'{meta_data_list[7]}\' '\
            f'where experiment_name = \'{meta_data_list[0]}\''
        try:
            self.database = self.execute_sql_command(self.database, q)
            self.logger.info(f'Wrote meta data for experiment \'{meta_data_list[0]}\' into database"')
            res = self.database.execute("select * from global_meta_data where experiment_name = \'{meta_data_list[0]}\' ").fetchdf()
            res_II = self.database.execute("select * from global_meta_data").fetchdf()
            return True
        except Exception as e:
            print(e)
            self.logger.info(f'FAILED to write meta data for experiment \'{meta_data_list[0]}\' into database with error {str(e)}')
            return False

    def get_meta_data_of_multiple_experiments(self):
        """
        @todo DZ add description .. implemented during load finished analysis
        @return:
        """
        q = f'select experiment_name from global_meta_data intersect (select experiment_name from experiment_analysis_mapping where analysis_id = {self.analysis_id})'
        experiment_names = self.get_data_from_database(self.database, q)

        meta_data = []
        for name in experiment_names:
            q= f'select condition from global_meta_data where experiment_name = \'{name[0]}\''
            meta_data.append(self.database.execute(q).fetchall()[0][0])

        return meta_data

    def get_analysis_id_specific_global_meta_data_table_part(self):

        q = f'select * from global_meta_data where experiment_name in (select experiment_name from ' \
            f'experiment_analysis_mapping where analysis_id = {self.analysis_id})'

        return self.database.execute(q).fetchdf()

    """---------------------------------------------------"""
    """    Functions to interact with table experiments    """
    """---------------------------------------------------"""

    def add_experiment_to_experiment_table(self, experiment_name):
        '''
        Adding a new experiment to the database table 'experiments'. Name-Duplicates (e.g. 211224_01) are NOT allowed-
        the experiment name of the already existing experiment will added to the current offline analysis mapping table.
        This is a measure to keep the performance of the db high and the related tables (== db storage size) small.
        TODO Add frontend popup/information/anything to notify the user about this performed procedure

        :param name:
        :param meta_data_group:
        :param series_name:
        :param mapping_id:
        :return 0: experiment was not added because it already exists, 1 it was added sucessfully, -1 something went wrong
        '''
        self.logger.info("adding experiment %s to_experiment_table", experiment_name)
        q = f'insert into experiments (experiment_name) values (\'{experiment_name}\')'

        try:
            self.database = self.execute_sql_command(self.database, q)
            self.logger.info(f'added experiment {experiment_name} succesfully to experiment table)')
            return 1
        except Exception as e:
            if "Constraint Error" in str(e):
                self.logger.info(
                    "Experiment with name %s was already registered in the database and was ot overwritten The experiment will be added to the mapping table.",
                    experiment_name)
                return 0
            else:
                print("adding experiment failed")
                print(e)
                self.logger.info("failed adding expseriment %s with error %s", experiment_name, e)
                return -1




    """---------------------------------------------------"""
    """    Functions to interact with table experiment_series    """
    """---------------------------------------------------"""

    def get_distinct_meta_data_groups_for_specific_experiment_label(self,label_list):
        meta_data_groups = []
        for label in label_list:
             q = f'select distinct condition from global_meta_data where experiment_label = \'{label}\''
             tmp_lst = self.get_data_from_database(self.database, q)
             meta_data_groups += tmp_lst
        return meta_data_groups

    def get_meta_data_table_of_specific_series(self, experiment_name:str, series_identifier: str):
        """
        :param experiment_name:
        :param series_name:
        :return:
        :author: dz, 29.06.2022
        """
        q = """select meta_data_table_name from experiment_series where experiment_name = (?) and series_identifier = (?)"""
        return self.return_requested_table(q, experiment_name, series_identifier)

    def get_sweep_table_for_specific_series(self, experiment_name: str, series_identifier: str):
        """
        Returns sweep_data_table for one specific series in an experiment identified by experiment name and series identifier
        :param experiment_name:
        :param series_identifier:
        :return: data table as pandas data frame
        :author: dz, 27.06.2022
        """

        q = """select sweep_table_name from experiment_series where experiment_name = (?) and series_identifier = (?)"""
        return self.return_requested_table(q,experiment_name,series_identifier)

    def return_requested_table(self, q: str, experiment_name: str, series_identifier: str):
        """
        internal function to reduce code copy. returns a requested table as data frame
        :param q:
        :param experiment_name:
        :param series_identifier:
        :return: pandas df
        """
        data_table_name = self.get_data_from_database(self.database, q, (experiment_name, series_identifier))[0][0]

        return self.database.execute(f'SELECT * FROM {data_table_name}').fetchdf()

    def get_experiment_name_for_given_sweep_table_name(self,sweep_table_name):
        """
        Get's the name of the experiment for a given sweep table name
        :param sweep_table_name: string of the name
        :return:
         :authored: dz, 29.04.2022
        """
        q = f'select experiment_name from experiment_series where sweep_table_name = \'{sweep_table_name}\''
        return self.get_data_from_database(self.database, q)[0][0]

    def get_cslow_value_for_sweep_table(self, series_name):
        '''
        get the cslow value for a specific sweep
        :param series_name: name of the sweep table in the database
        :return:
        :authored: dz, 29.04.2022
        '''

        # get meta data table name where experiment series = series_name
        # get cslow value from this specific meta data table name

        q = f'select meta_data_table_name from experiment_series where sweep_table_name = \'{series_name}\''
        # should return a list with only one tuple where the  key = meta data table name
        meta_data_table_name = self.get_data_from_database(self.database, q)[0][0]
        q = f'SELECT Parameter, sweep_1 FROM {meta_data_table_name}'
        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        return float(meta_data_dict.get('CSlow'))

    def add_single_series_to_database(self, experiment_name, series_name, series_identifier):
        self.logger.info(
            "Inserting series name %s with series identifier %s of experiment %s to experiment_series table",
            series_name, series_identifier, experiment_name)
        try:
            q = """insert into experiment_series(experiment_name, series_name, series_identifier,discarded,series_meta_data) values (?,?,?,?,?) """
            self.database = self.execute_sql_command(self.database, q,
                                                     (experiment_name, series_name, series_identifier, 0,"None"))
            # 0 indicates not discarded
            self.logger.info("insertion finished succesfully")
            print("insertion finished succesfully")
        except Exception as e:
            self.logger.info("insertion finished FAILED because of error %s", e)
            print("insertion finished FAILED because of error %s", e)

    def get_experiment_names_by_experiment_label(self,experiment_label,meta_data_list):
        """
        :param experiment_label:
        :return:
        :author: dz, 27.06.2022
        """

        for i in meta_data_list:
            print("meta data list = ", meta_data_list)
            if meta_data_list.index(i)==0:
                q = f'select experiment_name from global_meta_data where condition = \'' + i + '\''
            else:
                q+= ' or condition = \'' + i + '\''

        print(q)
        r2 = self.get_data_from_database(self.database, q)
        print(r2)
        #q = f'select experiment_name from experiments where experiment_label = \'{experiment_label}\' '
        #q = f"""select experiment_label from experiments where experiment_name = \' {201229_01} \' """
        #r = self.get_data_from_database(self.database,q)

        experiment_names = []
        for i in r2:
            experiment_names.append(i[0])

        return experiment_names

    def get_series_names_of_specific_experiment(self,experiment_name,discarded):
        """
        
        :param experiment_name:
        :return: a list of tuples [(series_name, series_identifier), ... ] e.g. [('Block Pulse', 'Series1'), ('IV','Series2'), .. ]
        :author: dz, 22.06.2022
        """
        q = f'select series_name, series_identifier from experiment_series where experiment_name = \'{experiment_name}\' and discarded = \'{discarded}\''
        r = self.get_data_from_database(self.database,q)
        return r

    """----------------------------------------------------------"""
    """    Functions to interact with table analysis_functions   """
    """----------------------------------------------------------"""

    def get_analysis_function_name_from_id(self,analysis_function_id):
        q= f'select function_name from analysis_functions where analysis_function_id = {analysis_function_id}'
        r = self.get_data_from_database(self.database, q)
        return r[0][0]

    def get_analysis_series_name_by_analysis_function_id(self,analysis_function_id):
        q = f'select analysis_series_name from analysis_functions where analysis_function_id = {analysis_function_id}'
        r = self.get_data_from_database(self.database, q)
        return r[0][0]

    def write_analysis_function_name_and_cursor_bounds_to_database(self, analysis_function, analysis_series_name,
                                                                   lower_bound, upper_bound):
        try:
            q = """insert into analysis_functions (function_name, analysis_series_name, analysis_id,lower_bound,upper_bound) values (?,?,?,?,?)"""
            self.database = self.execute_sql_command(self.database, q, (
            analysis_function, analysis_series_name, self.analysis_id, lower_bound, upper_bound))
            self.logger.info(
                f'added new row into analysis_function_table: {analysis_function}, {analysis_series_name},{self.analysis_id},{lower_bound},{upper_bound}')
        except:
            print("error")

    def get_last_inserted_analysis_function_id(self):
        q = """select analysis_function_id from analysis_functions """
        id_list = self.get_data_from_database(self.database, q)
        print("greatest identifier is: ", max(id_list)[0])
        return max(id_list)[0]

    def get_series_specific_analysis_functions(self, series_name):
        """
        get analysis function name and analysis function id that is linked offline analysis id
        :param series_name:
        :return: returns a tuple of analysis name, analysis_function_id
        """
        try:
            q = """ select function_name, analysis_function_id from analysis_functions where analysis_series_name = (?) AND analysis_id = (?) """
            return self.get_data_from_database(self.database, q, (series_name, self.analysis_id))
        except Exception as e:
            self.logger.error(f'error in get_series_specific_analysis_functions: {e}')
            return None

    def get_cursor_bounds_of_analysis_function(self, analysis_function_id, series_name):
        """
        Returns a list triples (lower, upper bound, id) for the specified analysis function name and the analysis id.
        :param function_name: name of the analysis function (e.g. min, max, .. )
        :param series_name: name of the analysis series (e.g. Block Pulse, ... )
        :return: a list of cursor bound triples, with cursor bound values at positions 0 and 1 and thed
        function analysis id at the third position
        """

        q = """select lower_bound, upper_bound from analysis_functions where analysis_function_id = (?) AND analysis_series_name=(?) AND analysis_id = (?)"""
        r = self.get_data_from_database(self.database, q, (analysis_function_id, series_name, self.analysis_id))

        return r

    def get_analysis_functions_for_specific_series(self,series_name):
        print(series_name)
        q = f'select function_name from analysis_functions where analysis_id = {self.analysis_id} and analysis_series_name=\'{series_name}\''
        return self.database.execute(q).fetchall()

    """----------------------------------------------------------"""
    """    Functions to interact with table sweeps   """
    """----------------------------------------------------------
    """

    def get_single_sweep_data_from_database_by_sweep_id(self, sweep_id):
        q = f'select data_array from sweeps where sweep_id = \"{sweep_id}\"'
        return self.get_data_from_database(self.database, q)[0][0]

    def get_sweep_meta_data(self, datalist, pos):
        """ write dictionary to array in database """

        data = datalist[pos + 1][2][0]
        data = list(data.items())

        return np.array(data)

    def write_analysis_function_to_database(self, function_list, series_type):
        for f in function_list:
            sql_command = """INSERT INTO analysis_functions (function_name,series_type) VALUES (?,?) """
            self.database = self.execute_sql_command(self.database, sql_command, (f, series_type))

    def get_sweep_parent(self, datalist, pos):
        ''' returns experiment name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''
        return self.find_node_type(datalist, pos, "Group", 1)

    def get_series_identifier(self, datalist, pos):
        ''' returns series identifier name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        return self.find_node_type(datalist, pos, "Series", 0)

    def find_node_type(self, datalist, pos, type, elem):
        '''type: internal helper_function, author: dz, 15.06.21 '''
        for d in range(pos, -1, -1):
            if type in datalist[d][0]:
                return datalist[d][elem]

    def get_sweep_number(self, sweep_name):
        '''get the sweep number out of a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        splitted_string = re.match(r"([a-z]+)([0-9]+)", sweep_name, re.I)
        res = splitted_string.groups()
        return (res[1])

    def write_coursor_bounds_to_database(self, lower_value, upper_value, series_name):
        '''adds the two 2 incoming values to all functions in the table.'''

        # from database: get the number of selected analysis functions
        q1 = """ SELECT function_name FROM analysis_functions """
        r1 = self.get_data_from_database(self.database, q1)
        q2 = """ select distinct function_name from analysis_functions """
        r2 = self.get_data_from_database(self.database, q2)
        zero = -1

        if len(r2) == len(r1):
            non_zero_bound = """ select lower_coursor from analysis_functions where function_name= (?)"""
            values = (r2[0][0])
            zero = self.execute_sql_command(self.database, non_zero_bound, values)

        if len(r2) > len(r1) or zero:
            for d in r2:
                q = """insert into analysis_functions(function_name,lower_coursor,upper_coursor) values (?,?,?)"""
                values = (d, lower_value, upper_value)
                self.database = self.execute_sql_command(self.database, q, values)
        else:
            q = """update analysis_functions set lower_coursor=(?), upper_coursor=(?) where function_name = (?) """
            for d in r2:
                values = (lower_value, upper_value, d[0])
                self.database = self.execute_sql_command(self.database, q, values)

        # from database: check if coursor bounds are empty (only when less then 2 duplicates available)

    def get_analysis_series_names_for_specific_analysis_id(self):

        q= f'select analysis_series_name from analysis_series where analysis_id = {self.analysis_id}'
        return self.database.execute(q).fetchall()


    def calculate_single_series_results_and_write_to_database(self, series_type):
        q = f'select s.sweep_id, s.data_array from  sweeps s inner join experiments e on  s.experiment_name = e.experiment_name AND e.series_name = \"{series_type}\";'  # [sweep_id, sweep_data_trace]
        sweeps = self.get_data_from_database(self.database, q)

        q = f'select id,function_name,lower_coursor,upper_coursor from analysis_functions where series_type = \"{series_type}\";'  # [anlysis_id,analysis_function,lower_bound,upper_bound]
        analysis_functions = self.get_data_from_database(self.database, q)

        q = f'select time from analysis_series where analysis_series_name = \"{series_type}\";'
        time = self.get_data_from_database(self.database, q)
        time = self.convert_string_to_array(time[0][0])

        for s in sweeps:
            data = self.convert_string_to_array(s[1])
            raw_analysis_class_object = ra.AnalysisRaw(time, data)

            for a in analysis_functions:
                raw_analysis_class_object.lower_bounds = a[2]
                raw_analysis_class_object.upper_bounds = a[3]

                raw_analysis_class_object.construct_trace()
                raw_analysis_class_object.slice_trace()

                res = raw_analysis_class_object.call_function_by_string_name(a[1])

                q = """ insert into results values (?,?,?) """
                self.write_result_to_database(a[0], s[0], res)

    def write_result_to_database(self, analysis_function_id, table_name, sweep_number, result_value):

        q = """insert into results values (?,?,?,?,?) """
        self.database = self.execute_sql_command(self.database, q, (
        self.analysis_id, analysis_function_id, table_name, sweep_number, result_value))

    # Still used ?
    def read_trace_data_and_write_to_database(self, series_type, data_path):
        ''' function to read data arrays of each sweep and write it to the sweeps table in the database, arrays are represented as strings'''

        q = f'SELECT experiment_name FROM experiments WHERE series_name = \"{series_type}\";'
        file_names = self.get_data_from_database(self.database, q)

        q = f'select time from analysis_series where analysis_series_name = \"{series_type}\";'
        time = self.get_data_from_database(self.database, q)

        for f in file_names:
            q = f'select series_identifier,sweep_number,sweep_id from sweeps where experiment_name = \"{f[0]}\";'
            sweeps = self.get_data_from_database(self.database, q)
            file_path = data_path + "/" + f[0]
            bundle = heka_reader.Bundle(file_path)
            for s in sweeps:
                series_name = s[0]
                sweep_number = s[1]
                series_number = self.get_sweep_number(
                    series_name)  # it's just the name of the function that is a little bit confusing - function is doing the right thing
                data_array = bundle.data[[0, int(series_number) - 1, int(sweep_number) - 1, 0]]

                # when the first data are entered, time will be set once for all sweeps of the sweep table
                # before this type of time is None
                if time is None:
                    time = np.linspace(0, len(data_array) - 1, len(data_array))
                    string_time = self.convert_array_to_string(time)

                    q = """update analysis_series set time = (?) where analysis_series_name = (?);"""
                    self.database = self.execute_sql_command(self.database, q, (string_time, series_type))

                # convert data array into comma separated string
                data_array = self.convert_array_to_string(data_array)

                q = """update sweeps set data_array = (?) where sweep_id = (?);"""
                self.database = self.execute_sql_command(self.database, q, (data_array, s[2]))

    def read_series_type_specific_analysis_functions_from_database(self, series_name):
        q = f'select distinct function_name from analysis_functions where series_type = \"{series_name}\" '
        res_string = self.get_data_from_database(self.database, q)
        string_list = []
        for t in res_string:
            string_list.append(t[0])
        return string_list

    def convert_string_to_array(self, array_as_string):
        sub_res = array_as_string.split(",")
        int_array = []
        for s in sub_res:
            int_array.append(float(s))

        return int_array

    def convert_array_to_string(self, data_array):
        output_string = ""
        for d in data_array:
            if output_string == "":
                output_string = str(d)
            else:
                output_string = output_string + "," + str(d)

        return output_string

    def add_sweep_df_to_database(self,experiment_name, series_identifier,data_df,meta_data_df, dat = True):
        try:
            
            #print(data_df)
            imon_trace_signal_table_name = self.create_imon_signal_table_name(experiment_name, series_identifier)

            # requires a little bit of different handling

            column_names = data_df.columns.tolist()
            part_1 = f'create table {imon_trace_signal_table_name} ('
            query_str = ""
            for c in range(0,len(column_names)):
                if c == len(column_names)-1:
                    part_1 = part_1 + column_names[c] + " " + "float"
                    query_str = query_str + column_names[c]
                else:
                    part_1 = part_1 + column_names[c] + " " + "float,"
                    query_str = query_str + column_names[c] + ","

            part_1 = part_1 + ")"

            print(part_1)
            print(query_str)
            try:
                self.database.execute(part_1)
                self.database.query(f'INSERT INTO {imon_trace_signal_table_name} SELECT {query_str} FROM data_df')

            except Exception as e:
                print(e)

            """
            try:
                self.database.register('df_data', data_df)
                print("registered succesfully")
            except Exception as e:
                print("register failed")

            try:
                self.database.execute(f'CREATE TABLE {imon_trace_signal_table_name} AS SELECT * FROM df_data')
                print("created tablr succesfully")
            except Exception as e:
                print("create table failed")
            
            """

            try:
                q = """update experiment_series set sweep_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
                self.execute_sql_command(self.database, q, (imon_trace_signal_table_name, experiment_name, series_identifier))
            except Exception as e:
                print("update table failed")

            print("added data df successfully")

            imon_trace_meta_data_table_name = self.create_imon_meta_data_table_name(experiment_name, series_identifier)

            column_names  = meta_data_df.columns.tolist()
            #print(column_names)
            meta_data_df = meta_data_df.reset_index()
            meta_data_df.columns = ['Parameter'] + column_names
            print("till here everything is fine and good")
            print(meta_data_df)

            '''@todo (dz, 17.08.2022): this hardcoded bugfix allows the use of duck db pre dev 0.4.1.dev1603.
            Max and I  encountered a bug with big data loading - this bug only solves when using duckdb > 0.4.0
            in dev 0.4.1.dev1603 somehow tinyint-> blob is not implemented yet. 
            therefore i have replaced all the meta data encoded as b'\x00' with their hexadecimal representation 
            '''

            if dat:
                affected_rows = [10,11,12,13,33]

                for r in affected_rows:
                    print("val")
                    print(meta_data_df['sweep_1'].iloc[r])
                    print(type(meta_data_df['sweep_1'].iloc[r]))

                    replace_val = int.from_bytes(meta_data_df['sweep_1'].iloc[r], "big")
                    print(replace_val)
                    for c in column_names:
                        meta_data_df[c].iloc[r]= replace_val

            print(meta_data_df)

            print("adding meta data --- ")

            try:
                self.database.register('meta_data_df', meta_data_df)
            except Exception as e:
                print("meta data register failed")

            try:
                self.database.execute(f'CREATE TABLE {imon_trace_meta_data_table_name} AS SELECT * FROM meta_data_df')
            except Exception as e:
                print(e)
                print("meta data create table failed")

            print("added meta data df successfully")

            q = """update experiment_series set meta_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
            self.execute_sql_command(self.database, q,
                                     (imon_trace_meta_data_table_name, experiment_name, series_identifier))


            self.logger.info("Successfully created both df tables of series %s in experiment %s", series_identifier, experiment_name)



        except Exception as e:
            print("add_sweep_df_to_database failed")
            print(e)



    def create_imon_signal_table_name(self, experiment_name, series_identifier):
        '''
        Creates unique names of database tables for i_mon sweep data. It's an extra function so multiple functions can access this naming convention.
        :param experiment_name: text representation of the experiment name
        :param series_identifier: text representation of the series identifier (e.g. Series1)
        :return: table name as string
        '''
        return 'imon_signal_' + experiment_name + '_' + series_identifier

    def create_imon_meta_data_table_name(self, experiment_name, series_identifier):
        '''
        Creates unique names of i_mon meta data database tables. It's an extra function so multiple functions can access this naming convention.
        :param experiment_name: text representation of the experiment name
        :param series_identifier: text representation of the series identifier (e.g. Series1)
        :return: table name as string
        '''
        return 'imon_meta_data_' + experiment_name + '_' + series_identifier



    def get_single_sweep_meta_data_from_database(self, data_array):
        '''
        Requests all meta data from a specific sweep in the database
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: meta data dictionary
        '''

        return self.get_single_sweep_values_according_to_parameter(data_array, 'meta_data')

    def get_single_sweep_data_from_database(self, data_array):
        """
        Requests a specific sweep trace from the database
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: data array (numpy array)
        """

        return self.get_single_sweep_values_according_to_parameter(data_array, 'trace_signal')

    def get_single_sweep_values_according_to_parameter(self, data_array, param):
        '''
        Requests different sweep data regarding the selected param.
        :param data_array: data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :param param: 'trace_signal' or 'meta_data'
        :return: in case of 'trace_signal' -> numpy array, when 'meta_data' -> dict
        '''

        # declaration not necessary - just here to improve readability
        experiment_name = data_array[0]
        series_identifier = data_array[1]
        sweep_number = data_array[2]

        # step 1:  get the name of the sweep table for this series: calling the name generator function,
        # a database request would be possible too but might be more time consuming
        column_name = 'sweep_' + str(sweep_number)

        if param == 'trace_signal':
            sweep_table_name = self.create_imon_signal_table_name(experiment_name, series_identifier)
            q = f'SELECT {column_name} FROM {sweep_table_name}'
            # query fetches a dict - only values needed, key == column name == not needed == will not be returned
            # cast to list needed before one can access the numpy array at position 0
            return list(self.database.execute(q).fetchnumpy().values())[0]

        else:
            sweep_table_name = self.create_imon_meta_data_table_name(experiment_name, series_identifier)
            q = f'SELECT Parameter, {column_name} FROM {sweep_table_name}'
            # returns a dict {'key':'value', 'key':'value',...} where keys will be parameter names
            return {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

    def discard_specific_series(self, experiment_name, series_identifier):
        """Change the column valid for a specifc series from 0 (valid) to 1 (discarded, in-valid)"""
        print("initial tree is calling discard button function with params", experiment_name, series_identifier)
        self.change_experiment_series_discarded_state(experiment_name, series_identifier, 1)

    def reinsert_specific_series(self, experiment_name, series_identifier):
        self.change_experiment_series_discarded_state(experiment_name, series_identifier, 0)

    def change_experiment_series_discarded_state(self, experiment_name, series_identifier, state):
        q = """update experiment_series set discarded = (?) where experiment_name = (?) AND series_identifier = (?);"""
        res = self.execute_sql_command(self.database, q, (state, experiment_name, series_identifier))

    def get_distinct_non_discarded_series_names(self):
        """
        get all distinct series names from experiments mapped with the current analysis id
        :return:
        """

        print("distinct_result = ", self.database.execute('select distinct series_name from experiment_series where discarded = False').fetchdf())
        print(self.analysis_id)
        q1 = f'select distinct series_name from experiment_series where discarded = False and experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.analysis_id})'

        q = f'select distinct exp.series_name from experiment_series exp inner join experiment_analysis_mapping map ' \
            f'on exp.experiment_name = map.experiment_name where map.analysis_id = \'{self.analysis_id}\' and exp.discarded = False'



        return self.get_data_from_database(self.database, q1)

    '''-------------------------------------------------------'''
    '''     create series specific pgf trace table            '''
    '''-------------------------------------------------------'''

    def create_series_specific_pgf_table (self, data_frame, pgf_table_name,experiment_name, series_identifier):
        """ adds new pgf table to the database        """
        self.database.register('df_1', data_frame)
       

        try:
            # create a new sweep table
            self.database.execute(f'create table {pgf_table_name} as select * from df_1')

            try:
                # update the series table by inserting the newly created pgf table name
                q = """update experiment_series set pgf_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""

                self.execute_sql_command(self.database, q, (pgf_table_name, experiment_name, series_identifier))

                self.logger.info("Successfully created %s table of series %s in experiment %s", pgf_table_name,
                                 series_identifier, experiment_name)

            except Exception as e:
                print(e)
                self.logger.error("Update Series table failed with error %s", e)

        except Exception as e:
            print(e)
            self.logger.error("Error::Couldn't create a new table with error %s", e)

    def get_entire_pgf_table_by_experiment_name_and_series_identifier(self,experiment_name, series_identifier):
        """
        Get the correct pgf table
        @param experiment_name:
        @param series_identifier:
        @return:
        """

        q = """select pgf_data_table_name from experiment_series where experiment_name = (?) and series_identifier = (?)"""
        pgf_table_name = self.get_data_from_database(self.database, q, [experiment_name,series_identifier])[0][0]

        self.database.execute(f'SELECT * FROM {pgf_table_name}')
        return self.database.fetchdf()

    def get_entire_pgf_table(self,data_table_name):
        """
        Query the enitre pgf table as dataframe as pandas data frame
        :param data_table_name:
        :return:
        """
        q = """select pgf_data_table_name from experiment_series where sweep_table_name = (?)"""
        pgf_table_name = self.get_data_from_database(self.database, q, [data_table_name])[0][0]

        self.database.execute(f'SELECT * FROM {pgf_table_name}')
        return self.database.fetchdf()

    def get_data_from_recording_specific_pgf_table(self,table_name,data_name,segment_number):
        q = f'select pgf_data_table_name from experiment_series where sweep_table_name = \'{table_name}\''
        pgf_table_names = self.get_data_from_database(self.database, q)

        pgf_table_name = pgf_table_names[0][0]

        val = None
        if data_name == 'holding':
            q = f'SELECT holding_potential FROM {pgf_table_name}'
            val = self.get_data_from_database(self.database, q)[segment_number][0]

        if data_name == 'increment':
            q = f'SELECT increment FROM {pgf_table_name}'
            val = self.get_data_from_database(self.database, q)[segment_number][0]

        # cast string and return as float value
        return float(val)


    def get_data_from_pgf_table(self,series_name,data_name,segment_number):
        """
        reads pgf information from the database and returns the requested floa value of the specified segment
        :param series_name:
        :param data_name: 'holding', 'increment'
        :param segment_number: int nubmer of the segment, first = 0
        :return:
        :author: dz, 21.06.2022
        """
        # @todo also check for the correct offline analysis id and only select these exoeriemnts?
        experiment_names = self.get_experiments_by_series_name_and_analysis_id(series_name)

        # take the first element, get the pgf_table_name, extract holding and
        experiment_name = experiment_names[0][0]


        q = """select pgf_data_table_name from experiment_series where experiment_name = (?) and series_name = (?) """
        pgf_table_names = self.get_data_from_database(self.database, q, (experiment_name, series_name))

        pgf_table_name = pgf_table_names[0][0]

        val = None
        if data_name == 'holding':
            q = f'SELECT holding_potential FROM {pgf_table_name}'
            val = self.get_data_from_database(self.database, q)[segment_number][0]

        if data_name == 'increment':
            q = f'SELECT increment FROM {pgf_table_name}'
            val = self.get_data_from_database(self.database, q)[segment_number][0]


        # cast string and return as float value
        return float(val)
    
    def get_pgf_file_selection(self,current_tab, pgf_selection):

        """Should retrieve the pgf_files for all the files in the current analysis id
        This should further retrieve each individual segment,
        pgf_selection: combobox that holds the inital segments"""
        analysis_id = self.analysis_id
        series_name = current_tab.objectName()
        experiment_name = self.database.execute(f"SELECT experiment_name FROM experiment_analysis_mapping WHERE analysis_id = {analysis_id};").fetchall()
        pgf_file_dict = {}
        for experiment in experiment_name:
            try:
                q = """select pgf_data_table_name from experiment_series where experiment_name = (?) and series_name = (?)"""
                pgf_sections = self.get_data_from_database(self.database, q, [experiment[0], series_name])[0][0]
                pgf_table = self.database.execute(f"SELECT * FROM {pgf_sections}").fetchdf()
                print(pgf_table.info)
                pgf_table = pgf_table[pgf_table["selected_channel"] == "1"] # this should be change to an input from the user if necessary
                pgf_file_dict[experiment[0]] = (pgf_table, pgf_table.shape[0])

            except IndexError:
                print(f"The error is at the experiment: {experiment[0]}")
                continue

        pgf_files_amount = {pgf_index[1] for pgf_index in pgf_file_dict.values()}

        if len(pgf_files_amount) <= 1:
            for i in range(1, int(list(pgf_files_amount)[0])+1):
                pgf_selection.addItem(f"Segment {i}")

        else:
            CustomErrorDialog("The number of segments is not the same for all experiments. Please check your data.", self.frontend_style)

        print(pgf_file_dict)

    '''-------------------------------------------------------'''
    '''     interaction with  table resutls       '''
    '''-------------------------------------------------------'''
    def update_results_table_with_new_specific_result_table_name(self, analysis_id,  function_analysis_id,
                                                             data_table_name, new_specific_result_table_name, result_data_frame):

        """
        creates a specific result data frame and stores it in the database and also updates result overview table
        :param analysis_id:
        :param function_analysis_id:
        :param data_table_name:
        :param new_specific_result_table_name:
        :param result_data_frame:
        :return:
        """
        self.database.register('df_1', result_data_frame)
        q = """insert into  results values (?,?,?,?) """ #set specific_result_table_name = (?) where analysis_id = (?) and analysis_function_id = (?) and sweep_table_name = (?) """

        try:
            # create a new sweep table
            self.database.execute(f'create table {new_specific_result_table_name} as select * from df_1')

            self.execute_sql_command(self.database, q, (analysis_id, function_analysis_id,data_table_name,new_specific_result_table_name))

            self.logger.info("Successfully created %s table of %s for analysis_function_id %d", new_specific_result_table_name,
                             data_table_name, function_analysis_id)
        except Exception as e:
            print("error")
            print(e)
    ###### deprecated ######

    # @todo deprecated ?
    def fill_database_from_treeview_list(self, data_list, series_type):
        ''' Function to read the list which was created to built the treeview in the frontend - this data list will be reused and
          it's data will be stored into the experiments or sweep table in the database.
          Furthermore the recording mode of the series type will be extracted and will be stored in the series table in
          column recording mode @date 23.06.2021, @author dz '''

        q = f'select recording_mode from series where name=\"{series_type}\"'
        rec_mode = self.get_data_from_database(self.database, q)

        # to avoid second insertation: once the rec mode was written, data have been also inserted at least once

        test = rec_mode[0]
        if rec_mode[0][0] is None:

            for d in data_list:
                if "Group" in d[0]:
                    sql_command = """INSERT INTO experiments VALUES (?,?,?)"""
                    values = (d[1], "control", series_type)
                    self.database = self.execute_sql_command(self.database, sql_command, values)

                if "Sweep" in d[0]:
                    experiment_number = self.get_sweep_parent(data_list, data_list.index(d))
                    meta_data = self.get_sweep_meta_data(data_list, data_list.index(d))

                    trace_rec_mode = str(data_list[data_list.index(d) + 1][2][0].get_fields()["RecordingMode"])
                    if rec_mode[0][0] is None:
                        q = f'update series set recording_mode = (?) where name = (?)'

                        print("found recording mode")
                        print(trace_rec_mode)

                        if trace_rec_mode == 3:
                            values = ("Voltage Clamp", series_type)
                            rec_mode[0] = ("Voltage Clamp",)
                        else:
                            values = ("Current Clamp", series_type)
                            rec_mode[0] = ("Current Clamp",)

                        self.database = self.execute_sql_command(self.database, q, values)

                    series_identifier = self.get_series_identifier(data_list, data_list.index(d))
                    sweep_number = self.get_sweep_number(d[0])

                    sql_command = "insert into sweeps (experiment_name,series_identifier,sweep_number,meta_data) values(?,?,?,?);"
                    values = (experiment_number, series_identifier, sweep_number, meta_data)

                    self.database = self.execute_sql_command(self.database, sql_command, values)

    def retrieve_selected_meta_data_list(self):
        meta_string = str(self.database.execute(f"Select selected_meta_data from offline_analysis WHERE analysis_id = {self.analysis_id}").fetchall())
        return [meta_string]

    def get_selected_meta_data(self, analysis_function_id = None):
        # get the meta data table that is stored in the database
		# if no meta data were assigned the name will be "None" which needs to be catched as an exception
        try:
            if analysis_function_id:
                q = f'select * from selected_meta_data where offline_analysis_id = {self.analysis_id} AND analysis_function_id = {analysis_function_id}'
            else:
                 q = f'select * from selected_meta_data where offline_analysis_id = {self.analysis_id} AND analysis_function_id = -1'
            selected_meta_data = self.get_data_from_database(self.database, q, fetch_mode = 2)["condition_column"].tolist()
            return selected_meta_data
        except Exception as e:
            print(e)
            if e == np.nan:
                print("Error: No meta data found")
                return None
            
    

        """ @deprecated dz 27.07.2022
        def add_single_sweep_to_database(self, experiment_name, series_identifier, sweep_number, meta_data, data_array):
        
         function to insert a new data array and related meta data information into the database
         :param experiment_name:
         :param series_identifier:
         :param sweep_number:
         :param meta_data:
         :param data_array:
         :return:
    

        self.logger.info("Adding sweep %s of series %s of experiment %s into database", str(sweep_number),
                         series_identifier, experiment_name)

        # create table names
        imon_trace_signal_table_name = self.create_imon_signal_table_name(experiment_name, series_identifier)
        imon_trace_meta_data_table_name = self.create_imon_meta_data_table_name(experiment_name, series_identifier)

        # @TODO extend for leakage currents also
        # @TODO add sweep meta data information anyhow. For now only meta data information of the imon trace will be stored.

        data_array_df = pd.DataFrame({'sweep_' + str(sweep_number): data_array})

        # get the meta data from the imon trace
        child_node = meta_data[0]
        child_node_ordered_dict = dict(child_node.get_fields())

        meta_data_df = pd.DataFrame.from_dict(data=child_node_ordered_dict, orient='index', columns=[sweep_number])

        if sweep_number == 1:
            print("creating and inserting new data table")
            # create one new table with all imon signal traces of each sweep of one
            # specific series (e.g. block pulse or iv)
            self.create_and_insert_into_new_trace_table(imon_trace_signal_table_name, data_array_df, experiment_name,
                                                        series_identifier, "data_array")

            print("creating and inserting new meta table")
            # create one new table with all imon trace meta data information of each imon trace
            # within one specific series (e.g. block pulse or iv)
            meta_data_df = pd.DataFrame(list(child_node_ordered_dict.items()), columns=('Parameter', 'sweep_1'))
            self.create_and_insert_into_new_trace_table(imon_trace_meta_data_table_name, meta_data_df, experiment_name,
                                                        series_identifier, "meta_data")

        else:
            print("inserting into existing trace table")
            # insert data trace
            self.insert_into_existing_trace_table(imon_trace_signal_table_name, sweep_number, data_array_df,"data_array")

            print("inserting into existing meta table")
            # insert meta data
            try:
                column_name = 'sweep_' + str(sweep_number)
                meta_data_df = pd.DataFrame(list(child_node_ordered_dict.items()), columns=('Parameter', column_name))
                # parameter column will be only written once in sweep = 1 above
                meta_data_df = meta_data_df.drop(columns='Parameter')
                self.insert_into_existing_trace_table(imon_trace_meta_data_table_name, sweep_number,
                                                  meta_data_df,"meta_data")
            except Exception as e:
                print(e)
        
        
            def insert_into_existing_trace_table(self, table_name, sweep_number, data_frame, table_type):
        '''
        Inserts trace signals and meta data information into already existing tables in the database.
        :param table_name: name of the already existing table
        :param sweep_number: number of the sweep within the series
        :param data_frame: pandas data frame object that will be stored in the database
        :return:
        '''

        self.logger.info("Inserting sweep %s into existing table %s ", str(sweep_number), table_name)

        try:
            if table_type =='data_array':
                sweep_name = data_frame.columns.tolist()[0]
                self.database.execute(f' alter table {table_name} add {sweep_name} float')
                self.database.execute(f'insert into {table_name} ({sweep_name}) select {sweep_name} from data_frame')

                #self.database.query(f'update {table_name} set {sweep_name} = data_frame')
            else:
                old_df = self.database.execute(f'select * from {table_name}').df()
                new_df = pd.concat([old_df, data_frame], axis = 1)
                self.database.register('df_1', new_df)
                self.database.execute(f'drop table {table_name}')
                self.database.execute(f'CREATE TABLE {table_name} AS SELECT * FROM df_1')

            print("succesfull insert")
        except Exception as e:
            print("Catched error:")
            print(e)

    def create_and_insert_into_new_trace_table(self, table_name, data_frame, experiment_name, series_identifier,
                                               table_type):
        '''
        Creates new tables for meta data and signal traces and stores already he first sweep information.
        Additionally the  name of the newly created table will be registered in the experiment_series table for further access.
        :param table_name: name of the table that will be created - follows specific identifier rules
        :param data_frame: pandas data frame to be stored in the new table
        :param experiment_name: name of the experiment in the database where this data belong to
        :param series_identifier: name of the series identifier whithin the given experiment
        :param table_type: string token to differenciate between signal data and meta data information
        :return:
        '''


        try:
            # create a new sweep table
            # self.database.execute(f'create table {table_name} as select * from df_1')
            if table_type == 'data_array':
                self.database.execute(f'create table {table_name}(sweep_1 float)')
                self.database.query(f'insert into {table_name}(sweep_1) select sweep_1 from data_frame')
            else:
                self.database.register('df_1',data_frame)
                self.database.execute(f'create table {table_name} as select * from df_1')

            print("successfully inserted sweep 1")
            try:
                # update the series table by inserting the newly created sweep table name
                if table_type == "data_array":
                    q = """"""update experiment_series set sweep_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""""""

                else:

                self.execute_sql_command(self.database, q, (table_name, experiment_name, series_identifier))

                self.logger.info("Successfully created %s table %s of series %s in experiment %s",table_type, table_name, series_identifier, experiment_name)

            except Exception as e:
                self.logger.info("Update Series table failed with error %s", e)

        except Exception as e:
            print(data_frame)
            print(table_name)
            print(experiment_name)
            print(series_identifier)
            print("Error::Couldn't create a new table with error %s", e)
            self.logger.info("Error::Couldn't create a new table with error %s", e)
        
        """


    '''
    def get_sweep_meta_data(self,datalist,pos):
        # the list entry after the sweeps positions (pos) holds the data trace
        # since sqlite does not allow array insertion, a string will be generated
        # data points will be separated by comma (,)

        data = datalist[pos+1][2][0].get_fields()
        data_string = ""
        for key,value in data.items():
            if type(value) != str:
                value = str(value)

            data_string = data_string + "(" + key + ","+ value + "),"

        return data_string
    '''


'''
    def get_single_sweep_meta_data_from_database(self,data_array):
        """
        returns the meta data array for a specific sweep
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: meta data array (numpy array)
        """

        # since the meta_data object is a a list of list, numpy will save it as object (narray)
        # therefore, the object is "pickled" into a byte stream and unpickled from byte stream into an object.
        # loaded pickled data seem to be able  to execute arbitrary code - for safety reasons pickling is therefore
        # disabled and needs to be enabled for the specific unpickle of meta data byte stream
        np.load.__defaults__ = (None, True, True, 'ASCII')
        res = self.get_single_sweep_parameter_from_database(data_array, "meta_data")

        # finally disable pickle again
        np.load.__defaults__ = (None, False, True, 'ASCII')
        return res
        
           def get_sweep_id_list_for_offline_analysis(self,series_name):
        """
        returns a list of id's of sweeps to be analyzed for this sepcific series name and analysis_id
        :param series_name:
        :return:
        """
        q = """select r.sweep_id from (select s.experiment_name, s.series_identifier, s.sweep_id from sweeps s inner join 
        experiment_analysis_mapping m where s.experiment_name = m.experiment_name AND m.analysis_id = (?)) r inner join 
        experiment_series es where r.experiment_name = es.experiment_name AND r.series_identifier = es.series_identifier 
        AND es.series_name = (?) ;"""
        sweep_id_tuples = self.get_data_from_database(self.database,q,(self.analysis_id,series_name))
        sweep_id_list = []
        for t in sweep_id_tuples:
            sweep_id_list.append(t[0])
        return sweep_id_list

'''
