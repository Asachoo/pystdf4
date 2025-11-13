from dataclasses import field, dataclass

from .DataType import U_1, U_2, U_4, I_1, I_2, I_4, R_4, B_n, B_1, C_n
from .DataType import UInt8, UInt16, UInt32, Int8, Int16, Int32, Float32
from .DataType import BinarySingle, BinaryVarLen, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(15, 10)
class PTR(StdfRecordBase):
    """
    Parametric Test Record (PTR)

    Function: Contains the results of a single execution of a parametric test in the test program. The first occurrence of this record also establishes the default values for all semi-static information about the test, such as limits, units, and scaling. The PTR is related to the Test Synopsis Record (TSR) by test number, head number, and site number.
    """

    REC_TYP = 15
    REC_SUB = 10

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
    PARM_FLG: BinarySingle = B_1()
    """
    Parametric test flags (drift, etc.)
    """
    RESULT: Float32 = R_4()
    """
    Test result
    """
    TEST_TXT: CharVarLen = C_n()
    """
    Test description text or label
    """
    ALARM_ID: CharVarLen = C_n()
    """
    Name of alarm
    """
    OPT_FLAG: BinarySingle = B_1()
    """
    Optional data flag
    """
    RES_SCAL: Int8 = I_1()
    """
    Test results scaling exponent
    """
    LLM_SCAL: Int8 = I_1()
    """
    Low limit scaling exponent
    """
    HLM_SCAL: Int8 = I_1()
    """
    High limit scaling exponent
    """
    LO_LIMIT: Float32 = R_4()
    """
    Low test limit value
    """
    HI_LIMIT: Float32 = R_4()
    """
    High test limit value
    """
    UNITS: CharVarLen = C_n()
    """
    Test units
    """
    C_RESFMT: CharVarLen = C_n()
    """
    ANSI C result format string
    """
    C_LLMFMT: CharVarLen = C_n()
    """
    ANSI C low limit format string
    """
    C_HLMFMT: CharVarLen = C_n()
    """
    ANSI C high limit format string
    """
    LO_SPEC: Float32 = R_4()
    """
    Low specification limit value
    """
    HI_SPEC: Float32 = R_4()
    """
    High specification limit value
    """


@dataclass
@register_record(15, 15)
class MPR(StdfRecordBase):
    """
    Multiple-Result Parametric Record (MPR)

    Function: Contains the results of a single execution of a parametric test in the test program where that test returns multiple values. The first occurrence of this record also establishes the default values for all semi-static information about the test, such as limits, units, and scaling. The MPR is related to the Test Synopsis Record (TSR) by test number, head number, and site number.
    """

    REC_TYP = 15
    REC_SUB = 15

    # TODO: Implement RTN_STAT, RTN_RSLT, RTN_INDX

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
    PARM_FLG: BinarySingle = B_1()
    """
    Parametric test flags (drift, etc.)
    """
    RTN_ICNT: UInt16 = U_2()
    """
    Count (j) of PMR indexes
    """
    RSLT_CNT: UInt16 = U_2()
    """
    Count (k) of returned results
    """
    RTN_STAT: list[B_n] = field(default_factory=list)
    """
    Array of returned states
    """
    RTN_RSLT: list[R_4] = field(default_factory=list)
    """
    Array of returned results
    """
    TEST_TXT: CharVarLen = C_n()
    """
    Descriptive text or label
    """
    ALARM_ID: CharVarLen = C_n()
    """
    Name of alarm
    """
    OPT_FLAG: BinarySingle = B_1()
    """
    Optional data flag
    """
    RES_SCAL: Int8 = I_1()
    """
    Test result scaling exponent
    """
    LLM_SCAL: Int8 = I_1()
    """
    Test low limit scaling exponent
    """
    HLM_SCAL: Int8 = I_1()
    """
    Test high limit scaling exponent
    """
    LO_LIMIT: Float32 = R_4()
    """
    Test low limit value
    """
    HI_LIMIT: Float32 = R_4()
    """
    Test high limit value
    """
    START_IN: Float32 = R_4()
    """
    Starting input value (condition)
    """
    INCR_IN: Float32 = R_4()
    """
    Increment of input condition
    """
    RTN_INDX: list[U_2] = field(default_factory=list)
    """
    Array of PMR indexes
    """
    UNITS: CharVarLen = C_n()
    """
    Units of returned results
    """
    UNITS_IN: CharVarLen = C_n()
    """
    Input condition units
    """
    C_RESFMT: CharVarLen = C_n()
    """
    ANSI C result format string
    """
    C_LLMFMT: CharVarLen = C_n()
    """
    ANSI C low limit format string
    """
    C_HLMFMT: CharVarLen = C_n()
    """
    ANSI C high limit format string
    """
    LO_SPEC: Float32 = R_4()
    """
    Low specification limit value
    """
    HI_SPEC: Float32 = R_4()
    """
    High specification limit value
    """


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
