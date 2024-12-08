def convert_temperature(value, unit):
    # Check if the input unit is Celsius
    if unit.lower() == 'c':
        return (value * 9 / 5) + 32, "Fahrenheit"
    # Check if the input unit is Fahrenheit
    elif unit.lower() == 'f':
        return (value - 32) * 5 / 9, "Celsius"
    else:
        return None, "Invalid unit"

# User inputs temperature and unit
temp_value = float(input("Enter temperature value: "))
temp_unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

converted_temp, converted_unit = convert_temperature(temp_value, temp_unit)
if converted_temp is not None:
    print(f"Converted temperature: {converted_temp:.2f} {converted_unit}")
else:
    print("Invalid unit. Please enter C or F.")
