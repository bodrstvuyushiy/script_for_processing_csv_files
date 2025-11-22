deps:
	poetry install --no-root

fmt:
	poetry run flake8
	poetry run ruff
	poetry run black
	