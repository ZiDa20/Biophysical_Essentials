
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

abf_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/abf.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
abf_logger.addHandler(file_handler)
abf_logger.setLevel(logging.INFO)
abf_logger.info("Started abf_file Logging")