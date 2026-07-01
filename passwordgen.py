import random
import string

# Custom password generator
def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Strong password generator (guaranteed complexity)
def strong_password(length):
    if length < 4:
        return "Password length should be at least 4"

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)

    return ''.join(password)


# Main program
print("1. Custom Password")
print("2. Strong Password")

choice = input("Choose option (1/2): ")

length = int(input("Enter password length: "))

if choice == "1":
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"
    
    password = generate_password(length, use_digits, use_special)
    print("Generated Password:", password)

elif choice == "2":
    password = strong_password(length)
    print("Strong Password:", password)

else:
    print("Invalid choice")
