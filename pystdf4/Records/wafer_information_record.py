from pystdf4.Core import U_1, U_4, C_n

from .base import StdfRecordBase


class WIR(StdfRecordBase):
    """
    Wafer Information Record (WIR)

    Function: Acts mainly as a marker to indicate where testing of a particular wafer begins for each wafer tested by the job plan. The WIR
    and the Wafer Results Record (WRR) bracket all the stored information pertaining to one tested wafer. This record is used only when
    testing at wafer probe. A WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values.
    """

    REC_TYP = 2
    REC_SUB = 10

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_GRP: U_1
    """
    Site group number
    """
    START_T: U_4
    """
    Date and time first part tested
    """
    WAFER_ID: C_n
    """
    Wafer ID
    """

    def __init__(
        self,
        HEAD_NUM: int,
        START_T: int,
        SITE_GRP: int = 255,
        WAFER_ID: str = "",
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_GRP = U_1(SITE_GRP)
        self.START_T = U_4(START_T)
        self.WAFER_ID = C_n(WAFER_ID)
