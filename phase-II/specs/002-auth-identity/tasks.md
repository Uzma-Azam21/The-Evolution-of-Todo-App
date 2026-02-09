# Tasks: Authentication & Security

**Feature**: 002-auth-identity 
**Created**: 2025-12-28  

---

## Task 1: Create User Model

**Description**: Create SQLModel User entity with all required fields

**Acceptance Criteria**:
- User model has id, email, password_hash, name, created_at, updated_at
- Email field is unique and indexed
- Password is stored as hash, never plain text

**Files to Modify**:
- `backend/models/user.py`

**Estimated Time**: 30 minutes

---

## Task 2: Implement Password Hashing

**Description**: Create utility functions for password hashing and verification

**Acceptance Criteria**:
- Password hashing uses bcrypt
- Hash function returns secure hash
- Verify function correctly validates passwords

**Files to Modify**:
- `backend/core/security.py`

**Estimated Time**: 20 minutes

---

## Task 3: Implement JWT Token Generation

**Description**: Create functions to generate and verify JWT tokens

**Acceptance Criteria**:
- Tokens contain user_id and expiration
- Tokens are signed with secret key
- Verification correctly decodes and validates tokens
- Expired tokens are rejected

**Files to Modify**:
- `backend/core/jwt.py`

**Estimated Time**: 30 minutes

---

## Task 4: Create Signup Endpoint

**Description**: Implement user registration endpoint

**Acceptance Criteria**:
- Endpoint accepts email, password, and optional name
- Validates email format
- Validates password strength (min 8 chars)
- Checks for duplicate email
- Creates user in database
- Returns success message

**Files to Modify**:
- `backend/routes/auth.py`

**Estimated Time**: 45 minutes

---

## Task 5: Create Signin Endpoint

**Description**: Implement user login endpoint

**Acceptance Criteria**:
- Endpoint accepts email and password
- Verifies credentials
- Returns JWT token on success
- Returns error on invalid credentials

**Files to Modify**:
- `backend/routes/auth.py`

**Estimated Time**: 30 minutes

---

## Task 6: Create JWT Middleware

**Description**: Implement middleware to verify JWT on protected routes

**Acceptance Criteria**:
- Extracts token from Authorization header
- Verifies token signature and expiration
- Adds user_id to request context
- Returns 401 for invalid/missing tokens

**Files to Modify**:
- `backend/core/middleware.py`
- `backend/app/main.py`

**Estimated Time**: 40 minutes

---

## Task 7: Configure Better Auth Frontend

**Description**: Set up Better Auth client in Next.js

**Acceptance Criteria**:
- Better Auth client is configured
- Points to correct backend URL
- JWT secret is configured

**Files to Modify**:
- `frontend/lib/auth.ts`
- `frontend/.env.local`

**Estimated Time**: 25 minutes

---

## Task 8: Create Signup Page

**Description**: Build signup form with validation

**Acceptance Criteria**:
- Form has email, password, confirm password fields
- Client-side validation
- Shows error messages
- Redirects on success

**Files to Modify**:
- `frontend/app/signup/page.tsx`
- `frontend/components/SignupForm.tsx`

**Estimated Time**: 45 minutes

---

## Task 9: Create Signin Page

**Description**: Build signin form

**Acceptance Criteria**:
- Form has email and password fields
- Client-side validation
- Shows error messages
- Stores JWT token on success
- Redirects to dashboard

**Files to Modify**:
- `frontend/app/signin/page.tsx`
- `frontend/components/SigninForm.tsx`

**Estimated Time**: 40 minutes

---

## Task 10: Create Protected Route Component

**Description**: Build component to protect routes that require authentication

**Acceptance Criteria**:
- Checks for valid JWT token
- Redirects to signin if not authenticated
- Shows loading state while checking

**Files to Modify**:
- `frontend/components/ProtectedRoute.tsx`

**Estimated Time**: 30 minutes

---

## Task 11: Write Authentication Tests

**Description**: Create tests for auth functionality

**Acceptance Criteria**:
- Password hashing tests pass
- JWT generation/verification tests pass
- Signup endpoint tests pass
- Signin endpoint tests pass
- Middleware tests pass

**Files to Modify**:
- `backend/tests/test_auth.py`

**Estimated Time**: 60 minutes

---

## Total Estimated Time: 7 hours 15 minutes
