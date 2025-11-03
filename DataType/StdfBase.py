import abc
from typing import TypeVar, Generic, Optional

T = TypeVar("T", int, float, str, bytes)


class StdfDataBase(abc.ABC, Generic[T]):
    """
    Base class for STDF record data types.

    Attributes:
        py_value: Python-native value of the field (int, float, str, bytes).
        c_value: Internal byte representation (core storage).
        stdf_value: STDF file representation (may include length prefixes or special encoding).

    Notes:
        - All conversions go through `c_value`.
        - Setting `py_value` or `stdf_value` automatically updates `c_value`.
        - Use `c_value` as the authoritative internal representation.
    """

    ENDIAN = "<"

    __slots__ = ("_code", "_description", "_bytes_len", "_max_len", "_c_value")

    def __init__(
        self, code: str, description: str, bytes_len: int = -1, max_len: int = -1
    ):
        """
        Initialize a STDF data field.

        Args:
            code: STDF type code (e.g., "C*12", "U*2", "I*4").
            description: Field description.
            bytes_len: Fixed byte length of the internal representation (-1 if variable).
            max_len: Maximum allowed byte length (-1 if unlimited).
        """
        self._code = code
        self._description = description
        self._bytes_len = bytes_len
        self._max_len = max_len
        self._c_value: Optional[bytes] = None

    def __str__(self) -> str:
        val = self.py_value if self._c_value is not None else "N/A"
        return f"{self._code} ({self._description}): {val}"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(code={self._code}, "
            f"description={self._description}, bytes_len={self._bytes_len})"
        )

    # region Properties

    @property
    def c_value(self) -> bytes:
        """Internal byte representation of the field."""
        if self._c_value is None:
            raise ValueError(f"C-Value for {self._code} is not set")
        return self._c_value

    @c_value.setter
    def c_value(self, value: bytes) -> None:
        """Set internal byte representation with length validation."""
        self._validate_length(value)
        self._c_value = value

    @property
    def py_value(self) -> T:
        """Python-native value, derived from c_value."""
        return self._parse_py()

    @py_value.setter
    def py_value(self, value: T) -> None:
        """Set Python value, automatically converting to internal c_value."""
        self.c_value = self._build_py(value)

    @property
    def stdf_value(self) -> bytes:
        """STDF file-level value (may include length prefix or special encoding)."""
        return self._parse_stdf()

    @stdf_value.setter
    def stdf_value(self, value: bytes) -> None:
        """Set STDF file-level value, automatically converting to internal c_value."""
        self.c_value = self._build_stdf(value)

    # endregion

    # region Private Methods

    def _validate_length(self, value: bytes):
        """Validate the length of the byte value against fixed/max length constraints."""
        if self._bytes_len != -1 and len(value) != self._bytes_len:
            raise ValueError(f"{self._code}: length {len(value)} != expected {self._bytes_len}")
        if self._max_len != -1 and len(value) > self._max_len:
            raise ValueError(f"{self._code}: length {len(value)} exceeds max {self._max_len}")

    # endregion

    # region Abstract Methods for Python Value

    @abc.abstractmethod
    def _build_py(self, py_value: T) -> bytes:
        """
        Convert a Python value to internal bytes.

        Must validate `py_value` before conversion.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _parse_py(self) -> T:
        """Convert internal bytes (c_value) to Python value."""
        raise NotImplementedError

    # endregion

    # region Abstract Methods for STDF File Value

    @abc.abstractmethod
    def _build_stdf(self, stdf_value: bytes) -> bytes:
        """Convert STDF file bytes to internal bytes (c_value)."""
        raise NotImplementedError

    @abc.abstractmethod
    def _parse_stdf(self) -> bytes:
        """Convert internal bytes (c_value) to STDF file bytes."""
        raise NotImplementedError

    # endregion
