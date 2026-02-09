# Component Contracts: Frontend Integration

**Feature**: 004-frontend-bridge  
**Created**: 2025-12-28  

---

## TaskItem Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| task | Task | Yes | Task data to display |
| onToggle | (id: number) => void | Yes | Callback when checkbox clicked |
| onEdit | (task: Task) => void | Yes | Callback when edit clicked |
| onDelete | (id: number) => void | Yes | Callback when delete clicked |

### Render States

**Default State**:
- Shows title (bold)
- Shows description (gray, smaller)
- Shows unchecked checkbox
- Shows edit and delete buttons

**Completed State**:
- Title has strikethrough
- Description has strikethrough
- Checkbox is checked
- Background slightly muted

### User Interactions

- Click checkbox → Calls onToggle
- Click edit button → Calls onEdit
- Click delete button → Calls onDelete

---

## TaskList Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| tasks | Task[] | Yes | Array of tasks |
| isLoading | boolean | Yes | Loading state |
| error | string \| null | Yes | Error message |
| onToggle | (id: number) => void | Yes | Toggle callback |
| onEdit | (task: Task) => void | Yes | Edit callback |
| onDelete | (id: number) => void | Yes | Delete callback |

### Render States

**Loading State**:
- Shows LoadingSpinner
- No task items rendered

**Error State**:
- Shows ErrorMessage
- Shows retry button if onRetry provided

**Empty State**:
- Shows EmptyState component
- Encourages user to add tasks

**Data State**:
- Maps through tasks
- Renders TaskItem for each

---

## TaskForm Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| task | Task | No | Task to edit (undefined for create) |
| onSubmit | (data: TaskCreate) => void | Yes | Submit callback |
| onCancel | () => void | Yes | Cancel callback |
| isLoading | boolean | Yes | Loading state |

### Render States

**Create Mode** (no task prop):
- Empty title input
- Empty description textarea
- "Create Task" button

**Edit Mode** (task prop provided):
- Pre-filled title input
- Pre-filled description textarea
- "Update Task" button

### Validation

- Title: Required, max 200 chars
- Description: Optional, max 1000 chars

### User Interactions

- Type in inputs → Updates form state
- Click submit → Validates, calls onSubmit
- Click cancel → Calls onCancel

---

## AddTaskButton Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| onClick | () => void | Yes | Click callback |

### Render

- Floating action button
- Plus icon
- Positioned bottom-right
- Primary color (blue)

---

## EditTaskModal Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| task | Task | Yes | Task to edit |
| isOpen | boolean | Yes | Modal visibility |
| onClose | () => void | Yes | Close callback |
| onSubmit | (data: TaskCreate) => void | Yes | Submit callback |
| isLoading | boolean | Yes | Loading state |

### Render

- Modal overlay (darkened background)
- Centered modal card
- Contains TaskForm
- Close on outside click

---

## DeleteConfirmation Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| taskTitle | string | Yes | Title of task to delete |
| isOpen | boolean | Yes | Modal visibility |
| onConfirm | () => void | Yes | Confirm callback |
| onCancel | () => void | Yes | Cancel callback |
| isLoading | boolean | Yes | Loading state |

### Render

- Modal overlay
- Warning message with task title
- "Delete" button (red)
- "Cancel" button (gray)

---

## LoadingSpinner Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| size | 'sm' \| 'md' \| 'lg' | No | Spinner size (default: 'md') |

### Render

- Animated spinner
- Centered by default
- Size based on prop

---

## ErrorMessage Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| message | string | Yes | Error message |
| onRetry | () => void | No | Retry callback |

### Render

- Error icon
- Error message (red)
- Optional retry button

---

## EmptyState Component

### Props

| Prop | Type | Required | Description |
|------|------|----------|-------------|
| title | string | No | Title text |
| message | string | No | Message text |

### Render

- Icon (clipboard or checkmark)
- Title (default: "No tasks yet")
- Message (default: "Add your first task to get started")
