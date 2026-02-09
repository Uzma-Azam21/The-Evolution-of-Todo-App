# Data Model: API Ownership & User Isolation

**Feature**: 003-api-access-rules 
**Created**: 2025-12-28  

---

## Updated Task Entity

The Task entity now includes a `user_id` field to establish ownership.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | integer | Primary Key, Auto-increment | Unique identifier for the task |
| user_id | string | Foreign Key → users.id, Not Null | Owner of the task |
| title | string | Not Null, Max 200 chars | Task title |
| description | string | Nullable, Max 1000 chars | Task description |
| completed | boolean | Default false | Completion status |
| created_at | datetime | Not Null | Creation timestamp |
| updated_at | datetime | Not Null | Last update timestamp |

**Indexes**:
- `user_id` (index for fast filtering)
- `user_id + completed` (composite index for filtering by status)

**Relationships**:
- Many-to-One with User (each task belongs to one user)

---

## SQLModel Definition

```python
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List

class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(
        foreign_key="users.id",
        nullable=False,
        index=True
    )
    title: str = Field(nullable=False, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship
    user: Optional["User"] = Relationship(back_populates="tasks")
```

---

## Updated User Entity

```python
class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship
    tasks: List["Task"] = Relationship(back_populates="user")
```

---

## Database Schema (PostgreSQL)

```sql
-- Users table (from 002-auth-security)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table (updated with user_id)
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_user_completed ON tasks(user_id, completed);
CREATE INDEX idx_tasks_created_at ON tasks(created_at);
```

---

## Query Patterns

### Get All Tasks for User
```python
# With user isolation
session.exec(select(Task).where(Task.user_id == current_user_id))
```

### Get Single Task (with ownership check)
```python
# Verify ownership
session.exec(
    select(Task)
    .where(Task.id == task_id)
    .where(Task.user_id == current_user_id)
)
```

### Create Task (with automatic ownership)
```python
# Set user_id from token
new_task = Task(
    user_id=current_user_id,
    title=task_data.title,
    description=task_data.description
)
```

---

## Security Notes

1. **Always filter by user_id**: Every task query must include `WHERE user_id = ?`
2. **Verify before update/delete**: Check ownership before modifying any task
3. **Cascade delete**: When a user is deleted, all their tasks are also deleted
4. **No null user_id**: All tasks must have an owner
