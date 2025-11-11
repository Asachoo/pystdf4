from pystdf4.Core import B_1, I_2, U_1, U_2, U_4, B_n, C_n

from .base import StdfRecordBase


class PRR(StdfRecordBase):
    """
    Part Results Record (PRR)

    Function: Contains the result information relating to each part tested by the test program. The PRR and the Part Information Record
    (PIR) bracket all the stored information pertaining to one tested part.
    """

    REC_TYP = 5
    REC_SUB = 20

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    PART_FLG: B_1
    """
    Part information flag
    """
    NUM_TEST: U_2
    """
    Number of tests executed
    """
    HARD_BIN: U_2
    """
    Hardware bin number
    """
    SOFT_BIN: U_2
    """
    Software bin number
    """
    X_COORD: I_2
    """
    (Wafer) X coordinate
    """
    Y_COORD: I_2
    """
    (Wafer) Y coordinate
    """
    TEST_T: U_4
    """
    Elapsed test time in milliseconds
    """
    PART_ID: C_n
    """
    Part identification
    """
    PART_TXT: C_n
    """
    Part description text
    """
    PART_FIX: B_n
    """
    Part repair information
    """

    def __init__(
        self,
        HEAD_NUM: int,
        SITE_NUM: int,
        PART_FLG: bytes,
        NUM_TEST: int,
        HARD_BIN: int,
        SOFT_BIN: int = 65535,
        X_COORD: int = -32768,
        Y_COORD: int = -32768,
        TEST_T: int = 0,
        PART_ID: str = "",
        PART_TXT: str = "",
        PART_FIX: bytes = b"",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.PART_FLG = B_1(PART_FLG)
        self.NUM_TEST = U_2(NUM_TEST)
        self.HARD_BIN = U_2(HARD_BIN)
        self.SOFT_BIN = U_2(SOFT_BIN)
        self.X_COORD = I_2(X_COORD)
        self.Y_COORD = I_2(Y_COORD)
        self.TEST_T = U_4(TEST_T)
        self.PART_ID = C_n(PART_ID)
        self.PART_TXT = C_n(PART_TXT)
        self.PART_FIX = B_n(PART_FIX)
