# Binary search algorithm works by repeatedly splitting a set
# of data into half until the target value is found.

# A function that takes a list and a target parameter.
# Multiple variables: Middle, Start, End, Steps
# Use of recursion or while loop
# Increase the steps each time a spit is done.
# Conditions to track target position.


def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle

        if element < list[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
target = 15

binary_search(my_list, target)
