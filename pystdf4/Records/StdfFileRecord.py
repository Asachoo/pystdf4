from dataclasses import dataclass

from .DataType import U_1, U_4, C_n
from .DataType import UInt8, UInt32, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(0, 10)
class FAR(StdfRecordBase):
    """
    File Attributes Record (FAR)

    Describes global attributes for the STDF file.
    """

    REC_TYP = 0
    REC_SUB = 10

    # CPU type that wrote this file
    CPU_TYPE: UInt8 = U_1()
    # STDF version number
    STDF_VER: UInt8 = U_1()


@dataclass
@register_record(0, 20)
class ATR(StdfRecordBase):
    """
    Audit Trail Record (ATR)

    Records actions or commands that modified the STDF file.
    """

    REC_TYP = 0
    REC_SUB = 20

    # Date and time of STDF file modification
    MOD_TIM: UInt32 = U_4()
    # Command line of program
    CMD_LINE: CharVarLen = C_n()
