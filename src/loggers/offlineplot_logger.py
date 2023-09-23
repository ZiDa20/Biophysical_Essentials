
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

offlineplot_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/main_log.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
offlineplot_logger.addHandler(file_handler)
offlineplot_logger.setLevel(logging.INFO)
offlineplot_logger.info("Started Offline Plot Logging")