install:
	poetry install

start:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

check:
	poetry check

lint:
	poetry run isort . && poetry run flake8 app

test:
	poetry run pytest -v

coverage:
	poetry run pytest --cov=app --cov-report=xml --cov-report=term-missing