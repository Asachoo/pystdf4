import abc
import struct
from typing import Any, ClassVar, Collection, Generic, Optional, TypeVar

from pystdf4.Core.dynamic_buffer import DynamicBuffer

_T = TypeVar("_T", int, float, str, bytes)

# region Base Field


class Field(abc.ABC):
    """
    Abstract base class for STDF (Standard Test Data Format) fields.

    This class defines a unified interface for all STDF field types, including fixed-length, variable-length, and byte-based fields. It
    supports efficient serialization and deserialization through a shared `DynamicBuffer`.

    Subclasses must implement:
        - `_pack_into(buffer, value)`
        - `unpack_from(buf_mv)`

    Attributes:
        ENDIAN (str): Byte order used in packing/unpacking. Defaults to little-endian.
        value (Any): The in-memory representation of the field value.
    """

    ENDIAN: ClassVar[str] = "<"
    __slots__ = ("value",)

    def __init__(self, value: Optional[Any] = None):
        """
        Initialize the field with an optional value.

        Args:
            value: The field's value. Can be any serializable type.
        """
        self.value = self.normalize_value(value)

    @classmethod
    def normalize_value(cls, value: Any) -> Any:
        """
        Hook for subclasses to sanitize or convert input before storing.

        Args:
            value: The input value.

        Returns:
            The sanitized/converted value.
        """
        return value

    def self_pack_into(self, buffer: DynamicBuffer) -> None:
        """
        Serialize (pack) this field into the provided buffer.

        Args:
            buffer: The `DynamicBuffer` instance to write into.

        Raises:
            ValueError: If no value is provided.
        """
        self.pack_into(buffer, self.value)

    @classmethod
    def pack_into(cls, buffer: DynamicBuffer, value: Any) -> None:
        """
        Serialize (pack) this field class into the provided buffer.

        Args:
            buffer: The `DynamicBuffer` instance to write into.
            value: Value to pack.

        Raises:
            ValueError: If no value is provided.
        """
        if value is None:
            raise ValueError("Value must be provided for class method packing")
        cls._pack_into(buffer, value)

    @classmethod
    @abc.abstractmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Any) -> None:
        """
        Subclass must implement packing logic.

        Args:
            buffer: Target buffer.
            value: Value to pack.
        """
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def unpack_from(cls, buf_mv: memoryview) -> Any:
        """
        Subclass must implement unpacking logic.

        Args:
            buf_mv: Memoryview pointing to raw bytes.

        Returns:
            The unpacked Python object.
        """
        raise NotImplementedError()

    def __repr__(self):
        """
        Return a human-readable representation for debugging.
        """
        return f"<{self.__class__.__name__} value={self.value!r}>"


# endregion


# region FixedField
class FixedField(Field, Generic[_T]):
    """
    Represents a fixed-length field with a pre-defined binary format.

    Subclasses define a struct format (e.g., `'B'`, `'H'`, `'I'`, `'f'`) via `_FMT`, which is compiled to a cached `struct.Struct` object at
    subclass creation.

    This design minimizes repeated format parsing overhead.

    Attributes:
        _FMT (str): The struct format string for this field.
        _packer (struct.Struct): Cached struct object for packing/unpacking.
    """

    _FMT: ClassVar[str]
    _packer: ClassVar[struct.Struct]

    def __init_subclass__(cls) -> None:
        """
        Validate and initialize subclass configuration.

        Raises:
            ValueError: If the subclass does not define _FMT.
        """
        super().__init_subclass__()
        if not hasattr(cls, "_FMT") or not cls._FMT:
            raise ValueError(f"{cls.__name__}: Must define class variable _FMT.")
        cls._packer = struct.Struct(cls.ENDIAN + cls._FMT)

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: _T):
        """
        Write the fixed-length value into the buffer.

        Args:
            buffer: Target DynamicBuffer.
            value: Value to serialize.
        """
        buffer.write_struct_from_pack(cls._packer, *(value,))

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> _T:
        """
        Read and decode a fixed-length field from memory.

        Args:
            buf_mv: Memoryview of binary data.

        Returns:
            The unpacked value (int, float, bytes, etc.).
        """
        return cls._packer.unpack_from(buf_mv)[0]


# endregion

# region VariableField


class VarLenField(Field, Generic[_T]):
    """
    Represents a variable-length array-like field.

    Example:
        >>> C_n(b"HELLO").pack_into(buffer)

    By default, the first byte is interpreted as the element count or length,
    followed by the actual data bytes.

    Attributes:
        _FMT (str): Format string for each element (e.g. `'c'`).
        value (Collection[_T]): The stored data.
    """

    _FMT: ClassVar[str]
    _HAS_PREFIX: ClassVar[bool] = True

    __slots__ = "value"

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Collection[_T], length: Optional[int] = None):
        length = length or len(value)
        buffer.write_struct(f"{cls.ENDIAN}{cls._FMT * length}", *value)

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> Collection[_T]:
        """
        Unpack a variable-length field from buffer.

        Args:
            buf_mv: Memoryview starting with 1-byte length prefix.

        Returns:
            Collection of unpacked elements.
        """
        length = int.from_bytes(buf_mv[:1], byteorder="little")
        return struct.unpack(f"{cls.ENDIAN}{cls._FMT * length}", buf_mv[1:])


# endregion

# region ByteField


class BytesField(Field):
    """
    Represents raw byte data (B_1 / B_n types).

    For variable-length fields (`B_n`), the first byte is the length prefix.
    """

    _VAR: ClassVar[bool] = False

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: bytes):
        if cls._VAR:
            value = len(value).to_bytes(1, byteorder="little") + value
        buffer.write_bytes(value)

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> bytes:
        """
        Unpack raw byte data.

        Args:
            buf_mv: Memoryview containing bytes.

        Returns:
            Raw bytes (excluding length prefix if `_VAR=True`).
        """
        offset = 1 if cls._VAR else 0
        return buf_mv[offset:].tobytes()


# endregion

# region Kx Field


class KxField(Field, Generic[_T]):
    __slots__ = ("length", "value")

    element_type: type[Field]

    def __init__(self, length: int = 0, value: Optional[Collection[_T]] = None):
        """
        Initialize a KxField with a sequence of values.

        Args:
            value: Sequence of scalar values (e.g. [1, 2, 3])
            length: Optional number of elements; defaults to len(value)
        """
        if value is None:
            value = tuple()

        if length != len(value):
            raise ValueError("length and value length must be equal")

        self.value = tuple(value)

    def __init_subclass__(cls, element_type=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if element_type is not None:
            cls.element_type = element_type

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Collection[_T]) -> None:
        elem_type = cls.element_type
        if issubclass(elem_type, FixedField):
            packer = elem_type._packer
            for v in value:
                buffer.write_struct_from_pack(packer, v)
        else:
            for v in value:
                elem_type.pack_into(buffer, v)

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> Collection[_T]:
        elem_type = cls.element_type
        if issubclass(elem_type, FixedField):
            element_size = elem_type._packer.size
            length = len(buf_mv) // element_size
            return [elem_type._packer.unpack_from(buf_mv, offset=i * element_size)[0] for i in range(length)]
        else:
            raise NotImplementedError()


# endregion

# region Basic Fixed Length Fields


# Unsigned integers
class U_1(FixedField[int]):
    _FMT = "B"


class U_2(FixedField[int]):
    _FMT = "H"


class U_4(FixedField[int]):
    _FMT = "I"


# Signed integers
class I_1(FixedField[int]):
    _FMT = "b"


class I_2(FixedField[int]):
    _FMT = "h"


class I_4(FixedField[int]):
    _FMT = "i"


# Floats
class R_4(FixedField[float]):
    _FMT = "f"


class R_8(FixedField[float]):
    _FMT = "d"


# Character
class C_1(FixedField[str]):
    _FMT = "c"

    @classmethod
    def normalize_value(cls, value: str) -> bytes:
        return str.encode(("" if value is None else value), "ascii")


# endregion


# region Variable Length Fields


class C_n(VarLenField[str]):
    _FMT = "c"

    @classmethod
    def normalize_value(cls, value: Collection[str]) -> Collection[bytes]:
        if value is None:
            return []
        return [str.encode(("" if v is None else v), "ascii") for v in value]


# endregion

# region Kx Fields


class KxU_1(KxField[int], element_type=U_1):
    pass


class KxU_2(KxField[int], element_type=U_2):
    pass


class KxC_n(KxField[str], element_type=C_n):
    pass


class KxR_4(KxField[float], element_type=R_4):
    pass


# endregion


# region Byte Fields


class B_1(BytesField):
    pass


class B_n(BytesField):
    _VAR = True


# endregion
