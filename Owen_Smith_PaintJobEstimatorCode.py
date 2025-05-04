# Paint Job Estimator Code
# By: Owen Smith
# Date: 5/2/25

import math

# Function to get a validated float input from the user
def getFloatInput(strPrompt):
    while True:
        try:
            fValue = float(input(strPrompt + ": "))
            if fValue <= 0:
                print("ERROR: Value must be greater than zero.")
            else:
                return fValue
        except ValueError:
            print("ERROR: Invalid input. Please enter a numeric value.")

# Function to get number of gallons needed (rounded up)
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

# Function to calculate total labor hours
def getLaborHours(fLaborHoursPerGallon, iTotalGallons):
    return fLaborHoursPerGallon * iTotalGallons

# Function to calculate labor cost
def getLaborCost(fTotalLaborHours, fLaborChargePerHour):
    return fTotalLaborHours * fLaborChargePerHour

# Function to calculate paint cost
def getPaintCost(iTotalGallons, fPaintPrice):
    return iTotalGallons * fPaintPrice

# Function to determine sales tax based on state
def getSalesTax(strState):
    strState = strState.upper()
    if strState == "CT":
        return 0.06
    elif strState == "MA":
        return 0.0625
    elif strState == "ME":
        return 0.085
    elif strState == "NH":
        return 0.0
    elif strState == "RI":
        return 0.07
    elif strState == "VT":
        return 0.06
    else:
        return 0.0

# Function to show and write cost estimate to file
def showCostEstimate(strLastName, fPaintCost, fLaborCost, fTaxRate, fTotalLaborHours, fLaborHoursPerGallon, iTotalGallons):
    fSubtotal = fPaintCost + fLaborCost
    fSalesTax = fSubtotal * fTaxRate
    fTotalCost = fSubtotal + fSalesTax

    strOutput = (
        f"Gallons of paint: {iTotalGallons} \n"
        f"Hours of labor: {fTotalLaborHours:.2f} \n"
        f"Paint charges: ${fPaintCost:,.2f}\n"
        f"Labor charges: ${fLaborCost:,.2f}\n"
        f"Tax: ${fSalesTax:,.2f}\n"
        f"Total cost: ${fTotalCost:,.2f}"
    )

    print(strOutput)

    strFilename = strLastName + "_PaintJobOutput.txt was created"
    with open(strFilename, "w") as fOutputFile:
        fOutputFile.write(strOutput)

    print(f"File: {strFilename}")

# Main function
def main():
    # Input prompts
    fSquareFeet = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fFeetPerGallon = getFloatInput("Enter feet per gallon")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon")
    fLaborChargePerHour = getFloatInput("Labor charge per hour")

    # Additional string inputs
    strState = input("State job is in: ").strip()
    strLastName = input("Customer Last Name: ").strip()

    # Calculations
    iTotalGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fTotalLaborHours = getLaborHours(fLaborHoursPerGallon, iTotalGallons)
    fLaborCost = getLaborCost(fTotalLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iTotalGallons, fPaintPrice)
    fTaxRate = getSalesTax(strState)

    # Output results
    showCostEstimate(strLastName, fPaintCost, fLaborCost, fTaxRate, fTotalLaborHours, fLaborHoursPerGallon, iTotalGallons)

# Run the program
if __name__ == "__main__":
    main()
