from dataclasses import dataclass

from .DataType import U_1
from .DataType import UInt8
from .base import StdfRecordBase, register_record


@dataclass
@register_record(5, 10)
class PIR(StdfRecordBase):
    """
    Part Information Record (PIR)

    Function: Acts as a marker to indicate where testing of a particular part begins for each part tested by the test program. The PIR and the Part Results Record (PRR) bracket all the stored information pertaining to one tested part.
    """

    REC_TYP = 5
    REC_SUB = 10

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
