#!/usr/bin/env python3

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    # Use the global factor to convert from Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    # Use the global factor to convert from Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to interact with the user and perform the temperature conversion.
    """
    try:
        # Ask the user to input a temperature value
        temperature = float(input("Enter the temperature to convert: "))

        # Ask the user to specify if the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Conversion logic based on the unit input
        if unit == "C":
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # If the unit is neither C nor F, print an error message
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        # Handle non-numeric input for the temperature
        print("Invalid temperature. Please enter a numeric value.")

# Ensure the script is run as a standalone program
if __name__ == "__main__":
    main()

