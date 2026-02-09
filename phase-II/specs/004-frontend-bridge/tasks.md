# Tasks: Frontend Integration

**Feature**: 004-frontend-bridge 
**Created**: 2025-12-28  

---

## Task 1: Initialize Next.js Project

**Description**: Set up Next.js 16+ project with TypeScript and Tailwind

**Acceptance Criteria**:
- Next.js project created
- TypeScript configured
- Tailwind CSS configured
- Project structure follows plan

**Files to Modify**:
- `frontend/` (entire project)

**Estimated Time**: 20 minutes

---

## Task 2: Create TypeScript Types

**Description**: Define TypeScript interfaces for all data models

**Acceptance Criteria**:
- Task interface defined
- User interface defined
- API response types defined
- All types exported

**Files to Modify**:
- `frontend/types/index.ts`

**Estimated Time**: 15 minutes

---

## Task 3: Create API Client

**Description**: Build HTTP client with authentication

**Acceptance Criteria**:
- Fetch wrapper with auth header
- All task endpoints implemented
- Error handling implemented
- 401 redirects to login

**Files to Modify**:
- `frontend/lib/api.ts`

**Estimated Time**: 30 minutes

---

## Task 4: Create Auth Utilities

**Description**: Build authentication helper functions

**Acceptance Criteria**:
- Token storage functions
- Token retrieval functions
- Token removal (logout)
- Auth state check

**Files to Modify**:
- `frontend/lib/auth.ts`

**Estimated Time**: 20 minutes

---

## Task 5: Create useAuth Hook

**Description**: Build custom hook for authentication

**Acceptance Criteria**:
- Returns current auth state
- Provides login function
- Provides logout function
- Handles token storage

**Files to Modify**:
- `frontend/hooks/useAuth.ts`

**Estimated Time**: 25 minutes

---

## Task 6: Create useTasks Hook

**Description**: Build custom hook for task management

**Acceptance Criteria**:
- Fetches tasks on mount
- Provides CRUD functions
- Manages loading state
- Manages error state

**Files to Modify**:
- `frontend/hooks/useTasks.ts`

**Estimated Time**: 35 minutes

---

## Task 7: Create LoadingSpinner Component

**Description**: Build reusable loading indicator

**Acceptance Criteria**:
- Shows animated spinner
- Centered by default
- Customizable size

**Files to Modify**:
- `frontend/components/LoadingSpinner.tsx`

**Estimated Time**: 10 minutes

---

## Task 8: Create ErrorMessage Component

**Description**: Build error display component

**Acceptance Criteria**:
- Shows error message
- Styled as error
- Optional retry button

**Files to Modify**:
- `frontend/components/ErrorMessage.tsx`

**Estimated Time**: 10 minutes

---

## Task 9: Create EmptyState Component

**Description**: Build empty state message

**Acceptance Criteria**:
- Shows friendly message
- Has icon
- Encourages action

**Files to Modify**:
- `frontend/components/EmptyState.tsx`

**Estimated Time**: 10 minutes

---

## Task 10: Create TaskItem Component

**Description**: Build individual task card

**Acceptance Criteria**:
- Shows title and description
- Has completion checkbox
- Has edit and delete buttons
- Styled for completed state
- Responsive layout

**Files to Modify**:
- `frontend/components/TaskItem.tsx`

**Estimated Time**: 30 minutes

---

## Task 11: Create TaskList Component

**Description**: Build task list container

**Acceptance Criteria**:
- Maps through tasks
- Renders TaskItem for each
- Shows loading state
- Shows empty state
- Shows error state

**Files to Modify**:
- `frontend/components/TaskList.tsx`

**Estimated Time**: 25 minutes

---

## Task 12: Create TaskForm Component

**Description**: Build create/edit task form

**Acceptance Criteria**:
- Title input (required)
- Description textarea (optional)
- Submit button
- Validation feedback
- Works for create and edit

**Files to Modify**:
- `frontend/components/TaskForm.tsx`

**Estimated Time**: 30 minutes

---

## Task 13: Create AddTaskButton Component

**Description**: Build floating add task button

**Acceptance Criteria**:
- Floating action button
- Opens TaskForm modal
- Styled prominently

**Files to Modify**:
- `frontend/components/AddTaskButton.tsx`

**Estimated Time**: 15 minutes

---

## Task 14: Create EditTaskModal Component

**Description**: Build modal for editing tasks

**Acceptance Criteria**:
- Modal overlay
- Contains TaskForm
- Pre-filled with task data
- Close on outside click

**Files to Modify**:
- `frontend/components/EditTaskModal.tsx`

**Estimated Time**: 20 minutes

---

## Task 15: Create DeleteConfirmation Component

**Description**: Build delete confirmation dialog

**Acceptance Criteria**:
- Modal overlay
- Warning message
- Confirm and cancel buttons
- Shows task title

**Files to Modify**:
- `frontend/components/DeleteConfirmation.tsx`

**Estimated Time**: 15 minutes

---

## Task 16: Create ProtectedRoute Component

**Description**: Build auth guard component

**Acceptance Criteria**:
- Checks for valid token
- Redirects to login if not authenticated
- Shows loading while checking
- Renders children if authenticated

**Files to Modify**:
- `frontend/components/ProtectedRoute.tsx`

**Estimated Time**: 20 minutes

---

## Task 17: Create Signin Page

**Description**: Build signin page

**Acceptance Criteria**:
- Email and password inputs
- Submit button
- Error messages
- Link to signup
- Redirects on success

**Files to Modify**:
- `frontend/app/signin/page.tsx`

**Estimated Time**: 30 minutes

---

## Task 18: Create Signup Page

**Description**: Build signup page

**Acceptance Criteria**:
- Email, password, name inputs
- Submit button
- Validation errors
- Link to signin
- Redirects on success

**Files to Modify**:
- `frontend/app/signup/page.tsx`

**Estimated Time**: 30 minutes

---

## Task 19: Create Dashboard Page

**Description**: Build main dashboard page

**Acceptance Criteria**:
- Shows TaskList
- Shows AddTaskButton
- Protected by auth
- Responsive layout
- Header with logout

**Files to Modify**:
- `frontend/app/page.tsx`

**Estimated Time**: 25 minutes

---

## Task 20: Create Root Layout

**Description**: Build root layout with providers

**Acceptance Criteria**:
- HTML structure
- Global styles
- Metadata
- Font configuration

**Files to Modify**:
- `frontend/app/layout.tsx`

**Estimated Time**: 15 minutes

---

## Task 21: Configure Environment Variables

**Description**: Set up environment variables

**Acceptance Criteria**:
- .env.example created
- API URL configured
- Auth secret configured
- Variables documented

**Files to Modify**:
- `frontend/.env.example`

**Estimated Time**: 10 minutes

---

## Task 22: Add Global Styles

**Description**: Add Tailwind custom styles

**Acceptance Criteria**:
- Custom colors defined
- Custom spacing defined
- Responsive utilities
- Animation utilities

**Files to Modify**:
- `frontend/app/globals.css`
- `frontend/tailwind.config.ts`

**Estimated Time**: 15 minutes

---

## Total Estimated Time: 8 hours 30 minutes
