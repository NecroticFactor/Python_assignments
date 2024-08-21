import math

# Main function that does everything
def main():
    shape = get_shape()
    calculation = get_calculation(shape)
    value = calculator(shape, calculation)
    if calculation in ["area"]:
        print(f"{value} cm²")
    elif calculation in ["circumference", "perimeter"]:
        print(f"{value} cm")

# Gets the desired shape
def get_shape():
    while True:
        shape = str(input("Enter the shape among 'Square, Rectangle, Circle': ")).lower().strip()
        if shape in ["square", "rectangle", "circle"]:
            return shape
        else:
            print("Enter a valid shape")

# Gets the desired calculation needed
def get_calculation(shape):
    while True:
        if shape in ["square", "rectangle"]:
            requirement = str(input("Area or Perimeter: ")).lower().strip()
            if requirement in ["area", "perimeter"]:
                return requirement
            else:
                print("Enter a valid requirement")
        elif shape == "circle":
            requirement = str(input("Area or Circumference: ")).lower().strip()
            if requirement in ["area", "circumference"]:
                return requirement
            else:
                print("Enter a valid requirement")

# Does the calculations
def calculator(shape, requirement):
    try:
        if shape == "circle":
            radius = float(input("Enter the radius in cm: "))
            if requirement == "circumference":
                return circumference_circle(radius)
            else:
                return area_circle(radius)

        elif shape == "rectangle":
            length = float(input("Enter the length in cm: "))
            width = float(input("Enter the width in cm: "))
            if requirement == "perimeter":
                return perimeter_rectangle(length, width)
            else:
                return area_rectangle(length, width)

        elif shape == "square":
            side = float(input("Enter the side in cm: "))
            if requirement == "perimeter":
                return perimeter_square(side)
            else:
                return area_square(side)
    except ValueError:
        print("Enter a valid number")

# Circle circumference function
def circumference_circle(radius):
    return round((2 * math.pi * radius), 2)

# Circle area function
def area_circle(radius):
    return round((math.pi * radius ** 2), 2)

# Rectangle perimeter function
def perimeter_rectangle(length, width):
    return round((2 * (length + width)), 2)

# Rectangle area function
def area_rectangle(length, width):
    return round((length * width), 2)

# Square perimeter function
def perimeter_square(side):
    return round((4 * side), 2)

# Square area function
def area_square(side):
    return round((side ** 2), 2)

main()
