from typing import TypeVar
from .StdfBase import StdfDataBase

T = TypeVar("T", bound=bytes)


class StdfBinaryBase(StdfDataBase[bytes]):
    """STDF Binary Data Type Base Class"""

    def _validate_py_value(self, py_value: bytes) -> None:
        # Validate py_value type
        if not isinstance(py_value, bytes):
            raise TypeError("Python value must be bytes")

        encoded_len = len(py_value)
        if self._max_len != -1 and encoded_len > self._max_len:
            raise ValueError(
                f"Binary data too long ({encoded_len} > {self._max_len} bytes)"
            )

        if self._bytes_len != -1 and encoded_len > self._bytes_len:
            raise ValueError(
                f"Binary data too long ({encoded_len} > {self._bytes_len} bytes)"
            )

    def _build_py(self, py_value: bytes) -> bytes:
        self._validate_py_value(py_value)
        return py_value

    def _parse_py(self) -> bytes:
        return self.internal_bytes

    def _build_stdf(self, stdf_bytes: bytes) -> bytes:
        if self._code == "B*n":
            # Extract data from length-prefixed format
            length_byte = stdf_bytes[0]
            data_bytes = stdf_bytes[1 : 1 + length_byte]
            if len(stdf_bytes) == 0:
                raise ValueError("Empty B*n data")
            if len(data_bytes) != length_byte:
                raise ValueError("Invalid length prefix in B*n data")
            return data_bytes
        elif self._code.startswith("B*") and "*" in self._code[1:]:
            # Fixed-length binary data like B*1
            expected_length = int(self._code.split("*")[1])
            if len(stdf_bytes) != expected_length:
                raise ValueError(f"Expected {expected_length} bytes for {self._code}")
            return stdf_bytes
        else:
            raise NotImplementedError(f"Unsupported binary type: {self._code}")

    def _parse_stdf(self) -> bytes:
        if self._code == "B*n":
            # Add length prefix for variable-length binary data
            length = len(self.internal_bytes)
            if length > 255:
                raise ValueError("B*n data too long (> 255 bytes)")
            return bytes([length]) + self.internal_bytes
        elif self._code.startswith("B*") and "*" in self._code[1:]:
            # Fixed-length binary data like B*1
            return self.internal_bytes
        else:
            raise NotImplementedError(f"Unsupported binary type: {self._code}")


class B_1(StdfBinaryBase):
    """
    Fixed length bit-encoded field (B*1).
    Data is a single bit (0 or 1).
    """

    def __init__(self):
        super().__init__(
            code="B*1",
            description="Fixed length bit-encoded field (1 byte)",
            bytes_len=1,
        )


class B_n(StdfBinaryBase):
    """
    Variable length bit-encoded field (B*n).
    First byte = unsigned count of bytes to follow (max 255).
    Data starts in least significant bit of the second byte.
    """

    def __init__(self):
        super().__init__(
            code="B*n",
            description="Variable length bit-encoded field (byte prefixed)",
            max_len=255,
        )
