
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

offline_analysis_widget_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/offline_analysis_widget.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
offline_analysis_widget_logger.addHandler(file_handler)
offline_analysis_widget_logger.setLevel(logging.INFO)
offline_analysis_widget_logger.info("Started offline_analysis_widget Logging")