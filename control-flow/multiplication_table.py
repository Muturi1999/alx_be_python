#!/usr/bin/env python3

# multiplication_table.py

def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for i in range(1, 11):
            print(f"{number} * {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()


