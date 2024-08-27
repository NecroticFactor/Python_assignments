import emoji


def main():
    user_emoji = get_emoji()
    output = emoji.emojize(user_emoji, language='alias')
    print(f"Output: {output}")

# Get user user prompt
def get_emoji():
    prompt = str(input("Input: "))
    return prompt



main()
