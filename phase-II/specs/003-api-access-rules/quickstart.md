# Quickstart: API Ownership & User Isolation

**Feature**: `003-api-access-rules`  
**Created**: 2025-12-28

---

## Backend Setup

### 1. Update Task Model

```python
# backend/models/task.py
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional

class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id", nullable=False, index=True)
    title: str = Field(nullable=False, max_length=200)
    description: Optional[str] = None
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

---

### 2. Create Get Current User Dependency

```python
# backend/core/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import os

security = HTTPBearer()
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    return user_id
```

---

### 3. Update Task Routes

```python
# backend/routes/tasks.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..core.dependencies import get_current_user
from ..core.database import get_session
from ..models.task import Task
from ..schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/api", tags=["tasks"])

@router.get("/tasks", response_model=list[TaskResponse])
async def list_tasks(
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """List all tasks for the current user."""
    tasks = session.exec(
        select(Task).where(Task.user_id == current_user_id)
    ).all()
    return tasks

@router.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskCreate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Create a new task for the current user."""
    db_task = Task(
        user_id=current_user_id,
        title=task.title,
        description=task.description
    )
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get a specific task (must belong to current user)."""
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.user_id == current_user_id)
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update a task (must belong to current user)."""
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.user_id == current_user_id)
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = task_update.title
    task.description = task_update.description
    task.updated_at = datetime.utcnow()
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/tasks/{task_id}", status_code=204)
async def delete_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Delete a task (must belong to current user)."""
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.user_id == current_user_id)
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    return None

@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
async def toggle_complete(
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Toggle task completion (must belong to current user)."""
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.user_id == current_user_id)
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
```

---

## Frontend Setup

### Update API Client

```typescript
// frontend/lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL;

function getToken(): string | null {
  return localStorage.getItem('token');
}

async function fetchWithAuth(url: string, options: RequestInit = {}) {
  const token = getToken();
  
  const response = await fetch(`${API_URL}${url}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
      ...options.headers,
    },
  });
  
  if (response.status === 401) {
    // Redirect to login
    window.location.href = '/signin';
    return;
  }
  
  return response;
}

export const api = {
  getTasks: () => fetchWithAuth('/tasks'),
  createTask: (data: any) => fetchWithAuth('/tasks', {
    method: 'POST',
    body: JSON.stringify(data),
  }),
  updateTask: (id: number, data: any) => fetchWithAuth(`/tasks/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  }),
  deleteTask: (id: number) => fetchWithAuth(`/tasks/${id}`, {
    method: 'DELETE',
  }),
  toggleComplete: (id: number) => fetchWithAuth(`/tasks/${id}/complete`, {
    method: 'PATCH',
  }),
};
```

---

## Testing

### Test User Isolation

```bash
# Create task as User A
curl -X POST http://localhost:8000/api/tasks \
  -H "Authorization: Bearer <user_a_token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"User A Task"}'

# Try to access as User B (should fail)
curl -X GET http://localhost:8000/api/tasks \
  -H "Authorization: Bearer <user_b_token>"
# Should not see User A's task
```

---

## Common Issues

### Issue: 401 Unauthorized on all requests
**Solution**: Check that token is being sent correctly in Authorization header.

### Issue: Can see other users' tasks
**Solution**: Verify `user_id` filter is added to all task queries.

### Issue: Can update other users' tasks
**Solution**: Ensure ownership check is performed before update.

---

**Status**: Implementation ready  
**Dependencies**: Better Auth, FastAPI, SQLModel