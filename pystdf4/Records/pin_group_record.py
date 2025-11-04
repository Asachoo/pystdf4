from dataclasses import dataclass, field

from .DataType import U_2, C_n
from .DataType import UInt16, CharVarLen
from .base import StdfRecordBase, register_record



@dataclass
@register_record(1, 62)
class PGR(StdfRecordBase):
    """
    Pin Group Record (PGR)

    Function: Associates a name with a group of pins. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 62

    GRP_INDX: UInt16 = U_2()
    """
    Unique index associated with pin group
    """
    GRP_NAM: CharVarLen = C_n()
    """
    Name of pin group
    """
    INDX_CNT: UInt16 = U_2()
    """
    Count (k) of PMR indexes
    """
    PMR_INDX: list[U_2] = field(default_factory=list)
    """
    Array of indexes for pins in the group
    """
