from pystdf4.Core import C_n

from .base import StdfRecordBase


class BPS(StdfRecordBase):
    """
    Begin Program Section Record (BPS)

    Function: Marks the beginning of a new program section (or sequencer) in the job plan.
    """

    REC_TYP = 20
    REC_SUB = 10

    SEQ_NAME: C_n
    """
    Program section (or sequencer) name
    """

    def __init__(self, SEQ_NAME: str = ""):
        self.SEQ_NAME = C_n(SEQ_NAME)
