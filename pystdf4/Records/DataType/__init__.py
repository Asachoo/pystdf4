from typing import TypeAlias

from .StdfBinary import B_1, B_n
from .StdfChar import C_1, C_n
from .StdfInteger import U_1, U_2, U_4, I_1, I_2, I_4
from .StdfFloat import R_4, R_8

UInt8: TypeAlias = int | U_1
UInt16: TypeAlias = int | U_2
UInt32: TypeAlias = int | U_4
Int8: TypeAlias = int | I_1
Int16: TypeAlias = int | I_2
Int32: TypeAlias = int | I_4

Float32: TypeAlias = float | R_4
Float64: TypeAlias = float | R_8

CharSingle: TypeAlias = str | C_1
CharVarLen: TypeAlias = str | C_n

BinarySingle: TypeAlias = bytes | B_1
BinaryVarLen: TypeAlias = bytes | B_n

__all__ = [
    # DataType
    "B_1",
    "B_n",
    "C_1",
    "C_n",
    "U_1",
    "U_2",
    "U_4",
    "I_1",
    "I_2",
    "I_4",
    "R_4",
    "R_8",
    # TypeAlias
    "UInt8",
    "UInt16",
    "UInt32",
    "Int8",
    "Int16",
    "Int32",
    "Float32",
    "Float64",
    "CharSingle",
    "CharVarLen",
    "BinarySingle",
    "BinaryVarLen",
]
