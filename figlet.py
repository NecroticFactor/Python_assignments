import pyfiglet
import sys
from pyfiglet import FigletFont

def main():
    plain_text = get_text()

    # Check if a font argument is provided
    if len(sys.argv) == 3:
        # Generate ASCII art with the specified font
        ascii_art = pyfiglet.figlet_format(plain_text, font=sys.argv[2])
    else:
        # Generate ASCII art with the default font
        ascii_art = pyfiglet.figlet_format(plain_text)

    print(ascii_art)

# Get plain text from user
def get_text():
    # If the user provides an argument, check if it’s valid
    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            sys.exit("Invalid usage")

        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in FigletFont.getFonts():
            sys.exit("Invalid usage")

    # Prompt for user input
    text = input("Input: ")
    return text

main()
