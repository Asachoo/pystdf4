from struct import Struct

from pystdf4.Core.dynamic_buffer import DynamicBuffer

from .base import ScalarField

# region Actual implementation


class U_1(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}B")


class U_2(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}H")


class U_4(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}I")


class I_1(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}b")


class I_2(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}h")


class I_4(ScalarField[int, int]):
    _packer = Struct(f"{ScalarField._endian}i")


class R_4(ScalarField[float, float]):
    _packer = Struct(f"{ScalarField._endian}f")


class R_8(ScalarField[float, float]):
    _packer = Struct(f"{ScalarField._endian}d")


class C_1(ScalarField[str, bytes]):
    _packer = Struct(f"{ScalarField._endian}c")

    @classmethod
    def _normalize(cls, value: str) -> bytes:
        return str.encode(value, "ascii")


class B_1(ScalarField[bytes, bytes]):
    @classmethod
    def _pack_into(cls, buffer: DynamicBuffer, value: bytes) -> None:
        buffer.write_bytes(value)

    @classmethod
    def _unpack_from(cls, buf_mv: memoryview) -> bytes:
        return buf_mv.tobytes()


# endregion
