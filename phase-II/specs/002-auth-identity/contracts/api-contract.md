# API Contracts: Authentication & Security

**Feature**: 002-auth-identity  
**Created**: 2025-12-28  

---

## POST /auth/signup

Register a new user account.

### Request

```http
POST /auth/signup
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}
```

### Request Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Valid email address |
| password | string | Yes | Min 8 characters |
| name | string | No | User's display name |

### Success Response (201 Created)

```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2025-12-28T10:00:00Z"
  }
}
```

### Error Responses

**400 Bad Request - Invalid Input**
```json
{
  "success": false,
  "error": "Invalid email format"
}
```

**400 Bad Request - Weak Password**
```json
{
  "success": false,
  "error": "Password must be at least 8 characters"
}
```

**409 Conflict - Email Exists**
```json
{
  "success": false,
  "error": "Email already registered"
}
```

---

## POST /auth/signin

Login with existing credentials.

### Request

```http
POST /auth/signin
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

### Request Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Registered email address |
| password | string | Yes | User's password |

### Success Response (200 OK)

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

### Error Responses

**401 Unauthorized - Invalid Credentials**
```json
{
  "success": false,
  "error": "Invalid email or password"
}
```

---

## POST /auth/logout

Logout the current user.

### Request

```http
POST /auth/logout
Authorization: Bearer <token>
```

### Success Response (200 OK)

```json
{
  "success": true,
  "message": "Logout successful"
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

---

## GET /auth/me

Get current user information.

### Request

```http
GET /auth/me
Authorization: Bearer <token>
```

### Success Response (200 OK)

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2025-12-28T10:00:00Z"
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
