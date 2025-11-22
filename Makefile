deps:
	poetry install --no-root

report-performance:
	python3 src/main.py --report performance --files ./docs/employees1.csv ./docs/employees2.csv

test:
	poetry run pytest

fmt:
	poetry run ruff format --line-length 120
	poetry run ruff check --fix --line-length 120
	poetry run flake8 src tests --exclude .venv --max-line-length 120
	make fmt-gitignore

fmt-gitignore:
	sort --output .gitignore .gitignore
	awk "NF" .gitignore > .gitignore.temp && mv .gitignore.temp .gitignore
