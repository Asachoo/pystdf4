from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(10, 30)
class TestSynopsisRecord(StdfRecord):
    """
    Test Synopsis Record (TSR)

    Contains execution and failure counts for a test in the test program.
    """

    REC_TYP = 10
    REC_SUB = 30
