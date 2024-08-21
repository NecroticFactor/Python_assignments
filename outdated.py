calendar = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def main():
    user_date = get_date()
    print(user_date)



def get_date():
    while True:
        date = (input("Date: ")).lower().replace('"',"").strip()
        if "/" in date:
            month,day,year = date.split("/")


        elif "," in date:
            date = date.replace(","," ").strip()
            month,day,year = date.split()
            if month in calendar:
                month = calendar.index(month) + 1
        try:
            if int(month) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue
        except UnboundLocalError:
            continue


    return(f"{year}-{int(month):02d}-{int(day):02d}")






main()
