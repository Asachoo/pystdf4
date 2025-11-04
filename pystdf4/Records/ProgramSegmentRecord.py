from pystdf4.DataType.StdfChar import C_n
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@register_record(20, 10)
class BPS(StdfRecordBase):
    """
    Begin Program Section Record (BPS)

    Marks the beginning of a program section or sequencer segment.
    """

    REC_TYP = 20
    REC_SUB = 10

    # Program section (or sequencer) name
    SEQ_NAME: C_n = C_n()


@register_record(20, 20)
class EPS(StdfRecordBase):
    """
    End Program Section Record (EPS)

    Marks the end of a program section or sequencer segment.
    """

    REC_TYP = 20
    REC_SUB = 20
