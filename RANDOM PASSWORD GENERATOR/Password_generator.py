# Ask a user if they want to generate a password or not.
# If yes, ask for the password length
# Generate the password
# Print password
# If initial response is no, exit program.


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$^&*()")


def generate_password():
    password_length = int(
        input("How long would you like your password to be?  "))
    print()

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/No): ")
print()

if option.upper() == "Yes".upper():
    generate_password()
    print()
elif option.upper() == "No".upper():
    print("Program Ended!")
    print()
else:
    print("Invalid input, please input Yes or No.")
    quit()
    print()
