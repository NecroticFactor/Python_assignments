
# Main function
def main():
    level = get_level()
    fuel_level = convert(level)
    result = gauge(fuel_level)
    print(result)



def get_level():
        return input("Fraction: ").strip()


# Get fuel function
def convert(fraction):
        try:
            (x,y) = fraction.split("/",1)
            x = float(x)
            y = int(y)

            if y == 0:
                 raise ZeroDivisionError("Cannot divide by Zero")

            # Check for invalid values
            if x < 0 or y <= 0 or x > y:
                raise ValueError("Invalid Fraction")

            # Convert to percentage
            percentage = float(x / y)*100
            return round(percentage)

        except ZeroDivisionError:
            raise
        except ValueError:
            raise


# Calculate percentage
def gauge(percentage):
    if  percentage >= 99:
        return "F"
    elif percentage <=1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
