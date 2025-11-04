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

    Contains results for a single execution of a parametric test.
    """

    REC_TYP = 15
    REC_SUB = 10

    # Test number
    TEST_NUM: UInt32 = U_4()
    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: BinarySingle = B_1()
    # Parametric test flags (drift, etc.)
    PARM_FLG: BinarySingle = B_1()
    # Test result
    RESULT: Float32 = R_4()
    # Test description text or label
    TEST_TXT: CharVarLen = C_n()
    # Name of alarm
    ALARM_ID: CharVarLen = C_n()
    # Optional data flag
    OPT_FLAG: BinarySingle = B_1()
    # Test results scaling exponent
    RES_SCAL: Int8 = I_1()
    # Low limit scaling exponent
    LLM_SCAL: Int8 = I_1()
    # High limit scaling exponent
    HLM_SCAL: Int8 = I_1()
    # Low test limit value
    LO_LIMIT: Float32 = R_4()
    # High test limit value
    HI_LIMIT: Float32 = R_4()
    # Test units
    UNITS: CharVarLen = C_n()
    # ANSI C result format string
    C_RESFMT: CharVarLen = C_n()
    # ANSI C low limit format string
    C_LLMFMT: CharVarLen = C_n()
    # ANSI C high limit format string
    C_HLMFMT: CharVarLen = C_n()
    # Low specification limit value
    LO_SPEC: Float32 = R_4()
    # High specification limit value
    HI_SPEC: Float32 = R_4()


@dataclass
@register_record(15, 15)
class MPR(StdfRecordBase):
    """
    Multiple-Result Parametric Record (MPR)

    Contains results for a parametric test that returns multiple values.
    """

    REC_TYP = 15
    REC_SUB = 15

    # TODO: Implement RTN_STAT, RTN_RSLT, RTN_INDX

    # Test number
    TEST_NUM: UInt32 = U_4()
    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: BinarySingle = B_1()
    # Parametric test flags (drift, etc.)
    PARM_FLG: BinarySingle = B_1()
    # Count (j) of PMR indexes
    RTN_ICNT: UInt16 = U_2()
    # Count (k) of returned results
    RSLT_CNT: UInt16 = U_2()
    # Array of returned states
    RTN_STAT: list[B_n] = field(default_factory=list)
    # Array of returned results
    RTN_RSLT: list[R_4] = field(default_factory=list)
    # Descriptive text or label
    TEST_TXT: CharVarLen = C_n()
    # Name of alarm
    ALARM_ID: CharVarLen = C_n()
    # Optional data flag
    OPT_FLAG: BinarySingle = B_1()
    # Test result scaling exponent
    RES_SCAL: Int8 = I_1()
    # Test low limit scaling exponent
    LLM_SCAL: Int8 = I_1()
    # Test high limit scaling exponent
    HLM_SCAL: Int8 = I_1()
    # Test low limit value
    LO_LIMIT: Float32 = R_4()
    # Test high limit value
    HI_LIMIT: Float32 = R_4()
    # Starting input value (condition)
    START_IN: Float32 = R_4()
    # Increment of input condition
    INCR_IN: Float32 = R_4()
    # Array of PMR indexes
    RTN_INDX: list[U_2] = field(default_factory=list)
    # Units of returned results
    UNITS: CharVarLen = C_n()
    # Input condition units
    UNITS_IN: CharVarLen = C_n()
    # ANSI C result format string
    C_RESFMT: CharVarLen = C_n()
    # ANSI C low limit format string
    C_LLMFMT: CharVarLen = C_n()
    # ANSI C high limit format string
    C_HLMFMT: CharVarLen = C_n()
    # Low specification limit value
    LO_SPEC: Float32 = R_4()
    # High specification limit value
    HI_SPEC: Float32 = R_4()


@dataclass
@register_record(15, 20)
class FTR(StdfRecordBase):
    """
    Functional Test Record (FTR)

    Contains results for a single execution of a functional test.
    """

    REC_TYP = 15
    REC_SUB = 20

    # TODO: Implement PTN_INDX, RTN_STAT, PGM_INDX, PGM_STAT

    # Test number
    TEST_NUM: UInt32 = U_4()
    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: BinarySingle = B_1()
    # Optional data flag
    OPT_FLAG: BinarySingle = B_1()
    # Cycle count of vector
    CYCL_CNT: UInt32 = U_4()
    # Relative vector address
    REL_VADR: UInt32 = U_4()
    # Repeat count of vector
    REPT_CNT: UInt32 = U_4()
    # Number of pins with 1 or more failures
    NUM_FAIL: UInt32 = U_4()
    # X logical device failure address
    XFAIL_AD: Int32 = I_4()
    # Y logical device failure address
    YFAIL_AD: Int32 = I_4()
    # Offset from vector of interest
    VECT_OFF: Int16 = I_2()
    # Count (j) of return data PMR indexes
    RTN_ICNT: UInt16 = U_2()
    # Count (k) of programmed state indexes
    PGM_ICNT: UInt16 = U_2()
    # Array of return data PMR indexes
    RTN_INDX: list[U_2] = field(default_factory=list)
    # Array of returned states
    RTN_STAT: list[B_n] = field(default_factory=list)
    # Array of programmed state indexes
    PGM_INDX: list[U_2] = field(default_factory=list)
    # Array of programmed states
    PGM_STAT: list[B_n] = field(default_factory=list)
    # Failing pin bitfield
    FAIL_PIN: BinaryVarLen = B_n()
    # Vector module pattern name
    VECT_NAM: CharVarLen = C_n()
    # Time set name
    TIME_SET: CharVarLen = C_n()
    # Vector Op Code
    OP_CODE: CharVarLen = C_n()
    # Descriptive text or label
    TEST_TXT: CharVarLen = C_n()
    # Name of alarm
    ALARM_ID: CharVarLen = C_n()
    # Additional programmed information
    PROG_TXT: CharVarLen = C_n()
    # Additional result information
    RSLT_TXT: CharVarLen = C_n()
    # Pattern generator number
    PATG_NUM: UInt8 = U_1()
    # Bit map of enabled comparators
    SPIN_MAP: BinaryVarLen = B_n()
