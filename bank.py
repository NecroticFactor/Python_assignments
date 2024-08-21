# Get greeting
greeting = str(input("Greeting: "))

# format greeting
format_greeting = greeting.lower().strip()

# Check greeting and print reward
if "hello" in format_greeting:
    print("$0")

elif "h" in format_greeting[0]:
    print("$20")

else:
    print("$100")

