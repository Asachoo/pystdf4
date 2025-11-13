import struct

import pytest

from pystdf4.Core.dynamic_buffer import DynamicBuffer


class TestDynamicBuffer:
    """Unit tests for DynamicBuffer"""

    def setup_method(self):
        """Initialize a fresh buffer for each test."""
        self.buf = DynamicBuffer(128)

    # region initialization tests
    def test_init_default(self):
        assert self.buf.capacity >= 128
        assert len(self.buf) == 0
        assert self.buf.offset == 0

    def test_init_custom_capacity(self):
        buf2 = DynamicBuffer(512)
        assert buf2.capacity == 512
        assert len(buf2) == 0

    # endregion

    # region write tests
    def test_write_bytes(self):
        data = b"hello world"
        start = self.buf.write_bytes(data)
        assert start == 0
        assert self.buf.to_bytes() == data
        assert len(self.buf) == len(data)

    def test_write_struct(self):
        fmt = "<HBB"
        values = (100, 10, 20)
        start = self.buf.write_struct(fmt, *values)
        unpacked = struct.unpack(fmt, self.buf.to_bytes())
        assert unpacked == values
        assert start == 0

    # endregion

    # region edit tests
    def test_edit_bytes_valid(self):
        self.buf.write_bytes(b"abcdefghij")
        self.buf.edit_bytes(2, b"xy")
        assert self.buf.to_bytes() == b"abxyefghij"

    def test_edit_bytes_invalid_offset(self):
        self.buf.write_bytes(b"abc")
        with pytest.raises(ValueError):
            self.buf.edit_bytes(5, b"xyz")

    def test_edit_bytes_negative_offset(self):
        self.buf.write_bytes(b"abc")
        with pytest.raises(ValueError):
            self.buf.edit_bytes(-1, b"x")

    def test_edit_struct_valid(self):
        fmt = "<H"
        self.buf.write_struct(fmt, 1000)
        self.buf.edit_struct(0, fmt, 2000)
        unpacked = struct.unpack(fmt, self.buf.to_bytes())
        assert unpacked[0] == 2000

    def test_edit_struct_invalid_offset(self):
        self.buf.write_bytes(b"abc")
        fmt = "<H"
        with pytest.raises(ValueError):
            self.buf.edit_struct(2, fmt, 100)

    # endregion

    # region read tests
    def test_read_bytes_valid(self):
        data = b"abcdefgh"
        self.buf.write_bytes(data)
        read_data = self.buf.read_bytes(0, 4)
        assert read_data == b"abcd"
        read_data2 = self.buf.read_bytes(4, 4)
        assert read_data2 == b"efgh"

    def test_read_bytes_out_of_bounds(self):
        self.buf.write_bytes(b"abc")
        with pytest.raises(ValueError):
            self.buf.read_bytes(0, 5)
        with pytest.raises(ValueError):
            self.buf.read_bytes(3, 1)

    def test_read_struct_valid(self):
        fmt = "<HBB"
        values = (1000, 10, 20)
        self.buf.write_struct(fmt, *values)
        unpacked = self.buf.read_struct(0, fmt)
        assert unpacked == values

    def test_read_struct_out_of_bounds(self):
        self.buf.write_bytes(b"\x00\x01")
        with pytest.raises(ValueError):
            self.buf.read_struct(0, "<I")

    # endregion

    # region reserve, view & slice tests
    def test_reserve_space(self):
        mv = self.buf.reserve(10)
        assert isinstance(mv, memoryview)
        assert mv.nbytes == 10
        mv[:] = b"A" * 10
        assert self.buf.to_bytes() == b"A" * 10

    def test_view_readonly(self):
        self.buf.write_bytes(b"data")
        mv = self.buf.view(readonly=True)
        assert mv.readonly is True
        assert mv.tobytes() == b"data"

    def test_view_writable(self):
        self.buf.write_bytes(b"data")
        mv = self.buf.view(readonly=False)
        mv[0:2] = b"up"
        assert self.buf.to_bytes() == b"upta"

    def test_slice_valid(self):
        data = b"abcdef"
        self.buf.write_bytes(data)
        mv = self.buf.slice(1, 4)
        assert mv.tobytes() == b"bcd"
        mv[0] = ord("X")
        assert self.buf.to_bytes() == b"aXcdef"

    def test_slice_out_of_bounds(self):
        self.buf.write_bytes(b"abc")
        with pytest.raises(ValueError):
            self.buf.slice(-1, 2)
        with pytest.raises(ValueError):
            self.buf.slice(0, 5)

    def test_read_after_reset(self):
        self.buf.write_bytes(b"abcd")
        self.buf.reset()
        with pytest.raises(ValueError):
            self.buf.read_bytes(0, 1)
        with pytest.raises(ValueError):
            self.buf.read_struct(0, "<B")

    # endregion

    # region reset & shrink tests
    def test_reset(self):
        self.buf.write_bytes(b"123456")
        self.buf.reset()
        assert self.buf.offset == 0
        assert self.buf.to_bytes() == b""

    def test_deep_reset(self):
        self.buf.write_bytes(b"abc")
        self.buf.edit_bytes(1, b"X")
        self.buf.reset(deep_reset=True)
        assert self.buf.offset == 0
        assert self.buf.to_bytes() == b""
        self.buf.write_bytes(b"abc")
        assert self.buf.to_bytes() == b"abc"

    def test_shrink_to_fit(self):
        self.buf.write_bytes(b"data")
        orig_cap = self.buf.capacity
        self.buf.shrink_to_fit()
        assert self.buf.capacity == len(b"data")
        assert self.buf.capacity < orig_cap

    # endregion

    # region capacity & length tests
    def test_capacity_setter_normal(self):
        self.buf.write_bytes(b"data")
        self.buf.capacity = 200
        assert self.buf.capacity == 200

    def test_capacity_setter_invalid(self):
        self.buf.write_bytes(b"12345")
        with pytest.raises(ValueError):
            self.buf.capacity = 3

    def test_len_property(self):
        self.buf.write_bytes(b"hello")
        assert len(self.buf) == 5

    def test_capacity_property(self):
        buf2 = DynamicBuffer(128)
        assert buf2.capacity == 128

    # endregion

    # region auto growth & large data tests
    def test_auto_grow(self):
        buf = DynamicBuffer(8)
        data = b"x" * 20
        start = buf.write_bytes(data)
        assert buf.capacity >= 20
        assert buf.to_bytes() == data
        assert start == 0

    def test_multi_grow(self):
        buf = DynamicBuffer(4)
        for _ in range(10):
            buf.write_bytes(b"abcd")
        assert buf.capacity >= 40
        assert len(buf) == 40

    def test_large_data_write(self):
        buf = DynamicBuffer(1024)
        data = b"x" * 100_000
        start = buf.write_bytes(data)
        assert buf.to_bytes() == data
        assert buf.capacity >= 100_000
        assert start == 0
