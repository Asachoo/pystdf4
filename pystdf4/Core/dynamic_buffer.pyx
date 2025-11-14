# cython: boundscheck=False, wraparound=False, initializedcheck=False
# cython: cdivision=True
# distutils: language = c++

cdef class DynamicBuffer:
    """
    High-performance dynamically resizable byte buffer.
    Cython accelerated version.
    """

    cdef public bytearray _buffer
    cdef public unsigned char[:] _mv
    cdef Py_ssize_t _capacity
    cdef public Py_ssize_t offset

    def __init__(self, int initial_capacity=1024*1024):
        self._buffer = bytearray(initial_capacity)
        self._mv = self._buffer
        self._capacity = initial_capacity
        self.offset = 0

    # ---- properties ----

    @property
    def capacity(self) -> int:
        return <int>self._capacity

    @capacity.setter
    def capacity(self, int value):
        if value < self.offset:
            raise ValueError(
                f"Cannot shrink below current offset ({self.offset} bytes)"
            )

        cdef bytearray new_buf = bytearray(value)
        new_buf[:self.offset] = self._buffer[:self.offset]

        self._buffer = new_buf
        self._mv = new_buf
        self._capacity = value

    def __len__(self):
        return self.offset

    def __repr__(self):
        return f"<DynamicBuffer offset={self.offset} capacity={self._capacity}>"

    # ---- private but Python-callable ----
    cpdef void _ensure_capacity(self, Py_ssize_t size):
        cdef Py_ssize_t target = self.offset + size
        cdef Py_ssize_t desired = self._capacity

        if target > desired:
            while desired < target:
                desired = (desired * 3 + 1) >> 1
            self.capacity = desired

    # ---- public ----

    def to_bytes(self) -> bytes:
        return bytes(self._mv[:self.offset])
