from dataclasses import dataclass

from .DataType import U_1, U_4, I_1, R_4, B_1, C_n
from .DataType import UInt8, UInt32, Int8, Float32
from .DataType import BinarySingle, CharVarLen
from .base import StdfRecordBase, register_record


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

