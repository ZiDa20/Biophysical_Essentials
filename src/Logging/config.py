# This module is the configuration file for the picologging
import picologging


LOG_LEVEL: str = "INFO"
# checks the currently selected log level
if LOG_LEVEL == "INFO":
    loglevel = picologging.INFO
elif LOG_LEVEL == "DEBUG":
    loglevel = picologging.DEBUG
elif LOG_LEVEL == "ERROR":
    loglevel = picologging.ERROR
elif LOG_LEVEL == "WARNING":
    loglevel = picologging.WARNING
# add other log levels if needed

picologging.basicConfig(
    format="Module: %(name)s | %(levelname)s | %(asctime)s | %(message)s",
    level=loglevel,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[picologging.StreamHandler()],
)
