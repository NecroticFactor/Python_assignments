punctuations = ["."," ","!", ","]


# Get plate choice
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Check if plate is valid
def is_valid(s):

    # Split the plate based on the presence of digit
    text = ""
    number = ""

    for i, char in enumerate(s):
        if char.isdigit():
            text = s[:i]
            number = s[i:]
            break

    # Check if first digit is not zero
    if number and number[0] == "0":
        return False

    # Check minmax of plate
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if none of the char in plates has punctuations
    for char in s:
        if char in punctuations:
            return False

    # Check if Index[0] and [1] are str
    if len(s) > 1 and (not s[0].isalpha() or not s[1].isalpha()):
        return False

    # Check if the order is right
    contains_digit = False
    for char in s:
        if char.isdigit():
            contains_digit = True
        elif contains_digit and char.isalpha():
            return False

    return True






main()
