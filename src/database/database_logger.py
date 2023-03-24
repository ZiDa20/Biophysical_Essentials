
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

database_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/database_manager.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
database_logger.addHandler(file_handler)
database_logger.setLevel(logging.INFO)
database_logger.info("Started Database Logging")