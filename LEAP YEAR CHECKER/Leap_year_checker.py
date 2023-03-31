def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year you entered is a leap year.")
            else:
                print("The year you entered is not a leap year.")
        else:
            print("The year you entered is a leap year.")
    else:
        print("The year you entered is not a leap year.")


is_leap_year(2012)
