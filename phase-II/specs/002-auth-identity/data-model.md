# Data Model: Authentication & Security

**Feature**: 002-auth-identity
**Created**: 2025-12-28  

---

## Entities

### User

The User entity represents a registered user of the Todo application.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | string | Primary Key, UUID | Unique identifier for the user |
| email | string | Unique, Indexed, Not Null | User's email address |
| password_hash | string | Not Null | Bcrypt hashed password |
| name | string | Nullable | User's display name |
| created_at | datetime | Not Null | Account creation timestamp |
| updated_at | datetime | Not Null | Last update timestamp |

**Indexes**:
- `email` (unique index for fast lookup)

**Relationships**:
- One-to-Many with Task (a user can have many tasks)

---

## SQLModel Definition

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        primary_key=True,
        index=True
    )
    email: str = Field(
        unique=True,
        index=True,
        nullable=False
    )
    password_hash: str = Field(nullable=False)
    name: Optional[str] = Field(default=None)
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
```

---

## Database Schema (PostgreSQL)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

---

## JWT Token Structure

### Payload

```json
{
  "sub": "user-uuid-here",
  "email": "user@example.com",
  "iat": 1703779200,
  "exp": 1704384000
}
```

| Claim | Description |
|-------|-------------|
| sub | Subject (user ID) |
| email | User's email |
| iat | Issued at timestamp |
| exp | Expiration timestamp |

---

## Security Notes

1. **Password Storage**: Never store plain text passwords. Always use bcrypt hashing.
2. **JWT Secret**: Store in environment variable, never commit to git.
3. **Token Expiration**: Set to 7 days for this application.
4. **HTTPS**: Always use HTTPS in production to protect tokens in transit.
