from pystdf4.Core import U_2

from .base import StdfRecordBase


class GDR(StdfRecordBase):
    """
    Generic Data Record (GDR)

    Function: Contains information that does not conform to any other record type defined by the STDF specification. Such records are
    intended to be written under the control of job plans executing on the tester. This data may be used for any purpose that the user
    desires.
    """

    REC_TYP = 50
    REC_SUB = 10

    # TODO: Implement GEN_DATA

    FLD_CNT: U_2
    """
    Count of data fields in record
    """

    # GEN_DATA: V_n =V_n()
    """
    Data type code and data for one field
    """

    def __init__(self, FLD_CNT: int):
        self.FLD_CNT = U_2(FLD_CNT)
