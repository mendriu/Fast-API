# FastAPI Project

A simple FastAPI application.

## Setup

1. Create virtual environment: `python -m venv .venv`
2. Activate: `. .venv/bin/activate` (Linux) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `uvicorn app.main:app --reload`

Or use make: `make install` and `make run`

## API

- GET / : Hello World
- GET /items/{item_id} : Get item by ID