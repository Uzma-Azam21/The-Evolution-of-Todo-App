# Research: API Ownership & User Isolation

**Feature**: `003-api-access-rules`  
**Created**: 2025-12-28

---

## Why User Isolation Matters

### Security
- Prevents users from accessing other users' private data
- Protects against data breaches
- Ensures compliance with privacy regulations

### User Experience
- Users expect their data to be private
- Builds trust in the application
- Prevents accidental data exposure

---

## Implementation Approaches

### 1. Row-Level Security (RLS) in PostgreSQL

**Pros:**
- Database-level enforcement
- Cannot be bypassed by application code
- Automatic filtering

**Cons:**
- More complex setup
- Requires PostgreSQL-specific knowledge
- Harder to debug

**Decision**: Not used - application-level filtering is sufficient and more flexible.

---

### 2. Application-Level Filtering (Chosen)

**Pros:**
- Simple to implement
- Easy to understand and debug
- Works with any database
- More control over error messages

**Cons:**
- Must be implemented consistently
- Risk of forgetting to add filter

**Mitigation**: Use FastAPI dependencies to enforce filtering automatically.

---

## FastAPI Dependency Pattern

```python
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user
```

---

## Query Filtering Pattern

```python
@app.get("/api/tasks")
async def list_tasks(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Always filter by current user
    tasks = session.exec(
        select(Task).where(Task.user_id == current_user.id)
    ).all()
    return tasks
```

---

## Ownership Verification Pattern

```python
@app.get("/api/tasks/{task_id}")
async def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Find task AND verify ownership in one query
    task = session.exec(
        select(Task)
        .where(Task.id == task_id)
        .where(Task.user_id == current_user.id)
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task
```

---

## Common Mistakes to Avoid

1. **Forgetting to add user filter**: Always include `WHERE user_id = ?`
2. **Separate existence and ownership checks**: Combine into one query
3. **Leaking information**: Return 404 (not 403) when task doesn't exist or belongs to another user
4. **Trusting client input**: Never use `user_id` from request body, always from token

---

## References

1. [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
2. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
3. [PostgreSQL Row-Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)

---

**Research Status**: Complete  
**Implementation Approach**: Application-level filtering with FastAPI dependencies