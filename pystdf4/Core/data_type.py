import abc
import struct
from typing import TYPE_CHECKING, Any, ClassVar, Collection, Generic, Optional, TypeVar

from pystdf4.Core.dynamic_buffer import DynamicBuffer

if TYPE_CHECKING:
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
        self.value = value

    def pack_into(self, buffer: "DynamicBuffer", value: Any = None) -> None:
        """
        Serialize (pack) this field into the provided buffer.

        Args:
            buffer: The `DynamicBuffer` instance to write into.
            value: Optional override for this field's stored value.

        Raises:
            ValueError: If neither an argument nor stored value is available.
        """
        value = self.value if value is None else value
        if value is None:
            raise ValueError("Value must be provided")
        self._pack_into(buffer, value)

    @abc.abstractmethod
    def _pack_into(self, buffer: "DynamicBuffer", value: Any) -> None:
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

    def __init__(self, value: Optional[_T] = None):
        """
        Initialize the fixed-length field with an optional value.

        Args:
            value: The field's value. Can be any serializable type.
        """
        super().__init__(value)

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

    def _pack_into(self, buffer: "DynamicBuffer", value: _T):
        """
        Write the fixed-length value into the buffer.

        Args:
            buffer: Target DynamicBuffer.
            value: Value to serialize.
        """
        buffer.write_struct_from_pack(self._packer, *(value,))

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> _T:
        """
        Read and decode a fixed-length field from memory.

        Args:
            buf_mv: Memoryview of binary data.

        Returns:
            The unpacked value (int, float, bytes, etc.).
        """
        return cls._packer.unpack_from(buffer=buf_mv)[0]


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

    __slots__ = "value"

    def __init__(
        self,
        value: Optional[Collection[_T]] = None,
    ):
        """
        Initialize the variable-length field.

        Args:
            value: The collection of elements.
            length: Optional length override.
        """
        self.value = value

    def _pack_into(
        self,
        buffer: "DynamicBuffer",
        value: Collection[_T],
        length: Optional[int] = None,
    ):
        """
        Pack a sequence of elements into the buffer.

        Args:
            buffer: Target DynamicBuffer.
            value: Sequence of elements to pack.
            length: Optional length override.

        Raises:
            ValueError: If no data provided.
        """
        length = length or len(value)
        buffer.write_struct(f"{self.ENDIAN}{self._FMT * length}", *value)

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

    def _pack_into(self, buffer: "DynamicBuffer", value: bytes):
        """
        Write raw bytes into the buffer.

        Args:
            buffer: Target DynamicBuffer.
            value: Bytes to write.
        """
        if self._VAR:
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

    def _pack_into(self, buffer: DynamicBuffer, value: Any) -> None:
        elem_type = self.element_type
        if issubclass(elem_type, FixedField):
            packer = elem_type._packer
            for v in value:
                buffer.write_struct_from_pack(packer, v)
        else:
            for v in value:
                elem_type(v).pack_into(buffer)

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> Collection[_T]:
        elem_type = cls.element_type
        if issubclass(elem_type, FixedField):
            element_size = elem_type._packer.size
            length = len(buf_mv) // element_size
            return [
                elem_type._packer.unpack_from(buf_mv, offset=i * element_size)[0]
                for i in range(length)
            ]
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
class C_1(FixedField[bytes]):
    _FMT = "c"

    def __init__(self, value: str):
        vb = value.encode("ascii")
        super().__init__(vb)


# endregion


# region Variable Length Fields


class C_n(VarLenField[bytes]):
    _FMT = "c"

    def __init__(self, value: Collection[str]):
        vs = [v.encode("ascii") for v in value]
        super().__init__(vs)


# endregion

# region Kx Fields


class KxU_1(KxField[int], element_type=U_1):
    element_type = U_1


class KxU_2(KxField[int], element_type=U_2):
    element_type = U_2


class KxC_n(KxField[str], element_type=C_n):
    element_type = C_n


class KxR_4(KxField[float], element_type=R_4):
    element_type = R_4


# endregion


# region Byte Fields


class B_1(BytesField):
    pass


class B_n(BytesField):
    _VAR = True


# endregion
