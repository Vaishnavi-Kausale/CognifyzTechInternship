def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return num1 % num2
    else:
        return "Invalid operator"

# Get user inputs for the calculator
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operation = input("Enter the operator (+, -, *, /, %): ")

result = calculator(first_num, second_num, operation)
print("Result:", result)
