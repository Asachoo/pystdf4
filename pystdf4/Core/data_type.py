from abc import ABC, abstractmethod
from struct import Struct
from typing import ClassVar, Generic, Sequence, TypeVar

from pystdf4.Core.dynamic_buffer import DynamicBuffer
from pystdf4.Core.mixins import CacheMixin

pyT = TypeVar("pyT", int, float, str, bytes)


# ============================================================
# Base Field Abstractions
# ============================================================


class FieldBase(ABC, Generic[pyT]):
    """Abstract base class for STDF fields."""

    @classmethod
    @abstractmethod
    def pack_into(cls, buffer: DynamicBuffer, value: pyT):
        raise NotImplementedError()


# ============================================================
# Fixed-Length Fields with CacheMixin
# ============================================================


class FixedLengthField(FieldBase[pyT], CacheMixin):
    """
    Base class for fixed-length fields with deferred buffer writing.
    """

    field_size: ClassVar[int]
    num_elements: ClassVar[int] = 1

    @classmethod
    def pack_into(cls, buffer: DynamicBuffer, value: pyT):
        """Reserve space, cache the value, and advance the buffer offset."""
        buffer._ensure_capacity(cls.field_size)
        cls._enqueue_value(value, buffer.offset, cls.field_size)
        buffer.offset += cls.field_size

    @classmethod
    def flush_cache_to_buffer(cls, buffer: DynamicBuffer):
        """Flush cached values to the buffer."""
        cls.flush_cache(memoryview(cls._serialize_sequence(cls.cached_values)), buffer)

    @classmethod
    @abstractmethod
    def _serialize_sequence(cls, sequence: Sequence[pyT]) -> bytes:
        raise NotImplementedError()


# ============================================================
# Struct-based Fields
# ============================================================


class PackBasedField(FixedLengthField[pyT]):
    """
    Field packed using `struct.Struct`.

    Attributes:
        endian: '<' or '>' for byte order.
        struct_format: struct format code (e.g., 'B', 'H', 'I', 'f', etc.).
    """

    endian: ClassVar[str] = "<"
    struct_format: ClassVar[str]

    def __init_subclass__(cls) -> None:
        """Initialize cache and compute element size."""
        super().__init_subclass__()
        cls.field_size = Struct(f"{cls.endian}{cls.num_elements}{cls.struct_format}").size

    @classmethod
    def _serialize_sequence(cls, sequence: Sequence[pyT]) -> bytes:
        """Pack sequence into bytes using struct."""
        count = len(cls.buffer_offsets) * cls.num_elements
        packer = Struct(f"{cls.endian}{count}{cls.struct_format}")
        return packer.pack(*sequence)


# ============================================================
# Byte-based Fields
# ============================================================


class ByteBasedField(FixedLengthField):
    """Field where values are raw bytes concatenated."""

    @classmethod
    def _serialize_sequence(cls, sequence: Sequence[bytes]) -> bytes:
        return b"".join(sequence)

    @classmethod
    def flush_cache_to_buffer(cls, buffer: DynamicBuffer):
        """Flush cached values to the buffer."""
        cls.flush_cache(memoryview(cls._serialize_sequence(cls.cached_values)), buffer)


# ============================================================
# Variable/Computed Length Fields
# ============================================================


class ComputedLengthField(ByteBasedField):
    length_format: ClassVar[str]
    length_packer: ClassVar[Struct]

    def __init_subclass__(cls) -> None:
        """Initialize cache and compute element size."""
        super().__init_subclass__()
        cls.length_packer = Struct(f"<{cls.length_format}")

    @classmethod
    def pack_into(cls, buffer: DynamicBuffer, value: str | bytes):
        data = value.encode("ascii") if isinstance(value, str) else value
        data = cls.length_packer.pack(len(data)) + data
        total_size = len(data)
        buffer._ensure_capacity(total_size)
        cls._enqueue_value(data, buffer.offset, total_size)
        buffer.offset += total_size

    @classmethod
    def flush_cache_to_buffer(cls, buffer: DynamicBuffer):
        cls.flush_cache_sequence(cls.cached_values, buffer)


class SpecificLengthField(FieldBase):
    """Field with externally determined length."""

    element_size: ClassVar[int]

    def __init__(self, num_elements: int):
        super().__init__()
        self.num_elements = num_elements


# ============================================================
# Numeric Field Implementations
# ============================================================


class U_1(PackBasedField[int]):
    struct_format = "B"


class U_2(PackBasedField[int]):
    struct_format = "H"


class U_4(PackBasedField[int]):
    struct_format = "I"


class I_1(PackBasedField[int]):
    struct_format = "b"


class I_2(PackBasedField[int]):
    struct_format = "h"


class I_4(PackBasedField[int]):
    struct_format = "i"


class R_4(PackBasedField[float]):
    struct_format = "f"


class R_8(PackBasedField[float]):
    struct_format = "d"


# ============================================================
# Character & Byte Fields
# ============================================================


class C_1(ByteBasedField):
    field_size = 1

    @classmethod
    def _enqueue_value(cls, value: str, offset: int, size: int):
        """Encode ASCII character before caching."""
        super()._enqueue_value(value.encode("ascii"), offset, size)


class B_1(ByteBasedField):
    field_size = 1


# ============================================================
# Variable-Length Fields
# ============================================================


class C_n(ComputedLengthField):
    length_format = "B"


class B_n(ComputedLengthField):
    length_format = "B"


class D_n(ComputedLengthField):
    length_format = "H"
