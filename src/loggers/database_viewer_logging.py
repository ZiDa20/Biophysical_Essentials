
import logging
# Module that creates the logging level and the logger
# Should be imported for the Database!

database_viewer_logger = logging.getLogger(__name__)
#file_handler = logging.FileHandler('../Logs/database_viewer.log')
file_handler = logging.FileHandler('../Logs/main_log.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
database_viewer_logger.addHandler(file_handler)
database_viewer_logger.setLevel(logging.INFO)
database_viewer_logger.info("Started offline_analysis_widget Logging")