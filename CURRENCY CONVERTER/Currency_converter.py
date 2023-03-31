def main():
    print("")
    print("Welcome to Kingsley's Currency Converter.")
    print("This program converts US Dollars to Pounds Sterling.")
    print("")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = convert_to_pounds(dollars)

    print("That is", pounds, "pounds.")
    print("")


def convert_to_pounds(dollars): return dollars * 0.82


main()
