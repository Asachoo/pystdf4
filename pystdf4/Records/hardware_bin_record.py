from typing import Literal

from pystdf4.Core import C_1, U_1, U_2, U_4, C_n

from .base import StdfRecordBase


class HBR(StdfRecordBase):
    """
    Hardware Bin Record (HBR)

    Function: Stores a count of the parts “physically” placed in a particular bin after testing. (In wafer testing, “physical” binning is
    not an actual transfer of the chip, but rather is represented by a drop of ink or an entry in a wafer map file.) This bin count can be
    for a single test site (when parallel testing) or a total for all test sites. The STDF specification also supports a Software Bin Record
    (SBR) for logical binning categories. A part is “physically” placed in a hardware bin after testing. A part can be “logically”
    associated with a software bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 40

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """
    HBIN_NUM: U_2
    """
    Hardware bin number
    """
    HBIN_CNT: U_4
    """
    Number of parts in bin
    """
    HBIN_PF: C_1
    """
    Pass/fail indication
    """
    HBIN_NAM: C_n
    """
    Hardware bin name
    """

    def __init__(
        self,
        SITE_NUM: int,
        HBIN_NUM: int,
        HBIN_CNT: int,
        HEAD_NUM: int = 255,
        HBIN_PF: Literal["P", "F", " "] = " ",
        HBIN_NAM: str = "",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
        self.HBIN_NUM = U_2(HBIN_NUM)
        self.HBIN_CNT = U_4(HBIN_CNT)
        self.HBIN_PF = C_1(HBIN_PF)
        self.HBIN_NAM = C_n(HBIN_NAM)
