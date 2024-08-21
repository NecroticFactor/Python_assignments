fruits = [
    {"name":"apple", "calories":"130"},
    {"name":"avocado", "calories":"50"},
    {"name":"banana", "calories":"110"},
    {"name":"cantaloupe", "calories":"50"},
    {"name":"grapefruit", "calories":"60"},
    {"name":"grapes", "calories":"90"},
    {"name":"honeydew melon", "calories":"50"},
    {"name":"kiwifruit", "calories":"90"},
    {"name":"lemon", "calories":"15"},
    {"name":"lime", "calories":"20"},
    {"name":"nectrine", "calories":"60"},
    {"name":"orange", "calories":"80"},
    {"name":"sweet cherries", "calories":"100"},
    {"name":"pear", "calories":"100"},
    {"name":"watermelon", "calories":"80"}

]

# Function to get user request
def main():
   user_request =str(input("Item: ")).strip().lower()
   facts = get_fruit(user_request)

   if facts:
        print("Calories:", facts)
   else:
        print("")


# Function that reads through the dict
def get_fruit(f):
    for fruit in fruits:
        if fruit["name"] == f:
            return fruit["calories"]

    return None

main()
