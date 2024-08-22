upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number = ["1","2","3","4","5","6","7","8","9","0"]
symbol = ["!","@","#","$","%","^","&","*","(",")"]

def main():
    password = get_password()
    valid = validator(password)
    strength = get_strength(valid)
    print(strength)

# Get user input
def get_password():
    return str(input("Enter your Password: "))

# Validate the password
def validator(password):
    while True:
        if len(password) < 8:
            print("Password must be at least 8 characters")
        elif not any(p in upper for p in password):
            print("Password must contain UPPERCASE")
        elif not any(p in lower for p in password):
            print("Password must contain lowercase")
        elif not any(p in number for p in password):
            print("Password must contain Numbers")
        elif not any(p in symbol for p in password):
            print("Password must contain Symbols")
        else:
            return password

# Assess the strength of the password
def get_strength(password):
    upper_count = sum(1 for p in password if p in upper)
    lower_count = sum(1 for p in password if p in lower)
    number_count = sum(1 for p in password if p in number)
    symbol_count = sum(1 for p in password if p in symbol)
    password_len = len(password)

    if 8 <= password_len < 10 and upper_count >= 1 and lower_count >= 1 and number_count >= 1 and symbol_count >= 1:
        return "WEAK PASSWORD"
    elif 10 <= password_len < 12 and upper_count >= 3 and lower_count >=2 and number_count >= 2 and symbol_count >= 1:
        return "QUITE STRONG PASSWORD"
    elif 12 <= password_len < 16 and upper_count >= 3 and lower_count >= 2 and number_count >= 3 and symbol_count >= 4:
        return "STRONG PASSWORD"
    elif 16 <= password_len < 18 and upper_count >= 4 and lower_count >= 4 and number_count >= 5 and symbol_count >= 6:
        return "HOLY SMOKES PASSWORD"
    elif password_len >= 18 and symbol_count >= 10:
        return "WHAT ARE YOU PROTECTING, MY LORD?"
    else:
        return "PASSWORD EXCEEDED STRONGEST CHARACTER LIMIT,CONSIDER MILITARY ENCRYPTION :/ "

main()
