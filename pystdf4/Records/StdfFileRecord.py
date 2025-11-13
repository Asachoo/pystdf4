from dataclasses import dataclass

from .DataType import U_1, U_4, C_n
from .DataType import UInt8, UInt32, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(0, 10)
class FAR(StdfRecordBase):
    """
    File Attributes Record (FAR)

    Function: Contains the information necessary to determine how to decode the STDF data contained in the file.
    """

    REC_TYP = 0
    REC_SUB = 10

    CPU_TYPE: UInt8 = U_1()
    """
    CPU type that wrote this file
    """
    STDF_VER: UInt8 = U_1()
    """
    STDF version number
    """


@dataclass
@register_record(0, 20)
class ATR(StdfRecordBase):
    """
    Audit Trail Record (ATR)

    Function: Used to record any operation that alters the contents of the STDF file. The name of the program and all its parameters should be recorded in the ASCII field provided in this record. Typically, this record will be used to track filter programs that have been applied to the data.
    """

    REC_TYP = 0
    REC_SUB = 20

    MOD_TIM: UInt32 = U_4()
    """
    Date and time of STDF file modification
    """
    CMD_LINE: CharVarLen = C_n()
    """
    Command line of program
    """
