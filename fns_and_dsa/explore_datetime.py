#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculates and displays the future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date and time
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

def main():
    """Main function to execute the datetime exploration tasks."""
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()

