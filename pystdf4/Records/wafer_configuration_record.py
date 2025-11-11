from typing import Literal

from pystdf4.Core import C_1, I_2, R_4, U_1

from .base import StdfRecordBase


class WCR(StdfRecordBase):
    """
    Wafer Configuration Record (WCR)

    Function: Contains the configuration information for the wafers tested by the job plan. The WCR provides the dimensions and orientation
    information for all wafers and dice in the lot. This record is used only when testing at wafer probe time.
    """

    REC_TYP = 2
    REC_SUB = 30

    WAFR_SIZ: R_4
    """
    Diameter of wafer in WF_UNITS
    """
    DIE_HT: R_4
    """
    Height of die in WF_UNITS
    """
    DIE_WID: R_4
    """
    Width of die in WF_UNITS
    """
    WF_UNITS: U_1
    """
    Units for wafer and die dimensions
    """
    WF_FLAT: C_1
    """
    Orientation of wafer flat
    """
    CENTER_X: I_2
    """
    X coordinate of center die on wafer
    """
    CENTER_Y: I_2
    """
    Y coordinate of center die on wafer
    """
    POS_X: C_1
    """
    Positive X direction of wafer
    """
    POS_Y: C_1
    """
    Positive Y direction of wafer
    """

    def __init__(
        self,
        WAFR_SIZ: float = 0.0,
        DIE_HT: float = 0.0,
        DIE_WID: float = 0.0,
        WF_UNITS: int = 0,
        WF_FLAT: Literal["U", "D", "L", "R", " "] = " ",
        CENTER_X: int = -32768,
        CENTER_Y: int = -32768,
        POS_X: Literal["L", "R", " "] = " ",
        POS_Y: Literal["U", "D", " "] = " ",
    ):
        self.WAFR_SIZ = R_4(WAFR_SIZ)
        self.DIE_HT = R_4(DIE_HT)
        self.DIE_WID = R_4(DIE_WID)
        self.WF_UNITS = U_1(WF_UNITS)
        self.WF_FLAT = C_1(WF_FLAT)
        self.CENTER_X = I_2(CENTER_X)
        self.CENTER_Y = I_2(CENTER_Y)
        self.POS_X = C_1(POS_X)
        self.POS_Y = C_1(POS_Y)
