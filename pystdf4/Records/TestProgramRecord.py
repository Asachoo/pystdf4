from pystdf4.DataType.StdfBinary import B_1
from pystdf4.DataType.StdfChar import C_1, C_n
from pystdf4.DataType.StdfInteger import U_1, U_4
from pystdf4.DataType.StdfFloat import R_4
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@register_record(10, 30)
class TSR(StdfRecordBase):
    """
    Test Synopsis Record (TSR)

    Contains execution and failure counts for a test in the test program.
    """

    REC_TYP = 10
    REC_SUB = 30

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Test type
    TEST_TYP: C_1 = C_1()
    # Test number
    TEST_NUM: U_4 = U_4()
    # Number of test executions
    EXEC_CNT: U_4 = U_4()
    # Number of test failures
    FAIL_CNT: U_4 = U_4()
    # Number of alarmed tests
    ALRM_CNT: U_4 = U_4()
    # Test name
    TEST_NAM: C_n = C_n()
    # Sequencer (program segment/flow) name
    SEQ_NAME: C_n = C_n()
    # Test label or text
    TEST_LBL: C_n = C_n()
    # Optional data flag
    OPT_FLAG: B_1 = B_1()
    # Average test execution time in seconds
    TEST_TIM: R_4 = R_4()
    # Lowest test result value
    TEST_MIN: R_4 = R_4()
    # Highest test result value
    TEST_MAX: R_4 = R_4()
    # Sum of test result values
    TST_SUMS: R_4 = R_4()
    # Sum of squares of test result values
    TST_SQRS: R_4 = R_4()
