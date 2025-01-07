#!/usr/bin/env python3

# Define the global conversion factors at the top
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    # Using the global variable FAHRENHEIT_TO_CELSIUS_FACTOR for the conversion
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    # Using the global variable CELSIUS_TO_FAHRENHEIT_FACTOR for the conversion
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function for interacting with the user and performing temperature conversion.
    """
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt user to specify the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Handle conversion based on user input
        if unit == "C":
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # Handle invalid input for unit
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Catch non-numeric input for temperature
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

