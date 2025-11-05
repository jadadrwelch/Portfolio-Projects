# Simple Python Calculator

# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for an operation
print("Choose an operation: +, -, *, /")
operation = input("Enter your choice: ")

# Perform the operation using if/elif/else
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Prevent division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operation.")
    result = None

# Show the result
if result is not None:
    print("Result:", result)
