from pathlib import Path
import sys
import csv
import pytest

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from dto import Employee  # noqa: E402
from main import read_csv_files  # noqa: E402


@pytest.fixture
def data_headers() -> list[str]:
    headers = [
        "name ",
        " position",
        "completed_tasks ",
        "performance ",
        "skills",
        "team",
        "experience_years",
    ]

    return headers


@pytest.fixture
def data_employees_1() -> list[list]:
    employees = [
        [
            "David Chen",
            "Mobile Developer",
            36,
            4.9,
            "Swift, Kotlin, React Native, iOS",
            "Mobile Team",
            3,
        ],
        [
            "Elena Popova",
            "Backend Developer",
            43,
            4.8,
            "Java, Spring Boot, MySQL, Redis",
            "API Team",
            3,
        ],
    ]

    return employees


@pytest.fixture
def data_employees_2() -> list[list]:
    employees = [
        [
            "Jhon Snow",
            "Mobile Developer",
            36,
            4.5,
            "Swift, Kotlin, React Native, iOS",
            "Mobile Team",
            3,
        ],
        [
            "Victor Hram",
            "Backend Developer",
            43,
            4.2,
            "Java, Spring Boot, MySQL, Redis",
            "API Team",
            3,
        ],
    ]

    return employees


@pytest.fixture
def path_1(tmp_path: Path, data_headers: list[str], data_employees_1: list[list]) -> Path:
    path = tmp_path / "employee123.csv"

    with path.open("w", encoding="utf-8", newline="") as file:
        csv_writter = csv.writer(file)
        csv_writter.writerow(data_headers)
        csv_writter.writerows(data_employees_1)

    return path


@pytest.fixture
def path_2(tmp_path: Path, data_headers: list[str], data_employees_2: list[list]) -> Path:
    path = tmp_path / "employee246.csv"

    with path.open("w", encoding="utf-8", newline="") as file:
        csv_writter = csv.writer(file)
        csv_writter.writerow(data_headers)
        csv_writter.writerows(data_employees_2)

    return path


@pytest.fixture
def data_list_objects(path_1: Path, path_2: Path) -> list[Employee]:
    list_str_files = [str(path_1), str(path_2)]
    return read_csv_files(list_str_files)
