from dataclasses import field, dataclass

from pystdf4.DataType.StdfBinary import B_n, B_1
from pystdf4.DataType.StdfChar import C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4
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
    TEST_NUM: U_4 = U_4()
    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: B_1 = B_1()
    # Parametric test flags (drift, etc.)
    PARM_FLG: B_1 = B_1()
    # Test result
    RESULT: R_4 = R_4()
    # Test description text or label
    TEST_TXT: C_n = C_n()
    # Name of alarm
    ALARM_ID: C_n = C_n()
    # Optional data flag
    OPT_FLAG: B_1 = B_1()
    # Test results scaling exponent
    RES_SCAL: I_1 = I_1()
    # Low limit scaling exponent
    LLM_SCAL: I_1 = I_1()
    # High limit scaling exponent
    HLM_SCAL: I_1 = I_1()
    # Low test limit value
    LO_LIMIT: R_4 = R_4()
    # High test limit value
    HI_LIMIT: R_4 = R_4()
    # Test units
    UNITS: C_n = C_n()
    # ANSI C result format string
    C_RESFMT: C_n = C_n()
    # ANSI C low limit format string
    C_LLMFMT: C_n = C_n()
    # ANSI C high limit format string
    C_HLMFMT: C_n = C_n()
    # Low specification limit value
    LO_SPEC: R_4 = R_4()
    # High specification limit value
    HI_SPEC: R_4 = R_4()


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
    TEST_NUM: U_4 = U_4()
    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: B_1 = B_1()
    # Parametric test flags (drift, etc.)
    PARM_FLG: B_1 = B_1()
    # Count (j) of PMR indexes
    RTN_ICNT: U_2 = U_2()
    # Count (k) of returned results
    RSLT_CNT: U_2 = U_2()
    # Array of returned states
    RTN_STAT: list[B_n] = field(default_factory=list)
    # Array of returned results
    RTN_RSLT: list[R_4] = field(default_factory=list)
    # Descriptive text or label
    TEST_TXT: C_n = C_n()
    # Name of alarm
    ALARM_ID: C_n = C_n()
    # Optional data flag
    OPT_FLAG: B_1 = B_1()
    # Test result scaling exponent
    RES_SCAL: I_1 = I_1()
    # Test low limit scaling exponent
    LLM_SCAL: I_1 = I_1()
    # Test high limit scaling exponent
    HLM_SCAL: I_1 = I_1()
    # Test low limit value
    LO_LIMIT: R_4 = R_4()
    # Test high limit value
    HI_LIMIT: R_4 = R_4()
    # Starting input value (condition)
    START_IN: R_4 = R_4()
    # Increment of input condition
    INCR_IN: R_4 = R_4()
    # Array of PMR indexes
    RTN_INDX: list[U_2] = field(default_factory=list)
    # Units of returned results
    UNITS: C_n = C_n()
    # Input condition units
    UNITS_IN: C_n = C_n()
    # ANSI C result format string
    C_RESFMT: C_n = C_n()
    # ANSI C low limit format string
    C_LLMFMT: C_n = C_n()
    # ANSI C high limit format string
    C_HLMFMT: C_n = C_n()
    # Low specification limit value
    LO_SPEC: R_4 = R_4()
    # High specification limit value
    HI_SPEC: R_4 = R_4()


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
    TEST_NUM: U_4 = U_4()
    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Test flags (fail, alarm, etc.)
    TEST_FLG: B_1 = B_1()
    # Optional data flag
    OPT_FLAG: B_1 = B_1()
    # Cycle count of vector
    CYCL_CNT: U_4 = U_4()
    # Relative vector address
    REL_VADR: U_4 = U_4()
    # Repeat count of vector
    REPT_CNT: U_4 = U_4()
    # Number of pins with 1 or more failures
    NUM_FAIL: U_4 = U_4()
    # X logical device failure address
    XFAIL_AD: I_4 = I_4()
    # Y logical device failure address
    YFAIL_AD: I_4 = I_4()
    # Offset from vector of interest
    VECT_OFF: I_2 = I_2()
    # Count (j) of return data PMR indexes
    RTN_ICNT: U_2 = U_2()
    # Count (k) of programmed state indexes
    PGM_ICNT: U_2 = U_2()
    # Array of return data PMR indexes
    RTN_INDX: list[U_2] = field(default_factory=list)
    # Array of returned states
    RTN_STAT: list[B_n] = field(default_factory=list)
    # Array of programmed state indexes
    PGM_INDX: list[U_2] = field(default_factory=list)
    # Array of programmed states
    PGM_STAT: list[B_n] = field(default_factory=list)
    # Failing pin bitfield
    FAIL_PIN: B_n = B_n()
    # Vector module pattern name
    VECT_NAM: C_n = C_n()
    # Time set name
    TIME_SET: C_n = C_n()
    # Vector Op Code
    OP_CODE: C_n = C_n()
    # Descriptive text or label
    TEST_TXT: C_n = C_n()
    # Name of alarm
    ALARM_ID: C_n = C_n()
    # Additional programmed information
    PROG_TXT: C_n = C_n()
    # Additional result information
    RSLT_TXT: C_n = C_n()
    # Pattern generator number
    PATG_NUM: U_1 = U_1()
    # Bit map of enabled comparators
    SPIN_MAP: B_n = B_n()
