# Initialize a list with the initial greeting
greetings = ["Adieu, adieu, to"]

# Initialize an empty list to take in names
friends = []

# Main function
def main():
    while True:
        try:
            name = get_names()
            if name: 
                friends.append(name)
        except EOFError:
            break

    get_list()

# Function that gets the name from the user
def get_names():
    return input("Name: ")

# Function that handles list modification and greeting construction
def get_list():
    if len(friends) == 0:
        final_greeting = ""
    elif len(friends) == 1:
        final_greeting = friends[0]
    elif len(friends) == 2:
        final_greeting = " and ".join(friends)
    else:
        final_greeting = ", ".join(friends[:-1]) + ", and " + friends[-1]

    # Add the greeting to the new_greetings list
    new_greetings = f"{greetings[0]} {final_greeting}"

    # Print the formatted greeting
    print(new_greetings)

main()
