from dataclasses import dataclass, field

from .DataType import U_1, U_2, U_4, C_1, C_n
from .DataType import UInt8, UInt16, UInt32, CharSingle, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(1, 10)
class MIR(StdfRecordBase):
    """
    Master Information Record (MIR)

    Function: The MIR and the MRR (Master Results Record) contain all the global information that is to be stored for a tested lot of parts. Each data stream must have exactly one MIR, immediately after the FAR (and the ATRs, if they are used). This will allow any data reporting or analysis programs access to this information in the shortest possible amount of time.
    """

    REC_TYP = 1
    REC_SUB = 10

    SETUP_T: UInt32 = U_4()
    """
    Date and time of job setup
    """
    START_T: UInt32 = U_4()
    """
    Date and time first part tested
    """
    STAT_NUM: UInt8 = U_1()
    """
    Tester station number
    """
    MODE_COD: CharSingle = C_1()
    """
    Test mode code (e.g. prod, dev)
    """
    RTST_COD: CharSingle = C_1()
    """
    Lot retest code
    """
    PROT_COD: CharSingle = C_1()
    """
    Data protection code
    """
    BURN_TIM: UInt16 = U_2()
    """
    Burn-in time (in minutes)
    """
    CMOD_COD: CharSingle = C_1()
    """
    Command mode code
    """
    LOT_ID: CharVarLen = C_n()
    """
    Lot ID (customer specified)
    """
    PART_TYP: CharVarLen = C_n()
    """
    Part Type (or product ID)
    """
    NODE_NAM: CharVarLen = C_n()
    """
    Name of node that generated data
    """
    TSTR_TYP: CharVarLen = C_n()
    """
    Tester type
    """
    JOB_NAM: CharVarLen = C_n()
    """
    Job name (test program name)
    """
    JOB_REV: CharVarLen = C_n()
    """
    Job (test program) revision number
    """
    SBLOT_ID: CharVarLen = C_n()
    """
    Sublot ID
    """
    OPER_NAM: CharVarLen = C_n()
    """
    Operator name or ID (at setup time)
    """
    EXEC_TYP: CharVarLen = C_n()
    """
    Tester executive software type
    """
    EXEC_VER: CharVarLen = C_n()
    """
    Tester exec software version number
    """
    TEST_COD: CharVarLen = C_n()
    """
    Test phase or step code
    """
    TST_TEMP: CharVarLen = C_n()
    """
    Test temperature
    """
    USER_TXT: CharVarLen = C_n()
    """
    Generic user text
    """
    AUX_FILE: CharVarLen = C_n()
    """
    Name of auxiliary data file
    """
    PKG_TYP: CharVarLen = C_n()
    """
    Package type
    """
    FAMLY_ID: CharVarLen = C_n()
    """
    Product family ID
    """
    DATE_COD: CharVarLen = C_n()
    """
    Date code
    """
    FACIL_ID: CharVarLen = C_n()
    """
    Test facility ID
    """
    FLOOR_ID: CharVarLen = C_n()
    """
    Test floor ID
    """
    PROC_ID: CharVarLen = C_n()
    """
    Fabrication process ID
    """
    OPER_FRQ: CharVarLen = C_n()
    """
    Operation frequency or step
    """
    SPEC_NAM: CharVarLen = C_n()
    """
    Test specification name
    """
    SPEC_VER: CharVarLen = C_n()
    """
    Test specification version number
    """
    FLOW_ID: CharVarLen = C_n()
    """
    Test flow ID
    """
    SETUP_ID: CharVarLen = C_n()
    """
    Test setup ID
    """
    DSGN_REV: CharVarLen = C_n()
    """
    Device design revision
    """
    ENG_ID: CharVarLen = C_n()
    """
    Engineering lot ID
    """
    ROM_COD: CharVarLen = C_n()
    """
    ROM code ID
    """
    SERL_NUM: CharVarLen = C_n()
    """
    Tester serial number
    """
    SUPR_NAM: CharVarLen = C_n()
    """
    Supervisor name or ID
    """


@dataclass
@register_record(1, 20)
class MRR(StdfRecordBase):
    """
    Master Results Record (MRR)

    Function: The Master Results Record (MRR) is a logical extension of the Master Information Record (MIR). The data can be thought of as belonging with the MIR, but it is not available when the tester writes the MIR information. Each data stream must have exactly one MRR as the last record in the data stream.
    """

    REC_TYP = 1
    REC_SUB = 20

    FINISH_T: UInt32 = U_4()
    """
    Date and time last part tested
    """
    DISP_COD: CharSingle = C_1()
    """
    Lot disposition code
    """
    USR_DESC: CharVarLen = C_n()
    """
    Lot description supplied by user
    """
    EXC_DESC: CharVarLen = C_n()
    """
    Lot description supplied by exec
    """


@dataclass
@register_record(1, 30)
class PCR(StdfRecordBase):
    """
    Part Count Record (PCR)

    Function: Contains the part count totals for one or all test sites. Each data stream must have at least one PCR to show the part count.
    """

    REC_TYP = 1
    REC_SUB = 30

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    PART_CNT: UInt32 = U_4()
    """
    Number of parts tested
    """
    RTST_CNT: UInt32 = U_4()
    """
    Number of parts retested
    """
    ABRT_CNT: UInt32 = U_4()
    """
    Number of aborts during testing
    """
    GOOD_CNT: UInt32 = U_4()
    """
    Number of good (passed) parts tested
    """
    FUNC_CNT: UInt32 = U_4()
    """
    Number of functional parts tested
    """


@dataclass
@register_record(1, 40)
class HBR(StdfRecordBase):
    """
    Hardware Bin Record (HBR)

    Function: Stores a count of the parts “physically” placed in a particular bin after testing. (In wafer testing, “physical” binning is not an actual transfer of the chip, but rather is represented by a drop of ink or an entry in a wafer map file.) This bin count can be for a single test site (when parallel testing) or a total for all test sites. The STDF specification also supports a Software Bin Record (SBR) for logical binning categories. A part is “physically” placed in a hardware bin after testing. A part can be “logically” associated with a software bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 40

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    HBIN_NUM: UInt16 = U_2()
    """
    Hardware bin number
    """
    HBIN_CNT: UInt32 = U_4()
    """
    Number of parts in bin
    """
    HBIN_PF: CharSingle = C_1()
    """
    Pass/fail indication
    """
    HBIN_NAM: CharVarLen = C_n()
    """
    Hardware bin name
    """


@dataclass
@register_record(1, 50)
class SBR(StdfRecordBase):
    """
    Software Bin Record (SBR)

    Function: Stores a count of the parts associated with a particular logical bin after testing. This bin count can be for a single test site (when parallel testing) or a total for all test sites. The STDF specification also supports a Hardware Bin Record (HBR) for actual physical binning. A part is “physically” placed in a hardware bin after testing. A part can be “logically” associated with a software bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 50

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    SBIN_NUM: UInt16 = U_2()
    """
    Software bin number
    """
    SBIN_CNT: UInt32 = U_4()
    """
    Number of parts in bin
    """
    SBIN_PF: CharSingle = C_1()
    """
    Pass/fail indication
    """
    SBIN_NAM: CharVarLen = C_n()
    """
    Software bin name
    """


@dataclass
@register_record(1, 60)
class PMR(StdfRecordBase):
    """
    Pin Map Record (PMR)

    Function: Provides indexing of tester channel names, and maps them to physical and logical pin names. Each PMR defines the information for a single channel/pin combination. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 60

    PMR_INDX: UInt16 = U_2()
    """
    Unique index associated with pin
    """
    CHAN_TYP: UInt16 = U_2()
    """
    Channel type
    """
    CHAN_NAM: CharVarLen = C_n()
    """
    Channel name
    """
    PHY_NAM: CharVarLen = C_n()
    """
    Physical name of pin
    """
    LOG_NAM: CharVarLen = C_n()
    """
    Logical name of pin
    """
    HEAD_NUM: UInt8 = U_1()
    """
    Head number associated with channel
    """
    SITE_NUM: UInt8 = U_1()
    """
    Site number associated with channel
    """


@dataclass
@register_record(1, 62)
class PGR(StdfRecordBase):
    """
    Pin Group Record (PGR)

    Function: Associates a name with a group of pins. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 62

    GRP_INDX: UInt16 = U_2()
    """
    Unique index associated with pin group
    """
    GRP_NAM: CharVarLen = C_n()
    """
    Name of pin group
    """
    INDX_CNT: UInt16 = U_2()
    """
    Count (k) of PMR indexes
    """
    PMR_INDX: list[U_2] = field(default_factory=list)
    """
    Array of indexes for pins in the group
    """


@dataclass
@register_record(1, 63)
class PLR(StdfRecordBase):
    """
    Pin List Record (PLR)

    Function: Defines the current display radix and operating mode for a pin or pin group. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 63

    GRP_CNT: UInt16 = U_2()
    """
    Count (k) of pins or pin groups
    """
    GRP_INDX: list[U_2] = field(default_factory=list)
    """
    Array of pin or pin group indexes
    """
    GRP_MODE: list[U_2] = field(default_factory=list)
    """
    Operating mode of pin group
    """
    GRP_RADX: list[U_1] = field(default_factory=list)
    """
    Display radix of pin group
    """
    PGM_CHAR: list[C_n] = field(default_factory=list)
    """
    Program state encoding characters
    """
    RTN_CHAR: list[C_n] = field(default_factory=list)
    """
    Return state encoding characters
    """
    PGM_CHAL: list[C_n] = field(default_factory=list)
    """
    Program state encoding characters
    """
    RTN_CHAL: list[C_n] = field(default_factory=list)
    """
    Return state encoding characters
    """


@dataclass
@register_record(1, 70)
class RDR(StdfRecordBase):
    """
    Retest Data Record (RDR)

    Function: Signals that the data in this STDF file is for retested parts. The data in this record, combined with information in the MIR, tells data filtering programs what data to replace when processing retest data.
    """

    REC_TYP = 1
    REC_SUB = 70

    NUM_BINS: UInt16 = U_2()
    """
    Number (k) of bins being retested
    """
    RTST_BIN: list[U_2] = field(default_factory=list)
    """
    Array of retest bin numbers
    """


@dataclass
@register_record(1, 80)
class SDR(StdfRecordBase):
    """
    Site Description Record (SDR)

    Function: Contains the configuration information for one or more test sites, connected to one test head, that compose a site group.
    """

    REC_TYP = 1
    REC_SUB = 80

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_GRP: UInt8 = U_1()
    """
    Site group number
    """
    SITE_CNT: UInt8 = U_1()
    """
    Number of test sites in site group
    """
    SITE_NUM: list[U_1] = field(default_factory=list)
    """
    Array of test site numbers
    """
    HAND_TYP: CharVarLen = C_n()
    """
    Handler or prober type
    """
    HAND_ID: CharVarLen = C_n()
    """
    Handler or prober ID
    """
    CARD_TYP: CharVarLen = C_n()
    """
    Probe card type
    """
    CARD_ID: CharVarLen = C_n()
    """
    Probe card ID
    """
    LOAD_TYP: CharVarLen = C_n()
    """
    Load board type
    """
    LOAD_ID: CharVarLen = C_n()
    """
    Load board ID
    """
    DIB_TYP: CharVarLen = C_n()
    """
    DIB board type
    """
    DIB_ID: CharVarLen = C_n()
    """
    DIB board ID
    """
    CABL_TYP: CharVarLen = C_n()
    """
    Interface cable type
    """
    CABL_ID: CharVarLen = C_n()
    """
    Interface cable ID
    """
    CONT_TYP: CharVarLen = C_n()
    """
    Handler contactor type
    """
    CONT_ID: CharVarLen = C_n()
    """
    Handler contactor ID
    """
    LASR_TYP: CharVarLen = C_n()
    """
    Laser type
    """
    LASR_ID: CharVarLen = C_n()
    """
    Laser ID
    """
    EXTR_TYP: CharVarLen = C_n()
    """
    Extra equipment type field
    """
    EXTR_ID: CharVarLen = C_n()
    """
    Extra equipment ID
    """
