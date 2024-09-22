import csv
import sys


students = []

def main():
    file_r, file_w = get_file()
    file_validator(file_r)
    file_changer(file_r, file_w)

def get_file():
    if len(sys.argv) < 3:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".py") or sys.argv[2].endswith(".py") :
        print("Not a valid file format")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]



def file_validator(name):
    try:
        with open(name) as file:
            pass
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def file_changer(read,write):
    with open(read) as file_r:
        reader = csv.DictReader(file_r)
        for row in reader:
            last_name, first_name = row["name"].split(", ")
            house = row["house"]
            students.append({"first": first_name, "last": last_name, "house": house})


    # Open the output file in write mode and write header
    with open(write, "w", newline="") as file_w:
        writer = csv.DictWriter(file_w, fieldnames=["first", "last", "house"])
        writer.writeheader()  # Write the header row
        for student in students:
            writer.writerow(student)  # Write each student row


if __name__ == "__main__":
    main()





