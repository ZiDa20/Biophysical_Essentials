import psycopg2
from data_db import DuckDBDatabaseHandler

#Class to handle the connection to the database which is currently located at the Amazon RDS Server EC2
# This should be replaced by an big data server which allows for online saving
# Also great backup option for potential data loss

class PostSqlHandler():

    """ Should handle the data connection with PostSql"""
    def __init__(self, duckdb_handler):
        self.database = None
        self.duckdb_handler = duckdb_handler    
        self.initialize_database()
        self.database_tables = self.get_all_tables_duckdb()
        self.write_all_tables()

    def get_all_tables_duckdb(self):
        try:
            all_tables = self.duckdb_handler.database.execute("SHOW TABLES").fetchdf()
            print(all_tables)
            return all_tables
        except Exception as e:
            print(e)


    def write_all_tables(self):
        for table in self.database_tables[1:]:
            try:
                query = f"SELECT * FROM '{table}';"
                data = self.duckdb_handler.database.execute(query).fetchdf()
                print(data)
            except Exception as e:
                print(e)
                pass


    def initialize_database(self):
        try:
            conn = psycopg2.connect(host = "ec2-3-73-36-35.eu-central-1.compute.amazonaws.com",
                        database="test_erp",
                        user="postgres",
                        password="datascience",
                        port = 5432)
            self.database = conn.cursor()

            sql = '''ROLLBACK;'''
            self.database.execute(sql)

            sql = '''CREATE TABLE IF NOT EXISTS final (id INT, name VARCHAR(255));'''
            self.database.execute(sql)
            
            sql = '''INSERT INTO final (id, name) VALUES (2, 'trial');'''
            self.database.execute(sql)

            trial = '''SELECT * FROM final;'''
            self.database.execute(trial)
        
            data = self.database.fetchall()
            print(data)

        except Exception as e:
            print(e)

    
