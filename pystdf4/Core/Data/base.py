from abc import ABC, abstractmethod
from struct import Struct
from typing import Any, ClassVar, Generic, Optional, Sequence, Type, TypeVar, cast

from pystdf4.Core.dynamic_buffer import DynamicBuffer

# region Base

_T_in = TypeVar("_T_in")
_T_out = TypeVar("_T_out")


class Field(ABC):
    _endian: ClassVar[str] = "<"
    __slots__ = ("value",)

    def __init__(self, value: Optional[Any] = None):
        self.value = value

    def __repr__(self):
        return f"<{self.__class__.__name__} value={self.value!r}>"

    @classmethod
    @abstractmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Any) -> None:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def _unpack_from(cls, buf_mv: memoryview) -> Any:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def _normalize(cls, value: Any) -> Any:
        raise NotImplementedError()

    # Export Methods
    @classmethod
    def pack_into(cls, buffer: DynamicBuffer, value: Any) -> None:
        if value is None:
            raise ValueError("Value must be provided for class method packing")
        cls._pack_into(buffer, cls._normalize(value))

    @classmethod
    def unpack_from(cls, buf_mv: memoryview) -> Any:
        return cls._unpack_from(buf_mv)

    # TODO: Remove this method at some point
    def self_pack_into(self, buffer: DynamicBuffer) -> None:
        self.pack_into(buffer, self.value)


# endregion


# region Scalar


class ScalarField(Field, Generic[_T_in, _T_out]):
    _packer: ClassVar[Optional[Struct]] = None

    @classmethod
    def _normalize(cls, value: _T_in) -> _T_out:
        return cast(_T_out, value)

    @classmethod
    def _get_packer(cls) -> Struct:
        if cls._packer is None:
            raise ValueError("Packer not defined for class")
        return cls._packer

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: _T_out) -> None:
        buffer.write_struct_from_pack(cls._get_packer(), value)

    @classmethod
    def _unpack_from(cls, buf_mv: memoryview) -> _T_out:
        return cls._get_packer().unpack_from(buf_mv)[0]


# endregion


# region Sequence


class SequenceField(Field, Generic[_T_in, _T_out], ABC):
    __slots__ = ("length", "value")

    @classmethod
    def _normalize(cls, value: Sequence[_T_in]) -> Sequence[_T_out]:
        return cast(Sequence[_T_out], value)


class FixLenField(SequenceField[_T_in, _T_out]):
    _length: ClassVar[int]

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Sequence[_T_out]) -> None:
        pass

    @classmethod
    def _unpack_from(cls, buf_mv: memoryview) -> Sequence[_T_out]:
        raise NotImplementedError()


class VarLenField(SequenceField[_T_in, _T_out]):
    _fmt: ClassVar[str] = ""

    @classmethod
    @abstractmethod
    def _normalize(cls, value: Sequence[_T_in]) -> bytes:
        raise NotImplementedError()

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: bytes) -> None:
        v = len(value).to_bytes(4, "little") + value
        buffer.write_bytes(v)

    @classmethod
    def _unpack_from(cls, buf_mv: memoryview) -> Sequence[_T_out]:
        raise NotImplementedError()


class KxLenField(SequenceField[_T_in, _T_out]):
    __slots__ = ("_length", "value")
    element_type: ClassVar[Type[Field]]

    def __init__(self, length: int, value: Optional[Sequence[_T_in]]):
        self._length = length
        super().__init__(value or tuple())

    @classmethod
    def _normalize(cls, value: Sequence[_T_in]) -> Sequence[_T_out]:
        return super()._normalize(value)

    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: Sequence[_T_out]) -> None:
        for v in value:
            cls.element_type._pack_into(buffer, v)

    @classmethod
    def _unpack_from(cls, buf_mv: memoryview) -> Sequence[_T_out]:
        raise NotImplementedError()


# endregion
