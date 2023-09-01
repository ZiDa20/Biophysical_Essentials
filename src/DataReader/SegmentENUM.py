from enum import Enum

class EnumSegmentTypes(Enum):
    CONSTANT = '\x00' 
    RAMP = '\x01'
    CONTINOUS = '\x02'
    SINE = '\x03'
    SQUARE = '\x04'
    CHIRP = '\x05'