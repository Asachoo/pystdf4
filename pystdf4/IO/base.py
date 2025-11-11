from pathlib import Path

from ..Core.dynamic_buffer import DynamicBuffer


class StdfIOBase:
    __slots__ = ("file_path", "buffer")

    def __init__(self, file_path: str):
        self.buffer = DynamicBuffer()
        self.file_path = Path(file_path)
