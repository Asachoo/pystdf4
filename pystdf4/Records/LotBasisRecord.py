from dataclasses import dataclass, field

from pystdf4.DataType.StdfChar import C_1, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(1, 10)
class MIR(StdfRecordBase):
    """
    Master Information Record (MIR)

    Contains lot-level setup and start-time information.
    """

    REC_TYP = 1
    REC_SUB = 10

    # Date and time of job setup
    SETUP_T: U_4 = U_4()
    # Date and time first part tested
    START_T: U_4 = U_4()
    # Tester station number
    STAT_NUM: U_1 = U_1()
    # Test mode code (e.g. prod, dev)
    MODE_COD: C_1 = C_1()
    # Lot retest code
    RTST_COD: C_1 = C_1()
    # Data protection code
    PROT_COD: C_1 = C_1()
    # Burn-in time (in minutes)
    BURN_TIM: U_2 = U_2()
    # Command mode code
    CMOD_COD: C_1 = C_1()
    # Lot ID (customer specified)
    LOT_ID: C_n = C_n()
    # Part Type (or product ID)
    PART_TYP: C_n = C_n()
    # Name of node that generated data
    NODE_NAM: C_n = C_n()
    # Tester type
    TSTR_TYP: C_n = C_n()
    # Job name (test program name)
    JOB_NAM: C_n = C_n()
    # Job (test program) revision number
    JOB_REV: C_n = C_n()
    # Sublot ID
    SBLOT_ID: C_n = C_n()
    # Operator name or ID (at setup time)
    OPER_NAM: C_n = C_n()
    # Tester executive software type
    EXEC_TYP: C_n = C_n()
    # Tester exec software version number
    EXEC_VER: C_n = C_n()
    # Test phase or step code
    TEST_COD: C_n = C_n()
    # Test temperature
    TST_TEMP: C_n = C_n()
    # Generic user text
    USER_TXT: C_n = C_n()
    # Name of auxiliary data file
    AUX_FILE: C_n = C_n()
    # Package type
    PKG_TYP: C_n = C_n()
    # Product family ID
    FAMLY_ID: C_n = C_n()
    # Date code
    DATE_COD: C_n = C_n()
    # Test facility ID
    FACIL_ID: C_n = C_n()
    # Test floor ID
    FLOOR_ID: C_n = C_n()
    # Fabrication process ID
    PROC_ID: C_n = C_n()
    # Operation frequency or step
    OPER_FRQ: C_n = C_n()
    # Test specification name
    SPEC_NAM: C_n = C_n()
    # Test specification version number
    SPEC_VER: C_n = C_n()
    # Test flow ID
    FLOW_ID: C_n = C_n()
    # Test setup ID
    SETUP_ID: C_n = C_n()
    # Device design revision
    DSGN_REV: C_n = C_n()
    # Engineering lot ID
    ENG_ID: C_n = C_n()
    # ROM code ID
    ROM_COD: C_n = C_n()
    # Tester serial number
    SERL_NUM: C_n = C_n()
    # Supervisor name or ID
    SUPR_NAM: C_n = C_n()


@dataclass
@register_record(1, 20)
class MRR(StdfRecordBase):
    """
    Master Results Record (MRR)

    Contains summary results for the lot.
    """

    REC_TYP = 1
    REC_SUB = 20

    # Date and time last part tested
    FINISH_T: U_4 = U_4()
    # Lot disposition code
    DISP_COD: C_1 = C_1()
    # Lot description supplied by user
    USR_DESC: C_n = C_n()
    # Lot description supplied by exec
    EXC_DESC: C_n = C_n()


@dataclass
@register_record(1, 30)
class PCR(StdfRecordBase):
    """
    Part Count Record (PCR)

    Records the number of parts tested for one or all sites.
    """

    REC_TYP = 1
    REC_SUB = 30

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Number of parts tested
    PART_CNT: U_4 = U_4()
    # Number of parts retested
    RTST_CNT: U_4 = U_4()
    # Number of aborts during testing
    ABRT_CNT: U_4 = U_4()
    # Number of good (passed) parts tested
    GOOD_CNT: U_4 = U_4()
    # Number of functional parts tested
    FUNC_CNT: U_4 = U_4()


@dataclass
@register_record(1, 40)
class HBR(StdfRecordBase):
    """
    Hardware Bin Record (HBR)

    Stores counts of parts physically placed into hardware bins.
    """

    REC_TYP = 1
    REC_SUB = 40

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Hardware bin number
    HBIN_NUM: U_2 = U_2()
    # Number of parts in bin
    HBIN_CNT: U_4 = U_4()
    # Pass/fail indication
    HBIN_PF: C_1 = C_1()
    # Hardware bin name
    HBIN_NAM: C_n = C_n()


@dataclass
@register_record(1, 50)
class SBR(StdfRecordBase):
    """
    Software Bin Record (SBR)

    Stores counts of parts associated with logical (software) bins.
    """

    REC_TYP = 1
    REC_SUB = 50

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Software bin number
    SBIN_NUM: U_2 = U_2()
    # Number of parts in bin
    SBIN_CNT: U_4 = U_4()
    # Pass/fail indication
    SBIN_PF: C_1 = C_1()
    # Software bin name
    SBIN_NAM: C_n = C_n()


@dataclass
@register_record(1, 60)
class PMR(StdfRecordBase):
    """
    Pin Map Record (PMR)

    Maps tester channel names to physical and logical pin names.
    """

    REC_TYP = 1
    REC_SUB = 60

    # Unique index associated with pin
    PMR_INDX: U_2 = U_2()
    # Channel type
    CHAN_TYP: U_2 = U_2()
    # Channel name
    CHAN_NAM: C_n = C_n()
    # Physical name of pin
    PHY_NAM: C_n = C_n()
    # Logical name of pin
    LOG_NAM: C_n = C_n()
    # Head number associated with channel
    HEAD_NUM: U_1 = U_1()
    # Site number associated with channel
    SITE_NUM: U_1 = U_1()


@dataclass
@register_record(1, 62)
class PGR(StdfRecordBase):
    """
    Pin Group Record (PGR)

    Associates a pin group name with a set of pins.
    """

    REC_TYP = 1
    REC_SUB = 62

    # TODO: Implement PMR_INDX

    # Unique index associated with pin group
    GRP_INDX: U_2 = U_2()
    # Name of pin group
    GRP_NAM: C_n = C_n()
    # Count (k) of PMR indexes
    INDX_CNT: U_2 = U_2()
    # Array of indexes for pins in the group
    PMR_INDX: list[U_2] = field(default_factory=list)


@dataclass
@register_record(1, 63)
class PLR(StdfRecordBase):
    """
    Pin List Record (PLR)

    Defines display radix and operating mode for pin or pin group lists.
    """

    REC_TYP = 1
    REC_SUB = 63

    # TODO: Implement GRP_INDX, GRP_MODE, GRP_RADX, PGM_CHAR, RTN_CHAR, PGM_CHAL, RTN_CHAL

    # Count (k) of pins or pin groups
    GRP_CNT: U_2 = U_2()
    # Array of pin or pin group indexes
    GRP_INDX: list[U_2] = field(default_factory=list)
    # Operating mode of pin group
    GRP_MODE: list[U_2] = field(default_factory=list)
    # Display radix of pin group
    GRP_RADX: list[U_1] = field(default_factory=list)
    # Program state encoding characters
    PGM_CHAR: list[C_n] = field(default_factory=list)
    # Return state encoding characters
    RTN_CHAR: list[C_n] = field(default_factory=list)
    # Program state encoding characters
    PGM_CHAL: list[C_n] = field(default_factory=list)
    # Return state encoding characters
    RTN_CHAL: list[C_n] = field(default_factory=list)


@dataclass
@register_record(1, 70)
class RDR(StdfRecordBase):
    """
    Retest Data Record (RDR)

    Indicates that the file contains data from retested parts.
    """

    REC_TYP = 1
    REC_SUB = 70

    # TODO: Implement RTST_BIN

    # Number (k) of bins being retested
    NUM_BINS: U_2 = U_2()
    # Array of retest bin numbers
    RTST_BIN: list[U_2] = field(default_factory=list)


@dataclass
@register_record(1, 80)
class SDR(StdfRecordBase):
    """
    Site Description Record (SDR)

    Contains configuration details for one or more test sites.
    """

    REC_TYP = 1
    REC_SUB = 80

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Site group number
    SITE_GRP: U_1 = U_1()
    # Number of test sites in site group
    SITE_CNT: U_1 = U_1()
    # Array of test site numbers
    SITE_NUM: list[U_1] = field(default_factory=list)
    # Handler or prober type
    HAND_TYP: C_n = C_n()
    # Handler or prober ID
    HAND_ID: C_n = C_n()
    # Probe card type
    CARD_TYP: C_n = C_n()
    # Probe card ID
    CARD_ID: C_n = C_n()
    # Load board type
    LOAD_TYP: C_n = C_n()
    # Load board ID
    LOAD_ID: C_n = C_n()
    # DIB board type
    DIB_TYP: C_n = C_n()
    # DIB board ID
    DIB_ID: C_n = C_n()
    # Interface cable type
    CABL_TYP: C_n = C_n()
    # Interface cable ID
    CABL_ID: C_n = C_n()
    # Handler contactor type
    CONT_TYP: C_n = C_n()
    # Handler contactor ID
    CONT_ID: C_n = C_n()
    # Laser type
    LASR_TYP: C_n = C_n()
    # Laser ID
    LASR_ID: C_n = C_n()
    # Extra equipment type field
    EXTR_TYP: C_n = C_n()
    # Extra equipment ID
    EXTR_ID: C_n = C_n()
