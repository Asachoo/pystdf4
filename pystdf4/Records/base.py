import abc
from struct import pack
from typing import Dict, Type
from .DataType.base import StdfDataBase


# Global registry mapping (REC_TYP, REC_SUB) → record class
_RECORD_REGISTRY: Dict[tuple, Type["StdfRecordBase"]] = {}


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


class StdfRecordBase(abc.ABC):
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

    # region Magic Methods

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
            if isinstance(value, StdfDataBase):
                attr = value
            else:
                attr.py_value = value
        else:
            super().__setattr__(name, value)

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the STDF record.

        Returns:
            str: Developer-friendly representation with class name and key attributes
        """
        return f"{self.__class__.__name__}(REC_TYP={self.REC_TYP!r}, REC_SUB={self.REC_SUB!r})"

    # endregion

    # region Factory Methods

    @classmethod
    def create(cls, rec_typ: int, rec_sub: int):
        """
        Create a record instance based on its type and subtype.

        Args:
            rec_typ (int): Record type identifier.
            rec_sub (int): Record subtype identifier.

        Returns:
            StdfRecordBase: An instance of the registered record class,
                        or a generic StdfRecordBase if not registered.
        """
        key = (rec_typ, rec_sub)
        if key in _RECORD_REGISTRY:
            record_cls = _RECORD_REGISTRY[key]
            return record_cls()
        obj = cls()
        obj.REC_TYP = rec_typ
        obj.REC_SUB = rec_sub
        return obj

    # endregion

    # region Properties

    @property
    def data_bytes(self) -> bytes:
        data_bytes = []
        for field_name in self.__annotations__:
            field_value = getattr(self, field_name)
            try:
                if isinstance(field_value, StdfDataBase):
                    data_bytes.append(field_value.stdf_value)
                elif isinstance(field_value, list):
                    for item in field_value:
                        item: StdfDataBase
                        data_bytes.append(item.stdf_value)
            except Exception as e:
                e.args = (
                    f"{self.__class__.__name__} Invalid value for {field_name}: {field_value}",
                )
                raise e
        return b"".join(data_bytes)

    @property
    def stdf_bytes(self) -> bytes:
        data = self.data_bytes
        return pack("<HBB", len(data), self.REC_TYP, self.REC_SUB) + data

    # endregion
