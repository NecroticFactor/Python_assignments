def main():
    # Get user input and convert it
    user_time = str(input("What time is it? ")).lower().strip()
    
    # Remove AM/PM and convert to 24-hour format
    if "a.m." in user_time:
        user_time = user_time.replace("a.m.", "").strip()
    elif "p.m." in user_time:
        user_time = user_time.replace("p.m.", "").strip()
        hour, minutes = user_time.split(":", 1)
        hour = float(hour)
        if hour != 12:
            hour += 12
        user_time = f"{hour}:{minutes}"
    formatted_time = convert(user_time)

    # Determine meal based on the time
    if 7.00 <= formatted_time <= 8.00:
        meal = "Breakfast time"
    elif 12.00 <= formatted_time <= 13.00:
        meal = "Lunch time"
    elif 18.00 <= formatted_time <= 19.00:
        meal = "Dinner time"
    else:
        meal = "Not the time to eat"

    print(meal)




def convert(time):
    # Split time into hour and minutes
    hour, minutes = time.split(":", 1)

    # Convert hour and minutes to float
    hour = float(hour)
    minutes = float(minutes) / 60

    # Calculate the decimal time
    result = hour + minutes
    return result



if __name__ == "__main__":
    main()



