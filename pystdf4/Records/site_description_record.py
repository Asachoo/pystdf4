from dataclasses import dataclass, field

from .DataType import U_1, C_n
from .DataType import UInt8, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(1, 80)
class SDR(StdfRecordBase):
    """
    Site Description Record (SDR)

    Function: Contains the configuration information for one or more test sites, connected to one test head, that compose a site group.
    """

    REC_TYP = 1
    REC_SUB = 80

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_GRP: UInt8 = U_1()
    """
    Site group number
    """
    SITE_CNT: UInt8 = U_1()
    """
    Number of test sites in site group
    """
    SITE_NUM: list[U_1] = field(default_factory=list)
    """
    Array of test site numbers
    """
    HAND_TYP: CharVarLen = C_n()
    """
    Handler or prober type
    """
    HAND_ID: CharVarLen = C_n()
    """
    Handler or prober ID
    """
    CARD_TYP: CharVarLen = C_n()
    """
    Probe card type
    """
    CARD_ID: CharVarLen = C_n()
    """
    Probe card ID
    """
    LOAD_TYP: CharVarLen = C_n()
    """
    Load board type
    """
    LOAD_ID: CharVarLen = C_n()
    """
    Load board ID
    """
    DIB_TYP: CharVarLen = C_n()
    """
    DIB board type
    """
    DIB_ID: CharVarLen = C_n()
    """
    DIB board ID
    """
    CABL_TYP: CharVarLen = C_n()
    """
    Interface cable type
    """
    CABL_ID: CharVarLen = C_n()
    """
    Interface cable ID
    """
    CONT_TYP: CharVarLen = C_n()
    """
    Handler contactor type
    """
    CONT_ID: CharVarLen = C_n()
    """
    Handler contactor ID
    """
    LASR_TYP: CharVarLen = C_n()
    """
    Laser type
    """
    LASR_ID: CharVarLen = C_n()
    """
    Laser ID
    """
    EXTR_TYP: CharVarLen = C_n()
    """
    Extra equipment type field
    """
    EXTR_ID: CharVarLen = C_n()
    """
    Extra equipment ID
    """
