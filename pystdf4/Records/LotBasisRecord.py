from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(1, 10)
class MIR(StdfRecord):
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


@register_record(1, 20)
class MasterResultsRecord(StdfRecord):
    """
    Master Results Record (MRR)

    Contains summary results for the lot.
    """

    REC_TYP = 1
    REC_SUB = 20


@register_record(1, 30)
class PartCountRecord(StdfRecord):
    """
    Part Count Record (PCR)

    Records the number of parts tested for one or all sites.
    """

    REC_TYP = 1
    REC_SUB = 30


@register_record(1, 40)
class HardwareBinRecord(StdfRecord):
    """
    Hardware Bin Record (HBR)

    Stores counts of parts physically placed into hardware bins.
    """

    REC_TYP = 1
    REC_SUB = 40


@register_record(1, 50)
class SoftwareBinRecord(StdfRecord):
    """
    Software Bin Record (SBR)

    Stores counts of parts associated with logical (software) bins.
    """

    REC_TYP = 1
    REC_SUB = 50


@register_record(1, 60)
class PinMapRecord(StdfRecord):
    """
    Pin Map Record (PMR)

    Maps tester channel names to physical and logical pin names.
    """

    REC_TYP = 1
    REC_SUB = 60


@register_record(1, 62)
class PinGroupRecord(StdfRecord):
    """
    Pin Group Record (PGR)

    Associates a pin group name with a set of pins.
    """

    REC_TYP = 1
    REC_SUB = 62


@register_record(1, 63)
class PinListRecord(StdfRecord):
    """
    Pin List Record (PLR)

    Defines display radix and operating mode for pin or pin group lists.
    """

    REC_TYP = 1
    REC_SUB = 63


@register_record(1, 70)
class RetestDataRecord(StdfRecord):
    """
    Retest Data Record (RDR)

    Indicates that the file contains data from retested parts.
    """

    REC_TYP = 1
    REC_SUB = 70


@register_record(1, 80)
class SiteDescriptionRecord(StdfRecord):
    """
    Site Description Record (SDR)

    Contains configuration details for one or more test sites.
    """

    REC_TYP = 1
    REC_SUB = 80
