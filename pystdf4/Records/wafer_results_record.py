from dataclasses import dataclass

from .DataType import U_1, U_4, C_n
from .DataType import UInt8, UInt32, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(2, 20)
class WRR(StdfRecordBase):
    """
    Wafer Results Record (WRR)

    Function: Contains the result information relating to each wafer tested by the job plan. The WRR and the Wafer Information Record (WIR) bracket all the stored information pertaining to one tested wafer. This record is used only when testing at wafer probe time. A WIR/WRR pair will have the same HEAD_NUM and SITE_GRP values.
    """

    REC_TYP = 2
    REC_SUB = 20

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_GRP: UInt8 = U_1()
    """
    Site group number
    """
    FINISH_T: UInt32 = U_4()
    """
    Date and time last part tested
    """
    PART_CNT: UInt32 = U_4()
    """
    Number of parts tested
    """
    RTST_CNT: UInt32 = U_4()
    """
    Number of parts retested
    """
    ABRT_CNT: UInt32 = U_4()
    """
    Number of aborts during testing
    """
    GOOD_CNT: UInt32 = U_4()
    """
    Number of good (passed) parts tested
    """
    FUNC_CNT: UInt32 = U_4()
    """
    Number of functional parts tested
    """
    WAFER_ID: CharVarLen = C_n()
    """
    Wafer ID
    """
    FABWF_ID: CharVarLen = C_n()
    """
    Fab wafer ID
    """
    FRAME_ID: CharVarLen = C_n()
    """
    Wafer frame ID
    """
    MASK_ID: CharVarLen = C_n()
    """
    Wafer mask ID
    """
    USR_DESC: CharVarLen = C_n()
    """
    Wafer description supplied by user
    """
    EXC_DESC: CharVarLen = C_n()
    """
    Wafer description supplied by exec
    """
