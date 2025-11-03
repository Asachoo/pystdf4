from typing import TypeVar
from .StdfBase import StdfDataBase

T = TypeVar("T", bound=bytes)


class StdfBinaryBase(StdfDataBase[bytes]):
    """STDF Binary Data Type Base Class"""

    def _build_py(self, py_value: bytes) -> bytes:
        if not isinstance(py_value, bytes):
            raise TypeError("Python value must be bytes")

        if self._max_len != -1 and len(py_value) > self._max_len:
            raise ValueError(
                f"Binary data too long ({len(py_value)} > {self._max_len} bytes)"
            )

        return py_value

    def _parse_py(self) -> bytes:
        return self.internal_bytes

    def _build_stdf(self, stdf_bytes: bytes) -> bytes:
        if self._code == "B*n":
            # Extract data from length-prefixed format
            if len(stdf_bytes) == 0:
                raise ValueError("Empty B*n data")
            length_byte = stdf_bytes[0]
            data_bytes = stdf_bytes[1 : 1 + length_byte]
            if len(data_bytes) != length_byte:
                raise ValueError("Invalid length prefix in B*n data")
            return data_bytes
        else:
            raise NotImplementedError(f"Unsupported binary type: {self._code}")

    def _parse_stdf(self) -> bytes:
        if self._code == "B*n":
            # Add length prefix for variable-length binary data
            length = len(self.internal_bytes)
            if length > 255:
                raise ValueError("B*n data too long (> 255 bytes)")
            return bytes([length]) + self.internal_bytes
        else:
            raise NotImplementedError(f"Unsupported binary type: {self._code}")


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
