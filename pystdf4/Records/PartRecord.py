from dataclasses import dataclass

from .DataType import U_1, U_2, U_4, I_2, B_n, B_1, C_n
from .DataType import UInt8, UInt16, UInt32, Int16
from .DataType import BinarySingle, BinaryVarLen, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(5, 10)
class PIR(StdfRecordBase):
    """
    Part Information Record (PIR)

    Marks the beginning of test data for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 10

    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()


@dataclass
@register_record(5, 20)
class PRR(StdfRecordBase):
    """
    Part Results Record (PRR)

    Contains test results for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 20

    # Test head number
    HEAD_NUM: UInt8 = U_1()
    # Test site number
    SITE_NUM: UInt8 = U_1()
    # Part information flag
    PART_FLG: BinarySingle = B_1()
    # Number of tests executed
    NUM_TEST: UInt16 = U_2()
    # Hardware bin number
    HARD_BIN: UInt16 = U_2()
    # Software bin number
    SOFT_BIN: UInt16 = U_2()
    # (Wafer) X coordinate
    X_COORD: Int16 = I_2()
    # (Wafer) Y coordinate
    Y_COORD: Int16 = I_2()
    # Elapsed test time in milliseconds
    TEST_T: UInt32 = U_4()
    # Part identification
    PART_ID: CharVarLen = C_n()
    # Part description text
    PART_TXT: CharVarLen = C_n()
    # Part repair information
    PART_FIX: BinaryVarLen = B_n()
