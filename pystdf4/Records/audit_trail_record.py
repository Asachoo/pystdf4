from dataclasses import dataclass

from .DataType import U_4, C_n
from .DataType import UInt32, CharVarLen
from .base import StdfRecordBase, register_record


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
