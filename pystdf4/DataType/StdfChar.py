from typing import TypeVar
from .StdfDataBase import StdfDataBase

T = TypeVar("T", bound=str)


class StdfStringBase(StdfDataBase[str]):
    """STDF Character Data Type Base Class"""

    def _validate_py_value(self, py_value: str) -> None:
        # Validate py_value type
        if not isinstance(py_value, str):
            raise TypeError("Python value must be a string")

        encoded_length = len(py_value.encode("ascii"))
        if self._max_len != -1 and encoded_length > self._max_len:
            raise ValueError(
                f"String too long ({encoded_length} > {self._max_len} bytes)"
            )
        if self._bytes_len != -1 and encoded_length > self._bytes_len:
            raise ValueError(
                f"String too long ({encoded_length} > {self._bytes_len} bytes)"
            )

    def _build_py(self, py_value: str) -> bytes:
        self._validate_py_value(py_value)
        return py_value.encode("ASCII")

    def _parse_py(self) -> str:
        return self.internal_bytes.decode("ASCII")

    def _build_stdf(self, stdf_bytes: bytes) -> bytes:
        if self.is_variable_length:
            # Variable-length strings are stored length-prefixed
            length_byte = stdf_bytes[0]
            data_bytes = stdf_bytes[1 : 1 + length_byte]
            if len(data_bytes) != length_byte:
                raise ValueError("Invalid length prefix in C*n data")
            return data_bytes
        else:
            # Fixed-length strings are confirmed by length
            expected_length = int(self._code.split("*")[1])
            if len(stdf_bytes) != expected_length:
                raise ValueError(f"Expected {expected_length} bytes for {self._code}")
            return stdf_bytes

    def _parse_stdf(self) -> bytes:
        if self.is_variable_length:
            # Add length prefix for variable-length strings
            length = len(self.internal_bytes)
            if length > 255:
                raise ValueError("C*n string too long (> 255 bytes)")
            return bytes([length]) + self.internal_bytes
        else:
            # Fixed-length strings are already properly formatted
            return self.internal_bytes


class C_1(StdfStringBase):
    """
    Fixed-length character string (C*1).
    """

    def __init__(self):
        super().__init__(
            code="C*1",
            description="Fixed-length character string",
        )


class C_n(StdfStringBase):
    """
    Variable-length character string (C*n).
    First byte = unsigned count of bytes to follow (max 255).
    """

    def __init__(self):
        super().__init__(
            code="C*n",
            description="Variable-length character string",
            max_len=255,
        )
