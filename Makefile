SHELL := /bin/bash
.ONESHELL:

.PHONY: venv install run docker-build docker-run format lint test check

venv:
	source .venv/bin/activate
	@echo "Virtual environment activated in this shell session."

install:
	source .venv/bin/activate
	pip install -r requirements.txt

run:
	source .venv/bin/activate
	uvicorn app.main:app --reload

docker-build:
	docker build -t fastapi-app .

docker-run:
	docker run -p 8000:8000 fastapi-app

# Formatting
format:
	black app/ tests/
	isort app/ tests/

# Linting
lint:
	black --check app/ tests/
	isort --check-only app/ tests/
	ruff check app/ tests/
	pylint --disable=C0114,C0115,C0116,R0903,C0414,C0103 app/
	mypy app/

# Testing
test:
	pytest

# All checks (format + lint + test)
check: format lint test

# Pre-commit setup
pre-commit-install:
	pre-commit install

pre-commit-run:
	pre-commit run --all-files
