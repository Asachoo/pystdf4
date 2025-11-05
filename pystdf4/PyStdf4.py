from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pystdf4.Records.base import StdfRecordBase


class PyStdf4:
    stdf_byte_segments: list[bytes]

    def __init__(self):
        self.stdf_byte_segments = list()

    def add_record(self, record: "StdfRecordBase"):
        self.stdf_byte_segments.append(record.stdf_bytes)

    def to_bytes(self) -> bytes:
        return b"".join(self.stdf_byte_segments)

    def parse_stdf(self, stdf_data: bytes):
        pass
