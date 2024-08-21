# Convert user emoticons to emoji
def convert(response):
    response = response.replace(":)", "🙂")
    response = response.replace(":(", "🙁")

    return response

# Get user's feeling
def main():
    user_feeling = str(input())
    converted_feeling = convert(user_feeling)
    print(converted_feeling)


# Output the result
main()

