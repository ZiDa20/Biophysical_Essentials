
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

logger = logging.getLogger()
file_handler = logging.FileHandler('../Logs/database_manager.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)