"""
Temperature Converter: Write a function convert_temp(value, unit) that converts:
    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
Use conditionals inside the function.
"""

def convert_temp(value, unit):
    if unit.upper() == "F":
        celsius = (value - 32) * 5 / 9
        return f"{value}°F is {celsius:.2f}°C"

    elif unit.upper() == "C":
        fahrenheit = (value * 9 / 5) + 32
        return f"{value}°C is {fahrenheit:.2f}°F"

    else:
        return "Invalid Unit. Please enter 'C' or 'F'."


value = float(input("Enter temperature value to convert: "))
unit = input("Enter the unit (C or F): ").strip()

print(convert_temp(value, unit))

