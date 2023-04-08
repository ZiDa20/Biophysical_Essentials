
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

start_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/start.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
start_logger.addHandler(file_handler)
start_logger.setLevel(logging.INFO)
start_logger.info("Started Program Main Logging")