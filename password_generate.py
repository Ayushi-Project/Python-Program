import random
import string

def generate_password(length, complexity):
    if complexity == "1":  # Easy: Only letters (lowercase)
        characters = string.ascii_lowercase
    elif complexity == "2":  # Medium: Letters (lowercase and uppercase) + digits
        characters = string.ascii_letters + string.digits
    elif complexity == "3":  # Hard: Letters (lowercase and uppercase) + digits + special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity choice. Using medium complexity.")
        characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    complexity = input("Choose complexity level:\n1. Easy\n2. Medium\n3. Hard\nEnter your choice (1/2/3): ")

    password = generate_password(length, complexity)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
