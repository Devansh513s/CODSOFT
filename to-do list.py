import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        
        pass

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  
        save_tasks()  
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()
        listbox.delete(task_index)
        save_tasks()  
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_all():
    listbox.delete(0, tk.END)
    save_tasks()  

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(fill="both", pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_button.pack(fill="both", pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 14), command=clear_all)
clear_button.pack(fill="both", pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=10, fill="both", expand=True)

load_tasks()

root.mainloop()
