import csv
import math
import re
import struct
import sys
from itertools import zip_longest
from pathlib import Path
from typing import List, Optional, Tuple

from pystdf4.IO import Stdf4Writer


def parse_test_data_segment(test_data_segment: List[str]) -> Tuple[float, ...]:
    return tuple(map(safg_float, test_data_segment))


def parse_coordinates_segment(coordinates_segment: List[str]) -> Tuple[int, ...]:
    return tuple(map(int, coordinates_segment))


def parse_moving_limit_segment(moving_limit_segment: str) -> Tuple[str, ...]:
    return tuple(moving_limit_segment.split(";"))


def parse_bins_segment(bins_segment: List[str]) -> Tuple[int, ...]:
    return tuple(map(int, bins_segment))


def parse_site_info_segment(
    site_info_segment: List[str],
) -> Tuple[Tuple[int, ...], ...]:
    site_number = len(site_info_segment) // 3
    if site_number * 3 != len(site_info_segment):
        raise ValueError("Site info segment should have 3 values per site.")
    return tuple(
        tuple(
            map(
                safe_int,
                [
                    site_info_segment[i],
                    site_info_segment[site_number + 2 * i],
                    site_info_segment[site_number + 2 * i + 1],
                ],
            )
        )
        for i in range(site_number)
    )


def safg_float(value: str) -> float:
    """
    Convert a string to float, and return nan if the string is empty.

    Args:
        value (str): _description_

    Returns:
        float: _description_
    """
    return float(value) if value else math.nan


def safe_int(value: str) -> int:
    """
    Convert a string to int, and return 0 if the string is empty.

    Args:
        value (str): _description_

    Returns:
        int: _description_
    """
    return int(value) if value else 0


class PTR_D:
    __slots__ = (
        "test_number",
        "result",
        "test_txt",
        "lo_limit",
        "hi_limit",
        "unit",
        "test_flag",
    )

    def __init__(
        self,
        test_number: int,
        result: float,
        test_txt: str,
        lo_limit: float,
        hi_limit: float,
        unit: str,
        test_pass: Optional[bool],
    ):
        """
        Part test parameters

        Args:
            test_number (int): _description_
            site_number (int): _description_
            result (float): _description_
            test_txt (str): _description_
            lo_limit (float): _description_
            hi_limit (float): _description_
            unit (str): _description_
            test_flag (bool, optional): _description_. Defaults to None.
        """
        self.test_number = test_number
        self.result = result
        self.test_txt = test_txt
        self.lo_limit = lo_limit
        self.hi_limit = hi_limit
        self.unit = unit
        # test_pass may be True, False or None
        # if test_pass is None, it means test_flg should be calculated based on lo_limit, hi_limit and result
        # if test_pass in True or False, directly set test_flg based on test_pass
        test_pass = (
            test_pass if test_pass is not None else (lo_limit <= result <= hi_limit)
        )
        self.test_flag = 0
        if not test_pass:
            self.test_flag |= 1 << 7


class PRR_D:
    __slots__ = ("hard_bin", "soft_bin", "x_coord", "y_coord", "test_t", "part_id")

    @property
    def part_flag(self) -> int:
        return 0 if self.hard_bin == 1 else 8

    def __init__(
        self,
        hard_bin: int,
        soft_bin: int,
        x_coord: int,
        y_coord: int,
        test_t: int,
        part_id: int,
    ):
        self.hard_bin = hard_bin
        self.soft_bin = soft_bin
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.test_t = test_t
        self.part_id = part_id


class Part:
    __slots__ = ("site_num", "PTRs", "PRR")
    PRR: Optional[PRR_D]
    PTRs: Tuple[PTR_D, ...]

    def __init__(self, site_num: int = -1):
        self.site_num = site_num
        self.PRR = None
        self.PTRs = tuple()

    def update_ptrs(self, ptrs: Tuple[PTR_D, ...]):
        self.PTRs = ptrs

    def edit_prr(
        self,
        hard_bin: int,
        soft_bin: int,
        x_coord: int,
        y_coord: int,
        test_t: int,
        part_id: int,
    ):
        self.PRR = PRR_D(
            hard_bin=hard_bin,
            soft_bin=soft_bin,
            x_coord=x_coord,
            y_coord=y_coord,
            test_t=test_t,
            part_id=part_id,
        )

    def record(self):
        pass


class StdfGenerator:
    csv_site_header_partten = re.compile(r"^Site(\d+) (Time|SOT|EOT)")
    pat_item_pattern = re.compile(r"\[\[?(\w+)&\w+(\d+)\|([\d\.]+)\]?\]")

    @property
    def site_count(self) -> int:
        return len(self.site_indices)

    @property
    def test_count(self) -> int:
        return len(self.lower_limits)

    def __init__(
        self,
        lower_limits: Tuple[float, ...],
        higher_limits: Tuple[float, ...],
        units: Tuple[str, ...],
        test_txts: Tuple[str, ...],
        site_indices: Tuple[int, ...],
    ):
        """
        Generate parts based on the given parameters.

        Args:
            lower_limits (Tuple[float, ...]): _description_
            higher_limits (Tuple[float, ...]): _description_
            units (Tuple[str, ...]): _description_
            test_txts (Tuple[str, ...]): _description_
            site_indices (Tuple[int, ...]): _description_
        """
        # Check input parameters validity
        if len(lower_limits) != len(higher_limits) or len(lower_limits) != len(units):
            raise ValueError("Length of limits, units and test_txts should be equal.")

        # Check site indices validity
        if len(site_indices) == 0:
            raise ValueError("Site indices should not be empty.")

        self.lower_limits = lower_limits
        self.higher_limits = higher_limits
        self.units = units
        self.test_txts = test_txts
        self.site_indices = site_indices

        # data properties
        self.parts: List[Part] = []

        # Stastics properties
        self.failed_count: dict[str, int] = {txt: 0 for txt in test_txts}
        self.failed_dut_count: int = 0
        self.passed_dut_count: int = 0

    def __repr__(self) -> str:
        repr_str = f"StdfGenerator(Site indices: {self.site_indices}; Test Items: {self.test_count})"
        for i, (lower_limit, higher_limit, unit, test_txt) in enumerate(
            zip(self.lower_limits, self.higher_limits, self.units, self.test_txts)
        ):
            repr_str += f"\n\tIndex: {i + 1}; Test Text: {test_txt}; Limit: [{lower_limit} - {higher_limit} {unit}]"

        return repr_str

    @classmethod
    def generate_stdf_object(
        cls,
        lower_limit_header: List[str],
        higher_limit_header: List[str],
        unit_header: List[str],
        test_txt_header: List[str],
    ) -> "StdfGenerator":
        lower_limits, higher_limits, units, test_txts = [], [], [], []
        site_indices = set()

        for lower_limit, higher_limit, unit, test_txt in zip_longest(
            lower_limit_header,
            higher_limit_header,
            unit_header,
            test_txt_header,
            fillvalue="",
        ):
            if test_txt in {"X", "Y", "MovingLimitFail", "HardBin", "SoftBin"}:
                continue
            elif match_rst := cls.csv_site_header_partten.match(test_txt):
                site_index = int(match_rst.group(1))
                site_indices.add(site_index)
            else:
                lower_limits.append(float(lower_limit))
                higher_limits.append(float(higher_limit))
                units.append(unit)
                test_txts.append(test_txt)
        return cls(
            tuple(lower_limits),
            tuple(higher_limits),
            tuple(units),
            tuple(test_txts),
            tuple(site_indices),
        )

    def evaluate_part_test(
        self,
        test_results: Tuple[float, ...],
        coordinates: Tuple[int, ...],
        moving_limit: Tuple[str, ...],
        bins: Tuple[int, ...],
        sites_information: Tuple[Tuple[int, ...], ...],
        part_id: int,
    ):
        """
        Evaluate the test result and return the test flag.

        Args:
            test_results (Tuple[float, ...]): _description_
        """
        # Check input parameters validity
        if len(test_results) != self.test_count:
            raise ValueError("Length of test_results should be equal to test_count.")

        # Get actual site number according to the SOT/EOT and Time
        site_number = -1
        for site_index, site_info in enumerate(sites_information):
            if sum(site_info) == 0:
                continue
            elif site_number == -1:
                site_number = site_index
            else:
                raise ValueError("Site number should be set only once!")

        # Create Part object and update PTRs
        if site_number == -1:
            raise ValueError("Site number should be set!")

        part_obj = Part(self.site_indices[site_number])

        ptrs = []
        moving_limit_set = set(moving_limit)

        # Append PTR objects to ptrs list
        for i, (lower_limit, higher_limit, test_txt, unit, result) in enumerate(
            zip(
                self.lower_limits,
                self.higher_limits,
                self.test_txts,
                self.units,
                test_results,
            ),
            start=1,
        ):
            test_pass = (
                test_txt not in moving_limit_set
                if self.pat_item_pattern.match(test_txt)
                else None
            )
            ptr = PTR_D(
                test_number=i,
                result=result,
                test_txt=test_txt,
                lo_limit=lower_limit,
                hi_limit=higher_limit,
                unit=unit,
                test_pass=test_pass,
            )
            if ptr.test_flag != 0:
                self.failed_count[test_txt] += 1

            ptrs.append(ptr)

        # Update PRR_D object
        part_obj.update_ptrs(tuple(ptrs))

        # Edit PRR_D object
        part_obj.edit_prr(
            hard_bin=bins[0],
            soft_bin=bins[1],
            x_coord=coordinates[0],
            y_coord=coordinates[1],
            test_t=sites_information[site_number][0],
            part_id=part_id,
        )
        if bins[0] != 1:
            self.failed_dut_count += 1
        else:
            self.passed_dut_count += 1

        self.parts.append(part_obj)

    @staticmethod
    def _gen_stdf_record(typ: int, sub: int, data: bytes) -> bytes:
        return struct.pack("<HBB", len(data), typ, sub) + data

    def write_stdf_file(
        self,
        stdf_file_path: Path,
        setup_time: int,
        start_time: int,
        finish_time: int,
        job_name: str,
        wafer_id: str,
        lot_id: str,
    ):
        # with open(stdf_file_path, "wb") as f:
        with Stdf4Writer(str(stdf_file_path)) as stdf:
            # stdf.write_record(FAR(CPU_TYPE=2, STDF_VER=4))
            stdf.FAR(CPU_TYPE=2, STDF_VER=4)

            # write MIR record
            stdf.MIR(
                SETUP_T=setup_time,
                START_T=start_time,
                STAT_NUM=0,
                BURN_TIM=0,
                LOT_ID=lot_id,
                JOB_NAM=job_name,
                PART_TYP="",
                NODE_NAM="",
                TSTR_TYP="",
            )

            # write SDR record
            stdf.SDR(HEAD_NUM=0, SITE_GRP=0, SITE_CNT=0)

            # write WIR record
            stdf.WIR(HEAD_NUM=0, SITE_GRP=0, START_T=start_time, WAFER_ID=wafer_id)

            for part in self.parts:
                # write PIR record
                stdf.PIR(HEAD_NUM=0, SITE_NUM=part.site_num)

                # write PTR records
                for ptr in part.PTRs:
                    stdf.PTR(
                        HEAD_NUM=0,
                        TEST_NUM=ptr.test_number,
                        SITE_NUM=part.site_num,
                        TEST_FLG=ptr.test_flag.to_bytes(1, "little"),
                        RESULT=ptr.result,
                        TEST_TXT=ptr.test_txt,
                        OPT_FLAG=int(14).to_bytes(1, "little"),
                        LO_LIMIT=ptr.lo_limit,
                        HI_LIMIT=ptr.hi_limit,
                        UNITS=ptr.unit,
                        PARM_FLG=b"\x00",
                    )

                if part.PRR is None:
                    raise ValueError("PRR object should not be None.")

                # write PRR record
                stdf.PRR(
                    HEAD_NUM=0,
                    SITE_NUM=part.site_num,
                    PART_FLG=part.PRR.part_flag.to_bytes(1, "little"),
                    NUM_TEST=0,
                    HARD_BIN=part.PRR.hard_bin,
                    SOFT_BIN=part.PRR.soft_bin,
                    X_COORD=part.PRR.x_coord,
                    Y_COORD=part.PRR.y_coord,
                    TEST_T=part.PRR.test_t,
                    PART_ID=str(part.PRR.part_id),
                )

            # write TSR records
            for i, test_txt in enumerate(self.test_txts, start=1):
                failed_count = self.failed_count.get(test_txt, 0)

                stdf.TSR(
                    HEAD_NUM=0,
                    SITE_NUM=255,
                    TEST_NUM=i,
                    EXEC_CNT=len(self.parts),
                    FAIL_CNT=failed_count,
                    TEST_NAM=test_txt,
                    OPT_FLAG=int(255).to_bytes(1, "little"),
                )

            # write HBR records
            stdf.HBR(
                HEAD_NUM=0,
                SITE_NUM=255,
                HBIN_NUM=1,
                HBIN_CNT=self.passed_dut_count,
                HBIN_NAM="Pass",
            )

            stdf.HBR(
                HEAD_NUM=0,
                SITE_NUM=255,
                HBIN_NUM=2,
                HBIN_CNT=self.failed_dut_count,
                HBIN_NAM="Fail",
            )

            # write PCR record
            stdf.PCR(
                HEAD_NUM=0,
                SITE_NUM=255,
                PART_CNT=len(self.parts),
                GOOD_CNT=self.passed_dut_count,
            )

            # write MRR record
            stdf.MRR(FINISH_T=finish_time)


def convert_csv_to_stdf(
    csv_path_str: str,
    setup_time: int,
    start_time: int,
    finish_time: int,
    wafer_id: str,
    lot_id: str,
    job_name: str,
):
    csv_path = Path(csv_path_str)
    if not csv_path.exists():
        raise FileNotFoundError(f"File {csv_path} does not exist.")

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        # Get headers
        lower_limit_header = next(reader)
        higher_limit_header = next(reader)
        unit_header = next(reader)
        test_txt_header = next(reader)

        stdf_obj = StdfGenerator.generate_stdf_object(
            lower_limit_header[1:],
            higher_limit_header[1:],
            unit_header[1:],
            test_txt_header[1:],
        )

        # Iterate over rows and parse data
        for row in reader:
            # Get test data, coordinates, moving limit, bins, site information separately
            test_data_segment = row[1 : stdf_obj.test_count + 1]
            coordinates_segment = row[stdf_obj.test_count + 1 : stdf_obj.test_count + 3]
            moving_limit_segment = row[stdf_obj.test_count + 3]
            bins_segment = row[stdf_obj.test_count + 4 : stdf_obj.test_count + 6]
            sites_information_segment = row[stdf_obj.test_count + 6 :]

            # Parse segments to corresponding data types
            part_id = int(row[0])
            test_data = parse_test_data_segment(test_data_segment)
            coordinates = parse_coordinates_segment(coordinates_segment)
            moving_limit = parse_moving_limit_segment(moving_limit_segment)
            bins = parse_bins_segment(bins_segment)
            sites_information = parse_site_info_segment(sites_information_segment)

            test_data = map(safg_float, test_data_segment)

            stdf_obj.evaluate_part_test(
                test_results=tuple(test_data),
                coordinates=coordinates,
                bins=bins,
                sites_information=sites_information,
                part_id=part_id,
                moving_limit=moving_limit,
            )

        stdf_obj.write_stdf_file(
            setup_time=setup_time,
            start_time=start_time,
            finish_time=finish_time,
            wafer_id=wafer_id,
            lot_id=lot_id,
            job_name=job_name,
            stdf_file_path=csv_path.with_suffix(".stdf"),
        )


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 7:
        raise ValueError("Invalid number of arguments.")

    csv_path_str, setup_time, start_time, finish_time, wafer_id, lot_id, job_name = args
    convert_csv_to_stdf(
        csv_path_str,
        int(setup_time),
        int(start_time),
        int(finish_time),
        wafer_id,
        lot_id,
        job_name,
    )
