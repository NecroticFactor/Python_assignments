import re
import sys

def main():
    print(count(input("Text: ")))
    sys.exit(1)


def count(s):
    # Pattern to match "um" as a whole word (optionally followed by punctuation or spaces)
    pattern = r"\bum\b"

    # Find all occurrences of "um" in the input string
    um_occurrences = re.findall(pattern, s, re.IGNORECASE)

    if um_occurrences:
        # Return the number of occurrences
        return len(um_occurrences)



if __name__ == "__main__":
    main()
