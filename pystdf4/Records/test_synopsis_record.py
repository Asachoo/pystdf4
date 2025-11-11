from typing import Literal

from pystdf4.Core import B_1, C_1, R_4, U_1, U_4, C_n

from .base import StdfRecordBase


class TSR(StdfRecordBase):
    """
    Test Synopsis Record (TSR)

    Function: Contains the test execution and failure counts for one parametric or functional test in the test program. Also contains static
    information, such as test name. The TSR is related to the Functional Test Record (FTR), the Parametric Test Record (PTR), and the
    Multiple Parametric Test Record (MPR) by test number, head number, and site number.
    """

    REC_TYP = 10
    REC_SUB = 30
    OPT_FLAG_CONFIG = {
        "TEST_TIM": 2,
        "TEST_MIN": 0,
        "TEST_MAX": 1,
        "TST_SUMS": 4,
        "TST_SQRS": 5,
    }

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    TEST_TYP: C_1
    """
    Test type
    """
    TEST_NUM: U_4
    """
    Test number
    """
    EXEC_CNT: U_4
    """
    Number of test executions
    """
    FAIL_CNT: U_4
    """
    Number of test failures
    """
    ALRM_CNT: U_4
    """
    Number of alarmed tests
    """
    TEST_NAM: C_n
    """
    Test name
    """
    SEQ_NAME: C_n
    """
    Sequencer (program segment/flow) name
    """
    TEST_LBL: C_n
    """
    Test label or text
    """
    OPT_FLAG: B_1
    """
    Optional data flag
    """
    TEST_TIM: R_4
    """
    Average test execution time in seconds
    """
    TEST_MIN: R_4
    """
    Lowest test result value
    """
    TEST_MAX: R_4
    """
    Highest test result value
    """
    TST_SUMS: R_4
    """
    Sum of test result values
    """
    TST_SQRS: R_4
    """
    Sum of squares of test result values
    """

    def __init__(
        self,
        HEAD_NUM: int,
        SITE_NUM: int,
        TEST_NUM: int,
        OPT_FLAG: bytes,
        TEST_TYP: Literal["P", "F", "M", " "] = " ",
        EXEC_CNT: int = 4294967295,
        FAIL_CNT: int = 4294967295,
        ALRM_CNT: int = 4294967295,
        TEST_NAM: str = "",
        SEQ_NAME: str = "",
        TEST_LBL: str = "",
        TEST_TIM: float = 0.0,
        TEST_MIN: float = 0.0,
        TEST_MAX: float = 0.0,
        TST_SUMS: float = 0.0,
        TST_SQRS: float = 0.0,
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.TEST_TYP = C_1(TEST_TYP)
        self.TEST_NUM = U_4(TEST_NUM)
        self.EXEC_CNT = U_4(EXEC_CNT)
        self.FAIL_CNT = U_4(FAIL_CNT)
        self.ALRM_CNT = U_4(ALRM_CNT)
        self.TEST_NAM = C_n(TEST_NAM)
        self.SEQ_NAME = C_n(SEQ_NAME)
        self.TEST_LBL = C_n(TEST_LBL)
        self.OPT_FLAG = B_1(OPT_FLAG)
        self.TEST_TIM = R_4(TEST_TIM)
        self.TEST_MIN = R_4(TEST_MIN)
        self.TEST_MAX = R_4(TEST_MAX)
        self.TST_SUMS = R_4(TST_SUMS)
        self.TST_SQRS = R_4(TST_SQRS)
