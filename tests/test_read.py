from pathlib import Path
import pytest
from main import read_csv_files


def test_read_csv_files(
        path_1: Path, path_2: Path, data_headers: list[str],
        data_employees_1: list, data_employees_2: list
        ) -> None:
    list_str_files = [str(path_1), str(path_2)]
    list_objects = read_csv_files(list_str_files)
    expected_count_objects = len(data_employees_1) + len(data_employees_2)
    expected_headers = [header.strip() for header in data_headers]
    expected_employees = data_employees_1 + data_employees_2

    assert len(list_objects) == expected_count_objects
    assert list(list_objects[0].__dict__.keys()) == expected_headers
    assert [
        [
            o.name, o.position, o.completed_tasks,
            o.performance, o.skills, o.team, o.experience_years
        ] for o in list_objects
    ] == expected_employees
