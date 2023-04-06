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