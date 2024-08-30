import requests
import sys

bitcoin = []

def main():
    quantity = get_coin()
    value = get_value(quantity)
    print(value)


def get_coin():
    try:
        quantity = float(sys.argv[1])
        if len(sys.argv) < 2:
            print("Missing CL Argument")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too Many Arguments")
            sys.exit(1)
        else:
            return quantity

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)




def get_value(coin):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin = response.json()
        rate = (bitcoin["bpi"]["USD"]["rate"]).replace(",","")

        return (f'$''{:,}'.format(round(float(rate) * float(coin), 4)))

    except requests.RequestException:
        print("Error")
    except TypeError:
        sys.exit(1)


if __name__ == "__main__":
    main()
