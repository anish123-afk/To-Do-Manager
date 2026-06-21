import tkinter
from tkinter import *
from tkinter import font

### creating a window 
root = Tk()

root.title("To-Do List")
root.geometry("1000x700")
root.configure(bg="#1e1e1e") 


### creating variables

task_var = tkinter.StringVar()
tasks = []
task_index = 1


### Functions

def add_task():
    task_var = ent_entry.get()
    if task_var == "":
        return
    tasks.append(task_var)
    task_list.insert(task_index, task_var)
    ent_entry.delete(0, END)
    # add_frame(task_var)
    print(tasks)

def del_task():
    selected_index = task_list.curselection()
    index = selected_index[0]
    task = task_list.get(index)

    i = 0
    for task_name in tasks:
        if task_name == task:
            break
        else:
            i += 1
    
    tasks.pop(i)
    task_list.delete(index)

    print(tasks)
    

def complete_task():
    selected_index = task_list.curselection()
    index = selected_index[0]
    task = task_list.get(index)

    i = 0
    for task_name in tasks:
        if task_name == task:
            break
        else:
            i += 1
    
    tasks[i] = f"✓ {task}"
    task_list.delete(index)
    task_list.insert(index, f"✓ {task}")

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

heading_label.grid(row=0, column=0, pady=20)

### Enter a task label 

ent_label = Label(
    root,
    text="Add a New Task",
    font=("Segoe UI", 12, "bold"),
    fg="#ffffff",
    bg="#1e1e1e"
)

ent_label.grid(row=1, column=0, pady=(10, 5))

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
    sticky="w"
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
    column=1,
    padx=(0, 20),
    pady=10
)


### tasks list

task_list = Listbox(
    root,
    height=10,
    width=50,
    font=("Segoe UI", 12),
    bg="#2d2d2d",          
    fg="white",
    selectbackground="#00d4ff",
    selectforeground="black",
    relief="flat",
    bd=0,
    highlightthickness=0
)

task_list.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=20,
    pady=20,
    sticky="nsew"
)


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
    row=4,
    column=0,
    columnspan=1,
    padx=(20, 10),
    pady=10,
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
    row=4,
    column=1,
    columnspan=1,
    padx=(10, 20),
    pady=10,
    sticky="ew"
)

root.mainloop()