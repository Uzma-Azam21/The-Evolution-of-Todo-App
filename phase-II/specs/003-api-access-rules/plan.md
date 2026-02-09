# Implementation Plan: API Ownership & User Isolation

**Feature**: 003-api-access-rules 
**Created**: 2025-12-28  
**Status**: Draft  

---

## Overview

This plan outlines how to implement user-specific task ownership in the Todo application. Each user will only be able to access, modify, and delete their own tasks.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│   Next.js       │────▶│   FastAPI       │────▶│   JWT           │
│   Frontend      │     │   Backend       │     │   Middleware    │
│                 │     │                 │     │                 │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │   Task Routes   │
                        │   (Protected)   │
                        └────────┬────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
              ┌─────────┐  ┌─────────┐  ┌─────────┐
              │  List   │  │ Create  │  │ Update  │
              │  Tasks  │  │  Task   │  │  Task   │
              └────┬────┘  └────┬────┘  └────┬────┘
                   │            │            │
                   └────────────┼────────────┘
                                ▼
                        ┌─────────────────┐
                        │   Neon DB       │
                        │   (Filtered by  │
                        │    user_id)     │
                        └─────────────────┘
```

## Implementation Strategy

### 1. Update Task Model

Add `user_id` field to the Task model as a foreign key to the users table.

### 2. Create JWT Dependency

Create a FastAPI dependency that:
- Extracts JWT from Authorization header
- Verifies the token
- Returns the user_id

### 3. Update All Task Endpoints

Modify each endpoint to:
- Use the JWT dependency
- Filter queries by user_id
- Verify ownership before update/delete

### 4. Update Frontend API Client

Modify the frontend to:
- Include JWT token in all API requests
- Handle 401/403 errors appropriately

## Endpoint Changes

| Endpoint | Change |
|----------|--------|
| GET /api/tasks | Add JWT check, filter by user_id |
| POST /api/tasks | Add JWT check, set user_id from token |
| GET /api/tasks/{id} | Add JWT check, verify ownership |
| PUT /api/tasks/{id} | Add JWT check, verify ownership |
| DELETE /api/tasks/{id} | Add JWT check, verify ownership |
| PATCH /api/tasks/{id}/complete | Add JWT check, verify ownership |

## Security Flow

1. **Request**: Frontend sends request with `Authorization: Bearer <token>` header
2. **Verify**: Backend middleware verifies JWT and extracts user_id
3. **Filter**: All database queries include `WHERE user_id = <extracted_id>`
4. **Check**: For single resource operations, verify resource belongs to user
5. **Response**: Return data or appropriate error (401/403)

## Error Handling

| Scenario | Status Code | Message |
|----------|-------------|---------|
| No token provided | 401 | "Authentication required" |
| Invalid token | 401 | "Invalid or expired token" |
| User not found | 401 | "User not found" |
| Access other user's task | 403 | "Access denied" |
| Task not found | 404 | "Task not found" |
