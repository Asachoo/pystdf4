from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pystdf4.Records.base import StdfRecordBase


class PyStdf4:
    records: list["StdfRecordBase"]

    def __init__(self):
        self.records = list()

    def add_record(self, record: "StdfRecordBase"):
        self.records.append(record)

    def to_bytes(self) -> bytes:
        return b"".join(record.stdf_bytes for record in self.records)

    def parse_stdf(self, stdf_data: bytes):
        # Parsing logic to populate records from stdf_data
        pass
