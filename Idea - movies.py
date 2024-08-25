movies = [
    {
        "title": "Inception",
        "year": 2010,
        "actors": [
            {"name": "Leonardo DiCaprio", "age": 46},
            {"name": "Joseph Gordon-Levitt", "age": 43},
            {"name": "Elliot Page", "age": 37}
        ]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "actors": [
            {"name": "Keanu Reeves", "age": 59},
            {"name": "Carrie-Anne Moss", "age": 56},
            {"name": "Laurence Fishburne", "age": 63}
        ]
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "actors": [
            {"name": "Marlon Brando", "age": 80},
            {"name": "Al Pacino", "age": 84},
            {"name": "James Caan", "age": 83}
        ]
    }
]

def main():
    get_movie_and_actors()
    get_table()

def get_movie_and_actors():
    for movie in movies:
        title = movie["title"]
        year = movie["year"]
        print(f"\033[1mThe movie {title} relesed in the year {year}.\033[0m")


        for actor in movie["actors"]:
            name = actor["name"]
            age = actor["age"]
            print(f"It's actor {name} is aged {age}.")
        print("")

def get_table():
    print("+----------------+------+----------------------+-----+")
    print("|     Title      | Year |        Actor         | Age |")
    print("+----------------+------+----------------------+-----+")

    for movie in movies:
        title = movie["title"]
        year = movie["year"]
        actors = movie["actors"]

        # Print the first row with the title, year, and the first actor's details
        first_actors = actors[0]
        print(f"| {title:<14} | {year:<4} | {first_actors['name']:<20} | {first_actors['age']:<3} |")

        # Print remaining
        for actor in actors[1:]:
            print(f"| {' ':<14} | {' ':<4} | {actor['name']:<20} | {actor['age']:<3} |")

        # Add a separator after each movie
        print("+----------------+------+----------------------+-----+")




main()
