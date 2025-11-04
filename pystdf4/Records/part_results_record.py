from dataclasses import dataclass

from .DataType import U_1, U_2, U_4, I_2, B_n, B_1, C_n
from .DataType import UInt8, UInt16, UInt32, Int16
from .DataType import BinarySingle, BinaryVarLen, CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(5, 20)
class PRR(StdfRecordBase):
    """
    Part Results Record (PRR)

    Function: Contains the result information relating to each part tested by the test program. The PRR and the Part Information Record (PIR) bracket all the stored information pertaining to one tested part.
    """

    REC_TYP = 5
    REC_SUB = 20

    HEAD_NUM: UInt8 = U_1()
    """
    Test head number
    """
    SITE_NUM: UInt8 = U_1()
    """
    Test site number
    """
    PART_FLG: BinarySingle = B_1()
    """
    Part information flag
    """
    NUM_TEST: UInt16 = U_2()
    """
    Number of tests executed
    """
    HARD_BIN: UInt16 = U_2()
    """
    Hardware bin number
    """
    SOFT_BIN: UInt16 = U_2()
    """
    Software bin number
    """
    X_COORD: Int16 = I_2()
    """
    (Wafer) X coordinate
    """
    Y_COORD: Int16 = I_2()
    """
    (Wafer) Y coordinate
    """
    TEST_T: UInt32 = U_4()
    """
    Elapsed test time in milliseconds
    """
    PART_ID: CharVarLen = C_n()
    """
    Part identification
    """
    PART_TXT: CharVarLen = C_n()
    """
    Part description text
    """
    PART_FIX: BinaryVarLen = B_n()
    """
    Part repair information
    """
