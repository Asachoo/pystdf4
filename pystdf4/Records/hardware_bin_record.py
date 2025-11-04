from dataclasses import dataclass

from .DataType import U_1, U_2, U_4, C_1, C_n
from .DataType import UInt8, UInt16, UInt32, CharSingle, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 40)
class HBR(StdfRecordBase):
    """
    Hardware Bin Record (HBR)

    Function: Stores a count of the parts “physically” placed in a particular bin after testing. (In wafer testing, “physical” binning is not an actual transfer of the chip, but rather is represented by a drop of ink or an entry in a wafer map file.) This bin count can be for a single test site (when parallel testing) or a total for all test sites. The STDF specification also supports a Software Bin Record (SBR) for logical binning categories. A part is “physically” placed in a hardware bin after testing. A part can be “logically” associated with a software bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 40

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    HBIN_NUM: UInt16 = U_2()
    """
    Hardware bin number
    """
    HBIN_CNT: UInt32 = U_4()
    """
    Number of parts in bin
    """
    HBIN_PF: CharSingle = C_1()
    """
    Pass/fail indication
    """
    HBIN_NAM: CharVarLen = C_n()
    """
    Hardware bin name
    """
