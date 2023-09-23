
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

online_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/main_log.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
online_logger.addHandler(file_handler)
online_logger.setLevel(logging.INFO)
online_logger.info("Started Offline Plot Logging")