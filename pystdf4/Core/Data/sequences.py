from typing import Any, Sequence

from pystdf4.Core.dynamic_buffer import DynamicBuffer

from .base import KxLenField, VarLenField
from .scalars import R_4, U_1, U_2

# region Actual implementation


class C_n(VarLenField[str, bytes]):
    _fmt = "c"

    @classmethod
    def _normalize(cls, value: Sequence[str]) -> Sequence[Any]:
        return [s.encode("ascii") for s in value]


class B_n(VarLenField[bytes, bytes]):
    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Sequence[bytes]) -> None:
        v = len(value).to_bytes(4, "little") + b"".join(value)
        buffer.write_bytes(v)


# endregion


class KxU_1(KxLenField[int, U_1]):
    element_type = U_1


class KxU_2(KxLenField[int, U_2]):
    element_type = U_2


class KxC_n(KxLenField[int, C_n]):
    element_type = C_n


class KxR_4(KxLenField[float, R_4]):
    element_type = R_4
