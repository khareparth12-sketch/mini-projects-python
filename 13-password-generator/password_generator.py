import random
import string

def generate_password(min_length, numbers = True, sp_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if sp_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if sp_char:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("How long the password should be? "))
has_number = input("Should the password contain numbers?(y/n) ").lower() == "y"
has_special = input("Should the password contain special charatcers?(y/n) ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(f"Generated Password is: {pwd}")