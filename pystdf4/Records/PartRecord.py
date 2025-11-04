from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(5, 10)
class PartInformationRecord(StdfRecord):
    """
    Part Information Record (PIR)

    Marks the beginning of test data for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 10


@register_record(5, 20)
class PartResultsRecord(StdfRecord):
    """
    Part Results Record (PRR)

    Contains test results for an individual part.
    """

    REC_TYP = 5
    REC_SUB = 20
