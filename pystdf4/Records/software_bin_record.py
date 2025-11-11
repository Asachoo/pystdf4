from typing import Literal

from pystdf4.Core import C_1, U_1, U_2, U_4, C_n

from .base import StdfRecordBase


class SBR(StdfRecordBase):
    """
    Software Bin Record (SBR)

    Function: Stores a count of the parts associated with a particular logical bin after testing. This bin count can be for a single test
    site (when parallel testing) or a total for all test sites. The STDF specification also supports a Hardware Bin Record (HBR) for actual
    physical binning. A part is “physically” placed in a hardware bin after testing. A part can be “logically” associated with a software
    bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 50

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    SBIN_NUM: U_2
    """
    Software bin number
    """
    SBIN_CNT: U_4
    """
    Number of parts in bin
    """
    SBIN_PF: C_1
    """
    Pass/fail indication
    """
    SBIN_NAM: C_n
    """
    Software bin name
    """

    def __init__(
        self,
        SITE_NUM: int,
        SBIN_NUM: int,
        SBIN_CNT: int,
        HEAD_NUM: int = 255,
        SBIN_PF: Literal["P", "F", " "] = " ",
        SBIN_NAM: str = "",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.SBIN_NUM = U_2(SBIN_NUM)
        self.SBIN_CNT = U_4(SBIN_CNT)
        self.SBIN_PF = C_1(SBIN_PF)
        self.SBIN_NAM = C_n(SBIN_NAM)
