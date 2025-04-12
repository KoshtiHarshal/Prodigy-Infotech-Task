def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    print("Temperature Converter")
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit of the temperature (Celsius, Fahrenheit, Kelvin): ").strip().lower()
    
    if unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is equal to {fahrenheit}°F and {kelvin}K.")
    
    elif unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equal to {celsius}°C and {kelvin}K.")
    
    elif unit == "kelvin":
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is equal to {celsius}°C and {fahrenheit}°F.")
    
    else:
        print("Invalid unit. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")

# Call the temperature_converter function to run the program
temperature_converter()