# First collect email from the user.
# Split the email using the @ symbol.
# First part is saved as the username and the second part as the domain.
# Then split the domain into using the dot (.)

def main():
    print("Welcome to Kingsley's Email Slicer.")
    print("")

    email_input = input("Enter your email address here: ")
    print("")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)
    print("")


while True:
    main()
    print("")
