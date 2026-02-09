# API Contracts: API Ownership & User Isolation

**Feature**: `003-api-access-rules`  
**Created**: 2025-12-28

---

## Authentication Header

All endpoints require Bearer token authentication:

```http
Authorization: Bearer <jwt_token>
```

---

## GET /api/tasks

List all tasks for the authenticated user.

### Request

```http
GET /api/tasks
Authorization: Bearer <token>
```

### Success Response (200 OK)

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "user_id": "550e8400-e29b-41d4-a716-446655440000",
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2025-12-28T10:00:00Z",
      "updated_at": "2025-12-28T10:00:00Z"
    }
  ]
}
```

### Error Responses

**401 Unauthorized - Missing Token**
```json
{
  "success": false,
  "error": "Authentication required"
}
```

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

---

## POST /api/tasks

Create a new task for the authenticated user.

### Request

```http
POST /api/tasks
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread"
}
```

### Request Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Task title (max 200 chars) |
| `description` | string | No | Task description |

### Success Response (201 Created)

```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2025-12-28T10:00:00Z",
    "updated_at": "2025-12-28T10:00:00Z"
  }
}
```

### Error Responses

**400 Bad Request - Invalid Input**
```json
{
  "success": false,
  "error": "Title is required"
}
```

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

---

## GET /api/tasks/{id}

Get a specific task (must belong to authenticated user).

### Request

```http
GET /api/tasks/1
Authorization: Bearer <token>
```

### Success Response (200 OK)

```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2025-12-28T10:00:00Z",
    "updated_at": "2025-12-28T10:00:00Z"
  }
}
```

### Error Responses

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

**404 Not Found - Task Doesn't Exist or Not Owned**
```json
{
  "success": false,
  "error": "Task not found"
}
```

---

## PUT /api/tasks/{id}

Update a task (must belong to authenticated user).

### Request

```http
PUT /api/tasks/1
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Buy groceries and fruits",
  "description": "Milk, eggs, bread, apples"
}
```

### Request Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Task title (max 200 chars) |
| `description` | string | No | Task description |

### Success Response (200 OK)

```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries and fruits",
    "description": "Milk, eggs, bread, apples",
    "completed": false,
    "created_at": "2025-12-28T10:00:00Z",
    "updated_at": "2025-12-28T11:00:00Z"
  }
}
```

### Error Responses

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

**404 Not Found - Task Doesn't Exist or Not Owned**
```json
{
  "success": false,
  "error": "Task not found"
}
```

---

## DELETE /api/tasks/{id}

Delete a task (must belong to authenticated user).

### Request

```http
DELETE /api/tasks/1
Authorization: Bearer <token>
```

### Success Response (204 No Content)

No response body.

### Error Responses

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

**404 Not Found - Task Doesn't Exist or Not Owned**
```json
{
  "success": false,
  "error": "Task not found"
}
```

---

## PATCH /api/tasks/{id}/complete

Toggle task completion (must belong to authenticated user).

### Request

```http
PATCH /api/tasks/1/complete
Authorization: Bearer <token>
```

### Success Response (200 OK)

```json
{
  "success": true,
  "data": {
    "id": 1,
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": true,
    "created_at": "2025-12-28T10:00:00Z",
    "updated_at": "2025-12-28T11:00:00Z"
  }
}
```

### Error Responses

**401 Unauthorized - Invalid Token**
```json
{
  "success": false,
  "error": "Invalid or expired token"
}
```

**404 Not Found - Task Doesn't Exist or Not Owned**
```json
{
  "success": false,
  "error": "Task not found"
}
```

---

**Version**: 1.0  
**Last Updated**: 2025-12-28