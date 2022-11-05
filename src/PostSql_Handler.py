import psycopg2
from data_db import DuckDBDatabaseHandler
from sqlalchemy import create_engine
from Worker import Worker

#Class to handle the connection to the database which is currently located at the Amazon RDS Server EC2
# This should be replaced by an big data server which allows for online saving
# Also great backup option for potential data loss

class PostSqlHandler():

    """ Should handle the data connection with PostSql"""
    def __init__(self, duckdb_handler: DuckDBDatabaseHandler, progress_callback):
        """ Initialize the PostSqlHandler
        args:
            duckdb_handler: DuckDBDatabaseHandler object which is used to get the data from the duckDB database
        """
        self.database = None
        self.duckdb_handler = duckdb_handler    
        self.progress_callback = progress_callback
        self.initialize_database()
        self.database_tables: list = self.get_all_tables_duckdb()
        self.write_all_tables()
        

    def get_all_tables_duckdb(self):
        """ return all the table written to the duckdb database"""
        try:
            all_tables: list = self.duckdb_handler.database.execute("SHOW TABLES").fetchdf()["name"].tolist()
            return all_tables
        except Exception as e:
            print(e)

    def write_all_tables(self, progress_callback=None):
        """ write all the tables of the duckDB database to the PostSql database
        Backup: This is a backup option for the data in case of data loss
        """
        update_progress = 100/len(self.database_tables)
        progess = 0
        for table in self.database_tables:
            print(f"this is the name of the {table}")
            try:
                query: str = f"SELECT * FROM {table};"
                data = self.duckdb_handler.database.execute(query).fetchdf()
                data.to_sql(table, con = self.conn, if_exists='replace', index=False, method='multi', chunksize=1000)
                progess += update_progress
                self.progress_callback.emit((progess, table))
            except Exception as e:
                print(e)
                pass
        self.close_connection()

    def initialize_database(self):
        """ Initialize the PostSql database connection
        """ 
        try:
            conn_string: str = 'postgresql://postgres:datascience@ec2-3-73-36-35.eu-central-1.compute.amazonaws.com/duckdb'
            db = create_engine(conn_string)
            self.conn = db.connect()
  
        except Exception as e:
            print(e)

    def close_connection(self):
        """ close the connection to the database
        """
        try:
            self.conn.close()
        except Exception as e:
            print(e)

    
