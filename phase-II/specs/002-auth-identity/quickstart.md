# Quickstart: Authentication & Security

**Feature**: 002-auth-identity
**Created**: 2025-12-28  

---

## Backend Setup

### 1. Install Dependencies

```bash
cd backend
pip install pyjwt passlib[bcrypt] python-jose[cryptography]
```

### 2. Set Environment Variables

```bash
# .env
JWT_SECRET=your-super-secret-jwt-key-here
JWT_EXPIRATION_DAYS=7
BETTER_AUTH_SECRET=your-better-auth-secret
```

### 3. Create User Model

```python
# backend/models/user.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

### 4. Create Password Utilities

```python
# backend/core/security.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### 5. Create JWT Utilities

```python
# backend/core/jwt.py
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
import os

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
```

---

## Frontend Setup

### 1. Install Better Auth

```bash
cd frontend
npm install better-auth
```

### 2. Configure Better Auth

```typescript
// frontend/lib/auth.ts
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  secret: process.env.NEXT_PUBLIC_BETTER_AUTH_SECRET,
});
```

### 3. Create Auth Provider

```typescript
// frontend/components/AuthProvider.tsx
import { auth } from "@/lib/auth";

export function AuthProvider({ children }) {
  return <auth.Provider>{children}</auth.Provider>;
}
```

---

## Testing Authentication

### Signup Test

```bash
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"SecurePass123!","name":"Test User"}'
```

### Signin Test

```bash
curl -X POST http://localhost:8000/auth/signin \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"SecurePass123!"}'
```

---

## Common Issues

### Issue: JWT token not working
**Solution**: Check that JWT_SECRET is set and matches between frontend and backend.

### Issue: CORS errors
**Solution**: Ensure CORS is properly configured in FastAPI with frontend URL.

### Issue: Password not hashing
**Solution**: Verify passlib is installed and bcrypt is available.
