# Initialize vowels
vowels = ["a","e","i","o","u", "A", "E","I","O","U"]


# Get user input
def main():
    tweet = str(input("Input: ")).strip()
    modified_tweet = converter(tweet, vowels)
    print("Output:",modified_tweet)



# Define converter
def converter(text, vowels):
    for vowel in vowels:
         text = text.replace(vowel, "")
    return text

main()


