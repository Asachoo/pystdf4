from pystdf4.Records.StdfRecordBase import StdfRecordBase


class PyStdf4:
    records: list[StdfRecordBase]

    def __init__(self):
        self.records = list()

    def add_record(self, record: StdfRecordBase):
        self.records.append(record)

    def to_bytes(self) -> bytes:
        stdf_bytes = bytearray()
        for record in self.records:
            stdf_bytes += record.stdf_bytes

        return stdf_bytes

    def parse_stdf(self, stdf_data: bytes):
        # Parsing logic to populate records from stdf_data
        pass
