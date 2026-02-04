# FastAPI Project

A simple FastAPI application with Docker support.

## Setup

### Docker (recommended)

```bash
docker-compose up --build
```

API will be available at http://localhost:8000

### Local

1. Create virtual environment: `python -m venv .venv`
2. Activate: `. .venv/bin/activate` (Linux) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `uvicorn app.main:app --reload`

Or use make: `make install` and `make run`

## API Endpoints

### Root
- `GET /` - Hello World

### Items
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/items/` | List all items |
| GET | `/items/{id}` | Get item by ID |
| POST | `/items/` | Create new item |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

### Item Schema
```json
{
  "name": "string (1-100 chars, required)",
  "description": "string (optional)",
  "price": "float > 0 (required)",
  "tax": "float (optional)"
}
```

## Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
