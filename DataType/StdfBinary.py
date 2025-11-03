# DataType/StdfBinary.py
from typing import Optional, List, Union
from .StdfBase import StdfDataBase

class B_n(StdfDataBase[bytes]):
    """
    Variable length bit-encoded field (B*n).
    First byte = unsigned count of bytes to follow (max 255).
    Data starts in least significant bit of the second byte.
    """
    def __init__(self):
        super().__init__(code="B*n", description="Variable length bit-encoded field (byte prefixed)")

    def _validate_py_value(self, py_value: str) -> bool:
        return super()._validate_py_value(py_value)
    
    def _build_c_from_py(self, py_value: str) -> bytes:
        return super()._build_c_from_py(py_value)
    
    def _parse_c_to_py(self) -> str:
        return super()._parse_c_to_py()
    
    def _validate_stdf_value(self, stdf_value: bytes) -> bool:
        return super()._validate_stdf_value(stdf_value)
    
    def _build_c_from_stdf(self, stdf_value: bytes) -> bytes:
        return super()._build_c_from_stdf(stdf_value)
    
    def _parse_c_to_stdf(self) -> bytes:
        return super()._parse_c_to_stdf()