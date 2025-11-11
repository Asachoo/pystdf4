from pathlib import Path

from pystdf4.Core.data_type import B_1, C_1, I_1, I_2, I_4, R_4, R_8, U_1, U_2, U_4, B_n, C_n, KxC_n, KxR_4, KxU_1, KxU_2
from pystdf4.Core.dynamic_buffer import DynamicBuffer


class StdfIOBase:
    __slots__ = (
        "file_path",
        "buffer",
        "B_1",
        "C_1",
        "I_1",
        "I_2",
        "I_4",
        "R_4",
        "R_8",
        "U_1",
        "U_2",
        "U_4",
        "B_n",
        "C_n",
        "KxC_n",
        "KxR_4",
        "KxU_1",
        "KxU_2",
    )

    def __init__(self, file_path: str):
        self.buffer = DynamicBuffer()
        self.file_path = Path(file_path)

        self.B_1 = B_1()
        self.C_1 = C_1()
        self.I_1 = I_1()
        self.I_2 = I_2()
        self.I_4 = I_4()
        self.R_4 = R_4()
        self.R_8 = R_8()
        self.U_1 = U_1()
        self.U_2 = U_2()
        self.U_4 = U_4()
        self.B_n = B_n()
        self.C_n = C_n()
        self.KxC_n = KxC_n()
        self.KxR_4 = KxR_4()
        self.KxU_1 = KxU_1()
        self.KxU_2 = KxU_2()
