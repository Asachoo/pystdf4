import pytest

from pystdf4.Core.dynamic_buffer import DynamicBuffer


class TestDynamicBuffer:
    """Unit tests for DynamicBuffer"""

    def setup_method(self):
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

    def test_init_large_capacity(self):
        buf = DynamicBuffer(10_000_000)
        assert buf.capacity == 10_000_000
        assert len(buf) == 0
    # endregion

    # region capacity tests
    def test_capacity_setter_normal(self):
        self.buf.capacity = 200
        assert self.buf.capacity == 200

    def test_capacity_setter_invalid(self):
        self.buf.offset = 10
        with pytest.raises(ValueError):
            self.buf.capacity = 5

    def test_multiple_capacity_changes(self):
        self.buf.capacity = 150
        assert self.buf.capacity == 150
        self.buf.capacity = 300
        assert self.buf.capacity == 300
    # endregion

    # region length / to_bytes tests
    def test_len_and_to_bytes(self):
        # offset starts at 0, so to_bytes() should be empty
        assert len(self.buf) == 0
        assert self.buf.to_bytes() == b""
        # manually increment offset to simulate writing
        self.buf.offset = 5
        assert len(self.buf) == 5
        assert self.buf.to_bytes() == b"\x00\x00\x00\x00\x00"
    # endregion

    # region _ensure_capacity / auto growth tests
    def test_ensure_capacity_no_grow_needed(self):
        self.buf.offset = 50
        self.buf._ensure_capacity(50)  # total 100 < 128
        assert self.buf.capacity == 128

    def test_ensure_capacity_growth(self):
        self.buf.offset = 120
        self.buf._ensure_capacity(20)  # total 140 > 128
        assert self.buf.capacity >= 140
        # ensure offset did not change
        assert self.buf.offset == 120

    def test_multiple_ensure_capacity_growth(self):
        self.buf.offset = 100
        for size in [50, 200, 500]:
            self.buf._ensure_capacity(size)
            assert self.buf.capacity >= self.buf.offset + size
    # endregion

    # region repr tests
    def test_repr(self):
        s = repr(self.buf)
        assert "DynamicBuffer" in s
        assert f"offset={self.buf.offset}" in s
        assert f"capacity={self.buf.capacity}" in s
    # endregion
