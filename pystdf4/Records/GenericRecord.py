from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(50, 10)
class GenericDataRecord(StdfRecord):
    """
    Generic Data Record (GDR)

    Holds user-defined data that do not conform to any standard STDF record.
    """

    REC_TYP = 50
    REC_SUB = 10


@register_record(50, 30)
class DatalogTextRecord(StdfRecord):
    """
    Datalog Text Record (DTR)

    Contains text strings for inclusion in datalog output.
    """

    REC_TYP = 50
    REC_SUB = 30
