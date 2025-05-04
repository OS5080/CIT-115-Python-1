# Compound Interest with Loops Code
# By: Owen Smith
# Date: 4/25/25

# Import necessary module for currency formatting
import locale

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, '')

# Function to get valid float input from user
def get_valid_float_input(prompt, allow_zero=False):
    while True:
        try:
            str_input = input(prompt)
            flt_value = float(str_input)
            if not allow_zero and flt_value <= 0:
                print("Input must a positive numeric value.")
            elif allow_zero and flt_value < 0:
                print("Input must 0 or greater")
            else:
                return flt_value
        except ValueError:
            print("Input must a positive numeric value.")

# Prompt User inputs with validation
fltDeposit = get_valid_float_input("What is the Original Deposit (positive value): ")
fltInterestRatePercent = get_valid_float_input("What is the Interest Rate (positive value): ")
intNumMonths = int(get_valid_float_input("What is the Number of Months (positive value): "))
fltGoal = get_valid_float_input("What is the Goal Amount (can enter 0 but not negative)): ", allow_zero=True)

# Convert users interest rate from percent to monthly decimal rate
fltMonthlyInterestRate = (fltInterestRatePercent / 100) / 12

# Calculate compounded balance over the specified number of months
fltBalance = fltDeposit
for intMonth in range(1, intNumMonths + 1):
    fltInterest = fltBalance * fltMonthlyInterestRate
    fltBalance += fltInterest
    print(f"Month:  {intMonth}  Account Balance is: {locale.currency(fltBalance, grouping=True)}")

# Predict how many months it will take user to reach the goal
fltBalance = fltDeposit  # Reset balance
intMonthsToGoal = 0

# Only calculate if the goal is greater than current deposit
if fltGoal > fltDeposit:
    while fltBalance < fltGoal:
        fltInterest = fltBalance * fltMonthlyInterestRate
        fltBalance += fltInterest
        intMonthsToGoal += 1
    print(f"It will take:  {intMonthsToGoal:,}  months to reach the goal of {locale.currency(fltGoal, grouping=True)}")
else:
    print("\nYour goal is already met with the current deposit amount.")
