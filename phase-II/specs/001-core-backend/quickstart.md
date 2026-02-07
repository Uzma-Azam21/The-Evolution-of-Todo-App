# Quick Start: Backend API

**Feature**: `001-core-backend` | **Date**: 2025-12-28

---

## Prerequisites

- Python 3.10+
- PostgreSQL (Neon account)
- pip or poetry

---

## Setup

### 1. Environment Variables

Create `.env`:
```env
DATABASE_URL=postgresql://user:pass@host/db?sslmode=require
API_PORT=8000
DEBUG=true
```

### 2. Install Dependencies

```bash
cd phase-II/core-backend
pip install -r requirements.txt
```

### 3. Initialize Database

```bash
python -m src.database.init_db
```

---

## Run Application

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

**Access:**
- API: http://localhost:8000/api/v1
- Docs: http://localhost:8000/docs

---

## Test Endpoints

### Create Task
```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task"}'
```

### List Tasks
```bash
curl http://localhost:8000/api/v1/tasks
```

### Get Task
```bash
curl http://localhost:8000/api/v1/tasks/1
```

### Update Task
```bash
curl -X PUT http://localhost:8000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Delete Task
```bash
curl -X DELETE http://localhost:8000/api/v1/tasks/1
```

---

## Run Tests

```bash
pytest tests/ -v --cov=src
```

---

## Troubleshooting

**Port in use:**
```bash
lsof -ti:8000 | xargs kill -9
```

**Database connection:**
```bash
python -c "from src.database import test_connection; test_connection()"
```

---

## Documentation

- Swagger UI: http://localhost:8000/docs
- API Contract: `specs/contracts/api-task-contract.md`