#!/usr/bin/env python3

# daily_reminder.py

def main():
    try:
        # Prompt the user for task details
        task = input("Enter your task: ").strip()
        priority = input("Priority (high/medium/low): ").strip().lower()
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

        # Validate priority input
        if priority not in ("high", "medium", "low"):
            print("Invalid priority level. Please choose from high, medium, or low.")
            return

        # Match case for priority level
        match priority:
            case "high":
                reminder = f"'{task}' is a high priority task."
            case "medium":
                reminder = f"'{task}' is a medium priority task."
            case "low":
                reminder = f"'{task}' is a low priority task."

        # Adjust reminder based on time sensitivity
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        elif time_bound == "no":
            reminder += " Consider completing it when you have free time."
        else:
            print("Invalid input for time-bound status. Please answer with yes or no.")
            return

        # Print the final reminder
        print(f"Reminder: {reminder}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()


