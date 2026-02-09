# Quickstart: Frontend Integration

**Feature**: 004-frontend-bridge
**Created**: 2025-12-28  

---

## Project Setup

### 1. Initialize Next.js Project

```bash
cd frontend
npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
```

### 2. Install Dependencies

```bash
npm install lucide-react
npm install -D @types/node
```

### 3. Set Environment Variables

```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_SECRET=your-secret-here
```

---

## Project Structure

```
frontend/
├── app/
│   ├── page.tsx
│   ├── layout.tsx
│   ├── globals.css
│   ├── signin/
│   │   └── page.tsx
│   └── signup/
│       └── page.tsx
├── components/
│   ├── TaskList.tsx
│   ├── TaskItem.tsx
│   ├── TaskForm.tsx
│   ├── AddTaskButton.tsx
│   ├── EditTaskModal.tsx
│   ├── DeleteConfirmation.tsx
│   ├── LoadingSpinner.tsx
│   ├── ErrorMessage.tsx
│   ├── EmptyState.tsx
│   └── ProtectedRoute.tsx
├── hooks/
│   ├── useAuth.ts
│   └── useTasks.ts
├── lib/
│   ├── api.ts
│   └── auth.ts
└── types/
    └── index.ts
```

---

## Key Components

### API Client

```typescript
// lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL;

function getToken() {
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
    window.location.href = '/signin';
    return;
  }
  
  return response.json();
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

### useTasks Hook

```typescript
// hooks/useTasks.ts
import { useState, useEffect, useCallback } from 'react';
import { api } from '@/lib/api';
import { Task } from '@/types';

export function useTasks() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await api.getTasks();
      setTasks(response.data || []);
      setError(null);
    } catch (err) {
      setError('Failed to fetch tasks');
    } finally {
      setIsLoading(false);
    }
  }, []);

  const createTask = async (data: { title: string; description?: string }) => {
    try {
      const response = await api.createTask(data);
      setTasks((prev) => [...prev, response.data]);
      return response.data;
    } catch (err) {
      throw new Error('Failed to create task');
    }
  };

  const updateTask = async (id: number, data: { title: string; description?: string }) => {
    try {
      const response = await api.updateTask(id, data);
      setTasks((prev) =>
        prev.map((task) => (task.id === id ? response.data : task))
      );
      return response.data;
    } catch (err) {
      throw new Error('Failed to update task');
    }
  };

  const deleteTask = async (id: number) => {
    try {
      await api.deleteTask(id);
      setTasks((prev) => prev.filter((task) => task.id !== id));
    } catch (err) {
      throw new Error('Failed to delete task');
    }
  };

  const toggleComplete = async (id: number) => {
    try {
      const response = await api.toggleComplete(id);
      setTasks((prev) =>
        prev.map((task) => (task.id === id ? response.data : task))
      );
      return response.data;
    } catch (err) {
      throw new Error('Failed to toggle task');
    }
  };

  useEffect(() => {
    fetchTasks();
  }, [fetchTasks]);

  return {
    tasks,
    isLoading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    deleteTask,
    toggleComplete,
  };
}
```

---

## Running the Frontend

```bash
# Development
npm run dev

# Build
npm run build

# Production
npm start
```

---

## Common Issues

### Issue: CORS errors
**Solution**: Ensure backend CORS is configured to allow frontend URL.

### Issue: 401 errors
**Solution**: Check that token is being stored and sent correctly.

### Issue: Build fails
**Solution**: Check for TypeScript errors and missing dependencies.
