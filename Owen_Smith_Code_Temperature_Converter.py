# Code Temperature Converter Project
# By: Owen Smith
# Date: 4/8/2025


# My personal Welcome message
print("Owen Smith's Temp Converter: ")
print()  # Blank line
print()  # Blank line

# User input for temperature
fTemp = float(input("Enter temperature: "))

# User input temperature type
sTEMPSCALE = input("Is the temp F Fahrenheit or C for Celsius? ")

# Conversion strip() removes spaces from string & lower() converts all characters to lowercase
sTEMPSCALE = sTEMPSCALE.strip().lower()

# Validate User input: must be 'f' or 'c' (exit() prints message and exits
if sTEMPSCALE not in {"f", "c"}:
    exit("You must enter a F or C")

# Convert Fahrenheit to Celsius
if sTEMPSCALE == 'f':
    if fTemp > 212:
        print("Temp can not be > 212")
    else:
        fCelsius = (5.0 / 9) * (fTemp - 32)
        print("The Celsius equivalent is:", round(fCelsius, 1))

# Convert Celsius to Fahrenheit
elif sTEMPSCALE == 'c':
    if fTemp > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheit = (9.0 / 5.0) * fTemp + 32
        print("The Fahrenheit equivalent is:", round(fFahrenheit, 1))
