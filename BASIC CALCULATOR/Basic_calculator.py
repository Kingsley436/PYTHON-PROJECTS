# First define the functions needed: add, sub, mul & div.
# Print options to the user.
# Get user inputs.
# Call the functions.
# While loop to continue the program until the user wants to exit.

def add(a, b):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer))


print('Welcome to Kingsley\'s Calculator.')

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    print()

    choice = input('Input your choice: ')
    print()

    try:

        if choice == 'a' or choice == 'A':
            print('Addition')
            a = int(input('Input the first number: '))
            b = int(input('Input second number: '))
            add(a, b)
            print()

        elif choice == 'b' or choice == 'B':
            print('Subtraction')
            a = int(input('Input the first number: '))
            b = int(input('Input second number: '))
            sub(a, b)
            print()

        elif choice == 'c' or choice == 'C':
            print('Multiplication')
            a = int(input('Input the first number: '))
            b = int(input('Input second number: '))
            mul(a, b)
            print()

        elif choice == 'd' or choice == 'D':
            print('Division')
            a = int(input('Input the first number: '))
            b = int(input('Input second number: '))
            div(a, b)
            print()

        elif choice == 'e' or choice == 'E':
            print('Program ended!')
            quit()
            print()

    except ValueError:
        print("Please enter a number instead.")
        print()
