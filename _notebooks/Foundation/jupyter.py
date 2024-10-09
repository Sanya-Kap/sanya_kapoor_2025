# Function to perform basic arithmetic operations
def basic_calculator():
    # Taking input from the user for the first number
    num1 = input("Enter the first number: ")

    # Checking if the input is a float or integer
    if '.' in num1:
        num1 = float(num1)
    else:
        num1 = int(num1)

    # Taking input for the operator (+, -, *, /)
    operator = input("Enter an operator (+, -, *, /): ")

    # Taking input for the second number
    num2 = input("Enter the second number: ")

    if '.' in num2:
        num2 = float(num2)
    else:
        num2 = int(num2)

    # Performing the chosen operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle division by zero
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operator!"

    # Printing the result
    print(f"The result is: {result}")

# Run the calculator function
basic_calculator()
