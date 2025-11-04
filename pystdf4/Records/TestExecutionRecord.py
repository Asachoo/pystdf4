from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(15, 10)
class ParametricTestRecord(StdfRecord):
    """
    Parametric Test Record (PTR)

    Contains results for a single execution of a parametric test.
    """

    REC_TYP = 15
    REC_SUB = 10


@register_record(15, 15)
class MultipleResultParametricRecord(StdfRecord):
    """
    Multiple-Result Parametric Record (MPR)

    Contains results for a parametric test that returns multiple values.
    """

    REC_TYP = 15
    REC_SUB = 15


@register_record(15, 20)
class FunctionalTestRecord(StdfRecord):
    """
    Functional Test Record (FTR)

    Contains results for a single execution of a functional test.
    """

    REC_TYP = 15
    REC_SUB = 20
