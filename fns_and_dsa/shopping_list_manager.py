#!/usr/bin/env python3

def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Initialize the shopping list as an array (Python list).

    while True:
        # Call the display_menu function.
        display_menu()

        # Get the user's choice and validate it's a number.
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
            continue

        if choice == 1:
            # Add an item to the shopping list.
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == 2:
            # Remove an item from the shopping list.
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        elif choice == 3:
            # Display the current shopping list.
            print("Current Shopping List:")
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            # Exit the program.
            print("Goodbye!")
            break
        else:
            # Handle invalid menu options.
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

