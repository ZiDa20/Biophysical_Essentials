# This module is the configuration file for the picologging
import picologging
import sys
import os 

if getattr(sys, 'frozen', False):
    EXE_LOCATION = sys._MEIPASS
else:
    EXE_LOCATION = os.path.dirname(os.path.dirname( os.path.realpath( __file__ ) ))

# Determine log level
LOG_LEVEL = "INFO"
loglevel = {
    "INFO": picologging.INFO,
    "DEBUG": picologging.DEBUG,
    "ERROR": picologging.ERROR,
    "WARNING": picologging.WARNING
}.get(LOG_LEVEL, picologging.INFO)

def setup_logging():
    """Ensures the Logs directory exists and configures logging."""
    log_dir = os.path.join(EXE_LOCATION, "Logging", "Logs")
    os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

    log_file = os.path.join(log_dir, "log.log")

    picologging.basicConfig(
        format="Module: %(name)s | %(levelname)s | %(asctime)s | %(message)s",
        level=loglevel,
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[picologging.FileHandler(log_file)]
    )


log_file = os.path.join(log_dir, "log.log")

# Configure logger
logger = picologging.getLogger("BPE")
logger.setLevel(loglevel)

# Add handlers only once
if not logger.handlers:
    file_handler = picologging.FileHandler(log_file)
    stream_handler = picologging.StreamHandler()  # optional: comment out if CI slow
    formatter = picologging.Formatter(
        "Module: %(name)s | %(levelname)s | %(asctime)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)