# Compound Interest Code
# By: Owen Smith Sr.
# Week 2

# User's input

Principal_Investment = float(input("Enter the starting principal: "))  # Principal amount (PV)
Annual_Interest_Rate = float(input("Enter the annual interest rate: "))  # Interest rate as a percentage (R)
Compounding = float(input("How many times per year is the interest compounded? "))  # Number of periods in years or fractions (t)
Number_Of_Periods = int(input("For how many years will the account earn interest? "))  # Number of times interest is compounded per period (m)

# Convert interest rate to decimal

Stated_Rate = Annual_Interest_Rate / 100

# Calculate future value using compound interest formula (FV)

Future_Value = Principal_Investment * (1 + Stated_Rate / Compounding) ** (Compounding * Number_Of_Periods)

# Print formatted output with dollar sign, comma, and two decimal places (FV) Calculated

print("At the end of 2 years you will have $ {:,.2f}".format(Future_Value))