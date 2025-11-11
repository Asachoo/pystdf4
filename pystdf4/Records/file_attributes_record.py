from pystdf4.Core import U_1

from .base import StdfRecordBase


class FAR(StdfRecordBase):
    """
    File Attributes Record (FAR)

    Function: Contains the information necessary to determine how to decode the STDF data contained in the file.
    """

    REC_TYP = 0
    REC_SUB = 10

    CPU_TYPE: U_1
    """
    CPU type that wrote this file
    """
    STDF_VER: U_1
    """
    STDF version number
    """

    def __init__(self, CPU_TYPE: int, STDF_VER: int):
        self.CPU_TYPE = U_1(CPU_TYPE)
        self.STDF_VER = U_1(STDF_VER)
