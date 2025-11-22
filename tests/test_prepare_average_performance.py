from pathlib import Path
import pytest
from main import read_csv_files
from reports import AveragePerformance


def test_prepare_average_performance(path_1: Path, path_2: Path) -> None:
    list_objects = read_csv_files([str(path_1), str(path_2)])
    report = AveragePerformance()
    result_items = report.prepare(list_objects)
    expected_max_performance = 4.70
    expected_min_performance = 4.50
    expected_max_position = "Mobile Developer"
    expected_min_position = "Backend Developer"

    assert result_items[0]["position"] == expected_max_position
    assert result_items[-1]["position"] == expected_min_position
    assert result_items[0]["performance"] == expected_max_performance
    assert result_items[-1]["performance"] == expected_min_performance


