import sys
import csv
from tabulate import tabulate

menu = []


def main():
    file_name = get_file()
    file_validator(file_name)
    read_file(file_name)
    table = get_table(menu)
    print(table)

# Get file name from CL
def get_file():
    if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
    elif sys.argv[1].endswith(".py"):
        print("Not a valid file format")
        sys.exit(1)
    return sys.argv[1]


# Check if file exists
def file_validator(name):
    try:
        with open(name) as file:
            pass
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

# Read the file
def read_file(name):
    with open(name) as file:
        reader = csv.DictReader(file)
        pizza_type = "Sicilian Pizza" if "sicilian" in name.lower() else "Regular Pizza"
        for row in reader:
            menu.append({
                pizza_type: row[pizza_type],
                "Small": row["Small"],
                "Large": row["Large"]
            })

# Format the table
def get_table(menu):
    return tabulate(menu, headers="keys", tablefmt="grid")

main()
