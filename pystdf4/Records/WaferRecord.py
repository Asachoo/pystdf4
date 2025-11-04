from dataclasses import dataclass

from pystdf4.DataType.StdfChar import C_1, C_n
from pystdf4.DataType.StdfInteger import U_1, U_4, I_2
from pystdf4.DataType.StdfFloat import R_4
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(2, 10)
class WIR(StdfRecordBase):
    """
    Wafer Information Record (WIR)

    Marks the beginning of test data for a wafer.
    """

    REC_TYP = 2
    REC_SUB = 10

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Site group number
    SITE_GRP: U_1 = U_1()
    # Date and time first part tested
    START_T: U_4 = U_4()
    # Wafer ID
    WAFER_ID: C_n = C_n()


@dataclass
@register_record(2, 20)
class WRR(StdfRecordBase):
    """
    Wafer Results Record (WRR)

    Contains summarized test results for a wafer.
    """

    REC_TYP = 2
    REC_SUB = 20

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Site group number
    SITE_GRP: U_1 = U_1()
    # Date and time last part tested
    FINISH_T: U_4 = U_4()
    # Number of parts tested
    PART_CNT: U_4 = U_4()
    # Number of parts retested
    RTST_CNT: U_4 = U_4()
    # Number of aborts during testing
    ABRT_CNT: U_4 = U_4()
    # Number of good (passed) parts tested
    GOOD_CNT: U_4 = U_4()
    # Number of functional parts tested
    FUNC_CNT: U_4 = U_4()
    # Wafer ID
    WAFER_ID: C_n = C_n()
    # Fab wafer ID
    FABWF_ID: C_n = C_n()
    # Wafer frame ID
    FRAME_ID: C_n = C_n()
    # Wafer mask ID
    MASK_ID: C_n = C_n()
    # Wafer description supplied by user
    USR_DESC: C_n = C_n()
    # Wafer description supplied by exec
    EXC_DESC: C_n = C_n()


@dataclass
@register_record(2, 30)
class WCR(StdfRecordBase):
    """
    Wafer Configuration Record (WCR)

    Describes configuration information for wafer-level testing.
    """

    REC_TYP = 2
    REC_SUB = 30

    # Diameter of wafer in WF_UNITS
    WAFR_SIZ: R_4 = R_4()
    # Height of die in WF_UNITS
    DIE_HT: R_4 = R_4()
    # Width of die in WF_UNITS
    DIE_WID: R_4 = R_4()
    # Units for wafer and die dimensions
    WF_UNITS: U_1 = U_1()
    # Orientation of wafer flat
    WF_FLAT: C_1 = C_1()
    # X coordinate of center die on wafer
    CENTER_X: I_2 = I_2()
    # Y coordinate of center die on wafer
    CENTER_Y: I_2 = I_2()
    # Positive X direction of wafer
    POS_X: C_1 = C_1()
    # Positive Y direction of wafer
    POS_Y: C_1 = C_1()
