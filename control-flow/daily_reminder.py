# control-flow/daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case for priority handling
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unrecognized priority level"

# Modify message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
    print(message)
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
    print(message)

# Print the customized reminder


