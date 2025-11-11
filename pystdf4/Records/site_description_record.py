from typing import Optional, Sequence

from pystdf4.Core import U_1, C_n, KxU_1

from .base import StdfRecordBase


class SDR(StdfRecordBase):
    """
    Site Description Record (SDR)

    Function: Contains the configuration information for one or more test sites, connected to one test head, that compose a site group.
    """

    REC_TYP = 1
    REC_SUB = 80

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_GRP: U_1
    """
    Site group number
    """
    SITE_CNT: U_1
    """
    Number of test sites in site group
    """
    SITE_NUM: KxU_1
    """
    Array of test site numbers
    """
    HAND_TYP: C_n
    """
    Handler or prober type
    """
    HAND_ID: C_n
    """
    Handler or prober ID
    """
    CARD_TYP: C_n
    """
    Probe card type
    """
    CARD_ID: C_n
    """
    Probe card ID
    """
    LOAD_TYP: C_n
    """
    Load board type
    """
    LOAD_ID: C_n
    """
    Load board ID
    """
    DIB_TYP: C_n
    """
    DIB board type
    """
    DIB_ID: C_n
    """
    DIB board ID
    """
    CABL_TYP: C_n
    """
    Interface cable type
    """
    CABL_ID: C_n
    """
    Interface cable ID
    """
    CONT_TYP: C_n
    """
    Handler contactor type
    """
    CONT_ID: C_n
    """
    Handler contactor ID
    """
    LASR_TYP: C_n
    """
    Laser type
    """
    LASR_ID: C_n
    """
    Laser ID
    """
    EXTR_TYP: C_n
    """
    Extra equipment type field
    """
    EXTR_ID: C_n
    """
    Extra equipment ID
    """

    def __init__(
        self,
        HEAD_NUM: int,
        SITE_GRP: int,
        SITE_CNT: int,
        SITE_NUM: Optional[Sequence[int]] = None,
        HAND_TYP: str = "",
        HAND_ID: str = "",
        CARD_TYP: str = "",
        CARD_ID: str = "",
        LOAD_TYP: str = "",
        LOAD_ID: str = "",
        DIB_TYP: str = "",
        DIB_ID: str = "",
        CABL_TYP: str = "",
        CABL_ID: str = "",
        CONT_TYP: str = "",
        CONT_ID: str = "",
        LASR_TYP: str = "",
        LASR_ID: str = "",
        EXTR_TYP: str = "",
        EXTR_ID: str = "",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_GRP = U_1(SITE_GRP)
        self.SITE_CNT = U_1(SITE_CNT)
        self.SITE_NUM = KxU_1(SITE_CNT, SITE_NUM)
        self.HAND_TYP = C_n(HAND_TYP)
        self.HAND_ID = C_n(HAND_ID)
        self.CARD_TYP = C_n(CARD_TYP)
        self.CARD_ID = C_n(CARD_ID)
        self.LOAD_TYP = C_n(LOAD_TYP)
        self.LOAD_ID = C_n(LOAD_ID)
        self.DIB_TYP = C_n(DIB_TYP)
        self.DIB_ID = C_n(DIB_ID)
        self.CABL_TYP = C_n(CABL_TYP)
        self.CABL_ID = C_n(CABL_ID)
        self.CONT_TYP = C_n(CONT_TYP)
        self.CONT_ID = C_n(CONT_ID)
        self.LASR_TYP = C_n(LASR_TYP)
        self.LASR_ID = C_n(LASR_ID)
        self.EXTR_TYP = C_n(EXTR_TYP)
        self.EXTR_ID = C_n(EXTR_ID)
