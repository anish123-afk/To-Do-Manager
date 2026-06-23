import tkinter
from tkinter import *
from tkinter import font
import json
from tkinter import messagebox
from tkinter import ttk
import os

### creating a window 
root = Tk()

root.title("To-Do List")
root.geometry("1000x700")
root.configure(bg="#1e1e1e") 


### creating variables

task_var = tkinter.StringVar()
tasks = []



### Functions
# def get_clr(priority):
#     if priority == 'HIGH':
#           return "🔴"
#     elif priority == 'MEDIUM':
#          return "🟡"
#     else:
#          return "🟢"

def add_task():
    task_var = ent_entry.get()
    priority_var = priority_combobox.get()
    if task_var == "":
        return
    # clr = get_clr(priority_var)
    # task_var = clr + " " + task_var
    print_task_var = task_var + " [" + priority_var + "]"
    tasks.append([task_var, priority_var, False])
    pending_list.insert(END, print_task_var)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    ent_entry.delete(0, END)
    # add_frame(task_var)
    print(tasks)

def del_task():
    selected_index_pending = pending_list.curselection()
    selected_index_completed = completed_list.curselection()
    
    if selected_index_pending or selected_index_completed:
        if selected_index_pending:
            index = selected_index_pending[0]
            task = pending_list.get(index)
            
            task_test_test = task.split(" ")[0:-1]
            task_test = " ".join(task_test_test)

            i = 0
            for task_row in tasks:
                task_name = task_row[0]
                if task_name == task_test:
                    break
                else:
                    i += 1
            
            tasks.pop(i)
            pending_list.delete(index)

            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=4)
        else:
            index = selected_index_completed[0]
            task = completed_list.get(index)

            task_test_test = task.split(" ")[0:-1]
            task_test = " ".join(task_test_test)

            i = 0
            for task_row in tasks:
                task_name = task_row[0]
                if task_name == task_test:
                    break
                else:
                    i += 1
            
            tasks.pop(i)
            completed_list.delete(index)

            with open("tasks.json", "w") as f:
                    json.dump(tasks, f, indent=4)

    else:
         messagebox.showerror("Error", "Please select a task first!")

    print(tasks)
    

def complete_task():
    selected_index_pending = pending_list.curselection()
    selected_index_completed = completed_list.curselection()

    if selected_index_pending or selected_index_completed:
        if selected_index_pending:
            index = selected_index_pending[0]
            task = pending_list.get(index)

            task_test_test = task.split(" ")[0:-1]
            task_test = " ".join(task_test_test)

            i = 0
            for task_row in tasks:
                task_name = task_row[0]
                if task_name == task_test:
                    break
                else:
                    i += 1
            
            tasks[i][0] = f"✔️ {task_test}"
            tasks[i][2] = True
            pending_list.delete(index)
            completed_list.insert(END, f"✔️ {task}")

            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=4)
        else:
            messagebox.showerror("Error", "This task is already completed!")

    else:
        messagebox.showerror("Error", "Please select a task first!")

        

    print(tasks)


def startup_task_load():
    global tasks
    with open("tasks.json", "r") as f:
          tasks = json.load(f)
    
    for task in tasks:
         print_task_var = task[0] + " [" + task[1] + "]"
         if task[2] == False:
            pending_list.insert(END, print_task_var)
         else:
             completed_list.insert(END, print_task_var)
        

    print(tasks)

# def add_frame(task):
#     task_frame = Frame(root, bg="#2d2d2d")
#     # task_frame.pack(fill="x", pady=5)

#     task_label = Label(
#         task_frame,
#         text=task,
#         bg="#2d2d2d",
#         fg="white",
#         font=("Segoe UI", 11)
#     )
#     task_label.pack(side="left", padx=10)

#     Button(task_frame, text="✓").pack(side="right")
#     Button(task_frame, text="Edit").pack(side="right")
#     Button(task_frame, text="Delete").pack(side="right")



### To-Do Manager heading
 
heading_label = Label(
    root,
    text="TO-DO MANAGER",
    font=("Segoe UI", 24, "bold"),
    fg="#00d4ff",      
    bg="#1e1e1e",      
    pady=20
)
 
heading_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")
 
### Enter a task label 
 
ent_label = Label(
    root,
    text="Add a New Task",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#1e1e1e"
)
 
ent_label.grid(row=1, column=0, columnspan=3, pady=(10, 5))
 
### Enter a task entry 
 
ent_entry = Entry(
    root,
    textvariable = task_var,
    font=("Segoe UI", 12),
    width=35,
    bg="#2d2d2d",     
    fg="white",       
    insertbackground="white", 
    relief="flat"
)
 
ent_entry.grid(
    row=2,
    column=0,
    padx=(20, 10),
    pady=10,
    ipady=8,
    sticky="e"
)
 
 
### Add Button
 
add_button = Button(
    root,
    text="Add Task",
    command=add_task,
    font=("Segoe UI", 11, "bold"),
    bg="#00d4ff",     
    fg="black",
    activebackground="#00b8e6",
    activeforeground="black",
    relief="flat",
    padx=15,
    pady=6,
    cursor="hand2"
)
 
add_button.grid(
    row=2,
    column=2,
    padx=(5, 20),
    pady=10,
    sticky="w"
)
 
 
### tasks list
 
# task_list = Listbox(
#     root,
#     height=10,
#     width=50,
#     font=("Segoe UI Symbol", 12),
#     bg="#2d2d2d",          
#     fg="white",
#     selectbackground="#00d4ff",
#     selectforeground="black",
#     relief="flat",
#     bd=0,
#     highlightthickness=0
# )
 
# task_list.grid(
#     row=3,
#     column=0,
#     columnspan=2,
#     padx=20,
#     pady=20,
#     sticky="nsew"
# )
 
 
# Complete Button
 
complete_button = Button(
    root,
    text="✅ Complete",
    command=complete_task,
    font=("Segoe UI", 10, "bold"),
    bg="#22c55e",
    fg="white",
    activebackground="#16a34a",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=6,
    cursor="hand2"
)
 
complete_button.grid(
    row=5,
    column=0,
    padx=(20, 10),
    pady=(0, 10),
    sticky="ew"
)
 
# Delete Button
 
del_button = Button(
    root,
    text="🗑️ Delete",
    command=del_task,
    font=("Segoe UI", 10, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=6,
    cursor="hand2"
)
 
del_button.grid(
    row=5,
    column=2,
    padx=(10, 20),
    pady=(0, 10),
    sticky="ew"
)
 
### priority system
 
style = ttk.Style()
style.theme_use("clam")
 
style.configure(
    "Custom.TCombobox",
    fieldbackground="#2d2d2d",
    background="#00d4ff",
    foreground="white",
    bordercolor="#00d4ff",
    arrowcolor="#00d4ff",
    padding=5
)
 
priority_combobox = ttk.Combobox(
    root,
    values=["HIGH", "MEDIUM", "LOW"],
    state="readonly",
    width=10,
    font=("Segoe UI", 11),
    style="Custom.TCombobox"
)
 
priority_combobox.set("Priority")
 
priority_combobox.grid(
    row=2,
    column=1,
    padx=5,
    pady=10,
    ipady=4,
    sticky="ew"
)
 
# Pending Label
 
pending_label = Label(
    root,
    text="Pending Tasks",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#1e1e1e"
)
 
pending_label.grid(row=3, column=0, pady=(5, 2))
 
# Completed Label
 
completed_label = Label(
    root,
    text="Completed Tasks",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#1e1e1e"
)
 
completed_label.grid(row=3, column=2, pady=(5, 2))
 
### Pending Listbox
 
pending_list = Listbox(
    root,
    height=15,
    width=35,
    font=("Segoe UI", 12),
    bg="#2d2d2d",
    fg="white",
    selectbackground="#00d4ff",
    selectforeground="black"
)
 
pending_list.grid(
    row=4,
    column=0,
    padx=(20, 5),
    pady=(2, 0),
    sticky="ew"
)
 
### Completed Listbox
 
completed_list = Listbox(
    root,
    height=15,
    width=35,
    font=("Segoe UI", 12),
    bg="#2d2d2d",
    fg="#22c55e",
    selectbackground="#00d4ff",
    selectforeground="black"
)
 
completed_list.grid(
    row=4,
    column=2,
    padx=(5, 20),
    pady=(2, 0),
    sticky="ew"
)



if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as f:
        json.dump([], f)
startup_task_load()

root.mainloop()