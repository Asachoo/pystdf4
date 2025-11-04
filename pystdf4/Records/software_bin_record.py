from dataclasses import dataclass

from .DataType import U_1, U_2, U_4, C_1, C_n
from .DataType import UInt8, UInt16, UInt32, CharSingle, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 50)
class SBR(StdfRecordBase):
    """
    Software Bin Record (SBR)

    Function: Stores a count of the parts associated with a particular logical bin after testing. This bin count can be for a single test site (when parallel testing) or a total for all test sites. The STDF specification also supports a Hardware Bin Record (HBR) for actual physical binning. A part is “physically” placed in a hardware bin after testing. A part can be “logically” associated with a software bin during or after testing.
    """

    REC_TYP = 1
    REC_SUB = 50

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    SBIN_NUM: UInt16 = U_2()
    """
    Software bin number
    """
    SBIN_CNT: UInt32 = U_4()
    """
    Number of parts in bin
    """
    SBIN_PF: CharSingle = C_1()
    """
    Pass/fail indication
    """
    SBIN_NAM: CharVarLen = C_n()
    """
    Software bin name
    """
