# Difine the arthmetic operator
operators = "+","-","/","*"

# Get user input for X Y Z
expression = str(input("Expression: "))


# Split X and Z from expression
x,y,z = expression.split()

x = float(x)
z = float(z)

#Operation logic
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "/":
    if z == 0:
        result = "Undefined"
    else:
        result = x / z
elif y == "*":
    result = x * z
else:
    print("Undefined result")

print(result)




