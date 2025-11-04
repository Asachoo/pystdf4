from pystdf4.DataType.StdfBinary import B_n, B_1
from pystdf4.DataType.StdfChar import C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_2
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(5, 10)
class PIR(StdfRecord):
    """
    Part Information Record (PIR)

    Marks the beginning of test data for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 10

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()


@register_record(5, 20)
class PRR(StdfRecord):
    """
    Part Results Record (PRR)

    Contains test results for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 20

    # Test head number
    HEAD_NUM: U_1 = U_1()
    # Test site number
    SITE_NUM: U_1 = U_1()
    # Part information flag
    PART_FLG: B_1 = B_1()
    # Number of tests executed
    NUM_TEST: U_2 = U_2()
    # Hardware bin number
    HARD_BIN: U_2 = U_2()
    # Software bin number
    SOFT_BIN: U_2 = U_2()
    # (Wafer) X coordinate
    X_COORD: I_2 = I_2()
    # (Wafer) Y coordinate
    Y_COORD: I_2 = I_2()
    # Elapsed test time in milliseconds
    TEST_T: U_4 = U_4()
    # Part identification
    PART_ID: C_n = C_n()
    # Part description text
    PART_TXT: C_n = C_n()
    # Part repair information
    PART_FIX: B_n = B_n()
