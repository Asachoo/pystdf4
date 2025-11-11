import abc
from typing import Optional, Sequence, Type, TypeVar

from pystdf4.Core.data_type import Field

T = TypeVar("T", int, float, str, bytes)

# Define a generic type variable for the record type
ElementT = TypeVar("ElementT", bound=Field)


class StdfRecordBase(abc.ABC):
    REC_TYP: int
    REC_SUB: int

    @property
    def header(self) -> tuple[int, int]:
        return (self.REC_TYP, self.REC_SUB)

    @property
    def fields(self) -> Sequence[Field]:
        return [getattr(self, field) for field in self.__annotations__]

    def validate_array(
        self,
        arr_name: str,
        arr_obj: Optional[Sequence[T]],
        count: int,
        ele_type: Type[ElementT],
    ) -> Sequence[ElementT]:
        """
        Validates an array of STDF data type elements.

        Args:

            arr_obj (Sequence[str | float| int | bytes]): Array of STDF data type elements.
            count (int): Expected number of elements in the array.

        Raise:
            ValueError: If the array is not valid.
        """
        # Initalize the array if it is None
        arr_obj = arr_obj or []

        # Check if the array has the expected length
        if count != len(arr_obj):
            raise ValueError(f"Record {arr_name} requires {count} elements, but got {len(arr_obj)}")

        return [ele_type(x) for x in arr_obj]
