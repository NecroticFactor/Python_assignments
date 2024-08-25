operations = ["multiplication table", "factorial", "fibonacci sequence", "sum of digits"]

# Main function that does everything here
def main():
    prompt = get_prompt()
    validator(prompt)

# Get user request
def get_prompt():
    while True:
        prompt = input(f"Enter operation ({', '.join(operations)}): ").lower().strip()
        if prompt in operations:
            return prompt
        print("Enter a valid operation")

# Validate the Operation
def validator(prompt):
    if prompt == "multiplication table":
        multiplication_table()
    elif prompt == "factorial":
        factorial()
    elif prompt == "fibonacci sequence":
        fibonacci_sequence()
    elif prompt == "sum of digits":
        sum_of_digits()

# Multiplication table
def multiplication_table():
    while True:
        try:
            number = int(input("Enter the number you would like to multiply: "))
            limit = int(input("Enter the upper bound up to which you would like to multiply: "))
            if limit < 1:
                print("The upper bound must be at least 1.")
                continue
            for i in range(1, limit + 1):
                print(f"{number} x {i} = {number * i}")
            break
        except ValueError:
            print("Enter a valid number")

# Factorial
def factorial():
    while True:
        try:
            number = int(input("Enter the number you would like to find the factorial for: "))
            if number < 0:
                print("Factorial is not defined for negative numbers.")
                continue
            result = 1
            for i in range(1, number + 1):
                result *= i
            print(f"The factorial of {number} is {result}")
            break
        except ValueError:
            print("Enter a valid number")

# Fibonacci sequence
def fibonacci_sequence():
    while True:
        try:
            limit = int(input("Enter the maximum sequence length you would like to generate: "))
            if limit < 1:
                print("The sequence length must be at least 1.")
                continue
            a, b = 0, 1
            fibonacci = []
            while len(fibonacci) < limit:
                fibonacci.append(a)
                a, b = b, a + b
            print(fibonacci)
            break
        except ValueError:
            print("Enter a valid number")

# Calculate sum of digits
def sum_of_digits():
    while True:
        number = input("Enter a number: ")
        if len(number) < 2 or not number.isdigit():
            print("Enter two or more digits.")
            continue
        total = sum(int(digit) for digit in number)
        print(f"Sum of digits: {total}")
        break

main()
