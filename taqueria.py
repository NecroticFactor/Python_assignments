menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0

def main():
    while True:
        try:
            item = get_item()
        except EOFError:
            print()
            break

        item_price = get_price(item)
        if item_price:
            total_cost(item_price)
            print(f"Total: ${total:.2f}")
        pass
    print(f"Total: ${total:.2f}")



def get_item():

    prompt = str(input("Item:")).strip().lower()
    return prompt


def get_price(name):
    return menu.get(name)

def total_cost(price):
    global total
    total += price


main()
