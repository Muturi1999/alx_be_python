#!/usr/bin/env python3

# pattern_drawing.py

def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))

        # Ensure the size is a positive integer
        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize a counter for the while loop
        row = 0

        # Use a while loop to iterate through each row
        while row < size:
            # Use a for loop to print each row of asterisks
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()

