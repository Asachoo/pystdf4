from pystdf4.DataType.StdfBinary import B_n
from pystdf4.DataType.StdfChar import C_1, C_12, C_n
from pystdf4.DataType.StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from pystdf4.DataType.StdfFloat import R_4, R_8
from pystdf4.Records.StdfRecordBase import StdfRecord, register_record


@register_record(20, 10)
class BeginProgramSectionRecord(StdfRecord):
    """
    Begin Program Section Record (BPS)

    Marks the beginning of a program section or sequencer segment.
    """

    REC_TYP = 20
    REC_SUB = 10


@register_record(20, 20)
class EndProgramSectionRecord(StdfRecord):
    """
    End Program Section Record (EPS)

    标记作业计划中当前程序段（或序列器）的结束。

    Attributes:
        REC_TYP: 记录类型，固定为20。
        REC_SUB: 记录子类型，固定为20。
    """

    REC_TYP = 20
    REC_SUB = 20
