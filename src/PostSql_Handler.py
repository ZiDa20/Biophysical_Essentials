import psycopg2
from data_db import DuckDBDatabaseHandler

#Class to handle the connection to the database which is currently located at the Amazon RDS Server EC2
# This should be replaced by an big data server which allows for online saving
# Also great backup option for potential data loss

class PostSqlHandler(DuckDBDatabaseHandler):

    """ Should handle the data connection with PostSql"""
    def __init__(self):
        super().__init__() # get the function from the data


    def initialize_database():
        try:
            conn = psycopg2.connect(host = "ec2-3-73-36-35.eu-central-1.compute.amazonaws.com",
                        database="test_erp",
                        user="postgres",
                        password="datascience",
                        port = 5432)
            self.database = conn.cursor()

        except Exception as e:
            print(e)
