.ONESHELL:

.PHONY: venv install run

venv:
	. .venv/bin/activate
	@echo "Virtual environment activated in this shell session."

install:
	. .venv/bin/activate
	pip install -r requirements.txt

run:
	. .venv/bin/activate
	uvicorn app.main:app --reload