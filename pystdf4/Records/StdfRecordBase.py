import abc
from typing import Dict, Type
from pystdf4.DataType.StdfBase import StdfDataBase


# Global registry mapping (REC_TYP, REC_SUB) → record class
_RECORD_REGISTRY: Dict[tuple, Type["StdfRecord"]] = {}


def register_record(rec_typ: int, rec_sub: int):
    """
    Decorator that registers an STDF record class in the global registry.

    Args:
        rec_typ (int): Record type identifier.
        rec_sub (int): Record subtype identifier.

    Returns:
        Callable: The decorator function.

    Raises:
        ValueError: If the record type and subtype are already registered.
    """

    def decorator(cls):
        key = (rec_typ, rec_sub)
        if key in _RECORD_REGISTRY:
            raise ValueError(
                f"Duplicate registration for REC_TYP={rec_typ}, REC_SUB={rec_sub}."
            )
        _RECORD_REGISTRY[key] = cls
        return cls

    return decorator


class StdfRecord(abc.ABC):
    """
    Abstract base class for all STDF records.

    Provides common initialization and factory behavior for
    creating record instances from type/subtype identifiers.

    Class Attributes:
        REC_TYP (int): Record type identifier.
        REC_SUB (int): Record subtype identifier.
    """

    REC_TYP: int
    REC_SUB: int

    def __init__(self, rec_typ=None, rec_sub=None):
        """
        Initialize a StdfRecord instance.

        Args:
            rec_typ (int, optional): Record type override. Defaults to the class-level REC_TYP.
            rec_sub (int, optional): Record subtype override. Defaults to the class-level REC_SUB.
        """
        self.REC_LEN: int = 0
        self.REC_TYP: int = rec_typ or self.REC_TYP
        self.REC_SUB: int = rec_sub or self.REC_SUB

    def __setattr__(self, name: str, value: object) -> None:
        """
        Override attribute assignment to update the py_value of
        STDF data type attributes instead of replacing the object.

        Args:
            name (str): Attribute name.
            value (object): Attribute value.
        """
        attr: StdfDataBase | None = getattr(self, name, None)

        if isinstance(attr, StdfDataBase):
            attr.py_value = value
        else:
            super().__setattr__(name, value)

    @classmethod
    def create(cls, rec_typ: int, rec_sub: int):
        """
        Create a record instance based on its type and subtype.

        Args:
            rec_typ (int): Record type identifier.
            rec_sub (int): Record subtype identifier.

        Returns:
            StdfRecord: An instance of the registered record class,
                        or a generic StdfRecord if not registered.
        """
        key = (rec_typ, rec_sub)
        if key in _RECORD_REGISTRY:
            record_cls = _RECORD_REGISTRY[key]
            return record_cls()
        return cls(rec_typ=rec_typ, rec_sub=rec_sub)

    def serialize(self) -> bytes:
        """Serialize this record into bytes. Must be implemented by subclasses."""
        raise NotImplementedError(
            f"{self.__class__.__name__}.serialize() not implemented."
        )

    def deserialize(self, data: bytes):
        """Deserialize record data from bytes. Must be implemented by subclasses."""
        raise NotImplementedError(
            f"{self.__class__.__name__}.deserialize() not implemented."
        )

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the STDF record.

        Returns:
            str: Developer-friendly representation with class name and key attributes
        """
        return (
            f"{self.__class__.__name__}(REC_TYP={self.REC_TYP!r}, "
            f"REC_SUB={self.REC_SUB!r}, REC_LEN={self.REC_LEN})"
        )
