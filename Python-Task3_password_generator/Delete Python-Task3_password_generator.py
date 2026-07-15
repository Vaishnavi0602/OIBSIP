import random
import string


def get_keyword():
    """Get a valid keyword from the user."""
    while True:
        keyword = input("Enter a keyword (e.g., github, wifi, bank): ").strip()

        if keyword == "":
            print("❌ Keyword cannot be empty.\n")
        elif " " in keyword:
            print("❌ Keyword should not contain spaces.\n")
        else:
            return keyword


def get_length(keyword):
    """Get a valid password length."""
    while True:
        try:
            length = int(input(f"Enter password length (minimum {max(8, len(keyword)+4)}): "))

            minimum = max(8, len(keyword) + 4)

            if length < minimum:
                print(f"❌ Password length must be at least {minimum}.\n")
                continue

            return length

        except ValueError:
            print("❌ Please enter a valid number.\n")


def generate_password(keyword, length):

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*?"

    # Randomly capitalize some letters of the keyword
    keyword_chars = [
        c.upper() if random.choice([True, False]) else c.lower()
        for c in keyword
    ]

    password = keyword_chars.copy()

    all_chars = upper + lower + digits + symbols

    # Ensure at least one digit and one symbol
    password.append(random.choice(digits))
    password.append(random.choice(symbols))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return "".join(password)


def main():

    print("=" * 60)
    print("         SMART RANDOM PASSWORD GENERATOR")
    print("=" * 60)

    while True:

        keyword = get_keyword()

        length = get_length(keyword)

        password = generate_password(keyword, length)

        print("\n" + "=" * 60)
        print("Generated Password:")
        print(password)
        print("=" * 60)

        again = input("\nGenerate another password? (Y/N): ").strip().lower()

        if again != "y":
            print("\nThank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
