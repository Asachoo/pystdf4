from dataclasses import dataclass, field

from .DataType import U_1, U_2, C_n
from .DataType import UInt16
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 63)
class PLR(StdfRecordBase):
    """
    Pin List Record (PLR)

    Function: Defines the current display radix and operating mode for a pin or pin group. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 63

    GRP_CNT: UInt16 = U_2()
    """
    Count (k) of pins or pin groups
    """
    GRP_INDX: list[U_2] = field(default_factory=list)
    """
    Array of pin or pin group indexes
    """
    GRP_MODE: list[U_2] = field(default_factory=list)
    """
    Operating mode of pin group
    """
    GRP_RADX: list[U_1] = field(default_factory=list)
    """
    Display radix of pin group
    """
    PGM_CHAR: list[C_n] = field(default_factory=list)
    """
    Program state encoding characters
    """
    RTN_CHAR: list[C_n] = field(default_factory=list)
    """
    Return state encoding characters
    """
    PGM_CHAL: list[C_n] = field(default_factory=list)
    """
    Program state encoding characters
    """
    RTN_CHAL: list[C_n] = field(default_factory=list)
    """
    Return state encoding characters
    """
