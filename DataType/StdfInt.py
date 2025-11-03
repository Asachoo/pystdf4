import struct
from .StdfBase import StdfDataBase

# Unsigned integers
class U_1(StdfDataBase[int]):
    def __init__(self):
        super().__init__(code="U*1", description="One byte unsigned integer", bytes_len=1)

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

class U_2(StdfDataBase[int]):
    def __init__(self): # Default to something common like Sun
        super().__init__(code="U*2", description="Two byte unsigned integer", bytes_len=2)

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

class U_4(StdfDataBase[int]):
    def __init__(self):
        super().__init__(code="U*4", description="Four byte unsigned integer", bytes_len=4)

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

# Signed integers (similar structure)
class I_1(StdfDataBase[int]):
    def __init__(self):
        super().__init__(code="I*1", description="One byte signed integer", bytes_len=1)

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

class I_2(StdfDataBase[int]):
    def __init__(self):
        super().__init__(code="I*2", description="Two byte signed integer", bytes_len=2)

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

class I_4(StdfDataBase[int]):
    def __init__(self):
        super().__init__(code="I*4", description="Four byte signed integer", bytes_len=4)

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
