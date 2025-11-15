from struct import Struct

import pytest

from pystdf4.Core.data_base import DeferredField, FieldBase, ImmediateField
from pystdf4.Core.dynamic_buffer import DynamicBuffer


# ===========================
# FieldBase Tests
# ===========================
class TestFieldBase:
    def test_pack_into_not_implemented(self):
        class DummyField(FieldBase):
            pass

        with pytest.raises(NotImplementedError):
            DummyField.pack_into(None, 123)  # type: ignore

    def test_unpack_from_not_implemented(self):
        class DummyField(FieldBase):
            pass

        with pytest.raises(NotImplementedError):
            DummyField.unpack_from(memoryview(b""))


# ===========================
# ImmediateField Tests
# ===========================
class TestImmediateField:
    class DummyImmediate(ImmediateField):
        @staticmethod
        def _normalize_value(value, size=0):
            return value

    def setup_method(self):
        self.buf = DynamicBuffer(16)
        self.field_cls = self.DummyImmediate

    def test_pascal_bytes(self):
        data = b"abc"
        result = self.field_cls._pascal_bytes(data)
        assert result == b"\x03abc"

    def test_pack_into_writes_data(self):
        data = b"xyz"
        self.field_cls.pack_into(self.buf, data)
        assert self.buf.to_bytes() == data
        assert self.buf.offset == len(data)

    def test_pack_into_with_field_size(self):
        self.field_cls.field_size = 5
        data = b"abcde"
        self.field_cls.pack_into(self.buf, data)
        # should write data and pad remaining 3 bytes with whatever is in buffer (0)
        written = self.buf.to_bytes()
        assert written[:2] == b"ab"
        assert len(written) == 5
        assert self.buf.offset == 5


# ===========================
# DeferredField Tests
# ===========================
class TestDeferredField:
    class DummyDeferred(DeferredField):
        num_elements = 1
        endian = "<"
        struct_format = "H"

        # Mock CacheMixin methods
        cached_values = []
        buffer_offsets = []

        @classmethod
        def _enqueue_value(cls, value, offset, size):
            cls.cached_values.append(value)
            cls.buffer_offsets.append(offset)

        @classmethod
        def flush_cache(cls, packed_mv: memoryview, buffer: DynamicBuffer):
            # write serialized bytes into buffer
            start = buffer.offset
            buffer._mv[start : start + len(packed_mv)] = packed_mv.tobytes()

    def setup_method(self):
        self.buf = DynamicBuffer(32)
        self.field_cls = self.DummyDeferred
        self.field_cls.cached_values.clear()
        self.field_cls.buffer_offsets.clear()

    def test_field_size_computed(self):
        # __init_subclass__ should compute field_size = struct.calcsize("<2H") = 4
        assert self.field_cls.field_size == Struct("<H").size

    def test_pack_into_caches_value(self):
        self.field_cls.pack_into(self.buf, 100)
        assert self.field_cls.cached_values == [100]
        assert self.field_cls.buffer_offsets == [0]
        assert self.buf.offset == self.field_cls.field_size

    def test_serialize_sequence(self):
        seq = [1]
        self.field_cls.buffer_offsets = [0]  # simulate two elements
        serialized = self.field_cls._serialize_sequence(seq)
        assert serialized == Struct("<H").pack(*seq)

    def test_flush_cache_to_buffer(self):
        # enqueue 2 values
        self.field_cls._enqueue_value(10, 0, 2)
        self.field_cls._enqueue_value(20, 2, 2)
        self.field_cls.flush_cache_to_buffer(self.buf)
        # total 2 * num_elements = 4 values written
        expected_bytes = Struct("<2H").pack(10, 20)  # last two 0 padding
        self.buf.offset += len(expected_bytes)
        assert self.buf.to_bytes()[: len(expected_bytes)] == expected_bytes
