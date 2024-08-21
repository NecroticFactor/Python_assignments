# Main function
def main():
    fuel_level = get_fuel()
    fuel_display(fuel_level)


def fuel_display(f):
    if  f >= 99:
        print("F")
    elif f <=1:
        print("E")
    else:
        print(f"{f}%")




# Get fuel function
def get_fuel():
    while True:
        try:
            sensor = str(input("Fraction: ")).strip()
            (x,y) = sensor.split("/",1)
            x = int(x)
            y = int(y)
            if x < 0 or y <= 0 or x > y:
                raise ValueError

        except ValueError:
            print("Enter a fraction")
        else:
            try:
                percentage = float(x / y)*100

            except ZeroDivisionError:
                print("Error")
            else:
                return round(percentage)






main()
