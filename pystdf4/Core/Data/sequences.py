from typing import Sequence

from .base import KxLenField, VarLenField
from .scalars import R_4, U_1, U_2

# region Actual implementation


class C_n(VarLenField[str, bytes]):
    _fmt = "c"

    @classmethod
    def _normalize(cls, value: Sequence[str]) -> bytes:
        return "".join(value).encode("ascii")


class B_n(VarLenField[bytes, bytes]):
    @classmethod
    def _normalize(cls, value: Sequence[bytes]) -> bytes:
        return b"".join(value)


# endregion


class KxU_1(KxLenField[int, U_1]):
    element_type = U_1


class KxU_2(KxLenField[int, U_2]):
    element_type = U_2


class KxC_n(KxLenField[int, C_n]):
    element_type = C_n


class KxR_4(KxLenField[float, R_4]):
    element_type = R_4
