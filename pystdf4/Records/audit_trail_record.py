from pystdf4.Core import U_4, C_n

from .base import StdfRecordBase


class ATR(StdfRecordBase):
    """
    Audit Trail Record (ATR)

    Function: Used to record any operation that alters the contents of the STDF file. The name of the program and all its parameters should
    be recorded in the ASCII field provided in this record. Typically, this record will be used to track filter programs that have been
    applied to the data.
    """

    REC_TYP = 0
    REC_SUB = 20

    MOD_TIM: U_4
    """
    Date and time of STDF file modification
    """
    CMD_LINE: C_n
    """
    Command line of program
    """

    def __init__(self, MOD_TIM: int, CMD_LINE: str):
        self.MOD_TIM = U_4(MOD_TIM)
        self.CMD_LINE = C_n(CMD_LINE)
