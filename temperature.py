# Main function to run the temperature converter
def main():
    metric = get_temperature_metric()
    temperature = get_temperature_value(metric)
    print(temperature)

# Function to get the temperature unit from the user
def get_temperature_metric():
    while True:
        metric = input("Is the temperature in Celcius or Fahrenheit: ").lower().strip()
        if metric in ["celcius", "fahrenheit"]:
            return metric
        else:
            print("Enter a valid unit")

# Function to get the temperature value and convert based on the unit
def get_temperature_value(metric):
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            if metric == "celcius":
                return convert_to_fahrenheit(temperature)
            elif metric == "fahrenheit":
                return convert_to_celcius(temperature)
        except ValueError:
            print("Enter a valid number")

# Convert Celcius to Fahrenheit
def convert_to_fahrenheit(temp):
    fahrenheit = round((temp * (9/5) + 32), 2)
    return f"{fahrenheit} F"

# Convert Fahrenheit to Celcius
def convert_to_celcius(temp):
    celcius = round(((temp - 32) * 5/9), 2)
    return f"{celcius} C"

main()
