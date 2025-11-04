import struct
from typing import TypeVar
from .StdfDataBase import StdfDataBase
from functools import cached_property

T = TypeVar("T", bound=float)


class StdfFloatBase(StdfDataBase[float]):
    """STDF Float Data Type Base Class"""

    # STDF code to struct format mapping
    _CODE_TO_FMT: dict[str, str] = {
        "R*4": "f",  # float
        "R*8": "d",  # double
    }

    @cached_property
    def fmt(self) -> str:
        fmt_code = self._CODE_TO_FMT.get(self._code, None)
        if fmt_code is None:
            raise ValueError(
                f"Unsupported float type code: {self._code}. Supported codes: {list(self._CODE_TO_FMT.keys())}"
            )
        return self._ENDIAN + fmt_code

    def _build_py(self, py_value: float) -> bytes:
        # Validate py_value type
        if not isinstance(py_value, (float, int)):
            raise TypeError(f"Expected float or int, got {type(py_value)}")

        try:
            return struct.pack(self.fmt, float(py_value))
        except struct.error as e:
            raise ValueError(f"Failed to pack {py_value} as {self._code}: {e}")

    def _parse_py(self) -> float:
        try:
            return struct.unpack(self.fmt, self.internal_bytes)[0]
        except struct.error as e:
            raise ValueError(
                f"Failed to unpack {self.internal_bytes.hex()} as {self._code}: {e}"
            )

    def _build_stdf(self, stdf_bytes: bytes) -> bytes:
        return stdf_bytes

    def _parse_stdf(self) -> bytes:
        return self.internal_bytes


class R_4(StdfFloatBase):
    def __init__(self):
        super().__init__(
            code="R*4",
            description="Four byte floating point number (IEEE 754)",
        )


class R_8(StdfFloatBase):
    def __init__(self):
        super().__init__(
            code="R*8",
            description="Eight byte floating point number (IEEE 754)",
        )
