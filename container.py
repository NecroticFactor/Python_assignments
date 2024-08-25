container = [
    {"name": "20ft", "volume": 38510848},
    {"name": "40ft", "volume": 76960896},
    {"name": "40ftHC", "volume": 43039536}
]

currency_info = [
    {
        "name": "INR",
        "denomination": [
            {"value": "10", "volume_cm3": 0.775},
            {"value": "20", "volume_cm3": 0.81},
            {"value": "50", "volume_cm3": 0.89},
            {"value": "100", "volume_cm3": 0.93},
            {"value": "500", "volume_cm3": 0.945},
            {"value": "2000", "volume_cm3": 1.10}
        ]
    }
]

user_choice_denomination = ""

def main():
    container_volume = get_container()
    currency = get_currency()
    unit = get_unit()
    denomination_volume = get_denomination(currency)
    quantity = get_quantity(container_volume, denomination_volume)
    total_value = do_calculator(quantity, denomination_volume)
    format_value = format_indian_number(total_value)
    print(f"The Value in your container is: {format_value} {unit}")

# Get choice of container from user and return it's volume from the dict
def get_container():
    while True:
        container_size = [c["name"] for c in container]
        choice = str(input(f"Which container would you like to use:\n{'\n'.join(container_size)}\nYour choice: ")).strip().lower().replace(" ","")
        for c in container:
            if c["name"] == choice:
                return int(c["volume"])
        print("Enter Valid Container Detail")


# Get choice of currency from user 
def get_currency():
    while True:
        currency_name = [n["name"] for n in currency_info]
        cur = str(input(f"Which currency would you like to ship?\n{'\n'.join(currency_name)}\nYour choice: ")).strip().replace(" ","")
        for n in currency_info:
            if n["name"] == cur:
                return n  # Return the entire currency dictionary
        print("Enter Valid Currency (Only INR Available at the moment)")


# Get choice of denomination based on currency and return it's volume from the dict
def get_denomination(currency):
    denomination = currency["denomination"]
    values = [denom["value"] for denom in denomination]
    while True:
        choice = str(input(f"Which Denomination:\n{'\n'.join(values)}\nYour choice: ")).strip().replace(" ","")
        global user_choice_denomination
        user_choice_denomination = int(choice)
        for denom in denomination:
            if denom["value"] == choice:
                return denom["volume_cm3"]
        print("Enter a Valid Denomination")


# Find the quantity if the denomnation in the whole container
def get_quantity(Volume1, Volume2):
    if Volume2 == 0:
        raise ValueError("Denomination volume cannot be zero.")
    return round((Volume1 / Volume2))


# Now find the total value
def do_calculator(quantity, denomination):
    return quantity * user_choice_denomination


# This is the indian numbering system
def format_indian_number(number):
    if number < 0:
        return "Negative numbers are not supported"

    units = [
        ("Crore", 10000000),
        ("Lakh", 100000),
        ("Thousand", 1000),
        ("Hundred", 100)
    ]

    result = []

    for unit, value in units:
        if number >= value:
            count = number // value
            number %= value
            result.append(f"{count} {unit}")

    if number > 0:
        result.append(f"{number} Only")

    formatted_number = ', '.join(result)

    return formatted_number

def get_unit():
    currency = "INR"
    if currency == "INR":
        return "Rupees"
    else:
        return None

main()
