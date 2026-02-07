# REST API Contract: Todo Tasks

**Feature**: `001-core-backend` | **Date**: 2025-12-28 | **Version**: 1.0.0

---

## Base Configuration

**Development**: `http://localhost:8000/api/v1`  
**Headers**: `Content-Type: application/json`

---

## Data Models

### Task Object
```json
{
  "id": 1,
  "title": "Task title",
  "completed": false,
  "created_at": "2025-01-12T10:30:00Z",
  "updated_at": "2025-01-12T10:30:00Z"
}
```

### Error Response
```json
{
  "detail": "Error message"
}
```

---

## Endpoints

### POST /tasks
Create new task.

**Request:**
```json
{"title": "Buy groceries"}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false,
  "created_at": "2025-01-12T10:30:00Z",
  "updated_at": "2025-01-12T10:30:00Z"
}
```

**Errors:**
- `400` - Invalid input (empty title, >100 chars)
- `422` - Validation failed

---

### GET /tasks
Retrieve all tasks.

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false,
    "created_at": "2025-01-12T10:30:00Z",
    "updated_at": "2025-01-12T10:30:00Z"
  }
]
```

**Errors:**
- `500` - Database error

---

### GET /tasks/{id}
Retrieve specific task.

**Response:** `200 OK` (Task object)

**Errors:**
- `404` - Task not found
- `400` - Invalid ID format

---

### PUT /tasks/{id}
Update task.

**Request:**
```json
{
  "title": "Updated title",
  "completed": true
}
```

**Response:** `200 OK` (Updated task object)

**Errors:**
- `404` - Task not found
- `400` - Invalid input

---

### DELETE /tasks/{id}
Delete task.

**Response:** `204 No Content`

**Errors:**
- `404` - Task not found

---

## Validation Rules

- **title**: 1-100 characters, required for POST, optional for PUT
- **completed**: boolean, optional
- **id**: positive integer

---

## Status Codes

| Code | Usage |
|------|-------|
| 200 | GET, PUT success |
| 201 | POST success |
| 204 | DELETE success |
| 400 | Invalid input |
| 404 | Not found |
| 422 | Validation error |
| 500 | Server error |