from dataclasses import field, dataclass

from .DataType import U_1, U_2, U_4, I_1, R_4, B_n, B_1, C_n
from .DataType import UInt8, UInt16, UInt32, Int8, Float32
from .DataType import BinarySingle, CharVarLen
from .base import StdfRecordBase, register_record



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

