
import logging

# Module that creates the logging level and the logger
# Should be imported for the Database!

treeview_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../Logs/tree_view_manager.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
treeview_logger.addHandler(file_handler)
treeview_logger.setLevel(logging.INFO)
treeview_logger.info("Started tree_view_manager Logging")