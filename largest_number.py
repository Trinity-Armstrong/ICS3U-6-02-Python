#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: December 2019
# This program identifies the largest of 10 random numbers


import random


def identify(array_of_numbers):
    # This function identifies the largest number in a list
    largest_number = 0

    # Process
    for counter in range(0, len(array_of_numbers)):
        if largest_number < array_of_numbers[counter]:
            largest_number = array_of_numbers[counter]

    # Output
    return largest_number


def main():
    # This function generates 10 random numbers and prints the largest

    # Array declaration
    random_numbers = []

    # Process
    for loop_counter in range(0, 10):
        number = random.randint(1, 100)
        random_numbers.append(number)
    print(random_numbers)

    # Call function
    largest = identify(random_numbers)

    # Output
    print("")
    print("The largest number in this list is", largest)


if __name__ == "__main__":
    main()
