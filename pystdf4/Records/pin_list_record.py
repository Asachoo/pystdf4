from typing import Optional, Sequence

from pystdf4.Core import U_2, KxC_n, KxU_1, KxU_2

from .base import StdfRecordBase


class PLR(StdfRecordBase):
    """
    Pin Sequence Record (PLR)

    Function: Defines the current display radix and operating mode for a pin or pin group. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 63

    GRP_CNT: U_2
    """
    Count (k) of pins or pin groups
    """
    GRP_INDX: KxU_2
    """
    Array of pin or pin group indexes
    """
    GRP_MODE: KxU_2
    """
    Operating mode of pin group
    """
    GRP_RADX: KxU_1
    """
    Display radix of pin group
    """
    PGM_CHAR: KxC_n
    """
    Program state encoding characters
    """
    RTN_CHAR: KxC_n
    """
    Return state encoding characters
    """
    PGM_CHAL: KxC_n
    """
    Program state encoding characters
    """
    RTN_CHAL: KxC_n
    """
    Return state encoding characters
    """

    def __init__(
        self,
        GRP_CNT: int,
        GRP_INDX: Optional[Sequence[int]] = None,
        GRP_MODE: Optional[Sequence[int]] = None,
        GRP_RADX: Optional[Sequence[int]] = None,
        PGM_CHAR: Optional[Sequence[str]] = None,
        RTN_CHAR: Optional[Sequence[str]] = None,
        PGM_CHAL: Optional[Sequence[str]] = None,
        RTN_CHAL: Optional[Sequence[str]] = None,
    ):
        self.GRP_CNT = U_2(GRP_CNT)
        self.GRP_INDX = KxU_2(GRP_CNT, GRP_INDX)
        self.GRP_MODE = KxU_2(GRP_CNT, GRP_MODE)
        self.GRP_RADX = KxU_1(GRP_CNT, GRP_RADX)
        self.PGM_CHAR = KxC_n(GRP_CNT, PGM_CHAR)
        self.RTN_CHAR = KxC_n(GRP_CNT, RTN_CHAR)
        self.PGM_CHAL = KxC_n(GRP_CNT, PGM_CHAL)
        self.RTN_CHAL = KxC_n(GRP_CNT, RTN_CHAL)
