from dataclasses import field, dataclass

from .DataType import U_1, U_2, U_4, I_2, I_4, B_n, B_1, C_n
from .DataType import UInt8, UInt16, UInt32, Int16, Int32
from .DataType import BinarySingle, BinaryVarLen, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(15, 20)
class FTR(StdfRecordBase):
    """
    Functional Test Record (FTR)

    Function: Contains the results of the single execution of a functional test in the test program. The first occurrence of this record also establishes the default values for all semi-static information about the test. The FTR is related to the Test Synopsis Record (TSR) by test number, head number, and site number.
    """

    REC_TYP = 15
    REC_SUB = 20

    # TODO: Implement PTN_INDX, RTN_STAT, PGM_INDX, PGM_STAT

    TEST_NUM: UInt32 = U_4()
    """
    Test number
    """
    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    TEST_FLG: BinarySingle = B_1()
    """
    Test flags (fail, alarm, etc.)
    """
    OPT_FLAG: BinarySingle = B_1()
    """
    Optional data flag
    """
    CYCL_CNT: UInt32 = U_4()
    """
    Cycle count of vector
    """
    REL_VADR: UInt32 = U_4()
    """
    Relative vector address
    """
    REPT_CNT: UInt32 = U_4()
    """
    Repeat count of vector
    """
    NUM_FAIL: UInt32 = U_4()
    """
    Number of pins with 1 or more failures
    """
    XFAIL_AD: Int32 = I_4()
    """
    X logical device failure address
    """
    YFAIL_AD: Int32 = I_4()
    """
    Y logical device failure address
    """
    VECT_OFF: Int16 = I_2()
    """
    Offset from vector of interest
    """
    RTN_ICNT: UInt16 = U_2()
    """
    Count (j) of return data PMR indexes
    """
    PGM_ICNT: UInt16 = U_2()
    """
    Count (k) of programmed state indexes
    """
    RTN_INDX: list[U_2] = field(default_factory=list)
    """
    Array of return data PMR indexes
    """
    RTN_STAT: list[B_n] = field(default_factory=list)
    """
    Array of returned states
    """
    PGM_INDX: list[U_2] = field(default_factory=list)
    """
    Array of programmed state indexes
    """
    PGM_STAT: list[B_n] = field(default_factory=list)
    """
    Array of programmed states
    """
    FAIL_PIN: BinaryVarLen = B_n()
    """
    Failing pin bitfield
    """
    VECT_NAM: CharVarLen = C_n()
    """
    Vector module pattern name
    """
    TIME_SET: CharVarLen = C_n()
    """
    Time set name
    """
    OP_CODE: CharVarLen = C_n()
    """
    Vector Op Code
    """
    TEST_TXT: CharVarLen = C_n()
    """
    Descriptive text or label
    """
    ALARM_ID: CharVarLen = C_n()
    """
    Name of alarm
    """
    PROG_TXT: CharVarLen = C_n()
    """
    Additional programmed information
    """
    RSLT_TXT: CharVarLen = C_n()
    """
    Additional result information
    """
    PATG_NUM: UInt8 = U_1()
    """
    Pattern generator number
    """
    SPIN_MAP: BinaryVarLen = B_n()
    """
    Bit map of enabled comparators
    """
