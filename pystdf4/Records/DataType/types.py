from __future__ import annotations
from typing import TypeAlias, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .binary import B_1, B_n
    from .character import C_1, C_n
    from .integer import U_1, U_2, U_4, I_1, I_2, I_4
    from .double import R_4, R_8

UInt8: TypeAlias = Union[int, "U_1"]
UInt16: TypeAlias = Union[int, "U_2"]
UInt32: TypeAlias = Union[int, "U_4"]
Int8: TypeAlias = Union[int, "I_1"]
Int16: TypeAlias = Union[int, "I_2"]
Int32: TypeAlias = Union[int, "I_4"]

Float32: TypeAlias = Union[float, "R_4"]
Float64: TypeAlias = Union[float, "R_8"]

CharSingle: TypeAlias = Union[str, "C_1"]
CharVarLen: TypeAlias = Union[str, "C_n"]

BinarySingle: TypeAlias = Union[bytes, "B_1"]
BinaryVarLen: TypeAlias = Union[bytes, "B_n"]
