from enum import Enum
class InputDataTypes(Enum):
    # basic input type manager
    BUNDLED_HEKA_DATA = "BUNDLED_HEKA_DATA"
    UNBUNDLED_HEKA_DATA = "UNBUNDLED_HEKA_DATA"
    ABF_DATA = "ABF_DATA"
    NANION_DATA = "NANION_DATA"
    BUNDLED_HEKA_FILE_ENDING = ".dat"
    ABF_FILE_ENDING = ".abf"