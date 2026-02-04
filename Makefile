SHELL := /bin/bash
.ONESHELL:

.PHONY: venv install run docker-build docker-run

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