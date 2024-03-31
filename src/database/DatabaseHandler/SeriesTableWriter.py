from enum import Enum
import pandas as pd
import picologging
#import debugpy
from Backend.tokenmanager import TableEnum

class ExperimentTableNames:
    """ Experiment Table Name Creator"""
    logger = picologging.getLogger(__name__)

    def __init__(self, experiment_name: str, series_identifier: str) -> None:
        self.experiment_name = experiment_name
        self.series_identifier = series_identifier
        self.imon_signal_table_name = self._create_table_name(TableEnum.IMON_SIGNAL)
        self.imon_meta_data_table_name = self._create_table_name(TableEnum.IMON_META_DATA)
        self.pgf_table = self._create_table_name(TableEnum.PGF_DATA)

    def _create_table_name(self, table_enum: TableEnum) -> str:
        return f'{table_enum.value}_{self.experiment_name}_{self.series_identifier}'

class SeriesTableWriter:
    """ Writes the Experiment Tables to the Database"""
    logger = picologging.getLogger(__name__)

    def __init__(self, database, experiment_name, series_identifier) -> None:
        self.experiment_name = experiment_name
        self.series_identifier = series_identifier
        self.database = database
        self.TableNames = ExperimentTableNames(experiment_name, series_identifier)
        print(self.TableNames)

    def add_sweep_df_to_database(self,
                                 data_df: pd.DataFrame,
                                 meta_data_df: pd.DataFrame,
                                 dat: bool = True) -> None:
        """_summary_: This function adds a sweep dataframe to the database
        holding all the necessary sweep information for a series
        """
        try:
            self.logger.info(f"Creating sweep table for series: {self.series_identifier}")
            self.build_imon_signal_query(data_df)
            self.build_imon_metadata(meta_data_df, dat)

            self._update_experiment_series(self.TableNames.imon_meta_data_table_name)

            self.logger.info("Successfully created both df tables of series %s in experiment %s", self.series_identifier, self.experiment_name)

        except Exception as e:
            self.logger.error("In general add sweep df to database failed with error: %s", e)

    def _update_experiment_series(self, table_name: str) -> None:
        """
        Update the meta_data_table_name for a specific experiment series.

        Args:
            table_name (str): The name of the metadata table.

        Returns:
            None
        """
        
        q = """update experiment_series set meta_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
        self.database.execute(q, (table_name, self.experiment_name, self.series_identifier))

    # Rest of the code remains the same...
    def build_imon_signal_query(self, data_df) -> str:
        """
        Builds and executes a SQL query to create a table for imon signal data and inserts the data from a DataFrame.

        Args:
            data_df (pandas.DataFrame): The DataFrame containing the imon signal data.

        Returns:
            bool: True if the table creation and data insertion are successful, False otherwise.
        """
        column_names = data_df.columns.tolist()
        part_1 = f'create table {self.TableNames.imon_signal_table_name} ('
        query_str = ""
        for i, column_name in enumerate(column_names):
            if i == len(column_names) - 1:
                part_1 = part_1 + column_name + " " + "float"
                query_str = query_str + column_name
            else:
                part_1 = part_1 + column_name + " " + "float,"
                query_str = query_str + column_name + ","

        part_1 = f"{part_1})"

        try:
            self.database.execute(part_1)
            self.database.query(f'INSERT INTO {self.TableNames.imon_signal_table_name} SELECT {query_str} FROM data_df')
            q = """update experiment_series set sweep_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
            self.database.execute(q, (self.TableNames.imon_signal_table_name,
                                      self.experiment_name,
                                      self.series_identifier))
            return True

        except Exception as e:
            self.logger.error(f"Failed to create imon signal table {self.TableNames.imon_signal_table_name} with error: " +  {e})
            return False

    def build_imon_metadata(self, meta_data_df, dat: bool = True) -> None:
        """This function builds the imon metadata table

        Args:
            meta_data_df (pd.DataFrame): Holding Metadata
            dat (bool, optional): _description_. Defaults to True.

        Returns:
            bool: True if successfull otherwise False
        """
        column_names  = meta_data_df.columns.tolist()
        meta_data_df = meta_data_df.reset_index()
        meta_data_df.columns = ['Parameter'] + column_names

        if dat:
            affected_rows = [10,11,12,13,33]

            for r in affected_rows:
                try:
                    replace_val = int.from_bytes(meta_data_df['sweep_1'].iloc[r], "big")
                    for c in column_names:
                        meta_data_df[c].iloc[r]= replace_val
                except Exception as e:
                    print("TODO: check this in general !!! might be not necessery in unbundled data loading")

        self.logger.info("Adding Meta Data to database")

        try:
            self.database.execute(f'CREATE TABLE {self.TableNames.imon_meta_data_table_name} AS SELECT * FROM meta_data_df')
            self.logger.info(f"Added Meta Data Table {self.TableNames.imon_meta_data_table_name} to databas successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create meta data table {self.TableNames.imon_meta_data_table_name} with error: " +  {e})
            return False



    def create_series_specific_pgf_table (self,
                                          pgf_table: pd.DataFrame,
                                          series_identifier: str,
                                          ) -> None:
        
        """
        Creates a series-specific table in the database using the provided Pandas DataFrame.

        Args:
            pgf_table (pd.DataFrame): The Pandas DataFrame containing the data to be stored in the table.
            series_identifier (str): The identifier of the series.

        Returns:
            None: This method does not return any value.

        Raises:
            Exception: If there is an error creating the table or updating the series table.
        """
        
        #self.database.register('df_1', data_frame)

        try:
            # create a new sweep table
            self.logger.info("Creating new pgf table %s", pgf_table)
            self.database.execute(f'create table {self.TableNames.pgf_table} as select * from pgf_table')

            try:
                # update the series table by inserting the newly created pgf table name
                q = """update experiment_series set pgf_data_table_name=(?) where experiment_name = (?) and series_identifier=(?)"""
                self.logger.info("Updating series table with new pgf table name %s", pgf_table)
                self.database.execute(q, (self.TableNames.pgf_table, self.experiment_name, series_identifier))

                self.logger.info("Successfully created %s table of series %s in experiment %s", self.TableNames.pgf_table,
                                 series_identifier, self.experiment_name)

            except Exception as e:
                self.logger.error("Update Series table failed with error %s", e)


        except Exception as e:
            self.logger.error("Error::Couldn't create a new table with error %s", e)


    def add_single_series_to_database(self, series_name:str, series_identifier: str) -> None:
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
            series_name, series_identifier, self.experiment_name)
        try:
            self.logger.info("inserting series %s to experiment_series table", series_name)
            q = """insert into experiment_series(experiment_name, series_name, series_identifier,discarded,series_meta_data) values (?,?,?,?,?) """
            self.database = self.database.execute(q,
                                                     (self.experiment_name,
                                                      series_name, series_identifier, 0,"None"))
            # 0 indicates not discarded
            self.logger.info("insertion finished succesfully")
        except Exception as e:
            self.logger.error("insertion finished FAILED because of error %s", e)