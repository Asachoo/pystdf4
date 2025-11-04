from dataclasses import dataclass

from .DataType import U_1, U_2, C_n
from .DataType import UInt8, UInt16, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 60)
class PMR(StdfRecordBase):
    """
    Pin Map Record (PMR)

    Function: Provides indexing of tester channel names, and maps them to physical and logical pin names. Each PMR defines the information for a single channel/pin combination. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 60

    PMR_INDX: UInt16 = U_2()
    """
    Unique index associated with pin
    """
    CHAN_TYP: UInt16 = U_2()
    """
    Channel type
    """
    CHAN_NAM: CharVarLen = C_n()
    """
    Channel name
    """
    PHY_NAM: CharVarLen = C_n()
    """
    Physical name of pin
    """
    LOG_NAM: CharVarLen = C_n()
    """
    Logical name of pin
    """
    HEAD_NUM: UInt8 = U_1()
    """
    Head number associated with channel
    """
    SITE_NUM: UInt8 = U_1()
    """
    Site number associated with channel
    """
