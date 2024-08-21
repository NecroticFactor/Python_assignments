groceries = {}


# Main function
def main():
    while True:
        try:
            item = get_item()
            store_item(item)
        except EOFError:
            break
    for item, quantity in sorted(groceries.items()):
        print(f"{quantity} {item}")

# Get user's items
def get_item():
    return str(input("")).strip().lower()

# Store the items in a dict and the quantity
def store_item(item):
    item_list = item.upper()

    if item_list in groceries:
        groceries[item_list] += 1
    else:
        groceries[item_list] = 1
main()
