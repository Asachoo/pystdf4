from dataclasses import dataclass

from .DataType import C_n
from .DataType import CharVarLen
from .base import StdfRecordBase, register_record


@dataclass
@register_record(20, 10)
class BPS(StdfRecordBase):
    """
    Begin Program Section Record (BPS)

    Function: Marks the beginning of a new program section (or sequencer) in the job plan.
    """

    REC_TYP = 20
    REC_SUB = 10

    SEQ_NAME: CharVarLen = C_n()
    """
    Program section (or sequencer) name
    """
