# Implementation Checklist: API Ownership & User Isolation

**Feature**: 003-api-access-rules 
**Created**: 2025-12-28  

---

## Database Layer

- [ ] Task model has user_id field
- [ ] user_id is not nullable
- [ ] Foreign key constraint to users table
- [ ] Index on user_id field
- [ ] Database migration created and applied

## Backend Layer

- [ ] get_current_user dependency created
- [ ] Dependency extracts token from Authorization header
- [ ] Dependency verifies JWT signature
- [ ] Dependency returns user_id
- [ ] GET /api/tasks filters by user_id
- [ ] POST /api/tasks sets user_id from token
- [ ] GET /api/tasks/{id} verifies ownership
- [ ] PUT /api/tasks/{id} verifies ownership
- [ ] DELETE /api/tasks/{id} verifies ownership
- [ ] PATCH /api/tasks/{id}/complete verifies ownership
- [ ] All endpoints return 401 for missing/invalid token
- [ ] All endpoints return 404 for non-existent tasks

## Frontend Layer

- [ ] API client includes Authorization header
- [ ] Token is retrieved from storage
- [ ] 401 errors redirect to login
- [ ] Error messages are displayed to user

## Testing

- [ ] Test: User A cannot see User B's tasks
- [ ] Test: User A cannot update User B's tasks
- [ ] Test: User A cannot delete User B's tasks
- [ ] Test: Unauthenticated requests return 401
- [ ] Test: Invalid token returns 401
- [ ] Test: Expired token returns 401
- [ ] Test: User can CRUD their own tasks

## Security

- [ ] No endpoint allows access without authentication
- [ ] user_id never comes from request body
- [ ] Ownership check is atomic (single query)
- [ ] Error messages don't leak information
