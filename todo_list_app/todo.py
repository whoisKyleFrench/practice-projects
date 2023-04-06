import tkinter as tk

tasks = {} # Initialize dictionary
task_id = 1 # Intialize task_id

# Function to add a task
def add_task() :
    global task_id
    task_description = task_text_box.get() # Get the user input
    tasks[task_id] = f"{task_description}\n" # Add the task to the dictionary
    task_id += 1
    update_task_list() # Update the task list display

# Function to update the task list display
def update_task_list() :
    task_list_display.delete(1.0, tk.END) # Clear the task list

    # Iterate over the tasks and add them to the list display
    for task_id, task_description in tasks.items() :
        task_text = f"{task_id}. {task_description}"
        task_list_display.insert(tk.END, task_text)

# Create the GUI
root = tk.Tk()
# Give the app a title
root.title = "My To-Do List"
# Set the window size
root.geometry("300x350")