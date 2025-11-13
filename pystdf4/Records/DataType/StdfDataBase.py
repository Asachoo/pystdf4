import abc
from functools import cached_property
from typing import TypeVar, Generic, Optional

T = TypeVar("T", int, float, str, bytes)


class StdfDataBase(abc.ABC, Generic[T]):
    """
    Base class for STDF record data types.

    Core Concepts:
        - Internal Representation (internal_bytes): The core byte storage
        - Python Value (py_value): Native Python representation (int, float, str, bytes)
        - STDF Storage Form (stdf_value): How data is stored in STDF file
          - For fixed-length types: stdf_value == internal_bytes
          - For variable-length types: stdf_value includes length prefixes
        - Missing Data Support: Values can be None to indicate missing data according to STDF spec

    Data Flow:
        Set py_value -> _build_py() -> internal_bytes -> _parse_stdf() -> stdf_value
        Set stdf_value -> _build_stdf() -> internal_bytes -> _parse_py() -> py_value

    Example:
        For a U*2 field with value 258:
        - py_value = 258 (int)
        - internal_bytes = b'\x02\x01' (2 bytes in little-endian)
        - stdf_value = b'\x02\x01' (same as internal_bytes for fixed-length)

        For a C*n field with value "Hello":
        - py_value = "Hello" (str)
        - internal_bytes = b'Hello' (5 bytes)
        - stdf_value = b'\x05Hello' (length-prefixed for variable-length)
    """

    _ENDIAN = "<"  # Little-endian byte order

    __slots__ = (
        "_code",
        "_description",
        "_bytes_len",
        "_max_len",
        "_internal_bytes",
        "_missing_default",
    )

    # region Magic Methods

    def __init__(
        self,
        code: str,
        description: str,
        max_len: int = -1,
        missing_default: Optional[T] = None,
    ):
        """
        Initialize a STDF data field.

        Args:
            code: STDF type code (e.g., "C*1", "U*2", "I*4", "C*n").
            description: Human-readable description of the field.
            bytes_len:
                - For fixed-length types: actual byte length (1, 2, 4, 12, etc.)
                - For variable-length types: -1
            max_len:
                - For bounded variable-length types: maximum allowed bytes
                - For unbounded or fixed-length types: -1
        """
        self._code = code
        self._description = description
        self._bytes_len = StdfDataBase._parse_bytes_len(code)
        self._max_len = max_len
        self._internal_bytes: Optional[bytes] = None
        self._missing_default = missing_default

    def __str__(self) -> str:
        """
        Return a string representation of the STDF data field.

        Returns:
            str: Formatted string showing code, description, and current value
        """
        val = self.py_value if self._internal_bytes is not None else "N/A"
        return f"{self._code} ({self._description}): {val}"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the STDF data field.

        Returns:
            str: Developer-friendly representation with class name and key attributes
        """
        return (
            f"{self.__class__.__name__}(code={self._code!r}, "
            f"description={self._description!r}, bytes_len={self._bytes_len})"
        )

    # region Properties

    @cached_property
    def is_variable_length(self) -> bool:
        """
        Check if the data type is variable-length.

        Returns:
            bool: True if the data type is variable-length, False otherwise
        """
        return self._bytes_len == -1

    @property
    def internal_bytes(self) -> bytes:
        """
        Internal byte representation of the field.

        This is the core storage format used for all conversions between
        Python values and STDF file representations.

        Returns:
            bytes: The internal byte representation of the field

        Raises:
            ValueError: If the internal bytes have not been set
        """
        if self._internal_bytes is None:
            raise ValueError(f"Internal bytes for {self._code} are not set")
        return self._internal_bytes

    @internal_bytes.setter
    def internal_bytes(self, value: bytes) -> None:
        """
        Set internal byte representation with length validation.

        Args:
            value: The byte value to set as internal representation

        Raises:
            ValueError: If the value doesn't meet length constraints
            TypeError: If value is not bytes
        """
        if not isinstance(value, bytes):
            raise TypeError(f"Expected bytes, got {type(value)}")
        self._validate_length(value)
        self._internal_bytes = value

    @property
    def py_value(self) -> T:
        """
        Python-native value, derived from internal_bytes.

        Returns:
            T: Native Python representation (int, float, str, or bytes)

        Note:
            This property is computed on-demand by calling _parse_py()
        """
        return self._parse_py()

    @py_value.setter
    def py_value(self, value: T) -> None:
        """
        Set Python value, automatically converting to internal internal_bytes.

        Args:
            value: Native Python value of the appropriate type

        Raises:
            TypeError: If value is not of the expected type
            ValueError: If value is invalid for this data type
        """
        self.internal_bytes = self._build_py(value)

    @property
    def stdf_value(self) -> bytes:
        """
        STDF file-level value (may include length prefix or special encoding).

        Returns:
            bytes: Representation as it appears in the STDF file

        Note:
            For fixed-length types: identical to internal_bytes
            For variable-length types: includes length prefixes or special encoding
            This property is computed on-demand by calling _parse_stdf()
        """
        if self._internal_bytes is None:
            if self._missing_default is not None:
                self.py_value = self._missing_default
        return self._parse_stdf()

    @stdf_value.setter
    def stdf_value(self, value: bytes) -> None:
        """
        Set STDF file-level value, automatically converting to internal internal_bytes.

        Args:
            value: Raw bytes as they appear in the STDF file

        Raises:
            ValueError: If the value is invalid for this data type
            TypeError: If value is not bytes
        """
        self.internal_bytes = self._build_stdf(value)

    # endregion

    # region Private Methods

    def _validate_length(self, value: bytes) -> None:
        """
        Validate the length of the byte value against fixed/max length constraints.

        Args:
            value: Byte value to validate

        Raises:
            ValueError: If length constraints are violated
        """
        if self._bytes_len != -1 and len(value) != self._bytes_len:
            raise ValueError(
                f"{self._code}: length {len(value)} != expected {self._bytes_len}"
            )
        if self._max_len != -1 and len(value) > self._max_len:
            raise ValueError(
                f"{self._code}: length {len(value)} exceeds max {self._max_len}"
            )

    @staticmethod
    def _parse_bytes_len(code: str) -> int:
        """
        Parse bytes length from STDF type code.

        Args:
            code: STDF type code (e.g., "C*1", "U*2", "I*4", "C*n")

        Returns:
            int: Number of bytes in the data type, or -1 for variable-length types
        """
        if code.endswith("*n"):
            return -1
        try:
            return int(code.split("*")[1])
        except (IndexError, ValueError):
            raise ValueError(f"Invalid code format: {code}")

    # endregion

    # region Abstract Methods for Python Value

    @abc.abstractmethod
    def _build_py(self, py_value: T) -> bytes:
        """
        Convert a Python value to internal bytes.

        This method must be implemented by subclasses to define how
        native Python values are converted to internal byte representation.

        Args:
            py_value: Native Python value of the correct type

        Returns:
            bytes: Internal byte representation

        Raises:
            TypeError: If py_value is not of the expected type
            ValueError: If py_value is out of valid range or invalid format

        Example:
            For U*2 with value 258:
            >>> _build_py(258)
            b'\\x02\\x01'  # 258 in little-endian 2-byte format
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _parse_py(self) -> T:
        """
        Convert internal bytes (internal_bytes) to Python value.

        This method must be implemented by subclasses to define how
        internal byte representation is converted to native Python values.

        Returns:
            T: Native Python representation (int, float, str, or bytes)

        Raises:
            ValueError: If internal_bytes contains invalid data

        Example:
            For U*2 with internal_bytes b'\\x02\\x01':
            >>> _parse_py()
            258  # 258 from little-endian 2-byte format
        """
        raise NotImplementedError

    # endregion

    # region Abstract Methods for STDF File Value

    @abc.abstractmethod
    def _build_stdf(self, stdf_bytes: bytes) -> bytes:
        """
        Convert STDF file bytes to internal bytes (internal_bytes).

        This method must be implemented by subclasses to define how
        raw STDF file bytes are converted to internal representation.

        Args:
            stdf_bytes: Raw bytes as they appear in STDF file

        Returns:
            bytes: Internal byte representation (internal_bytes)

        Note:
            For variable-length types, this extracts the actual data from the
            length-prefixed format.

        Example:
            For C*n with stdf_bytes b'\\x05Hello':
            >>> _build_stdf(b'\\x05Hello')
            b'Hello'  # Extract data, removing length prefix
        """
        raise NotImplementedError

    @abc.abstractmethod
    def _parse_stdf(self) -> bytes:
        """
        Convert internal bytes (internal_bytes) to STDF file bytes.

        This method must be implemented by subclasses to define how
        internal representation is converted to raw STDF file bytes.

        Returns:
            bytes: Representation as it appears in the STDF file

        Example:
            For C*n with internal_bytes b'Hello':
            >>> _parse_stdf()
            b'\\x05Hello'  # Add length prefix for variable-length format
        """
        raise NotImplementedError

    # endregion
