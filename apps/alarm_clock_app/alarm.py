import time
import datetime
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
from playsound import playsound


def show_calendar():
    top = Toplevel(root)
    cal = Calendar(top, selectmode="day")
    cal.pack()

    # Get the main window's position and size
    main_window_x = root.winfo_x()
    main_window_y = root.winfo_y()
    main_window_width = root.winfo_width()
    main_window_height = root.winfo_height()

    # Calculate the calendar window position
    calendar_width = top.winfo_reqwidth()
    calendar_height = top.winfo_reqheight()
    x_position = main_window_x + (main_window_width // 2) - (calendar_width // 2)
    y_position = main_window_y + (main_window_height // 2) - (calendar_height // 2)

    # Set the calendar window position
    top.geometry(f"+{x_position}+{y_position}")

    def get_date():
        global selectedDate, emptyDate
        selectedDate = cal.selection_get()
        # Hide the "Select date" button
        selectDateButton.pack_forget()
        # Destroy the calendar window
        top.destroy()
        return selectedDate

    # Create the OK button
    button = Button(top, text="OK", command=get_date)
    button.pack()


# Create the GUI window
root = tk.Tk()
# Set the window size
root.geometry("500x500")
# Set the window title
root.title("Alarm Clock Application")
# Create the menubar
menubar = Menu(root)
# Create the file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
# Create the edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Add Alarm", command="addAlarm")
editmenu.add_command(label="Delete Alarm", command="delAlarm")
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

# Create a label
var = StringVar()
label = Label(root, textvariable=var, font=("Arial", 16))
var.set("Please select a date and time for the alarm")
label.pack(pady="10")

# Create the calendar button
selectDateButton = Button(
    root,
    text="Select date",
    font=("Arial", 10),
    command=show_calendar,
    height="2",
    width="10",
)
selectDateButton.pack()


def main():
    # Run the GUI
    root.mainloop()
    # Ensure valid format, get alarm time and selected alarm tone from user
    invalid = True
    while invalid is True:
        print(
            "\nThe alarm format must be '00:00 AM/PM'\nWhat time would you like to set the alarm for?"
        )
        userInput = input("\nLet's set the alarm for: ")

        if userInput[-2:].upper() in ["AM", "PM"]:
            1
        time_parts = userInput[:-2].strip().split(":")
        if len(time_parts) == 2:
            try:
                hours, minutes = int(time_parts[0]), int(time_parts[1])
                if 0 <= hours <= 12 and 0 <= minutes < 60:
                    if userInput[-2:].upper() == "PM":
                        if hours != 12:
                            hours += 12
                    elif hours == 12:
                        hours = 0
                    invalid = False
                else:
                    print("Invalid time format. Please try again.")
                    invalid = True
            except ValueError:
                print("Invalid time format. Please try again.")
                invalid = True
        else:
            print("Invalid time format. Please try again.")
            invalid = True

    alarmTone = None
    while alarmTone is None:
        print(
            "\nPlease select an alarm tone:\n Classic Alarm', 'Dream Memory', 'Morning Joy' or 'Warning'"
        )
        selectedTone = input("\nThe alarm tone will be: ").lower()

        if selectedTone == "classic alarm":
            alarmTone = "alarm_sounds\clock-alarm-8761.mp3"
        elif selectedTone == "dream memory":
            alarmTone = "alarm_sounds\dream-memory-alarm-clock-109567.mp3"
        elif selectedTone == "morning joy":
            alarmTone = "alarm_sounds\morning-joy-alarm-clock-20961.mp3"
        elif selectedTone == "warning":
            alarmTone = "alarm_sounds\severe-warning-alarm-98704.mp3"
        else:
            print("Please select a valid alarm tone.")
            alarmTone = None

    # Calculate the total number of seconds until the alarm should sound
    alarmTime = [hours, minutes]
    seconds_hms = [3600, 60, 1]
    alarmSeconds = sum(
        [a * b for a, b in zip(seconds_hms[: len(alarmTime)], alarmTime)]
    )

    # Get the current time in seconds
    now = datetime.datetime.now()
    currentTimeInSeconds = sum(
        [a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])]
    )

    # This is the total amount of seconds until the alarm should
    secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

    # If the set alarm time has already passed, set the alarm time for tomorrow
    if secondsUntilAlarm < 0:
        secondsUntilAlarm += 86400

    print("\nAlarm has been set!")

    # Countdown timer
    while secondsUntilAlarm > 0:
        hours, remainder = divmod(secondsUntilAlarm, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        print(f"\rThe alarm will sound in: {countdown}", end="")
        time.sleep(1)
        secondsUntilAlarm -= 1

    # Sound the alarm
    print("\nYour alarm is going off!")
    playsound(alarmTone)


# Run the program
if __name__ == "__main__":
    main()
