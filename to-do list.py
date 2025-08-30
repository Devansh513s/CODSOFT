import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        # If the file doesn't exist, no tasks to load
        pass

# Function to save tasks to the file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  # Clear the input field
        save_tasks()  # Save the updated task list
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        task_index = listbox.curselection()
        listbox.delete(task_index)
        save_tasks()  # Save the updated task list
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_all():
    listbox.delete(0, tk.END)
    save_tasks()  # Save the empty task list

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("700x400")
root.resizable(False, False)

# Create input field for adding tasks
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Create buttons for add, delete, and clear actions
add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(fill="both", pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_button.pack(fill="both", pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 14), command=clear_all)
clear_button.pack(fill="both", pady=5)

# Create a listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 14), height=10, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=10, fill="both", expand=True)

# Load tasks from the file when the app starts
load_tasks()

# Run the application
root.mainloop()
