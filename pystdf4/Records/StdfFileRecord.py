from pystdf4.DataType.StdfChar import C_n
from pystdf4.DataType.StdfInteger import U_1, U_4
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(0, 10)
class FAR(StdfRecord):
    """
    File Attributes Record (FAR)

    Describes global attributes for the STDF file.
    """

    REC_TYP = 0
    REC_SUB = 10

    # CPU type that wrote this file
    CPU_TYPE: U_1 = U_1()
    # STDF version number
    STDF_VER: U_1 = U_1()


@register_record(0, 20)
class ATR(StdfRecord):
    """
    Audit Trail Record (ATR)

    Records actions or commands that modified the STDF file.
    """

    REC_TYP = 0
    REC_SUB = 20

    # Date and time of STDF file modification
    MOD_TIM: U_4 = U_4()
    # Command line of program
    CMD_LINE: C_n = C_n()
