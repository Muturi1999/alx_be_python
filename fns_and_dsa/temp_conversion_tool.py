#!/usr/bin/python3

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function to handle user interaction and temperature conversion"""
    try:
        # Get temperature input from user
        temp = input("Enter the temperature to convert: ")
        
        # Validate temperature input
        try:
            temp = float(temp)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        # Get temperature unit from user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        # Validate unit input and perform conversion
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
