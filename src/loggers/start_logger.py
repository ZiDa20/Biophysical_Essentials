
import logging
import os

# Create the Logs directory if it doesn't exist
log_dir = '../Logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up the logger
start_logger = logging.getLogger(__name__)
log_file_path = os.path.join(log_dir, 'main_log.log')

# Create the log file if it doesn't exist
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as file:
        file.write("Log file created.")

file_handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
start_logger.addHandler(file_handler)
start_logger.setLevel(logging.INFO)
start_logger.info("Started Program Main Logging")