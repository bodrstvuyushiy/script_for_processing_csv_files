from abc import ABC, abstractmethod
from collections import defaultdict

from tabulate import tabulate

from dto import Employee


class Report(ABC):
    slug: str

    @abstractmethod
    def prepare(self, list_items: list[Employee]) -> list[dict]:
        pass


class AveragePerformance(Report):
    slug = "performance"

    def prepare(self, list_objects: list[Employee]) -> list[dict]:
        prepare_dict: dict[str, list[float]] = defaultdict(list)
        for item in list_objects:
            prepare_dict[item.position].append(item.performance)

        result_items: list[dict] = []
        for position, performance in prepare_dict.items():
            result_items.append(
                {
                    "position": position,
                    "performance": round(sum(performance) / len(performance), 2),
                }
            )
        result_items.sort(key=lambda item: item["performance"], reverse=True)

        return result_items


REPORTS_REGISTRY: dict[str, Report] = {AveragePerformance.slug: AveragePerformance()}


def available_reports():
    return list(REPORTS_REGISTRY.keys())


def generate_report(name_report: str, list_objects: list[Employee]) -> str:
    report = REPORTS_REGISTRY[name_report]
    result_items = report.prepare(list_objects)

    table_data: list[list] = []
    for idx, item in enumerate(result_items, 1):
        row = [idx] + list(item.values())
        table_data.append(row)
    headers = [""] + list(result_items[0].keys())

    return tabulate(table_data, headers, floatfmt=".2f")
