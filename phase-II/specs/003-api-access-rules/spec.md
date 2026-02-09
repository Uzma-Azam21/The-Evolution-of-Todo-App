# Feature Specification: API Ownership & User Isolation

**Feature Branch**: `003-api-access-rules`  
**Created**: 2025-12-28  
**Status**: Draft  

**Input**: User description: "Implement user-specific task ownership where each user can only access and manage their own tasks. All task endpoints must verify JWT tokens and filter data by the authenticated user. Users should not be able to view, modify, or delete other users' tasks."

---

## User Scenarios & Testing (mandatory)

### User Story 1 - Create Personal Task (Priority: P1)

**As an authenticated user, I want to create tasks that are only visible to me.**

**Why this priority**: User isolation is fundamental for a multi-user todo application - users expect their data to be private.

**Independent Test**: Create a task as User A, verify User B cannot see it.

**Acceptance Scenarios**:
- **Given** I am logged in as User A,  
  **When** I create a new task,  
  **Then** the task should be associated with my user ID

- **Given** User A has created a task,  
  **When** User B requests all tasks,  
  **Then** User B should not see User A's task

### User Story 2 - View Only My Tasks (Priority: P1)

**As an authenticated user, I want to see only my own tasks.**

**Why this priority**: Users should never see other users' private task data.

**Independent Test**: Create tasks for multiple users, verify each only sees their own.

**Acceptance Scenarios**:
- **Given** I am logged in,  
  **When** I request my task list,  
  **Then** I should only see tasks belonging to me

- **Given** I have no tasks,  
  **When** I request my task list,  
  **Then** I should receive an empty list

### User Story 3 - Update Only My Tasks (Priority: P1)

**As an authenticated user, I should only be able to update my own tasks.**

**Why this priority**: Prevent unauthorized modifications to other users' data.

**Independent Test**: Try to update another user's task, verify access is denied.

**Acceptance Scenarios**:
- **Given** I am logged in,  
  **When** I update my own task,  
  **Then** the task should be updated successfully

- **Given** I am logged in,  
  **When** I try to update another user's task,  
  **Then** I should receive a 403 Forbidden error

### User Story 4 - Delete Only My Tasks (Priority: P1)

**As an authenticated user, I should only be able to delete my own tasks.**

**Why this priority**: Prevent unauthorized deletion of other users' data.

**Independent Test**: Try to delete another user's task, verify access is denied.

**Acceptance Scenarios**:
- **Given** I am logged in,  
  **When** I delete my own task,  
  **Then** the task should be deleted successfully

- **Given** I am logged in,  
  **When** I try to delete another user's task,  
  **Then** I should receive a 403 Forbidden error

### User Story 5 - Access Without Authentication (Priority: P1)

**As an unauthenticated user, I should not be able to access any task endpoints.**

**Why this priority**: All task data should be protected behind authentication.

**Independent Test**: Make requests without token, verify 401 response.

**Acceptance Scenarios**:
- **Given** I am not logged in,  
  **When** I try to access task endpoints,  
  **Then** I should receive a 401 Unauthorized error

- **Given** I have an expired token,  
  **When** I try to access task endpoints,  
  **Then** I should receive a 401 Unauthorized error

---

## Edge Cases

- What happens if a user tries to access a task that doesn't exist?
- What if a user manipulates the URL to access another user's task?
- How does the system handle concurrent access to the same task?
- What if the JWT token is valid but the user no longer exists in the database?

---

## Requirements (mandatory)

### Functional Requirements

| ID | Requirement |
|----|-------------|
| FR-001 | System MUST verify JWT token on all task endpoints |
| FR-002 | System MUST extract user_id from JWT token |
| FR-003 | System MUST filter all task queries by the authenticated user's ID |
| FR-004 | System MUST reject requests to access other users' tasks with 403 |
| FR-005 | System MUST associate new tasks with the authenticated user |
| FR-006 | System MUST return 401 for requests without valid token |
| FR-007 | System MUST validate that user exists before processing requests |
| FR-008 | System MUST return appropriate error messages for unauthorized access |

### Key Entities

**Task (Updated)**:
- `id`: Unique identifier (integer, auto-increment)
- `user_id`: Foreign key to users table (string, required)
- `title`: Task title (string, required)
- `description`: Task description (string, optional)
- `completed`: Completion status (boolean, default false)
- `created_at`: Creation timestamp (datetime)
- `updated_at`: Last update timestamp (datetime)

---

## Success Criteria (mandatory)

| ID | Criteria |
|----|----------|
| SC-001 | All task endpoints require valid JWT authentication |
| SC-002 | Users can only view their own tasks |
| SC-003 | Users can only update their own tasks |
| SC-004 | Users can only delete their own tasks |
| SC-005 | New tasks are automatically associated with the authenticated user |
| SC-006 | Attempts to access other users' tasks return 403 Forbidden |
| SC-007 | Unauthenticated requests return 401 Unauthorized |

---

## Out of Scope

- Admin access to all tasks
- Task sharing between users
- Public tasks
- Task permissions/roles
