students = [
    {
        "name": "Alice",
        "age": 16,
        "subjects": [
            {
                "subject": "Math",
                "grades": {
                    "midterm": 85,
                    "final": 90
                }
            },
            {
                "subject": "Science",
                "grades": {
                    "midterm": 88,
                    "final": 92
                }
            }
        ]
    },
    {
        "name": "Bob",
        "age": 17,
        "subjects": [
            {
                "subject": "Math",
                "grades": {
                    "midterm": 78,
                    "final": 84
                }
            },
            {
                "subject": "Science",
                "grades": {
                    "midterm": 82,
                    "final": 89
                }
            }
        ]
    }
]

def main():
    print("")
    get_table()
    print("")
    get_name_age_grades()

def get_name_age_grades():

    # Get students name and age from dict
    for student in students:
        name = student["name"]
        age = student["age"]
        print(f"\033[1mThe student {name} is aged {age}.\033[0m")

        # Print empty line after the Student's detail
        print("")

    # Get subject and grades from dict
        for subject in student["subjects"]:
                grade_midterm = subject["grades"]["midterm"]
                grade_final = subject["grades"]["final"]
                sub = subject["subject"]
                print(f"Scores for the Subject: \033[1m{sub}\033[0m")
                print(f"Midterm: {grade_midterm} and Final: {grade_final}" )

                # Print empty line after each subject
                print("")

    # Print empty line after the grades
        print("")

def get_table():
    print("")
    print("+-----------+--------+-------------+---------+---------+")
    print("| Name      | Age    |   Subject   | Midterm | Final   |")
    print("+-----------+--------+-------------+---------+---------+")

    for student in students:
        name = student["name"]
        age = student["age"]

        for subject in student["subjects"]:
            subject_name = subject["subject"]
            midterm_grade = subject["grades"]["midterm"]
            final_grade = subject["grades"]["final"]

            # Print the subject grades in table format
            print(f"| {name:<9} | {age:<6} | {subject_name:<11} | {midterm_grade:^7} | {final_grade:^7} |")

            # Print a separator line after each entry
            print("+-----------+---------+----------+---------+-----------+")

main()

