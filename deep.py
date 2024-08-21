# Ask the question and get response
response = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

# convert responses to a unified output
result = response.strip().lower().replace("-", " ").replace(" ", "")

# Condition to display the answer
if result == "42" or result == "forty two":
    print("yes")
else:
    print("No")

