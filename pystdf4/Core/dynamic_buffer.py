import struct
from typing import Any


class DynamicBuffer:
    """
    High-performance dynamically resizable byte buffer.

    This class is designed for low-level binary data construction (e.g., STDF or protocol records).
    It provides in-place memory writes, safe resizing, and minimal object creation overhead.
    """

    __slots__ = ("_buffer", "_mv", "_capacity", "offset")

    def __init__(self, initial_capacity: int = 1024**2):
        """
        Initialize the buffer.

        Args:
            initial_capacity (int): Initial memory capacity in bytes.
        """
        self._buffer = bytearray(initial_capacity)
        self.offset = 0
        self._mv = memoryview(self._buffer)
        self._capacity = initial_capacity

    # region properties
    @property
    def capacity(self) -> int:
        """Current capacity of the buffer."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """
        Resize the buffer to the given capacity.

        Raises:
            ValueError: If the new capacity is smaller than the current offset.
        """
        if value < self.offset:
            raise ValueError(f"Cannot shrink below current offset ({self.offset} bytes)")

        new_buf = bytearray(value)
        new_buf[: self.offset] = self._buffer[: self.offset]
        self._buffer = new_buf
        self._mv = memoryview(new_buf)
        self._capacity = value

    def __len__(self) -> int:
        """Number of valid bytes written to the buffer."""
        return self.offset

    def __repr__(self) -> str:
        return f"<DynamicBuffer offset={self.offset} capacity={self._capacity}>"

    # endregion

    # region private methods

    def _ensure_capacity(self, size: int):
        """
        Ensure sufficient capacity for the next write of `size` bytes.
        """
        if (target := self.offset + size) > self._capacity:
            # Expand at least double or fit the target size
            desired = self._capacity
            while desired < target:
                desired = (desired * 3 + 1) >> 1  # ~1.5x growth
            self.capacity = desired

    # endregion

    # region public methods
    def write_bytes(self, data: bytes) -> int:
        """
        Append bytes to the buffer.

        Args:
            data (bytes): The bytes to write.

        Returns:
            int: Starting offset of written region.
        """
        # Ensure that the buffer has enough capacity for the data
        size = len(data)
        self._ensure_capacity(size)

        start = self.offset
        end = start + size
        self._mv[start:end] = data
        self.offset = end
        return start

    def write_struct(self, fmt: str, *values) -> int:
        """
        Append a struct to the buffer.

        Args:
            fmt (str): The struct format string.
            *values: The values to write.

        Returns:
            int: Starting offset of written region.
        """
        return self.write_struct_from_pack(struct.Struct(fmt), *values)

    def write_struct_from_pack(self, packer: struct.Struct, *values) -> int:
        """
        Append a struct to the buffer using a pre-compiled struct.Struct object.

        Args:
            packer (struct.Struct): The pre-compiled struct.Struct object.
            *values: The values to write.

        Returns:
            int: Starting offset of written region.
        """
        self._ensure_capacity(packer.size)
        start = self.offset
        packer.pack_into(self._mv, start, *values)
        self.offset += packer.size
        return start

    def edit_bytes(self, offset: int, data: bytes) -> None:
        """
        Overwrite existing region in-place.

        Args:
            offset(int): The offset to start editing.
            data(bytes): The bytes to write.

        Raises:
            ValueError: If the edit region is beyond the written region.
        """
        end = offset + len(data)

        # Ensure that the bytes to edit have been written before
        if end > self.offset:
            raise ValueError(f"Edit beyond written region (end={end}, size={self.offset})")

        # Edit the bytes in the buffer inplace
        self._mv[offset:end] = data

    def edit_struct(self, offset: int, fmt: str, *values) -> None:
        """
        Overwrite existing struct in-place.

        Args:
            offset(int): The offset to start editing.
            fmt(str): The struct format string.
            *values: The values to write.

        Raises:
            ValueError: If the edit region is beyond the written region.
        """
        packer = struct.Struct(fmt)
        end = offset + packer.size
        if end > self.offset:
            raise ValueError(f"Edit beyond written region (end={end}, size={self.offset})")
        packer.pack_into(self._mv, offset, *values)

    def read_bytes(self, offset: int, size: int) -> bytes:
        """
        Read `size` bytes from the buffer starting at `offset`.

        Args:
            offset (int): Starting offset.
            size (int): Number of bytes to read.

        Raises:
            ValueError: If the read region is beyond the written region.

        Returns:
            bytes: The bytes read.
        """
        end = offset + size
        if end > self.offset:
            raise ValueError(f"Read beyond written region (end={end}, size={self.offset})")
        return self._mv[offset:end].tobytes()

    def read_struct(self, offset: int, fmt: str) -> Any:
        """
        Read a struct from the buffer starting at `offset`.

        Args:
            offset (int): Starting offset.
            fmt (str): The struct format string.

        Raises:
            ValueError: If the read region is beyond the written region.

        Returns:
            Any: The values read.
        """
        packer = struct.Struct(fmt)
        end = offset + packer.size
        if end > self.offset:
            raise ValueError(f"Read beyond written region (end={end}, size={self.offset})")
        return packer.unpack_from(self._mv, offset)

    def reserve(self, size: int) -> memoryview:
        """
        Reserve space for in-place writing.

        Args:
            size (int): Number of bytes to reserve.

        Returns:
            memoryview: A writable slice for direct modification.
        """
        self._ensure_capacity(size)
        start = self.offset
        end = start + size
        self.offset = end
        return self._mv[start:end]

    # endregion

    # region read / export operations

    def to_bytes(self) -> bytes:
        """Return the valid data as immutable bytes."""
        return self._mv[: self.offset].tobytes()

    def view(self, readonly: bool = True) -> memoryview:
        """
        Return a memoryview over the valid region.

        Args:
            readonly (bool): If True, view is read-only.

        Returns:
            memoryview: A slice of the buffer data.
        """
        mv = self._mv[: self.offset]
        return mv.toreadonly() if readonly else mv

    def reset(self, deep_reset: bool = False):
        """
        Reset the buffer to its initial state.
        """
        if deep_reset:
            self._buffer = bytearray(self._capacity)
            self._mv = memoryview(self._buffer)
        self.offset = 0

    def slice(self, start: int, end: int) -> memoryview:
        """Return a slice of the buffer as memoryview (no copy)."""
        if start < 0 or end > self.offset:
            raise ValueError("Slice out of bounds")
        return self._mv[start:end]

    def shrink_to_fit(self) -> None:
        """
        Reduce capacity to match current data length.
        """
        if self.offset < self._capacity:
            self.capacity = self.offset

    # endregion
