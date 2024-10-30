import sys
from PIL import Image, ImageOps

# Allowed image extensions
ALLOWED_FORMATS = (".jpg", ".jpeg", ".png")

def main():
    input_file, output_file = get_image()
    validator(input_file)
    do_edit(input_file, output_file)

# Get file names and check for conditions
def get_image():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if both input and output files have valid formats
    if not (input_file.lower().endswith(ALLOWED_FORMATS) and output_file.lower().endswith(ALLOWED_FORMATS)):
        print("Not a valid file format")
        sys.exit(1)

    # Ensure the input and output have the same extension
    if input_file.split('.')[-1].lower() != output_file.split('.')[-1].lower():
        print("Input and output have different extensions")
        sys.exit(1)

    # Ensure output file is valid
    if not output_file.lower().endswith(ALLOWED_FORMATS):
        print("Invalid output")
        sys.exit(1)

    return input_file, output_file

# Check if files exist
def validator(file):
    try:
        with Image.open(file) as img:
            img.verify()
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
    except (IOError, SyntaxError) as e:
        print("Invalid image file:", e)
        sys.exit(1)

def do_edit(input_file, output_file):
    # Load the input image
    input_image = Image.open(input_file)

    # Load the shirt image and resize it to match the input image size
    shirt_image = Image.open("shirt.png").convert("RGBA")
    input_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt on the input image
    input_image.paste(shirt_image, (0,0), shirt_image)

    # Save the result
    input_image.save(output_file)

if __name__ == "__main__":
    main()
