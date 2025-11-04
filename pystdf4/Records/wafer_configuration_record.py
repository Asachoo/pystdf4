from dataclasses import dataclass

from .DataType import U_1, I_2, R_4, C_1
from .DataType import UInt8, Int16, Float32, CharSingle
from .base import StdfRecordBase, register_record


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
