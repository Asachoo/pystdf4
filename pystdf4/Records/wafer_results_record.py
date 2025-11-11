from pystdf4.Core import U_1, U_4, C_n

from .base import StdfRecordBase


class WRR(StdfRecordBase):
    """
    Wafer Results Record (WRR)

    Function: Contains the result information relating to each wafer tested by the job plan. The WRR and the Wafer Information Record (WIR)
    bracket all the stored information pertaining to one tested wafer. This record is used only when testing at wafer probe time. A WIR/WRR
    pair will have the same HEAD_NUM and SITE_GRP values.
    """

    REC_TYP = 2
    REC_SUB = 20

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_GRP: U_1
    """
    Site group number
    """
    FINISH_T: U_4
    """
    Date and time last part tested
    """
    PART_CNT: U_4
    """
    Number of parts tested
    """
    RTST_CNT: U_4
    """
    Number of parts retested
    """
    ABRT_CNT: U_4
    """
    Number of aborts during testing
    """
    GOOD_CNT: U_4
    """
    Number of good (passed) parts tested
    """
    FUNC_CNT: U_4
    """
    Number of functional parts tested
    """
    WAFER_ID: C_n
    """
    Wafer ID
    """
    FABWF_ID: C_n
    """
    Fab wafer ID
    """
    FRAME_ID: C_n
    """
    Wafer frame ID
    """
    MASK_ID: C_n
    """
    Wafer mask ID
    """
    USR_DESC: C_n
    """
    Wafer description supplied by user
    """
    EXC_DESC: C_n
    """
    Wafer description supplied by exec
    """

    def __init__(
        self,
        HEAD_NUM: int,
        FINISH_T: int,
        PART_CNT: int,
        SITE_GRP: int = 255,
        RTST_CNT: int = 4294967295,
        ABRT_CNT: int = 4294967295,
        GOOD_CNT: int = 4294967295,
        FUNC_CNT: int = 4294967295,
        WAFER_ID: str = "",
        FABWF_ID: str = "",
        FRAME_ID: str = "",
        MASK_ID: str = "",
        USR_DESC: str = "",
        EXC_DESC: str = "",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_GRP = U_1(SITE_GRP)
        self.FINISH_T = U_4(FINISH_T)
        self.PART_CNT = U_4(PART_CNT)
        self.RTST_CNT = U_4(RTST_CNT)
        self.ABRT_CNT = U_4(ABRT_CNT)
        self.GOOD_CNT = U_4(GOOD_CNT)
        self.FUNC_CNT = U_4(FUNC_CNT)
        self.WAFER_ID = C_n(WAFER_ID)
        self.FABWF_ID = C_n(FABWF_ID)
        self.FRAME_ID = C_n(FRAME_ID)
        self.MASK_ID = C_n(MASK_ID)
        self.USR_DESC = C_n(USR_DESC)
        self.EXC_DESC = C_n(EXC_DESC)
