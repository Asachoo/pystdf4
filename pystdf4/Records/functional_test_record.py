from typing import Optional, Sequence

from pystdf4.Core import B_1, I_2, I_4, U_1, U_2, U_4, B_n, C_n, KxU_2

from .base import StdfRecordBase


class FTR(StdfRecordBase):
    """
    Functional Test Record (FTR)

    Function: Contains the results of the single execution of a functional test in the test program. The first occurrence of this record
    also establishes the default values for all semi-static information about the test. The FTR is related to the Test Synopsis Record (TSR)
    by test number, head number, and site number.
    """

    REC_TYP = 15
    REC_SUB = 20
    OPT_FLAG_CONFIG = {
        "CYCL_CNT": 0,
        "REL_VADR": 1,
        "REPT_CNT": 2,
        "NUM_FAIL": 3,
        "XFAIL_AD": 4,
        "YFAIL_AD": 4,
        "VECT_OFF": 5,
    }

    # TODO: Implement PTN_INDX, RTN_STAT, PGM_INDX, PGM_STAT

    TEST_NUM: U_4
    """
    Test number
    """
    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    TEST_FLG: B_1
    """
    Test flags (fail, alarm, etc.)
    """
    OPT_FLAG: B_1
    """
    Optional data flag
    """
    CYCL_CNT: U_4
    """
    Cycle count of vector
    """
    REL_VADR: U_4
    """
    Relative vector address
    """
    REPT_CNT: U_4
    """
    Repeat count of vector
    """
    NUM_FAIL: U_4
    """
    Number of pins with 1 or more failures
    """
    XFAIL_AD: I_4
    """
    X logical device failure address
    """
    YFAIL_AD: I_4
    """
    Y logical device failure address
    """
    VECT_OFF: I_2
    """
    Offset from vector of interest
    """
    RTN_ICNT: U_2
    """
    Count (j) of return data PMR indexesSequence
    """
    PGM_ICNT: U_2
    """
    Count (k) of programmed state indexes
    """
    RTN_INDX: KxU_2
    """
    Array of return data PMR indexes
    """
    RTN_STAT: Sequence[B_n]
    """
    Array of returned states
    """
    PGM_INDX: KxU_2
    """
    Array of programmed state indexes
    """
    PGM_STAT: Sequence[B_n]
    """
    Array of programmed states
    """
    FAIL_PIN: B_n
    """
    Failing pin bitfield
    """
    VECT_NAM: C_n
    """
    Vector module pattern name
    """
    TIME_SET: C_n
    """
    Time set name
    """
    OP_CODE: C_n
    """
    Vector Op Code
    """
    TEST_TXT: C_n
    """
    Descriptive text or label
    """
    ALARM_ID: C_n
    """
    Name of alarm
    """
    PROG_TXT: C_n
    """
    Additional programmed information
    """
    RSLT_TXT: C_n
    """
    Additional result information
    """
    PATG_NUM: U_1
    """
    Pattern generator number
    """
    SPIN_MAP: B_n
    """
    Bit map of enabled comparators
    """

    def __init__(
        self,
        TEST_NUM: int,
        HEAD_NUM: int,
        SITE_NUM: int,
        TEST_FLG: bytes,
        OPT_FLAG: bytes,
        RTN_ICNT: int,
        PGM_ICNT: int,
        CYCL_CNT: int = 0,
        REL_VADR: int = 0,
        REPT_CNT: int = 0,
        NUM_FAIL: int = 0,
        XFAIL_AD: int = 0,
        YFAIL_AD: int = 0,
        VECT_OFF: int = 0,
        RTN_INDX: Optional[Sequence[int]] = None,
        RTN_STAT: Optional[Sequence[bytes]] = None,
        PGM_INDX: Optional[Sequence[int]] = None,
        PGM_STAT: Optional[Sequence[bytes]] = None,
        FAIL_PIN: bytes = b"",
        VECT_NAM: str = "",
        TIME_SET: str = "",
        OP_CODE: str = "",
        TEST_TXT: str = "",
        ALARM_ID: str = "",
        PROG_TXT: str = "",
        RSLT_TXT: str = "",
        PATG_NUM: int = 255,
        SPIN_MAP: bytes = b"",
    ):
        self.TEST_NUM = U_4(TEST_NUM)
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.TEST_FLG = B_1(TEST_FLG)
        self.OPT_FLAG = B_1(OPT_FLAG)
        self.CYCL_CNT = U_4(CYCL_CNT)
        self.REL_VADR = U_4(REL_VADR)
        self.REPT_CNT = U_4(REPT_CNT)
        self.NUM_FAIL = U_4(NUM_FAIL)
        self.XFAIL_AD = I_4(XFAIL_AD)
        self.YFAIL_AD = I_4(YFAIL_AD)
        self.VECT_OFF = I_2(VECT_OFF)
        self.RTN_ICNT = U_2(RTN_ICNT)
        self.PGM_ICNT = U_2(PGM_ICNT)

        # Initialize optional list fields to empty lists if not provided
        self.RTN_INDX = KxU_2(RTN_ICNT, RTN_INDX)
        self.RTN_STAT = KxU_2(RTN_ICNT, RTN_STAT)
        self.PGM_INDX = KxU_2(PGM_ICNT, PGM_INDX)
        self.PGM_STAT = KxU_2(PGM_ICNT, PGM_STAT)

        self.FAIL_PIN = B_n(FAIL_PIN)
        self.VECT_NAM = C_n(VECT_NAM)
        self.TIME_SET = C_n(TIME_SET)
        self.OP_CODE = C_n(OP_CODE)
        self.TEST_TXT = C_n(TEST_TXT)
        self.ALARM_ID = C_n(ALARM_ID)
        self.PROG_TXT = C_n(PROG_TXT)
        self.RSLT_TXT = C_n(RSLT_TXT)
        self.PATG_NUM = U_1(PATG_NUM)
        self.SPIN_MAP = B_n(SPIN_MAP)
