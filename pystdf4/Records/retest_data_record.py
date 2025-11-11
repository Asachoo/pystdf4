from typing import Optional, Sequence

from pystdf4.Core import U_2, KxU_2

from .base import StdfRecordBase


class RDR(StdfRecordBase):
    """
    Retest Data Record (RDR)

    Function: Signals that the data in this STDF file is for retested parts. The data in this record, combined with information in the MIR,
    tells data filtering programs what data to replace when processing retest data.
    """

    REC_TYP = 1
    REC_SUB = 70

    NUM_BINS: U_2
    """
    Number (k) of bins being retested
    """
    RTST_BIN: KxU_2
    """
    Array of retest bin numbers
    """

    def __init__(self, NUM_BINS: int, RTST_BIN: Optional[Sequence[int]] = None):
        self.NUM_BINS = U_2(NUM_BINS)
        self.RTST_BIN = KxU_2(NUM_BINS, RTST_BIN)
