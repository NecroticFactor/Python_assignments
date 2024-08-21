# Declare total amount due
amountdue = 50

# Amount and Change calculation
def main():
    global amountdue

    while amountdue > 0:
        coin_inserted = get_coins()
        amountdue -= coin_inserted

        # Condition to handle change remaining
        if amountdue <= 0:
            print(f"Change Owed: {abs(amountdue)}")

        else:
            print(f"Amount Due: {amountdue}")


# Get coin function
def get_coins():
   while True:
        coin = int(input("Insert coin: "))
        if coin in [5,10,25]:
            return coin
        else:
            print(f"Amount Due: {amountdue}")


main()
