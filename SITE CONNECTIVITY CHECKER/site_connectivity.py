# import urllib
# use urllib.request to get data from the url
# Write a function that takes a url
# Returns a response


import urllib.request as urllib


def main(url):
    print("Checking connectivity .... ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully.")
    print("The response code was: ", response.getcode())
    print()


print("This is Kingsley's site connectivity checker program.")
input_url = input("Enter the url of the site you want to check here: ")

main(input_url)
