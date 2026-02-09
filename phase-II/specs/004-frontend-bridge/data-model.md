# Data Model: Frontend Integration

**Feature**: 004-frontend-bridge
**Created**: 2025-12-28  

---

## TypeScript Interfaces

### Task

```typescript
interface Task {
  id: number;
  user_id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;  // ISO 8601 format
  updated_at: string;  // ISO 8601 format
}
```

### User

```typescript
interface User {
  id: string;
  email: string;
  name?: string;
  created_at: string;
}
```

### TaskCreate (Request)

```typescript
interface TaskCreate {
  title: string;
  description?: string;
}
```

### TaskUpdate (Request)

```typescript
interface TaskUpdate {
  title: string;
  description?: string;
}
```

### API Response

```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}
```

### Auth State

```typescript
interface AuthState {
  isAuthenticated: boolean;
  user: User | null;
  token: string | null;
  isLoading: boolean;
}
```

### Tasks State

```typescript
interface TasksState {
  tasks: Task[];
  isLoading: boolean;
  error: string | null;
}
```

---

## Component Props

### TaskItem Props

```typescript
interface TaskItemProps {
  task: Task;
  onToggle: (id: number) => void;
  onEdit: (task: Task) => void;
  onDelete: (id: number) => void;
}
```

### TaskList Props

```typescript
interface TaskListProps {
  tasks: Task[];
  isLoading: boolean;
  error: string | null;
  onToggle: (id: number) => void;
  onEdit: (task: Task) => void;
  onDelete: (id: number) => void;
}
```

### TaskForm Props

```typescript
interface TaskFormProps {
  task?: Task;  // Optional for create mode
  onSubmit: (data: TaskCreate) => void;
  onCancel: () => void;
  isLoading: boolean;
}
```

### ErrorMessage Props

```typescript
interface ErrorMessageProps {
  message: string;
  onRetry?: () => void;
}
```

---

## Form Validation

### Create/Update Task

| Field | Rules |
|-------|-------|
| title | Required, min 1 char, max 200 chars |
| description | Optional, max 1000 chars |

### Signin

| Field | Rules |
|-------|-------|
| email | Required, valid email format |
| password | Required, min 8 chars |

### Signup

| Field | Rules |
|-------|-------|
| email | Required, valid email format |
| password | Required, min 8 chars |
| name | Optional, max 100 chars |

---

## State Management

### Auth Context

```typescript
interface AuthContextType {
  isAuthenticated: boolean;
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, name?: string) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
}
```

### Tasks Context

```typescript
interface TasksContextType {
  tasks: Task[];
  fetchTasks: () => Promise<void>;
  createTask: (data: TaskCreate) => Promise<void>;
  updateTask: (id: number, data: TaskUpdate) => Promise<void>;
  deleteTask: (id: number) => Promise<void>;
  toggleComplete: (id: number) => Promise<void>;
  isLoading: boolean;
  error: string | null;
}
```
