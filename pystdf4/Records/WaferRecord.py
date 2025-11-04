from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(2, 10)
class WaferInformationRecord(StdfRecord):
    """
    Wafer Information Record (WIR)

    Marks the beginning of test data for a wafer.
    """

    REC_TYP = 2
    REC_SUB = 10


@register_record(2, 20)
class WaferResultsRecord(StdfRecord):
    """
    Wafer Results Record (WRR)

    Contains summarized test results for a wafer.
    """

    REC_TYP = 2
    REC_SUB = 20


@register_record(2, 30)
class WaferConfigurationRecord(StdfRecord):
    """
    Wafer Configuration Record (WCR)

    Describes configuration information for wafer-level testing.
    """

    REC_TYP = 2
    REC_SUB = 30
