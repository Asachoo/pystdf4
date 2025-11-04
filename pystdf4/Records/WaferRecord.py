from dataclasses import dataclass

from .DataType import U_1, U_4, I_2, R_4, C_1, C_n
from .DataType import UInt8, UInt32, Int16, Float32, CharSingle, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


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


@dataclass
@register_record(2, 30)
class WCR(StdfRecordBase):
    """
    Wafer Configuration Record (WCR)

    Function: Contains the configuration information for the wafers tested by the job plan. The WCR provides the dimensions and orientation information for all wafers and dice in the lot. This record is used only when testing at wafer probe time.
    """

    REC_TYP = 2
    REC_SUB = 30

    WAFR_SIZ: Float32 = R_4()
    """
    Diameter of wafer in WF_UNITS
    """
    DIE_HT: Float32 = R_4()
    """
    Height of die in WF_UNITS
    """
    DIE_WID: Float32 = R_4()
    """
    Width of die in WF_UNITS
    """
    WF_UNITS: UInt8 = U_1()
    """
    Units for wafer and die dimensions
    """
    WF_FLAT: CharSingle = C_1()
    """
    Orientation of wafer flat
    """
    CENTER_X: Int16 = I_2()
    """
    X coordinate of center die on wafer
    """
    CENTER_Y: Int16 = I_2()
    """
    Y coordinate of center die on wafer
    """
    POS_X: CharSingle = C_1()
    """
    Positive X direction of wafer
    """
    POS_Y: CharSingle = C_1()
    """
    Positive Y direction of wafer
    """
