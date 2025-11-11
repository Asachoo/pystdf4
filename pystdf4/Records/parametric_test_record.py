from pystdf4.Core import B_1, I_1, R_4, U_1, U_4, C_n

from .base import StdfRecordBase


class PTR(StdfRecordBase):
    """
    Parametric Test Record (PTR)

    Function: Contains the results of a single execution of a parametric test in the test program. The first occurrence of this record also
    establishes the default values for all semi-static information about the test, such as limits, units, and scaling. The PTR is related to
    the Test Synopsis Record (TSR) by test number, head number, and site number.
    """

    REC_TYP = 15
    REC_SUB = 10
    OPT_FLAG_CONFIG = {
        "RES_SCAL": 0,
        "LLM_SCAL": 4,
        "HLM_SCAL": 5,
        "LO_LIMIT": 4,
        "HI_LIMIT": 5,
        "LO_SPEC": 2,
        "HI_SPEC": 3,
    }

    TEST_NUM: U_4
    """
    Test number
    """
    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    TEST_FLG: B_1
    """
    Test flags (fail, alarm, etc.)
    """
    PARM_FLG: B_1
    """
    Parametric test flags (drift, etc.)
    """
    RESULT: R_4
    """
    Test result
    """
    TEST_TXT: C_n
    """
    Test description text or label
    """
    ALARM_ID: C_n
    """
    Name of alarm
    """
    OPT_FLAG: B_1
    """
    Optional data flag
    """
    RES_SCAL: I_1
    """
    Test results scaling exponent
    """
    LLM_SCAL: I_1
    """
    Low limit scaling exponent
    """
    HLM_SCAL: I_1
    """
    High limit scaling exponent
    """
    LO_LIMIT: R_4
    """
    Low test limit value
    """
    HI_LIMIT: R_4
    """
    High test limit value
    """
    UNITS: C_n
    """
    Test units
    """
    C_RESFMT: C_n
    """
    ANSI C result format string
    """
    C_LLMFMT: C_n
    """
    ANSI C low limit format string
    """
    C_HLMFMT: C_n
    """
    ANSI C high limit format string
    """
    LO_SPEC: R_4
    """
    Low specification limit value
    """
    HI_SPEC: R_4
    """
    High specification limit value
    """

    def __init__(
        self,
        TEST_NUM: int,
        HEAD_NUM: int,
        SITE_NUM: int,
        TEST_FLG: bytes,
        PARM_FLG: bytes,
        OPT_FLAG: bytes,
        RESULT: float = 0.0,
        TEST_TXT: str = "",
        ALARM_ID: str = "",
        RES_SCAL: int = 0,
        LLM_SCAL: int = 0,
        HLM_SCAL: int = 0,
        LO_LIMIT: float = 0.0,
        HI_LIMIT: float = 0.0,
        UNITS: str = "",
        C_RESFMT: str = "",
        C_LLMFMT: str = "",
        C_HLMFMT: str = "",
        LO_SPEC: float = 0.0,
        HI_SPEC: float = 0.0,
    ):
        self.TEST_NUM = U_4(TEST_NUM)
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.TEST_FLG = B_1(TEST_FLG)
        self.PARM_FLG = B_1(PARM_FLG)
        self.RESULT = R_4(RESULT)
        self.TEST_TXT = C_n(TEST_TXT)
        self.ALARM_ID = C_n(ALARM_ID)
        self.OPT_FLAG = B_1(OPT_FLAG)
        self.RES_SCAL = I_1(RES_SCAL)
        self.LLM_SCAL = I_1(LLM_SCAL)
        self.HLM_SCAL = I_1(HLM_SCAL)
        self.LO_LIMIT = R_4(LO_LIMIT)
        self.HI_LIMIT = R_4(HI_LIMIT)
        self.UNITS = C_n(UNITS)
        self.C_RESFMT = C_n(C_RESFMT)
        self.C_LLMFMT = C_n(C_LLMFMT)
        self.C_HLMFMT = C_n(C_HLMFMT)
        self.LO_SPEC = R_4(LO_SPEC)
        self.HI_SPEC = R_4(HI_SPEC)
