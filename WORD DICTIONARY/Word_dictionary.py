# First create a python dictionary that has a key/value pair that represents a word and its definition.
# Then collect input from the user, input is a word
# Check if the word is in the dictionary
# Print the definition.


from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break

    print(dictionary.meaning(word))


# MULTIPLE WORD SEARCH
# dictionary = PyDictionary("person", "reflex", "incubator")

# print(dictionary.getMeanings())
