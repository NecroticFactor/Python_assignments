import sys
import inflect
from datetime import datetime, date

# A Human Class
class Human:
    def __init__(self, date_of_birth):
        self.date_of_birth = self.date_validation(date_of_birth)

    # Method to validate date
    def date_validation(self, user_input):
        try:
            date_object = datetime.strptime(user_input, "%Y-%m-%d").date()
            return date_object
        except ValueError:
            sys.exit("Invalid Date")

    # Method to caluculate the minutes
    def calculate_minutes(self):
        today = date.today()
        total_days = (today - self.date_of_birth)
        total_minutes = (24 * 60 * total_days.days)
        return total_minutes

    # Method to convert minutes from numbers to words
    def wordify(self, total_minutes):
        w = inflect.engine()
        number_to_words = w.number_to_words(total_minutes, andword='')
        return(str.capitalize(number_to_words + " " + "minutes"))

# Main function
def main():
    date_of_birth = input("Date of birth: ")
    person = Human(date_of_birth)
    total_minutes = person.calculate_minutes()
    in_words = person.wordify(total_minutes)
    print(in_words)

if __name__ == "__main__":
    main()

