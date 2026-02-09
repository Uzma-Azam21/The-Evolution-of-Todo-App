# Tasks: API Ownership & User Isolation

**Feature**: 003-api-access-rules 
**Created**: 2025-12-28  

---

## Task 1: Update Task Model with user_id

**Description**: Add user_id foreign key to Task model

**Acceptance Criteria**:
- Task model has user_id field
- user_id is required (not nullable)
- Foreign key constraint to users table
- Database migration created

**Files to Modify**:
- `backend/models/task.py`

**Estimated Time**: 20 minutes

---

## Task 2: Create Get Current User Dependency

**Description**: Create FastAPI dependency to extract user from JWT

**Acceptance Criteria**:
- Extracts token from Authorization header
- Verifies token signature and expiration
- Returns user_id from token payload
- Raises 401 for invalid/missing tokens

**Files to Modify**:
- `backend/core/dependencies.py`

**Estimated Time**: 30 minutes

---

## Task 3: Update List Tasks Endpoint

**Description**: Modify GET /api/tasks to filter by authenticated user

**Acceptance Criteria**:
- Requires authentication
- Returns only tasks belonging to current user
- Maintains existing filtering/sorting capabilities

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 20 minutes

---

## Task 4: Update Create Task Endpoint

**Description**: Modify POST /api/tasks to associate with current user

**Acceptance Criteria**:
- Requires authentication
- Sets user_id from token automatically
- Task is associated with authenticated user

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 15 minutes

---

## Task 5: Update Get Task Endpoint

**Description**: Modify GET /api/tasks/{id} to verify ownership

**Acceptance Criteria**:
- Requires authentication
- Returns 404 if task doesn't exist
- Returns 403 if task belongs to another user
- Returns task if owned by current user

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 20 minutes

---

## Task 6: Update Update Task Endpoint

**Description**: Modify PUT /api/tasks/{id} to verify ownership

**Acceptance Criteria**:
- Requires authentication
- Returns 404 if task doesn't exist
- Returns 403 if task belongs to another user
- Updates task if owned by current user

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 20 minutes

---

## Task 7: Update Delete Task Endpoint

**Description**: Modify DELETE /api/tasks/{id} to verify ownership

**Acceptance Criteria**:
- Requires authentication
- Returns 404 if task doesn't exist
- Returns 403 if task belongs to another user
- Deletes task if owned by current user

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 20 minutes

---

## Task 8: Update Toggle Complete Endpoint

**Description**: Modify PATCH /api/tasks/{id}/complete to verify ownership

**Acceptance Criteria**:
- Requires authentication
- Returns 404 if task doesn't exist
- Returns 403 if task belongs to another user
- Toggles completion if owned by current user

**Files to Modify**:
- `backend/routes/tasks.py`

**Estimated Time**: 15 minutes

---

## Task 9: Update Frontend API Client

**Description**: Modify frontend to include JWT in all requests

**Acceptance Criteria**:
- All API requests include Authorization header
- Token is retrieved from storage
- Handles 401 errors by redirecting to login

**Files to Modify**:
- `frontend/lib/api.ts`

**Estimated Time**: 25 minutes

---

## Task 10: Write Ownership Tests

**Description**: Create tests for user isolation

**Acceptance Criteria**:
- Test that users can only see their own tasks
- Test that users cannot update others' tasks
- Test that users cannot delete others' tasks
- Test that unauthenticated requests are rejected

**Files to Modify**:
- `backend/tests/test_ownership.py`

**Estimated Time**: 45 minutes

---

## Total Estimated Time: 3 hours 50 minutes
