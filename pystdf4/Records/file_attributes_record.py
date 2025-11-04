from dataclasses import dataclass

from .DataType import U_1
from .DataType import UInt8
from .base import StdfRecordBase, register_record


@dataclass
@register_record(0, 10)
class FAR(StdfRecordBase):
    """
    File Attributes Record (FAR)

    Function: Contains the information necessary to determine how to decode the STDF data contained in the file.
    """

    REC_TYP = 0
    REC_SUB = 10

    CPU_TYPE: UInt8 = U_1()
    """
    CPU type that wrote this file
    """
    STDF_VER: UInt8 = U_1()
    """
    STDF version number
    """