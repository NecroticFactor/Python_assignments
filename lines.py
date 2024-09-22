import sys

# Get file name from CL
def main():
    file_name = get_file()
    file_validator(file_name)
    print(read_file(file_name))


def get_file():
    if len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
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

# Read file function
def read_file(name):
    line_count = 0

    # Open the file
    with open(name) as file:
        # Read the lines
        for line in file:
            stripped_line = line.strip()

            # Skip if the line is empty
            if len(stripped_line) == 0:
                continue

            # Check if line starts with symbols
            if not (stripped_line.startswith("#") or stripped_line.startswith("/")):
                # # Increment count if the line is not a comment
                line_count += 1

    # Return the line count
    return line_count


if __name__ == "__main__":
    main()

