from pathlib import Path

from .pystdf4.PyStdf4 import PyStdf4


class StdfIO:
    def __init__(self):
        pass

    def read_stdf(self, file_path: str | Path) -> bytes:
        raise NotImplementedError()

    def write_stdf(self, file_path: str | Path):
        pass

    def read_pystdf4(self, data: PyStdf4):
        pass

    def write_pystdf4(self) -> PyStdf4:
        raise NotImplementedError()
