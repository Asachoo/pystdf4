from dataclasses import dataclass

from .DataType import U_1, U_2, U_4, C_1, C_n
from .DataType import UInt8, UInt16, UInt32, CharSingle, CharVarLen
from .base import StdfRecordBase, register_record


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
