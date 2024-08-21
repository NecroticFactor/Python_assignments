# Case convert function
def camel_to_snake(camel_case):
    # Initialize an empty string
    snake_case = ""

    for i in camel_case:
        if i.isupper():
            if snake_case:
                snake_case += "_"
            snake_case += i.lower()
        else:
            snake_case += i

    return snake_case

# Get user input
camel_case_input = input("camelCase: ")

# Convert to snake_case
snake_case_final = camel_to_snake(camel_case_input)
print("snake_case:", snake_case_final)
