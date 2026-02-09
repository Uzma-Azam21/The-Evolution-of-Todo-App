# Implementation Plan: Frontend Integration

**Feature**: 004-frontend-bridge 
**Created**: 2025-12-28  
**Status**: Draft  

---

## Overview

This plan outlines the implementation of a modern React frontend for the Todo application using Next.js 16+.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Next.js Frontend                      │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Pages     │  │ Components  │  │    API      │     │
│  │             │  │             │  │   Client    │     │
│  │ - Dashboard │  │ - TaskList  │  │             │     │
│  │ - Signin    │  │ - TaskItem  │  │ - Auth      │     │
│  │ - Signup    │  │ - TaskForm  │  │ - Tasks     │     │
│  │             │  │ - Loading   │  │             │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│         │                 │                 │            │
│         └─────────────────┼─────────────────┘            │
│                           │                              │
│                           ▼                              │
│                  ┌─────────────┐                         │
│                  │   Hooks     │                         │
│                  │  - useAuth  │                         │
│                  │  - useTasks │                         │
│                  └─────────────┘                         │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   FastAPI       │
                    │   Backend       │
                    └─────────────────┘
```

## Tech Stack

- **Framework**: Next.js 16+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **HTTP Client**: Fetch API
- **Auth**: Better Auth Client
- **Icons**: Lucide React

## Project Structure

```
frontend/
├── app/
│   ├── page.tsx              # Dashboard (root)
│   ├── layout.tsx            # Root layout
│   ├── signin/
│   │   └── page.tsx          # Signin page
│   ├── signup/
│   │   └── page.tsx          # Signup page
│   └── globals.css           # Global styles
├── components/
│   ├── TaskList.tsx          # Task list component
│   ├── TaskItem.tsx          # Individual task
│   ├── TaskForm.tsx          # Create/edit form
│   ├── AddTaskButton.tsx     # Add task button
│   ├── EditTaskModal.tsx     # Edit modal
│   ├── DeleteConfirmation.tsx # Delete dialog
│   ├── LoadingSpinner.tsx    # Loading indicator
│   ├── ErrorMessage.tsx      # Error display
│   ├── EmptyState.tsx        # Empty state
│   └── ProtectedRoute.tsx    # Auth guard
├── hooks/
│   ├── useAuth.ts            # Auth hook
│   └── useTasks.ts           # Tasks hook
├── lib/
│   ├── api.ts                # API client
│   └── auth.ts               # Auth utilities
└── types/
    └── index.ts              # TypeScript types
```

## Component Design

### TaskList
- Displays all tasks
- Handles loading and error states
- Maps through tasks and renders TaskItem

### TaskItem
- Displays task title and description
- Shows completion checkbox
- Has edit and delete buttons
- Styled differently for completed tasks

### TaskForm
- Input for title (required)
- Textarea for description (optional)
- Submit button
- Validation feedback

### AddTaskButton
- Floating action button
- Opens TaskForm modal

## State Management

### Local State (useState)
- Form inputs
- Modal open/close
- Loading states

### Custom Hooks
- `useAuth`: Manage authentication state
- `useTasks`: Fetch and manage tasks

## API Integration

```typescript
// lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const api = {
  getTasks: () => fetchWithAuth('/tasks'),
  createTask: (data) => fetchWithAuth('/tasks', { method: 'POST', body: JSON.stringify(data) }),
  updateTask: (id, data) => fetchWithAuth(`/tasks/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  deleteTask: (id) => fetchWithAuth(`/tasks/${id}`, { method: 'DELETE' }),
  toggleComplete: (id) => fetchWithAuth(`/tasks/${id}/complete`, { method: 'PATCH' }),
};
```

## Responsive Design

### Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

### Mobile Layout
- Full-width cards
- Stacked buttons
- Bottom sheet for forms

### Desktop Layout
- Centered container (max-width: 800px)
- Side-by-side buttons
- Modal for forms

## Error Handling

- Network errors: Show retry button
- 401 errors: Redirect to login
- 404 errors: Show "not found" message
- Validation errors: Show inline messages

## Loading States

- Initial load: Full page spinner
- CRUD operations: Button loading state
- List refresh: Skeleton cards
