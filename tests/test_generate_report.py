import pytest
from dto import Employee
from reports import generate_report


def test_generate_report_average_performance(data_list_objects: list[Employee]) -> None:
    output_data = generate_report("performance", data_list_objects)
    expected_output_data = (
        "    position             performance\n"
        "--  -----------------  -------------\n"
        " 1  Mobile Developer            4.70\n"
        " 2  Backend Developer           4.50"
    )

    assert output_data == expected_output_data
