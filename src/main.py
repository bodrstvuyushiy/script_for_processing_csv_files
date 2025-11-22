import argparse
import csv
from pathlib import Path

from dto import Employee
from reports import available_reports, generate_report


def read_csv_files(paths: list[str]) -> list[Employee]:
    list_objects: list[Employee] = []
    for raw_path in paths:
        path = Path(raw_path).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"Файл {raw_path} не найден")

        with path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            if reader.fieldnames:
                reader.fieldnames = [fieldname.strip() for fieldname in reader.fieldnames]

            try:
                for row in reader:
                    list_objects.append(
                        Employee(
                            name=row["name"],
                            position=row["position"],
                            completed_tasks=int(row["completed_tasks"]),
                            performance=float(row["performance"]),
                            skills=row["skills"],
                            team=row["team"],
                            experience_years=int(row["experience_years"]),
                        )
                    )
            except KeyError as e:
                raise KeyError(
                    f"Неверно записан заголовок {e},\nпроверьте файл {{path}} на корректность и поробуйте заново"
                )
            except ValueError as e:
                ValueError(
                    f"Значение записано в ячейку не в верном формате {e},\n"
                    "проверьте файл {path} на корректность и поробуйте заново"
                )

    return list_objects


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", choices=available_reports())
    args = parser.parse_args()

    list_objects = read_csv_files(args.files)
    if not list_objects:
        raise FileExistsError("Объектов для чтения не было обнаружено")
    output_data = generate_report(args.report, list_objects)
    print(output_data)


if __name__ == "__main__":
    main()
