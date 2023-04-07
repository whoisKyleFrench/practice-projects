import tkinter as tk

tasks = {} # Initialize dictionary
task_id = 1 # Intialize task_id

# Function to add a task
def add_task():
    global task_id # Make task_id a global variable
    task_description = "  " + task_text_box.get() # Get the user input
    tasks[task_id] = task_description # Add the task to the dictionary
    task_id += 1
    update_task_list() # Update the task list display
    task_text_box.delete(0, tk.END) # Delete the text in task_text_box

def complete_task() :
    # Get the index of the selected line
    index = task_list_display.curselection()

    if index:
        # Get the task_description from the index of the selected line
        task_description = task_list_display.get(index[0])

        # Find the task in the dictionary by its description
        task_id_to_complete = None
        for task_id, description in tasks.items():
            if description == task_description:
                task_id_to_complete = task_id
                break

        if task_id_to_complete is not None:
            # Add " (Complete)" to the task"
            tasks[task_id_to_complete] += " (Complete)"
            # Update the task list display
            update_task_list()


def delete_task():
    # Get the index of the selected line
    index = task_list_display.curselection()

    if index:
        # Get the task_description from the index of the selected line
        task_description = task_list_display.get(index[0])

        # Find the task in the dictionary by its description
        task_id_to_remove = None
        for task_id, description in tasks.items():
            if description == task_description:
                task_id_to_remove = task_id
                break

        if task_id_to_remove is not None:
            # Remove the task from the dictionary
            del tasks[task_id_to_remove]
            # Update the task list display
            update_task_list()



# Function to update the task list display
def update_task_list() :
    task_list_display.delete(0, tk.END) # Clear the task list
    # Iterate over the tasks and add them to the list display
    for task_id, task_description in tasks.items() :
        task_text = task_description
        task_list_display.insert(tk.END, task_text)

# Create the GUI
root = tk.Tk()
# Give the app a title
root.title("To-Do List App")
# Set the window size
root.geometry("400x425")
# Set the background color
bg_color = "#46485d"
root.configure(bg=bg_color)
# Set the foreground color
fg_color = "#FFFFFF"

# Create a label for the task list
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18))
title_label.pack(pady=5)
title_label.configure(bg=bg_color, fg=fg_color)

# Create the task list display
task_list_display = tk.Listbox(root, width=40, height=10, takefocus=0, font=("Arial", 14,))
task_list_display.pack(padx=5, pady=10)

# Create label for text entry field
entry_label = tk.Label(root, fg=fg_color, text="Please Enter Tasks Below", font=("Arial", 10))
entry_label.pack()
entry_label.configure(bg=bg_color)

# Create the text box for entering task descriptions
task_text_box = tk.Entry(root, width=26)
task_text_box.pack(pady=10)

# Create a button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
# Set button Frame background color
button_frame.configure(bg=bg_color)

# Create the button for adding tasks
add_task_button = tk.Button(button_frame, text="Add", command=lambda: add_task())
add_task_button.grid(row=0, column=0, pady=10)

# Create the button for completing tasks
complete_task_button = tk.Button(button_frame, text="Complete", command=lambda: complete_task())
complete_task_button.grid(row=0, column=1, padx=10, pady=10)

# Create the delete button for deleting tasks
delete_task_button = tk.Button(button_frame, text="Delete", command=lambda: delete_task())
delete_task_button.grid(row=0, column=2, pady=10)

# Start the main event loop
root.mainloop()