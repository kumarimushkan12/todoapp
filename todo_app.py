import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

# Function to clear all tasks
def clear_all_tasks():
    tasks_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Entry box for new tasks
task_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
task_entry.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Buttons
add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", width=12, command=clear_all_tasks)
clear_button.grid(row=0, column=2, padx=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, font=("Helvetica", 12), width=45, height=10, selectbackground="gray")
tasks_listbox.pack(pady=10)

# Run the app
root.mainloop()