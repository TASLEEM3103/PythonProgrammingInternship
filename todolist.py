import tkinter as tk
from tkinter import messagebox

# Function to add a task to the to-do list
def add_task():
    description = entry_description.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()

    if description:
        task_list.insert(tk.END, f"{description} (Due: {due_date}, Priority: {priority})")
        entry_description.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task description cannot be empty!")

# Function to mark a task as completed
def mark_completed():
    selected_task = task_list.curselection()
    if selected_task:
        completed_list.insert(tk.END, task_list.get(selected_task))
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Select a task to mark as completed!")

# Function to remove a task from the to-do list
def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Select a task to remove!")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Set background and foreground colors for the main window
root.configure(bg="lightblue")  # Background color

# Create input fields and labels
entry_bg_color = "white"  # Background color for input fields

label_description = tk.Label(root, text="Description:", bg="lightblue", fg="black")
entry_description = tk.Entry(root, bg=entry_bg_color)
label_due_date = tk.Label(root, text="Due Date:", bg="lightblue", fg="black")
entry_due_date = tk.Entry(root, bg=entry_bg_color)
label_priority = tk.Label(root, text="Priority:", bg="lightblue", fg="black")
entry_priority = tk.Entry(root, bg=entry_bg_color)

# Create buttons
button_bg_color = "white"  # Background color for buttons

add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_bg_color, fg="black")
mark_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg=button_bg_color, fg="black")
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg=button_bg_color, fg="black")

# Create task and completed task lists
list_bg_color = "white"  # Background color for lists

task_list = tk.Listbox(root, bg=list_bg_color)
completed_list = tk.Listbox(root, bg=list_bg_color)

# Create labels for the "To-Do List" and "Marked Completed" sections
label_fg_color = "black"  # Foreground (text) color for labels

todo_heading = tk.Label(root, text="To-Do List", bg="lightblue", fg=label_fg_color)
completed_heading = tk.Label(root, text="Marked Completed", bg="lightblue", fg=label_fg_color)

# Place widgets on the grid
label_description.grid(row=0, column=0)
entry_description.grid(row=0, column=1)
label_due_date.grid(row=1, column=0)
entry_due_date.grid(row=1, column=1)
label_priority.grid(row=2, column=0)
entry_priority.grid(row=2, column=1)
add_button.grid(row=3, column=0, columnspan=2)
mark_button.grid(row=4, column=0, columnspan=2)
remove_button.grid(row=5, column=0, columnspan=2)
todo_heading.grid(row=0, column=2, padx=10)
task_list.grid(row=1, column=2, rowspan=6, padx=10)
completed_heading.grid(row=0, column=3, padx=10)
completed_list.grid(row=1, column=3, rowspan=6, padx=10)

root.mainloop()
