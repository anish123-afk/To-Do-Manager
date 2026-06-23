# 📝 To-Do Manager

A clean, dark-themed desktop To-Do application built with Python and Tkinter. Manage your daily tasks with priority levels, persistent storage, and a modern UI.

---

## 📸 Preview

> _A 1000×700 dark-themed window with cyan accents, split into Pending and Completed task panels._

---

## ✨ Features

- ✅ **Add Tasks** with a name and priority level (HIGH / MEDIUM / LOW)
- 🗑️ **Delete Tasks** from either Pending or Completed list
- ✔️ **Mark as Complete** — moves task from Pending to Completed instantly
- 💾 **Persistent Storage** — tasks are saved to `tasks.json` and restored on next launch
- 🎨 **Dark Theme UI** — modern dark interface with cyan (`#00d4ff`) accent color
- ⚠️ **Input Validation** — warns if task name is empty or no priority is selected

---

## 🛠️ Built With

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Tkinter | GUI framework |
| ttk.Combobox | Priority dropdown |
| JSON | Task persistence |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Tkinter (comes pre-installed with Python on Windows and macOS)

On Linux, install Tkinter with:
```bash
sudo apt-get install python3-tk
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/todo-manager.git
cd todo-manager
```

2. **Run the app**
```bash
python todo.py
```

> No external dependencies required — only the Python standard library is used.

---

## 🖥️ Usage

| Action | How |
|---|---|
| Add a task | Type in the entry box → select priority → click **Add Task** |
| Complete a task | Select a task in Pending list → click **✅ Complete** |
| Delete a task | Select any task → click **🗑️ Delete** |

> Tasks are auto-saved to `tasks.json` in the same directory after every action.

---

## 📁 Project Structure
todo-manager/

│

├── todo.py          # Main application file

├── tasks.json       # Auto-generated task storage (created on first run)

└── README.md        # Project documentation
---

## ⚠️ Known Limitations

- If two tasks have the exact same name, the first match is always affected by delete/complete
- No editing of existing tasks (planned for a future update)

---

## 🔮 Planned Features

- [ ] Edit task name and priority
- [ ] Due dates with overdue highlighting
- [ ] Sort by priority
- [ ] Task counter badges


---

> _Built with Python & Tkinter_ 🐍