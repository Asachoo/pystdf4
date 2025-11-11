from .base import StdfRecordBase


class EPS(StdfRecordBase):
    """
    End Program Section Record (EPS)

    Function: Marks the end of the current program section (or sequencer) in the job plan.
    """

    REC_TYP = 20
    REC_SUB = 20
