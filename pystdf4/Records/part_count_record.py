from pystdf4.Core import U_1, U_4

from .base import StdfRecordBase


class PCR(StdfRecordBase):
    """
    Part Count Record (PCR)

    Function: Contains the part count totals for one or all test sites. Each data stream must have at least one PCR to show the part count.
    """

    REC_TYP = 1
    REC_SUB = 30

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    PART_CNT: U_4
    """
    Number of parts tested
    """
    RTST_CNT: U_4
    """
    Number of parts retested
    """
    ABRT_CNT: U_4
    """
    Number of aborts during testing
    """
    GOOD_CNT: U_4
    """
    Number of good (passed) parts tested
    """
    FUNC_CNT: U_4
    """
    Number of functional parts tested
    """

    def __init__(
        self,
        SITE_NUM: int,
        PART_CNT: int,
        HEAD_NUM: int = 255,
        RTST_CNT: int = 4294967295,
        ABRT_CNT: int = 4294967295,
        GOOD_CNT: int = 4294967295,
        FUNC_CNT: int = 4294967295,
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.PART_CNT = U_4(PART_CNT)
        self.RTST_CNT = U_4(RTST_CNT)
        self.ABRT_CNT = U_4(ABRT_CNT)
        self.GOOD_CNT = U_4(GOOD_CNT)
        self.FUNC_CNT = U_4(FUNC_CNT)
