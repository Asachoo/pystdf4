from dataclasses import dataclass

from .DataType import U_1, U_4, C_n
from .DataType import UInt8, UInt32, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(2, 10)
class WIR(StdfRecordBase):
    """
    Wafer Information Record (WIR)

    Function: Acts mainly as a marker to indicate where testing of a particular wafer begins for each wafer tested by the job plan. The WIR and the Wafer Results Record (WRR) bracket all the stored information pertaining to one tested wafer. This record is used only when testing at wafer probe. A WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values.
    """

    REC_TYP = 2
    REC_SUB = 10

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_GRP: UInt8 = U_1()
    """
    Site group number
    """
    START_T: UInt32 = U_4()
    """
    Date and time first part tested
    """
    WAFER_ID: CharVarLen = C_n()
    """
    Wafer ID
    """
