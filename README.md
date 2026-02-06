# FastAPI Project

A FastAPI application with Docker, PostgreSQL, JWT authentication, middleware and tests.

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
4. Set environment variables (DATABASE_URL, SECRET_KEY)
5. Run: `uvicorn app.main:app --reload`

Or use make: `make install` and `make run`

## Project Structure

```
app/
├── main.py              # FastAPI application
├── database.py          # Database configuration
├── auth.py              # JWT authentication utilities
├── middleware.py        # Request logging middleware
├── exceptions.py        # Custom exception handlers
├── schemas/             # Pydantic models (request/response)
│   ├── item.py
│   └── user.py
├── models/              # SQLAlchemy models (ORM)
│   ├── item.py
│   └── user.py
├── crud/                # Database operations
│   └── item.py
└── routers/             # API endpoints
    ├── auth.py
    └── items.py
tests/
├── conftest.py          # Pytest fixtures
├── test_main.py         # Root endpoint tests
├── test_auth.py         # Authentication tests
└── test_items.py        # Items CRUD tests
```

## Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_items.py

# Run specific test
pytest tests/test_auth.py::test_login_success
```

Tests use SQLite in-memory database for isolation.

## Database

PostgreSQL database running in Docker container:
- Host: `localhost`
- Port: `5432`
- Database: `fastapi_db`
- User: `postgres`
- Password: `postgres`

Data is persisted in Docker volume `postgres_data`.

## Middleware

### CORS
Cross-Origin Resource Sharing enabled for all origins.

### Request Logging
Every request is logged with:
- Unique request ID
- HTTP method and path
- Response status code
- Processing time

Response headers include:
- `X-Request-ID` - unique request identifier
- `X-Process-Time` - request processing time

### Exception Handling
- Custom `AppException` for controlled errors
- Global exception handler for unexpected errors (returns 500)

## Authentication

JWT-based authentication with OAuth2 password flow.

### Auth Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get JWT token |
| GET | `/auth/me` | Get current user info (requires auth) |

### Register
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "secret"}'
```

### Login
```bash
curl -X POST http://localhost:8000/auth/login \
  -d "username=user@example.com&password=secret"
```

### Use Token
```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer <your-token>"
```

## API Endpoints

### Root
- `GET /` - Hello World
- `GET /health` - Health check

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
