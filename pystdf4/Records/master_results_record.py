from dataclasses import dataclass

from .DataType import U_4, C_1, C_n
from .DataType import UInt32, CharSingle, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 20)
class MRR(StdfRecordBase):
    """
    Master Results Record (MRR)

    Function: The Master Results Record (MRR) is a logical extension of the Master Information Record (MIR). The data can be thought of as belonging with the MIR, but it is not available when the tester writes the MIR information. Each data stream must have exactly one MRR as the last record in the data stream.
    """

    REC_TYP = 1
    REC_SUB = 20

    FINISH_T: UInt32 = U_4()
    """
    Date and time last part tested
    """
    DISP_COD: CharSingle = C_1()
    """
    Lot disposition code
    """
    USR_DESC: CharVarLen = C_n()
    """
    Lot description supplied by user
    """
    EXC_DESC: CharVarLen = C_n()
    """
    Lot description supplied by exec
    """
