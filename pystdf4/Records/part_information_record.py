from pystdf4.Core import U_1

from .base import StdfRecordBase


class PIR(StdfRecordBase):
    """
    Part Information Record (PIR)

    Function: Acts as a marker to indicate where testing of a particular part begins for each part tested by the test program. The PIR and
    the Part Results Record (PRR) bracket all the stored information pertaining to one tested part.
    """

    REC_TYP = 5
    REC_SUB = 10

    HEAD_NUM: U_1
    """
    Test head number
    """
    SITE_NUM: U_1
    """
    Test site number
    """

    def __init__(
        self,
        HEAD_NUM: int,
        SITE_NUM: int,
    ):
        self.HEAD_NUM = U_1(HEAD_NUM)
        self.SITE_NUM = U_1(SITE_NUM)
