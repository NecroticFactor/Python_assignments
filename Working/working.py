import re
import sys


def main():
    user_time = input("Hours: ").lower()
    print(validate(user_time))


# Checks user Input
def validate(user_time):
    # Combined pattern for validating time ranges
    pattern = r"^(?P<starttime>(12 (am|pm)|[1-9](?::[0-5][0-9])? (am|pm)|1[0-2](?::[0-5][0-9])? (am|pm))) to (?P<endtime>(12 (am|pm)|[1-9](?::[0-5][0-9])? (am|pm)|1[0-2](?::[0-5][0-9])? (am|pm)))$"

    # Match the user input against the pattern
    if match := re.match(pattern, user_time):
        start_time = match.group("starttime")
        end_time = match.group("endtime")
        cvrt_start_time = converter(start_time)
        cvrt_end_time = converter(end_time)
        formatted_time = formatter(cvrt_start_time, cvrt_end_time)
        return formatted_time
    else:
        raise ValueError

# Converts into 24hr
def converter(time):
    # Unpack time and AM/PM
    time_of_day, time_indicator = time.split(" ",1)

    # Check if time has minutes
    if ":" in time:
        hour, minute = map(int, time_of_day.split(":"))
    else:
        hour = int(time_of_day)
        minute = 0

    # Check AM or PM and calculate based on it
    if time_indicator == "pm" and hour != 12:
        hour += 12
    elif time_indicator == "am" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

# Concats Start and End Time
def formatter(s_time,e_time):
    return f"{s_time} to {e_time}"


if __name__ == "__main__":
    main()

