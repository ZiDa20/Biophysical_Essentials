from enum import Enum
class InputDataTypes(Enum):
    # basic input type manager
    BUNDLED_HEKA_DATA = "BUNDLED_HEKA_DATA"
    UNBUNDLED_HEKA_DATA = "UNBUNDLED_HEKA_DATA"
    ABF_DATA = "ABF_DATA"
    NANION_DATA = "NANION_DATA"
    BUNDLED_HEKA_FILE_ENDING = ".dat"
    ABF_FILE_ENDING = ".abf"
    HEKA_DATA_FILE_ENDING = ".dat"
    HEKA_PULSE_FILE_ENDING = ".pul"
    HEKA_STIMULATION_FILE_ENDING = ".pgf"
    HEKA_CHANNEL_PGF = "Channel",
    HEKA_STIMULATION_PGF = "Stimulation"
    HEKA_STIM_CHANNEL_PGF = "StimChannel"


#@todo refactor the name ?  series table writer
class TableEnum(Enum):
    """Holder of Experiment Name Table Prefixes"""
    IMON_SIGNAL = "imon_signal"
    IMON_META_DATA = "imon_meta_data"
    PGF_DATA = "pgf_table"


class OfflineAnalysisTreeTokens(Enum):
    CONFIGURATOR_TOKEN = "Analysis Configurator"
    CONFFIGURATOR_INDEX = 0
    PLOT_TOKEN = "Plot"
    PLOT_INDEX = 1
    TABLES_TOKEN = "Tables"
    TABLES_INDEX = 2
    STATISTICS_TOKEN = "Statistics"
    STATISTICS_INDEX = 3
    MULTI_SERIES_TOKEN = "Multi-Series Analysis:"



