from dataclasses import dataclass

from .DataType import U_2, C_n
from .DataType import UInt16, CharVarLen
from pystdf4.Records.StdfRecordBase import StdfRecordBase, register_record


@dataclass
@register_record(50, 10)
class GDR(StdfRecordBase):
    """
    Generic Data Record (GDR)

    Holds user-defined data that do not conform to any standard STDF record.
    """

    REC_TYP = 50
    REC_SUB = 10

    # TODO: Implement GEN_DATA

    # Count of data fields in record
    FLD_CNT: UInt16 = U_2()
    # Data type code and data for one field
    # GEN_DATA: V_n =V_n()


@dataclass
@register_record(50, 30)
class DTR(StdfRecordBase):
    """
    Datalog Text Record (DTR)

    Contains text strings for inclusion in datalog output.
    """

    REC_TYP = 50
    REC_SUB = 30

    # ASCII text string
    TEXT_DAT: CharVarLen = C_n()
