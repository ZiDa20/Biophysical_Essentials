from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from Offline_Analysis.error_dialog_class import CustomErrorDialog
import re
import numpy as np
import pandas as pd

import duckdb
#from global_meta_data_table import GlobalMetaDataTable
import re
from pathlib import Path
from database.DuckDBInitalizer import DuckDBInitializer
from database.database_logger import database_logger

if TYPE_CHECKING:
    import logging
    from StyleFrontend.frontend_style import Frontend_Style


class DuckDBDatabaseHandler():
    ''' A class to handle all data in a duck db database.
     @date: 23.06.2021, @author dz'''

    def __init__(self, frontend_style, db_file_name="duck_db_analysis_database.db", in_memory = False, database_path = "./database/"):

        #@toDO add properties instead of open variable names like analysis_id and database path
        # set up the classes for the main tables
        #self.global_meta_data_table = GlobalMetaDataTable(self.database,self.analysis_id)
        # logger settings
        self.db_file_name: str = db_file_name
        self.database_path: str = database_path
        self.logger: logging.Logger = database_logger
        self.duckdb_database: DuckDBInitializer = DuckDBInitializer(self.logger, self.db_file_name, in_memory, database_path)
        self.frontend_style: Frontend_Style = frontend_style
        self.logger.info('Database Manager Initialized')
        self.duck_db_database: str = "DUCK_DB"
        self.database, self.analysis_id = self.duckdb_database.init_database()

        # change manually for now .. maybe to be implemented in settings tabs
        #self.database_architecture = self.duck_db_database  # you can select between 'DUCK_DB' or 'SQ_LITE
        #self.init_database()

    """---------------------------------------------------"""
    """ General database functions                        """
    """---------------------------------------------------"""

    def open_connection(self, read_only: bool = False) -> None:
        """_summary_: Open a connection to the database

        Args:
            read_only (bool, optional): If the database should be opened
            read only or not (Important for threading). Defaults to False.
        """
        self.database = self.duckdb_database.open_connection(read_only)

    def get_data_from_database(self, database: duckdb.DuckDBPyConnection,
                               sql_command: str,
                               values: Optional[int]=None,
                               fetch_mode: Optional[int]=None):
        """_summary_

        Args:
            database (duckdb.DuckDBPyConnection): database Connection
            sql_command (str): SQL query to execute
            values (Optional[int], optional): values to query for. Defaults to None.
            fetch_mode (Optional[int], optional): which DuckDB Fetch Mode. Defaults to None.

        Returns:
            _type_: _description_
        """
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

    def get_tables(self) -> None:
        """_summary_: Returns all tables in the database"""
        return self.get_data_from_database(self.database, "SHOW TABLES;", fetch_mode=2)

    """--------------------------------------------------------------"""
    """ Functions to interact with table experiment_analysis_mapping """
    """--------------------------------------------------------------"""

    def create_table_for_database(self, table: pd.DataFrame , table_name: str) -> None:
        """_summary_: Creates a table in the database

        Args:
            table (pd.DataFrame): The table construct as pd. DataFrame
            table_name (str): The name the table should have in the database
        """
        new_df = table
        self.database.execute(f"CREATE TABLE {table_name} as SELECT * FROM new_df;")
        trial = self.database.execute(f"Select * from {table_name};").fetch_df()
        self.logger.info(f"Created Solution Table {table_name}")

    def add_solution_table_to_mapping(self, table_name: str, solution_type: str) -> None:
        """_summary_: Adds a solution table to the database

        Args:
            table_name (str): The name of the solution table to add
        """
        self.database.execute("INSERT INTO solution (solutions, type) VALUES (?,?);", [table_name, solution_type])
        self.logger.info(f"Added Solution Table {table_name} to mapping")

    def create_mapping_between_experiments_and_analysis_id(self, experiment_id: int) -> None:
        """_summary_: Creates a mapping between an experiment and the current analysis id

        Args:
            experiment_id (int): The experiment id
        """
        q = 'insert into experiment_analysis_mapping values (?,?)'
        try:
            self.database.execute(q, (experiment_id, self.analysis_id))
            self.logger.info("Mapped experiment %s to analysis %i", experiment_id, self.analysis_id)
            print("Mapped experiment %s to analysis %i", experiment_id, self.analysis_id)
        except Exception as e:
            self.logger.info("Mapping between experiment %s and analysis %i FAILED", experiment_id, self.analysis_id)


    def create_mapping_between_series_and_analysis_id(self):
        """
        create the series mapping table by joining already existing analysis experiment mapping table with the experiment series table.
        importantly, only the mappings of the current id should be added to the series analysis mapping table.
        """

        q = "Insert into series_analysis_mapping (analysis_id, experiment_name, series_identifier, series_name, renamed_series_name, analysis_discarded) \
                SELECT experiment_analysis_mapping.analysis_id, experiment_analysis_mapping.experiment_name, experiment_series.series_identifier, experiment_series.series_name, experiment_series.series_name, experiment_series.discarded \
                FROM experiment_analysis_mapping \
                JOIN experiment_series \
                ON experiment_analysis_mapping.experiment_name = experiment_series.experiment_name where experiment_analysis_mapping.analysis_id = (?);"

        try:
            self.database = self.database.execute(q,[self.analysis_id])
            print("Series Mapping fpr analysis id", self.analysis_id)
            #self.logger.info("Series Mapping fpr analysis id", self.analysis_id)
        except Exception as e:
            print(e)
            #self.logger.info("Series Mapping Failed")


    """---------------------------------------------------"""
    """    Functions to interact with treeview              """
    """---------------------------------------------------"""

    def update_discarded_selected_series(self, old_id, new_id):
        """update the current analysis with previous selected and discarded experiments"""

        template_df = self.database.execute(f'select * from series_analysis_mapping where analysis_id = {old_id} ').fetchdf()

        template_df = template_df[template_df["analysis_discarded"]=="true"] # per default all are false, so better just update the trues to reduce time
        for name, identifier, val in zip(template_df["experiment_name"].values, template_df["series_identifier"].values, template_df["analysis_discarded"].values):
            self.database.execute(f'update series_analysis_mapping set analysis_discarded = \'{val}\' where experiment_name = \'{name}\' and series_identifier = \'{identifier}\' and analysis_id = {new_id}')

        # might be helpful for debug
        #print("fetching updated")
        #print(self.database.execute(f'select * from series_analysis_mapping where analysis_id == {new_id} and experiment_name = \'{"cell_10"}\' ').fetchdf())



    """---------------------------------------------------"""
    """    Functions to interact with table filters       """
    """---------------------------------------------------"""

    def write_filter_into_database(self, filter_name: str,
                                   lower_threshold: float,
                                   upper_threshold: float):
        """_summary_: Writes a filter into the database

        Args:
            filter_name (str): The name of the filter
            lower_threshold (float): The lower threshold
            upper_threshold (float): The upper threshold
        """

        q = """ insert into filters values (?,?,?,?)"""
        self.database = self.database.execute(q,(filter_name, lower_threshold, upper_threshold, self.analysis_id))

    """---------------------------------------------------"""
    """    Functions to interact with table analysis_series     """
    """---------------------------------------------------"""

    def write_analysis_series_types_to_database(self, name_list: list) -> None:
        '''Takes the user selected series types (e.g. block pulse, iv, ...) and places them in the referring database
        table "series"
        @date: 23.06.2021, @author: dz '''

        for n in name_list:
            # query the recording mode
            recording_mode = self.query_recording_mode(n)

            q = """insert into analysis_series (analysis_series_name, recording_mode, analysis_id) values (?,?,?) """

            try:
                self.database = self.database.execute(q, (n, recording_mode, self.analysis_id))
                self.logger.info(f'inserting new analysis_series with id  {self.analysis_id}')
            except Exception as e:
                self.logger.info(f'ERROR while inserting new analysis_series with id  {self.analysis_id}')

        self.logger.info("inserted all series")

    def query_recording_mode(self, series_name: str) -> str:
        """
        Get the recording mode from the meta data table of a (by-name-) specified series
        selects only the first
        :param series_name:
        :return: str Voltage Clamp or Current Clamp
        """

        if isinstance(series_name,tuple):
            series_name = series_name[0]

        q = """select experiment_name, series_identifier from series_analysis_mapping where renamed_series_name=(?) and analysis_id = (?)"""
        res = self.get_data_from_database(self.database, q, (series_name, self.analysis_id))

        q = """ select meta_data_table_name from experiment_series where experiment_name = (?) and series_identifier = (?)"""
        name = self.get_data_from_database(self.database, q, (res[0][0], res[0][1]))[0][0]

        q = f'SELECT Parameter, sweep_1 FROM {name}'
        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        x = str(meta_data_dict.get('RecordingMode'))
        return "Voltage Clamp" if int(x) == 3 else "Current Clamp"


    def write_recording_mode_to_analysis_series_table(self, recording_mode, analysis_series_name, analysis_id):
        q = 'update analysis_series set recording_mode = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.database.execute(q, (recording_mode, analysis_series_name, analysis_id))

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
        return np.linspace(
            x_start,
            x_start + x_interval * (number_of_datapoints - 1) * 1000,
            number_of_datapoints,
        )

    # used dz 29.06.2022#
    def get_time_in_ms_of_analyzed_series(self, experiment_name: str, series_identifier: str) -> np.ndarray:

        # get the related meta data table name from the first experiment in the list
        q = """select meta_data_table_name from experiment_series where experiment_name = (?) AND series_name = (?)"""
        res = self.get_data_from_database(self.database, q, (experiment_name, series_identifier))[0][0]

        # calculated time again as in plot widget manager
        q = f'SELECT Parameter, sweep_1 FROM {res}'

        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        x_start = float(meta_data_dict.get('XStart'))
        x_interval = float(meta_data_dict.get('XInterval'))
        number_of_datapoints = int(meta_data_dict.get('DataPoints'))
        return np.linspace(
            x_start,
            x_start + x_interval * (number_of_datapoints - 1) * 1000,
            number_of_datapoints,
        )

    def get_ymin_from_metadata_by_sweep_table_name(self,table_name: str,sweep: str) -> tuple[float,float]:
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

    def get_sweep_table_names_for_offline_analysis(self, series_name: str, meta: Optional[bool] = None) -> list[str]:
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

                q = 'select sweep_table_name \
                    from experiment_series as t1\
                        inner join (\
                            select * from series_analysis_mapping \
                            where analysis_id = (?) and analysis_discarded = (?) ) \
                        as t2\
                        on t1.experiment_name = t2.experiment_name and t1.series_identifier = t2.series_identifier\
                        where t1.series_meta_data = (?) and t2.renamed_series_name = (?) and t1.experiment_name = (?)'


                #q = 'select sweep_table_name from experiment_series where experiment_name = (?) AND series_name = (?) ' \
                #    'AND discarded = (?) AND series_meta_data = (?)'
                try:
                    r = self.get_data_from_database(self.database, q, (self.analysis_id, False, meta, series_name, experiment_tuple[0]))[0]
                    sweep_table_names.extend(r)
                except Exception as e:
                    self.logger.error(f"Error in get_sweep_table_names_for_offline_analysis: {e}")
            else:
                #q = 'select sweep_table_name from experiment_series where experiment_name = (?) AND series_name = (?) AND discarded = (?)'

                q = 'select sweep_table_name \
                    from experiment_series as t1\
                        inner join (\
                            select * from series_analysis_mapping \
                            where analysis_id = (?) and analysis_discarded = (?) ) \
                        as t2\
                        on t1.experiment_name = t2.experiment_name and t1.series_identifier = t2.series_identifier\
                        where t2.renamed_series_name = (?) and t1.experiment_name = (?)'
                try:
                    r = self.get_data_from_database(self.database, q, (self.analysis_id, False, series_name, experiment_tuple[0]), fetch_mode = 2)["sweep_table_name"].tolist()
                    sweep_table_names.extend(r)
                except Exception as e:
                    self.logger.error(f"Error in get_sweep_table_names_for_offline_analysis: {e}")

        return sweep_table_names

    def get_experiments_by_series_name_and_analysis_id(self, series_name):
        '''
        Find experiments of the current analysis containing the series specified by the series name.
        :param series_name: name of the series (e.g. Block Pulse, .. )
        :return: list of tuples of experimentnames (e.g. [(experiment_1,),(experiment_2,)]
        '''
        q = """select experiment_name from experiment_analysis_mapping where analysis_id = (?) intersect (select experiment_name from series_analysis_mapping where renamed_series_name = (?) and analysis_id = (?))"""
        return self.get_data_from_database(
            self.database, q, (self.analysis_id, series_name,self.analysis_id)
        )

    def get_experiments_by_series_name_and_analysis_id_with_meta(self, series_name, meta_data):
        '''
        Find experiments of the current analysis containing the series specified by the series name.
        :param series_name: name of the series (e.g. Block Pulse, .. )
        :param meta_data associated
        :return: list of tuples of experimentnames (e.g. [(experiment_1,),(experiment_2,)]
        '''
        q = """select experiment_name from experiment_analysis_mapping where analysis_id = (?) intersect (select experiment_name from series_analysis_mapping where renamed_series_name = (?) AND series_meta_data = (?) and analysis_id = (?))"""
        return self.get_data_from_database(
            self.database, q, (self.analysis_id, series_name, meta_data,self.analysis_id)
        )

    def get_experiments_by_series_name_and_analysis_id_with_series(self, series_name, meta_data):
        '''
        Find experiments of the current analysis containing the series specified by the series name.
        :param series_name: name of the series (e.g. Block Pulse, .. )
        :param meta_data associated
        :return: list of tuples of experimentnames (e.g. [(experiment_1,),(experiment_2,)]
        '''
        q = """select experiment_name from experiment_analysis_mapping where analysis_id = (?) intersect (select experiment_name from series_analysis_mapping where renamed_series_name = (?) AND series_identifier = (?) and analysis_id = (?))"""
        return self.get_data_from_database(
            self.database, q, (self.analysis_id, series_name, meta_data,self.analysis_id)
        )

    def get_experiment_from_sweeptable_series(self, series_name, sweep_table_name):
        q = f"""SELECT experiment_name FROM experiment_series WHERE sweep_table_name = '{sweep_table_name}'""" #AND series_name = '{series_name}
        print(q)
        return self.database.execute(q).fetchall()[0][0]

    def get_sweep_table_name(self, experiment_name, series_identifier):
        '''
        returns the sweep table name for a given experiment and series name
        :param experiment_name:
        :param series_name:
        :return:
        '''
        if not isinstance(experiment_name, str):
            raise TypeError(f"expected String type and not {type(experiment_name)}")
        q = f'select sweep_table_name from experiment_series where experiment_name = \'{experiment_name}\' AND series_identifier = \'{series_identifier}\''
        res = self.database.execute(q).fetchdf()

        # check if the result is not empty
        return res["sweep_table_name"].tolist()[0] if not res.empty else None

    def get_extracellular_solutions(self) -> list:
        """_summary_: Retrieves all extracellular solutions from the database.

        Returns:
            list: Names of the extracellular solutions.
        """
        ecs = self.database.execute('select * from solution').fetchdf()
        return ecs[ecs["type"] == "Extracellular"]["solutions"].tolist()

    def get_intracellular_solutions(self) -> list:
        """_summary_: Retrieves all intracellular solutions from the database.

        Returns:
            list: Names of the intracellular solutions.
        """
        ics = self.database.execute('select * from solution').fetchdf()
        return ics[ics["type"] == "Intracellular"]["solutions"].tolist()

    def get_entire_sweep_table(self, table_name, fetchmode = 1):
        '''
        Fetches all sweeps in a sweep table.
        :param table_name:
        :return: the table as dict {column: numpy_array(data ... )]}
        '''
        try:
            if fetchmode == 1:
                return self.database.execute(f'select * from {table_name}').fetchnumpy()
            else:
                return self.database.execute(f'select * from {table_name}').fetchdf()
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
            self.database = self.database.execute(q)
            #self.logger.info(meta_data[0], "added succesfully to global_meta_data")
            return 1
        except Exception as e:
            if "Constraint Error" in str(e):
                self.logger.info(
                    "Experiment with name %s was already in global meta data")
            else:
                print("adding experiment to global meta data failed")

    def get_available_category_groups(self,category):
        """
        return all available label in the database
        @return: a tuple list
        """
        q = f'select distinct {category} from global_meta_data'

        return self.get_data_from_database(self.database, q)

    def get_meta_data_group_of_specific_experiment(self, experiment_name):
        """
        :param experiment_name:
        :return:
        :author dz, 28.06.2022
        """
        if not isinstance(experiment_name, str):
            raise TypeError(f"The entered value is of type {type(experiment_name)}, but str is expected")
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
            self.database = self.database.execute(q)
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
            self.database = self.database.execute(q)
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

    def get_experiment_name_for_given_sweep_table_name(self,sweep_table_name: str) -> list:
        """
        Get's the name of the experiment for a given sweep table name
        :param sweep_table_name: string of the name
        :return:
         :authored: dz, 29.04.2022
        """
        q = f'select experiment_name from experiment_series where sweep_table_name = \'{sweep_table_name}\''
        return self.get_data_from_database(self.database, q)[0][0]

    def get_cslow_value_from_experiment_name_and_series_identifier(self,experiment_name,series_identifier):
        """
        implemented to replace the function below
        """
        print(experiment_name, series_identifier)
        q = """select meta_data_table_name, sweep_table_name from experiment_series where experiment_name = (?) and series_identifier = (?)"""
        print(q)
        # should return a list with only one tuple with meta_data_name and sweep table name
        res = self.get_data_from_database(self.database, q, (experiment_name,series_identifier))[0]
        sweep_table_name = res[1]
        q = f'SELECT Parameter, sweep_1 FROM {res[0]}'
        meta_data_dict = {x[0]: x[1] for x in self.database.execute(q).fetchdf().itertuples(index=False)}

        return float(meta_data_dict.get('CSlow')), sweep_table_name

    def get_normalization_values(self, function_id):
        q = f'select sweep_table_name, normalization_value from normalization_values where offline_analysis_id = (?) and function_id = (?)'
        return self.database.execute(q, (self.analysis_id, function_id)).fetch_df()

    """
    def get_cslow_value_for_sweep_table(self, series_name: str) -> float:
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

    """

    def add_single_series_to_database(self, experiment_name: str, series_name:str, series_identifier: str) -> None:
        """ Adds a single series to the database. This function is used when a new series is added to an existing experiment

        Args:
            experiment_name (str): name of the experiment
            series_name (str): name of the series
            series_identifier (str): identifier of the series
        Returns:
            None
        """
        self.logger.info(
            "Inserting series name %s with series identifier %s of experiment %s to experiment_series table",
            series_name, series_identifier, experiment_name)
        try:
            self.logger.info("inserting series %s to experiment_series table", series_name)
            q = """insert into experiment_series(experiment_name, series_name, series_identifier,discarded,series_meta_data) values (?,?,?,?,?) """
            self.database = self.database.execute(q,
                                                     (experiment_name, series_name, series_identifier, 0,"None"))
            # 0 indicates not discarded
            self.logger.info("insertion finished succesfully")
        except Exception as e:
            self.logger.error("insertion finished FAILED because of error %s", e)


    def get_experiment_names_by_experiment_label(self,experiment_label: str,meta_data_list: list) -> list:
        """
        :param experiment_label:
        :return:
        :author: dz, 27.06.2022
        """

        for i in meta_data_list:
            if meta_data_list.index(i)==0:
                q = f'select experiment_name from global_meta_data where condition = \'' + i + '\''
            else:
                q+= ' or condition = \'' + i + '\''

        r2 = self.get_data_from_database(self.database, q) #  retrieves the experiment names for the given meta data
        experiment_names = []
        for i in r2:
            experiment_names.append(i[0])

        return experiment_names

    def get_series_names_of_specific_experiment(self,experiment_name: str,discarded: bool = False) -> list:
        """

        :param experiment_name:
        :return: a list of tuples [(series_name, series_identifier), ... ] e.g. [('Block Pulse', 'Series1'), ('IV','Series2'), .. ]
        :author: dz, 22.06.2022
        """
        q = f'select series_name, series_identifier from experiment_series where experiment_name = \'{experiment_name}\' and discarded = \'{discarded}\''
        return self.get_data_from_database(self.database,q)

    """----------------------------------------------------------"""
    """    Functions to interact with table analysis_functions   """
    """----------------------------------------------------------"""

    def get_analysis_function_name_from_id(self,analysis_function_id: int) -> Optional[str]:
        """_summary_: This function returns the name of the analysis function for a given analysis function id

        Args:
            analysis_function_id (int): The Analysis function id

        Returns:
            Optional[str]: Analysis Function returned
        """
        q= f'select function_name from analysis_functions where analysis_function_id = {analysis_function_id}'
        if r := self.get_data_from_database(self.database, q):
            return r[0][0]
        else:
            return None

    def get_analysis_series_name_by_analysis_function_id(self,analysis_function_id:str) -> str:
        """_summary_: This function returns the name of the analysis series for a given analysis function id

        Args:
            analysis_function_id (str): The Analysis function id
        Returns:
            str: Analysis Series returned
        """
        q = f'select analysis_series_name from analysis_functions where analysis_function_id = {analysis_function_id}'
        r = self.get_data_from_database(self.database, q)
        return r[0][0]

    def write_analysis_function_name_and_cursor_bounds_to_database(self,
                                                                    analysis_function: str,
                                                                    analysis_series_name: str,
                                                                    lower_bound: float,
                                                                    upper_bound: float,
                                                                    pgf_segment: int) -> None:

        try:
            q = """insert into analysis_functions (function_name, analysis_series_name, analysis_id,lower_bound,upper_bound,pgf_segment) values (?,?,?,?,?,?)"""
            self.database = self.database.execute(q, (
            analysis_function, analysis_series_name, self.analysis_id, lower_bound, upper_bound, pgf_segment))
            self.logger.info(
                f'added new row into analysis_function_table: {analysis_function}, {analysis_series_name},{self.analysis_id},{lower_bound},{upper_bound}')
            print(f'added new row into analysis_function_table: {analysis_function}, {analysis_series_name},{self.analysis_id},{lower_bound},{upper_bound}')
        except Exception as e:
            print("Insertion of analysis function name and cursor bounds into database failed because of error %s", e)


    def get_last_inserted_analysis_function_id(self):
        """Returns the last inserted analysis function id"""
        q = """select analysis_function_id from analysis_functions """
        id_list = self.get_data_from_database(self.database, q)
        print("greatest identifier is: ", max(id_list)[0])
        return max(id_list)[0]

    def get_series_specific_analysis_functions(self, series_name: str) -> Optional[list]:
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

    def get_cursor_bounds_of_analysis_function(self, analysis_function_id: int, series_name: str) -> list:
        """
        Returns a list triples (lower, upper bound, id) for the specified analysis function name and the analysis id.
        :param function_name: name of the analysis function (e.g. min, max, .. )
        :param series_name: name of the analysis series (e.g. Block Pulse, ... )
        :return: a list of cursor bound triples, with cursor bound values at positions 0 and 1 and thed
        function analysis id at the third position
        """

        q = """select lower_bound, upper_bound from analysis_functions where analysis_function_id = (?) AND analysis_series_name=(?) AND analysis_id = (?)"""
        return self.get_data_from_database(
            self.database, q, (analysis_function_id, series_name, self.analysis_id)
        )

    def get_analysis_functions_for_specific_series(self,series_name: str) -> list:
        """ Returns a list of analysis function names for a given series name
        Args:
            series_name (str): The series name
        Returns:
            list: List of analysis function names
        """

        q = f'select function_name from analysis_functions where analysis_id = {self.analysis_id} and analysis_series_name=\'{series_name}\''
        return self.database.execute(q).fetchall()

    """----------------------------------------------------------"""
    """    Functions to interact with table sweeps   """
    """----------------------------------------------------------
    """

    def get_single_sweep_data_from_database_by_sweep_id(self, sweep_id: str):
        q = f'select data_array from sweeps where sweep_id = \"{sweep_id}\"'
        return self.get_data_from_database(self.database, q)[0][0]

    def get_sweep_meta_data(self, datalist: list, pos: int) -> np.ndarray:
        """ write dictionary to array in database """

        data = datalist[pos + 1][2][0]
        data = list(data.items())

        return np.array(data)

    def write_analysis_function_to_database(self, function_list: list, series_type: str) -> None:
        """_summary_: This function writes the analysis functions to the database
        Args:
            function_list (list): List of analysis functions
            series_type (str): The series type
        """
        for f in function_list:
            sql_command = """INSERT INTO analysis_functions (function_name,series_type) VALUES (?,?) """
            self.database = self.database.execute(sql_command, (f, series_type))

    def get_sweep_parent(self, datalist: list, pos: int):
        ''' returns experiment name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''
        return self.find_node_type(datalist, pos, "Group", 1)

    def get_series_identifier(self, datalist:list, pos: int):
        ''' returns series identifier name as a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        return self.find_node_type(datalist, pos, "Series", 0)

    def find_node_type(self, datalist:list, pos: int, type: str, elem):
        '''type: internal helper_function, author: dz, 15.06.21 '''
        for d in range(pos, -1, -1):
            if type in datalist[d][0]:
                return datalist[d][elem]

    def get_sweep_number(self, sweep_name: str) -> str:
        '''get the sweep number out of a string,
        type: internal helper_function, author: dz, 15.06.21 '''

        splitted_string = re.match(r"([a-z]+)([0-9]+)", sweep_name, re.I)
        res = splitted_string.groups()
        return (res[1])

    def write_coursor_bounds_to_database(self,
                                         lower_value: float,
                                         upper_value: float,
                                         series_name: str):
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
            zero = self.database.execute(non_zero_bound, values)

        if len(r2) > len(r1) or zero:
            for d in r2:
                q = """insert into analysis_functions(function_name,lower_coursor,upper_coursor) values (?,?,?)"""
                values = (d, lower_value, upper_value)
                self.database = self.database.execute(q, values)
        else:
            q = """update analysis_functions set lower_coursor=(?), upper_coursor=(?) where function_name = (?) """
            for d in r2:
                values = (lower_value, upper_value, d[0])
                self.database = self.database.execute(q, values)

        # from database: check if coursor bounds are empty (only when less then 2 duplicates available)

    def get_analysis_series_names_for_specific_analysis_id(self):

        q= f'select analysis_series_name from analysis_series where analysis_id = {self.analysis_id}'
        return self.database.execute(q).fetchall()

    def write_result_to_database(self,
                                 analysis_function_id: int,
                                 table_name: str,
                                 sweep_number: str,
                                 result_value: float) -> None:

        q = """insert into results values (?,?,?,?,?) """
        self.database = self.database.execute(q, (
        self.analysis_id, analysis_function_id, table_name, sweep_number, result_value))


    def read_series_type_specific_analysis_functions_from_database(self, series_name: str) -> list:
        q = f'select distinct function_name from analysis_functions where series_type = \"{series_name}\" '
        res_string = self.get_data_from_database(self.database, q)
        return [t[0] for t in res_string]

    def convert_string_to_array(self, array_as_string: str) -> list:
        """_summary_: This function converts a string to an array

        Args:
            array_as_string (str): This is a string that should be converted to
            an array

        Returns:
            list: holding the values of the array
        """
        sub_res = array_as_string.split(",")
        return [float(s) for s in sub_res]

    def convert_array_to_string(self, data_array: list) -> str:
        output_string = ""
        for d in data_array:
            if output_string == "":
                output_string = str(d)
            else:
                output_string = output_string + "," + str(d)

        return output_string

    def add_sweep_df_to_database(self,experiment_name: str,
                                 series_identifier: str,
                                 data_df: pd.DataFrame,
                                 meta_data_df: pd.DataFrame,
                                 dat: bool = True) -> None:

        """_summary_: This function adds a sweep dataframe to the database
        holding all the necessary sweep information for a series

        Args:
            series_identifier (str): This is the series identifier such as IV
            data_df (pd.DataFrame): This is the data frame holding the data for the series holding the sweeps
            meta_data_df (pd.DataFrame): This is the data frame holding the meta data for the series
            data (bool, optional): This is a boolean indicating if the data should be added to the database. Defaults to True.
        """
        try:
            self.logger.info(f"Createing sweep table for series: {series_identifier}")
            imon_trace_signal_table_name = self.create_imon_signal_table_name(experiment_name, series_identifier)
            # requires a little bit of different handling

            column_names = data_df.columns.tolist()
            part_1 = f'create table {imon_trace_signal_table_name} ('
            query_str = ""
            for c in range(len(column_names)):
                if c == len(column_names)-1:
                    part_1 = part_1 + column_names[c] + " " + "float"
                    query_str = query_str + column_names[c]
                else:
                    part_1 = part_1 + column_names[c] + " " + "float,"
                    query_str = query_str + column_names[c] + ","

            part_1 = f"{part_1})"
            try:
                self.database.execute(part_1)
                self.database.query(f'INSERT INTO {imon_trace_signal_table_name} SELECT {query_str} FROM data_df')

            except Exception as e:
                self.logger.error("")

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
                self.database.execute(q, (imon_trace_signal_table_name, experiment_name, series_identifier))
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

            self.logger.info("Adding Meta Data to database")

            try:
                self.database.execute(f'CREATE TABLE {imon_trace_meta_data_table_name} AS SELECT * FROM meta_data_df')
            except Exception as e:
                self.logger.error("Failed to create meta data table with error: %s", e)

            self.logger.info("Added Meta Data to databas successfully")

            q = """update experiment_series set meta_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
            self.database.execute(q,
                                     (imon_trace_meta_data_table_name, experiment_name, series_identifier))


            self.logger.info("Successfully created both df tables of series %s in experiment %s", series_identifier, experiment_name)

        except Exception as e:
            self.logger.error("In general add sweep df to database failed with error: %s", e)



    def create_imon_signal_table_name(self, experiment_name: str, series_identifier: str) -> str:
        '''
        Creates unique names of database tables for i_mon sweep data. It's an extra function so multiple functions can access this naming convention.
        :param experiment_name: text representation of the experiment name
        :param series_identifier: text representation of the series identifier (e.g. Series1)
        :return: table name as string
        '''
        return f'imon_signal_{experiment_name}_{series_identifier}'

    def create_imon_meta_data_table_name(self, experiment_name: str, series_identifier: str) -> str:
        '''
        Creates unique names of i_mon meta data database tables. It's an extra function so multiple functions can access this naming convention.
        :param experiment_name: text representation of the experiment name
        :param series_identifier: text representation of the series identifier (e.g. Series1)
        :return: table name as string
        '''
        return f'imon_meta_data_{experiment_name}_{series_identifier}'



    def get_single_sweep_meta_data_from_database(self, data_array: np.ndarray):
        '''
        Requests all meta data from a specific sweep in the database
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: meta data dictionary
        '''

        return self.get_single_sweep_values_according_to_parameter(data_array, 'meta_data')

    def get_single_sweep_data_from_database(self, data_array: np.ndarray)-> np.ndarray:
        """
        Requests a specific sweep trace from the database
        :param data_array: data array with 3 fields (experiment_name, series_identifier, sweep_number)
        :return: data array (numpy array)
        """

        return self.get_single_sweep_values_according_to_parameter(data_array, 'trace_signal')

    def get_single_sweep_values_according_to_parameter(self, data_array: np.ndarray, param: str) -> Union[np.list, dict]:
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
        column_name = f'sweep_{str(sweep_number)}'

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

    def discard_specific_series(self, experiment_name: str, series_identifier: str) -> None:
        """Change the column valid for a specifc series from 0 (valid) to 1 (discarded, in-valid)"""
        print("initial tree is calling discard button function with params", experiment_name, series_identifier)
        self.change_experiment_series_discarded_state(experiment_name, series_identifier, 1)

    def reinsert_specific_series(self, experiment_name: str, series_identifier: str) -> None:
        self.change_experiment_series_discarded_state(experiment_name, series_identifier, 0)

    def change_experiment_series_discarded_state(self, experiment_name: str, series_identifier: str, state: str) -> None:
        q = """update experiment_series set discarded = (?) where experiment_name = (?) AND series_identifier = (?);"""
        self.database.execute(q, (state, experiment_name, series_identifier))

    def get_distinct_non_discarded_series_names(self) -> None:
        """
        get all distinct series names from series mapped with the current analysis id
        :return:
        """
        # @todo: why do we need the discarded = False in here ?
        q1 = f'select distinct renamed_series_name from series_analysis_mapping where analysis_discarded = False and analysis_id = {self.analysis_id}'

        return self.get_data_from_database(self.database, q1)

    '''-------------------------------------------------------'''
    '''     create series specific pgf trace table            '''
    '''-------------------------------------------------------'''

    def create_series_specific_pgf_table (self,
                                          data_frame: pd.DataFrame,
                                          pgf_table_name: pd.DataFrame,
                                          experiment_name: str,
                                          series_identifier: str) -> None:
        """ adds new pgf table to the database        """
        #self.database.register('df_1', data_frame)

        try:
            # create a new sweep table
            self.logger.info("Creating new pgf table %s", pgf_table_name)
            self.database.execute(f'create table {pgf_table_name} as select * from data_frame')

            try:
                # update the series table by inserting the newly created pgf table name
                q = """update experiment_series set pgf_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
                self.logger.info("Updating series table with new pgf table name %s", pgf_table_name)
                self.database.execute(q, (pgf_table_name, experiment_name, series_identifier))

                self.logger.info("Successfully created %s table of series %s in experiment %s", pgf_table_name,
                                 series_identifier, experiment_name)

            except Exception as e:
                self.logger.error("Update Series table failed with error %s", e)

        except Exception as e:
            self.logger.error("Error::Couldn't create a new table with error %s", e)

    def get_entire_pgf_table_by_experiment_name_and_series_identifier(self,experiment_name: str, series_identifier: str)-> pd.DataFrame:
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

    def get_entire_pgf_table(self,data_table_name: str)-> pd.DataFrame:
        """
        Query the enitre pgf table as dataframe as pandas data frame
        :param data_table_name:
        :return:
        """
        q = """select pgf_data_table_name from experiment_series where sweep_table_name = (?)"""
        pgf_table_name = self.get_data_from_database(self.database, q, [data_table_name])[0][0]

        self.database.execute(f'SELECT * FROM {pgf_table_name}')
        return self.database.fetchdf()

    def get_data_from_recording_specific_pgf_table(self,table_name:str,data_name:str,segment_number:int)->float:
        """_summary_: get the holding potential or increment from the pgf table

        Args:
            table_name (str): The name of the sweep table
            data_name (str): The name of the data to be retrieved
            segment_number (int): Which PGF segment to retrieve the data from

        Returns:
            float: increment or holding potential
        """
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


    def get_pgf_file_selection(self,current_tab):

        """Should retrieve the pgf_files for all the files in the current analysis id
        This should further retrieve each individual segment,
        pgf_selection: combobox that holds the inital segments"""
        analysis_id = self.analysis_id
        series_name = current_tab.objectName()
        experiment_name = self.database.execute(f"SELECT experiment_name FROM experiment_analysis_mapping WHERE analysis_id = {analysis_id};").fetchall()
        pgf_file_dict = {}
        ref_elem_exp = None
        for experiment in experiment_name:
            try:
                q = """select pgf_data_table_name from experiment_series where experiment_name = (?) and series_name = (?)"""
                pgf_sections = self.get_data_from_database(self.database, q, [experiment[0], series_name])[0][0]
                pgf_table = self.database.execute(f"SELECT * FROM {pgf_sections}").fetchdf()

                if pgf_table[pgf_table["selected_channel"] == "1"].empty:
                    if pgf_table[pgf_table["selected_channel"] == "2"].empty:
                         pgf_table = pgf_table[pgf_table["selected_channel"] == "3"]
                    else:
                        pgf_table = pgf_table[pgf_table["selected_channel"] == "2"]
                else:
                    pgf_table = pgf_table[pgf_table["selected_channel"] == "1"] # this should be change to an input from the user if necessary
                pgf_file_dict[experiment[0]] = (pgf_table, pgf_table.shape[0])
                ref_elem_exp = experiment[0]
            except IndexError:
                print(f"The error is at the experiment: {experiment[0]}")
                continue

        pgf_files_amount = {pgf_index[1] for pgf_index in pgf_file_dict.values()}

        if len(pgf_files_amount) <= 1:
            trial = pgf_file_dict.get(ref_elem_exp)[0]
            cnts = trial["selected_channel"].value_counts()
            seg_list = []
            for i in range(1,cnts[0]+1):
                seg_list.append(str(i))
            return seg_list

        else:
            CustomErrorDialog("The number of segments is not the same for all experiments. Please check your data.", self.frontend_style)
            return {"Segments are unequal"}


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
        print(result_data_frame)
        q = """insert into  results values (?,?,?,?) """ #set specific_result_table_name = (?) where analysis_id = (?) and analysis_function_id = (?) and sweep_table_name = (?) """
        print("updating results table with new specific result ")
        try:
            print("inside try")
            # create a new sweep table
            self.database.execute(f'create table {new_specific_result_table_name} as select * from df_1')

            self.database.execute(q, (analysis_id, function_analysis_id,data_table_name,new_specific_result_table_name))

            self.logger.info("Successfully created %s table of %s for analysis_function_id %d", new_specific_result_table_name,
                             data_table_name, function_analysis_id)
        except Exception as e:
            print("inside error")
            print("error")
            print(e)

    @staticmethod
    def create_new_specific_result_table_name(analysis_function_id:int, data_table_name:str) -> str:
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        return f"results_analysis_function_{analysis_function_id}_{data_table_name}"

    def get_selected_meta_data(self, analysis_function_id):
        # get the meta data table that is stored in the database
		# if no meta data were assigned the name will be "None" which needs to be catched as an exception

        q_analysis = f'select * from selected_meta_data where offline_analysis_id = {self.analysis_id} AND analysis_function_id = -1'
        q_specific = f'select * from selected_meta_data where offline_analysis_id = {self.analysis_id} AND analysis_function_id = {analysis_function_id}'

        selected_meta_data = self.get_data_from_database(self.database,q_specific, fetch_mode = 2)["condition_column"].tolist()
        if selected_meta_data:
            return selected_meta_data
        else:
            selected_meta_data = self.get_data_from_database(self.database,q_analysis, fetch_mode = 2)["condition_column"].tolist()
            if selected_meta_data:
                return selected_meta_data
            else:
                return None

    ######################################
    # deprecated  Sections:
    ######################################
    def write_ms_spaced_time_array_to_analysis_series_table(self, time_np_array, analysis_series_name, analysis_id):
        """
        dz 22.02.2022 deprecated
        :param time_np_array: time in milliseconds already converted into numpy array
        :return:
        """
        q = 'update analysis_series set time = (?) where analysis_series_name = (?) AND analysis_id = (?)'
        self.database = self.database.execute(q, (time_np_array, analysis_series_name, analysis_id))


## deprecated ??

"""
    def get_data_from_pgf_table(self, series_name: str, data_name: str, segment_number: int) -> float:

        reads pgf information from the database and returns the requested floa value of the specified segment
        :param series_name:
        :param data_name: 'holding', 'increment'
        :param segment_number: int nubmer of the segment, first = 0
        :return:
        :author: dz, 21.06.2022

        # @todo also check for the correct offline analysis id and only select these exoeriemnts?
        experiment_names = self.get_experiments_by_series_name_and_analysis_id(series_name)

        # take the first element, get the pgf_table_name, extract holding and
        experiment_name = experiment_names[0][0]


        q = select pgf_data_table_name from experiment_series where experiment_name = (?) and series_name = (?)
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

        q = f'SELECT experiment_name FROM experiments WHERE series_name = \"{series_type}\";'
        file_names = self.get_data_from_database(self.database, q)

        q = f'select time from analysis_series where analysis_series_name = \"{series_type}\";'
        time = self.get_data_from_database(self.database, q)

        for f in file_names:
            q = f'select series_identifier,sweep_number,sweep_id from sweeps where experiment_name = \"{f[0]}\";'
            sweeps = self.get_data_from_database(self.database, q)
            file_path = f"{data_path}/{f[0]}"
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

                    q =update analysis_series set time = (?) where analysis_series_name = (?);
                    self.database = self.database.execute(q, (string_time, series_type))

                # convert data array into comma separated string
                data_array = self.convert_array_to_string(data_array)

                q = update sweeps set data_array = (?) where sweep_id = (?);
                self.database = self.database.execute(q, (data_array, s[2]))
        """


