import time
import datetime
from playsound import playsound


def main():
    # Ensure valid format, get alarm time and selected alarm tone from user
    invalid = True
    while invalid:
        print(
            "\nThe alarm format must be '00:00 AM/PM'\nWhat time would you like to set the alarm for?"
        )
        userInput = input("\nLet's set the alarm for: ")

        alarmTone = None
        print(
            "\nPlease select an alarm tone:\nAlarm Clock', 'Dream Alarm', 'Morning Joy' or 'Severe Warning'"
        )
        selectedTone = input("\nThe alarm tone will be: ").lower()

        if selectedTone == "alarm clock":
            alarmTone = "alarm_sounds\clock-alarm-8761.mp3"
        elif selectedTone == "dream alarm":
            alarmTone = "alarm_sounds\dream-memory-alarm-clock-109567.mp3"
        elif selectedTone == "morning joy":
            alarmTone = "alarm_sounds\morning-joy-alarm-clock-20961.mp3"
        elif selectedTone == "severe warning":
            alarmTone = "alarm_sounds\severe-warning-alarm-98704.mp3"
        else:
            print("Please select a valid alarm tone.")

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
            except ValueError:
                print("Invalid time format. Please try again.")
        else:
            print("Invalid time format. Please try again.")

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


# Run the program
if __name__ == "__main__":
    main()
