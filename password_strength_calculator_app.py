import math
import string #vs manually entering all the strings manually (26,10,32) using a module instead

def main():
    print("Welcome to the passheff a entropy/strength calculator")

    password = input("what is your password?\n")
    length = len(password)

    character_sets = {
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "numbers": string.digits,
        "punctuation": string.punctuation
    }

    character_set_size = 0
    used_sets = set()

    for character in password:
        for name, charset in character_sets.items():
            if character in charset:
                used_sets.add(name)

    for charset_name in used_sets:
        if charset_name == "lower" or charset_name == "upper":
            character_set_size += 26
        elif charset_name == "numbers":
            character_set_size += 10
        elif charset_name == "punctuation":
            character_set_size += 32

    password_entropy = length * math.log2(character_set_size)

    cracking_time_years = pow(character_set_size, length) / (2 * (1e9)) / (86400 * 365.25)

    print(f"Your password has an entropy of {password_entropy:.2f} bits.")
    print(f"It would take approximately {cracking_time_years:.6f} years to crack your password at 1 billion guesses per second.")

if __name__ == "__main__":
    main()
