from typing import Literal

from pystdf4.Core import C_1, U_1, U_2, U_4, C_n

from .base import StdfRecordBase


class MIR(StdfRecordBase):
    """
    Master Information Record (MIR)

    Function: The MIR and the MRR (Master Results Record) contain all the global information that is to be stored for a tested lot of parts.
    Each data stream must have exactly one MIR, immediately after the FAR (and the ATRs, if they are used). This will allow any data
    reporting or analysis programs access to this information in the shortest possible amount of time.
    """

    REC_TYP = 1
    REC_SUB = 10

    SETUP_T: U_4
    """
    Date and time of job setup
    """
    START_T: U_4
    """
    Date and time first part tested
    """
    STAT_NUM: U_1
    """
    Tester station number
    """
    MODE_COD: C_1
    """
    Test mode code (e.g. prod, dev)
    """
    RTST_COD: C_1
    """
    Lot retest code
    """
    PROT_COD: C_1
    """
    Data protection code
    """
    BURN_TIM: U_2
    """
    Burn-in time (in minutes)
    """
    CMOD_COD: C_1
    """
    Command mode code
    """
    LOT_ID: C_n
    """
    Lot ID (customer specified)
    """
    PART_TYP: C_n
    """
    Part Type (or product ID)
    """
    NODE_NAM: C_n
    """
    Name of node that generated data
    """
    TSTR_TYP: C_n
    """
    Tester type
    """
    JOB_NAM: C_n
    """
    Job name (test program name)
    """
    JOB_REV: C_n
    """
    Job (test program) revision number
    """
    SBLOT_ID: C_n
    """
    Sublot ID
    """
    OPER_NAM: C_n
    """
    Operator name or ID (at setup time)
    """
    EXEC_TYP: C_n
    """
    Tester executive software type
    """
    EXEC_VER: C_n
    """
    Tester exec software version number
    """
    TEST_COD: C_n
    """
    Test phase or step code
    """
    TST_TEMP: C_n
    """
    Test temperature
    """
    USER_TXT: C_n
    """
    Generic user text
    """
    AUX_FILE: C_n
    """
    Name of auxiliary data file
    """
    PKG_TYP: C_n
    """
    Package type
    """
    FAMLY_ID: C_n
    """
    Product family ID
    """
    DATE_COD: C_n
    """
    Date code
    """
    FACIL_ID: C_n
    """
    Test facility ID
    """
    FLOOR_ID: C_n
    """
    Test floor ID
    """
    PROC_ID: C_n
    """
    Fabrication process ID
    """
    OPER_FRQ: C_n
    """
    Operation frequency or step
    """
    SPEC_NAM: C_n
    """
    Test specification name
    """
    SPEC_VER: C_n
    """
    Test specification version number
    """
    FLOW_ID: C_n
    """
    Test flow ID
    """
    SETUP_ID: C_n
    """
    Test setup ID
    """
    DSGN_REV: C_n
    """
    Device design revision
    """
    ENG_ID: C_n
    """
    Engineering lot ID
    """
    ROM_COD: C_n
    """
    ROM code ID
    """
    SERL_NUM: C_n
    """
    Tester serial number
    """
    SUPR_NAM: C_n
    """
    Supervisor name or ID
    """

    def __init__(
        self,
        SETUP_T: int,
        START_T: int,
        STAT_NUM: int,
        LOT_ID: str,
        PART_TYP: str,
        NODE_NAM: str,
        TSTR_TYP: str,
        JOB_NAM: str,
        MODE_COD: Literal[
            "A",
            "C",
            "D",
            "E",
            "M",
            "P",
            "Q",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            " ",
        ] = " ",
        RTST_COD: Literal["Y", "N", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "] = " ",
        PROT_COD: str = " ",
        BURN_TIM: int = 65535,
        CMOD_COD: str = " ",
        JOB_REV: str = "",
        SBLOT_ID: str = "",
        OPER_NAM: str = "",
        EXEC_TYP: str = "",
        EXEC_VER: str = "",
        TEST_COD: str = "",
        TST_TEMP: str = "",
        USER_TXT: str = "",
        AUX_FILE: str = "",
        PKG_TYP: str = "",
        FAMLY_ID: str = "",
        DATE_COD: str = "",
        FACIL_ID: str = "",
        FLOOR_ID: str = "",
        PROC_ID: str = "",
        OPER_FRQ: str = "",
        SPEC_NAM: str = "",
        SPEC_VER: str = "",
        FLOW_ID: str = "",
        SETUP_ID: str = "",
        DSGN_REV: str = "",
        ENG_ID: str = "",
        ROM_COD: str = "",
        SERL_NUM: str = "",
        SUPR_NAM: str = "",
    ):
        self.SETUP_T = U_4(SETUP_T)
        self.START_T = U_4(START_T)
        self.STAT_NUM = U_1(STAT_NUM)
        self.MODE_COD = C_1(MODE_COD)
        self.RTST_COD = C_1(RTST_COD)
        self.PROT_COD = C_1(PROT_COD)
        self.BURN_TIM = U_2(BURN_TIM)
        self.CMOD_COD = C_1(CMOD_COD)
        self.LOT_ID = C_n(LOT_ID)
        self.PART_TYP = C_n(PART_TYP)
        self.NODE_NAM = C_n(NODE_NAM)
        self.TSTR_TYP = C_n(TSTR_TYP)
        self.JOB_NAM = C_n(JOB_NAM)
        self.JOB_REV = C_n(JOB_REV)
        self.SBLOT_ID = C_n(SBLOT_ID)
        self.OPER_NAM = C_n(OPER_NAM)
        self.EXEC_TYP = C_n(EXEC_TYP)
        self.EXEC_VER = C_n(EXEC_VER)
        self.TEST_COD = C_n(TEST_COD)
        self.TST_TEMP = C_n(TST_TEMP)
        self.USER_TXT = C_n(USER_TXT)
        self.AUX_FILE = C_n(AUX_FILE)
        self.PKG_TYP = C_n(PKG_TYP)
        self.FAMLY_ID = C_n(FAMLY_ID)
        self.DATE_COD = C_n(DATE_COD)
        self.FACIL_ID = C_n(FACIL_ID)
        self.FLOOR_ID = C_n(FLOOR_ID)
        self.PROC_ID = C_n(PROC_ID)
        self.OPER_FRQ = C_n(OPER_FRQ)
        self.SPEC_NAM = C_n(SPEC_NAM)
        self.SPEC_VER = C_n(SPEC_VER)
        self.FLOW_ID = C_n(FLOW_ID)
        self.SETUP_ID = C_n(SETUP_ID)
        self.DSGN_REV = C_n(DSGN_REV)
        self.ENG_ID = C_n(ENG_ID)
        self.ROM_COD = C_n(ROM_COD)
        self.SERL_NUM = C_n(SERL_NUM)
        self.SUPR_NAM = C_n(SUPR_NAM)
