import numpy as np
import re, struct, collections

from Backend.DataReader.heka_reader import Struct
from Backend.DataReader.heka_reader import StructArray
from Backend.DataReader.heka_reader import TreeNode
from Backend.DataReader.heka_reader import cstr
from Backend.DataReader.heka_reader import Bundle
from Backend.tokenmanager import InputDataTypes



class GroupRecord(TreeNode):
    field_info = [

        ('Mark', 'i'),
        ('Label', '32s', cstr),
        ('Text', '80s', cstr),
        ('ExperimentNumber', 'i'),
        ('GroupCount', 'i'),
        ('CRC', 'i'),
    ]
    size_check = 128

class SeriesRecord(TreeNode):
    field_info = [
            ("Mark", "i"),  # (* INT32 *)
            ("Label", "32s", cstr),  # (* String32Type *)
            ("Comment", "80s", cstr),  # (* String80Type *)
            ("SeriesCount", "i"),  # (* INT32 *)
            ("NumberSweeps", "i"),  # (* INT32 *)
            ("AmplStateOffset", "i"),  # (* INT32 *)
            ("AmplStateSeries", "i"),  # (* INT32 *)
            ("SeMethodTag", "i"),  # (* INT32 *)
            ("SeTime", "d"),  # * LONGREAL *)
            ("SePageWidth", "d"),  # * LONGREAL *)
            ("SeSwUserParamDescr", "160s"),# UserParamDescrType(4)),  # (* ARRAY[0..3] OF UserParamDescrType = 4*40 *)
            ("SeMethodName", "32s", cstr),  # (* String32Type *)
            ("SeSeUserParams1", "4d"),  # (* ARRAY[0..3] OF LONGREAL *)
            ("SeLockInParams", "96s"),#. LockInParams_v9()),  # (* SeLockInSize = 96, see "Pulsed.de" *)
            ("SeAmplifierState", "400s"),#, AmplifierState_v9()),  # (* AmplifierStateSize = 400 *)
            ("SeUsername", "80s", cstr),  # (* String80Type *)
            ("SeSeUserParamDescr1", "160s"), #UserParamDescrType(4)),  # (* ARRAY[0..3] OF UserParamDescrType = 4*40 *)
            ("SeFiller1", "i"),  # (* INT32 *)
            ("SeCRC", "I"),  # (* CARD32 *)
            ("SeSeUserParams2", "4d"),  # (* ARRAY[0..3] OF LONGREAL *)
            ("SeSeUserParamDescr2", "160s"), #UserParamDescrType(4)),  # (* ARRAY[0..3] OF UserParamDescrType = 4*40 *)
            ("SeScanParams", "96s", cstr),  # (* ScanParamsSize = 96 *)
        ]
    size_check = 1408

class SweepRecord(TreeNode):
    field_info = [
        ('Mark', 'i'),
        ('Label', '32s', cstr),
        ('AuxDataFileOffset', 'i'),
        ('StimCount', 'i'),
        ('SweepCount', 'i'),
        ('Time', 'd'),
        ('Timer', 'd'),
        ('SwUserParams', '4d'),
        ('Temperature', 'd'),
        ('OldIntSol', 'i'),
        ('OldExtSol', 'i'),
        ('DigitalIn', 'h'),
        ('SweepKind', 'h'),
        ('Filler1', 'i', None),
        ('Markers', '4d'),
        ('Filler2', 'i', None),
        ('CRC', 'i'),
    ]
    size_check = 160

class TraceRecord(TreeNode):
   field_info = [ 
            ("Mark", "i"),  # (* INT32 *)
            ("Label", "32s", cstr),  # (* String32Type *)
            ("TraceCount", "i"),  # (* INT32 *)
            ("Data", "i"),  # (* INT32 *)
            ("DataPoints", "i"),  # (* INT32 *)
            ("InternalSolution", "i"),  # (* INT32 *)
            ("AverageCount", "i"),  # (* INT32 *)
            ("LeakCount", "i"),  # (* INT32 *)
            ("LeakTraces", "i"),  # (* INT32 *)
            ("DataKind", "h"), #get_data_kind),  # (* SET16 *)
            ("Filler1", "h"),
            ("RecordingMode", "b"), #get_recording_mode),  # (* BYTE *)
            ("AmplIndex", "c"),  # (* CHAR *)
            ("DataFormat", "b"),  # (* BYTE *)
            ("DataAbscissa", "b"),  # (* BYTE *)
            ("DataScaler", "d"),  # (* LONGREAL *)
            ("TimeOffset", "d"),  # (* LONGREAL *)
            ("ZeroData", "d"),  # (* LONGREAL *)
            ("YUnit", "8s", cstr),  # (* String8Type *)
            ("XInterval", "d"),  # (* LONGREAL *)
            ("XStart", "d"),  # (* LONGREAL *)
            ("XUnit", "8s", cstr),  # (* String8Type *)
            ("YRange", "d"),  # (* LONGREAL *)
            ("YOffset", "d"),  # (* LONGREAL *)
            ("Bandwidth", "d"),  # (* LONGREAL *)
            ("PipetteResistance", "d"),  # (* LONGREAL *)
            ("CellPotential", "d"),  # (* LONGREAL *)
            ("SealResistance", "d"),  # (* LONGREAL *)
            ("CSlow", "d"),  # (* LONGREAL *)
            ("GSeries", "d"),  # (* LONGREAL *)
            ("RsValue", "d"),  # (* LONGREAL *)
            ("GLeak", "d"),  # (* LONGREAL *)
            ("MConductance", "d"),  # (* LONGREAL *)
            ("LinkDAChannel", "i"),  # (* INT32 *)
            ("ValidYrange", "?"),  # (* BOOLEAN *)
            ("AdcMode", "b"),  # (* CHAR *)        # "c" is not read properly
            ("AdcChannel", "h"),  # (* INT16 *)
            ("Ymin", "d"),  # (* LONGREAL *)
            ("Ymax", "d"),  # (* LONGREAL *)
            ("SourceChannel", "i"),  # (* INT32 *)
            ("ExternalSolution", "i"),  # (* INT32 *)
            ("CM", "d"),  # (* LONGREAL *)
            ("GM", "d"),  # (* LONGREAL *)
            ("Phase", "d"),  # (* LONGREAL *)
            ("DataCRC", "I"),  # (* CARD32 *)
            ("CRC", "I"),  # (* CARD32 *)
            ("GS", "d"),  # (* LONGREAL *)
            ("SelfChannel", "i"),  # (* INT32 *)
            # Sigtool added the below 15.08.2012
            ("InterleaveSize", "i"),  # (* INT32 *)
            ("InterleaveSkip", "i"),  # (* INT32 *)
            ("ImageIndex", "i"),  # (* INT32 *)
            ("TrMarkers", "10d"),  # (* ARRAY[0..9] OF LONGREAL *)
            ("SECM_X", "d"),  # (* LONGREAL *)
            ("SECM_Y", "d"),  # (* LONGREAL *)
            ("SECM_Z", "d"),  # (* LONGREAL *)
        ]
   size_check = 408


class Pulsed(TreeNode):
    field_info = [
        ('Version', 'i'), # (* INT32 *)
        ('Mark', 'i'), # (* INT32 *)
        ('VersionName', '32s', cstr), # (* String32Type *)
        ('AuxFileName', '80s', cstr),  # (* String80Type *)
        ('RootText', '400s', cstr), # (* String400Type *)
        ('StartTime', 'd'), # (* LONGREAL *)
        ('MaxSamples', 'i'), # (* INT32 *)
        ('CRC', 'i'), # (* CARD32 *)
        ('Features', 'h'), # (* SET16 *)
        ('Filler1', 'h', None), # (* SET16 *)
        ('Filler2', 'i', None), # (* INT32 *)
    ]
    size_check = 544

    rectypes = [
        None,
        GroupRecord,
        SeriesRecord,
        SweepRecord,
        TraceRecord
    ]

    def __init__(self, file_name, offset=0, size=None):
        fh = open(file_name, 'rb')
        fh.seek(offset)

        # read .pul header
        magic = fh.read(4)
        if magic == b'eerT':
            self.endian = '<'
        elif magic == b'Tree':
            self.endian = '>'
        else:
            raise RuntimeError('Bad file magic: %s' % magic)

        levels = struct.unpack(self.endian + 'i', fh.read(4))[0]
        # read size of each level (one int per level)
        self.level_sizes = []
        for i in range(levels):
            size = struct.unpack(self.endian + 'i', fh.read(4))[0]
            self.level_sizes.append(size)

        TreeNode.__init__(self, fh, self)

class StimulationPGF(TreeNode): # first node from root
    field_info = [
        ('Mark', 'i'),
        ('EntryName', '32s',cstr),
        ('FileName', '32s', cstr),
        ('AnalName', '32s',cstr),
        ('DataStartSegment', 'i'),
        ('DataStartTime', 'd'),
        ('SampleInterval', 'd'),
        ('SweepInterval', 'd'),
        ('LeakDelay', 'd'),
        ('FilterFactor', 'd'),
        ('NumberSweeps', 'i'),
        ('NumberLeaks', 'i'),
        ('NumberAverages', 'i'),
        ('ActualAdcChannels', 'i'),
        ('ActualDacChannels', 'i'),
        ('ExtTriggers', 'c'),
        ('NoStartWait', '?'),
        ('UseScanRate', '?'),
        ('NoContAq', '?'),
        ('HasLockIn', '?'),
        ('OldStartMacKind', 'c'),
        ('OldEndMacKind', '?'),
        ('AutoRange', 'c'),
        ('BreakNext', '?'),
        ('IsExpanded', '?'),
        ('LeakCompMode', '?'),
        ('HasChirp', '?'),
        ('OldStartMacro', '32s', cstr),
        ('OldEndMacro', '32s', cstr),
        ('IsGapFree', '?'),
        ('HandledExternally', '?'),
        ('Filler1', '?'),
        ('Filler2', '?'),
        ('CRC', 'I'),

    ]
    size_check = 248


class ChannelPGF(TreeNode): # pfg tree second from root
    
    field_info = [
        ('Mark', 'i'),
        ('LinkedChannel', 'i'),
        ('CompressionFactor', 'i'),
        ('YUnit', '8s',cstr),
        ('AdcChannel', 'h'),
        ('AdcMode', 'c'),
        ('DoWrite', '?'),
        ('LeakStore', 'c'),
        ('AmplMode', 'c'),
        ('OwnSegTime', '?'),
        ('SetLastSeqVmemb', '?'),
        ('DacChannel', 'h'),
        ('DacMode', 'c'),
        ('HasLockInSquare', 'c'),
        ('RelevantXSegment', 'i'),
        ('RelevantYSegment', 'i'),
        ('DacUnit', '8s', cstr),
        ('Holding', 'd'),
        ('LeakHolding', 'd'),
        ('LeakSize', 'd'),
        ('LeakHoldMode', 'c'),
        ('LeakAlternate', '?'),
        ('AltLeakAveraging', '?'),
        ('LeakPulseOn', '?'),
        ('StimToDacId', 'h'),
        ('CompressionMode', 'h'),
        ('CompressionSkip', 'i'),
        ('DacBit', 'h'),
        ('HasLockInSine', '?'),
        ('BreakMode', 'c'),
        ('ZeroSeq', 'i'),
        ('StimSweep', 'i'),
        ('Sine_Cycle', 'd'),
        ('Sine_Amplitude', 'd'),
        ('LockIn_VReversal', 'd'),
        ('StartFreq', 'd'),
        ('EndFreq', 'd'),
        ('MinPoints', 'd'),
        ('NegAmpl', 'd'),
        ('Square_DurFactor', 'd'),
        ('LockIn_Skip', 'i'),
        ('Photo_MaxCycles', 'i'),
        ('Photo_SeqmentNo', 'i'),
        ('LockIn_AvgCycles', 'i'),
        ('Imaging_RoiNo', 'i'),
        ('Chirp_SKIP', 'i'),
        ('chirp_amplitude', 'd'),
        ('Photo_Adapt', 'c'),
        ('SineKind', 'c'),
        ('Chirp_PreChirp', 'c'),
        ('Sine_source', 'c'),
        ('Square_NegSource', 'c'),
        ('Square_PosSource', 'c'),
        ('Chirp_Kind', 'c'),
        ('ChirpSource', 'c'),
        ('DacOffset', 'd'),
        ('AdcOffset', 'd'),
        ('TraceMathFormat', 'c'),
        ('HasChirp', '?'),
        ('Square_kind', 'c'),
        ('Filler2',	'5s'), #219  ####### new ones
        ('SquareBaseIncr','d'),
        ('Square_Cycle','d'), # 
        ('Square_PosAmpl','d'), #
        ('CompressionOffset','i'), #
        ('PhotoMode','i'), #
        ('BreakLevel', 'd'), #
        ('TraceMath', '128s'), #
        ('Filler3','i'), #
        ('CRC','I') #
    ]
    size_check = 400
  
class StimChannelPGF(TreeNode): # pgf tree last from root
    field_info = [
        ('Mark', 'i'),
        ('Class', 'c'),
        ('Store', '?'),
        ('VoltageIncMode', 'c'),
        ('DurationIncMode', 'c'),
        ('Voltage', 'd'),
        ('VoltageSource', 'i'),
        ('DeltaVFactor', 'd'),
        ('DeltaVIncrement', 'd'),
        ('Duration', 'd'),
        ('DurationSource', 'i'),
        ('DeltaTFactor', 'd'),
        ('DeltaTIncrement', 'd'),
        ('Filler1', 'i'),
        ('CRC', 'I'),
        ('ScanRate', 'd'),

    ]
    size_check = 80
    
class Pgf(TreeNode):
    """ field info for the PGF file, manually adapted the size we maybe need to have a further look"""

    field_info = [
        ('Version', 'i'), # 4
        ('Mark', 'i'), # 8
        ('VersionName', '32s', cstr), # 40
        ('MaxSample', 'i'), #44
        ('Filler1', 'i'), # 48
        ('Params', '10d'), # 56
        ('ParamText', '320s',cstr), #
        ('Reserved', '128s',cstr), # 380
        ('Filler2', 'i'), # 384
        ('Reserved2', '560b'), # 384
        ('CRC', 'I'), # 388
    ]
    size_check = 1144

    rectypes = [
        None,
        StimulationPGF,
        ChannelPGF,
        StimChannelPGF
    ]

    def __init__(self, file_name, offset=0, size=None):
        fh = open(file_name, 'rb')
        fh.seek(offset)

        # read .pul header
        magic = fh.read(4)
        if magic == b'eerT':
            self.endian = '<'
        elif magic == b'Tree':
            self.endian = '>'
        else:
            raise RuntimeError('Bad file magic: %s' % magic)

        levels = struct.unpack(self.endian + 'i', fh.read(4))[0]

        # read size of each level (one int per level)
        self.level_sizes = []
        for i in range(levels):
            size = struct.unpack(self.endian + 'i', fh.read(4))[0]
            self.level_sizes.append(size)

        TreeNode.__init__(self, fh, self)


class Data(object):
    def __init__(self, pul, file_name, offset=0, size=None):
       
        self.offset = offset
        self.pul = pul
        self.file_name = file_name

    def __getitem__(self, *args):
        index = args[0]
        assert len(index) == 4

        trace = self.pul[index[0]][index[1]][index[2]][index[3]]

        fh = open(self.file_name, 'rb')
        fh.seek(trace.Data)

        fmt = 0#bytearray(trace.DataFormat)[0]
        dtype = [np.int16, np.int32, np.float16, np.float32][fmt]
        data = np.fromfile(fh, count=trace.DataPoints, dtype=dtype)

        #print('{:.6e}=>{:0=6.2f}e-15'.format(trace.DataScaler,trace.DataScaler/1e-15))
        roundet_scaler ='{:.6e}=>{:0=5.1f}e-15'.format(trace.DataScaler,trace.DataScaler/1e-15)
        roundet_scaler = roundet_scaler.split('=>')
        roundet_scaler = float(roundet_scaler[1])

        #print('{:.6e}=>{:0=6.2f}e-12'.format(trace.ZeroData, trace.ZeroData / 1e-12))
        roundet_zero = '{:.6e}=>{:0=6.2f}e-12'.format(trace.ZeroData, trace.ZeroData / 1e-12)
        roundet_zero = roundet_zero.split('=>')
        roundet_zero = float(roundet_zero[1])

        return_res_old = data * trace.DataScaler - trace.ZeroData
        r1 = data * trace.DataScaler + trace.ZeroData # original !!!!
        r2 = data * trace.DataScaler + trace.ZeroData/2
        r3 = data * trace.DataScaler + 2*trace.ZeroData
        r4 = data * trace.DataScaler - trace.ZeroData/2
        r5 = data * trace.DataScaler
        return_res = data* roundet_scaler + roundet_zero
        return return_res_old

class BundleFromUnbundled(object):
    """
        qthread_heka_unbundled_reading function: Read the .pul, .dat und .pgf file individually 

        Args:
            directory_path (str): path of the data dir
            file_name (str): name of the file

        Returns:
            Bundle: a fake bundle with the items as Pulsed, Data and PGF object rather than a BundleItem
        @author: dz, 20240331
    """

    def __init__(self, pathname, file_name):
        self.pathname = pathname
        self.file_name = file_name
        self.pul = Pulsed(pathname + file_name + ".pul")
        self.pgf = Pgf(pathname + file_name + ".pgf")
        self.dat = Data(self.pul, pathname + file_name + ".dat")

    def generate_bundle(self):
        return Bundle(self.pathname + self.file_name + InputDataTypes.HEKA_DATA_FILE_ENDING.value,
                      [(InputDataTypes.HEKA_PULSE_FILE_ENDING.value, self.pul),
                       (InputDataTypes.HEKA_DATA_FILE_ENDING.value, self.dat),
                       (InputDataTypes.HEKA_STIMULATION_FILE_ENDING.value, self.pgf)])