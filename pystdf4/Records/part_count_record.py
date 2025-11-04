from dataclasses import dataclass

from .DataType import U_1, U_4
from .DataType import UInt8, UInt32
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 30)
class PCR(StdfRecordBase):
    """
    Part Count Record (PCR)

    Function: Contains the part count totals for one or all test sites. Each data stream must have at least one PCR to show the part count.
    """

    REC_TYP = 1
    REC_SUB = 30

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    PART_CNT: UInt32 = U_4()
    """
    Number of parts tested
    """
    RTST_CNT: UInt32 = U_4()
    """
    Number of parts retested
    """
    ABRT_CNT: UInt32 = U_4()
    """
    Number of aborts during testing
    """
    GOOD_CNT: UInt32 = U_4()
    """
    Number of good (passed) parts tested
    """
    FUNC_CNT: UInt32 = U_4()
    """
    Number of functional parts tested
    """
