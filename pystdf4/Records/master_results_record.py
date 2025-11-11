from pystdf4.Core import C_1, U_4, C_n

from .base import StdfRecordBase


class MRR(StdfRecordBase):
    """
    Master Results Record (MRR)

    Function: The Master Results Record (MRR) is a logical extension of the Master Information Record (MIR). The data can be thought of as
    belonging with the MIR, but it is not available when the tester writes the MIR information. Each data stream must have exactly one MRR
    as the last record in the data stream.
    """

    REC_TYP = 1
    REC_SUB = 20

    FINISH_T: U_4
    """
    Date and time last part tested
    """
    DISP_COD: C_1
    """
    Lot disposition code
    """
    USR_DESC: C_n
    """
    Lot description supplied by user
    """
    EXC_DESC: C_n
    """
    Lot description supplied by exec
    """

    def __init__(
        self,
        FINISH_T: int,
        DISP_COD: str = " ",
        USR_DESC: str = "",
        EXC_DESC: str = "",
    ):
        self.FINISH_T = U_4(FINISH_T)
        self.DISP_COD = C_1(DISP_COD)
        self.USR_DESC = C_n(USR_DESC)
        self.EXC_DESC = C_n(EXC_DESC)
