from typing import Optional, Sequence

from pystdf4.Core import U_2, C_n, KxU_2

from .base import StdfRecordBase


class PGR(StdfRecordBase):
    """
    Pin Group Record (PGR)

    Function: Associates a name with a group of pins. See "Using the Pin Mapping Records" on page 77.
    """

    REC_TYP = 1
    REC_SUB = 62

    GRP_INDX: U_2
    """
    Unique index associated with pin group
    """
    GRP_NAM: C_n
    """
    Name of pin group
    """
    INDX_CNT: U_2
    """
    Count (k) of PMR indexes
    """
    PMR_INDX: KxU_2
    """
    Array of indexes for pins in the group
    """

    def __init__(
        self,
        GRP_INDX: int,
        INDX_CNT: int,
        PMR_INDX: Optional[Sequence[int]] = None,
        GRP_NAM: str = "",
    ):
        self.GRP_INDX = U_2(GRP_INDX)
        self.GRP_NAM = C_n(GRP_NAM)
        self.INDX_CNT = U_2(INDX_CNT)
        self.PMR_INDX = KxU_2(INDX_CNT, PMR_INDX)
