import os
import numpy as np
import re, struct, collections


########

#rebuilding this shit: https://www.mathworks.com/matlabcentral/fileexchange/70164-heka-patchmaster-importer

def HI_ImportHEKAtoMat(obj):
    # ImportHEKA imports HEKA PatchMaster and ChartMaster .DAT files
    # Filepath is taken from the input object.
    #
    # ImportHEKA has been tested with Windows generated .DAT files on Windows,
    # Linux and Mac OS10.4.
    #
    # Both bundled and unbundled data files are supported. If your files are
    # unbundled, they must all be in the same folder.
    #
    # Details of the HEKA file format are available from
    #       ftp://server.hekahome.de/pub/FileFormat/Patchmasterv9/

    #--------------------------------------------------------------------------
    # Author: Malcolm Lidierth 12/09
    # Copyright � The Author & King's College London 2009-
    #--------------------------------------------------------------------------
    # Revisions
    # 17.04.10  TrXUnit: see within
    # 28.11.11  TrXUnit: see within
    # 15.08.12  Updated to support interleaved channels and PatchMaster 2.60
    #               files dated 24-Jan-2011 onwards.
    # 19.05.13 Modified by Samata Katta to output Matlab variable containing data
    # 12.08.15 Don't save *.kcl file (line 793 commented out).
    # 03.07.17 Modified by Samata Katta to read in stimulus parameters from
    # .pgf section of .dat file.
    # 01.01.2019 Modified by Christian Keine to read solution parameters from
    # .sol section of .dat file.
    # 04.02.2019: combine readout of dataTree, stimTree and solTree.
    #
    # See also	HEKA_Importer
    # 			HEKA_Importer.HI_loadHEKAFile
    # 			HEKA_Importer.HI_extractHEKASolutionTree
    # 			HEKA_Importer.HI_extractHEKAStimTree
    # 			HEKA_Importer.HI_extractHEKADataTree
    #			HEKA_Importer.HI_readPulseFileHEKA
    #			HEKA_Importer.HI_readStimulusFileHEKA
    #			HEKA_Importer.HI_readAmplifierFileHEKA
    #			HEKA_Importer.HI_readSolutionFileHEKA
    
    #pathname, filename, ext = os.path.splitext(obj.opt.filepath)

    class FileData:
        def __init__(self):
            self.fh = None
            self.Sizes = None
            self.Position = None
            self.fileExt = None
            self.Counter = 0
            self.Tree= []
            self.Level = 0

    class Opt:
        def __init__(self):
            self.fileData = FileData()

    class Obj:
        def __init__(self):
            self.opt = Opt()
            self.trees = {}  # Initialize trees as an empty dictionary


    pathname = "/home/data-science/Downloads/test_data_dat1/"
    filename = "PATCH4_2023278_07"
    suffix = ".dat"

    obj = Obj()

    endian = 'big'  # Assume little-endian to begin with
    with open(pathname+filename+suffix,'rb') as fh:
        bundle, littleendianflag, isBundled = getBundleHeader(fh)
    
    # Big endian so repeat process
    if littleendianflag is False:
        endian = 'big'
        with open(pathname+filename+suffix, 'rb') as fh:
            bundle, _, _ = getBundleHeader(fh)

    # GET DATA, STIM AND SOLUTION TREE
    fileExt = ['.pul', '.pgf', '.sol', '.amp']
    treeName = ['dataTree', 'stimTree', 'solTree', 'ampTree']

    for iidx in fileExt:
        fileExist = True
        if isBundled:
            ext = [item.oExtension for item in bundle.oBundleItems]
            try:
                idx = ext.index(iidx)
                start = bundle.oBundleItems[idx].oStart
            except ValueError:
                fileExist = False
        else:
            start = 0
            try:
                with open(os.path.join(pathname, filename + iidx), 'rb') as fh:
                    pass
            except FileNotFoundError:
                fileExist = False

        if fileExist:
            with open(pathname+filename+iidx, 'rb') as fh:
                fh.seek(start)
                Magic = fh.read(4).decode('utf-8')
                Levels = np.fromfile(fh, dtype=np.int32, count=1)[0]
                Sizes = np.fromfile(fh, dtype=np.int32, count=Levels)
                Position = fh.tell()

                # Get the tree structures form the file sections
                obj.opt.fileData.fh = fh
                obj.opt.fileData.Sizes = Sizes
                obj.opt.fileData.Position = Position
                obj.opt.fileData.fileExt = iidx

                obj.trees[treeName[fileExt.index(iidx)]] = getTree(obj)
        else:
            obj.trees[treeName[fileExt.index(iidx)]] = []

    # clean-up remaining temporary data
    try:
        del obj.opt.fileData['Sizes']
        del obj.opt.fileData['Position']
        del obj.opt.fileData['fileExt']
        del obj.opt.fileData['Counter']
        del obj.opt.fileData['Tree']
        del obj.opt.fileData['Level']
    except KeyError:
        pass

    # GET DATA
    if isBundled:
        idx = [item.oExtension for item in bundle.oBundleItems].index('.dat')
        start = bundle.oBundleItems[idx].oStart
    else:
        start = bundle.BundleHeaderSize

    with open(obj.opt.filepath, 'rb') as fh:
        fh.seek(start)
        ngroup = 1
        grp_row = []
        for k in range(len(obj.trees['dataTree'])):
            if obj.trees['dataTree'][k][1] is not None:
                grp_row.append(k)
        matData2 = []
        dataRaw = []
        for iGr, grp in enumerate(grp_row):
            matData2.append(LocalImportGroup(fh, obj.trees['dataTree'], iGr, grp_row))
            dataRaw.append([])
            for iSer in range(len(matData2[iGr])):
                dataRaw[iGr].append([])
                for item in matData2[iGr][iSer]:
                    dataRaw[iGr][iSer].append(np.random.randn(*item.shape) * np.finfo(float).eps)
        obj['RecTable']['dataRaw'] = np.vstack(dataRaw)
        obj['RecTable'] = dict2table(obj['RecTable'])

def getBundleHeader(fh):
    # Get the bundle header from a HEKA .dat file
    fh.seek(0)
    oSignature = fh.read(8).decode('utf-8').rstrip('\x00')
    #header = BundleHeader(fh, "<")
    #sg = header.Signature
    if oSignature == 'DATA':
        # Old format: nothing to do
        oVersion = None
        oTime = None
        oItems = None
        oIsLittleEndian = None
        oBundleItems = None
        BundleHeaderSize = 0
        isBundled = False
    elif oSignature in ['DAT1', 'DAT2']:
        # Newer format
        #oVersion = fh.read(32).decode('utf-8').strip()
        oVersion = fh.read(32).decode('utf-8', errors='replace').strip('\x00')
        oTime = np.fromfile(fh, dtype=np.double, count=1)[0]
        oItems = np.fromfile(fh, dtype=np.int32, count=1)[0]
        oIsLittleEndian = bool(np.fromfile(fh, dtype=np.uint8, count=1)[0])
        BundleHeaderSize = 256
        if oSignature == 'DAT1':
            oBundleItems = None
            isBundled = False
        elif oSignature == 'DAT2':
            oBundleItems = []
            for _ in range(12):
                oStart = np.fromfile(fh, dtype=np.int32, count=1)[0]
                oLength = np.fromfile(fh, dtype=np.int32, count=1)[0]
                oExtension = fh.read(8).decode('utf-8').strip()
                oBundleItems.append({'oStart': oStart, 'oLength': oLength, 'oExtension': oExtension})
            isBundled = True
    else:
        raise ValueError('This legacy file format is not supported')
    littleendianflag = oIsLittleEndian
    return {'oSignature': oSignature, 'oVersion': oVersion, 'oTime': oTime,
            'oItems': oItems, 'oIsLittleEndian': oIsLittleEndian, 'oBundleItems': oBundleItems,
            'BundleHeaderSize': BundleHeaderSize}, littleendianflag, isBundled

def getTree(obj):
    # Main entry point for loading tree
    return getTreeReentrant(obj, 0)

def getTreeReentrant(obj, Level):
    # Recursive routine called from LoadTree
    if obj.opt.fileData.fileExt == '.pul':
        HI_readPulseFileHEKA(obj,Level)

    elif obj.opt.fileData['fileExt'] == '.pgf':
        obj.HI_readStimulusFileHEKA(Level)
    elif obj.opt.fileData['fileExt'] == '.sol':
        obj.HI_readSolutionFileHEKA(Level)
    elif obj.opt.fileData['fileExt'] == '.amp':
        obj.HI_readAmplifierFileHEKA(Level)

    for _ in range(50):
        getTreeReentrant(obj, Level+1)
    return obj.opt.fileData['Tree']

def LocalImportGroup(fh, dataTree, grp, grp_row):
    # Create a structure for the series headers
    # Pad the indices for last series of last group
    grp_row.append(len(dataTree))
    # Collect the series headers and row numbers for this group into a
    # structure array
    ser_row, nseries = getSeriesHeaders(dataTree, grp_row, grp)
    # Pad for last series
    ser_row.append(grp_row[grp+1])
    dataoffsets = []
    # Create the channels
    matData2 = []
    for ser in range(nseries):
        sw_s, sw_row, nsweeps = getSweepHeaders(dataTree, ser_row, ser)
        # Make sure the sweeps are in temporal sequence
        if any(np.diff([item['SwTime'] for item in sw_s]) <= 0):
            raise ValueError('Sweeps not in temporal sequence')
        sw_row.append(ser_row[ser+1])
        # Get the trace headers for this sweep
        tr_row = getTraceHeaders(dataTree, sw_row)
        for k in range(len(tr_row)):
            tr_s, isConstantScaling, isConstantFormat, isFramed = LocalCheckEntries(dataTree, tr_row, k)
            # Check whether interleaving is supported with this file version
            # Note: HEKA added interleaving Jan 2011.
            # TrInterleaveSkip was previously in a filler block, so should always
            # be zero with older files.
            INTERLEAVE_SUPPORTED = tr_s[0]['TrInterleaveSize'] > 0 and tr_s[0]['TrInterleaveSkip'] > 0
            data = np.zeros((max([item['TrDataPoints'] for item in tr_s]), len(tr_row)))
            for tr in range(len(tr_row)):
                fmt, nbytes = LocalFormatToString(tr_s[tr]['TrDataFormat'])
                # Always read into double
                readfmt = np.dtype(fmt).newbyteorder('<').str
                # Skip to start of the data
                fh.seek(dataTree[tr_row[k][tr]][5]['TrData'])
                # Store data offset for later error checks
                dataoffsets.append(dataTree[tr_row[k][tr]][5]['TrData'])
                # Read the data
                if not INTERLEAVE_SUPPORTED or dataTree[tr_row[k][tr]][5]['TrInterleaveSize'] == 0:
                    data[:dataTree[tr_row[k][tr]][5]['TrDataPoints'], tr] = np.fromfile(fh, dtype=readfmt, count=dataTree[tr_row[k][tr]][5]['TrDataPoints'])
                else:
                    offset = 0
                    nelements = int(dataTree[tr_row[k][tr]][5]['TrInterleaveSize'] / nbytes)
                    for nread in range(int(data.size / (dataTree[tr_row[k][tr]][5]['TrInterleaveSize'] / nbytes))):
                        data[offset:offset+nelements], _ = np.fromfile(fh, dtype=readfmt, count=nelements)
                        offset += nelements
                        fh.seek(dataTree[tr_row[k][tr]][5]['TrInterleaveSkip'] - dataTree[tr_row[k][tr]][5]['TrInterleaveSize'], os.SEEK_CUR)
            # Now scale the data to real world units
            # Note we also apply zero adjustment
            for col in range(data.shape[1]):
                data[:, col] = data[:, col] * tr_s[col]['TrDataScaler'] + tr_s[col]['TrZeroData']
            matData2.append(data)
    if len(set(dataoffsets)) < len(dataoffsets):
        print('This should never happen - please report to sigtool@kcl.ac.uk if you see this warning.')
        print('sigTOOL: Unexpected result: Some data blocks appear to have been read more then once')
    return matData2

def LocalFormatToString(n):
    # Convert format number to string and get number of bytes
    if n == 0:
        fmt = 'i2'
        nbytes = 2
    elif n == 1:
        fmt = 'i4'
        nbytes = 4
    elif n == 2:
        fmt = 'f4'
        nbytes = 4
    elif n == 3:
        fmt = 'f8'
        nbytes = 8
    else:
        raise ValueError('Unknown format number')
    return fmt, nbytes

def LocalCheckEntries(tree, tr_row, k):
    # Check units are the same for all traces
    tr_s = [tree[tr][5] for tr in tr_row[k]]
    if len(set([item['TrYUnit'] for item in tr_s])) > 1:
        raise ValueError('Waveform units are not constant')
    if len(set([item['TrXUnit'] for item in tr_s])) > 1:
        raise ValueError('Time units are not constant')
    if len(set([item['TrXInterval'] for item in tr_s])) != 1:
        raise ValueError('Unequal sample intervals')
    # Other unexpected conditions - give user freedom to create these but warn
    # about them
    if len(set([item['TrLabel'] for item in tr_s])) > 1:
        print('Different trace labels')
    if len(set([item['TrAdcChannel'] for item in tr_s])) > 1:
        print('Data collected from different ADC channels')
    if len(set([item['TrRecordingMode'] for item in tr_s])) > 1:
        print('Traces collected using different recording modes')
    if len(set([item['TrCellPotential'] for item in tr_s])) > 1:
        print('Traces collected using different Em')
    # Check scaling factor is constant
    ScaleFactor = set([item['TrDataScaler'] for item in tr_s])
    if len(ScaleFactor) == 1:
        isConstantScaling = True
    else:
        isConstantScaling = False
    #... and data format
    if len(set([item['TrDataFormat'] for item in tr_s])) == 1:
        isConstantFormat = True
    else:
        isConstantFormat = False
    # Do we have constant epoch lengths and offsets?
    if len(set([item['TrDataPoints'] for item in tr_s])) == 1 and len(set([item['TrTimeOffset'] for item in tr_s])) == 1:
        isFramed = True
    else:
        isFramed = False
    return tr_s, isConstantScaling, isConstantFormat, isFramed

def getSeriesHeaders(tree, grp_row, grp):
    # Collect the series headers and row numbers for this group into a
    # structure array
    nseries = 0
    ser_row = []
    for k in range(grp_row[grp]+1, grp_row[grp+1]):
        if tree[k][2] is not None:
            ser_row.append(k)
            nseries += 1
    return ser_row, nseries

def getSweepHeaders(tree, ser_row, ser):
    # Collect the sweep headers and row numbers for this series into a
    # structure array
    nsweeps = 0
    sw_s = []
    sw_row = []
    for k in range(ser_row[ser]+1, ser_row[ser+1]):
        if tree[k][3] is not None:
            sw_s.append(tree[k][3])
            sw_row.append(k)
            nsweeps += 1
    return sw_s, sw_row, nsweeps

def getTraceHeaders(tree, sw_row):
    # Collect the trace headers and row numbers for this sweep into a
    # structure array
    tr_row = [[]]
    for k in range(sw_row[0]+1, sw_row[-1]+1):
        if tree[k][4] is not None:
            tr_row[-1].append(k)
        else:
            tr_row.append([])
    return tr_row

def dict2table(d):
    # Convert dictionary to table
    try:
        import pandas as pd
        return pd.DataFrame(d)
    except ImportError:
        print("Pandas library not available. Please install pandas to use dict2table function.")






class Struct(object):
    """High-level wrapper around struct.Struct that makes it a bit easier to
    unpack large, nested structures.
    """

    field_info = None
    size_check = None
    _fields_parsed = None

    def __init__(self, data, endian="<"):
        """Read the structure from *data* and return an ordered dictionary of
        fields.

        *data* may be a string or file.
        *endian* may be '<' or '>'
        """
        field_info = self._field_info()
        if not isinstance(data, (str, bytes)):
            data = data.read(self._le_struct.size)
        if endian == "<":
            items = self._le_struct.unpack(data)
        elif endian == ">":
            items = self._be_struct.unpack(data)
        else:
            raise ValueError("Invalid endian: %s" % endian)

        fields = collections.OrderedDict()

        i = 0
        for name, fmt, func in field_info:
            # pull item(s) out of the list based on format string
            if len(fmt) == 1 or fmt[-1] == "s":
                item = items[i]
                i += 1
            else:
                n = int(fmt[:-1])
                item = items[i : i + n]
                i += n

            # try unpacking sub-structure
            if isinstance(func, tuple):
                substr, func = func
                item = substr(item, endian)

            # None here means the field should be omitted
            if func is None:
                continue
            # handle custom massaging function
            if func is not True:
                item = func(item)
            fields[name] = item
            setattr(self, name, item)

        self.fields = fields

    @classmethod
    def _field_info(cls):
        if cls._fields_parsed is not None:
            return cls._fields_parsed

        fmt = ""
        fields = []
        for items in cls.field_info:
            if len(items) == 3:
                name, ifmt, func = items
            else:
                name, ifmt = items
                func = True

            if isinstance(ifmt, type) and issubclass(ifmt, Struct):
                func = (
                    ifmt,
                    func,
                )  # instructs to unpack with sub-struct before calling function
                ifmt = "%ds" % ifmt.size()
            elif len(ifmt) > 1 and re.match(r"\d*[xcbB?hHiIlLqQfdspP]", ifmt) is None:
                raise TypeError('Unsupported format string "%s"' % ifmt)

            fields.append((name, ifmt, func))
            fmt += ifmt
        cls._le_struct = struct.Struct("<" + fmt)
        cls._be_struct = struct.Struct(">" + fmt)
        cls._fields_parsed = fields
        if cls.size_check is not None:
            #            print(cls._le_struct.size, cls.size_check)
            assert cls._le_struct.size == cls.size_check
        return fields

    @classmethod
    def size(cls):
        cls._field_info()
        return cls._le_struct.size

    @classmethod
    def array(cls, x):
        """Return a new StructArray class of length *x* and using this struct
        as the array item type.
        """
        return type(
            cls.__name__ + "[%d]" % x,
            (StructArray,),
            {"item_struct": cls, "array_size": x},
        )

    def __repr__(self, indent=0):
        indent_str = "    " * indent
        r = indent_str + "%s(\n" % self.__class__.__name__
        if not hasattr(self, "fields"):
            r = r[:-1] + "<initializing>)"
            return r
        for k, v in self.fields.items():
            if isinstance(v, Struct):
                r += indent_str + "    %s = %s\n" % (
                    k,
                    v.__repr__(indent=indent + 1).lstrip(),
                )
            else:
                r += indent_str + "    %s = %r\n" % (k, v)
        r += indent_str + ")"
        return r

    def get_fields(self):
        """Recursively convert struct fields+values to nested dictionaries."""
        fields = self.fields.copy()
        for k, v in fields.items():
            if isinstance(v, StructArray):
                fields[k] = [x.get_fields() for x in v.array]
            elif isinstance(v, Struct):
                fields[k] = v.get_fields()
        return fields


class StructArray(Struct):
    item_struct = None
    array_size = None

    def __init__(self, data, endian="<"):
        if not isinstance(data, (str, bytes)):
            data = data.read(self.size())
        items = []
        isize = self.item_struct.size()
        for i in range(self.array_size):
            d = data[:isize]
            data = data[isize:]
            items.append(self.item_struct(d, endian))
        self.array = items

    def __getitem__(self, i):
        return self.array[i]

    @classmethod
    def size(self):
        return self.item_struct.size() * self.array_size

    def __repr__(self, indent=0):
        r = "    " * indent + "%s(\n" % self.__class__.__name__
        for item in self.array:
            r += item.__repr__(indent=indent + 1) + ",\n"
        r += "    " * indent + ")"
        return r


def cstr(byt):
    """Convert C string bytes to python string."""
    try:
        ind = byt.index(b"\0")
    except ValueError:
        return byt
    return byt[:ind].decode("utf-8", errors="ignore")


class BundleItem(Struct):
    field_info = [
        ("Start", "i"),
        ("Length", "i"),
        ("Extension", "8s", cstr),
    ]
    size_check = 16


class BundleHeader(Struct):
    ## DAT2 version file
    field_info = [
        ("Signature", "8s", cstr),
        ("Version", "32s", cstr),
        ("Time", "d"),
        ("Items", "i"),
        ("IsLittleEndian", "12s"),
        ("BundleItems", BundleItem.array(12)),
    ]
    size_check = 256


def HI_readPulseFileHEKA(obj, Level):
    # extracts data stored in the "*.pul" file, or the corresponding portion of the bundled ".dat" file

    # Gets one record of the tree and the number of children
    s = getOneRecord(obj, Level)
    #obj.opt.fileData.Tree[obj.opt.fileData.Counter, Level + 1] = s
    #obj.opt.fileData.Position += obj.opt.fileData.Sizes[Level + 1]
    #obj.opt.fileData.fh.seek(obj.opt.fileData.Position, 0)
    #obj.opt.fileData.nchild = np.fromfile(obj.opt.fileData.fh, dtype=np.int32, count=1)[0]
    
    #if obj.opt.fileData.nchild > 10:
    #    pass
    # 
    #obj.opt.fileData.Position = obj.opt.fileData.fh.tell()


def getOneRecord(obj, Level):
    # Gets one record
    obj.opt.fileData.Counter += 1
    switcher = {
        0: getRoot,
        1: getGroup,
        2: getSeries,
        3: getSweep,
        4: getTrace
    }
    func = switcher.get(Level, lambda: "Unexpected Level")
    return func(obj)


def getRoot(obj):
    # Root record
    fh = obj.opt.fileData.fh
    p = {}
    p["RoVersion"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    p["RoMark"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    p["RoVersionName"] = np.fromfile(fh, dtype="S32", count=1)[0].decode("utf-8").strip()  # String32Type
    p["RoAuxFileName"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8").strip()  # String80Type
    p["RoRootText"] = np.fromfile(fh, dtype="S400", count=1)[0].decode("utf-8").strip()  # String400Type
    p["RoStartTime"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    p["RoStartTimeMATLAB"] = 0#obj.HI_time2date(p["RoStartTime"])
    p["RoMaxSamples"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    p["RoCRC"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # CARD32
    p["RoFeatures"] = np.fromfile(fh, dtype=np.int16, count=1)[0]  # SET16
    p["RoFiller1"] = np.fromfile(fh, dtype=np.int16, count=1)[0]  # INT16
    p["RoFiller2"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    p["RoTcEnumerator"] = np.fromfile(fh, dtype=np.int16, count=32)  # ARRAY[0..Max_TcKind_M1] OF INT16
    p["RoTcKind"] = np.fromfile(fh, dtype=np.int8, count=32)  # ARRAY[0..Max_TcKind_M1] OF INT8
    p["RootRecSize"] = 640  # = 80 * 8
    p = orderfields(p)
    obj.opt.fileData.fileVersion = p["RoVersion"]
    return p


def getGroup(obj):
    # Group record
    fh = obj.opt.fileData.fh
    g = {}
    g["GrMark"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    g["GrLabel"] = np.fromfile(fh, dtype="S32", count=1)[0].decode("utf-8").strip()  # String32Size
    g["GrText"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8").strip()  # String80Size
    g["GrExperimentNumber"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    g["GrGroupCount"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    g["GrCRC"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # CARD32
    g["GrMatrixWidth"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GrMatrixHeight"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GrRectBottom"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GrRectLeft"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GrRectTop"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GrRectRight"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    g["GroupRecSize"] = 448  # = 56 * 8
    g = orderfields(g)
    return g


def getSeries(obj):
    # Series record
    fh = obj.opt.fileData.fh
    s = {}
    s["SeMark"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    s["SeLabel"] = np.fromfile(fh, dtype="S32", count=1)[0].decode("utf-8").strip()  # String32Size
    #s["SeText"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8").strip()  # String80Size
    s["SeText"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8", errors="replace").strip()  # String80Size

    s["SeUnit"] = np.fromfile(fh, dtype="S8", count=1)[0].decode("utf-8", errors="replace").strip()  # String8Size
    s["SeRate"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    s["SeStartTime"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    s["SeEndTime"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    s["SeMaxSamples"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    s["SeMaxSampleSize"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    s["SeRate2"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    s["SeCRC"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # CARD32
    s["SeriesRecSize"] = 248  # = 31 * 8
    s = orderfields(s)
    return s


def getSweep(obj):
    # Sweep record
    fh = obj.opt.fileData.fh
    sw = {}
    sw["SwMark"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    sw["SwLabel"] = np.fromfile(fh, dtype="S32", count=1)[0].decode("utf-8", errors="replace").strip()  # String32Size
    sw["SwText"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8", errors="replace").strip()  # String80Size
    sw["SwTime"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    sw["SwFilter"] = np.fromfile(fh, dtype="S2", count=1)[0].decode("utf-8", errors="replace").strip()  # String2Type
    sw["SwKind"] = np.fromfile(fh, dtype=np.int16, count=1)[0]  # INT16
    sw["SwPeriod"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    sw["SwRate"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    sw["SwRate2"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    sw["SwCRC"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # CARD32
    sw["SweepRecSize"] = 144  # = 18 * 8
    sw = orderfields(sw)
    return sw


def getTrace(obj):
    # Trace record
    fh = obj.opt.fileData.fh
    t = {}
    t["TrMark"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    t["TrLabel"] = np.fromfile(fh, dtype="S32", count=1)[0].decode("utf-8", errors="replace").strip()  # String32Size
    t["TrText"] = np.fromfile(fh, dtype="S80", count=1)[0].decode("utf-8", errors="replace").strip()  # String80Size
    t["TrPoints"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    t["TrMaxSamples"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # INT32
    t["TrGain"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    t["TrOffset"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    t["TrRate"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    t["TrRate2"] = np.fromfile(fh, dtype=np.double, count=1)[0]  # LONGREAL
    t["TrCRC"] = np.fromfile(fh, dtype=np.int32, count=1)[0]  # CARD32
    t["TraceRecSize"] = 240  # = 30 * 8
    t = orderfields(t)
    return t


def orderfields(dictionary):
    # Reorders fields in the dictionary
    keys = sorted(dictionary.keys())
    return {k: dictionary[k] for k in keys}