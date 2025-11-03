import struct
from .StdfBase import StdfDataBase

class R_4(StdfDataBase[float]):
    def __init__(self):
        super().__init__(code="R*4", description="Four byte floating point number (IEEE 754)", bytes_len=4)

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

class R_8(StdfDataBase[float]):
    def __init__(self):
        super().__init__(code="R*8", description="Eight byte floating point number (IEEE 754)", bytes_len=8)

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