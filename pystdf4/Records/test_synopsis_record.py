from dataclasses import dataclass

from .DataType import U_1, U_4, R_4, B_1, C_1, C_n
from .DataType import UInt8, UInt32, Float32
from .DataType import BinarySingle, CharSingle, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(10, 30)
class TSR(StdfRecordBase):
    """
    Test Synopsis Record (TSR)

    Function: Contains the test execution and failure counts for one parametric or functional test in the test program. Also contains static information, such as test name. The TSR is related to the Functional Test Record (FTR), the Parametric Test Record (PTR), and the Multiple Parametric Test Record (MPR) by test number, head number, and site number.
    """

    REC_TYP = 10
    REC_SUB = 30

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    TEST_TYP: CharSingle = C_1()
    """
    Test type
    """
    TEST_NUM: UInt32 = U_4()
    """
    Test number
    """
    EXEC_CNT: UInt32 = U_4()
    """
    Number of test executions
    """
    FAIL_CNT: UInt32 = U_4()
    """
    Number of test failures
    """
    ALRM_CNT: UInt32 = U_4()
    """
    Number of alarmed tests
    """
    TEST_NAM: CharVarLen = C_n()
    """
    Test name
    """
    SEQ_NAME: CharVarLen = C_n()
    """
    Sequencer (program segment/flow) name
    """
    TEST_LBL: CharVarLen = C_n()
    """
    Test label or text
    """
    OPT_FLAG: BinarySingle = B_1()
    """
    Optional data flag
    """
    TEST_TIM: Float32 = R_4()
    """
    Average test execution time in seconds
    """
    TEST_MIN: Float32 = R_4()
    """
    Lowest test result value
    """
    TEST_MAX: Float32 = R_4()
    """
    Highest test result value
    """
    TST_SUMS: Float32 = R_4()
    """
    Sum of test result values
    """
    TST_SQRS: Float32 = R_4()
    """
    Sum of squares of test result values
    """
