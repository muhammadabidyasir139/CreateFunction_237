def convert(temperature_value, temperature_unit):
    temperature_unit = input("Enter the unit (Celcius / Fahrenheit) ")
    temperature_value = float(input("Enter the temperature unit: "))
    if temperature_unit.upper() == "CELCIUS":
        fahrenheit = (temperature_value * 9 / 5) + 32
        return fahrenheit
    elif temperature_unit.upper() == "FAHRENHEIT":
        celcius = (temperature_value - 32) * 5 / 9
        return celcius
    else:
        print("Invalid unit")

print(convert(f"temperature_value", "temperature_unit"))
