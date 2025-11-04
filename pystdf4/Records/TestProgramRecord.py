from dataclasses import dataclass

from .DataType import U_1, U_4, R_4, B_1, C_1, C_n
from .DataType import UInt8, UInt32, Float32
from .DataType import BinarySingle, CharSingle, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(10, 30)
class TSR(StdfRecordBase):
    """
    Test Synopsis Record (TSR)

    Contains execution and failure counts for a test in the test program.
    """

    REC_TYP = 10
    REC_SUB = 30

    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()
    # Test type
    TEST_TYP: CharSingle = C_1()
    # Test number
    TEST_NUM: UInt32 = U_4()
    # Number of test executions
    EXEC_CNT: UInt32 = U_4()
    # Number of test failures
    FAIL_CNT: UInt32 = U_4()
    # Number of alarmed tests
    ALRM_CNT: UInt32 = U_4()
    # Test name
    TEST_NAM: CharVarLen = C_n()
    # Sequencer (program segment/flow) name
    SEQ_NAME: CharVarLen = C_n()
    # Test label or text
    TEST_LBL: CharVarLen = C_n()
    # Optional data flag
    OPT_FLAG: BinarySingle = B_1()
    # Average test execution time in seconds
    TEST_TIM: Float32 = R_4()
    # Lowest test result value
    TEST_MIN: Float32 = R_4()
    # Highest test result value
    TEST_MAX: Float32 = R_4()
    # Sum of test result values
    TST_SUMS: Float32 = R_4()
    # Sum of squares of test result values
    TST_SQRS: Float32 = R_4()
