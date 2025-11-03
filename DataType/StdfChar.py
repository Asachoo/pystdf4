from .StdfBase import StdfDataBase


class C_n(StdfDataBase[str]):
    """
    Variable-length character string (C*n).
    """

    def __init__(self):
        super().__init__(code="C*n", description="Variable-length character string", max_len=255)

    def _build_py(self, py_value: str) -> bytes:
        if not isinstance(py_value, str):
            raise TypeError("Python value must be a string")
        if len(py_value.encode("ASCII")) > 255:
            raise ValueError("Python value must be less than or equal to 255 bytes")
        return py_value.encode("ASCII")

    def _parse_py(self) -> str:
        return self.c_value.decode("ASCII")

    def _build_stdf(self, stdf_value: bytes) -> bytes:
        bytes_length = stdf_value[0]
        return stdf_value[1 : 1 + bytes_length]

    def _parsestdf(self) -> bytes:
        bytes_length = len(self.c_value)
        return bytes([bytes_length]) + self.c_value


class C_12(StdfDataBase[str]):
    """
    Fixed-length character string (C*12). Left-justified, padded with spaces.
    """

    def __init__(self):
        super().__init__(
            code="C*12", description="Fixed-length character string", bytes_len=12
        )

    def _validate_py_value(self, py_value: str) -> bool:
        if not isinstance(py_value, str):
            raise TypeError("Python value must be a string")
        if len(py_value.encode("utf-8")) > 12:
            raise ValueError("Python value must be less than or equal to 12 bytes")
        return True

    def _build_c_from_py(self, py_value: str) -> bytes:
        return py_value.ljust(self._bytes_len).encode("utf-8")

    def _parse_c_to_py(self) -> str:
        return self.c_value.decode("utf-8").strip()

    def _validate_stdf_value(self, stdf_value: bytes) -> bool:
        if len(stdf_value) != 12:
            raise ValueError("STDF value must be 12 bytes long")
        return True

    def _build_c_from_stdf(self, stdf_value: bytes) -> bytes:
        return stdf_value

    def _parse_c_to_stdf(self) -> bytes:
        return self.c_value
