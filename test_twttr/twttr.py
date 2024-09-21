# Initialize vowels
vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]

# Get user input
def main():
    tweet = input("Input: ")
    modified_tweet = shorten(tweet)
    if modified_tweet is not False:
        print("Output:", modified_tweet)


# Define converter
def shorten(text):
    if text.isdigit():
        return text
    else:
        text = text.strip()
        for vowel in vowels:
            text = text.replace(vowel, "")
        return text


if __name__ == "__main__":
    main()
