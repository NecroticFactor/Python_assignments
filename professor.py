import random

levels = ["1", "2", "3"]
score = 0
max_attempts = 3

def main():
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        if not handle_question(x, y, correct_answer):
            print(f"{x} + {y} = {correct_answer}")
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in levels:
            return level


def generate_integer(level):
    level = int(level)
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

def handle_question(x, y, correct_answer):
    attempts = 0
    while attempts < max_attempts:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if do_compare(user_answer, correct_answer):
                global score
                score += 1
                return True
            else:
                print("EEE")
                attempts += 1

        except ValueError:
            attempts += 1

    return False

def do_compare(user_answer, correct_answer):
    return user_answer == correct_answer

if __name__ == "__main__":
    main()
