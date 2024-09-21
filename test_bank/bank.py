def main():
    greeting = get_greeting()
    result = value(greeting)
    print(result)


def get_greeting():
    greeting = str(input("Greeting: "))
    format_greeting = greeting.strip()
    return format_greeting

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
