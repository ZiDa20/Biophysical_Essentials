#import boto3
from dataclasses import dataclass

@dataclass
class ResultHolder:
    """_summary_: Class that holds the final result tables
    This class should be 
    """
    database_handler = None
    analysis_result_dictionary = []
    
    def upload_to_S3_bucket(self):
        pass
    
    def update_duckdb_database(self):
        pass
    
    def construct_meta_data_table_results(self):
        pass
    
    
    
        