import random
import sys

def main():
    level = get_level()
    random_number = randomise(level)
    while True:
        number = get_number()
        result = checker(random_number, number)
        print(result)
        if result == "Just right!":
            sys.exit()

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Level must be greater than 0")
        except ValueError:
            print("Please enter a positive integer")

def get_number():
    while True:
        try:
            number = int(input("Guess: "))
            if number > 0:
                return number
            else:
                print("Guess must be greater than 0")
        except ValueError:
            print("Please enter a positive integer")

def randomise(range_value):
    return random.randint(1, range_value)

def checker(comp, user):
    if user > comp:
        return "Too large!"
    elif user < comp:
        return "Too small!"
    else:
        return "Just right!"

main()
