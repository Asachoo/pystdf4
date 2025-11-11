from typing import Sequence

from pystdf4.Records.base import Field, StdfRecordBase

from .base import StdfIOBase


class Stfd4Writer(StdfIOBase):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def write_record(self, record: StdfRecordBase):
        # Step 1: Write the header of the record
        record_start = self._write_header(record.header)

        # Step 2: Write the fields of the record
        self._write_fields(record.fields)

        # Step 3: Update the length of the record
        record_end = self.buffer.offset
        record_length = record_end - (record_start + 4)
        self.buffer.edit_struct(record_start, "<H", record_length)

    def _write_header(self, header: tuple[int, int]) -> int:
        """
        Write the header of a record to the file.
        """
        return self.buffer.write_struct("<HBB", 0, *header)

    def _write_fields(self, fields: Sequence[Field]):
        for field in fields:
            field.pack_into(self.buffer)

    def _write_field(self, field: Field):
        field.pack_into(self.buffer)
