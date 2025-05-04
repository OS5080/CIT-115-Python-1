# Grade Analyzer Code
# By: Owen Smith
# Date: 4/18/2025

# Step 1: Prompt user for their name
strName = input("Name of person that we are calculating the grandes for: ")

# Step 2: Prompt User for 4 test scores
intScore1 = int(input("Test 1: "))
intScore2 = int(input("Test 2: "))
intScore3 = int(input("Test 3: "))
intScore4 = int(input("Test 4: "))

# Step 4: Validate all users scores are >= 0
if intScore1 < 0 or intScore2 < 0 or intScore3 < 0 or intScore4 < 0:
    strDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ").upper()
    print("Test scores must be greater than 0.")
    raise SystemExit

# Step 3: Ask user if lowest grade should be dropped
strDropLowest = input("Do you wish to Drop the Lowest Grade Y or N? ").upper()

# Step 5: Validate Y or N input
if strDropLowest not in ['Y', 'N']:
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Step 6: Drop user lowest test score logic (no lists, no min())
# Initialize total and count
intTotal = 0
intCount = 4

# Drop user test score logic using if/elif/else and only add the highest 3 scores
if strDropLowest == 'Y':
    intCount = 3  # Since we drop one score
    # Check all combinations to find the lowest and exclude it from sum
    if intScore1 <= intScore2 and intScore1 <= intScore3 and intScore1 <= intScore4:
        intTotal = intScore2 + intScore3 + intScore4
    elif intScore2 <= intScore1 and intScore2 <= intScore3 and intScore2 <= intScore4:
        intTotal = intScore1 + intScore3 + intScore4
    elif intScore3 <= intScore1 and intScore3 <= intScore2 and intScore3 <= intScore4:
        intTotal = intScore1 + intScore2 + intScore4
    else:
        intTotal = intScore1 + intScore2 + intScore3
else:
    # No score is dropped, add all
    intTotal = intScore1 + intScore2 + intScore3 + intScore4

# Step 7: Calculate user test score average as a float
fltAverage = float(intTotal) / intCount

# Step 8: Determine users letter grade
if fltAverage >= 97.0:
    strLetterGrade = "A+"
elif fltAverage >= 94.0:
    strLetterGrade = "A"
elif fltAverage >= 90.0:
    strLetterGrade = "A-"
elif fltAverage >= 87.0:
    strLetterGrade = "B+"
elif fltAverage >= 84.0:
    strLetterGrade = "B"
elif fltAverage >= 80.0:
    strLetterGrade = "B-"
elif fltAverage >= 77.0:
    strLetterGrade = "C+"
elif fltAverage >= 74.0:
    strLetterGrade = "C"
elif fltAverage >= 70.0:
    strLetterGrade = "C-"
elif fltAverage >= 67.0:
    strLetterGrade = "D+"
elif fltAverage >= 64.0:
    strLetterGrade = "D"
elif fltAverage >= 60.0:
    strLetterGrade = "D-"
else:
    strLetterGrade = "F"

# Step 13: Output users name, average, and letter grade

print(strName + " test average is: {:.1f}".format(fltAverage))  # Step 14: Format average to 1 decimal
print("Letter Grade for the test is:", strLetterGrade)
