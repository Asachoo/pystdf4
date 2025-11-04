from dataclasses import dataclass, field

from .DataType import U_2
from .DataType import UInt16
from .base import StdfRecordBase, register_record



@dataclass
@register_record(1, 70)
class RDR(StdfRecordBase):
    """
    Retest Data Record (RDR)

    Function: Signals that the data in this STDF file is for retested parts. The data in this record, combined with information in the MIR, tells data filtering programs what data to replace when processing retest data.
    """

    REC_TYP = 1
    REC_SUB = 70

    NUM_BINS: UInt16 = U_2()
    """
    Number (k) of bins being retested
    """
    RTST_BIN: list[U_2] = field(default_factory=list)
    """
    Array of retest bin numbers
    """