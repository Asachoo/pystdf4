from pystdf4.DataType.StdfChar import C_n
from pystdf4.DataType.StdfInteger import U_2
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(50, 10)
class GDR(StdfRecord):
    """
    Generic Data Record (GDR)

    Holds user-defined data that do not conform to any standard STDF record.
    """

    REC_TYP = 50
    REC_SUB = 10

    # TODO: Implement GEN_DATA

    # Count of data fields in record
    FLD_CNT: U_2 = U_2()
    # Data type code and data for one field
    # GEN_DATA: V_n =V_n()


@register_record(50, 30)
class DTR(StdfRecord):
    """
    Datalog Text Record (DTR)

    Contains text strings for inclusion in datalog output.
    """

    REC_TYP = 50
    REC_SUB = 30

    # ASCII text string
    TEXT_DAT: C_n = C_n()
