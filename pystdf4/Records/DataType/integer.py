import struct
from typing import TypeVar
from .base import StdfDataBase
from functools import cached_property

T = TypeVar("T", bound=int)


class StdfIntBase(StdfDataBase[int]):
    """STDF Integer Data Type Base Class"""

    # STDF code to struct format mapping
    _CODE_TO_FMT: dict[str, str] = {
        "U*1": "B",  # unsigned char
        "U*2": "H",  # unsigned short
        "U*4": "I",  # unsigned int
        "I*1": "b",  # signed char
        "I*2": "h",  # short
        "I*4": "i",  # int
    }

    @cached_property
    def fmt(self) -> str:
        fmt_code = self._CODE_TO_FMT.get(self._code, None)
        if fmt_code is None:
            raise ValueError(
                f"Unsupported integer type code: {self._code}. Supported codes: {list(self._CODE_TO_FMT.keys())}"
            )
        return self._ENDIAN + fmt_code

    def _build_py(self, py_value: int) -> bytes:
        # Validate py_value type
        if not isinstance(py_value, int):
            raise TypeError(f"Expected int, got {type(py_value)}")

        # Validate value range
        if self._code.startswith("U"):
            if py_value < 0:
                raise ValueError(f"Unsigned integer cannot be negative: {py_value}")
            max_val = (1 << (8 * self._bytes_len)) - 1
            if py_value > max_val:
                raise ValueError(
                    f"Value {py_value} exceeds maximum {max_val} for {self._code}"
                )
        else:  # Signed integers
            min_val = -(1 << (8 * self._bytes_len - 1))
            max_val = (1 << (8 * self._bytes_len - 1)) - 1
            if not (min_val <= py_value <= max_val):
                raise ValueError(
                    f"Value {py_value} out of range [{min_val}, {max_val}] for {self._code}"
                )

        try:
            return struct.pack(self.fmt, py_value)
        except struct.error as e:
            raise ValueError(f"Failed to pack {py_value} as {self._code}: {e}")

    def _parse_py(self) -> int:
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


# Unsigned integers
class U_1(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="U*1",
            description="One byte unsigned integer",
            missing_default=0,
        )


class U_2(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="U*2",
            description="Two byte unsigned integer",
            missing_default=0,
        )


class U_4(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="U*4",
            description="Four byte unsigned integer",
            missing_default=0,
        )


# Signed integers
class I_1(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="I*1",
            description="One byte signed integer",
            missing_default=0,
        )


class I_2(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="I*2",
            description="Two byte signed integer",
            missing_default=0,
        )


class I_4(StdfIntBase):
    def __init__(self):
        super().__init__(
            code="I*4",
            description="Four byte signed integer",
            missing_default=0,
        )
