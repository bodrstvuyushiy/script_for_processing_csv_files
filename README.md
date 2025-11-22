# script_for_processing_csv_files

1. Для вашего удобство зависимости настроеные через Poetry, можно установить командой:`make deps`.
2. Отчет по performance запускается командой: `make report-performance`.
Конечно он сработает, если документы для обработки находятся в каталоге docs (vash_computer/script_for_processing_csv_files/docs/). Если ваши файлы находятся в другой директории или вам нравится более классический способ, то команда будет выглядеть так: `python3 src/main.py --report performance --files ./docs/employees1.csv ./docs/employees2.csv`.
Или чем-то подобным: `python3 src/main.py --report performance --files /directoriya/k/vashemu/documentu/employees1.csv /directoriya/k/vashemu/documentu/employees2.csv`.
3. Тесты запускаем командой: `make test` или `poetry run pytest`
4. И прогоняем форматеры/линтеры: `make fmt`.


Благодарю вас за это задания)