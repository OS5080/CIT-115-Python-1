# List and Real Estate Analyzer Code
# By: Owen Smith
# Date: 5/4/2025

# Function to get validated float input from the user
def getFloatInput(prompt):
    while True:
        try:
            user_input = input(prompt)
            value = float(user_input)
            if value <= 0:

             print(end="")
            else:
                return value
        except ValueError:
            print("Input a number that is greater than 0.\n")

# Function to calculate the median of a list
def getMedian(sales_list):
    n = len(sales_list)
    if n == 0:
        return 0.0  # Handle empty list case if needed
    if n % 2 == 1:
        return sales_list[n // 2]  # Middle element for odd count
    else:
        mid1 = sales_list[n // 2 - 1]
        mid2 = sales_list[n // 2]
        return (mid1 + mid2) / 2  # Average of two middle elements for even count

# Main function to run the sales analyzer
def main():
    sales = []

    # Input loop for user to enter sales prices
    while True:
        price = getFloatInput("Enter property sales value: ")
        sales.append(price)

        while True:
            more_input = input("Enter another value Y or N: ").strip().lower()
            if more_input in ('y', 'n'):
                break
            else:
                print(end="")

        if more_input == 'n':
            break

    # Sort the list for proper median and display
    sales.sort()

    # Display sorted sales list with Property #
    for index, value in enumerate(sales, start=1):
        print(f"Property {index} $  {value:,.2f}")

    # Calculate required statistics
    min_sale = min(sales)
    max_sale = max(sales)
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    median_sale = getMedian(sales)
    commission = total_sales * 0.03

    # Display analytics
    print(f"Minimum:    ${min_sale:13,.2f}")
    print(f"Maximum:    ${max_sale:13,.2f}")
    print(f"Total:      ${total_sales:13,.2f}")
    print(f"Average:    ${average_sales:13,.2f}")
    print(f"Median:     ${median_sale:13,.2f}")
    print(f"Commission: ${commission:12,.2f}")

# Run the program
if __name__ == "__main__":
    main()
