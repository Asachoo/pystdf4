from pystdf4.Core import U_1, U_2, C_n

from .base import StdfRecordBase


class PMR(StdfRecordBase):
    """
    Pin Map Record (PMR)

    Function: Provides indexing of tester channel names, and maps them to physical and logical pin names. Each PMR defines the information
    for a single channel/pin combination.
    """

    REC_TYP = 1
    REC_SUB = 60

    PMR_INDX: U_2
    """
    Unique index associated with pin
    """
    CHAN_TYP: U_2
    """
    Channel type
    """
    CHAN_NAM: C_n
    """
    Channel name
    """
    PHY_NAM: C_n
    """
    Physical name of pin
    """
    LOG_NAM: C_n
    """
    Logical name of pin
    """
    HEAD_NUM: U_1
    """
    Head number associated with channel
    """
    SITE_NUM: U_1
    """
    Site number associated with channel
    """

    def __init__(
        self,
        PMR_INDX: int,
        CHAN_TYP: int = 0,
        CHAN_NAM: str = "",
        PHY_NAM: str = "",
        LOG_NAM: str = "",
        HEAD_NUM: int = 1,
        SITE_NUM: int = 1,
    ):
        self.PMR_INDX = U_2(PMR_INDX)
        self.CHAN_TYP = U_2(CHAN_TYP)
        self.CHAN_NAM = C_n(CHAN_NAM)
        self.PHY_NAM = C_n(PHY_NAM)
        self.LOG_NAM = C_n(LOG_NAM)
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
